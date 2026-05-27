---
name: parole-hearing-summary
title: Parole Hearing Summary
description: Summarizes parole hearing transcripts into structured analytical documents covering case identification, inmate testimony, victim impact, evidence review, board decision, and strategic analysis. Use when summarizing parole hearings, board decisions, parole denials, parole grant conditions, or preparing for future hearings and post-conviction strategy.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/parole-hearing-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: criminal
language: en
---

# Parole Hearing Summary

Distills parole hearing transcripts and exhibits into a structured, standalone record for attorney reference and future hearing preparation.

## Prerequisites

- Hearing transcript(s) — full or partial
- Exhibits — disciplinary records, psych evaluations, program certificates, parole plans, risk assessments, support letters
- Victim impact statements (if available)
- Prior hearing records — previous decisions, denial reasons, conditions (if applicable)

## Quick Start

1. Gather all hearing materials listed above
2. Produce the summary following the output structure below
3. Review against the checks in Guidelines before finalizing

## Output Structure

### 1. Case Identification Header

| Field | Content |
|---|---|
| Inmate Name / ID | Full name, DOC or BOP number |
| Offense of Conviction | Charge(s), conviction date, case number |
| Current Sentence | Term, min/max, time served |
| Hearing Date & Location | Date, facility, hearing type (initial/subsequent) |
| Board Panel | Names and titles of board members |
| Participants | Inmate, counsel, victims/representatives, witnesses, officials |

### 2. Procedural Matters

- Opening statements or preliminary rulings
- Continuances, objections, or procedural issues

### 3. Inmate Testimony

Summarize covering each area:

- [ ] Acceptance of responsibility and expressions of remorse
- [ ] Account of offense circumstances
- [ ] Institutional conduct and disciplinary history
- [ ] Rehabilitative programming (substance abuse, mental health, anger management)
- [ ] Educational / vocational achievements
- [ ] Post-release plan: housing, employment, family support, supervision
- [ ] Board Q&A — substance of board questions and inmate responses

### 4. Victim Impact

- Key points from victim or representative statements
- Ongoing impact and public safety concerns raised
- Position on parole suitability (support / oppose / neutral)

### 5. Witness Testimony

- Per witness: relationship to inmate, substance of testimony
- Board reaction or questioning of witnesses

### 6. Documentary Evidence

| Exhibit | Type | Key Content | Board Response |
|---|---|---|---|
| Ex. A | Psych evaluation | Low recidivism risk per [instrument] | Questioned methodology |
| Ex. B | Program certificates | Completed X, Y, Z programs | Noted positively |

Cover: disciplinary records, risk assessments, parole plans, expert reports, support letters.

### 7. Board Decision

**If DENIED:** reasons cited, statutory/regulatory factors, next eligible hearing date, recommendations for inmate.

**If GRANTED:** proposed release date, conditions of parole, special supervision, reporting obligations.

**If CONTINUED/DEFERRED:** information or actions required, timeline for follow-up.

### 8. Strategic Analysis

- Key factors influencing the board's decision
- Unresolved issues affecting future hearings
- Recommendations for counsel preparing subsequent proceedings
- Comparison to prior hearing outcomes (if applicable)

## Guidelines

- **Objectivity** — report without advocacy framing; distinguish direct testimony, documentary evidence, and board commentary
- **Quotations** — use direct quotes only when specific language is critical to board reasoning or inmate admissions
- **Length** — target 3–8 pages depending on hearing complexity
- **Factual basis** — every assertion must trace to the hearing record; flag inferences with `[INFERRED]`
- **Section headings** — keep all headings even if a section is "N/A" to preserve scanability
- **Confidentiality** — note sealed or redacted portions; never reconstruct sealed content

---
