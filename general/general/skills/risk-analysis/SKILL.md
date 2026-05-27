---
name: risk-analysis
title: Risk Analysis Summary
description: Generates structured risk analysis summaries for legal matters, identifying and evaluating risks by severity and likelihood with quantified exposures and mitigation strategies. Use when preparing risk assessments, exposure analyses, liability summaries, or pre-filing risk evaluations across litigation, regulatory, contractual, reputational, and operational domains.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/risk-analysis
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Risk Analysis Summary

Produces a prioritized risk analysis from matter documents, quantifying exposures and recommending mitigations for attorneys, clients, and stakeholders.

## Prerequisites

1. **Matter documents** — contracts, pleadings, correspondence, regulatory filings, insurance policies
2. **Matter context** — jurisdiction, industry, phase (pre-filing / active / settlement), key parties
3. **Risk tolerance** — if known, acceptable exposure thresholds or strategic constraints

## Workflow

### 1. Executive Overview

- **Matter snapshot** — one-paragraph factual summary
- **Top 3–5 risks** — ranked by severity × likelihood, one sentence each with estimated exposure
- **Immediate actions** — time-sensitive deadlines, SOL dates, regulatory windows

### 2. Risk Register

Assign each risk a sequential ID (R-01, R-02, ...) and complete:

| Field | Content |
|---|---|
| Category | Contractual / Regulatory / Litigation / Financial / Reputational / Operational |
| Description | Specific risk statement grounded in document evidence |
| Factual basis | Cite provisions, regulatory sections, correspondence, or facts |
| Legal authority | Statutes, regulations, case law — mark `[VERIFY]` if uncertain |
| Likelihood | High / Medium / Low with reasoning |
| Severity | Critical / Major / Moderate / Minor |
| Financial exposure | Best-case / most-likely / worst-case range |
| Non-monetary impact | Reputational harm, sanctions, operational disruption |
| Mitigating factors | Defenses, insurance coverage, factual counterarguments |
| Interdependencies | Other risk IDs that compound or conflict |

### 3. Risk Matrix

Plot risk IDs on a 3×3 severity (rows) × likelihood (columns) grid:

```
              │ Low            │ Medium         │ High
──────────────┼────────────────┼────────────────┼──────────────
Critical      │                │                │
Major         │                │                │
Moderate      │                │                │
```

### 4. Mitigation Strategies

For each risk rated Major/High or above:

- **Action** — specific, practical step
- **Type** — Legal defense / Procedural / Settlement / Insurance / Operational
- **Feasibility** — High / Medium / Low
- **Effectiveness** — estimated exposure reduction
- **Resources** — cost, time, personnel
- **Trade-offs** — whether this mitigation exacerbates another risk

### 5. Timeline

| Priority | Risk ID | Action | Deadline/Trigger | Owner |
|---|---|---|---|---|
| Urgent | | | | |
| Near-term (30–90 days) | | | | |
| Strategic (90+ days) | | | | |

Flag all hard deadlines: statutes of limitations, cure periods, regulatory filing dates.

### 6. Information Gaps

List areas needing additional investigation, discovery, or expert consultation to refine the assessment.

## Pitfalls

- **Ungrounded risks** — every risk must cite specific documents or facts; never assert risk in the abstract
- **Missing quantification** — provide dollar ranges with stated assumptions; flag estimates as conservative or aggressive
- **Fact vs. inference** — clearly distinguish established facts, reasonable inferences, and speculative scenarios
- **Tone imbalance** — neither minimize genuine risks nor catastrophize manageable exposures
- **Audience mismatch** — use language accessible to business stakeholders; define legal terms on first use
- **Unacknowledged uncertainty** — state confidence levels; identify what additional information would change the assessment
- **Ignored interdependencies** — flag where addressing one risk may worsen another
- **Jurisdiction blindness** — note where analysis depends on forum, governing law, or regulatory body
