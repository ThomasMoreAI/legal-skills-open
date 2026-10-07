# Archer MSA and Medicare Advantage MSA Distributions

Most 1099-SAs the agent encounters will have Box 5 = HSA. But Form 1099-SA also reports distributions from two other (much rarer) account types: Archer MSAs and Medicare Advantage MSAs. These flow to **Form 8853**, not Form 8889. Line numbers below verified against the 2025 Form 8853 (created 3/27/25) and 2025 Instructions for Form 8853; re-check https://www.irs.gov/forms-pubs/about-form-8853 each year.

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
- **Distributions for non-QME**: taxable as ordinary income + **20% additional tax** (IRC §220(f)(4)(A); 2025 Form 8853 line 9b "Additional 20% tax")
- Exception to the 20% additional tax: distributions made after the account holder dies, becomes disabled, or turns 65 (2025 Instructions for Form 8853, "Exceptions to the Additional 20% Tax")

### Form 8853 Section A, Part II

The recipient files **Form 8853 Section A, Part II** (2025 form):

| Line | Field |
|------|-------|
| 6a | Total distributions you and your spouse received from all Archer MSAs |
| 6b | Rollovers to another Archer MSA or an HSA, plus excess contributions (and earnings) withdrawn by the unextended due date |
| 6c | Line 6a − Line 6b |
| 7 | Unreimbursed qualified medical expenses |
| 8 | Taxable Archer MSA distributions: Line 6c − Line 7 (not less than 0) |
| 9a | Checkbox: an exception to the additional 20% tax applies |
| 9b | Additional 20% tax on the part of Line 8 with no exception |

Form 8853 Section A Part I handles Archer MSA contributions; Section A Part II handles Archer distributions; Section B handles Medicare Advantage MSA distributions; Section C handles long-term care insurance contracts.

The taxable portion (Line 8) flows to **Schedule 1 Line 8e** ("Income from Form 8853"). The 20% additional tax (Line 9b) flows to **Schedule 2 Line 17e**.

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
- Exception to the 50% additional tax: there is **no age exception** for MA MSAs (the recipient is already a Medicare beneficiary), but distributions on or after death or disability are excepted (2025 Instructions for Form 8853, "Exceptions to the Additional 50% Tax")
- Only qualified medical expenses of the account holder count (Form 1099-SA, Instructions for Recipient)

### Form 8853 Section B

The recipient files **Form 8853 Section B** (2025 form):

| Line | Field |
|------|-------|
| 10 | Total distributions from all MA MSAs |
| 11 | Unreimbursed qualified medical expenses |
| 12 | Taxable MA MSA distributions: Line 10 − Line 11 (not less than 0) |
| 13a | Checkbox: an exception to the additional 50% tax applies |
| 13b | Additional 50% tax (Additional 50% Tax Worksheet—Line 13b if the account existed on December 31 of the prior year) |

The taxable portion (Line 12) flows to **Schedule 1 Line 8e**. The 50% additional tax (Line 13b) flows to **Schedule 2 Line 17f**.

---

## Quick comparison: HSA vs. Archer MSA vs. MA MSA

| Attribute | HSA | Archer MSA | MA MSA |
|-----------|-----|------------|--------|
| Authority | IRC §223 | IRC §220 | IRC §138 |
| Recipient form | Form 8889 | Form 8853 Sec A Part II | Form 8853 Sec B |
| New accounts allowed? | Yes (since 2004) | No (closed Dec 2007) | Yes (Medicare-only) |
| QME definition | IRC §223(d)(2) | IRC §220(d)(2) (same as HSA) | IRC §138(b) (same as HSA) |
| Non-QME ordinary tax | Yes | Yes | Yes |
| Additional tax % | 20% | 20% | 50% |
| Age 65 exception | Yes | Yes | N/A (already Medicare) |
| Disability exception | Yes | Yes | Yes |
| Death exception | Yes | Yes | Yes |
| Spouse becomes account holder at death | Yes | Yes | Yes (no new contributions) |

---

## Identifying the right form on the 1099-SA

The 1099-SA Box 5 has three checkboxes — exactly one is marked:
- "HSA" → Form 8889
- "Archer MSA" → Form 8853 Section A, Part II
- "Medicare Advantage MSA" → Form 8853 Section B

If Box 5 is unmarked or has multiple boxes marked, the 1099-SA is defective — request a correction from the custodian.

---

## Authority cited

- IRC §220 — Archer MSAs
- IRC §220(f) — Archer MSA distributions
- IRC §220(f)(4) — 20% additional tax
- IRC §138 — Medicare Advantage MSAs
- IRC §138(c) — MA MSA distributions
- IRC §138(c)(2) — 50% additional tax
- IRS Form 8853 and instructions
- Pub 969 — covers HSAs, Archer MSAs, MA MSAs, Health FSAs, HRAs

## Verify before filing

- Whether the user's MA MSA is from a current Medicare Advantage plan with MSA option (verify enrollment with the plan)
- Whether the user's Archer MSA is still active (some custodians have wound them down; the user may have rolled into an HSA at some point)
- Form 8853 Section B current line numbering (the form is updated periodically and line numbers shift)
