---
name: risk-assessment
title: Legal Risk Assessment
description: Generates structured legal risk assessment reports with categorized risks, 5x5 scoring matrices, and mitigation strategies. Use when preparing risk assessments, due diligence reports, transaction risk reviews, venture analysis, or board-level risk summaries.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/risk-assessment
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Legal Risk Assessment

Produces executive-ready risk reports evaluating likelihood, impact, and mitigation across legal risk categories for business scenarios, transactions, or operational decisions.

## Prerequisites

Gather before starting:
- **Scenario description** — transaction summary, venture details, or decision under review
- **Source documents** — contracts, term sheets, regulatory filings, corporate records
- **Organizational context** — industry, jurisdiction(s), risk tolerance, strategic objectives
- **Known constraints** — timeline, budget, regulatory environment, stakeholder concerns

## Workflow

### 1. Document Review

Extract from all provided materials:

| Element | Look For |
|---|---|
| Obligations & duties | Performance requirements, deadlines, conditions precedent |
| Representations & warranties | Scope, survival periods, indemnification triggers |
| Financial exposure | Stated amounts, penalties, liquidated damages |
| Jurisdictional issues | Choice of law, forum selection, regulatory bodies |
| Notice & cure provisions | Timelines, methods, non-compliance consequences |
| Ambiguous or silent terms | Missing definitions, unclear risk allocation, gaps |

### 2. Risk Identification

Categorize all material risks:

| Category | Key Inquiry |
|---|---|
| Regulatory compliance | Licensing, permits, reporting, pending rule changes |
| Contractual liability | Breach exposure, indemnification chains, liability gaps |
| Litigation probability | Dispute history, enforceability, venue risk |
| IP vulnerability | Ownership disputes, licensing gaps, infringement exposure |
| Employment & labor | Classification, non-competes, WARN Act, benefits |
| Tax implications | Structure-dependent exposure, transfer pricing, nexus |
| Reputational & governance | Fiduciary duties, disclosure obligations, ESG |

### 3. Risk Scoring

Rate each risk on a 5x5 matrix. **Rating = Likelihood x Impact.**

**Likelihood:** 1 Remote — 2 Unlikely — 3 Possible — 4 Likely — 5 Near certain

**Impact:** 1 Negligible (<$50K) — 2 Minor ($50K–$500K) — 3 Moderate ($500K–$5M) — 4 Major ($5M–$50M) — 5 Severe (>$50M)

**Thresholds:** Low (1–6), Medium (7–12), High (13–19), Critical (20–25)

### 4. Mitigation Strategies

For each Medium/High/Critical risk, propose mitigations and assess feasibility, cost, and residual risk:

| Strategy | Examples |
|---|---|
| Eliminate | Restructure transaction, remove problematic terms |
| Transfer | Insurance, indemnification, contractual risk allocation |
| Reduce | Compliance protocols, enhanced due diligence, reps & warranties |
| Accept | Document rationale, establish reserves, monitor triggers |

### 5. Gap Analysis

Flag explicitly:
- Missing documents or facts affecting risk precision
- Unsettled legal standards or pending regulatory changes
- Recommended due diligence steps or expert consultations

## Output Structure

```
## Executive Summary
- 3–5 sentence risk posture overview
- Top 3 risks with ratings
- Go / No-Go / Conditional recommendation

## Risk Matrix
[Table: Risk | Category | Likelihood | Impact | Rating | Key Driver]

## Detailed Risk Analysis
### [Risk Category]
#### [Specific Risk]
- **Exposure**: factual basis with document references
- **Legal basis**: applicable statute or case law
- **Likelihood rationale**: enforcement trends, precedent
- **Impact quantification**: dollar range, operational consequences
- **Mitigation options**: ranked by effectiveness

## Information Gaps & Limitations
[Bulleted list with recommended next steps]

## Recommendations
- Numbered, actionable items tied to specific risks
- Prioritized by risk rating and feasibility
- Decision framework: proceed / modify / decline
```

## Checks

- Reference specific contract sections, statutes, and facts — no generic risk language
- Quantify exposure with dollar ranges; acknowledge uncertainty explicitly
- Calibrate recommendations to the organization's stated risk tolerance
- Distinguish deal-breakers from commercially acceptable risks
- Mark unverifiable authority with `[VERIFY]`
- Do not minimize risks to favor a preferred outcome
- Note jurisdiction-specific variations where U.S. state law divergence is material
- Keep the executive summary accessible to non-lawyers
