---
name: transactional
title: Transactional Practice
description: Routes and governs transactional legal work—contracts, deals, and business formations. Covers M&A, real estate, financing, franchise, employment, asset purchase, estate planning, IP licensing, and commercial leasing. Triggers on any transactional matter, deal structuring, contract drafting, or entity formation task.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/transactional
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
tags: [research, transactional]
---

# Transactional Practice

Root skill for structuring, negotiating, and documenting business deals and agreements. Route to a sub-practice skill when one exists; otherwise apply the principles below.

## Quick Start

1. Identify the transaction type from the routing table below.
2. Confirm governing law, choice of forum, and notice provisions.
3. Flag any regulatory approvals or third-party consents required for closing.
4. Apply core drafting principles throughout.

## Sub-Practice Routing

| Area | Typical Work Product |
|---|---|
| Mergers & Acquisitions | LOIs, purchase agreements, disclosure schedules |
| Commercial Real Estate | Purchase/sale agreements, due diligence reports |
| Residential Real Estate | Contracts of sale, title review, closing documents |
| Loan & Financing | Loan agreements, promissory notes, security instruments |
| Franchise Agreements | FDDs, franchise agreements, area development agreements |
| Employment & Consulting | Offer letters, employment agreements, consulting agreements |
| Asset Purchase | APAs, bills of sale, assignment/assumption agreements |
| Estate Planning | Wills, trusts, powers of attorney, beneficiary designations |
| IP Licensing | License agreements, royalty schedules, assignment agreements |
| Commercial Leasing | Lease agreements, amendments, subleases, estoppels |

## Core Drafting Principles

- **Precision over prose** — eliminate ambiguity; define all key terms
- **Risk allocation** — assign every material risk via reps, warranties, indemnities, or insurance
- **Diligence integration** — draft reflects findings; flag open items
- **Business alignment** — structure serves commercial goals, not just legal defensibility
- **Regulatory compliance** — confirm federal, state, and industry-specific requirements before drafting

## Pitfalls

- Omitting governing law or forum selection until late drafts
- Failing to surface required regulatory approvals or third-party consents
- Drafting without completed diligence—flag gaps explicitly with `[VERIFY]`
- When no sub-skill exists, still flag jurisdiction-specific requirements

---

Key changes from the original:

- **Description**: tightened to third-person with explicit trigger guidance ("Triggers on…")
- **Added Quick Start**: 4-step workflow so agents know the entry path immediately
- **Renamed "Sub-Practice Areas" → "Sub-Practice Routing"**: clarifies this is a dispatch table
- **Trimmed drafting principles**: removed filler words while keeping the same five tenets
- **Replaced "Guidelines" → "Pitfalls"**: reframed as failure modes to watch for, which is more actionable than generic guidelines
- **Added `[VERIFY]` convention**: aligns with the codebase pattern for flagging items needing attorney review
