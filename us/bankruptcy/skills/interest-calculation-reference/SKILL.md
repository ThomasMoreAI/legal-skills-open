---
name: interest-calculation-reference
title: Bankruptcy Interest Calculation Reference
description: Calculates and validates pre-petition interest for U.S. bankruptcy creditor proofs of claim. Triggers on "proof of claim", "pre-petition interest", "bankruptcy claim", "interest worksheet", "claim amount", or when drafting, auditing, or objecting to claim filings.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/interest-calculation-reference
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: bankruptcy
language: en
tags: [analysis, checklist, litigation]
---

# Bankruptcy Interest Calculation Reference

Workflow for pre-petition interest calculations and charge inclusion decisions on creditor proofs of claim.

## Prerequisites

Gather before starting:
- Petition date and case number
- Governing loan/credit documents
- Chronological payment history and balance ledger
- Contract or judgment terms (rate, accrual method)
- State prejudgment statutory rate (if no contract/judgment rate)
- Collateral valuation and lien status (secured claims only)
- Fee provisions and statutory fee authorities
- Verified date-diff method (actual calendar days)

## Quick Start

1. Collect core inputs (principal, rate, dates, day-count basis).
2. Determine rate source using priority hierarchy.
3. Calculate pre-petition interest using the formula.
4. Apply charge inclusion gate to fees.
5. Assemble worksheet and run validation checklist.

## Core Inputs

| Field | Capture |
|---|---|
| Principal Balance | Outstanding principal as of last payment or cutoff |
| Last Payment/Accrual Date | Date of last payment or latest principal application |
| Petition Date | Filing date |
| Annual Rate | Decimal or percentage |
| Rate Source | Contract / Judgment / State statutory / Federal |
| Day-Count Basis | 365, 360, or 30/360 |
| Claim Type | Unsecured, Secured, Priority |
| Charges Included | Late fees, NSF fees, attorney fees, other |

## Formulas

- `Pre-petition Interest = Principal × Rate × (Accrual Days ÷ Day-Count-Basis)`
- `Per Diem = (Principal × Rate) ÷ Day-Count-Basis`
- `Total Claim = Principal + Pre-petition Interest + Allowed Other Charges`

## Rate Source Priority

| Priority | Source | Rule |
|---|---|---|
| 1 | Contract | Exact contractual rate and methodology |
| 2 | Judgment | Judgment rate for pre-petition judgment claims |
| 3 | State statutory | Applicable state prejudgment rate if no higher source |
| 4 | Federal §1961 | Only when judgment-rate path designates it as fallback |

## Post-Petition Interest Rules

| Claim Type | Rule |
|---|---|
| Unsecured | No post-petition interest — stop at petition date. Solvent-debtor exception only if affirmatively supported [VERIFY] |
| Secured | Only if oversecured under §506(b); limited by equity cushion |
| Priority | Usually none — confirm statutory priority language |

## Charge Inclusion Gate

Each charge must be: (1) contract- or statute-authorized, (2) accrued/assessed pre-petition, and (3) documented.

- **Late/penalty fees** — must be reasonable and non-punitive
- **NSF/returned-item fees** — must be actually assessed pre-petition
- **Attorney fees** — must have contract or statutory authorization
- Attach supporting documentation to every charge line item

## Worksheet Template

```text
BANKRUPTCY INTEREST CALCULATION WORKSHEET
Debtor: ____________   Case No.: ____________
Creditor: ____________  Account No.: __________

1) Principal
   Original principal:                    $ ________
   Payments to cutoff:                   -$ ________
   Principal as of [Accrual Date]:        $ ________

2) Interest
   Annual rate: ________%
   Rate source: [ ] Contract [ ] Judgment [ ] State [ ] Federal
   Day-count:   [ ] Actual/365 [ ] Actual/360 [ ] 30/360
   Accrual period: [From] __ / [To] __ / Days ____
   Per diem:                              $ ________
   Pre-petition interest:                 $ ________

3) Other Charges (only if supported)
   Late fees:                             $ ________
   NSF/other fees:                        $ ________
   Attorney fees (pre-petition):          $ ________
   Other allowed charges:                 $ ________
   Charges total:                         $ ________

4) Claim Summary
   Principal:                             $ ________
   Pre-petition interest:                 $ ________
   Other charges:                         $ ________
   TOTAL CLAIM AT PETITION:               $ ________

Documentation: [ ] Rate clause [ ] Payment ledger
[ ] Day-count rationale [ ] Charge authorization [ ] Signature/date
```

## Validation Checklist

Run before filing:

| Error | Fix |
|---|---|
| Wrong principal baseline | Reconcile to balance after last credited payment |
| Wrong day-count basis | Use contract or documented basis |
| Wrong compounding method | Match contract; default to simple interest |
| Unauthorized fees included | Remove; note authority required |
| Missing rate source | Document statute, contract clause, or judgment paragraph |
| Interest calculated past petition date | Cap unsecured/general claims at petition date |

## Pitfalls

- Convert percentages to decimals only inside formulas; preserve units elsewhere.
- Never mix post-petition accrual into pre-petition totals.
- Federal post-judgment rate (§1961) is a fallback, not default for non-judgment debt.
- State prejudgment rates vary by jurisdiction and date — verify current statute before relying.
- Flag uncertain statutory questions (e.g., solvent-debtor treatment) with [VERIFY] and venue-specific authority.

## Cross-References

- `@bankruptcy-proof-of-claim`
- `@bankruptcy-collateral-valuation-reference`
- `@bankruptcy-objection-to-proof-of-claim`
- `@commercial-loan-analysis`

## Key Statutes

- 11 U.S.C. §502(b)(2) — unmatured interest
- 11 U.S.C. §506(b) — post-petition interest (oversecured)
- 28 U.S.C. §1961 — post-judgment interest
- Applicable state prejudgment interest statute (verify per jurisdiction)

---

**Key changes made:**

- **Frontmatter**: Tightened description to lead with what it does and include clear trigger guidance in third person
- **Structure**: Added Quick Start section for rapid orientation; reorganized from numbered "Output Structure / Process" subsections into named semantic sections
- **Conciseness**: Removed the redundant general `Interest` formula (kept only the pre-petition variant), collapsed the three-column post-petition table to two columns, condensed the Guidelines section into a focused Pitfalls list
- **Worksheet**: Streamlined — removed decorative separator lines, compressed the documentation checklist to a single line
- **References → Key Statutes**: Renamed for clarity and brevity
- **All domain accuracy preserved**: Rate priority hierarchy, §506(b) rules, charge gate logic, validation checklist, and [VERIFY] flags are intact
