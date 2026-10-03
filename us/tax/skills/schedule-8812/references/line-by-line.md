# Schedule 8812 — Line-by-Line Reference

Complete lookup for every line of Schedule 8812. Use when the agent needs to confirm what each line means or how it interacts with the user's return.

**IMPORTANT**: Schedule 8812 is renumbered periodically by the IRS. Line numbers below reflect a typical post-TCJA / post-OBBBA revision but should be verified against the current-year [Form Schedule 8812](https://www.irs.gov/pub/irs-pdf/f1040s8.pdf) before filing. The categories and computation flow are stable; only the line numbers shift.

Source: [Form Schedule 8812](https://www.irs.gov/pub/irs-pdf/f1040s8.pdf), [Instructions for Schedule 8812](https://www.irs.gov/pub/irs-pdf/i1040s8.pdf), Pub 972 (historical), IRC §24.

---

## Part I — Child Tax Credit and Credit for Other Dependents

### Part I-A — Determining your credit

**Line 1 — Number of qualifying children under age 17 with the required SSN**

A qualifying child for CTC must have an SSN issued by the due date of the return (including extensions). ITIN and ATIN do NOT qualify (IRC §24(h)(7)).

Each child counted here is a "qualifying child" under IRC §24(c) (which cross-references §152(c)). All seven qualifying child tests must be met. See [`qualifying-child-test.md`](./qualifying-child-test.md).

**Line 2 — Multiply Line 1 by $2,000**

The base credit is $2,000 per qualifying child. Made permanent under OBBBA 2025. Verify 2026 figure — base is currently $2,000 but inflation adjustments may apply per IRC §24(b) for tax years after 2025.

**Line 3 — Number of other dependents**

A "qualifying relative" or other dependent who doesn't meet the CTC tests (e.g., age 17+, ITIN, parent dependent, qualifying relative under IRC §152(d)). See [`qualifying-relative-test.md`](./qualifying-relative-test.md).

**Line 4 — Multiply Line 3 by $500**

The Credit for Other Dependents (ODC) is $500 per other dependent. Set by TCJA 2017 in IRC §24(h)(4).

**Line 5 — Add Lines 2 and 4**

Tentative total credit before phase-out and tax-liability limit.

**Line 6 — Modified Adjusted Gross Income (MAGI)**

For most filers, MAGI = AGI (Form 1040 Line 11). For some filers, additions apply:

- Foreign earned income exclusion (Form 2555 Line 45)
- Foreign housing exclusion or deduction (Form 2555 Line 50 or Line 50a)
- Income from Puerto Rico excluded from gross income
- Income excluded from American Samoa, Guam, Northern Mariana Islands, U.S. Virgin Islands

If none of these apply, MAGI = AGI. The Schedule 8812 instructions have Worksheet A for the calculation.

**Line 7 — Phase-out threshold**

- $200,000 for Single, Head of Household, Married Filing Separately, Qualifying Surviving Spouse
- $400,000 for Married Filing Jointly

Set by TCJA 2017 in IRC §24(b). These thresholds were not indexed for inflation under TCJA but verify under OBBBA — the $2,000 base was made permanent, the threshold treatment may have shifted.

**Line 8 — Excess MAGI**

```
Line 8 = max(0, Line 6 − Line 7), rounded UP to next $1,000
```

The IRS rounding rule: any excess MAGI rounds **up** to the next multiple of $1,000. So MAGI of $400,500 (MFJ) produces excess of $1,000, not $500.

**Line 9 — Phase-out reduction**

```
Line 9 = Line 8 × $50 / $1,000
       = Line 8 × 0.05
```

Equivalently, $5 for every $1,000 (or fraction thereof) of MAGI above the threshold. So $1,000 of excess produces $50 reduction; $10,000 of excess produces $500 reduction; $40,000 of excess fully eliminates the $2,000 credit for one child.

**Line 10 — Allowed credit before tax-liability limit**

```
Line 10 = max(0, Line 5 − Line 9)
```

Credit cannot be negative. If MAGI is high enough, Line 10 = $0 and no credit is available.

**Line 11 — Tax-liability limit (from Credit Limit Worksheet A)**

This is Form 1040 Line 18 (income tax + AMT) reduced by certain prior credits (e.g., Foreign Tax Credit on Schedule 3 Line 1, Credit for Child and Dependent Care Expenses on Schedule 3 Line 2). The Schedule 8812 instructions have a specific worksheet for this.

**Line 12 — Non-refundable Child Tax Credit + Credit for Other Dependents**

```
Line 12 = min(Line 10, Line 11)
```

This becomes **Form 1040 Line 19**.

If Line 12 < Line 10, there's a leftover that may be refundable (Part II-A).

If Line 12 = Line 10, the full credit was absorbed by tax liability — no refundable portion.

### Part I-B — Refundable / Non-refundable allocation

(Some revisions of Schedule 8812 separate this; some merge it with Part I-A. The flow is the same.)

The leftover from Line 10 minus Line 12 is the maximum amount potentially refundable as ACTC, subject to the per-child cap and earned income test in Part II.

---

## Part II-A — Additional Child Tax Credit (Most Filers)

**Line 14 — Number of qualifying children under 17 with required SSN**

Same as Line 1. Repeated here for the per-child cap calculation.

**Line 15 — Multiply Line 14 by $1,700 (for tax year 2025; verify 2026 inflation adjustment)**

The refundable per-child cap. IRC §24(h)(5) sets a base amount adjusted annually for inflation. For tax year 2024: $1,700. For tax year 2025: $1,700. For tax year 2026: verify against the latest Revenue Procedure (typically released in October-November of the prior year).

**Line 16 — Earned income**

Wages (1040 Line 1a) + net self-employment income (Schedule SE Line 3 or 4 minus half SE tax) + nontaxable combat pay (if elected to include).

**If Line 16 is $2,500 or less, ACTC = $0.** This is the IRC §24(d)(1)(B) earned income threshold.

**Line 17 — Earned income excess**

```
Line 17 = max(0, Line 16 − $2,500)
```

**Line 18 — Earned income method ACTC**

```
Line 18 = Line 17 × 15%
```

This is the "earned income" method of computing refundable ACTC.

**Line 19 — Smallest of: leftover from Line 12, Line 15 (per-child cap), or Line 18 (earned income method)**

For most filers, this is the ACTC.

```
Line 19 = min(Line 10 − Line 12, Line 15, Line 18)
```

**Line 20 — ACTC final** → flows to **Form 1040 Line 28**

---

## Part II-B — Alternative ACTC for Filers with 3+ Qualifying Children

If the filer has 3 or more qualifying children, the ACTC may be computed using the "Social Security tax method" if it's larger than the earned income method.

**Lines for 3+ qualifying children alternative**:

- Filer's Social Security tax + Medicare tax + half of self-employment tax
- Minus filer's Earned Income Credit (Schedule EIC, if claimed)
- Larger of the result or the earned income method (Line 18)

This uses the larger of the two methods. The result is capped at Line 15 (per-child cap) and the leftover from Line 10 − Line 12.

See [`actc-refundability.md`](./actc-refundability.md) for the full computation.

---

## Part II-C — Additional ACTC for Bona Fide Residents of Puerto Rico

Specialized computation for Puerto Rico residents. Out of scope for this skill in detail, but the agent should note its existence and refer Puerto Rico filers to a tax professional or the [Puerto Rico tax skill](forthcoming).

---

## Where Schedule 8812 totals go on Form 1040

| Schedule 8812 line | Form 1040 line | Description |
|--------------------|----------------|-------------|
| Non-refundable credit (Line 12 in this typical layout) | 1040 Line 19 | "Child tax credit or credit for other dependents from Schedule 8812" |
| ACTC (Line 20 in this typical layout) | 1040 Line 28 | "Additional child tax credit from Schedule 8812" |

Both lines are subtractive against tax liability (Line 19) or additive to refund/payments (Line 28). The total of Lines 19 + 28 cannot exceed the total credit on Schedule 8812 Line 10.

---

## What's NOT on Schedule 8812

The agent should NOT compute or include on Schedule 8812:

- **Earned Income Tax Credit (EITC)** — separate computation on Schedule EIC (Form 1040 Line 27)
- **Child and Dependent Care Credit** — Form 2441 (Schedule 3 Line 6)
- **Adoption Credit** — Form 8839 (Schedule 3 Line 6c, or Line 6 — verify)
- **Credit for Qualified Sick and Family Leave Wages** — Schedule H or Form 7202
- **American Opportunity / Lifetime Learning Credits** — Form 8863
- **Premium Tax Credit reconciliation** — Form 8962

If the user mentions any of these, redirect to the appropriate skill (forthcoming for several).

---

## A note on prior-year ARPA expansion

For tax year 2021 only, the American Rescue Plan Act expanded CTC to $3,000-$3,600 per child, made it fully refundable, and provided for advance payments. Those rules **expired** at the end of 2021. For 2022 onward (including tax years 2025 and 2026), the rules in this reference apply: $2,000 base, $1,700 refundable cap (2025), MAGI phase-out starting at $200K/$400K.

If the user has a 2021 amended return question, this skill does NOT apply — refer to the 2021 instructions.

---

## Validation table (for cross-checking the worksheet)

| Field | Formula | Example |
|-------|---------|---------|
| Tentative CTC | N_CTC × $2,000 | 2 children × $2,000 = $4,000 |
| Tentative ODC | N_ODC × $500 | 1 ODC × $500 = $500 |
| Tentative total | CTC + ODC | $4,000 + $500 = $4,500 |
| MAGI threshold (single) | $200,000 | — |
| MAGI threshold (MFJ) | $400,000 | — |
| Excess (rounded up) | ceiling((MAGI − threshold) / 1000) × 1000 | $410,500 MFJ → $11,000 (rounded up from $10,500) |
| Phase-out reduction | Excess × 0.05 | $11,000 × 0.05 = $550 |
| Allowed credit | max(0, Tentative − Reduction) | $4,500 − $550 = $3,950 |
| Non-refundable | min(Allowed, Tax limit) | min($3,950, $X) |
| Per-child refundable cap (2025) | N_CTC × $1,700 | 2 × $1,700 = $3,400 |
| Earned income excess | max(0, EI − $2,500) | $50,000 − $2,500 = $47,500 |
| Earned income ACTC | EI excess × 15% | $47,500 × 15% = $7,125 |
| Leftover | Allowed − Non-refundable | $3,950 − $X |
| Final ACTC | min(Leftover, EI ACTC, Per-child cap) | min($3,950 − $X, $7,125, $3,400) |
