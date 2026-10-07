# Example: High-Income MFJ with 3 Children, AGI $450,000 (Partial Phase-Out)

The MAGI phase-out in action. MFJ couple with three qualifying children, MAGI $50,000 above the threshold. The CTC is reduced by $2,500, but most of the credit remains.

Line numbers are from the 2025 Schedule 8812 and 2025 Form 1040.

## The filers

- **Names**: Caroline and Marcus Thornton
- **Filing status**: MFJ
- **AGI**: $450,000
- **MAGI**: $450,000 (no foreign income)
- **Earned income**: $440,000 (W-2 wages: Caroline $260K + Marcus $180K); the other $10,000 of AGI is taxable interest
- **SSNs**: both spouses have SSNs valid for employment
- **Tax year**: 2025 (filing in 2026)

## Dependents

| Dependent             | Relationship | Age 12/31 | SSN before due date | Classification |
|-----------------------|--------------|-----------|------------------|----------------|
| Charlotte Thornton    | Daughter     | 14        | Yes              | Qualifying child (CTC) |
| Henry Thornton        | Son          | 11        | Yes              | Qualifying child (CTC) |
| Eleanor Thornton      | Daughter     | 7         | Yes              | Qualifying child (CTC) |

All three pass the qualifying child tests.

- **N_CTC** = 3 (line 4)
- **N_ODC** = 0 (line 6)

## Step 3 — Tentative credit

```
Line 5  Tentative CTC = 3 × $2,200 = $6,600
Line 7  Tentative ODC = 0 × $500 = $0
Line 8  Tentative total = $6,600
```

## Step 4 — MAGI phase-out

```
Line 3   MAGI = $450,000
Line 9   Threshold (MFJ) = $400,000
Line 10  Excess = $50,000  (already a multiple of $1,000, no rounding)
Line 11  Phase-out reduction = $50,000 × 5% = $2,500

Line 12  Allowed credit = $6,600 − $2,500 = $4,100
```

The Thorntons lose $2,500 of credit due to the phase-out. They retain $4,100 of the $6,600 tentative.

### What if their MAGI were $450,500?

```
Excess (raw) = $50,500
Line 10 (rounded UP) = $51,000  (round $500 up to next $1,000)
Line 11 = $51,000 × 5% = $2,550
Line 12 = $6,600 − $2,550 = $4,050
```

Notice: the $500 of additional MAGI rounds up to a full $1,000 of excess, costing $50 of credit. This is how the "round up" rule bites — even a tiny amount over a $1,000 step costs $50.

## Step 5 — Non-refundable credit (1040 line 19)

The Thorntons' tax computation:

- Standard deduction (MFJ 2025): $31,500
- Taxable income: $450,000 − $31,500 = $418,500
- Tax (2025 MFJ rates, Tax Computation Worksheet): $80,398 + 32% × ($418,500 − $394,600) = $88,046
- No AMT: tentative minimum tax on $450,000 AMTI less the $137,000 MFJ exemption is $82,858, below the regular tax
- Additional Medicare Tax (0.9% × ($440,000 − $250,000) = $1,710) goes on Schedule 2 line 11 → Form 1040 line 23, not line 18

Pre-credit tax (Form 1040 line 18): $88,046. No Schedule 3 credits, so Credit Limit Worksheet A (line 13) = $88,046.

```
Line 14  Non-refundable credit = min($4,100, $88,046) = $4,100
```

The full $4,100 fits within tax liability. **Form 1040 line 19 = $4,100**.

## Step 6 — Refundable ACTC (1040 line 28)

```
Line 16a Leftover = $4,100 − $4,100 = $0  → stop
```

No leftover → no ACTC. **Form 1040 line 28 = $0**.

(Even if there were leftover, Part II-B might apply because line 16b would be 3 × $1,700 = $5,100. But with $0 on line 16a, the form stops.)

## The completed worksheet

```markdown
# Schedule 8812 — DRAFT WORKSHEET for tax year 2025

## Filing facts
- Filing status: MFJ
- Filer's MAGI: $450,000
- Earned income: $440,000
- Tax before credits (1040 line 18): $88,046
- Credit Limit Worksheet A (line 13): $88,046
- Filer SSN valid for employment before due date: Yes (both spouses)
- Phase-out threshold (line 9): $400,000 (MFJ)

## Dependents classified
| Dependent             | Relationship | Age 12/31 | SSN/ITIN | Classification |
|-----------------------|--------------|-----------|----------|----------------|
| Charlotte Thornton    | Daughter     | 14        | SSN      | Qualifying child (CTC) |
| Henry Thornton        | Son          | 11        | SSN      | Qualifying child (CTC) |
| Eleanor Thornton      | Daughter     | 7         | SSN      | Qualifying child (CTC) |

- Line 4 N_CTC: 3
- Line 6 N_ODC: 0

## Part I — lines 1–14
- Line 1  AGI: $450,000
- Line 2d: $0
- Line 3  MAGI: $450,000
- Line 5  CTC tentative: 3 × $2,200 = $6,600
- Line 7  ODC tentative: 0 × $500 = $0
- Line 8  **Tentative total**: $6,600
- Line 9  Threshold: $400,000
- Line 10 Excess (rounded up to next $1,000): $50,000
- Line 11 Phase-out reduction: $50,000 × 5% = $2,500
- Line 12 **Allowed credit**: $6,600 − $2,500 = $4,100
- Line 13 Credit Limit Worksheet A: $88,046
- Line 14 Non-refundable credit: min($4,100, $88,046) = $4,100 → **1040 line 19**

## Part II-A — lines 15–27
- Line 15 Reserved
- Line 16a Leftover: $4,100 − $4,100 = $0 → stop
- Line 27 ACTC: $0 → **1040 line 28**: $0

## Verification
- Line 14 + line 27 ≤ line 12: $4,100 + $0 = $4,100 ✓
- Each dependent classified once: ✓
- SSN-before-due-date verified for the filers and each child: ✓
- Phase-out calculation: ($450,000 − $400,000) = $50,000 × 5% = $2,500 ✓

## Validation summary
- Math: all checks passed
- Sanity:
  - All 3 children qualify for CTC (under 17, SSN, etc.)
  - MAGI $50K above MFJ threshold → $2,500 phase-out reduction
  - Tax liability ($88,046) easily absorbs $4,100 → no ACTC
  - PATH Act delay: not applicable (no ACTC claimed)
- Next steps:
  - Form 1040 line 19: $4,100
  - Form 1040 line 28: $0
  - Tax after CTC (line 22): $88,046 − $4,100 = $83,946
  - The credit is fully phased out once line 10 reaches $132,000 ($6,600 ÷ 5%), i.e., MAGI above $531,000 (MFJ)
  - Each additional $1,000 (or fraction) of MAGI above $400K costs $50 of credit until full elimination

## Sources cited in this draft
- IRS Schedule 8812 (Form 1040) (2025)
- IRS Instructions for Schedule 8812 (2025)
- IRC §24(h)(2) — $2,200 credit per child
- IRC §24(b)(1), §24(h)(3) — phase-out ($50 per $1,000 over $400,000 MFJ)
- IRC §24(c) — qualifying child definition
- IRC §24(h)(7) — SSN requirement
- Rev. Proc. 2024-40 — 2025 tax rate tables and AMT exemption
```

## Why each non-obvious choice

**Why does the credit fully phase out above MFJ MAGI $531,000?** Each $1,000 (or fraction) of excess MAGI costs $50 of credit. With $6,600 of tentative credit, the credit is fully eliminated when:

```
Line 11 = line 10 × 5%
$6,600  = line 10 × 5%
line 10 = $132,000

MAGI = $400,000 + $132,000 = $532,000 → line 12 = $0
Any MAGI above $531,000 rounds line 10 up to $132,000, so the credit is $0 above $531,000.
```

For comparison: a one-child family ($2,200 tentative credit) loses the whole credit at $44,000 of excess (MAGI about $244,000 single / $444,000 MFJ). A two-child family ($4,400) loses it at $88,000 of excess (about $288,000 single / $488,000 MFJ). The Thorntons are $50,000 into an $132,000 phase-out band, so they keep $4,100 of the $6,600 tentative.

**Why no ACTC even though tax was high?** Tax liability ($88,046) is much larger than the credit ($4,100), so the full credit is non-refundable. No leftover for ACTC. ACTC is for filers whose tax liability is too small to absorb the full CTC.

**When would Part II-B matter here?** Only if there were a leftover on line 16a. If the Thorntons had a tax liability of, say, $3,000 (hypothetically), line 16a would be $4,100 − $3,000 = $1,100, line 17 = min($1,100, $5,100) = $1,100, and line 20 (15% of $437,500 = $65,625) would exceed line 17, so the form skips Part II-B and line 27 = $1,100.

**Why is the standard deduction $31,500?** This is the MFJ 2025 standard deduction as raised by P.L. 119-21 §70102 (2025 Form 1040; Rev. Proc. 2025-32 §2.08). For 2026 it is $32,200 (Rev. Proc. 2025-32 §4.14).

**Audit defense**: the Thorntons' files should include:
1. Birth certificates and SSNs for all three children
2. Proof of residency (lease, school enrollment)
3. The Schedule 8812 worksheet showing the phase-out computation
4. MAGI computation showing AGI = MAGI (no foreign income exclusion)
5. The Form 1040 line 18 tax liability computation

The phase-out reduction of $2,500 follows directly from line 10; the IRS recomputes it automatically, but the documentation should be available.
