---
name: cd-tolerance-reference
title: TRID CD Tolerance Reference
description: Guides the agent through TRID tolerance compliance under 12 CFR § 1026.19(e)(3), comparing Closing Disclosure fees to Loan Estimate fees across zero, 10% cumulative, and unlimited tolerance categories. Use when reviewing a CD for tolerance variances, determining whether a revised LE is permitted, calculating cure amounts, or resolving post-closing tolerance violations.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/cd-tolerance-reference
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: finance
language: en
tags: [analysis, policy, regulatory, transactional]
---

# TRID CD Tolerance Reference

Determines whether CD fees comply with TRID tolerance limits set by the most recent valid LE, and calculates any required cure.

## Prerequisites

- Most recent valid LE (original or revised) with line-item fees
- Final CD with line-item fees
- Lender's written list of service providers (classifies shopped services)
- Documentation of any changed circumstances supporting a revised LE

## Tolerance Categories

Authority: 12 CFR § 1026.19(e)(3). Always compare CD fees to the most recent valid LE.

| Category | Rule | Measurement |
|----------|------|-------------|
| Zero | Cannot increase at all | Per item |
| 10% Cumulative | CD category total ≤ LE total × 110% | Aggregate |
| Unlimited | May change freely (good faith at LE required) | None |

## Zero Tolerance (0%)

Any increase from LE to CD is a violation requiring cure.

| Category | Examples |
|----------|---------|
| Creditor/broker fees | Origination, application, underwriting, processing, discount points, commitment, rate lock |
| Affiliate fees | Any fee to entity affiliated with creditor/broker |
| Transfer taxes | State/local transfer taxes, mansion tax, documentary stamps |
| Services borrower cannot shop | Appraisal (creditor-selected), credit report, flood determination, tax monitoring |

Compliant: every item variance ≤ $0. Any positive variance = cure amount.

## 10% Cumulative Tolerance

Measured as **category aggregate**, not per item.

| Category | Examples |
|----------|---------|
| Recording fees | Deed recording, mortgage recording, other recording |
| Shopped services from lender's list | Title policies, title search, settlement/closing fee, notary, survey, pest inspection, settlement attorney |

If borrower chose a provider **not** on lender's written list, that fee moves to unlimited tolerance.

Cure calculation:
- Maximum permitted = LE total × 110%
- Excess = CD total − maximum permitted (if positive)

## Unlimited Tolerance

No cure required. Includes:

- Prepaid interest, insurance premiums (homeowner's, flood, hazard)
- Initial escrow deposits (taxes, insurance, MIP, aggregate adjustment)
- Property costs not required by creditor (prepaid taxes, HOA)
- Services where borrower chose provider off lender's list
- Optional services (home warranty, optional owner's title, non-required inspections)

## Changed Circumstances

A valid changed circumstance permits a revised LE that resets tolerances for **affected fees only**. Per 12 CFR § 1026.19(e)(3)(iv):
- Deliver revised LE within **3 business days** of learning of the change
- At least **4 business days** before consummation

| Type | Examples |
|------|---------|
| Extraordinary event | Natural disaster, war, civil unrest |
| Information inaccuracy | Income/assets differ; property differs from disclosed |
| Previously unavailable info | Title defect, survey encroachment |
| Borrower-requested change | Different product, property, or added borrower |
| Rate lock | Borrower locks after floating |
| LE expiration | Closing delayed beyond 10 business days after LE |

**Invalid reasons:** creditor error, market fluctuation, processing delays, simple underestimates, bad-faith original estimate.

## Cure Requirements

Authority: 12 CFR § 1026.19(f)(2)(v). All within **60 calendar days** after consummation:

1. Refund excess amount to borrower
2. Provide corrected CD reflecting the cure
3. Document cure in loan file

| Category | Maximum Permitted | Cure |
|----------|-------------------|------|
| Zero tolerance | = LE amount | CD − LE (if positive) |
| 10% cumulative | = LE total × 110% | CD total − max permitted (if positive) |

## Pitfalls

| Mistake | Correction |
|---------|-----------|
| Testing 10% items individually | Measure as cumulative category total |
| Applying 10% to affiliate fees | Affiliate fees are zero tolerance |
| Changed circumstance increasing unrelated fees | Only revise affected fees |
| Revised LE > 3 business days after learning of change | Must issue within 3 business days |
| Comparing net fees after credits | Compare **gross** fees; credits don't affect tolerance |
| Missing 60-day cure deadline | Calendar from consummation date |

## Key Rules

- **Seller credits** don't affect tolerance — always compare gross fees
- **Specific lender credits** tied to a fee reduce it for tolerance; **general credits** do not
- **Construction loans:** tolerances apply separately per phase
- **Subordinate financing:** each loan has independent tolerances; no fee-shifting between loans
- Always verify affiliate status — misclassification as 10% item is a common exam finding

## References

- 12 CFR § 1026.19(e)(3) — Tolerance categories
- 12 CFR § 1026.19(e)(3)(iv) — Changed circumstances
- 12 CFR § 1026.19(f)(2)(v) — Cure requirements
- CFPB Official Interpretation, Comments 19(e)(3)(i)-1 through -6
- CFPB Official Interpretation, Comments 19(e)(3)(iv)-1 through -6
- CFPB TRID Small Entity Compliance Guide, Section 7
