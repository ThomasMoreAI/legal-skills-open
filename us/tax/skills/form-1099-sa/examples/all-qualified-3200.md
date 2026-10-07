# Example: HSA Holder Paying $3,200 of Qualified Medical Expenses

The canonical "everything is qualified" Form 1099-SA case. The user took distributions during the year, all for legitimate medical expenses, and owes no tax or penalty on the distribution.

This example shows that **Form 8889 Part II is still required** even when there's no taxable amount — the form documents the QME treatment to the IRS.

## The filer

- **Name**: Aisha Rahman
- **Tax year**: 2025 (filing in 2026)
- **Age at year-end**: 38
- **Filing status**: Single
- **HSA custodian**: HealthEquity (single HSA)
- **Insurance**: Self-only HDHP through her employer all year
- **Aisha's contribution to HSA in 2025**: $4,300 (the full self-only limit per IRS Rev. Proc.)

## Inputs gathered

### 1099-SA from HealthEquity

```
PAYER: HealthEquity, <payer TIN as printed on the form>
RECIPIENT: Aisha Rahman, SSN ***-**-XXXX

Box 1 (Gross distribution):                $3,200
Box 2 (Earnings on excess):                $0
Box 3 (Distribution code):                 1 (Normal)
Box 4 (FMV on date of death):              $0
Box 5 (Account type):                      [HSA checked]
```

### Qualified Medical Expenses paid in 2025

| Category | Provider | Date | Amount | Receipt? |
|----------|----------|------|--------|----------|
| Annual physical co-pay | Dr. Lee, internal medicine | Mar 12 | $40 | Yes |
| Specialist visit (dermatology) | Dr. Patel | May 4 | $80 | Yes |
| Lab work (blood panel) | Quest Diagnostics | Mar 15 | $120 | Yes |
| Generic prescriptions (4 fills) | CVS Pharmacy | Various | $180 | Yes (year-end Rx summary) |
| Dental cleaning + X-ray | Dr. Kim DDS | Apr 8 | $250 | Yes |
| Vision exam + 1 pair glasses | LensCrafters | Jun 21 | $310 | Yes |
| Therapy sessions (10 × $120) | Sarah Brooks LCSW | Various | $1,200 | Yes (provider invoices) |
| Allergy medication OTC (Zyrtec, Flonase) | CVS | Various | $90 | Yes (CVS register receipts) |
| Bandages, thermometer, first aid | Target | Various | $40 | Yes |
| Prescription for migraine medication | CVS | Sep 14 | $480 | Yes |
| Urgent care visit (sprained ankle) | MedExpress | Oct 3 | $410 | Yes |
| **Total QME** | | | **$3,200** | |

Aisha matches every dollar of the $3,200 distribution to a QME with a receipt. Her HSA portal "Distribution by category" report confirms this.

## Step-by-step computation

### Step 1 — Confirm Box 5 = HSA → Form 8889

Yes → Form 8889 Part II.

### Step 2 — Box 3 = Code 1 (Normal distribution)

Standard treatment: non-QME portion taxable + 20% penalty if under 65. Aisha is 38, so penalty would apply if any non-QME existed.

### Step 3 — QME total = $3,200

Matches Box 1 exactly. Aisha kept careful records throughout the year using a spreadsheet she updates after each HSA debit card swipe.

### Step 4-5 — Form 8889 Part II computation

```
Line 14a (Total distributions):                  $3,200
Line 14b (Rollovers):                            $0
Line 14c (14a − 14b):                            $3,200
Line 15 (QME paid using HSA):                    $3,200
Line 16 (Taxable distributions, 14c − 15):       $0
Line 17a (Exception):                            N/A (Line 16 = $0, no penalty)
Line 17b (20% additional tax):                   $0
```

## The completed Form 8889 Part II draft

```markdown
# Form 8889 Part II — DRAFT for tax year 2025

## 1099-SA(s) received

| Custodian      | Box 1   | Box 2 | Box 3 | Box 4 | Box 5 |
|----------------|---------|-------|-------|-------|-------|
| HealthEquity   | $3,200  | $0    | 1     | $0    | HSA   |
| **Total**      | $3,200  |       |       |       |       |

## Qualified medical expenses (QME) breakdown

| Category                        | Amount   | Receipts? |
|---------------------------------|----------|-----------|
| Doctor visits / co-pays / urgent care | $530     | Yes       |
| Lab work                        | $120     | Yes       |
| Prescriptions (generic + migraine)| $660    | Yes       |
| Dental                          | $250     | Yes       |
| Vision (exam + glasses)         | $310     | Yes       |
| Mental health therapy           | $1,200   | Yes       |
| OTC medications (allergy)       | $90      | Yes       |
| First aid supplies              | $40      | Yes       |
| **Total QME**                   | **$3,200** |         |

## Form 8889 Part II — line-by-line

14a. Total distributions:                        $3,200
14b. Rollovers:                                  $0
14c. Subtract 14b from 14a:                     $3,200
15.  Qualified medical expenses paid using HSA: $3,200
16.  Taxable HSA distributions (14c − 15):       $0
17a. Exception reason:                           N/A
17b. Additional 20% tax (16 × 0.20):             $0

## Required attachments
- [x] Form 8889 (full form, including Part I for Aisha's $4,300 contribution)
- [ ] Form 5329 — N/A
- [ ] Form 8853 — N/A

## Validation summary
- Math: all checks passed
  - Line 14c = $3,200 (= 14a − 14b) ✓
  - Line 16 = $0 (= 14c − 15) ✓
  - Line 17b = $0 (no taxable distribution) ✓
- Sanity: none flagged
  - All receipts substantiate QME ✓
  - HSA was open before any QME was incurred ✓
  - All QME for Aisha (HSA holder); no dependent or non-dependent issues ✓
- Next steps:
  - Schedule 1 Line 8f: $0 (no taxable HSA distribution to add to AGI)
  - Schedule 2 Line 17c: $0 (no additional tax)
  - Form 8889 Part I: separately reports Aisha's $4,300 contribution (deductible on Schedule 1 Line 13 if made via personal funds, or already pre-tax via payroll)
  - Receipts retention: retain all QME receipts for at least 3 years (April 15, 2029)

## Sources cited in this draft
- IRS Form 1099-SA (Rev. April 2025)
- IRS Instructions for Forms 1099-SA and 5498-SA (2025)
- IRS Form 8889 (2025)
- IRS Pub 502 (qualified medical expenses)
- IRS Pub 969 (HSAs)
- IRC §223(f)(1) (taxable on non-QME — N/A here since Line 16 = $0)
- IRC §223(d)(2)(A) (HSA QME definition)
- CARES Act 2020 (OTC medications and menstrual care as QME)
```

## Why each non-obvious choice

**Why is Form 8889 Part II filed even with Line 16 = $0?** Two reasons:
1. The IRS receives a copy of Aisha's 1099-SA from HealthEquity. If the IRS sees a $3,200 distribution but no Form 8889 from Aisha, it triggers a CP2000 notice assuming the entire $3,200 is taxable. Filing Form 8889 with $0 taxable PROVES the distribution was for QME.
2. Form 8889 also handles Aisha's $4,300 HSA contribution (Part I) — Form 8889 is the single form covering both contributions and distributions for the year.

**Why is therapy with Sarah Brooks (LCSW) qualified?** Mental health services from a licensed mental health provider are QME under IRC §213(d) and Pub 502. LCSW (Licensed Clinical Social Worker) is a qualified provider. The same would apply to LMFT (marriage and family therapist) or psychologist.

**Why are OTC allergy medications now QME?** The CARES Act (2020) restored OTC medications and menstrual care products to the QME list. From 2011 through 2019, OTC medicines (other than insulin) required a prescription to be QME — that requirement was removed for amounts paid after 2019.

**Why Aisha's vision glasses qualify?** Corrective eyewear (glasses, contacts, contact solution, vision exams, even some over-the-counter reading glasses) are QME. Cosmetic colored contacts without vision correction would NOT be.

**What about Aisha's gym membership?** Aisha didn't include it. Gym memberships are generally NOT QME unless prescribed by a physician for a specific medical condition (with a Letter of Medical Necessity). For general fitness, no.

**What if Aisha had used the HSA debit card at a Whole Foods checkout for some non-medical groceries?** That portion would be non-QME → taxable + 20% penalty. The HSA debit card system doesn't pre-validate every transaction; some custodians block obviously-non-medical merchant codes, but coding errors slip through. Aisha's spreadsheet and receipt retention catch these.

## Audit defense

If the IRS questioned Aisha's Form 8889 Part II:
1. Aisha presents her HSA portal "Distribution by category" report showing $3,200 in distributions matched to medical merchant codes
2. For each distribution, Aisha presents a receipt showing date, provider, patient (Aisha herself), service description, and amount
3. The therapy sessions are substantiated by Sarah Brooks LCSW's invoices listing CPT codes for behavioral health therapy
4. The OTC purchases are substantiated by CVS register receipts showing item descriptions
5. Total QME = $3,200 = Box 1 of 1099-SA → Line 16 = $0 → no taxable income or penalty owed

The IRS's audit would close without changes. Aisha's record retention is the model — every transaction, every receipt, every category labeled.
