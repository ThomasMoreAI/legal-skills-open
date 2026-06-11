---
name: stock-option-grant
title: Stock Option Grant Agreement
description: Drafts Stock Option Grant Agreements for ISOs or NQSOs under a company's equity incentive plan. Covers vesting, exercise mechanics, termination, tax (IRC §422/§409A), securities compliance, and change-in-control provisions. Use when drafting option grants, equity compensation agreements, or stock option award letters.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/stock-option-grant
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employee-benefits
language: en
---

# Stock Option Grant Agreement

Drafts a binding option grant agreement governing ISO or NQSO issuance, integrated with the company's equity incentive plan.

## Prerequisites

Collect before drafting:

- [ ] Adopted equity incentive plan (with amendments)
- [ ] Board/committee resolution (grant date, share count, exercise price, recipient)
- [ ] Certificate of incorporation + bylaws (authorized shares, stock classes)
- [ ] Recipient's employment/consulting agreement (equity, acceleration, post-termination terms)
- [ ] Cap table context (stockholders' agreement, ROFR/co-sale/drag-along)
- [ ] 409A valuation (private) or closing price (public) establishing FMV at grant date
- [ ] Insider trading / equity admin policies (if any)

## Quick Start

1. Confirm option type: **ISO** (§422) or **NQSO** — tax treatment diverges significantly
2. Verify exercise price meets FMV floor (100% FMV for ISO; 110% for >10% shareholders)
3. Draft agreement sections below in order
4. Cross-check acceleration terms against all existing agreements

## Document Sections

### 1. Caption & Recitals

Include: grant date (from board resolution), company legal name + state, optionee name, plan title with adoption/amendment dates, "Subject to and governed by the Plan" incorporation clause.

### 2. Definitions

| Term | Requirements |
|---|---|
| Option | ISO (§422) or NQSO; if ISO, savings clause converting excess to NQSO |
| Shares | Class of stock (typically common) |
| Continuous Service | Employee/director/consultant; parent/subsidiary service treatment |
| Exercise Price | Per-share price + FMV methodology |
| Vesting Commencement Date | Grant date, hire date, or specified date |
| Cause | Dishonesty, fraud, felony, fiduciary breach, material policy violation |
| Change in Control | Merger, asset sale, stock sale, board change — with threshold percentages |

### 3. Grant Terms

- [ ] Number of shares and exercise price per share
- [ ] ISO: exercise price ≥ 100% FMV (110% for >10% shareholders)
- [ ] NQSO: exercise price ≥ FMV (§409A compliance)
- [ ] Maximum term: 10 years (5 years for >10% shareholder ISOs)

### 4. Vesting Schedule

Standard four-year structure:

```
Cliff:     12 months — 0% before first anniversary
Year 1:    25% on first anniversary of Vesting Commencement Date
Years 2–4: 75% in 36 equal monthly installments
Condition: Continued Service through each vesting date
```

For performance vesting: specify milestones, verification method, certification process.

**Acceleration provisions:**

| Trigger | Type | Effect |
|---|---|---|
| Change in Control alone | Single-trigger | Specify % or full acceleration |
| CiC + qualifying termination (12–18 mo) | Double-trigger | Specify % or full acceleration |
| Death or Disability | Single-trigger | Per plan terms |
| Involuntary w/o Cause (no CiC) | If applicable | Per employment agreement |

Confirm alignment with separate employment/severance/CiC agreements.

### 5. Exercise Procedures

**Payment methods** (include all that apply): cash/check, broker-assisted cashless, net exercise/share withholding, stock swap.

**Post-exercise delivery:** book-entry or certificate; private companies add securities law + stockholders' agreement legends; public companies add lock-up obligations.

### 6. Termination Matrix

| Scenario | Unvested | Vested — Exercise Period |
|---|---|---|
| Cause | Immediate termination | Immediate termination |
| Voluntary resignation | Immediate termination | 30–90 days (not beyond max term) |
| Involuntary w/o Cause | Terminate (unless acceleration) | 90 days (or per agreement) |
| Death | Terminate (unless acceleration) | 12 months; estate/beneficiary exercises |
| Disability | Terminate (unless acceleration) | 12 months |

**Change in Control treatment:**
1. Assumed/substituted → vesting continues (+ acceleration terms)
2. Not assumed → full vesting pre-closing; limited exercise window
3. Cash-out → cancellation for spread payment
4. All CiC provisions must comply with §409A

### 7. Tax Provisions

**NQSO:** Ordinary income at exercise (FMV − exercise price); income + employment tax withholding required; withholding is condition-precedent to exercise.

**ISO:** No ordinary income if holding periods met (2yr from grant + 1yr from exercise); AMT adjustment = spread at exercise; require disqualifying disposition notice to company.

**Reporting:** W-2 (employees), 1099 (consultants), Form 3921 (ISO exercises), Form 3922 (ESPP).

### 8. Securities Law Compliance

- [ ] Unregistered shares; issued under §4(a)(2), Rule 701, or Reg D
- [ ] Investment representations (acquiring for investment, not distribution)
- [ ] Transfer restriction (non-transferable except by will/intestacy)
- [ ] Reference stockholders'/ROFR/co-sale/drag-along agreements
- [ ] §16 officers/directors: Rule 16b-3 compliance

### 9. Administrative Provisions

- [ ] Governing law (state of incorporation)
- [ ] Severability; plan controls over agreement; administrator interpretations final
- [ ] Amendment requires written consent; company may amend unilaterally for §409A/securities/tax compliance
- [ ] Notice mechanics with delivery method + deemed-received timing
- [ ] At-will acknowledgment; data privacy consent
- [ ] International addendum placeholder for non-US optionees

### 10. Execution & Exhibits

**Signatures:** Company authorized officer + optionee, with dates.

**Optionee acknowledgment:** receipt of plan document, opportunity to consult advisors, understanding option is subject to agreement and plan.

**Exhibit A — Grant Summary:**

```
Grant Date:                [DATE]
Option Shares:             [NUMBER]
Exercise Price Per Share:  $[PRICE]
Option Type:               [ISO / NQSO]
Vesting Commencement:      [DATE]
Vesting Schedule:          [CLIFF + MONTHLY/QUARTERLY]
Expiration Date:           [DATE]
```

## Critical Rules

- **ISO $100K limit:** Annual vesting cap of $100,000 FMV (measured at grant) first exercisable per year; excess auto-converts to NQSO [IRC §422(d)]
- **§409A floor:** NQSO exercise price must never be below FMV at grant — discounted options trigger immediate taxation + 20% penalty
- **Private company valuation:** Require current 409A valuation; safe harbor = independent appraisal within 12 months
- **>10% shareholder ISOs:** 110% FMV exercise price + 5-year max term [IRC §422(c)(5)]
- **Tax disclaimer:** Do not draft tax advice as legal advice — include disclaimer directing optionee to personal tax advisor
- **Preferred stock check:** If company has outstanding preferred, confirm common stock class and any anti-dilution or protective provisions affecting option shares
- **Acceleration conflicts:** Cross-check all acceleration terms against existing agreements
