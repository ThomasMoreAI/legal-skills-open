# Example: $5,000 Distribution with $4,000 Qualified, $1,000 Non-Qualified

A mixed case where the user has a partial non-QME distribution. Demonstrates the taxable amount calculation, the 20% additional tax for an under-65 user, and the impact on Schedule 1 + Schedule 2.

## The filer

- **Name**: Marcus Tate
- **Tax year**: 2025 (filing in 2026)
- **Age at year-end**: 41
- **Filing status**: Married filing jointly (with spouse Lena)
- **HSA custodian**: Fidelity Investments
- **Insurance**: Family HDHP all year (covers Marcus, Lena, and 2 children)
- **Marcus's HSA contribution in 2025**: $8,550 (the family limit per Rev. Proc. 2024-25)
- **Lena's HSA**: separate; Lena contributed $0 for 2025, so the shared family limit went entirely to Marcus
- **Marcus's W-2 wages**: $95,000

## Inputs gathered

### 1099-SA from Fidelity

```
PAYER: Fidelity Investments, <payer TIN as printed on the form>
RECIPIENT: Marcus Tate, SSN ***-**-XXXX

Box 1 (Gross distribution):                $5,000
Box 2 (Earnings on excess):                $0
Box 3 (Distribution code):                 1 (Normal)
Box 4 (FMV on date of death):              $0
Box 5 (Account type):                      [HSA checked]
```

### Distributions breakdown

| Date | Merchant | Amount | Category | QME? |
|------|----------|--------|----------|------|
| Feb 5 | CVS Pharmacy | $180 | Prescriptions | Yes |
| Mar 12 | Aetna co-pay | $250 | Doctor visit (Marcus) | Yes |
| Apr 22 | Lena's OB-GYN | $400 | Doctor visit (Lena, spouse — qualified) | Yes |
| May 1 | Pediatrician (kids) | $300 | Doctor visits (children, dependents) | Yes |
| Jun 15 | Vitamin Shoppe | $400 | Multivitamins (no Rx, general health) | **No** |
| Jul 3 | Walgreens | $90 | OTC ibuprofen + cold medicine | Yes |
| Aug 28 | Quest Diagnostics | $140 | Lab work | Yes |
| Sep 4 | Premier Fitness | $600 | Gym membership annual fee | **No** |
| Oct 11 | Dental Associates | $1,200 | Family dental cleanings + crown | Yes |
| Nov 22 | Optometrist | $440 | Eye exams + contacts (Marcus + Lena) | Yes |
| Dec 30 | UrgentCare | $1,000 | Marcus emergency room visit | Yes |
| **Total** | | **$5,000** | | $4,000 QME / $1,000 non-QME |

The two non-QME items:
- **Vitamin Shoppe ($400)**: multivitamins purchased without a Letter of Medical Necessity. General health, not QME. (If Marcus had a doctor's prescription for a specific deficiency, an LMN-supported supplement purchase would qualify — but he doesn't.)
- **Premier Fitness ($600)**: gym membership for general fitness. Not QME without a doctor's prescription for a specific medical condition like obesity treatment.

### Substantiation

Marcus has receipts for every transaction. He's clear-eyed about the non-QME portions — he knew when he made those swipes that they weren't qualified, but he wanted the convenience and is prepared to pay tax + penalty on those.

## Step-by-step computation

### Step 1 — Confirm Box 5 = HSA → Form 8889

Yes.

### Step 2 — Box 3 = Code 1 (Normal distribution)

Standard treatment: non-QME portion taxable + 20% additional tax (Marcus is 41, no exception).

### Step 3 — QME total

$4,000 (per the breakdown above).

### Step 4-5 — Form 8889 Part II computation

```
Line 14a (Total distributions):              $5,000
Line 14b (Rollovers):                        $0
Line 14c (14a − 14b):                        $5,000
Line 15 (QME paid using HSA):                $4,000
Line 16 (Taxable distributions, 14c − 15):   $1,000
Line 17a (Exception):                        None (Marcus is 41, not disabled, not died)
Line 17b (20% additional tax, $1,000 × 0.20):$200
```

## The completed Form 8889 Part II draft

```markdown
# Form 8889 Part II — DRAFT for tax year 2025

## 1099-SA(s) received

| Custodian | Box 1  | Box 2 | Box 3 | Box 4 | Box 5 |
|-----------|--------|-------|-------|-------|-------|
| Fidelity  | $5,000 | $0    | 1     | $0    | HSA   |
| **Total** | $5,000 |       |       |       |       |

## Qualified medical expenses (QME) breakdown

| Category                              | Amount  | Receipts? | Patient   |
|---------------------------------------|---------|-----------|-----------|
| Doctor visits / co-pays               | $950    | Yes       | All family|
| Prescriptions                         | $180    | Yes       | Marcus    |
| OTC medications                       | $90     | Yes       | Family    |
| Lab work                              | $140    | Yes       | Marcus    |
| Dental (cleanings + crown)            | $1,200  | Yes       | Family    |
| Vision (eye exams + contacts)         | $440    | Yes       | Marcus, Lena |
| Emergency / urgent care               | $1,000  | Yes       | Marcus    |
| **Total QME**                         | **$4,000** |        |           |

## Non-QME breakdown (taxable portion)

| Item                  | Amount  | Why not QME                                |
|-----------------------|---------|---------------------------------------------|
| Multivitamins         | $400    | General health, no LMN, not for a specific condition |
| Gym membership        | $600    | General fitness, no doctor's prescription   |
| **Total non-QME**     | **$1,000** |                                          |

## Form 8889 Part II — line-by-line

14a. Total distributions:                        $5,000
14b. Rollovers:                                  $0
14c. Subtract 14b from 14a:                      $5,000
15.  Qualified medical expenses paid using HSA:  $4,000
16.  Taxable HSA distributions (14c − 15):       $1,000  → Schedule 1 Line 8f
17a. Exception reason:                           None (Marcus is 41, not disabled, not died)
17b. Additional 20% tax (16 × 0.20):             $200    → Schedule 2 Line 17c

## Required attachments
- [x] Form 8889 (full form, including Part I for $8,550 contribution)
- [ ] Form 5329 — N/A (no excess contribution)
- [ ] Form 8853 — N/A

## Validation summary
- Math: all checks passed
  - Line 14c = $5,000 ✓
  - Line 15 = $4,000 (substantiated with receipts) ✓
  - Line 16 = $1,000 ✓
  - Line 17b = $200 (= $1,000 × 0.20) ✓
- Sanity:
  - Marcus is 41 → 20% penalty applies (no age 65 exception) ✓
  - Marcus is not disabled, did not die → no other exceptions ✓
  - All QME for Marcus, spouse Lena, or dependent children ✓
  - Receipts retained for both QME and non-QME items ✓
- Next steps:
  - Schedule 1 Line 8f: $1,000 (added to AGI as ordinary income)
  - Schedule 2 Line 17c: $200 (additional tax on Form 1040 Line 23)
  - Marcus's marginal tax rate (likely 22% federal at his income): the $1,000 costs him $220 in income tax + $200 penalty = $420 total tax cost on the $1,000 non-QME distribution
  - For 2026: Marcus should not use his HSA for non-QME items — the 42% combined cost makes it economically irrational vs. paying out of pocket from already-taxed wages

## Sources cited in this draft
- IRS Form 1099-SA (Rev. April 2025)
- IRS Instructions for Forms 1099-SA and 5498-SA (2025)
- IRS Form 8889 (2025)
- IRS Pub 502 (qualified medical expenses)
- IRS Pub 969 (HSAs)
- IRC §223(f)(1) (non-QME taxable as income)
- IRC §223(f)(4) (20% additional tax) and §223(f)(4)(B)–(C) (exceptions — none apply to Marcus)
- IRC §223(d)(2)(A) (HSA QME definition referencing IRC §213(d))
```

## Why each non-obvious choice

**Why aren't multivitamins QME?** Pub 502 and IRS guidance require nutritional supplements to be **prescribed for a specific medical condition** to be QME. General-purpose multivitamins for "wellness" are not. The user can get an LMN from a doctor for a specific deficiency (e.g., vitamin D for osteoporosis prevention) and convert these to QME — but Marcus didn't.

**Why is the gym membership $600 not QME?** Same reasoning: gym memberships for general fitness are not QME. Exception: a doctor prescribes the membership for a specific condition (obesity treatment, cardiac rehabilitation), with an LMN. Without it, no.

**Why does Marcus's family qualify for QME (his spouse, his children)?** IRC §223(d)(2) allows the HSA holder to use the HSA for qualified medical expenses of:
- The HSA holder
- Their spouse
- Their tax dependents

Lena (spouse) and the two children (dependents on the joint return) all qualify.

**Why does the 20% additional tax apply?** Marcus is 41, not disabled, did not die. None of the IRC §223(f)(4)(B)–(C) exceptions apply. The 20% applies on top of ordinary income tax.

**Total cost calculation for the $1,000 non-QME**:
- Federal income tax (22% marginal rate): $220
- 20% additional tax: $200
- State income tax (varies by state — say 5%): $50
- **Total**: $470 on a $1,000 distribution = 47% effective tax rate

This makes non-QME HSA distributions economically irrational for under-65 users. Better to pay out-of-pocket from already-taxed wages and let the HSA grow tax-free.

**What if Marcus had been 65 or older?** For distributions made after his 65th birthday, Line 17a would be checked and Line 17b = $0. The $1,000 would still be ordinary income (Line 16), but the 20% penalty would be waived. This is the famous "HSAs become a stealth IRA at 65" feature — non-QME distributions still owe income tax but no penalty, similar to a traditional IRA at age 59½.

**Should Marcus pay back the non-QME amount?** Once a distribution is taken, the IRS rules don't allow "paying it back" except through the limited rollover rule (IRC §223(f)(5)) — only within 60 days, one rollover per 1-year period — or the mistaken-distribution rule, which needs a mistake of fact due to reasonable cause (e.g., believing an expense was qualified) and a custodian that accepts the repayment (2025 Instructions for Forms 1099-SA and 5498-SA, "HSA Mistaken Distributions"). Marcus knew these purchases were not qualified, so neither applies. Marcus owes the tax + penalty.

## Audit defense

If the IRS questioned Marcus's Form 8889:
1. The HSA portal report shows $5,000 in distributions; receipts substantiate $4,000 as QME (Line 15)
2. The $1,000 non-QME items are clearly labeled (gym, multivitamins) and Marcus paid the appropriate tax + penalty
3. Schedule 1 Line 8f shows $1,000 added to AGI
4. Schedule 2 Line 17c shows $200 additional tax
5. The audit would close without changes — Marcus correctly identified and reported the non-QME portion
