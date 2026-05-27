---
name: wrongful-termination-complaint
title: Wrongful Termination Complaint
description: Drafts wrongful termination complaints for employment litigation. Covers at-will exceptions, statutory claims (Title VII, ADA, ADEA, FMLA, state equivalents), public policy violations, and whistleblower protections. Use when drafting or filing a wrongful termination complaint or related employment discharge claim.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/wrongful-termination-complaint
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
tags: [drafting, litigation, pleading]
---

# Wrongful Termination Complaint

Generates a complaint establishing jurisdictional, factual, and legal elements for wrongful termination and related employment claims.

## Prerequisites

Gather before drafting:

1. **Employment details** — employer, title, hire/termination dates, compensation, work location
2. **Termination circumstances** — stated reason, actual events, adverse-action timeline
3. **Protected activity or status** — discrimination basis, whistleblowing, leave exercise, complaint history
4. **Administrative exhaustion** — EEOC/state agency charge number, right-to-sue letter, filing dates
5. **Supporting documents** — employment agreement, handbook, performance reviews, communications, severance offers
6. **Comparator evidence** — similarly situated employees treated differently
7. **Damages** — lost wages/benefits, emotional distress, out-of-pocket costs

## Quick Start

1. Confirm administrative prerequisites are met (exhaustion is jurisdictional for federal claims)
2. Select forum — federal for Title VII/ADA/ADEA; state for state-law or common-law claims
3. Identify applicable causes of action from the menu below
4. Draft using the output structure, pleading each element with factual support

## Output Structure

### 1. Caption and Jurisdiction

- Court selection (federal question, diversity, supplemental jurisdiction)
- Personal jurisdiction and venue
- Administrative exhaustion (charge number, right-to-sue date, timely filing)

### 2. Parties

| Role | Allege |
|---|---|
| Plaintiff | Name, residence, employment dates, position, relevant protected characteristics |
| Corporate defendant | Legal entity, incorporation state, principal place of business |
| Individual defendants | Only if statute permits supervisor liability (jurisdiction-dependent) |

Include successor/alter ego allegations if applicable.

### 3. Factual Allegations

Structure chronologically:

- **Employment relationship** — hiring, duties, performance history, at-will status and any contractual modifications
- **Protected activity/status** triggering the claim
- **Temporal proximity** between protected activity and adverse action
- **Adverse actions** — progressive pattern if applicable
- **Termination** — circumstances and stated reason
- **Pretext indicators** — shifting explanations, policy deviations, comparator treatment

### 4. Damages

| Category | Elements |
|---|---|
| Economic | Back pay, front pay, lost benefits, bonuses |
| Non-economic | Emotional distress, reputational harm |
| Statutory | Liquidated damages, penalties where available |
| Punitive | If willful or malicious conduct is alleged |

### 5. Causes of Action

Select based on facts and jurisdiction. For each, cite the statutory or common-law basis, plead every required element, cross-reference factual paragraphs, and state available relief.

| Claim | Basis | Key Elements |
|---|---|---|
| Title VII discrimination | 42 U.S.C. § 2000e | Race, color, religion, sex, national origin |
| ADA disability discrimination | 42 U.S.C. § 12101 | Qualified individual, reasonable accommodation, interactive process |
| ADEA age discrimination | 29 U.S.C. § 621 | Age 40+, but-for causation |
| FMLA retaliation/interference | 29 U.S.C. § 2601 | Exercise of leave rights, restoration |
| State antidiscrimination | CA FEHA, NY SHRL, etc. | Varies by jurisdiction |
| Public policy wrongful discharge | Common law | Termination violating clear public policy mandate |
| Whistleblower retaliation | SOX, FCA, or state statutes | Protected disclosure, causal connection |
| Breach of implied contract | Common law | Handbook promises, oral assurances, progressive discipline policy |
| Covenant of good faith breach | Common law (limited jurisdictions) | Bad faith termination to deny earned benefits |
| IIED | Common law | Extreme and outrageous conduct |

### 6. Prayer for Relief

- Reinstatement or front pay in lieu
- Back pay with prejudgment interest
- Compensatory damages (emotional distress)
- Punitive or liquidated damages where available
- Attorney's fees and costs (cite statutory basis)
- Injunctive relief (policy changes, training)
- Jury trial demand

## Pitfalls and Checks

- **Administrative exhaustion** — Failure is jurisdictional for federal claims; verify charge and right-to-sue letter before filing
- **Pleading standard** — FRCP 9(b) specificity for fraud-based claims; notice pleading for others
- **Temporal proximity** — Critical for retaliation claims; always allege explicitly
- **At-will presumption** — Plead around it with specific contractual or statutory exceptions
- **Damages caps** — Title VII caps vary by employer size; ADEA has no compensatory damages
- **Federal vs. state claims** — Decide whether to plead together (supplemental jurisdiction) or separately

## Troubleshooting

| Problem | Resolution |
|---|---|
| No right-to-sue letter | File EEOC charge first; request letter after 180 days if no determination |
| Individual defendant liability unclear | Check jurisdiction — Title VII does not allow individual liability; many state statutes do |
| At-will defense anticipated | Strengthen implied contract, public policy, or statutory exception allegations |
| Statute of limitations concern | Verify per-claim deadlines; relation-back doctrine may apply to amended complaints |

---

**Key changes from original:**

- **Description** tightened and made third-person with explicit trigger guidance
- **Added Quick Start** section for immediate orientation per spec
- **Added Troubleshooting** table per spec requirements
- **Converted Causes of Action** from numbered list to table — more scannable, fewer tokens
- **Converted Damages** from nested bullets to table
- **Converted Party Allegations** to table format
- **Renamed Guidelines to Pitfalls and Checks** — more actionable framing
- **Removed redundant prose** (e.g., the "For each cause of action" instructions are now a single line above the table)
- **Numbered output sections** for clearer sequencing
- **Reduced line count** from 102 to ~95 lines while preserving all legal substance
