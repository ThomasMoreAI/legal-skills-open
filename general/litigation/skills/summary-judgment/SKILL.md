---
name: summary-judgment
title: Summary Judgment Analysis
description: Produces structured summaries of summary judgment motions, orders, and decisions. Use when the user needs to summarize an MSJ ruling, prepare a case status report, evaluate appeal posture, or brief a client on a dispositive motion outcome.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/summary-judgment
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
tags: [analysis, motion, summarization, summary]
---

# Summary Judgment Analysis

Structured summary of a summary judgment motion, order, or decision for rapid assessment without reading the full document.

## Required Inputs

1. Summary judgment document (motion, opposition, reply, and/or court order)
2. Case caption and docket number
3. Jurisdiction (federal or state; which court)

## Quick Start

1. Identify the motion type (MSJ / Partial MSJ / Cross-MSJ), moving party, and disposition.
2. Extract undisputed material facts; flag genuine disputes.
3. Map each claim or defense to the court's ruling and reasoning.
4. Identify surviving issues for trial.
5. Assess practical implications: appealability, trial scope, relief, deadlines, settlement impact.

## Output Structure

### 1. Executive Overview

| Field | Content |
|-------|---------|
| Case caption | Full caption with docket number |
| Court | Jurisdiction, judge |
| Motion type | MSJ / Partial MSJ / Cross-MSJ |
| Moving party | Name and role |
| Disposition | Granted / Denied / Granted in part |
| Date | Date of order |

Follow with a 2–3 sentence plain-language summary of the ruling and its bottom-line effect.

### 2. Undisputed Material Facts

List facts the court deemed established (chronological or thematic). Flag:
- Genuine disputes → mark **DISPUTED**
- Evidentiary rulings excluding evidence
- Credibility determinations that influenced the outcome

### 3. Claims/Defenses Addressed

For each claim or defense ruled upon:

| Element | Detail |
|---------|--------|
| Claim/Defense | Name and legal basis |
| Legal standard | Statute, rule, or common-law test |
| Key authority | Primary cases/statutes relied on |
| Moving party's burden | How the court assessed the initial burden |
| Non-movant's response | Whether genuine issues of material fact were raised |
| Ruling | Granted/Denied with reasoning |

### 4. Surviving Issues

- Claims or defenses remaining for trial
- Unresolved factual disputes
- Conditions or limitations (e.g., leave to amend)

### 5. Practical Implications

| Question | Answer |
|----------|--------|
| Final/appealable? | Immediately appealable or interlocutory |
| Trial scope | Issues proceeding to trial |
| Relief granted | Dismissal, judgment entry, damages, fees, injunctive relief |
| Deadlines/obligations | Immediate compliance requirements |
| Settlement impact | How the ruling shifts leverage |

## Pitfalls and Checks

- **Accuracy over brevity** — never mischaracterize holdings; distinguish undisputed facts from legal conclusions.
- **Burden-shifting** — always trace whether the movant met the initial burden (Celotex / state equivalent) and whether the non-movant raised genuine disputes.
- **Jurisdiction** — note federal (FRCP 56) vs. state rules; flag jurisdiction-specific standards (e.g., heightened MSJ thresholds).
- **Standard of review** — note the standard applied (all inferences to non-movant) and whether the court deviated.
- **No editorial opinions** — do not predict appeal outcomes or insert strategy unless specifically requested.
- **Ambiguity** — when the court's reasoning supports multiple interpretations, acknowledge rather than choose one.
- **Citations** — reference page/paragraph numbers from the source for quick verification.
