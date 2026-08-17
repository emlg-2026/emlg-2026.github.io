# EMLG 2026 DOCX abstract importer

The importer enriches the existing `_talks/*.md` files generated from the final programme.  It deliberately preserves the programme's `name`, `speakers` and `track` fields and adds the submitted author list, affiliations, contact e-mail, abstract, acknowledgements, references and figures.

## Install

```bash
python -m pip install -r tools/requirements.txt
```

## Dry run

```bash
python tools/import_abstracts.py source_abstracts/ \
  --talks-dir _talks \
  --assets-dir assets/abstracts \
  --dry-run
```

## Import

```bash
python tools/import_abstracts.py source_abstracts/ \
  --talks-dir _talks \
  --assets-dir assets/abstracts
```

The script matches the DOCX title against the existing talk title.  It reports `MATCHED`, `AMBIGUOUS`, `UNMATCHED`, or `ERROR`.  By default it will **not** create new talks for unmatched submissions, preventing accidental duplicates.

Images embedded in Word are extracted and deduplicated.  They are written under `assets/abstracts/<talk-slug>/` and linked from the generated Markdown.

The parser is tailored to the EMLG/JMLG submission pattern represented by `Abranches2.docx` and `Nishiyama1.docx`: title, author line(s), numbered affiliations, e-mail, abstract body, optional acknowledgements, optional figures, and references.
