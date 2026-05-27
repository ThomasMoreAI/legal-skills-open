---
name: bankruptcy-interest-calculation
title: Bankruptcy Claim Interest Calculation
description: Calculates pre-petition interest for bankruptcy proofs of claim and produces a filing-ready worksheet. Covers rate source hierarchy, day-count conventions, simple interest formulas, post-petition rules under 11 U.S.C. § 506(b), and fee inclusion standards. Use when preparing interest components of a proof of claim, calculating creditor claim amounts, or verifying interest calculations.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/bankruptcy-interest-calculation
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: bankruptcy
language: en
---

# Bankruptcy Claim Interest Calculation

Calculates pre-petition interest and generates a defensible worksheet for attachment to a proof of claim.

## Prerequisites

1. Principal balance as of last payment or accrual date
2. Annual interest rate and governing source (contract, judgment, or statute)
3. Last payment date and petition date
4. Underlying agreement (for day-count convention and fee authorization)

## Quick Start

```
Per Diem = (Principal × Annual Rate) ÷ Day-Count Divisor
Pre-Petition Interest = Per Diem × Days (Last Payment → Petition Date)
```

Use the day-count divisor required by the contract or governing standard (e.g., 365 or 360).

## Core Workflow

### 1. Determine Interest Rate

| Priority | Source | Notes |
|----------|--------|-------|
| 1 | Contract rate | Express provision in loan agreement or note |
| 2 | Judgment rate | Rate from pre-petition judgment |
| 3 | State statutory | Applicable state prejudgment rate |
| 4 | Federal rate | 28 U.S.C. § 1961 (Treasury bill rate) |

Cite the source in the proof of claim with section number or statutory citation.

### 2. Select Day-Count Convention

| Convention | Divisor | Typical Use |
|------------|---------|-------------|
| Actual/365 | 365 | Consumer loans, mortgages (default if unspecified) |
| Actual/360 | 360 | Commercial loans, credit facilities |
| 30/360 | 360 (30-day months) | Bonds, commercial paper |

Follow the contract. Default to Actual/365 only when unspecified.

### 3. Calculate Interest

Simple interest (most common for bankruptcy claims):

```
Per Diem = (Principal × Annual Rate) ÷ Day-Count Divisor
Interest = Per Diem × Actual Days in Accrual Period
Total Claim = Principal + Interest + Authorized Charges
```

### 4. Apply Post-Petition Rules

| Claim Type | Post-Petition Interest? |
|------------|------------------------|
| Unsecured | No — stop at petition date (exception: solvent-debtor cases) |
| Secured (oversecured) | Yes — under § 506(b), to extent of equity cushion |
| Secured (undersecured) | No |
| Priority | No |

### 5. Verify Additional Charges

**Late fees** — include only if all apply:
- [ ] Contract expressly authorizes (cite section)
- [ ] Assessed pre-petition
- [ ] Not punitive or unconscionable

**Attorney fees** — include only if:
- [ ] Contract fee-shifting provision or statutory authorization
- [ ] Itemized statement attached (dates, hours, rates, descriptions)
- [ ] Pre-petition only; post-petition collection fees excluded

### 6. Complete Worksheet

```
═══════════════════════════════════════════════════════
            INTEREST CALCULATION WORKSHEET
Case: [Debtor Name], Case No. [XX-XXXXX]
Creditor: [Creditor Name]   Account No.: [Number]
═══════════════════════════════════════════════════════

PRINCIPAL
  Original Debt Amount:                      $__________
  Less: Payments Received:                  ($__________)
  Principal Balance as of [Last Pmt Date]:   $__________

INTEREST
  Principal Balance:                         $__________
  Annual Interest Rate:                      __________%
  Rate Source: [ ] Contract §__ [ ] Judgment [ ] Statutory [ ] Federal
  Accrual: [Last Pmt Date] → [Petition Date] = ____ days
  Day-Count: [ ] Actual/365  [ ] Actual/360  [ ] 30/360
  Per Diem = ($______ × ____%) ÷ _____ =    $__________
  Interest = $______ × ____ days =           $__________

OTHER CHARGES
  Late Fees (Contract §__):                  $__________
  NSF/Returned Check Fees:                   $__________
  Attorney Fees (see itemization):           $__________
  Other: ______________________:             $__________

CLAIM SUMMARY
  Principal:                                 $__________
  Pre-Petition Interest:                     $__________
  Other Charges:                             $__________
───────────────────────────────────────────────────────
  TOTAL CLAIM AS OF PETITION DATE:           $__________
═══════════════════════════════════════════════════════
Prepared by: __________________  Date: _______________
```

## Common Pitfalls

| Mistake | Fix |
|---------|-----|
| Post-petition interest on unsecured claim | Stop accrual at petition date |
| Wrong day-count divisor | Follow contract; default Actual/365 |
| Compounding on simple-interest contract | Match contract methodology exactly |
| Unauthorized late/attorney fees | Only include contractually or statutorily permitted charges |
| Using original loan amount as principal | Use balance after last credited payment |
| Missing rate citation | Always cite contract section or statute — unsupported rates invite objection |

Attach supporting documentation: rate source excerpt, payment history, fee authorization clause.

## Key Authorities

- **11 U.S.C. § 502(b)** — Allowance of claims; interest limitations
- **11 U.S.C. § 506(b)** — Post-petition interest for oversecured creditors
- **28 U.S.C. § 1961** — Federal post-judgment interest rate
