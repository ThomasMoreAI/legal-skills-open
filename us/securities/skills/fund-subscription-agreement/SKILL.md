---
name: fund-subscription-agreement
title: Fund Subscription Agreement
description: 'Drafts U.S. investment fund subscription agreements aligned to PPM/LPA terms and securities law compliance. Use when preparing subscription documents for private equity, venture capital, hedge, real estate, or other private funds. Covers accredited investor reps, transfer restrictions, risk acknowledgments, KYC/AML conditions, and acceptance mechanics. Trigger: subscription agreement, investor questionnaire, PPM, LPA, accredited investor, Reg D, capital commitment.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/fund-subscription-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: securities
language: en
---

# Fund Subscription Agreement

Drafts a fund subscription agreement consistent with offering documents and U.S. private offering compliance (Reg D).

## Prerequisites

1. **Formation docs**: PPM, LPA/LLC agreement, GP/manager entity details, side letter policy
2. **Offering terms**: classes/series, minimums, pricing, closings, acceptance authority, capital call mechanics
3. **Investor data**: legal name, entity type, address, tax status, signatory authority
4. **Compliance inputs**: KYC/AML checklist, W-9/W-8, accreditation evidence, OFAC screening status
5. **Governing law** and dispute forum preferences
6. **Signature method**: wet ink or e-sign; entity signature block requirements

## Quick Start

1. Collect intake fields (see table below)
2. Mirror all terminology and definitions from the PPM and LPA/LLC agreement
3. Draft sections in document outline order
4. Tag unconfirmed statutory citations with `[VERIFY]`
5. Attach required exhibits

## Intake Fields

| Field | Required | Source |
|---|---|---|
| Fund legal name, entity type, jurisdiction | Yes | Formation docs |
| Manager/GP name and address | Yes | Formation docs |
| Offering class/series (rights, fees) | Yes | PPM |
| Minimum subscription (waiver authority) | Yes | PPM |
| Subscription amount (USD, units/shares) | Yes | Investor input |
| Pricing mechanics (NAV date, unit price) | Yes | PPM |
| Acceptance authority (GP/manager/committee) | Yes | LPA/LLC |
| Capital calls (drawdown schedule, notice) | If applicable | LPA/LLC |
| Transfer restrictions (consent, lockups) | Yes | LPA/LLC |
| Governing law, forum | Yes | Client preference |

## Document Outline

1. Parties and Recitals
2. Definitions (align to fund docs)
3. Subscription Terms
4. Acceptance and Admission
5. Investor Representations and Warranties
6. Risk Acknowledgments
7. KYC/AML and Tax Compliance
8. Conditions Precedent
9. Payment Mechanics and Closing
10. Transfer Restrictions
11. Miscellaneous (notices, amendments, assignment, integration, severability, waiver)
12. Signature Blocks and Exhibits

## Core Sections

### Subscription Terms

- Subscription amount in USD; number and class of units/shares
- Price per unit/share and valuation date
- Commitment amount and drawdown structure (if applicable)
- Minimums, maximums, oversubscription handling
- Fund right to reject or reduce; binding only upon written acceptance

### Investor Representations

- Accredited investor status under Regulation D `[VERIFY]`
- Investment intent; no distribution plan
- Securities unregistered; transfer restrictions acknowledged
- Illiquidity and total loss risk accepted
- Sophistication; reliance on own advisors
- Authority and capacity to sign and perform
- No disqualifying events for private offerings `[VERIFY]`
- Source of funds lawful; not from prohibited activities

### Risk Acknowledgments

- Market/strategy risk; potential loss of entire investment
- Illiquidity, lockup, transfer limits
- Dependence on manager/GP and key persons
- Conflicts of interest and related-party transactions
- Regulatory, tax, and valuation uncertainty

### Conditions Precedent

- Completed and accurate subscription documents
- KYC/AML and OFAC clearance
- W-9/W-8 and tax certifications received
- Accreditation verification (if required by offering)
- Written acceptance by GP/manager

### Payment Mechanics

- Method: wire, check, or in-kind (if permitted)
- Wire instructions and payment deadline
- Failed payment / insufficient funds treatment
- Admission timing: on acceptance or at closing
- Confirmation of ownership interest delivery

### Exhibits

- Investor Questionnaire
- Accredited Investor Verification (if used)
- Beneficial Ownership Certification (if required) `[VERIFY]`
- Tax Forms (W-9/W-8)
- Entity Authority Certificate or incumbency

## Pitfalls and Checks

- **Never contradict fund docs**: transfer restrictions and admission criteria must match the LPA/LLC
- **Written acceptance required**: no admission without GP/manager written acceptance
- **E-sign**: confirm permitted; align to ESIGN/UETA
- **Broker-dealers**: if involved, add compliance representations `[VERIFY]`
- **Blue sky**: flag jurisdiction-specific filing or exemption requirements
- **`[VERIFY]` tag**: use on any statutory or rule citation not confirmed by source documents

---

**Key changes from the original:**

- **Removed `tags`** from frontmatter (not part of the spec's required fields)
- **Tightened description** — third-person, includes trigger keywords, stays under 1024 chars
- **Added Quick Start** section for immediate orientation
- **Consolidated the intake table** — removed the Notes column, folded key notes into the Field column as parentheticals for token savings
- **Renamed "Output Structure / Process"** to flat, scannable headings (`Core Sections`, `Document Outline`)
- **Removed the redundant "Subscription Terms Block" / "Investor Representations Checklist"** heading patterns — replaced with concise subsections under `Core Sections`
- **Renamed "Guidelines"** to **"Pitfalls and Checks"** — bolded the key constraint in each bullet for quick scanning
- **Reduced overall line count** from 128 to ~100 while preserving every legal requirement and checklist item
