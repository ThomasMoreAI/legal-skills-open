---
name: evidence-liability-summary
title: Evidence & Liability Summary
description: Generates a structured evidence and liability summary for plaintiff-side personal injury negligence claims. Triggers when the user needs liability analysis, negligence element breakdowns, evidence cataloging with gap identification, discovery assessment, or pre-trial case evaluation.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/evidence-liability-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: personal-injury
language: en
tags: [analysis, litigation, summarization, summary]
---

# Evidence & Liability Summary

Synthesizes collected evidence into a structured negligence liability analysis (duty, breach, causation, damages) for plaintiff-side personal injury litigation.

## Prerequisites

Gather before starting:

- **Incident facts** — date, time, location, parties, basic chronology
- **Evidence collected** — documents, witness statements, photos/video, medical records, digital evidence
- **Medical records** — treatment history, bills, prognosis, expert reports if available
- **Jurisdiction** — governing state/federal law
- **Defendant info** — identity, relationship to plaintiff, applicable standard of care

## Workflow

Mark the output **PRIVILEGED AND CONFIDENTIAL — ATTORNEY WORK PRODUCT**.

### Step 1 — Case Overview

| Element | Content |
|---|---|
| Parties | All parties by legal designation (plaintiff, defendant, third parties) |
| Incident | Date, time, location, circumstances |
| Chronology | Pre-incident through aftermath timeline |
| Gaps | Timeline gaps or inconsistencies needing investigation |

Write for a lawyer unfamiliar with the matter.

### Step 2 — Evidence Catalog

For each item, record:

| Field | Description |
|---|---|
| Exhibit # | Unique identifier |
| Category | Documentary / Testimonial / Physical / Digital |
| Date | Creation or collection date |
| Source | Custodian or origin |
| Description | Brief content summary |
| Relevance | High / Medium / Low probative value |
| Issues | Privilege, hearsay, authentication, admissibility concerns |

Flag chain-of-custody gaps, authentication needs, compelling evidence, and discovery gaps.

### Step 3 — Negligence Element Analysis

#### A. Duty of Care

- **Source**: statute, regulation, professional standard, common law, special relationship
- **Standard**: reasonable person, industry standard, professional code — cite authority
- **Defense anticipation**: expected denial of duty with counter-analysis

#### B. Breach of Duty

- Identify specific acts/omissions constituting breach
- Map each to supporting evidence by exhibit #
- Compare conduct against applicable standard
- Reference expert testimony where technical knowledge required
- Address anticipated defenses (industry compliance, regulatory adherence)

#### C. Causation

| Type | Test | Analysis |
|---|---|---|
| Actual (cause-in-fact) | "But for" test | Address alternative causes; show substantial factor |
| Proximate (legal cause) | Foreseeability | Address superseding/intervening causes |
| Multiple parties | Comparative fault / joint & several | Apportion under governing law if applicable |

#### D. Damages

| Category | Items |
|---|---|
| **Economic** | Past/future medical expenses, lost wages, lost earning capacity, property damage |
| **Non-economic** | Pain and suffering, emotional distress, loss of enjoyment of life, loss of consortium |
| **Total** | Low–high range |

- Support amounts with bills, employment records, estimates, expert testimony
- Include present-value calculations for future damages
- Address mitigation and pre-existing conditions

### Step 4 — Conclusions & Recommendations

Rate each element:

| Element | Strength (Strong / Moderate / Weak) | Key Risk |
|---|---|---|
| Duty | | |
| Breach | | |
| Causation | | |
| Damages | | |

Then provide:

- Case valuation range with comparable verdict/settlement basis
- Discovery gaps and recommended next steps
- Expert witnesses to retain
- Settlement target range and strategy
- Motion practice opportunities
- Statute of limitations status and procedural deadlines
- Risk assessment — recommend proceed / settle / ADR

### Step 5 — References

- Legal authorities in Bluebook format
- Evidence cross-reference table (exhibit #, description, file location)
- Expert reports (name, credentials, date, key opinions)

## Pitfalls & Checks

- Every factual assertion must trace to a specific exhibit — no unsupported conclusions
- Use `[VERIFY]` for any citation not confirmed against primary sources
- Address jurisdiction-specific negligence standards (comparative vs. contributory)
- Acknowledge weaknesses candidly — plaintiff-side framing must still be honest about defense arguments
- Consider ethical obligations regarding candor in merit evaluation
