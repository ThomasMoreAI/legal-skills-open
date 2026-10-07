# Example: MFJ Couple with 2 Qualifying Children, AGI $150K (Full $4,400 CTC)

The "everything works as intended" pattern. Married couple filing jointly, two young children, AGI well below the phase-out threshold, sufficient tax liability to absorb the full non-refundable CTC. No ACTC needed.

Line numbers are from the 2025 Schedule 8812 and 2025 Form 1040.

## The filers

- **Names**: Jordan and Priya Mehta
- **Filing status**: MFJ
- **AGI**: $150,000 (Form 1040 line 11a)
- **MAGI**: $150,000 (no foreign earned income exclusion; Schedule 8812 line 3)
- **Earned income**: $148,000 (Jordan's $90K W-2 + Priya's $58K W-2; the other $2,000 is bank interest)
- **SSNs**: both spouses have SSNs valid for employment
- **Tax year**: 2025 (filing in 2026)

## Dependents

| Dependent     | Relationship | Age 12/31 | SSN before due date | Classification |
|---------------|--------------|-----------|------------------|----------------|
| Aanya Mehta   | Daughter     | 8         | Yes              | Qualifying child (CTC) |
| Rohan Mehta   | Son          | 5         | Yes              | Qualifying child (CTC) |

Both children:
- Lived with the Mehtas all year
- Did not provide their own support
- Are U.S. citizens
- Did not file joint returns
- Have SSNs issued at birth

Both are qualifying children for CTC.

- **N_CTC** = 2 (line 4)
- **N_ODC** = 0 (line 6)

## Step 3 — Tentative credit

```
Line 5  Tentative CTC = 2 × $2,200 = $4,400
Line 7  Tentative ODC = 0 × $500 = $0
Line 8  Tentative total = $4,400
```

## Step 4 — MAGI phase-out

```
Line 3   MAGI = $150,000
Line 9   Threshold (MFJ) = $400,000
Line 10  Excess = max(0, $150,000 − $400,000) = $0
Line 11  Phase-out reduction = $0
Line 12  Allowed credit = $4,400
```

The Mehtas are well below the phase-out threshold. Full credit available.

## Step 5 — Non-refundable credit (1040 line 19)

The Mehtas' tax computation:

- Standard deduction (MFJ 2025): $31,500 (2025 Form 1040, line 12e margin)
- Taxable income: $150,000 − $31,500 = $118,500
- Tax (2025 MFJ rates, Tax Computation Worksheet because taxable income is $100,000 or more): $11,157 + 22% × ($118,500 − $96,950) = $15,898

Pre-credit tax (Form 1040 line 18): $15,898. No Schedule 3 credits, so Credit Limit Worksheet A (line 13) = $15,898.

```
Line 14  Non-refundable credit = min($4,400, $15,898) = $4,400
```

The full $4,400 fits within tax liability. **Form 1040 line 19 = $4,400**.

## Step 6 — Refundable ACTC

```
Line 16a Leftover = line 12 − line 14
                  = $4,400 − $4,400 = $0  → stop
```

No leftover → no ACTC. **Form 1040 line 28 = $0**.

The Mehtas don't need ACTC because their tax liability fully absorbed the non-refundable CTC. They get the full $4,400 benefit.

## The completed worksheet

```markdown
# Schedule 8812 — DRAFT WORKSHEET for tax year 2025

## Filing facts
- Filing status: MFJ
- Filer's MAGI: $150,000
- Earned income: $148,000
- Tax before credits (1040 line 18): $15,898
- Credit Limit Worksheet A (line 13): $15,898
- Filer SSN valid for employment before due date: Yes (both spouses)
- Phase-out threshold (line 9): $400,000 (MFJ)

## Dependents classified
| Dependent     | Relationship | Age 12/31 | SSN/ITIN | Classification |
|---------------|--------------|-----------|----------|----------------|
| Aanya Mehta   | Daughter     | 8         | SSN      | Qualifying child (CTC) |
| Rohan Mehta   | Son          | 5         | SSN      | Qualifying child (CTC) |

- Line 4 N_CTC: 2
- Line 6 N_ODC: 0

## Part I — lines 1–14
- Line 1  AGI: $150,000
- Line 2d: $0
- Line 3  MAGI: $150,000
- Line 5  CTC tentative: 2 × $2,200 = $4,400
- Line 7  ODC tentative: 0 × $500 = $0
- Line 8  **Tentative total**: $4,400
- Line 9  Threshold: $400,000
- Line 10 Excess: $0
- Line 11 Phase-out reduction: $0
- Line 12 **Allowed credit**: $4,400
- Line 13 Credit Limit Worksheet A: $15,898
- Line 14 Non-refundable credit: min($4,400, $15,898) = $4,400 → **1040 line 19**

## Part II-A — lines 15–27
- Line 15 Reserved
- Line 16a Leftover: $4,400 − $4,400 = $0 → stop
- Line 27 ACTC: $0 → **1040 line 28**: $0

## Verification
- Line 14 + line 27 ≤ line 12: $4,400 + $0 = $4,400 ✓
- Each dependent classified once: ✓
- SSN-before-due-date verified for the filers and each qualifying child: ✓

## Validation summary
- Math: all checks passed
- Sanity:
  - Both children under 17 with SSN → CTC eligible
  - MAGI well below $400K threshold → no phase-out
  - Tax liability ($15,898) fully absorbs $4,400 non-refundable credit → no ACTC
- Next steps:
  - Form 1040 line 19: $4,400
  - Form 1040 line 28: $0
  - Tax after CTC (line 22): $15,898 − $4,400 = $11,498
  - Refund or balance due depends on withholding (1040 line 25a)

## Sources cited in this draft
- IRS Schedule 8812 (Form 1040) (2025)
- IRS Instructions for Schedule 8812 (2025)
- IRC §24(h)(2) — $2,200 credit per child
- IRC §24(b)(1), §24(h)(3) — phase-out (no impact at $150K MFJ)
- IRC §24(c) — qualifying child definition
- IRC §24(h)(7) — SSN requirement
- Rev. Proc. 2024-40 — 2025 tax rate tables
```

## Why each non-obvious choice

**Why $2,200 per child (and not the 2021 ARPA $3,000-$3,600)?** The American Rescue Plan Act of 2021 expanded CTC for tax year 2021 only. For 2025, P.L. 119-21 (OBBBA) §70104 set the credit at $2,200 per child and made the post-2017 rules permanent (2025 Schedule 8812 line 5). The Mehtas get $2,200/child, not the higher 2021 amount.

**Why isn't there any ACTC?** ACTC is the refundable portion of CTC. It only matters when the non-refundable CTC was capped by tax liability. The Mehtas' $15,898 tax liability is much larger than the $4,400 credit, so the full credit is non-refundable. ACTC = $0 by design.

**Why not also claim Earned Income Tax Credit?** EITC has its own phase-out and AGI limits. For MFJ with 2 children, the EITC fully phases out at $64,430 AGI for 2025 (Rev. Proc. 2024-40 §2.06). The Mehtas' AGI of $150K is far above the EITC phase-out — not eligible. EITC is on Form 1040 line 27a (Schedule EIC), not Schedule 8812.

**Why not also claim Childcare Credit?** Form 2441 (Child and Dependent Care Credit) is a separate credit for daycare expenses while both parents work. The Mehtas may or may not qualify (they didn't mention childcare expenses). If they do, that credit goes on Schedule 3 line 2, and Credit Limit Worksheet A subtracts it before the CTC (line 13 would fall but still exceed $4,400).

**Audit defense**: the Mehtas' return shows:
1. Both children listed as dependents on Form 1040 with SSNs
2. "Child tax credit" box checked in row (7) for both children
3. Schedule 8812 properly completed
4. MAGI well below phase-out → no risk of phase-out adjustment
5. Birth certificates and Social Security cards in the file (audit defense materials)

The IRS may match the children's SSNs against records to confirm they weren't claimed on another return. As long as the Mehtas were the only claimants, no issue.
