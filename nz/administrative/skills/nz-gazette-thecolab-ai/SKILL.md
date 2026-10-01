---
name: nz-gazette-thecolab-ai
title: NZ Gazette
description: Search and retrieve authoritative New Zealand Gazette notices by keyword, identifier, date, category and legislation. Retrieval only; not legal advice.
author: thecolab-ai
author_url: https://github.com/thecolab-ai/.skills/tree/main/skills/nz-gazette
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: nz
practice: administrative
language: en
sources:
- title: Source Notes
  path: references/source-notes.md
---

# NZ Gazette

Use the read-only Python CLI to retrieve and filter records exposed by the official first-party source.
Every command supports `--json`, bounded requests, stable exit codes, source URLs and retrieval timestamps.

## Commands

```bash
# search official notices
python3 scripts/cli.py search QUERY --json
# list latest notice resources
python3 scripts/cli.py latest --json
# find a Gazette notice identifier
python3 scripts/cli.py notice ID --json
# search notices under named legislation
python3 scripts/cli.py under-act ACT_NAME --json
# filter notice category
python3 scripts/cli.py category NAME --json
# discover notices in an inclusive ISO date range
python3 scripts/cli.py date --from YYYY-MM-DD --to YYYY-MM-DD --json
```

Add `--limit N` (1–100) to bound any command. Human output is the default.
Malformed or reversed date ranges fail as invalid input before any source request.

## Coverage and interpretation

- Notice retrieval is not legal advice and does not determine legal effect.
- Check linked amendments, revocations and corrections.
- Return only personal detail necessary to identify the official notice.

The CLI reads the Gazette's server-rendered official search surface and returns canonical notice/search links. Gazette IDs, dates, notice types and legislation remain tied to the linked official notice; this connector does not determine legal effect.

## Resources

- `scripts/cli.py` — canonical command entrypoint
- `scripts/test_contract.py` — deterministic repository contract audit
- `scripts/smoke_test.py` — parser fixture and bounded live probe
- `tests/fixtures/search.html` and `notice.html` — deterministic official-schema fixtures
- `references/source-notes.md` — feasibility, provenance and source limits
