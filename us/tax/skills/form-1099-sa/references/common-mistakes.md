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

**Citation**: Form 8889 structure (Part I = contributions; Part II = distributions; Part III = income and additional tax for failure to maintain HDHP coverage).

---

## 4. Health insurance premiums claimed as QME

**Mistake**: User pays $5,000 in health insurance premiums for the year and reimburses themselves from the HSA, treating premiums as QME.

**Why it's wrong**: Most health insurance premiums are NOT QME under IRC §223(d)(2)(B). The exceptions are narrow:
- COBRA continuation premiums
- Health coverage while receiving unemployment compensation
- Medicare and other health coverage premiums when the account holder is 65 or older (Medigap excluded)
- Long-term care insurance premiums (with age caps)
- For months after December 31, 2025, direct primary care fees up to $150 a month ($300 if more than one person) (IRC §223(d)(2)(C); Notice 2026-5)

If the user paid premiums for their regular HDHP, those are NOT QME. Reimbursing from the HSA = non-QME = taxable + 20% penalty.

**Fix**: Subtract the disallowed premium amount from QME. Recalculate Line 16. Add Line 17b 20% additional tax if under 65.

**Citation**: IRC §223(d)(2)(B); Pub 969.

---

## 5. Adult child medical expenses claimed when child is not a dependent

**Mistake**: Parent uses HSA to pay 25-year-old child's medical bills. The 25-year-old is self-supporting and is NOT the parent's dependent.

**Why it's wrong**: HSA QME rules cover the HSA holder, their spouse, their dependents, and any person who would be a dependent except that the person filed a joint return, had gross income above the limit, or the holder can be claimed as someone else's dependent (2025 Instructions for Form 8889, Line 15). The Affordable Care Act allows children up to age 26 on a parent's HDHP, but that plan rule does not make the child's expenses QME. A 25-year-old who is not a student can be the parent's qualifying child only if permanently and totally disabled; otherwise the qualifying-relative support test must be met. ASK who provided over half of the child's support before deciding.

**Fix**: If the child is neither a dependent nor a would-be dependent, treat the parent's HSA distribution as non-QME → taxable + 20% penalty. The child can open their own HSA if they're HSA-eligible separately.

**Citation**: IRC §223(d)(2)(A); IRC §152 (dependent definition); 2025 Instructions for Form 8889, Line 15.

---

## 6. Forgetting the 20% additional tax (Line 17b)

**Mistake**: User has $1,500 non-QME distribution. They report it as taxable income on Schedule 1 Line 8f but skip Form 8889 Line 17b (20% additional tax = $300).

**Why it's wrong**: The 20% additional tax under IRC §223(f)(4) is separate from ordinary income tax. It must be reported on Form 8889 Line 17b → Schedule 2 Line 17c → Form 1040 Line 23.

**Fix**: Complete Line 17b. The penalty is in addition to ordinary income tax — a $1,500 non-QME distribution costs the user (1) ordinary income tax × marginal rate (e.g., 22% = $330) PLUS (2) $300 (20% × $1,500) penalty = $630 total.

**Citation**: IRC §223(f)(4); Form 8889 Line 17b.

---

## 7. Applying 20% penalty when account holder is 65+

**Mistake**: User is age 67 and took a $5,000 non-QME distribution. They paid the 20% additional tax penalty thinking it always applies.

**Why it's wrong**: IRC §223(f)(4)(C) waives the 20% additional tax for distributions made after the account holder turns 65. The non-QME portion is still taxable as ordinary income, but the 20% penalty does NOT apply.

**Fix**: Check Line 17a. Set Line 17b = $0 (in the year of the 65th birthday, 20% still applies to distributions made before the birthday).

**Citation**: IRC §223(f)(4)(C); Form 8889 Line 17a.

---

## 8. Not aggregating multiple HSAs

**Mistake**: User has HSAs at HealthEquity and Fidelity. They received two 1099-SAs ($2,000 and $3,000). They file two separate Form 8889s, treating the accounts as independent.

**Why it's wrong**: A single user files **one Form 8889** aggregating all their HSAs. Line 14a sums Box 1 from all 1099-SAs. The QME breakdown on Line 15 also aggregates.

**Fix**: One Form 8889 per user. Aggregate Line 14a = $5,000. Enter total QME paid from all HSA distributions on Line 15.

**Citation**: 2025 Instructions for Form 8889, Line 14a ("total distributions your HSAs made"). Exception: a person who is the beneficiary of a deceased holder's HSA and also has their own HSA completes a separate "statement" Form 8889 for each and a controlling Form 8889 ("Death of Account Beneficiary").

---

## 9. Both spouses' HSAs combined

**Mistake**: Married couple files jointly. Each spouse has their own HSA. The couple combines both spouses' 1099-SAs onto a single Form 8889.

**Why it's wrong**: HSAs are individually owned. Each spouse files **their own Form 8889** even on a joint return. The contribution limits, distributions, and Form 8889 lines are per-spouse.

**Fix**: Two separate Form 8889s — one per spouse. Each spouse aggregates only their own HSA(s) on their own Form 8889.

**Citation**: IRC §223(b)(5) (joint contribution rules); 2025 Instructions for Form 8889, "Name and social security number (SSN)" (separate Form 8889 for each spouse).

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

**Mistake**: User opened and funded the HSA in March 2024. In December 2024, they reimburse themselves $2,000 for medical bills incurred in January 2024 (before the HSA was established).

**Why it's wrong**: Notice 2004-50 Q&A 39 requires the QME to be incurred **after the HSA was established**. State trust law sets the establishment date; most states require the account to be funded (Notice 2008-59 Q&A-38). Pre-establishment medical expenses cannot be reimbursed from the HSA.

**Fix**: Treat the $2,000 reimbursement as non-QME → taxable + 20% penalty. The user can claim the January medical expense on Schedule A (itemized deductions, subject to AGI floor) instead, but not from the HSA.

**Citation**: Notice 2004-50 Q&A 39.

---

## 12. Code 4 inheritance: forgetting deceased's pre-death QME deduction

**Mistake**: Beneficiary inherits HSA worth $30,000 (Code 4 1099-SA). The deceased had $4,000 in unpaid pre-death medical bills the beneficiary paid after inheritance. Beneficiary reports the entire $30,000 as ordinary income.

**Why it's wrong**: IRC §223(f)(8)(B)(ii)(I) reduces a non-estate beneficiary's income by the decedent's QME incurred before death and paid by the beneficiary within **1 year after death**.

**Fix**: Form 8889 headed "Death of HSA account beneficiary": Line 14a = $30,000 (FMV at death), Line 15 = $4,000. Net taxable on Line 16: $26,000 instead of $30,000.

**Citation**: IRC §223(f)(8)(B)(ii)(I); 2025 Instructions for Form 8889, "Death of Account Beneficiary".

---

## 13. Code 6 misread as a spouse rollover

**Mistake**: A nonspouse beneficiary receives a Code 6 1099-SA in the year after the death and treats it as nontaxable, or reports the whole amount in the year received.

**Why it's wrong**: Code 6 is a death distribution **after the year of death to a nonspouse beneficiary** (Form 1099-SA, Box 3). The FMV on the date of death is income for the **year of death** (Form 1099-SA, Instructions for Recipient, "Nonspouse beneficiary"); only the earnings after death (Box 1 − Box 4) belong to the year received. A spouse beneficiary gets no Code 6: the HSA simply becomes the spouse's (IRC §223(f)(8)(A)).

**Fix**: Report the Box 4 amount on the year-of-death Form 8889 (amend that year with Form 1040-X if needed); report Box 1 − Box 4 as other income for the current year.

**Citation**: IRC §223(f)(8); Form 1099-SA (Rev. April 2025) Box 3 and Instructions for Recipient.

---

## 14. Code 2 excess contribution: wrong Form 5329 handling

**Mistake**: User had a Code 2 1099-SA for an excess withdrawn (with earnings) by the due date of the return. They either add the excess to Form 5329 Part VII, or put Box 2 earnings on Form 8889 Line 16.

**Why it's wrong**: An excess withdrawn with its earnings by the due date including extensions is treated as not contributed; it is not entered on Form 5329 Line 47, and the withdrawn excess and earnings go on Form 8889 Lines 14a and 14b. The earnings are "Other income" for the year received. Form 5329 Part VII is needed only for excess that stayed past the due date (6% for each year).

**Fix**: Lines 14a/14b for the withdrawal; Box 2 to Schedule 1 Line 8z; Form 5329 only for excess still in the account after the due date.

**Citation**: IRC §223(f)(3); IRC §4973; 2025 Instructions for Form 5329, Line 47.

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
| 6 | Skipping 20% additional tax | Line 17b | 20% on Line 16 if made before 65 |
| 7 | Penalty when 65+ | Line 17a | Check Line 17a for distributions after 65 |
| 8 | Not aggregating multiple HSAs | Line 14a | Sum all 1099-SAs |
| 9 | Combining spouses on one form | — | One Form 8889 per spouse |
| 10 | Estimating QME without receipts | Line 15 | Substantiate or treat as non-QME |
| 11 | Pre-HSA establishment QME | Line 15 | Not allowed; treat as non-QME |
| 12 | Forgetting deceased's pre-death QME (Code 4) | Line 15 | Subtract QME paid within 1 year after death |
| 13 | Code 6 misread | Line 14a, year of death | FMV is income for the year of death |
| 14 | Code 2 handled wrong | Lines 14a/14b, Form 5329 | Timely withdrawn excess: 14a/14b, no Form 5329 |
| 15 | Full-QME but reported taxable | Line 16 | Should be $0 |
