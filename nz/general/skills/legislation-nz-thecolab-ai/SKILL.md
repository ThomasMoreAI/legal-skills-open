---
name: legislation-nz-thecolab-ai
title: New Zealand Legislation
description: Resolves, searches, and checks New Zealand Acts, Bills, secondary legislation, sections, point-in-time versions, and update feeds from official legislation.govt.nz and PCO sources. Use when a task needs NZ legislation text, exact section citations, current in-force status, amendments since a date, current Bills, or source caveats.
author: thecolab-ai
author_url: https://github.com/thecolab-ai/.skills/tree/main/skills/legislation-nz
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

# New Zealand Legislation

## Goal

Use official New Zealand Legislation sources to resolve legislation records, quote current or point-in-time sections, list versions, inspect current Bills, and check recent publication/update feeds.

## Quick triage

Use this when:
- A user cites an Act or regulation by year/number and needs exact text
- A finding needs a current "as at" section citation from legislation.govt.nz
- A workflow needs to check versions or amendments since a date
- A user asks for Bills currently before Parliament
- A task needs to distinguish keyless web/XML access from the keyed PCO API

Do not use this for:
- Legal advice or statutory interpretation beyond quoting/checking source text
- Non-NZ legislation
- Unofficial commentary, case law, or policy guidance

## CLI

```bash
python3 skills/legislation-nz/scripts/cli.py search "Grocery Industry" --type act --json
python3 skills/legislation-nz/scripts/cli.py get-act 2003/52 --json
python3 skills/legislation-nz/scripts/cli.py get-section 2003/52 9C --json
python3 skills/legislation-nz/scripts/cli.py get-section 1993/105 "Schedule 7" --json
python3 skills/legislation-nz/scripts/cli.py get-section 1993/105 "Schedule 7 clause 1" --json
python3 skills/legislation-nz/scripts/cli.py versions 2003/52 --json
python3 skills/legislation-nz/scripts/cli.py updates --since 2026-07-01 --json
python3 skills/legislation-nz/scripts/cli.py list-bills --json
python3 skills/legislation-nz/scripts/cli.py sources --json
```

Commands:

- `search QUERY [--type act|bill|regulation|secondary-legislation] [--field title|content] [--source auto|web|api] [--limit N] [--json]`
- `get-act ACT_ID [--version YYYY-MM-DD|latest] [--sections-limit N|--all-sections] [--json]`
- `get-section ACT_ID SECTION [--version YYYY-MM-DD|latest] [--json]`
- `versions ACT_ID [--version YYYY-MM-DD|latest] [--limit N] [--json]`
- `updates --since YYYY-MM-DD [--type act|bill|regulation|secondary-legislation] [--limit N] [--json]`
- `list-bills [QUERY] [--all-statuses] [--limit N] [--json]`
- `sources` or `datasets` for source metadata and caveats

`ACT_ID` can be a `year/number` pair such as `2003/52`, a work/version id such as `act_public_2003_52`, or a canonical legislation.govt.nz URL.

`SECTION` accepts a body section label (`9C`), a schedule (`Schedule 7`, `sch 7`, `sched 7`), or a clause within a schedule (`Schedule 7 clause 1`, `sch 7 cl 1`). Schedules live in a separate XML tree from body sections, so they must be asked for by name. Bare numeric labels always resolve to the body section first — `get-section 1993/105 7` returns s7 "Control defined", not Schedule 7. Each result carries a `kind` field of `section`, `schedule`, or `schedule-clause`; schedule clauses also carry a `schedule` field. Check `kind` before quoting a result as a section.

## Source Behaviour

- `get-act` and `get-section` use keyless official XML format URLs from legislation.govt.nz.
- `search`, `versions`, and `list-bills` use keyless official legislation.govt.nz web pages by default.
- `updates` uses the official public web-feed generator and parses the returned Atom feed.
- `search --source api` uses the PCO developer API and requires `LEGISLATION_NZ_API_KEY` or `PCO_API_KEY`.
- Network calls time out after 10 seconds by default. Upstream blocks, bot challenges, missing API keys, and parse failures are surfaced as explicit non-stacktrace errors.

## Resources

- CLI: `scripts/cli.py`
- Smoke test: `scripts/smoke_test.py`
- Source notes and caveats: `references/api-notes.md`
