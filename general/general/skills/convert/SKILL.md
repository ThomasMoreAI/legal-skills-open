---
name: convert
title: cite2footnote
description: Convert hyperlinked citations in a Word document (.docx) to Bluebook-formatted footnotes or endnotes. Use when the user mentions bluebook, footnote, endnote, citation conversion, or asks to convert citations.
author: anitasrinivasan
author_url: https://github.com/anitasrinivasan/cite2fn/tree/main/skills/cite2footnote
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# cite2footnote

Convert citations (hyperlinked, parenthetical, inline author-date) in a .docx document to Bluebook-formatted footnotes or endnotes.

## When to use

When the user provides a .docx file and asks to convert citations to Bluebook footnotes/endnotes, or mentions "bluebook", "footnote", "endnote", or "citation conversion".

## Prerequisites

The cite2fn Python package must be installed. If `python3 -m cite2fn.cli detect --help` fails, install it first:

```bash
pip install -e <plugin_directory>
```

Where `<plugin_directory>` is the root of the cite2fn plugin (the directory containing `pyproject.toml`). You can find it by looking for the `cite2fn` package in the plugin's install location.

## Workflow

### Step 1: Detect citations

Run citation detection on the input document:

```bash
python3 -m cite2fn.cli detect "<input.docx>"
```

This outputs JSON with all detected citations. Present a summary to the user:
- Count by type (hyperlink_external, hyperlink_internal, parenthetical, inline_author_date, existing_footnote)
- List any citations with issues (no URL, no year, etc.)
- Ask if the user wants footnotes or endnotes

### Step 2: Parse references (if applicable)

If the document has internal-anchor hyperlinks or parenthetical citations without URLs, parse the references section:

```bash
python3 -m cite2fn.cli parse-references "<input.docx>"
```

Match citations to reference entries to get full bibliographic information.

### Step 3: Fetch URL metadata

For citations with external URLs, fetch metadata:

1. Write the list of unique URLs to a temp JSON file
2. Run: `python3 -m cite2fn.cli fetch-urls <urls.json>`
3. This returns metadata (title, authors, journal, year, etc.) for each URL

### Step 4: Format citations in Bluebook

For each citation, use ALL available information to generate proper Bluebook formatting. You have:
- Display text from the document
- URL and fetched metadata (title, authors, journal, year, DOI)
- Matched reference entry text (from References section)
- Surrounding sentence context

Apply these Bluebook 21st edition rules:
- **Journal articles**: Author, *Title*, Volume ~JOURNAL~ First_Page (Year).
- **Books**: ~AUTHOR~, ~TITLE~ Page (Publisher Year).
- **Web/online sources**: Author, *Title*, ~SITE NAME~ (Date), URL.
- **Cases**: *Case Name*, Volume Reporter Page (Court Year).

CRITICAL — Formatting markers for the `bluebook_text` field:
- Wrap titles, case names, *Id.*, *supra*, and other Bluebook-italicized text in `*asterisks*` (e.g., `*The Role of AI in Law*`, `*Id.* at 5`, `*supra* note 3`).
- Wrap journal names, institutional authors, and other Bluebook small-caps text in `~tildes~` using **title case** (e.g., `~Harv. L. Rev.~`, `~Google Developers Blog~`, `~Tech Pol'y Press~`). Title case is required because Word's small caps formatting only transforms lowercase letters into smaller capitals — all-caps input renders with no visible size variation.
- **Do NOT use `~tildes~` for acronyms or initialisms.** Terms that are naturally all-caps in normal prose (SEC, CFTC, NIST, W3C, IMDA, ACLU, etc.) should be written as plain uppercase text with no tilde markers. Small caps are only for source names composed of words or word abbreviations. Examples: `SEC, *Algorithmic Trading...*` (no tildes on SEC), `NIST, *Announcing...*` (no tildes on NIST), but `~Harv. L. Rev.~` and `~Nat'l Cybersecurity Ctr. of Excellence~` use tildes because they are words.
- These markers are rendered as Word italic and small caps formatting in the output document.

Set confidence to "needs_review" if information is insufficient. Prefix with [NEEDS MANUAL FORMATTING] if you can't confidently format.

Output the citations as a JSON list with `bluebook_text` and `confidence` filled in for each.

### Step 5: User review

Present the formatted citations to the user in a clear table:
- Original display text -> Bluebook formatted text
- Flag any "needs_review" items
- Ask for corrections before proceeding

### Step 6: Assemble the document

Write the final citations JSON and run assembly:

```bash
python3 -m cite2fn.cli assemble "<input.docx>" <citations.json> -o "<output.docx>" [--endnotes] [--keep-references]
```

This will:
- Insert footnotes/endnotes with Bluebook text
- Clean inline text (remove years, parentheticals, hyperlink formatting)
- Add Word comments for flagged issues
- Apply supra/id. short forms for repeated sources
- Remove the References section (unless --keep-references)

### Step 7: Report results

Show the user:
- Number of footnotes inserted
- Number of existing footnotes converted
- Number of comments added
- Any issues encountered
- Path to the output file

Print this warning:

```
IMPORTANT: This tool provides a strong first pass, but human verification is still required.
Check: all Word comments, author name retention, italicization/small caps, pin cites, supra/id. cross-references.
```

## Important notes

- Always work on a COPY of the document (the assemble command writes to a new file)
- The original file is never modified
- If the document has no citations detected, inform the user and stop
