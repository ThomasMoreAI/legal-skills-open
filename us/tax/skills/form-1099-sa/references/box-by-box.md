# Form 1099-SA Box-by-Box Reference

Complete lookup for every box on Form 1099-SA. Use this when the agent needs to confirm what a box means or how to interpret an entry.

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

### Aggregation rule

If the user has **multiple HSAs at different custodians**, each custodian sends a separate 1099-SA. The user aggregates Box 1 across all 1099-SAs on Form 8889 Line 14a.

If the user has multiple HSAs at the **same custodian** (some custodians issue separate accounts for "spending" vs. "investment"), the custodian usually consolidates into a single 1099-SA. But not always — if two 1099-SAs arrive from the same custodian with different account numbers, treat each separately and aggregate on Line 14a.

---

## Box 2 — Earnings on excess contributions

Populated **only if Box 3 = Code 2** (excess contribution + earnings withdrawn).

If the user contributed too much to their HSA in a year (over the IRC §223(b) annual limit, e.g., $4,300 self-only / $8,550 family for 2025), they have until the tax filing deadline (typically April 15) to withdraw the excess plus any earnings. The custodian issues a Code 2 1099-SA showing:

- Box 1 = total distributed (excess + earnings)
- Box 2 = earnings portion only (this is the taxable income)
- Box 3 = Code 2

**Box 2 is taxable as ordinary income** on Form 8889 Line 16. The excess contribution itself was already accounted for separately — if not withdrawn by the deadline, it's subject to a 6% excise tax under IRC §4973 (reported on Form 5329).

If Box 2 = $0 (which it will be for most filers), no special treatment needed.

---

## Box 3 — Distribution code

A single digit identifying the type of distribution. Six possible values:

| Code | Meaning |
|------|---------|
| 1 | Normal distribution |
| 2 | Excess contributions returned + earnings |
| 3 | Disability |
| 4 | Death distribution to non-spouse beneficiary or estate |
| 5 | Prohibited transaction |
| 6 | Death distribution to spouse beneficiary |

Full treatment of each code: see [`distribution-codes.md`](./distribution-codes.md).

The code drives:
- Whether the distribution is taxable (most are taxable on the non-QME portion only; Code 5 and Code 4 are mostly taxable; Code 6 to spouse is not)
- Whether the 20% additional tax applies (yes for Code 1 if under 65; no for Codes 3, 4, 6)
- Whether other forms must be filed (Code 2 → Form 5329; Code 5 → consult a tax pro)

---

## Box 4 — FMV on date of death

Populated **only if the account holder died** during the tax year and the 1099-SA reflects a death distribution (Code 4 or Code 6).

The fair market value of the HSA on the date of death. Used by:

- **Code 4 (non-spouse beneficiary or estate)**: the beneficiary inherits cash equal to Box 1 (which equals or is close to Box 4). The amount is fully taxable as ordinary income to the beneficiary in the year received. Box 4 establishes the basis for any subsequent investment gain (none, typically — the funds are distributed in cash).
- **Code 6 (spouse beneficiary)**: the spouse takes over the HSA as their own. Box 4 establishes the new account value at the spouse's takeover. Not taxable.

If Box 4 > Box 1, the difference indicates earnings between date of death and date of distribution — those earnings may be taxable to the recipient depending on jurisdiction. Refer to a tax pro.

For most filers (account holder did not die), Box 4 = $0 / blank.

---

## Box 5 — Account type

Three checkboxes; one is marked:

| Checkbox | Account type | Recipient files |
|----------|--------------|-----------------|
| HSA | Health Savings Account (IRC §223) | **Form 8889 Part II** |
| Archer MSA | Archer Medical Savings Account (IRC §220) — pre-2008 enrollment, mostly grandfathered | **Form 8853 Part II Section A** |
| Medicare Advantage MSA | Medicare Advantage MSA (IRC §138) — for Medicare beneficiaries on certain MA plans | **Form 8853 Part II Section B** |

This skill primarily covers HSA. For Archer and MA MSA, see [`archer-and-ma-msa.md`](./archer-and-ma-msa.md).

---

## "Corrected" checkbox

If the 1099-SA has a "CORRECTED" indicator at the top, it supersedes the prior 1099-SA from the same custodian for the same year. Use only the corrected version.

If the user has both an original and a corrected 1099-SA: discard the original; use only the corrected.

If the user files using the original and the correction arrives later, file an amended return (Form 1040-X).

---

## Sample 1099-SA interpretation

Example: HealthEquity issues this 1099-SA to Lisa Park for tax year 2025:

```
PAYER: HealthEquity Inc., 15 W Scenic Pointe Dr Ste 100, Draper UT 84020, EIN 52-2153069
RECIPIENT: Lisa Park, 555 Main St, Brooklyn NY 11201, SSN ***-**-1234

Box 1: $4,250
Box 2: $0
Box 3: 1
Box 4: $0
Box 5: [HSA checked]
```

Interpretation:
- Lisa took $4,250 in distributions from her HealthEquity HSA in 2025
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
- Line 17b (20% additional tax, assuming Lisa is under 65) = $450 × 0.20 = $90

Lisa owes ordinary income tax on $450 plus a $90 additional tax penalty.

---

## Authority cited

- IRC §223 — Health Savings Accounts
- IRC §220 — Archer MSAs
- IRC §138 — Medicare Advantage MSAs
- IRC §4973 — excise tax on excess contributions
- IRS Instructions for Forms 1099-SA and 5498-SA — annual revision
- Treasury Reg. §1.223-2 — HSA distribution rules
- IRS Notice 2004-50 — HSA Q&A guidance

## Verify before filing

- That Box 5 matches the actual account type (HSA / Archer / MA MSA)
- That Box 3 distribution code matches the user's situation (e.g., a Code 1 from a custodian when the user actually inherited the HSA → custodian error; request correction)
- That Box 1 ties to the user's HSA portal "Total distributions" report
- That all 1099-SAs from all custodians are received before filing — if the user expects a 1099-SA but hasn't received it by mid-February, contact the custodian
