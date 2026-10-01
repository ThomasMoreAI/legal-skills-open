---
name: nz-parliament-thecolab-ai
title: NZ Parliament
description: Track New Zealand Parliament bills and their legislative progress from the public bills.parliament.nz API. Use when the task involves NZ bills, legislation before Parliament, a bill's status or stage (first reading, select committee, etc.), who introduced a bill, government vs member's bills, or searching bills by keyword. Keyless, read-only; no login. Covers bills only (not MP directory, votes, Hansard, or petitions).
author: thecolab-ai
author_url: https://github.com/thecolab-ai/.skills/tree/main/skills/nz-parliament
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: nz
practice: general
language: en
sources:
- title: Api Notes
  path: references/api-notes.md
- title: Source Notes
  path: references/source-notes.md
---

# NZ Parliament

Track bills before the New Zealand Parliament and their progress through the House,
from the public **bills.parliament.nz** JSON API. Keyless, read-only; no login,
account, or API key.

## Use this when

- A user asks **what bills are before Parliament**, or to search bills by keyword
- A user wants a **bill's status / current stage** (first reading, select committee,
  second reading, royal assent, etc.) and its stage timeline
- A user wants to know **who introduced a bill**, or government vs member's bills
- A workflow needs machine-readable NZ legislation-in-progress data

## Do not use this for

- MP directory, electorates, party lists — not covered (bot-protected source)
- Votes / divisions, Hansard debates, written questions, petitions — not covered
- The full text of enacted law — use legislation.govt.nz
- Government press releases / ministers — use the `nz-ministers` skill

## Commands

```bash
cli=skills/nz-parliament/scripts/cli.py

# Current bills before the House
python3 $cli bills
python3 $cli bills --limit 30 --json

# Search bills by keyword (across all bills, not just current)
python3 $cli bills --keyword climate --all
python3 $cli bills -k "firearms" --all --json

# One bill's detail + stage timeline (by bill number or id)
python3 $cli bill 324-1
python3 $cli bill 204-1 --json
```

### Arguments

- `bills` — `-k/--keyword TEXT`, `--all` (include non-current bills), `--limit N`
  (1–50, default 20), `--page N`, `--json`
- `bill <ref>` — `<ref>` is a bill number (e.g. `324-1`) or bill id (GUID); `--json`

## Resources

- CLI entrypoint: `scripts/cli.py`
- Smoke test: `scripts/smoke_test.py`
- API endpoints, response shapes, and scope: `references/api-notes.md`

## Notes

- Data are live snapshots from bills.parliament.nz.
- The bill **list** shows the bill type (Government / Member's / Local / Private)
  but not the sponsoring MP; the sponsoring MP appears in `bill` **detail**.
- `--json` on every command gives machine-readable output for agent chaining.
- Use NZ English in any summaries built from the output (organisation, colour).
