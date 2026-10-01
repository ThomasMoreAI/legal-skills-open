---
name: scotuschecker-dgk-law-and-cognition-lab
title: SCOTUS Checker
description: Analyze Supreme Court opinions for principle invocation and methodological consistency. Use when the user asks about SCOTUS cases, principle weights, judicial methodology, constitutional principles, or consistency analysis. Also use when the user asks to "code an opinion," "check a case," "analyze a SCOTUS term," or anything involving Berman's model, SAW aggregation, or principled positivism.
author: DGK-Law-and-Cognition-Lab
author_url: https://github.com/DGK-Law-and-Cognition-Lab/SCOTUSChecker
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: constitutional
language: en
---

# SCOTUS Checker

Automated principle extraction and consistency auditing for Supreme Court opinions,
based on Mitchell Berman's Simple Additive Weighting model.

## What This Skill Does

This skill reads Supreme Court opinions and identifies which legal principles each
opinion invokes, how prominently each principle figures in the reasoning, and whether
each principle supports or opposes the outcome. It can:

1. **Code a single case** — fetch an opinion from Court Listener and produce a coding sheet
2. **Code a full term** — process all cases from an October Term in batch
3. **Run consistency analysis** — compare a case's principle usage against the Court's baseline weights
4. **Track principle weights over time** — estimate how the Court's methodology shifts across terms

## Modes

### Single Case
When the user asks about a specific case (e.g., "code the Dobbs opinion" or "analyze Bruen"):

1. Search Court Listener for the case using `scripts/scotus_code.py search "<case name>"`
2. Fetch and code the opinion using `scripts/scotus_code.py code --cluster <id>`
3. Display the coding sheet and save results to `data/codings/`

### Full Term
When the user asks to code a term (e.g., "code OT 2022" or "analyze the 2023 term"):

1. Run `scripts/scotus_code.py term <year> --output data/codings/ot<year>.csv`
2. This takes a while (2-4 hours depending on rate limits). Report progress.
3. When done, summarize findings: how many cases coded, top principles, consistency rate.

### Consistency Check
When the user asks whether a specific case is consistent with the Court's methodology:

1. Load baseline weights from `data/weights/` (or compute them if not cached)
2. Code the target case
3. Apply SAW formula: net_force = sum(weight * activation) across principles
4. Compare predicted vs actual outcome
5. If inconsistent, run discrepancy decomposition showing which weights would need to change

### Weight Tracking
When the user asks about how methodology has shifted:

1. Load or compute term-level weights from `data/weights/`
2. Plot weight trajectories over time
3. Flag principle shedding events (weights dropping to near-zero)

## Principle Taxonomy

### Tier 1: Interpretive Methodologies
- **T1 TEXTUALISM** — "plain meaning," "ordinary meaning," "text of the statute," "as written"
- **T2 ORIGINALISM** — "original meaning," "at the founding," "deeply rooted in history and tradition"
- **T3 PURPOSIVISM** — "legislative history," "congressional intent," "committee report"
- **T4 PRAGMATISM** — "practical consequences," "absurd results," "unworkable"

### Tier 2: Substantive Constitutional Principles
- **S1 STARE DECISIS** — "stare decisis," "precedent," "reliance interests." Only code when the opinion discusses WHETHER to follow or depart from prior decisions, not when merely citing a case.
- **S2 EQUAL PROTECTION** — "equal protection," "discrimination," "similarly situated"
- **S3 DUE PROCESS** — "due process," "fundamental right," "liberty interest"
- **S4 FREE SPEECH** — "First Amendment," "free speech," "content-based"
- **S5 FEDERALISM** — "federalism," "state sovereignty," "separation of powers"
- **S6 DIGNITY** — "dignity," "inherent worth," "evolving standards." Only code when the opinion independently appeals to dignity beyond a specific doctrinal framework.

### Tier 3: Doctrinal Tools (code only when explicitly relied on)
- **D1 AVOIDANCE CANON** — "constitutional doubt," "construe to avoid"
- **D2 CLEAR STATEMENT** — "clear statement," "unmistakably clear"
- **D3 DEFERENCE** — "Chevron," "deference," "agency interpretation"

## Prominence Scale (1-5)

1. **Mentioned** — footnote, passing reference
2. **Supporting** — paragraph or two, secondary consideration
3. **Significant** — sustained discussion, one of several pillars
4. **Central** — one of the opinion's two or three main lines of reasoning
5. **Dispositive** — the opinion's primary and controlling reason

When in doubt, go lower.

## Direction Coding

- **+1** — supports the outcome the opinion reaches
- **-1** — opposes the outcome (opinion discusses it but argues it's outweighed)
- **0** — neutral/indeterminate (rare)

Code direction as the opinion frames it. For dissents, the "outcome" is the dissent's preferred result.

## Key Decision Rules

- Citing a case for a proposition ≠ invoking stare decisis
- Code overlapping principles separately when the opinion makes distinct arguments
- Principles in footnotes get prominence 1 almost always
- If the opinion discusses a principle then rejects it, code it with direction -1
- Only code quoted reasoning if the opinion adopts it as its own

## Running the Scripts

All scripts are in `scripts/`. They require `python3`, `requests`, and `pandas`.

```bash
# Search for a case
python3 scripts/scotus_code.py search "Dobbs Jackson"

# Code a single cluster
python3 scripts/scotus_code.py code --cluster 6481357

# Code a full term
python3 scripts/scotus_code.py term 2022 --output data/codings/ot2022.csv

# Compute term-level weights
python3 scripts/scotus_code.py weights --terms 2018,2019,2020,2021,2022

# Run consistency check on a case against baseline weights
python3 scripts/scotus_code.py check --cluster 6481357 --baseline data/weights/ot2018-2022.json
```

## Output Format

Coding results are saved as both CSV and JSON in `data/codings/`.

CSV columns: case_name, author, opinion_type, outcome, principle_id, principle_name, prominence, direction, evidence

JSON includes full structured output with principles_not_coded and metadata.

## Data Storage

- `data/codings/` — raw coding sheets (CSV and JSON per term)
- `data/weights/` — estimated principle weights per term
- `data/consistency/` — consistency reports and discrepancy decompositions
- `data/corpus/` — cached opinion texts from Court Listener

## Court Listener API

Requires a free auth token (set as COURTLISTENER_TOKEN env var).
Get one at courtlistener.com — sign up, go to profile, copy token.
Rate limit: 5,000 requests/hour with token.

## LLM Configuration

The coding engine uses whatever model OpenClaw is configured with. The system prompt
for principle extraction is embedded in `scripts/scotus_code.py`. The prompt follows
the coding protocol exactly — same taxonomy, same prominence scale, same direction rules,
same decision rules.

## Background / Theory

Based on Mitchell Berman's principled positivism: net legal force = sum(weight × activation)
across all relevant principles. See: Kamper, "Computational Jurisprudence: Testing Berman's
Principled Positivism Through Agent-Based Modeling" (2026).

Code and data: https://dgk-law-and-cognition-lab.github.io/BermanModeling/
