---
name: deposition-transcript-analyzer
title: Deposition Transcript Analyzer
description: 'Analyzes deposition transcripts to extract litigation work product including executive summaries, testimony indexes, admission compilations, impeachment maps, credibility assessments, motion/trial designations, and follow-up checklists. Use when reviewing a deposition for case strategy, summary judgment prep, trial prep, or post-deposition analysis. Triggers: deposition analysis, transcript review, testimony index, admissions, impeachment, trial designations.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/deposition-transcript-analyzer
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Deposition Transcript Analyzer

Extracts and organizes deposition testimony into structured work product for motions, trial, and case strategy.

## Prerequisites

1. Completed deposition transcript (full text or upload)
2. Witness identity and role (party/third-party, represented side)
3. Claims and defenses at issue
4. Prior statements or documents for impeachment comparison (optional)

## Quick Start

Collect prerequisites, then run phases 1–7 sequentially. For time-limited review, run Phase 1 only and flag key admissions and impeachment points inline.

## Workflow

### Phase 1 — Executive Summary

Produce a structured summary covering:

- **Header**: Witness name, role, date, page count, examining counsel
- **Witness profile**: Demeanor (cooperative/hostile/evasive/credible), preparation level (well-prepared/poorly prepared/over-coached)
- **Key takeaways**: Top 3 most significant testimony points
- **Helpful vs. harmful testimony**: Side-by-side with page citations
- **Credibility**: Assessment with likely jury appeal
- **Follow-up needed**: Documents to obtain, witnesses to depose, discovery requests, legal research

### Phase 2 — Testimony Index

Table: `Page:Line | Topic | Summary | Importance (High/Med/Low) | Use (Liability/Damages/Impeachment)`

Organize by: chronology, key events, witness knowledge, documents discussed, admissions, denials, credibility issues, damages, expert-related.

### Phase 3 — Admission Compilation

Classify each admission by type:

| Type | Meaning |
|------|---------|
| Direct | Witness explicitly concedes a fact |
| Implied | Testimony logically supports your position |
| Adoptive | Witness adopts document content or another's statement |
| Party binding | Party-witness statement binding under FRE 801(d)(2) |

For each admission record: factual proposition, citation (page:line), exact quote, significance to claim element. Group by liability, damages, and credibility.

### Phase 4 — Impeachment Index

Table: `Issue | Depo Testimony | Contradicting Source | Citation | Use At (SJ/Trial)`

Categories:

- **Internal inconsistencies** — contradictions within same deposition (cite both page refs)
- **Prior inconsistent statements** — conflicts with prior depo, interrogatories, declarations (FRE 613)
- **Document contradictions** — testimony vs. exhibit content
- **Implausibility** — memory gaps on events witness organized or owned
- **Bias/interest** — financial stake, relationship, animosity

### Phase 5 — Motion & Trial Designations

**Summary judgment** (FRCP 56): Table with `Motion Topic | Page:Line | Summary | Support/Oppose SJ`

**Trial** (FRCP 32): Table with `Purpose | Page:Line | Content Summary | Est. Time`

**Counter-designations**: For each expected opposing designation, identify context pages that qualify or contradict (FRE 106 completeness).

### Phase 6 — Credibility Assessment

Table: `Factor | Rating | Transcript Examples (p. refs)`

Factors: Consistency, Responsiveness (direct/evasive/argumentative), Memory (good/selective/poor), Bias indicators, Document support.

Note jury appeal: likeability, believability, witness strengths and weaknesses.

### Phase 7 — Follow-Up Checklist

Table: `Action | Basis in Transcript | Priority (High/Med/Low)`

Action types: subpoena documents, depose identified witnesses, RFAs to lock admissions, legal research on issues raised.

## Pitfalls

- **Always cite page:line** — no paraphrasing without citation
- **Distinguish party-witness admissions** (FRE 801(d)(2) non-hearsay) from third-party testimony
- **Flag errata-sheet changes** — original testimony may still be usable for impeachment
- **Video depositions** — bracket demeanor observations as `[OBSERVATION]` to distinguish from transcript text
- **Counter-designations** must provide context without distorting meaning (FRE 106)
- **FRCP 32 admissibility** — confirm witness unavailability or adverse-party status before designating
- **Check local rules** for designation/counter-designation exchange deadlines

## Key Authorities

- FRCP 32 — Using depositions in court proceedings
- FRCP 56 — Summary judgment (deposition use)
- FRE 801(d)(2) — Party-opponent admissions (non-hearsay)
- FRE 613 — Prior inconsistent statements (impeachment)
