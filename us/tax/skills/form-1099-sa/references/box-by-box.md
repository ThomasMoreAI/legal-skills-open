# Form 1099-SA Box-by-Box Reference

Complete lookup for every box on Form 1099-SA. Use this when the agent needs to confirm what a box means or how to interpret an entry. Verified against Form 1099-SA (Rev. April 2025) and the 2025 Instructions for Forms 1099-SA and 5498-SA; re-check https://www.irs.gov/forms-pubs/about-form-1099-sa for a newer revision.

---

## Header (payer and recipient information)

### Payer

| Field | What it means |
|-------|---------------|
| PAYER'S name, address, ZIP, federal ID number | The HSA / MSA custodian (Fidelity Investments, HealthEquity, Lively, Optum Bank, WEX/Discovery Benefits, Inspira/PayFlex, etc.). The TIN is the custodian's EIN. |
| PAYER'S phone number | Custodian customer service. Useful if the user needs to dispute a 1099-SA entry. |

### Recipient

| Field | What it means |
|-------|---------------|
| RECIPIENT'S name | Account holder's legal name. Should match Form 1040. |
| RECIPIENT'S TIN | Account holder's SSN (or ITIN). The custodian collected this on Form W-9 at account opening. |
| RECIPIENT'S address | Account holder's address on file with the custodian. If outdated, the user should update with the custodian (does not affect the IRS filing — the SSN is the lookup key). |
| Account number | Custodian's internal account number. Useful if the user has multiple HSAs at the same custodian. |

---

## Box 1 — Gross distribution

The total dollar amount distributed from the account during the calendar year. Includes:

- HSA debit card swipes (each pharmacy / doctor / retailer charge)
- ATM withdrawals from the HSA
- Online transfers from HSA to checking
- Custodian-cut checks for reimbursement
- Direct payments by the custodian to providers (rare; some HSAs offer "pay provider directly" feature)
- Investment sub-account withdrawals (when the HSA has a brokerage tier and the user sells investments to fund a distribution)

Excludes:

- **Trustee-to-trustee transfers** between HSAs (not a distribution; not reported on 1099-SA)
- **Direct contributions** (those go on Form 5498-SA from the custodian, not 1099-SA)
- **Investment gains within the HSA** (untaxed and unreported)
- **Excess employer contributions (and earnings) returned to the employer**, and a **mistaken distribution the user repaid** (2025 Instructions for Forms 1099-SA and 5498-SA, Box 1 and "HSA Mistaken Distributions")

### Aggregation rule

If the user has **multiple HSAs at different custodians**, each custodian sends a separate 1099-SA. The user aggregates Box 1 across all 1099-SAs on Form 8889 Line 14a.

If the user has multiple HSAs at the **same custodian** (some custodians issue separate accounts for "spending" vs. "investment"), the custodian usually consolidates into a single 1099-SA. But not always — if two 1099-SAs arrive from the same custodian with different account numbers, treat each separately and aggregate on Line 14a.

---

## Box 2 — Earnings on excess contributions

Populated **only if Box 3 = Code 2** (excess contribution + earnings withdrawn).

If the user contributed too much to their HSA in a year (over the IRC §223(b) annual limit, e.g., $4,300 self-only / $8,550 family for 2025; $4,400 / $8,750 for 2026), they have until the due date of their return, **including extensions**, to withdraw the excess plus any earnings (IRC §223(f)(3)(A)). The custodian issues a Code 2 1099-SA for the year of the withdrawal showing:

- Box 1 = total distributed (excess + earnings)
- Box 2 = earnings portion only (this is the taxable income)
- Box 3 = Code 2

**Box 2 is taxable as ordinary income** ("Other income", Schedule 1 Line 8z) for the year the withdrawal is received; the excess and earnings go on Form 8889 Lines 14a and 14b, so they do not reach Line 16. If the excess was not withdrawn by the due date, it's subject to a 6% excise tax under IRC §4973 for each year it remains (Form 5329 Part VII).

If Box 2 = $0 (which it will be for most filers), no special treatment needed.

---

## Box 3 — Distribution code

A single digit identifying the type of distribution. Six possible values:

| Code | Meaning (Form 1099-SA, Rev. April 2025) |
|------|---------|
| 1 | Normal distribution (also a spouse beneficiary after the year of death) |
| 2 | Excess contributions |
| 3 | Disability |
| 4 | Death distribution other than code 6 |
| 5 | Prohibited transaction |
| 6 | Death distribution after year of death to a nonspouse beneficiary |

Full treatment of each code: see [`distribution-codes.md`](./distribution-codes.md).

The code drives:
- Whether the distribution is taxable (most are taxable on the non-QME portion only; Codes 4 and 6 make the FMV at death taxable for the year of death; Code 5 makes the whole account taxable)
- Whether the 20% additional tax applies (yes for Code 1 before 65; no for Codes 3, 4, 6)
- Whether other forms must be filed (Code 2 → Form 5329 only if the excess stayed past the due date; Code 5 → consult a tax pro)

---

## Box 4 — FMV on date of death

Populated **only if the account holder died** and the 1099-SA reflects a death distribution (Code 4 in the year of death or to the estate; Code 6 to a nonspouse beneficiary after the year of death).

The fair market value of the HSA on the date of death (for a distribution after the year of death, reduced by the decedent's qualified medical expenses paid within 1 year after death). Used by:

- **Non-spouse beneficiary other than the estate (Code 4 or 6)**: the FMV is income for the **year the account owner died**, even if the money came in a later year. It goes on Form 8889 Line 14a under the heading "Death of HSA account beneficiary"; the decedent's pre-death medical bills the beneficiary paid within 1 year after death go on Line 15.
- **Estate (Code 4)**: the FMV is included on the decedent's final income tax return.
- **Spouse beneficiary**: no Box 4 death distribution; the HSA becomes the spouse's own (IRC §223(f)(8)(A)).

If Box 1 > Box 4, the difference is earnings after the date of death; it is taxable to the recipient as "Other income" for the year received (Form 1099-SA, Instructions for Recipient, "Nonspouse beneficiary").

For most filers (account holder did not die), Box 4 = $0 / blank.

---

## Box 5 — Account type

Three checkboxes; one is marked:

| Checkbox | Account type | Recipient files |
|----------|--------------|-----------------|
| HSA | Health Savings Account (IRC §223) | **Form 8889 Part II** |
| Archer MSA | Archer Medical Savings Account (IRC §220) — pre-2008 enrollment, mostly grandfathered | **Form 8853 Section A, Part II (lines 6a–9b)** |
| Medicare Advantage MSA | Medicare Advantage MSA (IRC §138) — for Medicare beneficiaries on certain MA plans | **Form 8853 Section B (lines 10–13b)** |

This skill primarily covers HSA. For Archer and MA MSA, see [`archer-and-ma-msa.md`](./archer-and-ma-msa.md).

---

## "Corrected" checkbox

If the 1099-SA has a "CORRECTED" indicator at the top, it supersedes the prior 1099-SA from the same custodian for the same year. Use only the corrected version.

If the user has both an original and a corrected 1099-SA: discard the original; use only the corrected.

If the user files using the original and the correction arrives later, file an amended return (Form 1040-X).

---

## Sample 1099-SA interpretation

Example: Lisa's HSA custodian issues this 1099-SA to Lisa Park for tax year 2025:

```
PAYER: <HSA custodian name, address, TIN>
RECIPIENT: Lisa Park, <address>, SSN ***-**-1234

Box 1: $4,250
Box 2: $0
Box 3: 1
Box 4: $0
Box 5: [HSA checked]
```

Interpretation:
- Lisa took $4,250 in distributions from her HSA in 2025
- All a "normal" distribution (Code 1)
- No excess contribution earnings
- Account holder is alive (Box 4 = $0)
- This is an HSA → Lisa files Form 8889 Part II

Lisa now needs to determine, separately, how much of the $4,250 went to qualified medical expenses. If she paid $3,800 in QME and used $450 to buy a non-qualified item (gym membership without doctor's note, for example):

- Form 8889 Line 14a = $4,250
- Line 14b (rollovers) = $0
- Line 14c = $4,250
- Line 15 (QME) = $3,800
- Line 16 (taxable) = $4,250 − $3,800 = $450
- Line 17b (20% additional tax, assuming the distributions were made before Lisa turned 65) = $450 × 0.20 = $90

Lisa owes ordinary income tax on $450 plus a $90 additional tax penalty.

---

## Authority cited

- IRC §223 — Health Savings Accounts
- IRC §220 — Archer MSAs
- IRC §138 — Medicare Advantage MSAs
- IRC §4973 — excise tax on excess contributions
- IRS Instructions for Forms 1099-SA and 5498-SA (2025; Rev. December 2026 for 2026 distributions)
- IRS Notice 2004-50 — HSA Q&A guidance

## Verify before filing

- That Box 5 matches the actual account type (HSA / Archer / MA MSA)
- That Box 3 distribution code matches the user's situation (e.g., a Code 1 to a nonspouse beneficiary who inherited the HSA → custodian error; request correction. Code 1 is correct for a spouse beneficiary)
- That Box 1 ties to the user's HSA portal "Total distributions" report
- That all 1099-SAs from all custodians are received before filing — if the user expects a 1099-SA but hasn't received it by mid-February, contact the custodian
