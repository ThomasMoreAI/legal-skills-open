---
name: decision-record-verification
title: Decision Record Verification
description: Cross-references a judge's decision, court opinion, or final order against one or more hearing/trial/deposition transcripts to verify whether the record supports each finding. Produces strict dual-citation blocks with document names, page/line references, and verbatim quotes from both sources. Use when preparing appellate review, post-trial motions, record discrepancy audits, or transcript-based fact checks of judicial findings.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/decision-record-verification
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
tags: [analysis, summary]
---

# Decision Record Verification

Cross-reference a court decision against transcripts and surface record alignments, discrepancies, and gaps with exact dual-source citations.

## Prerequisites

- **Decision document** — opinion/order/judgment to test against the record
- **Transcript set** — one or more sessions (trial, hearing, or deposition) with page/line numbering when available
- **Session labels** — clear names for each transcript file (for example, `Day 1 AM`, `Day 1 PM`)
- **Scope confirmation** — identify whether review is full-document or limited to specific findings/issues

If required documents are missing or unlabeled, request them before analysis.

## Quick Start

1. Read the decision in full and extract each factual finding, credibility determination, and testimony-dependent legal conclusion.
2. Convert each finding into a verification claim.
3. Review transcripts in session order and capture support/conflict passages for each claim.
4. Write one citation block per match using exact quotes and pinpoint citations.
5. Finish with a findings summary: alignments, discrepancies, and record gaps.

## Workflow

### 1. Anchor the Decision

- Treat the decision as the baseline source.
- Extract only claims that depend on testimony or the trial/hearing record.
- Keep each claim atomic (one proposition per claim) to avoid mixed citations.

### 2. Cross-Reference Transcripts

- Review each transcript session in chronological order.
- Tag each matched passage as:
  - **`[ALIGNMENT]`** — transcript directly supports the decision's characterization
  - **`[DISCREPANCY]`** — transcript contradicts, materially differs from, or fails to contain what the decision attributes to the record

### 3. Build Citation Blocks

Use this exact field order for every block:

- **`[ALIGNMENT]` or `[DISCREPANCY]`**
- **Document Name (Decision):** full decision filename/title
- **Location (Decision):** `Page X, Line Y` (or paragraph/section when line numbers do not exist)
- **Decision Quote:** exact verbatim excerpt
- **Document Name (Transcript):** full transcript filename/session label
- **Location (Transcript):** `Page X, Line Y`
- **Transcript Quote:** exact verbatim excerpt
- **Note:** optional 1-2 sentence explanation of why the pair is support or divergence

### 4. Summarize Findings

After all citation blocks, provide:

- **Primary Alignments** — highest-impact ways the record supports the decision
- **Primary Discrepancies** — highest-impact ways the record diverges from the decision
- **Record Gaps** — decision findings with no located supporting/opposing transcript passage

## Output Order

1. **Header block** listing all reviewed documents and transcript session labels
2. **Citation blocks** grouped by session, in session order
3. Within each session group: list **`[ALIGNMENT]`** blocks first, then **`[DISCREPANCY]`** blocks
4. **Large-corpus override:** if the corpus is very large or the user requests priority triage, list **`[DISCREPANCY]`** blocks first, then **`[ALIGNMENT]`** blocks
5. **Summary of Findings**

## Quality Controls

- Quote verbatim in both `Decision Quote` and `Transcript Quote`; do not paraphrase those fields.
- Never invent page/line references.
- If pinpoint location cannot be determined, write:
  - `Page/Line unavailable — approximate location: <section or paragraph description>`
- Do not treat similar language as equivalent to an exact statement.
- If a decision paraphrases testimony, flag that in `Note`.
- Flag sessions with zero relevant passages; absence can be material.
- Mark uncertain citations or interpretations with `[VERIFY]`.

## Edge Cases

- **Multi-session transcripts**: treat each file as a distinct source and keep session label in every block.
- **Incomplete/redacted transcripts**: record the limitation under `Record Gaps`.
- **Privileged or sealed material**: do not reproduce protected excerpts; flag and advise handling under governing order.
- **Non-U.S. records**: adapt pinpoint format to the jurisdiction's transcript citation convention.
