---
name: caselaw-query
title: caselaw-query
description: Find appellate cases that cite or interpret a given statute via the CourtListener API (Free Law Project). Use AFTER a Harvester or web_fallback hit, when the user wants case law interpreting the statute. Returns case_name, court, date_filed, courtlistener URL, and a snippet — no opinion text generation. Strict no-fabrication.
author: barndonmai
author_url: https://github.com/barndonmai/specter/tree/main/openclaw/skills/caselaw_query
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# caselaw-query

Surfaces real appellate decisions that cite a statute. The "case law interpreting key sections" axis from the hackathon rubric.

## When to use this skill

- After `harvester_query.lookup_citation` returns a hit and the user asks
  things like:
  - *"any cases on this?"*
  - *"how have courts interpreted this?"*
  - *"is there precedent?"*
  - *"what's the standard for 'reasonable' under § 22350?"*
- After `pi_brief_format` renders a brief, as a follow-up enrichment.
- For doctrine-level questions where the user names a known section.

## When NOT to use it

- Not for fact-pattern triage ("client tripped on a sidewalk…"). CourtListener
  is statute-citation-driven, not fact-pattern-driven.
- Not for damages comparables (CourtListener is appellate opinions, not jury
  verdicts; settlements aren't there).
- Not as a first-line statute lookup. **Always do statute lookup first** —
  this skill enriches the answer, doesn't replace it.

## Hard rules — no fabrication

This skill **only surfaces what CourtListener returns**. Do not:

- Summarize an opinion you haven't fetched.
- Claim a holding the search snippet doesn't mention.
- Combine multiple cases into "the law says X" without citing each.
- Attribute a quote to an opinion unless the snippet shows it verbatim.

The brief response shape: list the top N cases with case name, court,
date, and the URL. The user clicks the URL to read the actual opinion.
Specter's role is *retrieval*, not *summarization* (per SOUL voice rules).

## Required env

```bash
COURTLISTENER_API_KEY=<token from https://www.courtlistener.com/help/api/rest/#authentication>
```

Free tier (5,000 queries/hour) is more than enough for the hackathon.
Don't commit the key — `.env` is gitignored.

## How to call

### Shell

```bash
cd ~/Specter && .venv/bin/python -m openclaw.skills.caselaw_query.client \
    "Cal. Veh. Code § 23152(a)" --k 5
```

```bash
cd ~/Specter && .venv/bin/python -m openclaw.skills.caselaw_query.client \
    "Tex. Transp. Code § 545.351" --jurisdiction TX --k 3
```

### Python

```python
from openclaw.skills.caselaw_query.client import cases_for_statute, healthz

cases_for_statute("Cal. Veh. Code § 23152(a)", k=5)
# returns list of dicts:
#   [{"case_name": "...", "court": "...", "date_filed": "...",
#     "url": "https://www.courtlistener.com/opinion/.../",
#     "snippet": "...", "citation_id": ...}, ...]
```

## Output for WhatsApp

Specter formats results like this — short, sourced, terse:

```
Cases interpreting Cal. Veh. Code § 23152(a):

  1. State v. Michaelson — Idaho Ct. App., 2025
     https://www.courtlistener.com/opinion/10692005/state-v-michaelson/

  2. State v. Polaski — Mont. Sup. Ct., 2005
     https://www.courtlistener.com/opinion/887401/state-v-polaski/

  3. United States v. Thornton — 9th Cir., 2006
     https://www.courtlistener.com/opinion/3036985/united-states-v-thornton/

5 total. Click for full opinion text.
```

If the user wants more detail on a specific case, Specter can run a fresh
CourtListener query for *that* opinion. **Specter does not paraphrase the
opinion's content from training-data knowledge.** If the API didn't return
a snippet for the case, she says so:

> "Top case is *State v. Michaelson* (Idaho 2025). I don't have a snippet — open the link for the holding."

## Coverage caveats

CourtListener has strong coverage for:
- US federal courts (SCOTUS, Circuits, District Courts)
- State **appellate** courts (state supreme + state courts of appeal)
- Some state trial courts (limited and uneven)

Empirically tested coverage for our hackathon citations:
- ✅ FL DUI § 316.193 — 54 results
- ✅ TX speed § 545.351 — 8 results
- ✅ CA DUI § 23152(a) — 5 results
- ⚠️ CA basic speed § 22350 — 1 result (citation-string formatting variance is the likely cause)
- ⚠️ NY VTL § 1192 — 2 results (same reason)

**Specter must report counts honestly.** If only 1 or 2 cases come back,
she says so — doesn't pretend a sparse result is comprehensive.

## What it does NOT do

- ❌ Damages / settlement amounts (those are paywalled in private DBs)
- ❌ Trial-court verdicts (CourtListener has very limited trial-court coverage)
- ❌ Predict case outcomes
- ❌ Provide legal advice
- ❌ Paraphrase opinions Specter hasn't fetched

If the user asks for any of those, Specter declines politely and points
at what CourtListener *can* answer — citing precedent, finding interpretive
opinions, cross-jurisdiction analogues.
