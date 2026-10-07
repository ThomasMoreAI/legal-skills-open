# Example: Single Parent, 1 Qualifying Child + 1 Elderly Parent Dependent

A single parent (Head of Household) with one qualifying child (CTC) and one elderly parent claimed as a dependent (ODC). Modest income → ACTC kicks in. Demonstrates mixed CTC + ODC + ACTC computation.

Line numbers are from the 2025 Schedule 8812 and 2025 Form 1040.

## The filer

- **Name**: DeShawn Williams
- **Filing status**: Head of Household
- **AGI**: $42,000
- **MAGI**: $42,000 (no foreign income)
- **Earned income**: $42,000 (W-2 wages, no self-employment)
- **SSN**: DeShawn has an SSN valid for employment
- **Tax year**: 2025 (filing in 2026)

## Dependents

DeShawn lives with his 6-year-old son and his 71-year-old mother (who has Alzheimer's and lives with him).

| Dependent       | Relationship | Age 12/31 | SSN before due date | Classification |
|-----------------|--------------|-----------|------------------|----------------|
| Marcus Williams | Son          | 6         | Yes              | Qualifying child (CTC) |
| Linda Williams  | Mother       | 71        | Yes              | Qualifying relative (ODC) |

### Marcus — qualifying child for CTC

- Relationship: son ✓
- Age: 6 (under 17) ✓
- Residency: lives with DeShawn full-time ✓
- Support: did not provide own support ✓
- Joint return: never married ✓
- Citizenship: U.S. citizen ✓
- SSN valid for employment, issued before the due date: yes ✓ (and DeShawn has one too)

All seven tests pass → qualifying child.

### Linda — qualifying relative for ODC

- Not a qualifying child (parents aren't qualifying children) ✓
- Relationship: mother (in §152(d)(2) list) ✓
- Gross income: $9,200 Social Security only, none of it taxable under IRC §86 → gross income for §152(d) purposes $0 < $5,200 ✓
- Support: DeShawn provides housing, food, medical care, etc. — clearly > 50% ✓
- U.S. citizen with an SSN ✓

Linda qualifies as Other Dependent for ODC.

- **N_CTC** = 1 (Marcus, line 4)
- **N_ODC** = 1 (Linda, line 6)

## Step 3 — Tentative credit

```
Line 5  Tentative CTC = 1 × $2,200 = $2,200
Line 7  Tentative ODC = 1 × $500 = $500
Line 8  Tentative total = $2,700
```

## Step 4 — MAGI phase-out

```
Line 3   MAGI = $42,000
Line 9   Threshold (HoH) = $200,000
Line 10  Excess = $0
Line 11  Reduction = $0
Line 12  Allowed credit = $2,700
```

DeShawn's MAGI is far below threshold. Full credit available.

## Step 5 — Non-refundable credit (1040 line 19)

DeShawn's tax computation:

- Standard deduction (HoH 2025): $23,625 (2025 Form 1040 margin; Instructions What's New)
- Taxable income: $42,000 − $23,625 = $18,375
- Tax (2025 Tax Table, HoH column, row $18,350–$18,400): $1,865 (10% of $17,000 = $1,700, plus 12% of the $1,375 above $17,000 = $165)

Pre-credit tax (Form 1040 line 18): $1,865. No Schedule 3 credits, so Credit Limit Worksheet A (line 13) = $1,865.

```
Line 14  Non-refundable credit = min($2,700, $1,865) = $1,865
```

The non-refundable portion is capped at the tax liability ($1,865). **Form 1040 line 19 = $1,865**.

There's leftover credit: $2,700 − $1,865 = $835. This may be refundable as ACTC, limited to $1,700 per qualifying child (Marcus only; the ODC creates no per-child cap of its own).

## Step 6 — Refundable ACTC (1040 line 28)

```
Line 16a Leftover = $2,700 − $1,865 = $835
Line 16b Per-child cap = 1 × $1,700 = $1,700
Line 17  smaller of 16a or 16b = $835
```

Earned income method:

```
Line 18a Earned income = $42,000
Line 19  $42,000 − $2,500 = $39,500
Line 20  $39,500 × 15% = $5,925
```

Line 16b is less than $5,100 (fewer than 3 qualifying children) and DeShawn is not a Puerto Rico resident, so Part II-B is skipped.

```
Line 27  ACTC = smaller of line 17 or line 20
              = min($835, $5,925)
              = $835
```

The ACTC is capped by the **leftover** ($835), not the per-child cap. Because the non-refundable credit already absorbed most of the total, only $835 remains potentially refundable.

**Form 1040 line 28 = $835**.

Note: the **ODC** ($500 for Linda) is **non-refundable by itself**. Schedule 8812 does not track which part of line 16a came from the ODC; the leftover on line 16a is simply capped by line 16b ($1,700 × number of CTC children). With no qualifying child, line 16b would be $0 and nothing would be refundable.

## The completed worksheet

```markdown
# Schedule 8812 — DRAFT WORKSHEET for tax year 2025

## Filing facts
- Filing status: Head of Household
- Filer's MAGI: $42,000
- Earned income: $42,000
- Tax before credits (1040 line 18): $1,865
- Credit Limit Worksheet A (line 13): $1,865
- Filer SSN valid for employment before due date: Yes
- Phase-out threshold (line 9): $200,000 (HoH)

## Dependents classified
| Dependent       | Relationship | Age 12/31 | SSN/ITIN | Classification |
|-----------------|--------------|-----------|----------|----------------|
| Marcus Williams | Son          | 6         | SSN      | Qualifying child (CTC) |
| Linda Williams  | Mother       | 71        | SSN      | Qualifying relative (ODC) |

- Line 4 N_CTC: 1
- Line 6 N_ODC: 1

## Part I — lines 1–14
- Line 1  AGI: $42,000
- Line 2d: $0
- Line 3  MAGI: $42,000
- Line 5  CTC tentative: 1 × $2,200 = $2,200
- Line 7  ODC tentative: 1 × $500 = $500
- Line 8  **Tentative total**: $2,700
- Line 9  Threshold: $200,000
- Line 10 Excess: $0
- Line 11 Phase-out reduction: $0
- Line 12 **Allowed credit**: $2,700
- Line 13 Credit Limit Worksheet A: $1,865
- Line 14 Non-refundable credit: min($2,700, $1,865) = $1,865 → **1040 line 19**

## Part II-A — lines 15–27
- Line 15 Reserved
- Line 16a Leftover: $2,700 − $1,865 = $835
- Line 16b Per-child cap (1 × $1,700): $1,700
- Line 17 smaller of 16a or 16b: $835
- Line 18a Earned income: $42,000
- Line 18b Nontaxable combat pay: $0
- Line 19 Earned income over $2,500: $39,500
- Line 20 15% of line 19: $5,925
- Lines 21–26: N/A (fewer than 3 qualifying children)
- Line 27 ACTC = min($835, $5,925) = $835 → **1040 line 28**

## Verification
- Line 14 + line 27 ≤ line 12: $1,865 + $835 = $2,700 ✓
- Each dependent classified once: ✓
- SSN-before-due-date verified for DeShawn and Marcus: ✓
- Linda has SSN (meets the ODC TIN requirement): ✓

## Validation summary
- Math: all checks passed
- Sanity:
  - Marcus (age 6) qualifies for CTC
  - Linda's $9,200 Social Security is not taxable → not gross income → passes the $5,200 test
  - DeShawn provides > 50% support of Linda (lives with him, he pays bills) → passes test
  - Earned income $42K > $2,500 threshold → ACTC available
- Next steps:
  - DeShawn files Schedule 8812 with his HoH 1040
  - 1040 line 19: $1,865 (reduces tax to $0)
  - 1040 line 28: $835 (refundable; adds to refund)
  - Total credit benefit: $1,865 + $835 = $2,700 (full credit utilized)
  - PATH Act: refund will not issue before mid-February (returns claiming ACTC)

## Sources cited in this draft
- IRS Schedule 8812 (Form 1040) (2025) and Instructions (2025)
- IRC §24(h)(2) — $2,200 credit per child
- IRC §24(d) — Refundable ACTC
- IRC §24(d)(1)(B), §24(h)(6) — 15% of earned income over $2,500
- IRC §24(h)(4) — Credit for Other Dependents ($500)
- IRC §24(h)(5), §24(i)(1) — Refundable cap $1,700 (2025)
- IRC §152(d) — Qualifying relative definition
- IRC §86 — taxable part of Social Security benefits; Pub 501 (2025) — gross income test (taxable social security benefits count)
- Rev. Proc. 2024-40 — 2025 inflation adjustments ($5,200 gross income limit, tax rates)
```

## Why each non-obvious choice

**Why is Linda's Social Security excluded from her gross income?** Per IRC §152(d)(1)(B), the test is "gross income," and Pub 501 (2025, p.19) counts only *taxable* social security benefits. Under IRC §86, if Linda's only income is Social Security and her provisional income (half her benefits plus other income) stays under the base amount ($25,000 for a single filer), none of her benefits are taxable, and her gross income for §152(d) is $0.

If Linda also had $5,000 of pension income, her gross income would be $5,000 — still below the $5,200 limit, so she'd still pass.

If Linda had $6,000 of pension income, gross income = $6,000 > $5,200 → fail. She couldn't be claimed as a dependent and the ODC wouldn't apply.

**Why does DeShawn get $835 refundable when his leftover is $835?** Line 27 is the smallest of three amounts:
1. Leftover from non-refundable (line 16a): $835
2. Per-child cap (line 16b): $1,700
3. Earned income method (line 20): $5,925

The leftover is the binding constraint here — only $835 remains after the non-refundable credit. If DeShawn had had tax liability of $2,700 or more, the entire CTC + ODC would be non-refundable; ACTC = $0. If DeShawn had had tax liability of $1,000, the non-refundable would be $1,000, leftover would be $1,700, and ACTC would be min($1,700, $1,700, $5,925) = $1,700.

**Why is the ODC ($500 for Linda) not refundable?** IRC §24(d)(1) and §24(h)(5) limit the refundable amount to $1,700 per *qualifying child*; the ODC has no refundable portion of its own. It can reduce tax liability but cannot create a refund beyond the per-child cap.

**What if DeShawn's tax liability were $0 (very low income)?** Line 14 would be $0, line 16a would be $2,700. ACTC = min($2,700, $1,700, $5,925) = $1,700. The remaining $1,000 (the $500 ODC and $500 of the CTC) would be lost (no tax to reduce, not refundable). DeShawn would get $1,700 refundable.

**What about EITC?** With 1 qualifying child and HoH filing, AGI $42K is in the 2025 EITC phase-out range (phase-out from $23,350 to $50,434; Rev. Proc. 2024-40 §2.06). DeShawn would get roughly $1,300–$1,400 of EITC from the EIC Table — a separate computation on Schedule EIC and Form 1040 line 27a (no skill in this repo yet).

**Audit defense**:
1. Marcus's birth certificate and SSN
2. Linda's SSN and proof of relationship
3. Documentation that Linda lives with DeShawn (lease showing both names, or DeShawn as sole tenant with Linda as occupant)
4. Documentation that DeShawn provides > 50% of Linda's support (rent receipts, grocery receipts, medical bills paid by DeShawn)
5. Linda's Social Security statement showing $9,200 (no other income)
