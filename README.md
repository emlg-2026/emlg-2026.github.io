# EMLG 2026 conference website

Starter repository for the EMLG 2026 programme and online book of abstracts, using
`DigitaleGesellschaft/jekyll-theme-conference` as a remote Jekyll theme.

## 1. Put these files in GitHub

Create the repository:

    emlg-2026/emlg-2026.github.io

Then copy the contents of this starter folder into the repository and push to the
`main` branch.

## 2. Preview locally

Requirements: Ruby/Bundler.

    bundle install
    bundle exec jekyll serve

Open http://localhost:4000/

## 3. Publish with GitHub Pages

The included `.github/workflows/pages.yml` builds and deploys the site.

In GitHub, open:

    Settings -> Pages -> Build and deployment -> Source

and select **GitHub Actions**. Push to `main`. The organisation-level Pages URL is:

    https://emlg-2026.github.io/

## 4. Replace the sample content

The repository contains one placeholder talk, speaker, room, and programme entry so
that you can test the site immediately. Delete these files once the real content is
imported:

    _talks/example-emlg-2026-talk.md
    _speakers/jane-example.md
    _rooms/main-auditorium.md

The importer generates files prefixed with `generated-`.

## 5. Word -> website import

Install the Python dependencies:

    python -m venv .venv
    source .venv/bin/activate
    pip install -r tools/requirements.txt

The generic importer is style-driven. Edit `tools/import_config.yml` so that its Word
style names match those used in the abstract book. Then run:

    python tools/import_docx.py path/to/EMLG2026_Abstracts.docx

It generates:

    _talks/generated-*.md
    _speakers/generated-*.md
    _rooms/generated-*.md
    _data/program.yml

The generic importer assumes the **first author is the presenter**. This is only a
starter rule. Once the real Word file is inspected, adapt the parser to whatever
marks the presenting author in the book (asterisk, underline, bold, explicit label,
etc.).

### Recommended Word styles

For the cleanest automatic conversion, use distinct paragraph styles such as:

    Heading 1 / Day          -> conference day
    Heading 2 / Session      -> session title
    Heading 3 / Abstract Title -> talk title
    Authors                  -> author line
    Affiliations             -> affiliation paragraph(s)
    Abstract                 -> abstract paragraph(s)
    Time                     -> HH:MM
    Room                     -> room name

The actual importer should be tuned after inspecting the real `.docx`; do not spend
time manually restyling the whole book until that inspection has been done.

## 6. Add the final PDF

Copy the conventional PDF abstract book to:

    documents/EMLG2026-abstract-book.pdf

The navigation link is already configured.

## 7. Files you will normally edit

- `_config.yml` - conference title, timezone, navigation, theme settings
- `index.md` - landing-page copy
- `_data/program.yml` - generated programme
- `_talks/` - generated abstract pages
- `_speakers/` - generated presenter pages
- `_rooms/` - generated rooms
- `tools/import_config.yml` - Word style mapping
- `tools/import_docx.py` - importer logic

## Theme

https://github.com/DigitaleGesellschaft/jekyll-theme-conference

Pinned remote theme version in `_config.yml`: `v4.0.2`.
