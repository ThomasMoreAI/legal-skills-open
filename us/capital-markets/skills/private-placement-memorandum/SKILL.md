---
name: private-placement-memorandum
title: Private Placement Memorandum (PPM)
description: Drafts U.S. Regulation D Private Placement Memoranda (PPMs) with required legends, risk factors, capitalization, securities terms, and subscription procedures. Trigger when drafting a PPM, preparing a Reg D (506(b) or 506(c)) offering, building accredited-investor disclosure, or structuring private placement documents to minimize 10b-5 liability.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/private-placement-memorandum
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: capital-markets
language: en
tags: [corporate, drafting, memo, regulatory, transactional]
---

# Private Placement Memorandum (PPM)

Draft a Regulation D-compliant PPM delivering full-and-fair disclosure with a defensible liability record.

## Quick Start

Collect before drafting:

1. **Issuer profile** — legal name, formation state/date, addresses, prior names/reorgs.
2. **Offering terms** — security type, price/valuation, min/max raise, use of proceeds, timeline, escrow.
3. **Cap table** — authorized/outstanding classes, options/warrants/convertibles, major holders.
4. **Financials** — historical statements, burn, runway, audit status.
5. **Business materials** — deck, plan, key contracts, IP, regulatory posture.
6. **Management bios** — roles, tenure, relevant history.
7. **Compliance inputs** — 506(b) vs 506(c), investor eligibility plan, blue sky scope.

## Core Workflow

### 1. Determine Exemption

| Factor | 506(b) | 506(c) |
|---|---|---|
| General solicitation | Prohibited | Permitted |
| Investors | Accredited + ≤35 sophisticated non-accredited | Accredited only |
| Verification | Reasonable belief | Reasonable steps to verify |
| Disclosure | Enhanced if non-accredited present | Accredited-only package |

Record the exemption choice and its disclosure implications in the PPM.

### 2. Intake & Gap Log

Audit available documents against required inputs:
- Governing docs (charter, bylaws/operating agreement, investor rights, ROFR/co-sale)
- Security terms (dividend/interest, liquidation, conversion, voting, protective provisions)
- Material contracts (top customers/suppliers, IP licenses, debt)
- Litigation/regulatory (claims, investigations, sanctions)
- Financials (last 2–3 years or since inception; audited vs unaudited)

Track gaps in a single table:

| Section | Missing Data | Source | Owner | Deadline |
|---|---|---|---|---|

### 3. Cover Page + Legends

Required elements:
- Issuer name, security type, max amount, date
- **Confidentiality legend** — restrict distribution; require return/destroy
- **Securities legend** — not registered under the 1933 Act or state laws; offered under exemptions; no government approval
- **Transfer restrictions** — restricted securities; no public market; must hold indefinitely

### 4. Executive Summary

Structured fields: issuer identity and state, offering terms (security, valuation, min/max, closings, escrow), key investor rights (dividend, liquidation preference, conversion, voting), top 3–5 use-of-proceeds categories with percentages, 3–5 highest-impact risks, investor eligibility and verification approach.

### 5. Risk Factors

Minimum categories — each with bold heading and 2–5 sentences (what, why material, consequence):
- Financial/capital (losses, burn, dilution)
- Business/market (adoption, competition, market assumptions)
- Regulatory/compliance (licensing, investigations)
- Technology/IP (development risk, obsolescence, disputes)
- Key personnel (dependence, recruiting)
- Customer/supplier concentration
- Securities-specific (illiquidity, transfer limits, no dividends, management discretion)

### 6. Use of Proceeds

| Category | Min Raise | Max Raise | Description |
|---|---|---|---|
| Product/Engineering | $ | $ | Milestones, hires, infra |
| Sales/Marketing | $ | $ | Channels, headcount |
| Working Capital | $ | $ | Ops, inventory, receivables |
| Debt Repayment | $ | $ | Lender, rate, maturity |
| Fees/Offering Costs | $ | $ | Legal, accounting, escrow |

Include discretion disclaimer and conditional allocations if max not reached.

### 7. Business Description

Cover: company history/milestones, products/services and roadmap, market size and customer profile, competitive landscape, go-to-market, operations/supply chain, regulatory framework, intellectual property.

### 8. Management & Board

| Name | Role | Tenure | Relevant Experience | Education | Equity/Comp |
|---|---|---|---|---|---|

### 9. Capitalization

Provide pre-offering cap table, post-offering cap table (min and max scenarios), fully diluted schedule, and notes on options/warrants/convertibles with conversion assumptions.

### 10. Securities Terms

Term-sheet format covering: dividends/interest, liquidation preference (multiple, participation, deemed liquidation events), conversion (ratio, adjustments, auto-triggers), voting/protective provisions, redemption, transfer restrictions (ROFR, co-sale, lock-ups, legends), registration rights, preemptive rights, information and board rights.

### 11. Distribution & Subscription

- Direct vs placement agent; fees
- Offering timeline, closings, escrow terms
- Form D filing within 15 days of first sale [VERIFY]
- State blue sky notice filings and timing [VERIFY]
- Subscription steps: (1) review PPM + exhibits → (2) execute subscription agreement + questionnaire → (3) accredited verification if 506(c) → (4) wire funds → (5) acceptance notice and issuance

### 12. Legal Matters & Disclaimers

Counsel and accountant identification, audit status disclaimer, forward-looking statements cautionary language, no-update obligation.

### 13. Investor Qualifications

- Accredited investor definition with current thresholds [VERIFY]
- Net worth test excludes primary residence [VERIFY]
- Sophistication and illiquidity warning
- Company discretion to reject subscriptions

## Final QA Checklist

- [ ] Defined terms consistent throughout
- [ ] Numbers reconcile across all sections
- [ ] Risk factors match issuer-specific facts
- [ ] All three legends present and prominent
- [ ] No general solicitation language if 506(b)
- [ ] Exhibits attached and cross-referenced
- [ ] All `[VERIFY]` items confirmed against current law

## Pitfalls

- **No puffery** — neutral language only; no unsupported projections or absolute guarantees.
- **Tailor risks** — issuer-specific; never use generic boilerplate lists.
- **Gap discipline** — every missing item goes in the Gap Log; do not draft around holes.
- **Blue sky variance** — confirm state-specific notice filing requirements and deadlines.
- **Mark uncertainties** — tag any unconfirmed citations or thresholds with `[VERIFY]`.
