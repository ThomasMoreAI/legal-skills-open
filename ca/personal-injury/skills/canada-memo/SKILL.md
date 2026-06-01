---
name: canada-memo
title: canada-memo
description: When the user's message starts with "Canada" (case-insensitive), generate a full Ontario PI Case Assessment Memo from the case_stressor corpus and return it verbatim. This is the primary handler for Canadian fact patterns — DO NOT ask clarifying questions first; run the memo and let the lawyer react.
author: barndonmai
author_url: https://github.com/barndonmai/specter/tree/main/openclaw/skills/canada_memo
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ca
practice: personal-injury
language: en
---

# canada-memo

The case_stressor pipeline produces a structured **PI Case Assessment Memo**
backed by 340 real Ontario PI decisions. This skill is the agent's hook into
that pipeline.

## Trigger

Use this skill **whenever the user's message starts with the word
"Canada" / "canada" / "CANADA"** (any case), with or without a comma after.

Examples that trigger:

- `Canada, my child was playing soccer outside Target and got hurt`
- `canada slip and fall on icy sidewalk in Toronto`
- `CANADA: 55yo woman rear-ended on highway, soft tissue, treatment gap`
- `Canada — bicyclist hit by SUV in Ottawa`

## How to call

Strip the leading `Canada` (and any leading punctuation/whitespace) to get
the fact pattern, then call:

```python
from openclaw.skills.canada_memo.client import generate_memo
memo_text = generate_memo(facts)
```

Or via shell from within the OpenClaw harness:

```bash
cd ~/Specter && python3 -m openclaw.skills.canada_memo.client \
    "my child was playing soccer outside Target and got hurt"
```

The function returns a single markdown string. Print it **verbatim** as the
WhatsApp reply — do not summarize, do not paraphrase, do not add headers.
The memo already contains its own structure (`PI CASE ASSESSMENT MEMO …`).

## What NOT to do

- **Do not** ask clarifying questions before running the memo.
  The corpus is fact-pattern-indexed; a thin query still returns useful
  comparables. The memo itself flags "facts not provided" gaps inside the
  WEAKEST POINTS section — let the memo do the asking.
- **Do not** call `harvester_query.search` for Canadian queries that match
  this trigger — that would route to the small Canada vector slice without
  running the full memo (stats + Claude analysis + 3 key precedents).
- **Do not** invent precedents. Everything the memo cites comes from real
  CanLII data already in `case_stressor/chroma_db`.

## After the memo

The memo ends with:

> TYPE "what if [changed fact]?" TO STRESS-TEST YOUR CASE

If the user's NEXT message starts with `what if`, route to the
`/canada/whatif` endpoint with the prior facts as `original_facts` and the
new message as `modified_facts`. (Future enhancement — for now the agent
can re-run the baseline memo with adjusted filters.)

## Latency

The memo takes ~10–25 seconds because it embeds the query via Voyage and
asks Claude Opus to write the analysis from the retrieved cases. Set the
WhatsApp typing indicator if the surface supports it; otherwise just let
the memo land.

## Hard rules — no fabrication

The memo is grounded in the case_stressor query result. Don't:

- Append your own "additional thoughts" after the memo.
- Invent a damages range outside what the memo states.
- Claim a holding the memo doesn't.

If the user wants more detail on a single cited case, call
`caselaw_query` with that citation — that's the next-layer skill.
