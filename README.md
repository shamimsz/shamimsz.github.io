# Academic Portfolio

A Python-first professional portfolio for AI, data science, backend systems, and
research-oriented software.
The site is built as a static website generated from YAML, Markdown, and Jinja2
templates. It is designed for GitHub Pages.

## Set up

```bash
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
```

## Build and preview

```bash
./venv/bin/python scripts/export_static.py
python3 -m http.server 8000 --directory dist
```

Then open `http://127.0.0.1:8000`.

Do not edit files inside `dist/` directly. Edit the YAML/Markdown source files
and build again.

## Export for GitHub Pages

GitHub Pages hosts static files. The build script exports the site to plain HTML.

```bash
./venv/bin/python scripts/export_static.py
```

The generated site appears in `dist/`.

For a normal project repository, GitHub Pages serves the site under
`https://your-username.github.io/repository-name/`. The included GitHub Actions
workflow handles that path automatically. For a user site repository named
`your-username.github.io`, it exports for the root URL.
