# Common Form 1099-SA / Form 8889 Mistakes

The most common audit-trip and IRS-notice mistakes when reporting HSA distributions, with citations and fixes.

---

## 1. Filing the 1099-SA itself

**Mistake**: User attaches the 1099-SA to their Form 1040 as if it were a tax form to file.

**Why it's wrong**: Form 1099-SA is an **information return** sent by the custodian to both the recipient and the IRS. The recipient does NOT file the 1099-SA — the custodian already did. The recipient files **Form 8889** (HSA) or **Form 8853** (Archer / MA MSA), which incorporates the 1099-SA boxes.

**Fix**: Don't attach the 1099-SA. Keep it in your records. File Form 8889 / 8853 instead.

**Citation**: General 1099 form rule — informational returns are not filed by recipients.

---

## 2. Forgetting Form 8889 entirely when distributions = QME

**Mistake**: User had a Code 1 distribution of $4,000, all for QME. They think "no taxable income, no need to file Form 8889" and skip the form.

**Why it's wrong**: Form 8889 is required **whenever** the user has HSA contributions OR distributions in the year (Form 8889 Part II is filled even with $0 taxable). Skipping it triggers an IRS CP2000 notice — the IRS knows from the custodian's 1099-SA filing that the user took a distribution; not seeing Form 8889 raises a flag.

**Fix**: File Form 8889 Part II showing Line 14a = $4,000, Line 15 = $4,000, Line 16 = $0. This documents to the IRS that the distribution was fully QME.

**Citation**: Form 8889 Instructions, "Who Must File."

---

## 3. Treating HSA contributions as distributions

**Mistake**: User confuses 1099-SA (distributions) with 5498-SA (contributions) and reports their HSA contributions on Form 8889 Part II.

**Why it's wrong**: 1099-SA is for money **leaving** the HSA. 5498-SA is for money **going into** the HSA. They flow to different parts of Form 8889 (Part I vs. Part II). Reporting contributions as distributions inflates taxable income.

**Fix**:
- If the user has a 1099-SA → Form 8889 Part II (distributions)
- If the user has a 5498-SA → Form 8889 Part I (contributions)
- Both can apply in the same year and both go on the same Form 8889

**Citation**: Form 8889 structure (Part I = contributions; Part II = distributions; Part III = funding distribution).

---

## 4. Health insurance premiums claimed as QME

**Mistake**: User pays $5,000 in health insurance premiums for the year and reimburses themselves from the HSA, treating premiums as QME.

**Why it's wrong**: Most health insurance premiums are NOT QME under IRC §223(d)(2)(B). The exceptions are narrow:
- COBRA continuation premiums
- Health coverage while receiving unemployment compensation
- Medicare Parts B / D / Advantage (when the user is age 65+ and enrolled)
- Long-term care insurance premiums (with age caps)

If the user paid premiums for their regular HDHP, those are NOT QME. Reimbursing from the HSA = non-QME = taxable + 20% penalty.

**Fix**: Subtract the disallowed premium amount from QME. Recalculate Line 16. Add Line 17b 20% additional tax if under 65.

**Citation**: IRC §223(d)(2)(B); Pub 969.

---

## 5. Adult child medical expenses claimed when child is not a dependent

**Mistake**: Parent uses HSA to pay 25-year-old child's medical bills. The 25-year-old is NOT a tax dependent (over age 24, not disabled).

**Why it's wrong**: HSA QME rules require the medical expense to be for the HSA holder, their spouse, or their tax dependent (Form 1040 dependent). The Affordable Care Act allows children up to age 26 on a parent's HDHP — but for HSA purposes, the child must be a tax dependent, which requires being under age 24 (or any age if disabled).

**Fix**: Treat the parent's HSA distribution as non-QME → taxable + 20% penalty. The child can open their own HSA if they're HSA-eligible separately.

**Citation**: IRC §223(d)(2)(A); IRC §152 (dependent definition).

---

## 6. Forgetting the 20% additional tax (Line 17b)

**Mistake**: User has $1,500 non-QME distribution. They report it as taxable income on Schedule 1 Line 8f but skip Form 8889 Line 17b (20% additional tax = $300).

**Why it's wrong**: The 20% additional tax under IRC §223(f)(4) is separate from ordinary income tax. It must be reported on Form 8889 Line 17b → Schedule 2 Line 17c → Form 1040 Line 23.

**Fix**: Complete Line 17b. The penalty is in addition to ordinary income tax — a $1,500 non-QME distribution costs the user (1) ordinary income tax × marginal rate (e.g., 22% = $330) PLUS (2) $300 (20% × $1,500) penalty = $630 total.

**Citation**: IRC §223(f)(4); Form 8889 Line 17b.

---

## 7. Applying 20% penalty when account holder is 65+

**Mistake**: User is age 67 and took a $5,000 non-QME distribution. They paid the 20% additional tax penalty thinking it always applies.

**Why it's wrong**: IRC §223(f)(4)(B) waives the 20% additional tax when the account holder is age 65 or older at the time of distribution. The non-QME portion is still taxable as ordinary income, but the 20% penalty does NOT apply.

**Fix**: Mark the age 65+ exception on Form 8889 Line 17a. Set Line 17b = $0.

**Citation**: IRC §223(f)(4)(B); Form 8889 Line 17a.

---

## 8. Not aggregating multiple HSAs

**Mistake**: User has HSAs at HealthEquity and Fidelity. They received two 1099-SAs ($2,000 and $3,000). They file two separate Form 8889s, treating the accounts as independent.

**Why it's wrong**: A single user files **one Form 8889** aggregating all their HSAs. Line 14a sums Box 1 from all 1099-SAs. The QME breakdown on Line 15 also aggregates.

**Fix**: One Form 8889 per user. Aggregate Line 14a = $5,000. Enter total QME paid from all HSA distributions on Line 15.

**Citation**: Form 8889 Instructions, "Multiple HSAs."

---

## 9. Both spouses' HSAs combined

**Mistake**: Married couple files jointly. Each spouse has their own HSA. The couple combines both spouses' 1099-SAs onto a single Form 8889.

**Why it's wrong**: HSAs are individually owned. Each spouse files **their own Form 8889** even on a joint return. The contribution limits, distributions, and Form 8889 lines are per-spouse.

**Fix**: Two separate Form 8889s — one per spouse. Each spouse aggregates only their own HSA(s) on their own Form 8889.

**Citation**: IRC §223(b)(5) (joint contribution rules); Form 8889 Instructions, "Married Couples."

---

## 10. Estimating QME without receipts

**Mistake**: User can't find receipts. They estimate "around $3,500" of the $4,000 distribution went to QME.

**Why it's wrong**: The IRS expects substantiation under IRC §6001 (general recordkeeping requirement) and IRC §6501 (audit window of 3 years). Without receipts, the IRS may disallow the claimed QME on audit, treating the entire distribution as non-QME → ordinary tax + 20% penalty.

**Fix**:
- Pull HSA portal "Distribution by category" report (most custodians offer)
- Reconstruct receipts from credit card / bank statements + provider EOBs
- For unrecoverable transactions, conservatively treat as non-QME (taxable + penalty)

**Citation**: IRC §6001; Pub 583.

---

## 11. Reimbursing for QME paid before HSA was established

**Mistake**: User opened HSA in March 2024. In December 2024, they reimburse themselves $2,000 for medical bills incurred in January 2024 (before HSA was opened).

**Why it's wrong**: Notice 2004-50 Q&A 39 requires the QME to be incurred **after the HSA was established**. Pre-establishment medical expenses cannot be reimbursed from the HSA.

**Fix**: Treat the $2,000 reimbursement as non-QME → taxable + 20% penalty. The user can claim the January medical expense on Schedule A (itemized deductions, subject to AGI floor) instead, but not from the HSA.

**Citation**: Notice 2004-50 Q&A 39.

---

## 12. Code 4 inheritance: forgetting deceased's pre-death QME deduction

**Mistake**: Beneficiary inherits HSA worth $30,000 (Code 4 1099-SA). The deceased had $4,000 in unpaid pre-death medical bills the beneficiary paid after inheritance. Beneficiary reports the entire $30,000 as ordinary income.

**Why it's wrong**: IRC §223(f)(8)(A) allows the beneficiary to subtract amounts paid for the deceased's QME within **1 year of death**. The taxable inheritance is reduced by qualified pre-death medical expenses.

**Fix**: Reduce Line 14a (or the equivalent line on the beneficiary's tax return) by $4,000. Net taxable: $26,000 instead of $30,000.

**Citation**: IRC §223(f)(8)(A).

---

## 13. Spouse Code 6 inheritance: filing as taxable

**Mistake**: Spouse inherits the HSA upon the account holder's death (Code 6). They file Form 8889 Part II showing the full Box 1 as taxable.

**Why it's wrong**: IRC §223(f)(8)(B) allows the surviving spouse to **take over the HSA as their own** with no tax consequence. The 1099-SA is essentially informational — Code 6 means "spouse rollover."

**Fix**: The spouse does NOT report the Code 6 distribution as taxable. They simply continue filing Form 8889 in future years for the inherited HSA (which is now in their name).

**Citation**: IRC §223(f)(8)(B); Form 8889 Instructions, "Death of HSA Holder — Spouse Beneficiary."

---

## 14. Code 2 excess contribution: missing Form 5329

**Mistake**: User had Code 2 1099-SA (excess contribution + earnings withdrawn). They report Box 2 earnings as income on Form 8889 but forget Form 5329.

**Why it's wrong**: Code 2 means the excess was **withdrawn timely** (avoiding the 6% excise) but the user must still document the excess on Form 5329 Part VII for tracking purposes. If the excess was NOT withdrawn timely, Form 5329 is mandatory and computes the 6% excise.

**Fix**: Add Form 5329 Part VII. If timely withdrawn (Code 2), Form 5329 documents $0 excise. If not timely, compute the 6% on the cumulative excess remaining in the HSA.

**Citation**: IRC §4973; Form 5329 Part VII.

---

## 15. Code 1 with full QME but Form 8889 still filed showing taxable

**Mistake**: User had $3,000 Code 1 distribution, all for QME. They report Line 16 = $3,000 (taxable) instead of $0.

**Why it's wrong**: When QME = full distribution, Line 15 = Line 14a → Line 16 = $0. This is a computation error.

**Fix**:
- Line 14a = $3,000
- Line 15 = $3,000
- Line 16 = $0
- Line 17b = $0
- No income tax impact, no penalty.

**Citation**: Form 8889 Lines 14a, 15, 16.

---

## Summary table

| # | Mistake | Form/Line | Fix |
|---|---------|-----------|-----|
| 1 | Filing 1099-SA itself | — | File Form 8889 instead |
| 2 | Skipping Form 8889 when QME = distribution | Form 8889 | File anyway with $0 taxable |
| 3 | Confusing 1099-SA with 5498-SA | Part I vs II | Distributions = Part II |
| 4 | Insurance premiums as QME | Line 15 | Most premiums are NOT QME |
| 5 | Adult non-dependent's expenses | Line 15 | Tax dependent only |
| 6 | Skipping 20% additional tax | Line 17b | 20% on Line 16 if under 65 |
| 7 | Penalty when 65+ | Line 17a | Mark age 65 exception |
| 8 | Not aggregating multiple HSAs | Line 14a | Sum all 1099-SAs |
| 9 | Combining spouses on one form | — | One Form 8889 per spouse |
| 10 | Estimating QME without receipts | Line 15 | Substantiate or treat as non-QME |
| 11 | Pre-HSA establishment QME | Line 15 | Not allowed; treat as non-QME |
| 12 | Forgetting deceased's pre-death QME (Code 4) | Line 15 | Subtract within 1 year of death |
| 13 | Spouse Code 6 as taxable | Line 16 | Spouse rollover; not taxable |
| 14 | Code 2 missing Form 5329 | Form 5329 | Add Part VII for tracking |
| 15 | Full-QME but reported taxable | Line 16 | Should be $0 |
