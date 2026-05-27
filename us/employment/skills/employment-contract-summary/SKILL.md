---
name: employment-contract-summary
title: Employment Contract Summary
description: Produces structured U.S. employment contract summaries with section-level citations, capturing key terms, obligations, risks, and notable omissions. Use when summarizing an employment contract, executive employment agreement, offer letter, or consulting agreement. Triggers on "employment contract summary," "employment agreement," "compensation," "severance," "non-compete," "non-solicit," "confidentiality," or "restrictive covenant."
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/employment-contract-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
---

# Employment Contract Summary

Produce a citation-backed summary of an employment agreement with risks and gaps flagged.

## Prerequisites

Before starting, collect:

1. **Complete agreement set** — main contract plus exhibits, schedules, equity plans, and referenced policies.
2. **Governing law and venue** — from the document; if missing, mark as absent.
3. **Role context** — job title, level (executive/non-executive), and start date if known.

## Quick Start

1. Read the full agreement set.
2. Produce each section below in order, citing section/page for every material term.
3. Close with a risk assessment and recommended follow-ups.

## Output Sections

Produce sections in this exact order. Every cell must include a section/page citation or "missing."

### 1. Snapshot (4–6 lines)

Parties, role/title, start date, at-will vs. term, governing law, dispute forum.

### 2. Parties & Role

| Item | Details | Citation |
|---|---|---|
| Employer | | |
| Employee | | |
| Title/Reporting | | |
| Duties/Scope | | |

### 3. Term & Renewal

| Item | Details | Citation |
|---|---|---|
| Term length | | |
| Renewal/extension | | |
| Probationary period | | |

### 4. Compensation & Equity

| Component | Amount/Formula | Timing/Conditions | Citation |
|---|---|---|---|
| Base salary | | | |
| Bonus/incentive | | | |
| Commission | | | |
| Equity/RSUs/options | | | |
| Cash benefits | | | |

### 5. Benefits & Perks

| Benefit | Eligibility | Cost Split | Citation |
|---|---|---|---|
| Health/retirement | | | |
| PTO/leave | | | |
| Expenses/perqs | | | |

### 6. Termination & Severance

| Scenario | Notice | Cause Definition | Severance/Conditions | Citation |
|---|---|---|---|---|
| For cause | | | | |
| Without cause | | | | |
| Resignation | | | | |
| Change in control | | | | |

### 7. Restrictive Covenants

| Covenant | Duration | Geography | Scope | Exceptions | Citation |
|---|---|---|---|---|---|
| Non-compete | | | | | |
| Non-solicit | | | | | |
| Confidentiality | | | | | |
| Non-disparagement | | | | | |

If governing law is specified, add state-specific enforceability notes. Otherwise state: "state-specific enforceability varies."

### 8. IP & Work Product

| Topic | Obligation | Carve-outs | Citation |
|---|---|---|---|
| Assignment of inventions | | | |
| Prior inventions schedule | | | |
| Works outside scope | | | |

### 9. Dispute Resolution

| Mechanism | Rules/Forum | Class Waiver | Fees | Remedies Limits | Citation |
|---|---|---|---|---|---|
| Arbitration/litigation | | | | | |

### 10. Compliance & Statutory Conflicts (Flag Only)

- Minimum wage/overtime classification risks.
- Non-waivable rights (leave, anti-discrimination, whistleblower).
- 409A, golden-parachute, or tax gross-up concerns for executives.

### 11. Risks, Ambiguities & Missing Terms

Bullet list — each item gets a citation or "missing." Flag inconsistent defined terms and cross-reference errors.

### 12. Risk Assessment & Follow-ups

```
RISK LEVEL: Low / Medium / High (brief rationale)
KEY ISSUES: ...
MISSING/UNCLEAR: ...
```

List targeted follow-up questions or documents needed (e.g., equity plan, bonus plan, policy handbook).

## Pitfalls

- **Quantify everything** — dollars, dates, percentages, vesting schedules.
- **Distinguish "silent" vs. "expressly excluded"** — these have different legal weight.
- **Non-competes are state-dependent** — never assume enforceability; flag for jurisdiction review.
- **No legal advice** — flag issues and conflicts only; do not predict outcomes.
