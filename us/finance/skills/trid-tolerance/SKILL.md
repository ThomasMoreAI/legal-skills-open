---
name: trid-tolerance
title: TRID Tolerance
description: Classifies closing costs into zero, 10% cumulative, and unlimited tolerance buckets under 12 CFR § 1026.19(e)(3). Validates changed circumstances for revised Loan Estimates and computes cure amounts. Use when reviewing a Closing Disclosure against a Loan Estimate, calculating tolerance variances, determining whether a revised LE is permitted, or computing cure amounts for tolerance violations.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/trid-tolerance
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: finance
language: en
---

# TRID Tolerance

Classifies fees into tolerance buckets, calculates CD-vs-LE variances, validates changed circumstances, and computes cure amounts under Regulation Z.

## Prerequisites

1. Loan Estimate (original + any revised, with dates)
2. Closing Disclosure (final or proposed)
3. Creditor's written list of service providers (shopped vs. unshopped classification)
4. Documentation of any changed circumstances

## Tolerance Categories

### Zero Tolerance (0%) — Cannot Increase

Any increase requires a valid changed circumstance and revised LE.

| Category | Examples |
|---|---|
| Creditor/broker fees | Origination, application, underwriting, processing, discount points, commitment, rate lock |
| Affiliate fees | Any fee paid to lender/broker affiliate (title, appraisal, etc.) |
| Transfer taxes | State/local transfer tax, mansion tax, documentary stamps |
| Services borrower cannot shop for | Appraisal (creditor-selected), credit report, flood determination, tax monitoring |

### 10% Cumulative Tolerance

The **aggregate total** of all 10% items on CD cannot exceed the aggregate total on LE by more than 10%.

| Category | Examples |
|---|---|
| Recording fees | Deed recording, mortgage/deed of trust recording |
| Shopped services (from lender's list) | Lender's title, settlement/closing, title search, survey, notary, pest, attorney |

If borrower chose a provider **not on lender's written list**, that fee shifts to unlimited tolerance.

### Unlimited Tolerance

May change freely; original LE must have been made in good faith.

- Prepaid interest, insurance premiums (homeowner's, flood, MI)
- Initial escrow deposits (taxes, insurance, MI, aggregate adjustment)
- Property costs not required by creditor (HOA, assessments, prepaid taxes)
- Services from a provider **not** on lender's list
- Optional services (home warranty, optional owner's title, elective inspections)

## Variance Calculation

### Zero Tolerance

For each zero-tolerance fee: `Variance = CD Amount − LE Amount`

- Compliant: every variance ≤ $0
- Violation: any positive variance is the cure amount for that fee

### 10% Cumulative Tolerance
