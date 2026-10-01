---
name: nz-case-law-thecolab-ai
title: NZ Case Law
description: Search publicly available official New Zealand judgments by citation, court, party, judge, date and subject. Retrieval only; coverage is not exhaustive and this is not legal advice.
author: thecolab-ai
author_url: https://github.com/thecolab-ai/.skills/tree/main/skills/nz-case-law
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: nz
practice: general
language: en
sources:
- title: Source Notes
  path: references/source-notes.md
---

# NZ Case Law

Use the read-only Python CLI to retrieve and filter records exposed by the official first-party source.
Every command supports `--json`, bounded requests, stable exit codes, source URLs and retrieval timestamps.

## Commands

```bash
# search published judgments
python3 scripts/cli.py search QUERY --json
# find a neutral citation
python3 scripts/cli.py citation CITATION --json
# filter by court code
python3 scripts/cli.py court CODE --json
# filter by judge
python3 scripts/cli.py judge NAME --json
# discover recent judgments
python3 scripts/cli.py recent --court VALUE --json
# find a judgment identifier
python3 scripts/cli.py judgment ID --json
```

Add `--limit N` (1–100) to bound any command. Human output is the default.

## Coverage and interpretation

- Retrieval only: not legal advice or outcome prediction.
- Coverage is not exhaustive and varies by court and publication date.
- Respect suppression orders, statutory restrictions and source redactions.
- The connector does not bypass portal or bulk-access controls.

The CLI parses official Courts judgment cards and preserves neutral citation, court, date, judge
where published, summary and PDF provenance. Court sources fail independently, and valid zero-result
searches return empty success. Coverage limits are explicit on each record.

## Resources

- `scripts/cli.py` — canonical command entrypoint
- `scripts/test_contract.py` — deterministic repository contract audit
- `scripts/smoke_test.py` — parser fixture and bounded live probe
- `tests/fixtures/judgments.html` — deterministic official judgment-card fixture
- `references/source-profile.json` — command schema, source allowlist and warnings
- `references/source-notes.md` — feasibility, provenance and source limits
