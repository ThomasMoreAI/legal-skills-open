---
name: bailii-case-download-ciaransaunders
title: BAILII case downloader
description: Search BAILII (www.bailii.org) for a UK or Irish case and download the full judgment as a clean PDF. Use whenever the user wants a case from BAILII, gives a neutral citation (e.g. "[2024] EAT 114", "[2021] UKSC 5") or a BAILII URL and asks to fetch/download/save it, asks for "the full case as a PDF", wants to verify a case PDF against the authoritative source, or asks to find a case on BAILII by name. Also trigger when the user mentions BAILII, case law downloads, or building a bundle of authorities and needs the underlying judgments.
author: ciaransaunders
author_url: https://github.com/ciaransaunders/Skills-Public/tree/main/bailii-case-download
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: litigation
language: en
---

# BAILII case downloader

Fetches UK/Irish judgments from BAILII and saves them as clean, readable PDFs
(BAILII chrome, nav, search forms, donation banners and footers removed).

BAILII now sits behind **Anubis** — a JavaScript proof-of-work bot wall, on top
of its long-standing cloud-IP block. The bundled script solves the proof-of-work
in pure Python (no browser needed) and handles BAILII's CGI quirks, so prefer it
over `web_fetch`/`curl`, which will just hit the "Making sure you're not a bot!"
page.

## The script

`scripts/bailii_fetch.py` — self-contained, Python 3 stdlib only for fetching.
PDF rendering uses the first available of: `wkhtmltopdf` → headless
Chrome/Chromium → `weasyprint`. If none is present it saves the cleaned HTML and
says so in the output (you can then convert it yourself).

Run it with `python3 scripts/bailii_fetch.py <command> ...`. All commands print
JSON to stdout.

## Choosing a command (in order of preference)

**1. `cite` — when you have a neutral citation. Most reliable; use this first.**

```
python3 scripts/bailii_fetch.py cite "[2024] EAT 114" --out DIR
```

Resolves the citation via BAILII's citation finder and downloads the case.
Works for the usual courts: UKSC, UKHL, UKPC, EWCA, EWHC, EAT/UKEAT, UKUT, etc.
Exits with code 2 and a helpful message if the citation doesn't resolve.

**2. `url` — when you already have the BAILII case URL.**

```
python3 scripts/bailii_fetch.py url "https://www.bailii.org/uk/cases/UKSC/2021/5.html" --out DIR
```

**3. `search` — when you only have the case name. Returns candidates; does NOT auto-download.**

```
python3 scripts/bailii_fetch.py search "Uber Aslam" --limit 6
```

Prints a JSON list of `{url, title}` candidates (title-scoped search — fuzzy by
design). **Pick the right one yourself**, confirm with the user if ambiguous,
then download it with `url`. Don't assume the first result is correct; BAILII
often returns the whole litigation chain (ET → EAT → CA → SC) and you want the
specific instance the user means.

## Options

- `--out DIR`     where to save (default: current dir). Create/choose a sensible
                  folder, e.g. an authorities bundle directory.
- `--keep-html`   also keep the cleaned standalone HTML next to the PDF.
- `--no-pdf`      save cleaned HTML only, skip PDF rendering.
- `--limit N`     (search only) max candidates to return.

## Output

`cite` and `url` print JSON with `title`, `source_url`, `pdf` (path), optionally
`html`, and `pdf_engine`. The PDF carries a small "Retrieved from BAILII · <url>"
provenance banner at the top so the source is always traceable — useful for an
authorities bundle.

## Notes / caveats

- **Anubis is occasionally flaky.** The script already solves-and-retries and
  validates the final page (rejects bot-wall pages, checks it's a real
  `/cases/...html` judgment). If a fetch still fails, just run it again.
- **Always sanity-check the result.** Confirm the returned `title` matches the
  case the user asked for before relying on it — especially after `search`.
- This pulls **public** judgments from a free public legal database. It is not a
  substitute for a citator: BAILII does not show subsequent treatment / whether
  a case is still good law.
- Filenames are derived from the case title and capped in length; the script
  handles the awkward characters.
