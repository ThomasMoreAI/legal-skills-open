---
name: dip-financing-motion
title: DIP Financing Motion
description: Drafts U.S. bankruptcy DIP financing motions under 11 U.S.C. §§ 361-364, including superpriority claims, priming liens, and adequate protection. Use when preparing a DIP financing motion, Section 364(c)/(d) motion, priming lien motion, or emergency post-petition financing request.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/dip-financing-motion
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: bankruptcy
language: en
---

# DIP Financing Motion

Drafts a court-ready motion seeking approval of post-petition financing under the Bankruptcy Code.

## Prerequisites

Gather before drafting:

1. **Caption**: court, district, case number, debtor name(s), chapter, judge, hearing date/time
2. **Facility terms**: lender, size, pricing, maturity, draw conditions, covenants, milestones, defaults
3. **Budget**: 13-week cash flow forecast and sources/uses
4. **Capital structure**: existing secured debt, lien priorities, collateral description, cash collateral status
5. **Adequate protection**: proposed replacement liens, cash payments, equity cushion, reporting
6. **Financing process**: marketing efforts, alternatives considered, why unsecured credit is unavailable
7. **Exhibits**: term sheet or credit agreement, budget, declaration(s), proposed order
8. **Local rules**: judge-specific procedures for emergency relief, notice, and service

## Motion Structure

```
I.    Preliminary Statement / Relief Sought
II.   Jurisdiction, Venue, and Statutory Authority
III.  Background and Need for Financing
IV.   Terms of Proposed DIP Facility
V.    Adequate Protection for Prepetition Secured Parties
VI.   Legal Standard and Argument
VII.  Notice and Hearing
VIII. Conclusion
```

## Relief Sought Matrix

| Relief | Statute | Required Showing | Evidence |
|---|---|---|---|
| Superpriority admin expense | § 364(c)(1) | Unsecured credit unavailable under § 503(b)(1); reasonable terms | Process declaration; term sheet |
| Lien on unencumbered property | § 364(c)(2) | Same + identify unencumbered collateral | Collateral schedule; lien analysis |
| Junior lien on encumbered property | § 364(c)(3) | Same + priority structure | UCC/lien summary; intercreditor terms |
| Priming lien | § 364(d) | Cannot obtain credit otherwise; adequate protection of existing lienholders | Adequate protection package; valuation |

## Required Findings

- [ ] Debtor cannot obtain unsecured credit under § 503(b)(1)
- [ ] DIP terms are fair, reasonable, arm's-length, and in the estate's best interests
- [ ] Adequate protection for existing secured creditors (if primed or subordinated)
- [ ] Financing necessary to preserve going-concern value

## Adequate Protection Tools

| Tool | When Used | Data Needed |
|---|---|---|
| Replacement liens | Collateral base stability | Collateral description; lien order |
| Periodic cash payments | Cash collateral use or priming | Budget items; payment schedule |
| Equity cushion | Oversecured collateral | Valuation support |
| Reporting package | Ongoing monitoring | KPI and variance format |
| Carve-out | Professional fees | Amount; beneficiaries |

## Exhibits

- DIP credit agreement or term sheet
- 13-week cash flow forecast
- CFO/CRO/financial advisor declaration(s)
- Proposed order
- Lien and capital structure summary

## Proposed Order Checklist

- [ ] Facility size and use of proceeds
- [ ] Authorized liens and priorities
- [ ] Adequate protection terms
- [ ] Reporting, milestones, and default remedies
- [ ] Final hearing scheduling / interim relief
- [ ] Service and notice findings

## Pitfalls

- **Priming liens**: do not request unless adequate protection record is concrete and documented.
- **Roll-ups / cross-collateralization**: flag explicitly; provide statutory and case authority. Mark uncertain citations `[VERIFY]`.
- **Statutory references**: cite precisely for every relief request. Mark uncertain citations `[VERIFY]`.
- **Factual assertions**: tie every claim to a declaration or exhibit.
- **Local rules**: verify judge-specific emergency relief standards and notice requirements before filing.
