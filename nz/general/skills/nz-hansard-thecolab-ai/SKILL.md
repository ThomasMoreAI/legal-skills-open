---
name: nz-hansard-thecolab-ai
title: NZ Hansard
description: Search official New Zealand parliamentary debates, speeches and oral-question transcripts by speaker, date, topic, bill and sitting.
author: thecolab-ai
author_url: https://github.com/thecolab-ai/.skills/tree/main/skills/nz-hansard
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

# NZ Hansard

Use the read-only Python CLI to retrieve and filter records exposed by the official first-party source.
Every command supports `--json`, bounded requests, stable exit codes, source URLs and retrieval timestamps.

## Commands

```bash
# list recent debate and question resources
python3 scripts/cli.py latest --json
# search transcript text across the latest five sittings
python3 scripts/cli.py search QUERY --sittings 5 --json
# filter by speaker across a bounded sitting corpus
python3 scripts/cli.py speaker NAME --sittings 5 --json
# discover oral questions by date
python3 scripts/cli.py oral-questions --date VALUE --json
# find debates relating to a bill across a bounded sitting corpus
python3 scripts/cli.py bill QUERY --sittings 5 --json
# find a complete debate item
python3 scripts/cli.py debate ID --json
```

Add `--limit N` (1–100) to bound returned records. Undated search, speaker and bill commands fetch the latest five official sittings by default; set `--sittings N` (1–20) to adjust that bounded corpus or `--date YYYY-MM-DD` for one exact sitting. Malformed dates fail before any source request. Human output is the default.

## Coverage and interpretation

- Quotes and attribution must remain tied to the official transcript.
- Speaker turns keep the published name in `speaker_as_published` and expose any parenthetical role or party separately as `role_or_party`.
- Preserve corrected or provisional transcript status when published.
- Do not infer a speaker's position beyond the retrieved words and context.

The CLI parses the official transcript listing and exact sitting pages at `/hansard-transcript/YYYY-MM-DD`. A date narrows search, speaker and bill commands; otherwise they search the explicitly bounded latest-sittings corpus. Debate IDs combine the sitting date with the published heading. Complete transcript pages remain the authoritative text and attribution surface.

## Resources

- `scripts/cli.py` — canonical command entrypoint
- `scripts/test_contract.py` — deterministic repository contract audit
- `scripts/smoke_test.py` — parser fixture and bounded live probe
- `tests/fixtures/listing.html` and `transcript.html` — official listing/transcript-schema fixtures
- `references/source-notes.md` — feasibility, provenance and source limits
