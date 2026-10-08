---
name: oia-statistics-nz-thecolab-ai
title: OIA Statistics NZ
description: Query New Zealand Public Service Commission six-monthly OIA compliance statistics with per-period and per-agency views, including timeliness, extensions, transfers, refusals, proactive publication, and Ombudsman complaints.
author: thecolab-ai
author_url: https://github.com/thecolab-ai/.skills/tree/main/skills/oia-statistics-nz
license: MIT
version: 0.1.2
execution_mode: open
jurisdiction: nz
practice: administrative
language: en
sources:
- title: Api Notes
  path: references/api-notes.md
- title: Source Notes
  path: references/source-notes.md
---

# OIA Statistics NZ

## Goal

Expose the Public Service Commission six-monthly Official Information Act (OIA) statistics in a small, deterministic CLI that removes scraping friction for downstream civic-transparency workflows.

The skill uses the PSC all-data CSV and official dated release workbooks. The CSV retains historical rows, including undated records when the upstream date column is damaged.

## Use this when

- You need per-agency OIA workload and performance series for NZ public-sector bodies.
- You need a machine-readable on-time rate, complaint, extension, transfer, or refusal snapshot for a period.
- You need the latest period and historical aggregate totals for reporting or comparison.
- You need official links and discovered OIA release table URLs for reproducible citations.

## Do not use this for

- Accessing any non-OIA datasets.
- Requesting private or protected internal agency systems.
- Non-official or third-party mirror data.

## Commands

- `list-agencies [--json]` - list distinct agencies that have a PSC OrgID. Release records without an OrgID are not listed separately; when merged by name (see Notes) they count toward that agency's `period_count`, otherwise query them by exact name with `agency`.
- `agency <name-or-org-id> [--period YYYY-MM-DD|latest] [--json]` - full per-period time series for one agency or one period. A name that resolves to one OrgID returns that agency's whole dated history.
- `period <YYYY-MM-DD|latest> [--sort name|worst|best|requests] [--json]` - all agencies for one period with computed timeliness percentage.
- `periods [--json]` - list all discovered survey periods with simple period-level counts.
- `tables [--format all|csv|xlsx|pdf] [--json]` - discover PSC OIA table assets from the landing page (plus the stable all-data CSV fallback).
- `timeliness [--period latest] [--sort worst|best|name] [--limit 20] [--json]` - agency timeliness metrics for a period.
- `refusals [--period latest] [--sort worst|best|name] [--limit 20] [--json]` - refusal count and percentage per agency.
- `extensions [--period latest] [--sort worst|best|name] [--limit 20] [--json]` - extension count and percentage per agency.
- `complaints [--period latest] [--sort complaints|final_opinions|worst|best|name] [--limit 20] [--json]` - Ombudsman complaints and final-opinion counts.
- `totals [--period latest] [--json]` - sector-wide totals and computed aggregate on-time rate for a period.

## CLI

Run with:

```bash
python3 skills/oia-statistics-nz/scripts/cli.py <command> [flags]
```

## Notes

- No API key, auth, or browser automation required for implemented commands.
- Network timeout and upstream-unavailable handling are built in for blocked upstreams.
- CSV remains preferred. If its reporting dates are invalid, `scripts/oia_workbooks.py` reads dated release workbooks using stdlib ZIP/XML.
- Release downloads have a 24-hour cache in `.cache/` inside the skill. Cached provenance retains the original retrieval time.
- Recovery never infers dates from CSV row order. Every agency record in a dated release workbook counts toward that period, so period totals equal the workbook. Release records with no exact CSV match keep `org_id: null` and an `identity_warning`. CSV rows that match no release record remain undated and are excluded from period totals. Published ID conflicts remain explicit warnings; use exact agency names for affected records.
- Release records without an OrgID are merged into an OrgID agency's history when their normalised name (macrons, punctuation and the CSV `?` placeholder ignored) equals, or is a whole-word part of, the names of exactly one OrgID agency that has no record of its own in that period. Merged records keep `org_id: null` and add `inferred_org_id`; they never count as a separate agency for ambiguity. Period totals are unaffected.
- A blank on-time count (e.g. NZ Police, Jul-Dec 2018, which could not report it) stays `null` with `timeliness_pct: null`; it is never treated as 0%. Aggregate on-time counts and percentages (`totals`, `periods`, `period`, `timeliness`) exclude such agencies from both numerator and denominator, report `on_time_coverage` (covered and missing agencies/requests) and add a warning. `requests_handled` totals still include them, and `timeliness --sort worst|best` lists them last.

## Resources

- API notes: `references/api-notes.md`
