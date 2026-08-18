#!/usr/bin/env python3
"""Import EMLG/JMLG abstract DOCX files into jekyll-theme-conference talk pages.

The programme/talk files remain authoritative for talk title, speaker and track.
This importer reads abstract submissions and enriches the matching `_talks/*.md`
file with authors, affiliations, contact e-mail, abstract body, acknowledgements,
references and embedded figures.

Typical use:
    python tools/import_abstracts.py source_abstracts/*.docx \
        --talks-dir _talks --assets-dir assets/abstracts

Run with --dry-run first.  The script prints MATCHED / AMBIGUOUS / UNMATCHED
status and never creates a new talk page unless --allow-create is supplied.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import re
import shutil
import sys
import unicodedata
from dataclasses import dataclass, field
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, Iterable
from zipfile import ZipFile

import yaml
from docx import Document
from lxml import etree


TITLE_OVERRIDES = {
    "Takamuku1.docx": (
        "LCST-type Phase Separation of "
        "Phosphonium-based Ionic Liquid-Water Mixed Solutions"
    ),
    "RuizBarragan1.docx": (
        "Water self-dissociation in slit pores "
        "displays non-monotonic behavior as a function of water filling"
    ),
}

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
V_NS = "urn:schemas-microsoft-com:vml"
REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"


def normalize_ws(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("\xa0", " ")).strip()


def normalize_title(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = text.casefold()
    text = text.replace("–", "-").replace("—", "-").replace("β", "beta")
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return normalize_ws(text)


def slugify(text: str, max_len: int = 72) -> str:
    norm = normalize_title(text).replace(" ", "-")
    return norm[:max_len].strip("-") or "abstract"


def strip_superscript_digits_from_paragraph(paragraph) -> str:
    parts: list[str] = []
    for run in paragraph.runs:
        if run.font.superscript and re.fullmatch(r"[\d,\-–]+", run.text.strip()):
            continue
        parts.append(run.text)
    return normalize_ws("".join(parts))


def paragraph_with_sup_html(paragraph) -> str:
    parts: list[str] = []
    for run in paragraph.runs:
        text = html.escape(run.text)
        if run.font.superscript and run.text.strip():
            parts.append(f"<sup>{text}</sup>")
        else:
            parts.append(text)
    return normalize_ws("".join(parts))


def leading_superscript_label(paragraph) -> str | None:
    for run in paragraph.runs:
        if not run.text.strip():
            continue
        if run.font.superscript and re.fullmatch(r"\d+", run.text.strip()):
            return run.text.strip()
        break
    m = re.match(r"^(\d+)\s*(?=[A-Z])", paragraph.text.strip())
    return m.group(1) if m else None


def paragraph_text_without_leading_superscript(paragraph) -> str:
    skipped = False
    pieces: list[str] = []
    for run in paragraph.runs:
        if not skipped and run.font.superscript and re.fullmatch(r"\d+", run.text.strip()):
            skipped = True
            continue
        pieces.append(run.text)
    text = normalize_ws("".join(pieces))
    if not skipped:
        text = re.sub(r"^\d+\s*(?=[A-Z])", "", text)
    return normalize_ws(text)


def split_authors(author_paragraphs: list[Any]) -> tuple[list[str], str]:
    plain_parts = [strip_superscript_digits_from_paragraph(p) for p in author_paragraphs]
    plain = normalize_ws(" ".join(plain_parts))
    # Names are comma-delimited in the supplied EMLG examples.  A final name can
    # follow a comma-less line break, so normalize those paragraphs first.
    authors = [normalize_ws(x) for x in re.split(r",\s*", plain) if normalize_ws(x)]

    html_parts = [paragraph_with_sup_html(p) for p in author_paragraphs]
    author_html = normalize_ws(" ".join(html_parts))
    return authors, author_html


def extract_email(text: str) -> str | None:
    m = re.search(r"[A-Z0-9._%+\-]+@[A-Z0-9.\-]+\.[A-Z]{2,}", text, re.I)
    return m.group(0) if m else None


def image_relationships(docx_path: Path) -> tuple[dict[str, str], dict[str, bytes]]:
    with ZipFile(docx_path) as zf:
        rels = etree.fromstring(zf.read("word/_rels/document.xml.rels"))
        rel_map: dict[str, str] = {}
        for rel in rels.xpath(".//r:Relationship", namespaces={"r": REL_NS}):
            if "image" in rel.get("Type", ""):
                rel_map[rel.get("Id")] = rel.get("Target")
        media: dict[str, bytes] = {}
        for rid, target in rel_map.items():
            path = "word/" + target.lstrip("/")
            try:
                media[rid] = zf.read(path)
            except KeyError:
                pass
    return rel_map, media


def paragraph_image_ids(paragraph) -> list[str]:
    root = etree.fromstring(paragraph._p.xml.encode("utf-8"))
    ns = {"a": A_NS, "r": R_NS, "v": V_NS}
    ids = root.xpath(".//a:blip/@r:embed | .//v:imagedata/@r:id", namespaces=ns)
    return list(dict.fromkeys(ids))


def paragraph_caption(paragraph) -> str | None:
    root = etree.fromstring(paragraph._p.xml.encode("utf-8"))
    texts = root.xpath(".//w:txbxContent//w:t/text()", namespaces={"w": W_NS})
    if not texts:
        return None
    # Office may store both DrawingML and VML fallback copies of the same caption.
    joined = normalize_ws("".join(texts))
    if len(joined) % 2 == 0 and joined[: len(joined)//2] == joined[len(joined)//2 :]:
        joined = joined[: len(joined)//2]
    # More robust repeated-sentence fallback.
    m = re.match(r"^(.+?)(?:\s+\1)$", joined)
    if m:
        joined = m.group(1)
    # Example files duplicate 'Fig. 1...' exactly in fallback shapes.
    half = len(joined) // 2
    if half and normalize_ws(joined[:half]) == normalize_ws(joined[half:]):
        joined = normalize_ws(joined[:half])
    return joined or None


@dataclass
class Figure:
    data: bytes
    extension: str
    caption: str | None = None
    digest: str = ""


@dataclass
class ParsedAbstract:
    source: Path
    title: str
    authors: list[str]
    author_html: str
    affiliations: list[str]
    email: str | None
    abstract_blocks: list[tuple[str, Any]] = field(default_factory=list)  # ('text', str) / ('figure', Figure)
    acknowledgements: list[str] = field(default_factory=list)
    references: list[str] = field(default_factory=list)


def parse_docx(path: Path) -> ParsedAbstract:
    doc = Document(path)
    paras = doc.paragraphs
    nonempty = [i for i, p in enumerate(paras) if normalize_ws(p.text)]
    if not nonempty:
        raise ValueError("document contains no text paragraphs")

    title_i = nonempty[0]
    title = normalize_ws(paras[title_i].text)

    email_i = None
    for i in nonempty:
        if i > title_i and re.search(r"\be-?mail\b|@", paras[i].text, re.I):
            if extract_email(paras[i].text):
                email_i = i
                break
    if email_i is None:
        raise ValueError("could not locate contact e-mail; cannot reliably separate metadata from abstract")

    # Find first affiliation paragraph between title and e-mail.
    affiliation_start = None
    for i in range(title_i + 1, email_i):
        if not normalize_ws(paras[i].text):
            continue
        if leading_superscript_label(paras[i]) is not None:
            affiliation_start = i
            break
    if affiliation_start is None:
        # fallback: centered, non-bold paragraphs immediately before e-mail
        candidates = [i for i in range(title_i + 1, email_i) if normalize_ws(paras[i].text)]
        if len(candidates) < 2:
            raise ValueError("could not distinguish author and affiliation paragraphs")
        affiliation_start = candidates[-1]

    author_paras = [
        paras[i] for i in range(title_i + 1, affiliation_start)
        if normalize_ws(paras[i].text)
    ]
    if not author_paras:
        raise ValueError("no author paragraph found")
    authors, author_html = split_authors(author_paras)

    affiliations = []
    for i in range(affiliation_start, email_i):
        if not normalize_ws(paras[i].text):
            continue
        label = leading_superscript_label(paras[i])
        text = paragraph_text_without_leading_superscript(paras[i])
        affiliations.append(f"{label}. {text}" if label else text)

    email = extract_email(paras[email_i].text)
    _, media_by_rid = image_relationships(path)

    state = "abstract"
    abstract_blocks: list[tuple[str, Any]] = []
    acknowledgements: list[str] = []
    references: list[str] = []
    seen_figure_digests: set[str] = set()

    for i in range(email_i + 1, len(paras)):
        p = paras[i]
        text = normalize_ws(p.text)
        lower = text.casefold().rstrip(":")
        if lower in {"acknowledgments", "acknowledgements"}:
            state = "acknowledgements"
            continue
        if lower in {"references", "reference"}:
            state = "references"
            continue

        if text:
            if state == "abstract":
                abstract_blocks.append(("text", text))
            elif state == "acknowledgements":
                acknowledgements.append(text)
            else:
                references.append(text)

        ids = paragraph_image_ids(p)
        if ids and state == "abstract":
            caption = paragraph_caption(p)
            for rid in ids:
                data = media_by_rid.get(rid)
                if not data:
                    continue
                digest = hashlib.sha256(data).hexdigest()
                if digest in seen_figure_digests:
                    continue
                seen_figure_digests.add(digest)
                # Determine extension from relationship target where possible.
                ext = ".png"
                try:
                    rels, _ = image_relationships(path)
                    ext = Path(rels.get(rid, "image.png")).suffix or ".png"
                except Exception:
                    pass
                abstract_blocks.append(("figure", Figure(data=data, extension=ext, caption=caption, digest=digest)))

    if not any(kind == "text" and value for kind, value in abstract_blocks):
        raise ValueError("no abstract body found")

    return ParsedAbstract(
        source=path,
        title=title,
        authors=authors,
        author_html=author_html,
        affiliations=affiliations,
        email=email,
        abstract_blocks=abstract_blocks,
        acknowledgements=acknowledgements,
        references=references,
    )


def parse_front_matter(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.S)
    if not m:
        raise ValueError(f"{path}: missing YAML front matter")
    data = yaml.safe_load(m.group(1)) or {}
    return data, m.group(2)


def load_talks(talks_dir: Path) -> list[tuple[Path, dict[str, Any]]]:
    talks = []
    for path in sorted(talks_dir.glob("*.md")):
        try:
            fm, _ = parse_front_matter(path)
        except Exception:
            continue
        if fm.get("name"):
            talks.append((path, fm))
    return talks


def match_talk(title: str, talks: list[tuple[Path, dict[str, Any]]], threshold: float, ambiguity_gap: float):
    nt = normalize_title(title)
    exact = [(p, fm, 1.0) for p, fm in talks if normalize_title(str(fm.get("name", ""))) == nt]
    if len(exact) == 1:
        return "matched", exact[0], []
    scored = []
    for path, fm in talks:
        score = SequenceMatcher(None, nt, normalize_title(str(fm.get("name", "")))).ratio()
        scored.append((path, fm, score))
    scored.sort(key=lambda x: x[2], reverse=True)
    if not scored or scored[0][2] < threshold:
        return "unmatched", None, scored[:3]
    if len(scored) > 1 and scored[0][2] - scored[1][2] < ambiguity_gap:
        return "ambiguous", None, scored[:3]
    return "matched", scored[0], scored[:3]


def dump_front_matter(data: dict[str, Any]) -> str:
    return yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=1000).strip()


def render_markdown(parsed: ParsedAbstract, talk_slug: str, figure_files: list[tuple[Figure, str]]) -> str:
    lines: list[str] = []
####    if parsed.author_html:
####        lines += ["### Authors", "", parsed.author_html, ""]
####    if parsed.affiliations:
####        lines += ["### Affiliations", ""]
####        lines += [f"{a}  " for a in parsed.affiliations]
####        lines.append("")
####    if parsed.email:
####        lines += [f"**Contact:** [{parsed.email}](mailto:{parsed.email})", ""]

    lines += ["### Abstract", ""]
    fig_iter = iter(figure_files)
    for kind, value in parsed.abstract_blocks:
        if kind == "text":
            lines += [value, ""]
        else:
            fig, relpath = next(fig_iter)
            alt = fig.caption or f"Figure from {parsed.source.name}"
            lines += [f"![{alt}]({{{{ '{relpath}' | relative_url }}}})", ""]
            if fig.caption:
                lines += [f"*{fig.caption}*", ""]

    if parsed.acknowledgements:
        lines += ["### Acknowledgements", ""]
        for p in parsed.acknowledgements:
            lines += [p, ""]
    if parsed.references:
        lines += ["### References", ""]
        for ref in parsed.references:
            lines += [ref, ""]
    return "\n".join(lines).rstrip() + "\n"


def update_talk_file(parsed: ParsedAbstract, talk_path: Path, fm: dict[str, Any], assets_dir: Path, assets_url_prefix: str, dry_run: bool) -> None:
    slug = talk_path.stem
    figures = [v for k, v in parsed.abstract_blocks if k == "figure"]
    figure_files: list[tuple[Figure, str]] = []
    if figures:
        outdir = assets_dir / slug
        if not dry_run:
            outdir.mkdir(parents=True, exist_ok=True)
        for idx, fig in enumerate(figures, 1):
            filename = f"figure-{idx}{fig.extension.lower()}"
            if not dry_run:
                (outdir / filename).write_bytes(fig.data)
            # Jekyll path must be site-root relative, not filesystem absolute.
            rel = "/" + f"{assets_url_prefix.strip('/')}/{slug}/{filename}"
            figure_files.append((fig, rel))

    # Preserve programme-authoritative fields, add abstract metadata.
    fm["authors"] = parsed.authors
    fm["affiliations"] = parsed.affiliations
    if parsed.email:
        fm["email"] = parsed.email
    fm["abstract_source"] = parsed.source.name

    body = render_markdown(parsed, slug, figure_files)
    content = f"---\n{dump_front_matter(fm)}\n---\n\n{body}"
    if not dry_run:
        talk_path.write_text(content, encoding="utf-8")


def create_talk_file(parsed: ParsedAbstract, talks_dir: Path, assets_dir: Path, assets_url_prefix: str, dry_run: bool) -> Path:
    slug = slugify(parsed.title)
    path = talks_dir / f"{slug}.md"
    fm = {"name": parsed.title, "speakers": [], "authors": parsed.authors, "affiliations": parsed.affiliations}
    if parsed.email:
        fm["email"] = parsed.email
    fm["abstract_source"] = parsed.source.name
    if not dry_run:
        talks_dir.mkdir(parents=True, exist_ok=True)
        path.write_text(f"---\n{dump_front_matter(fm)}\n---\n\n", encoding="utf-8")
    update_talk_file(parsed, path, fm, assets_dir, assets_url_prefix, dry_run)
    return path


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("docx", nargs="+", type=Path, help="DOCX file(s) or directories containing DOCX files")
    ap.add_argument("--talks-dir", type=Path, default=Path("_talks"))
    ap.add_argument("--assets-dir", type=Path, default=Path("assets/abstracts"))
    ap.add_argument("--assets-url-prefix", default=None, help="site URL prefix for extracted figures (defaults to asset-dir)")
    ap.add_argument("--threshold", type=float, default=0.86, help="minimum fuzzy-title score (default: 0.86)")
    ap.add_argument("--ambiguity-gap", type=float, default=0.04, help="minimum gap between top two matches (default: 0.04)")
    ap.add_argument("--dry-run", action="store_true", help="parse and match, but do not modify files")
    ap.add_argument("--allow-create", action="store_true", help="create a talk page if no programme match exists")
    args = ap.parse_args(argv)
    if args.assets_url_prefix is None:
        args.assets_url_prefix = str(args.assets_dir)
    sources: list[Path] = []
    for item in args.docx:
        if item.is_dir():
            sources.extend(sorted(item.glob("*.docx")))
        elif item.suffix.lower() == ".docx":
            sources.append(item)
    sources = list(dict.fromkeys(sources))
    if not sources:
        ap.error("no DOCX files found")
    if not args.talks_dir.exists() and not args.allow_create:
        ap.error(f"talks directory does not exist: {args.talks_dir}")

    talks = load_talks(args.talks_dir) if args.talks_dir.exists() else []
    counts = {"matched": 0, "ambiguous": 0, "unmatched": 0, "error": 0, "created": 0}

    for source in sources:
        try:
            parsed = parse_docx(source)
        except Exception as exc:
            counts["error"] += 1
            print(f"ERROR     {source.name}: {exc}")
            continue

        matched_title = TITLE_OVERRIDES.get(source.name, parsed.title)

        status, match, alternatives = match_talk(matched_title, talks, args.threshold, args.ambiguity_gap)
        if status == "matched" and match:
            talk_path, fm, score = match
            counts["matched"] += 1
            print(f"MATCHED   {source.name} -> {talk_path.name}  score={score:.3f}")
            update_talk_file(parsed, talk_path, fm, args.assets_dir, args.assets_url_prefix, args.dry_run)
        elif status == "ambiguous":
            counts["ambiguous"] += 1
            choices = "; ".join(f"{p.name} ({s:.3f})" for p, _fm, s in alternatives)
            print(f"AMBIGUOUS {source.name}: {parsed.title}\n          {choices}")
        else:
            if args.allow_create:
                counts["created"] += 1
                path = create_talk_file(parsed, args.talks_dir, args.assets_dir, args.assets_url_prefix, args.dry_run)
                print(f"CREATED   {source.name} -> {path.name}")
                if not args.dry_run:
                    fm, _ = parse_front_matter(path)
                    talks.append((path, fm))
            else:
                counts["unmatched"] += 1
                choices = "; ".join(f"{p.name} ({s:.3f})" for p, _fm, s in alternatives)
                print(f"UNMATCHED {source.name}: {parsed.title}")
                if choices:
                    print(f"          closest: {choices}")

    print("\nSummary: " + ", ".join(f"{k}={v}" for k, v in counts.items()))
    if counts["error"] or counts["ambiguous"] or (counts["unmatched"] and not args.allow_create):
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
