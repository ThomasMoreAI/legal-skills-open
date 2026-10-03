# Form 1099-SA Distribution Codes (Box 3)

The single-digit code in Box 3 drives the entire tax treatment of the distribution. There are six valid codes. This file explains each.

---

## Code 1 — Normal distribution

**Meaning**: A regular, voluntary distribution from the HSA / MSA. The account holder withdrew funds — by debit card swipe, ATM, online transfer, check, or claim reimbursement — during the year.

**Frequency**: Most common code. The vast majority of 1099-SAs the agent will see have Code 1.

**Tax treatment**:
- Distributions used for qualified medical expenses (QME): **not taxable**
- Distributions NOT used for QME: **taxable as ordinary income** (Form 8889 Line 16)
- Plus **20% additional tax** on the non-QME portion if account holder is under age 65 (Form 8889 Line 17b)
- Exceptions to the 20% tax: account holder is age 65+, disabled, or died (IRC §223(f)(4)(B)). Code 1 with an exception still produces taxable income but no penalty.

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

**Meaning**: The account holder contributed more than the IRC §223(b) annual limit and is withdrawing the excess (plus any earnings) before the tax filing deadline. Typically initiated by the user filing a "return of excess contribution" form with the custodian.

**Frequency**: Uncommon. Occurs when a user makes an error or changes coverage mid-year (e.g., moves from family HDHP to self-only HDHP, lowering the contribution limit retroactively).

**Tax treatment**:
- **Box 1** (gross distribution = excess + earnings): the **excess portion is NOT taxable** at the distribution stage (it was technically "your money" since the contribution was disallowed)
- **Box 2** (earnings on excess): **taxable as ordinary income** in the year of distribution
- The **6% excise tax** under IRC §4973 may apply on the excess contribution itself; reported on Form 5329 Part VII. If the excess was withdrawn by the tax-filing deadline, the 6% is avoided.

**Authority**: IRC §223(f)(3)(A) (return of excess), IRC §4973 (excise on excess), Treasury Reg. §1.408-11 (mechanics of return-of-excess).

**Worked example**:

User contributed $5,000 to an HSA in 2025 but their actual limit was $4,300 (self-only HDHP). They withdrew the excess on March 1, 2026, before filing. The HSA had earned $30 on the excess between contribution and withdrawal.

```
Custodian sends Code 2 1099-SA:
  Box 1 = $730 ($700 excess + $30 earnings)
  Box 2 = $30
  Box 3 = 2

User reporting:
  Form 8889 Line 16: $30 (Box 2 earnings only)
  No 20% additional tax under IRC §223(f)(4) for excess withdrawals
  Form 5329 Part VII: $0 excise (withdrawn timely)
  
  Schedule 1 Line 8f: $30
  Schedule 2 Line 17c: $0
```

If the excess was NOT withdrawn timely, the user owes 6% excise on $700 = $42 (cumulative each year the excess remains).

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

## Code 4 — Death distribution to non-spouse beneficiary or estate

**Meaning**: The HSA account holder died, and the named beneficiary is **not their spouse** (or there's no beneficiary and the HSA passes to the estate).

**Frequency**: Rare; only relevant when an HSA holder dies.

**Tax treatment**:
- The HSA loses its tax-favored status at the date of death
- **Box 1 is fully taxable as ordinary income** to the beneficiary or estate in the year received
- Exception: amounts paid for the deceased's QME incurred before death (within 1 year of death) can be subtracted (IRC §223(f)(8)(A))
- **No 20% additional tax** (the death exception under IRC §223(f)(4)(B) waives the penalty)
- **Box 4 (FMV on date of death)** establishes the deceased's HSA value for estate tax purposes (separate from income tax)

**Authority**: IRC §223(f)(8)(A) (deceased's QME), IRC §223(f)(4)(B) (death exception to 20% tax).

**Worked example**:

Aunt Joan dies in March 2025. Her HSA had $25,000. She named her nephew Jamal as beneficiary. The custodian distributes $25,000 cash to Jamal in May 2025. Aunt Joan had $1,500 in unpaid medical bills from before her death; Jamal pays them.

```
Custodian sends Code 4 1099-SA to Jamal:
  Box 1 = $25,000
  Box 3 = 4
  Box 4 = $25,000 (FMV on date of death)

Jamal's reporting on his own Form 1040:
  The $25,000 is ordinary income to Jamal in 2025
  Jamal can subtract the $1,500 he paid for Aunt Joan's pre-death QME (within 1 year of death)
  Net taxable: $25,000 − $1,500 = $23,500
  No 20% additional tax (death exception)
  
  Schedule 1 Line 8f: $23,500 (or per state-of-the-art Form 8889 instructions)
  Schedule 2 Line 17c: $0
```

The $25,000 is NOT subject to the 10% early-distribution penalty (HSAs don't have one) or the 20% additional tax (death exception).

**Estate tax**: The $25,000 was part of Aunt Joan's gross estate at her death — handled separately on Form 706 if the estate exceeds the federal exemption.

---

## Code 5 — Prohibited transaction

**Meaning**: The account holder engaged in a prohibited transaction with the HSA — e.g., used HSA assets as collateral for a loan, sold a personal asset to the HSA, or otherwise self-dealt. Under IRC §223(e)(2) and IRC §4975, the **entire HSA is treated as distributed on January 1 of the year of the prohibited transaction**.

**Frequency**: Very rare.

**Tax treatment**:
- The **entire account balance** is treated as distributed
- **Fully taxable as ordinary income** unless used for QME (which it never is, by definition — a prohibited transaction is not a QME)
- **20% additional tax** applies (under 65; and the disability/death exceptions don't apply by their nature)
- Account is essentially terminated; future contributions are not deductible

**Authority**: IRC §223(e)(2), IRC §4975 (prohibited transactions).

**Action**: Refer the user to a tax professional immediately. The consequences extend beyond this single 1099-SA — the user may need to amend prior years and the entire HSA structure may need to be unwound.

---

## Code 6 — Death distribution to spouse beneficiary

**Meaning**: The HSA account holder died, and the named beneficiary is **their spouse**.

**Tax treatment**:
- The surviving spouse **takes over the HSA as their own** (IRC §223(f)(8)(B))
- **Not taxable** at the death event
- The spouse continues filing Form 8889 in future years for the HSA
- Future distributions from the inherited HSA follow the spouse's own age-based rules (e.g., spouse becomes age 65 → no 20% penalty going forward)

**Worked example**:

Husband dies in 2025. Wife is the beneficiary. The custodian retitles the HSA to the wife and issues a Code 6 1099-SA showing the full account value as a "distribution" (to the husband) for IRS reporting purposes — but no tax is due.

```
Custodian sends Code 6 1099-SA:
  Box 1 = $30,000
  Box 3 = 6
  Box 4 = $30,000 (FMV on date of death; informational)
  
Wife's reporting:
  Form 8889 Part II is NOT required for this distribution (Code 6 to spouse)
  The HSA is now in the wife's name; she continues Form 8889 for her own contributions and distributions going forward
  
  Schedule 1 Line 8f: $0
  Schedule 2 Line 17c: $0
```

The custodian issues the 1099-SA primarily to clear the IRS records — the original account was in the husband's SSN and now needs to be transferred. The 1099-SA closes the husband's tax record.

---

## Quick decision table

| Code | Taxable? | 20% penalty? | Other forms |
|------|----------|--------------|-------------|
| 1 | Non-QME portion | Yes (under 65, no exception) | Form 8889 |
| 2 | Box 2 earnings only | No | Form 8889; possibly Form 5329 (excess excise) |
| 3 | Non-QME portion | No (disability exception) | Form 8889 |
| 4 | Yes (less pre-death QME) | No (death exception) | Form 8889 (beneficiary's) |
| 5 | Entire account | Yes (no exception by nature) | Form 8889; consult tax pro |
| 6 | No | No | None — spouse continues normal Form 8889 going forward |

---

## Authority cited

- IRC §223(f)(1) — distribution treatment
- IRC §223(f)(4) — 20% additional tax + exceptions (age 65, disability, death)
- IRC §223(f)(3) — return of excess contribution
- IRC §223(f)(8) — death distributions (subsection A: QME for deceased; subsection B: spouse rollover)
- IRC §223(e)(2) — prohibited transactions
- IRC §4973 — excise on excess contributions
- IRC §4975 — prohibited transaction tax
- IRC §72(m)(7) — disability definition
- IRS Instructions for Forms 1099-SA and 5498-SA (current revision) — Box 3 code definitions
- Pub 969 — HSAs and Other Tax-Favored Health Plans
