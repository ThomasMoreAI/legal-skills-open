---
name: reg-bi-policy
title: Suitability and Best Interest Policy (Reg BI)
description: Drafts board-ready Suitability and Best Interest policies for broker-dealers under FINRA Rule 2111 and SEC Regulation Best Interest (Reg BI). Covers the four Reg BI component obligations, suitability framework, Form CRS integration, supervision, and recordkeeping. Use when drafting Reg BI compliance policies, suitability procedures, or best interest obligation frameworks for financial services firms.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/reg-bi-policy
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: securities
language: en
---

# Suitability and Best Interest Policy (Reg BI)

Drafts a board-ready compliance policy governing broker-dealer recommendations to retail customers under FINRA Rule 2111 and SEC Reg BI (17 CFR 240.15l-1).

## Prerequisites

Gather before drafting:

- **Firm details** — business model, product offerings, compensation structures, org chart
- **Existing compliance materials** — current policies, manuals, supervisory procedures
- **Product inventory** — securities, strategies, and product types offered
- **Compensation arrangements** — all structures, revenue-sharing, third-party payments

## Quick Start

Draft a formal policy with hierarchical section numbering (1.1, 1.2, etc.) suitable for board approval. Include a definitions section for key terms (retail customer, investment profile, associated person, etc.). Use the section order below.

## Policy Sections

### 1. Policy Statement

- Commitment to FINRA Rule 2111 and Reg BI compliance
- Integration with firm's broader compliance framework
- Effective date and review cycle

### 2. FINRA Rule 2111 Suitability Framework

| Component | Scope | Key Requirements |
|-----------|-------|-----------------|
| **Reasonable-Basis** | Product/strategy | Due diligence on risks, rewards, costs, complexity, liquidity, volatility; written approval; enhanced review for complex/novel products |
| **Customer-Specific** | Individual customer | Match to investment profile: age, finances, tax status, objectives, experience, time horizon, liquidity needs, risk tolerance |
| **Quantitative** | Transaction patterns | Turnover ratios, cost-to-equity ratios, trading frequency; customer-initiated vs. recommended; review thresholds |

For customer-specific suitability, also address:
- Minimum information requirements before any recommendation
- Profile update intervals and life-event triggers
- Protocols when customers decline to provide information

### 3. Reg BI Four-Obligation Framework

#### 3a. Disclosure Obligation

Written disclosure before or at time of recommendation, in plain English:

| Category | Content |
|----------|---------|
| Relationship | Capacity (BD vs. advisor), service scope, limitations |
| Costs | Material fees, transaction costs, account-level costs |
| Conflicts | Compensation-driven conflicts, proprietary products, third-party payments |

Include procedures for keeping disclosures current.

#### 3b. Care Obligation

Three-part test for each recommendation:
1. Understand potential risks, rewards, and costs
2. Reasonable basis it could benefit at least some retail customers
3. Reasonable basis it is in **this** customer's best interest given their profile

Require a **reasonably available alternatives analysis** — evaluate less costly, less complex, or lower-risk alternatives meeting the same objectives. Document the analytical framework.

#### 3c. Conflict of Interest Obligation

Systematic conflict identification:
- [ ] Differential compensation by product
- [ ] Sales contests, bonuses, special compensation
- [ ] Proprietary/affiliate products
- [ ] Third-party payments and revenue sharing
- [ ] Principal trading

For each conflict: disclose + mitigate, or eliminate. Mitigation includes compensation restructuring, supervisory review layers, product limitations.

#### 3d. Compliance Obligation

- CCO or designated senior officer ownership
- **Training**: initial (before any recommendations) + ongoing CE (regulatory updates, new products, enforcement lessons)
- **Supervisory review**: pre-approval where applicable, post-trade surveillance, periodic account audits, disclosure compliance testing
- Escalation and disciplinary procedures

### 4. Form CRS Integration

- Deliver before or at earliest of: recommendation, account type recommendation, or account opening
- Required content per 17 CFR 240.17a-14 `[VERIFY]` and 17 CFR 279.2 `[VERIFY]`: relationships/services, fees/costs/conflicts, standard of conduct, disciplinary history, how to get more info
- File amendments within 30 days of material inaccuracy; annual review minimum
- Form CRS supplements but does not replace Reg BI Disclosure Obligation

### 5. Documentation and Recordkeeping

Per-recommendation checklist:
- [ ] Date, substance, and basis of recommendation
- [ ] Associated person identity
- [ ] Current customer investment profile
- [ ] Reasonable-basis and customer-specific analysis
- [ ] Alternatives considered
- [ ] Disclosures provided
- [ ] Conflicts identified and addressed
- [ ] Supervisory review/approval

Retention: 6 years minimum per SEC Rule 17a-4; first 2 years in easily accessible location. Index for examination retrieval.

### 6. Supervision and Enforcement

- Define roles: line supervisors, compliance department, senior management, board
- Consequences scaled to severity, intent, customer harm, pattern, history
- Remediation: enhanced supervision, retraining, restitution, policy revision
- Customer complaint and regulatory inquiry handling procedures

## Pitfalls and Checks

- Mark uncertain regulatory citations with `[VERIFY]` — always verify against current rule text
- Tailor thresholds and governance to firm size and complexity
- Frame as compliance policy template requiring firm counsel review — not legal advice
- Address both dual-registrant and standalone BD scenarios where applicable
- Jurisdiction is U.S. federal (SEC/FINRA); note state blue sky requirements may apply

---

**Key changes made:**
- Removed non-standard `tags` frontmatter field
- Tightened the `description` while preserving trigger keywords
- Replaced verbose "Output Structure" heading with "Quick Start" + "Policy Sections" structure matching the best-practices template
- Renamed "Guidelines" to "Pitfalls and Checks" for alignment with the skill format
- Trimmed redundant prose throughout (e.g., collapsed verbose table cells, shortened retention language, condensed Compliance Obligation into inline bold labels)
- Reduced from 131 lines to ~107 lines while preserving all substantive legal content
