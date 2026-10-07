# Form 1099-SA Distribution Codes (Box 3)

The single-digit code in Box 3 drives the entire tax treatment of the distribution. There are six valid codes. This file explains each. Code definitions verified against Form 1099-SA (Rev. April 2025) and the 2025 Instructions for Forms 1099-SA and 5498-SA, Box 3.

---

## Code 1 — Normal distribution

**Meaning**: A regular, voluntary distribution from the HSA / MSA, including direct payments to a medical provider. The account holder withdrew funds — by debit card swipe, ATM, online transfer, check, or claim reimbursement — during the year. Custodians also use Code 1 for distributions after the year of death to a spouse beneficiary, and whenever no other code applies.

**Frequency**: Most common code. The vast majority of 1099-SAs the agent will see have Code 1.

**Tax treatment**:
- Distributions used for qualified medical expenses (QME): **not taxable**
- Distributions NOT used for QME: **taxable as ordinary income** (Form 8889 Line 16)
- Plus **20% additional tax** on the non-QME portion if account holder is under age 65 (Form 8889 Line 17b)
- Exceptions to the 20% tax: distribution made after the account holder turned 65 (IRC §223(f)(4)(C)), became disabled, or died (§223(f)(4)(B)). Code 1 with an exception still produces taxable income but no penalty.

**Authority**: IRC §223(f)(1) (taxable on non-QME), §223(f)(4) (20% additional tax + exceptions).

**Worked example**:

User receives Code 1 1099-SA Box 1 = $5,000. User used $4,000 for QME. User is age 45.

```
Form 8889 Line 14a: $5,000
Line 14b (rollovers): $0
Line 14c: $5,000
Line 15 (QME): $4,000
Line 16 (taxable): $5,000 − $4,000 = $1,000
Line 17a: no exception
Line 17b: $1,000 × 0.20 = $200

Schedule 1 Line 8f: $1,000  (added to ordinary income)
Schedule 2 Line 17c: $200   (additional tax)
```

---

## Code 2 — Excess contributions plus earnings

**Meaning**: The account holder contributed more than the IRC §223(b) annual limit and is withdrawing the excess (plus any earnings). Box 2 earnings are reported only for excess returned by the due date of the return. Typically initiated by the user filing a "return of excess contribution" form with the custodian.

**Frequency**: Uncommon. Occurs when a user makes an error or changes coverage mid-year (e.g., moves from family HDHP to self-only HDHP, lowering the contribution limit retroactively).

**Tax treatment**:
- **Box 1** (gross distribution = excess + earnings): if withdrawn by the due date of the return **including extensions**, the excess is treated as not contributed and is **not taxable**; the excess and earnings go on Form 8889 Lines 14a and 14b (2025 Instructions for Form 5329, Line 47)
- **Box 2** (earnings on excess): **taxable as ordinary income** ("Other income", Schedule 1 Line 8z) for the year the distribution is received (IRC §223(f)(3)(A))
- The **6% excise tax** under IRC §4973 applies only to excess left in the account after that due date; reported on Form 5329 Part VII. A timely withdrawn excess is not entered on Form 5329.

**Authority**: IRC §223(f)(3)(A) (return of excess), IRC §4973 (excise on excess), Treasury Reg. §1.408-11 (earnings calculation the custodian uses, per the 1099-SA instructions for Box 2).

**Worked example**:

User contributed $5,000 to an HSA in 2025 but their actual limit was $4,300 (self-only HDHP). They withdrew the excess on March 1, 2026, before filing. The HSA had earned $30 on the excess between contribution and withdrawal.

```
Custodian sends Code 2 1099-SA:
  Box 1 = $730 ($700 excess + $30 earnings)
  Box 2 = $30
  Box 3 = 2

User reporting (the 1099-SA is for 2026, the year of the withdrawal):
  2025 Form 8889: Line 2 $5,000, Line 13 $4,300; the $700 is not an excess for Form 5329 because it was withdrawn by the due date
  2026 Form 8889: Line 14a $730, Line 14b $730, Line 14c $0, Line 16 $0
  2026 Schedule 1 Line 8z ("Other income"): $30 (Box 2 earnings)
  No 20% additional tax; Form 5329 not needed
```

If the excess was NOT withdrawn by the due date, the user owes 6% excise on $700 = $42 for 2025 (and again for each later year the excess remains).

---

## Code 3 — Disability

**Meaning**: The account holder became disabled (within meaning of IRC §72(m)(7)) and took a distribution. "Disabled" requires a physician's certification that the impairment prevents substantial gainful activity and is expected to last 12+ months or result in death.

**Frequency**: Uncommon. The custodian must mark Code 3 only when the account holder has documented disability — usually evidenced by a Social Security disability determination or physician's letter on file.

**Tax treatment**:
- Distributions used for QME: **not taxable** (same as Code 1)
- Distributions NOT used for QME: **taxable as ordinary income**
- **No 20% additional tax** (the disability exception under IRC §223(f)(4)(B) waives the penalty)

**Authority**: IRC §223(f)(4)(B), IRC §72(m)(7) (disability definition).

**Worked example**:

Disabled account holder receives Code 3 Box 1 = $8,000. Used $5,500 for QME (medications, durable medical equipment, in-home care).

```
Form 8889 Line 14a: $8,000
Line 14c: $8,000
Line 15 (QME): $5,500
Line 16 (taxable): $2,500
Line 17a: "Disability" exception
Line 17b: $0  (penalty waived)

Schedule 1 Line 8f: $2,500
Schedule 2 Line 17c: $0
```

---

## Code 4 — Death distribution other than code 6

**Meaning**: The custodian learned of the account holder's death and made a distribution **in the year of death** (to any beneficiary), or made a payment to the **estate** after the year of death (2025 Instructions for Forms 1099-SA and 5498-SA, "Death of Account Holder" and Box 3).

**Frequency**: Rare; only relevant when an HSA holder dies.

**Tax treatment** (non-spouse beneficiary or estate; a spouse beneficiary simply becomes the account holder, IRC §223(f)(8)(A)):
- The account stops being an HSA on the date of death (IRC §223(f)(8)(B)(i))
- The **FMV on the date of death (Box 4)** is income for the **year of death**: to the beneficiary, or on the decedent's final return if the estate is the beneficiary
- A beneficiary other than the estate reduces that amount by the decedent's qualified medical expenses incurred before death and paid within 1 year after death (IRC §223(f)(8)(B)(ii)(I)); this goes on Form 8889 Line 15
- Earnings after the date of death (Box 1 − Box 4) are other income in the year received
- **No 20% additional tax** (death exception under IRC §223(f)(4)(B))
- A beneficiary may deduct estate tax attributable to the amount (IRC §223(f)(8)(B)(ii)(II))

**Authority**: IRC §223(f)(8)(B) (non-spouse beneficiary), IRC §223(f)(4)(B) (death exception to 20% tax); 2025 Instructions for Form 8889, "Death of Account Beneficiary".

**Worked example**:

Aunt Joan dies in March 2025. Her HSA had $25,000. She named her nephew Jamal as beneficiary. The custodian distributes $25,000 cash to Jamal in May 2025. Aunt Joan had $1,500 in unpaid medical bills from before her death; Jamal pays them.

```
Custodian sends Code 4 1099-SA to Jamal:
  Box 1 = $25,000
  Box 3 = 4
  Box 4 = $25,000 (FMV on date of death)

Jamal's reporting on his own 2025 Form 1040 (Form 8889 headed "Death of HSA account beneficiary", Part I skipped):
  Line 14a: $25,000 (FMV on date of death)
  Line 15: $1,500 (Aunt Joan's pre-death QME Jamal paid within 1 year of death)
  Line 16: $25,000 − $1,500 = $23,500 → Schedule 1 Line 8f
  Line 17b: $0 (death exception)
  Earnings after death: Box 1 − Box 4 = $0
```

The $25,000 is NOT subject to the 20% additional tax (death exception).

**Estate tax**: The $25,000 was part of Aunt Joan's gross estate at her death — handled separately on Form 706 if the estate exceeds the federal exemption; any estate tax attributable to it is deductible by Jamal (IRC §223(f)(8)(B)(ii)(II)).

---

## Code 5 — Prohibited transaction

**Meaning**: The account holder engaged in a prohibited transaction with the HSA — e.g., sold a personal asset to the HSA or otherwise self-dealt. Under IRC §223(e)(2) and IRC §4975, the account stops being an HSA as of **January 1 of the year of the prohibited transaction** and its FMV on that date goes on Form 8889 Line 14a. Pledging the HSA as security for a loan is a separate rule: only the pledged portion is treated as distributed and is reported as income on Schedule 1, Line 8f (2025 Instructions for Form 8889, "Deemed Distributions From HSAs").

**Frequency**: Very rare.

**Tax treatment**:
- The **entire account balance** is treated as distributed
- **Fully taxable as ordinary income** unless used for QME (which it never is, by definition — a prohibited transaction is not a QME)
- **20% additional tax** generally applies (2025 Instructions for Form 8889, "Deemed Distributions"); the after-65 exception still applies if the deemed distribution falls after the 65th birthday
- Account is essentially terminated; future contributions are not deductible

**Authority**: IRC §223(e)(2), IRC §4975 (prohibited transactions).

**Action**: Refer the user to a tax professional immediately. The consequences extend beyond this single 1099-SA — the user may need to amend prior years and the entire HSA structure may need to be unwound.

---

## Code 6 — Death distribution after year of death to a nonspouse beneficiary

**Meaning**: The account holder died in an earlier year, and the custodian paid a **nonspouse beneficiary other than an estate** after the year of death (2025 Instructions for Forms 1099-SA and 5498-SA, Box 3). Never used together with Code 4.

**Tax treatment**:
- The account stopped being an HSA on the date of death (IRC §223(f)(8)(B)(i))
- The **FMV on the date of death** is income for the **year of death**, even though the money arrived later (Form 1099-SA, Instructions for Recipient, "Nonspouse beneficiary"). Box 4 shows that FMV reduced by the decedent's qualified medical expenses the custodian paid within 1 year after death
- If the beneficiary did not report it for the year of death, they need an amended return for that year ([`../../form-1040-x/SKILL.md`](../../form-1040-x/SKILL.md))
- Earnings after death (Box 1 − Box 4) are other income for the year received
- **No 20% additional tax** (death exception, IRC §223(f)(4)(B))

**Worked example**:

Mother dies November 20, 2025, naming her son as beneficiary. The FMV on the date of death is $30,000. The custodian pays the son $30,450 on February 10, 2026 and issues a 2026 Form 1099-SA.

```
Custodian sends Code 6 1099-SA (for 2026):
  Box 1 = $30,450
  Box 3 = 6
  Box 4 = $30,000 (FMV on date of death)

Son's reporting:
  2025 Form 8889 ("Death of HSA account beneficiary"): Line 14a $30,000; Line 15 any of mother's pre-death QME he paid within 1 year; Line 16 → 2025 Schedule 1 Line 8f
  2026 return: $450 (Box 1 − Box 4) as other income
  Schedule 2 Line 17c: $0 in both years
```

**Spouse beneficiary (no special code)**: the HSA is treated as the surviving spouse's own HSA (IRC §223(f)(8)(A)); there is no taxable event at death, later distributions to the spouse are reported with Code 1, and the spouse reports them on their own Form 8889.

---

## Quick decision table

| Code | Taxable? | 20% penalty? | Other forms |
|------|----------|--------------|-------------|
| 1 | Non-QME portion | Yes (before 65, no exception) | Form 8889 |
| 2 | Box 2 earnings only (if withdrawn by due date) | No | Form 8889 Lines 14a/14b; Form 5329 only if the excess stayed past the due date |
| 3 | Non-QME portion | No (disability exception) | Form 8889 |
| 4 | FMV at death less pre-death QME paid within 1 year, for the year of death | No (death exception) | Beneficiary's Form 8889, or decedent's final return if the estate |
| 5 | Entire account (FMV on January 1) | Generally yes | Form 8889; consult tax pro |
| 6 | FMV at death for the year of death; earnings after death in year received | No (death exception) | Beneficiary's Form 8889 for the year of death (amend if needed) |

---

## Authority cited

- IRC §223(f)(1) — distribution treatment
- IRC §223(f)(4) — 20% additional tax + exceptions (age 65, disability, death)
- IRC §223(f)(3) — return of excess contribution
- IRC §223(f)(8) — death of account beneficiary ((A) spouse treated as account beneficiary; (B) other beneficiaries: FMV income, (B)(ii)(I) pre-death QME reduction, (B)(ii)(II) estate tax deduction)
- IRC §223(e)(2) — prohibited transactions
- IRC §4973 — excise on excess contributions
- IRC §4975 — prohibited transaction tax
- IRC §72(m)(7) — disability definition
- IRS Instructions for Forms 1099-SA and 5498-SA (current revision) — Box 3 code definitions
- Pub 969 — HSAs and Other Tax-Favored Health Plans
