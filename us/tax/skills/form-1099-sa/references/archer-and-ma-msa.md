# Archer MSA and Medicare Advantage MSA Distributions

Most 1099-SAs the agent encounters will have Box 5 = HSA. But Form 1099-SA also reports distributions from two other (much rarer) account types: Archer MSAs and Medicare Advantage MSAs. These flow to **Form 8853**, not Form 8889.

---

## Archer Medical Savings Account (Archer MSA)

### Background

Archer MSAs were created by the Health Insurance Portability and Accountability Act (HIPAA) in 1996 as a pilot program. New Archer MSAs **could not be opened after December 31, 2007** (the program was effectively replaced by HSAs starting in 2004). Existing Archer MSAs may continue to receive contributions if the account holder remains eligible.

### Eligibility (legacy)

- Self-employed individual or employee of a small employer (≤50 employees) who had an Archer MSA before the cutoff
- Covered by a high-deductible health plan (HDHP) — slightly different definition than HSA HDHP
- Must NOT be covered by other non-HDHP health insurance

### Contribution limits

Different from HSAs and inflation-adjusted yearly. See Pub 969.

### Tax treatment of distributions

Substantially similar to HSAs:
- **Distributions for QME** (defined under IRC §220 — same general definition): not taxable
- **Distributions for non-QME**: taxable as ordinary income + **15% additional tax** (NOT 20% — Archer MSAs use a 15% rate per IRC §220(f)(4))
- Exception to the 15% additional tax: age 65+, disability, death

### Form 8853 Part II Section A

The recipient files **Form 8853 Part II Section A**:

| Line | Field |
|------|-------|
| 6 | Total distributions from Archer MSAs |
| 7 | Distributions used for QME |
| 8 | Subtract Line 7 from Line 6 (taxable portion) |
| 9 | Additional 15% tax (Line 8 × 0.15) — unless exception |

Form 8853 Part I handles Archer MSA contributions; Part II handles distributions; Part III handles long-term care insurance contracts (separate area).

The taxable portion (Line 8) flows to **Schedule 1 Line 8f** alongside any HSA taxable distributions. The 15% additional tax (Line 9) flows to **Schedule 2 Line 17c** alongside the HSA 20% additional tax.

---

## Medicare Advantage MSA (MA MSA)

### Background

Medicare Advantage MSAs are HSAs designed for Medicare beneficiaries enrolled in certain "high-deductible Medicare Advantage" plans. The MA plan deposits funds into the MSA on the beneficiary's behalf; the beneficiary uses the MSA to pay deductibles and qualified medical costs.

### Eligibility

- Medicare-eligible (typically 65+, but earlier with disability)
- Enrolled in a participating MA plan with an MSA option
- Funded by the MA plan, not the beneficiary (the beneficiary cannot contribute)

### Tax treatment of distributions

Substantially similar to HSAs:
- **Distributions for QME**: not taxable
- **Distributions for non-QME**: taxable as ordinary income + **50% additional tax** (significantly higher than HSA's 20% — IRC §138(c)(2))
- Exception to the 50% additional tax: there is **no age exception** for MA MSAs (the recipient is already a Medicare beneficiary), but disability and death exceptions apply

### Form 8853 Part II Section B

The recipient files **Form 8853 Part II Section B**:

| Line | Field |
|------|-------|
| 10 | Total distributions from MA MSAs |
| 11 | Distributions used for QME |
| 12 | Subtract Line 11 from Line 10 (taxable portion) |
| 13a | Net taxable amount (special calc — see Form 8853 instructions) |
| 13b | Additional 50% tax (Line 13a × 0.50) — unless exception |

The taxable portion flows to **Schedule 1 Line 8f**. The 50% additional tax flows to **Schedule 2 Line 17c**.

---

## Quick comparison: HSA vs. Archer MSA vs. MA MSA

| Attribute | HSA | Archer MSA | MA MSA |
|-----------|-----|------------|--------|
| Authority | IRC §223 | IRC §220 | IRC §138 |
| Recipient form | Form 8889 | Form 8853 Part II Sec A | Form 8853 Part II Sec B |
| New accounts allowed? | Yes (since 2004) | No (closed Dec 2007) | Yes (Medicare-only) |
| QME definition | IRC §223(d)(2) | IRC §220(d)(2) (same as HSA) | IRC §138(b) (same as HSA) |
| Non-QME ordinary tax | Yes | Yes | Yes |
| Additional tax % | 20% | 15% | 50% |
| Age 65 exception | Yes | Yes | N/A (already Medicare) |
| Disability exception | Yes | Yes | Yes |
| Death exception | Yes | Yes | Yes |
| Spouse rollover at death | Yes | Yes | Yes |

---

## Identifying the right form on the 1099-SA

The 1099-SA Box 5 has three checkboxes — exactly one is marked:
- "HSA" → Form 8889
- "Archer MSA" → Form 8853 Part II Section A
- "Medicare Advantage MSA" → Form 8853 Part II Section B

If Box 5 is unmarked or has multiple boxes marked, the 1099-SA is defective — request a correction from the custodian.

---

## Authority cited

- IRC §220 — Archer MSAs
- IRC §220(f) — Archer MSA distributions
- IRC §220(f)(4) — 15% additional tax
- IRC §138 — Medicare Advantage MSAs
- IRC §138(c) — MA MSA distributions
- IRC §138(c)(2) — 50% additional tax
- IRS Form 8853 and instructions
- Pub 969 — covers HSAs, Archer MSAs, MA MSAs, Health FSAs, HRAs

## Verify before filing

- Whether the user's MA MSA is from a current Medicare Advantage plan with MSA option (verify enrollment with the plan)
- Whether the user's Archer MSA is still active (some custodians have wound them down; the user may have rolled into an HSA at some point)
- Form 8853 Section B current line numbering (the form is updated periodically and line numbers shift)
