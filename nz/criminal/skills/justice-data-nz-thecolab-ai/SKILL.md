---
name: justice-data-nz-thecolab-ai
title: Justice Data NZ
description: Query New Zealand Ministry of Justice data tables for finalised charges, convictions, sentencing outcomes, family-violence offences, and youth justice statistics. Use when Codex needs official MoJ justice statistics, workbook URLs, or JSON rows from public no-key justice data tables.
author: thecolab-ai
author_url: https://github.com/thecolab-ai/.skills/tree/main/skills/justice-data-nz
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: nz
practice: criminal
language: en
sources:
- title: Api Notes
  path: references/api-notes.md
- title: Source Notes
  path: references/source-notes.md
---

# Justice Data NZ

## Goal

Query official Ministry of Justice public data tables through a deterministic CLI with human-readable and JSON output.

## Use this when

- A user asks for New Zealand court charges, conviction, sentencing, family-violence, or youth-justice statistics
- A workflow needs a current Ministry of Justice data-table workbook URL
- Another tool or agent needs machine-readable rows for a given table year
- A user needs to cite the MoJ data-tables source rather than one-off PDF summaries

## Do not use this for

- Police-recorded victimisations, proceedings, or calls-for-service data
- Corrections prison muster, remand, parole, or sentence-management data
- Stats NZ table-builder extraction unless the user specifically asks for Stats NZ mirrors
- Private court data, suppressed case details, or authenticated Ministry systems

## Preferred workflow

1. Run `scripts/cli.py tables --json` to discover the current Ministry of Justice workbook URLs
2. Use `convictions --year YYYY` for people convicted plus finalised and convicted charges by offence
3. Use `sentencing --year YYYY` for sentencing outcomes for people and convicted charges
4. Use `family-violence --year YYYY` for family-violence offence counts, outcomes, convictions, and sentences
5. Use `youth --year YYYY` for children and young people statistics; add `--scope youth-court` for Youth Court-only data
6. Use `--json` when another tool or agent needs machine-readable output
7. Mention the Ministry of Justice as the upstream source and include the workbook URL when reporting figures

## CLI

Run with:

```bash
python3 skills/justice-data-nz/scripts/cli.py <command> [flags]
```

Commands:

- `tables [--query TEXT] [--limit N] [--json]` - list available MoJ data-table workbooks
- `convictions --year YYYY [--offence TEXT] [--json]` - people convicted, finalised charges, and convicted charges by offence
- `sentencing --year YYYY [--json]` - people convicted and convicted charges by most serious sentence
- `family-violence --year YYYY [--offence TEXT] [--json]` - family-violence offence, outcome, conviction, and sentence series
- `youth --year YYYY [--scope any-court|youth-court] [--age-group TEXT|all] [--offence TEXT] [--json]` - youth justice charge, people, offence, and order series

Examples:

```bash
python3 skills/justice-data-nz/scripts/cli.py tables --json
python3 skills/justice-data-nz/scripts/cli.py convictions --year 2025 --offence assault --json
python3 skills/justice-data-nz/scripts/cli.py sentencing --year 2025
python3 skills/justice-data-nz/scripts/cli.py family-violence --year 2025 --json
python3 skills/justice-data-nz/scripts/cli.py youth --year 2025 --scope youth-court --json
```

## Resources

- CLI entrypoint: `scripts/cli.py`
- Smoke test: `scripts/smoke_test.py`
- Source and fallback notes: `references/api-notes.md`

## Notes

- The CLI uses public, no-key Ministry of Justice workbook downloads linked from the data-tables page
- Workbooks are parsed with Python standard-library `zipfile` and XML tools; no external packages are required
- `tables` can fall back to data.govt.nz CKAN metadata if the MoJ page is blocked, but current values require the direct MoJ workbook downloads
- Every network call has a timeout and upstream failures are reported as clear user-facing errors
