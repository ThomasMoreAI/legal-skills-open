---
name: firmvault-search
title: FirmVault Search
description: Search FirmVault legal case documents — medical records, legal filings, insurance papers, correspondence. Use when looking up case files, finding documents by date / provider / category, locating records inside a case folder, or querying across cases. Auto-detects current case from working directory. Triggers on phrases like "find in case", "medical records", "legal documents", case names, provider names, or date ranges.
author: Whaleylaw
author_url: https://github.com/Whaleylaw/Roscoe-hermes/tree/main/skills/legal/firmvault-search
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: personal-injury
language: en
---

# FirmVault Search

Retrieve documents from the FirmVault case corpus by semantic similarity + structured filters. Backed by `qmd query` and a Python wrapper that adds frontmatter-based filters and case-scope auto-detection.

## When to use

- "Find Dr. Smith's notes in the Whaley v. Acme case"
- "Show me all medical records from October 2025"
- "What did the insurance adjuster say last month?"
- "Search across cases for surgery records mentioning rotator cuff"
- "Find all correspondence with State Farm in the active case"
- "Pull up legal filings from the Acme matter"

## How to call

```bash
uv run firmvault_search "<query text>" \
  [--scope all|case|<slug>] \
  [--category medical|legal|insurance|communication] \
  [--case <slug>] \
  [--date 2025-10-15] \
  [--date-range 2025-10-01..2025-10-31] \
  [--provider <name>] \
  [--limit 10]
```

Output is a JSON array — one object per hit:

```json
{
  "file_path": "/Users/.../FirmVault/cases/<slug>/medical/2025-10-15-dr-smith-visit.md",
  "score": 0.87,
  "snippet": "Patient presented with...",
  "frontmatter_excerpt": {
    "case_slug": "whaley-v-acme",
    "document_category": "medical",
    "document_date": "2025-10-15",
    "provider": "Dr. Smith Clinic",
    "document_type": "office_visit_note"
  }
}
```

## Scope auto-detection

If `--scope` is not given OR `--scope=case`:

- The CLI walks up from cwd looking for `FirmVault/cases/<slug>/`. If found, the search scopes to that slug automatically.
- If no such ancestor exists, the search falls back to cross-case (all cases).

Pass `--scope=all` to force cross-case. Pass `--scope=<slug>` to target a specific case explicitly.

## Filters

- `--category` — exact `document_category` match (`medical` | `legal` | `insurance` | `communication`)
- `--case` — exact `case_slug` match (alternative to `--scope=<slug>`)
- `--date` — exact `document_date` match (YYYY-MM-DD)
- `--date-range START..END` — inclusive `document_date` range
- `--provider` — case-insensitive substring match on `provider` / `sender` / `recipient`
- `--limit` — max hits returned (default `10`)

Filters apply Python-side post-filter on the markdown frontmatter, so unindexed fields still work.

## Tips

- Read the top hit's `file_path` with the Read tool to surface details to the user.
- For "find all X" queries, set `--limit 25` or higher and summarize.
- Use the `snippet` for at-a-glance scanning — only Read full files when needed.
- When inside a case directory, omit `--scope` to get case-scoped results automatically.
