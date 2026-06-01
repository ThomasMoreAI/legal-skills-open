---
name: nano-pdf
title: nano-pdf — natural-language PDF editing
description: Edit PDFs in place using natural-language instructions via the `nano-pdf` CLI — fix typos, swap titles, update dates, rename clients on a specific page without rebuilding the document. Use when an operator needs a small, targeted text fix on an existing PDF (decks, contracts, reports) and rebuilding the source isn't worth it.
author: spotcircuit
author_url: https://github.com/spotcircuit/rebar/tree/main/.claude/skills/productivity/nano-pdf
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# nano-pdf — natural-language PDF editing

Adapted from the Hermes Agent `nano-pdf` skill. Point it at a page, tell it what to change.

When this skill writes the edited PDF, drop it next to the source under `clients/{client}/pdf-edits-{YYYY-MM-DD}/` or `apps/{app}/pdf-edits-{date}/`. Never overwrite the original — write a new file alongside it. Never write to `~/`.

## Prerequisites

```bash
# Recommended
uv pip install nano-pdf

# Or
pip install nano-pdf
```

The CLI uses an LLM under the hood — make sure the appropriate API key env var is set (`nano-pdf --help` shows current config).

## Usage

```bash
nano-pdf edit <file.pdf> <page_number> "<instruction>"
```

## Examples

```bash
# Title fix on page 1
nano-pdf edit deck.pdf 1 "Change the title to 'Q3 Results' and fix the typo in the subtitle"

# Update a date
nano-pdf edit report.pdf 3 "Update the date from January to February 2026"

# Rename a client
nano-pdf edit contract.pdf 2 "Change the client name from 'Acme Corp' to 'Acme Industries'"
```

## When to reach for it

- Last-minute deck fix before a client meeting (typo, wrong date, swapped client name)
- Boilerplate contract update where regenerating from source is overkill
- Single-page text correction on a PDF we don't own the source files for

## When NOT to use it

- Layout changes, image swaps, or anything beyond text — escalate to a designer or rebuild from source
- Multi-page edits with cross-references — do those upstream in the source document
- Anything legally binding without a human re-read of the output

## Pitfalls

- Page numbers may be 0-based or 1-based depending on `nano-pdf` version. If the edit lands on the wrong page, retry with ±1.
- Always verify the output PDF after editing — open it, eyeball it, diff page count vs the original.
- Keep the original in source control or alongside the edit so a bad LLM rewrite doesn't lose the only copy.
