---
name: adr-outcomes-summary
title: ADR Outcomes Summary
description: Generates structured summaries of mediation and arbitration proceedings, extracting outcomes, settlement terms, monetary amounts, obligations, releases, and enforcement steps. Trigger when the user needs to document mediation settlements, arbitration awards, or partial ADR resolutions from transcripts, agreements, mediator reports, or awards.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/adr-outcomes-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: arbitration
language: en
tags: [analysis, litigation, summarization, summary]
---

# ADR Outcomes Summary

Produces a structured summary of mediation or arbitration proceedings for client communication, internal records, and enforcement reference.

## Quick Start

Collect before drafting:
1. Source document — transcript, settlement agreement, MOU, mediator report, or arbitration award
2. Party names and representatives
3. Underlying dispute and procedural history
4. Any confidentiality agreements governing the ADR process

## Workflow

### Step 1 — Executive Overview

2–3 sentences stating: settled or awarded, primary terms, binding status.

### Step 2 — Background Table

| Field | Details |
|---|---|
| Parties | Names and roles (claimant / respondent) |
| Representatives | Counsel and party contacts |
| Neutral | Mediator or arbitrator, credentials |
| Session Date(s) | Dates and location |
| Dispute | Brief claim description |
| ADR Trigger | Clause, court order, or stipulation |

### Step 3 — Substantive Outcomes

**Mediation settlements** — extract each:
- Payment amounts and schedules (exact figures, due dates, method)
- Performance obligations with deadlines
- Release scope (claims released, parties covered, carve-outs)
- Confidentiality provisions (scope, duration, exceptions)
- Non-disparagement, non-admission, or reservation-of-rights clauses
- Ongoing relationship or future-dealings terms

**Arbitration awards** — extract each:
- Claims and counterclaims addressed
- Findings of fact and legal standards applied
- Relief granted or denied per issue
- Damages (compensatory, punitive, fees, interest, costs)
- Appeal or modification rights and deadlines
- Enforcement mechanism (FAA confirmation, state equivalent) — VERIFY applicable statute

**Unresolved issues** — list claims explicitly reserved, deferred, or left open.

### Step 4 — Next Steps Table

| Action | Responsible Party | Deadline |
|---|---|---|
| Execute formal settlement documents | [Party] | [Date] |
| Payment / performance | [Party] | [Date] |
| Court filing / dismissal / judgment entry | [Counsel] | [Date] |
| Compliance monitoring | [Party/Neutral] | [Ongoing] |

Flag whether court approval is required before the agreement takes effect.

## Pitfalls and Checks

- **Binding vs. non-binding** — distinguish enforceable arbitration awards (FAA or state statute) from mediation MOUs requiring full execution
- **Confidentiality** — flag ADR confidentiality scope prominently; omit protected mediation communications beyond the audience's authorization
- **Precision** — use exact dollar amounts, dates, and party names; no vague references
- **Objectivity** — present compromises neutrally; do not editorialize on outcome quality
- **Partial resolutions** — clearly delineate resolved vs. unresolved issues to avoid overstating scope
- **Jurisdiction** — US-focused; note when state-specific arbitration statutes (vs. FAA) govern enforcement
