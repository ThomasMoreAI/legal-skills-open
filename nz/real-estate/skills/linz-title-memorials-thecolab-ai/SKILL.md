---
name: linz-title-memorials-thecolab-ai
title: LINZ Title Memorials
description: Use when researching NZ Records of Title memorials, Building Act 2004 s73/s74 natural-hazard title entries, or LINZ/Landonline title memorial aggregate counts. Inspects public LINZ/LDS metadata safely, explains public-data and privacy limits, and generates aggregate-only OIA request templates; does not expose title, owner, address, or small-cell data.
author: thecolab-ai
author_url: https://github.com/thecolab-ai/.skills/tree/main/skills/linz-title-memorials
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: nz
practice: real-estate
language: en
sources:
- title: Api Notes
  path: references/api-notes.md
- title: Source Notes
  path: references/source-notes.md
---

# LINZ Title Memorials

## Goal

Inspect the public LINZ/LDS boundary for title memorial and Building Act 2004 s73/s74 natural-hazard title-entry research without exposing title-level records.

## Commands

```bash
python3 skills/linz-title-memorials/scripts/cli.py metadata --json
python3 skills/linz-title-memorials/scripts/cli.py boundary
python3 skills/linz-title-memorials/scripts/cli.py oia-template --group-by territorial_authority,year
```

Commands:

- `metadata [--json]` - fetch public LDS catalogue metadata for the NZ Property Titles layer and relevant Landonline title memorial tables; never fetches row samples or downloads.
- `boundary [--json]` - explain which outputs are safe and which are blocked.
- `oia-template [--group-by ...] [--min-cell-size N] [--json]` - draft an aggregate-only OIA request to LINZ.
- `count-building-act-hazard-notices [--group-by ...] [--json]` - returns a structured blocked response and the OIA next step.
- `count-building-act-hazard-removals [--group-by ...] [--json]` - returns a structured blocked response and the OIA next step.
- `list-instrument-types [--json]` - returns a structured blocked response rather than row-level code extraction.

## Privacy Boundary

Use only aggregate-safe outputs. Do not fetch or reveal individual Records of Title, title numbers, owner names, addresses, parcel identifiers, instrument numbers, memorial text, or unsuppressed small cells. The public LDS catalogue exposes metadata for relevant Landonline tables, but the joins needed for s73/s74 hazard counts include title/action/instrument identifiers.

## Workflow

1. Run `metadata --json` to confirm the live public source metadata and field boundary.
2. If the user asks for counts, explain that this keyless skill cannot compute them from row-level Landonline tables.
3. Run `oia-template` with the requested grouping and minimum cell size.
4. Return only aggregate-safe metadata or request wording.

## Resources

- CLI: `scripts/cli.py`
- Smoke test: `scripts/smoke_test.py`
- Source and privacy notes: `references/api-notes.md`
