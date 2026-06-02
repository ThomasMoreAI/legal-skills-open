---
name: xref
title: Xref
description: Cross-reference and defined term resolver for legal documents. Produces an interactive HTML viewer where every internal reference, defined term, and external statutory citation is hoverable/expandable in place.
author: dvelton
author_url: https://github.com/dvelton/xref/tree/main/skills/xref
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Xref

Resolve cross-references and defined terms in legal documents. When activated, Xref produces an interactive HTML file on the user's Desktop where internal references, defined terms, unresolved items, and external citations are navigable.

## Activation

Use this skill when the user asks to:
- "use xref on..."
- "run xref..."
- "resolve the cross-references in..."
- "make this document navigable"
- "link up the references in..."

Respond with:

> **Xref is active.** I'll parse the document, resolve cross-references and defined terms, and save an interactive HTML viewer on your Desktop.

Then run the workflow below.

## Supported sources

- Word documents (`.docx`): primary and most reliable input format
- PDF files (`.pdf`): supported, but less reliable because PDFs usually lack semantic structure

## Tool location

The Xref Python utility is located at:

```bash
<plugin_dir>/skills/xref/tools/xref.py
```

To find the actual path, run:

```bash
find ~/.copilot/installed-plugins -name "xref.py" -path "*/xref/*" 2>/dev/null
```

If not found there, check the cloned repo directory.

## First-run setup

Before first use, check that dependencies are installed:

```bash
python3 <path-to>/xref.py setup-check
```

If anything is missing, run the setup script from the xref repo or plugin directory:

```bash
bash setup.sh
```

For optional web tooling:

```bash
bash setup.sh --web
```

## Standard workflow

Use the single `run` command. Do not make the user manage intermediate JSON files.

```bash
python3 <path-to>/xref.py run --source "<path-to-document>"
```

This command:
1. Extracts document structure, including parent sections, subsections, schedules, exhibits, and section body text.
2. Finds internal references, defined-term uses, possible undefined terms, and external citations.
3. Resolves references to targets where possible.
4. Fetches external citation text when available.
5. Builds a self-contained HTML viewer.
6. Saves the output to `~/Desktop/<document-name>-xref.html` unless `--output` is supplied.

Use `--output` when the user requested a specific destination:

```bash
python3 <path-to>/xref.py run \
  --source "<path-to-document>" \
  --output "$HOME/Desktop/<document-name>-xref.html"
```

Use `--no-fetch-external` if network access is unavailable or the user wants to avoid external requests:

```bash
python3 <path-to>/xref.py run --source "<path-to-document>" --no-fetch-external
```

Use `--compact` if the document is large and the user wants a smaller HTML file:

```bash
python3 <path-to>/xref.py run --source "<path-to-document>" --compact
```

## Reporting results

After the command finishes, report:
- The saved output path
- Internal references resolved and unresolved
- Defined terms indexed, term uses, and possible undefined terms
- External citations found and fetched
- Any likely drafting issues, such as broken references

Example:

> **Done.** Saved to `~/Desktop/vendor-agreement-xref.html`.
>
> Xref indexed 45 sections, resolved 15 internal references, found 2 broken references, indexed 10 defined terms, flagged 2 possible undefined terms, and found 3 external citations.

## Error handling

If the document has no extractable text:

> This document does not appear to have extractable text. It may be a scanned PDF. Please provide a Word version or OCR the PDF first.

If many references do not resolve:

> The section structure appears unusual, so some references could not be matched. The viewer will still open, and unresolved items are listed in the Health tab.

If external citation fetching fails:

Do not fail the task. The viewer still renders the citations and links to official sources when URLs are available. Mention that external citation text was not fetched.

## Advanced/debugging commands

Use these only when investigating parser output or debugging Xref itself:

```bash
python3 xref.py extract-structure --source "<path-to-document>" > structure.json
python3 xref.py find-references --source "<path-to-document>" > references.json
python3 xref.py resolve-references --structure structure.json --references references.json > resolved.json
python3 xref.py fetch-external --citations '[{"citation_type":"eu_regulation","regulation":"GDPR","article":"28"}]' > externals.json
python3 xref.py build --source "<path-to-document>" --resolved resolved.json --externals externals.json --output ~/Desktop/document-xref.html
```

## Notes

- The viewer works in any modern browser with no server required.
- The source text is not rewritten or summarized.
- Broken internal references and possible undefined terms are surfaced as document health issues rather than silently guessed.
- Touch devices use tap-to-open panels instead of hover.
