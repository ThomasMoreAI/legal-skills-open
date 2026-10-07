---
name: schedule-8812
title: Schedule 8812 — Credits for Qualifying Children and Other Dependents
description: 'Use this skill when an individual taxpayer needs to claim the Child Tax Credit (CTC), the refundable Additional Child Tax Credit (ACTC), or the Credit for Other Dependents (ODC) on Form 1040 by completing Schedule 8812. Triggers on phrases like "Child Tax Credit", "CTC", "qualifying child credit", "Schedule 8812", "Credit for Other Dependents", "ODC", "ACTC", "refundable child credit", "credit for elderly parent dependent", "claim $2,200 per child", "kid tax credit". Do NOT use for: dependent care expenses (Form 2441; no skill in this repo yet), Earned Income Tax Credit (Schedule EIC; no skill yet), Adoption Credit (Form 8839; no skill yet), or the Child and Dependent Care Credit. The Child Tax Credit and the Child and Dependent Care Credit are two different credits — this skill is only for the former. Whether a person is your dependent at all is a Form 1040 question — use form-1040.'
author: jupid-tax
author_url: https://github.com/jupid-tax/jupid-skills/tree/main/forms/schedule-8812
license: MIT
version: 0.1.2
execution_mode: open
jurisdiction: us
practice: tax
language: en
sources:
- title: Actc refundability
  path: references/actc-refundability.md
- title: Common mistakes
  path: references/common-mistakes.md
- title: Line by line
  path: references/line-by-line.md
- title: Qualifying child test
  path: references/qualifying-child-test.md
- title: Qualifying relative test
  path: references/qualifying-relative-test.md
---

# Schedule 8812 — Credits for Qualifying Children and Other Dependents

This skill computes three closely-related credits on a single schedule:

1. **Child Tax Credit (CTC)** — non-refundable credit of up to $2,200 per qualifying child under 17 (tax years 2025 and 2026; Schedule 8812 line 5; Rev. Proc. 2025-32 §4.05(1))
2. **Additional Child Tax Credit (ACTC)** — the refundable portion of the CTC, up to $1,700 per qualifying child (tax years 2025 and 2026; Schedule 8812 line 16b; Rev. Proc. 2025-32 §4.05(2))
3. **Credit for Other Dependents (ODC)** — non-refundable credit of $500 per dependent who doesn't meet the CTC tests (Schedule 8812 line 7; IRC §24(h)(4))

The skill walks through each of the three credits, applies the MAGI-based phase-out, computes the refundable portion using the earned income test, and produces an audit-grade worksheet showing every line including zeros.

The arithmetic is mechanical. The judgment is in (1) which children count as "qualifying children" for CTC vs. "qualifying relatives" for ODC, (2) whether the SSN-before-the-due-date requirement is met for the child AND, starting with 2025 returns, for the taxpayer (one spouse on a joint return) — no valid SSN means no CTC/ACTC, only ODC if a TIN exists, and (3) how the phase-out interacts with the refundable cap.

**Form revision.** The line map in this skill was verified against the **2025 Schedule 8812 (Form 1040)** (created 7/30/25) and the **2025 Instructions for Schedule 8812** (Jan 23, 2026), filed in 2026. The IRS revises the schedule every year: before using this skill for a later tax year, re-check the current revision at [About Schedule 8812](https://www.irs.gov/forms-pubs/about-schedule-8812-form-1040).

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Schedule 8812, the Child Tax Credit, CTC, ACTC, or the Credit for Other Dependents
- The user asks "how much credit do I get for my kids?", "is my child still eligible at age 17?", "can I claim my mother as a dependent for the credit?", or similar
- The user has dependents on their Form 1040 and is computing total tax (Schedule 8812 reduces tax on Form 1040 Line 19 + Line 28)
- The user's tax software is returning a CTC amount the user wants to verify

Do **not** engage this skill when:

- The user is asking about the **Child and Dependent Care Credit** (Form 2441) — different credit, for childcare expenses while parent is working. The two are often confused.
- The user is asking about the Earned Income Tax Credit (EITC) — Schedule EIC and Form 1040 line 27a (no skill in this repo yet)
- The user is asking about the Adoption Credit — Form 8839 (no skill in this repo yet)
- The user wants to know how to claim a dependent on their return at all — that's a Form 1040 question ([`form-1040`](../form-1040/SKILL.md)); this skill assumes dependent eligibility is established and the question is the credit value

For users with multiple credits (CTC + EITC + Childcare), run this skill for the CTC/ODC portion only; the other credits go through their own skills, and Form 1040 totals them all.

---

## Prerequisites

Before producing anything, the agent must collect the following. If any are missing, **ASK** with a tight question and stop.

1. **Tax year** the return covers. CTC/ACTC parameters can change yearly: the $2,200 credit is inflation-indexed for years after 2025 (IRC §24(i)(2)) and the refundable cap is indexed (IRC §24(i)(1)); the $200,000/$400,000 phase-out thresholds are not indexed (IRC §24(h)(3)). Tax year 2025: $2,200 per child, $1,700 refundable (2025 Instructions for Schedule 8812, What's New and Reminders). Tax year 2026: $2,200 and $1,700 (Rev. Proc. 2025-32 §4.05). P.L. 119-21 (OBBBA) §70104 made these rules permanent.

2. **Filer's filing status**. Single, MFJ, MFS, HoH, QSS. The MAGI phase-out thresholds depend on this.

3. **Filer's MAGI** for the year (Schedule 8812 line 3). For most filers, MAGI = AGI (Form 1040 line 11a). For some, it's AGI + excluded Puerto Rico income (line 2a) + Form 2555 lines 45 and 50 (foreign earned income and housing exclusions, line 2b) + Form 4563 line 15 (American Samoa exclusion, line 2c). Confirm with the user.

4. **Earned income for the year** (Schedule 8812 line 18a). Use the Earned Income Chart / Earned Income Worksheet in the Schedule 8812 instructions: Form 1040 line 1z + nontaxable combat pay + statutory employee income + net self-employment profit, minus the deductible half of SE tax (Schedule 1 line 15) and any excluded Medicaid waiver payments the filer did not choose to include. Nontaxable combat pay always counts for the ACTC (IRC §24(d)(1) flush language); the combat pay election exists only for the EITC. Required for the $2,500 earned income threshold.

5. **List of every dependent**. For each, collect:
   - Legal name
   - SSN or ITIN or ATIN (and its issue date if it may have been issued after the return's due date)
   - Relationship to filer
   - Birthdate
   - Whether they lived with the filer for more than half the year
   - Whether the filer (or filer's spouse if MFJ) provided more than half of their support
   - Whether they're a U.S. citizen, U.S. national, or U.S. resident alien
   - Whether they file their own joint return (disqualifies them as dependent unless filing only to claim refund)
   - For children: whether they have an SSN valid for employment issued before the due date of the return (including extensions)
   - For each: dependent classification ("qualifying child" or "qualifying relative" — see [`references/qualifying-child-test.md`](./references/qualifying-child-test.md))

   Also ask for the **filer's own SSN status** (and spouse's on a joint return): starting with 2025 returns, the CTC and ACTC require that the taxpayer, or at least one spouse on a joint return, has an SSN valid for employment issued before the due date; the other spouse needs an SSN or ITIN issued on or before the due date (2025 Instructions for Schedule 8812, p.1; IRC §24(h)(7)(A)(i)). The ODC requires the filer (and spouse) to have an SSN or ITIN issued on or before the due date.

6. **Tax before credits**. Form 1040 line 18 = line 16 (tax) + line 17 (Schedule 2 line 3: AMT and excess advance premium tax credit repayment). The CTC + ODC are limited by this amount (non-refundable portion).

7. **Other nonrefundable credits** that Credit Limit Worksheet A subtracts before the CTC: Schedule 3 lines 1 (foreign tax credit), 2 (child and dependent care), 3 (education), 4 (saver's credit), 5b (energy efficient home improvement), 6d (elderly or disabled), 6f (clean vehicle), 6l (Form 8978), and 6m (previously owned clean vehicle). If the filer claims the mortgage interest credit (Form 8396), adoption credit (Form 8839), residential clean energy credit (Form 5695 Part I) or DC first-time homebuyer credit (Form 8859), Credit Limit Worksheet B also applies.

For the refundable ACTC computation (Part II-B, only with 3+ qualifying children), additionally ask:

- Social security and Medicare tax withheld (Form W-2 boxes 4 and 6, both spouses if MFJ), Schedule 1 line 15, Schedule 2 lines 5, 6 and 13, the EIC on Form 1040 line 27a, and Schedule 3 line 11 (excess social security withheld)

---

## Workflow

Execute these steps in order.

### Step 1 — Classify each dependent

For each dependent on the user's 1040, determine whether they are:

**(a) A qualifying child for CTC purposes** — must satisfy ALL of:

- Relationship: filer's son, daughter, stepchild, eligible foster child, brother, sister, half-brother/sister, stepbrother/sister, or descendant of any of these (e.g., grandchild, niece, nephew)
- Age: under 17 at the end of the tax year (so 16 or younger as of December 31)
- Residency: lived with filer more than half the year (with exceptions for temporary absence, divorce, etc.)
- Support: did not provide more than half of their own support
- Joint return: did not file a joint return for the year (other than to claim a refund)
- Citizenship: U.S. citizen, U.S. national, or U.S. resident alien
- **SSN before the due date**: must have an SSN valid for employment issued before the due date of the return (including extensions). ITIN or ATIN does NOT qualify for CTC. The filer (or one spouse on a joint return) must also have such an SSN. (IRC §24(h)(7); 2025 Instructions for Schedule 8812, p.1.)

**(b) A qualifying relative or other dependent for ODC purposes** — anyone who can be claimed as a dependent on the 1040 but does NOT meet (a). Examples:

- The filer's child who is 17 or older
- The filer's parent or other relative claimed as a dependent
- A child without an SSN (has an ITIN or ATIN) — qualifies for ODC, not CTC
- A non-relative living with the filer who meets the qualifying-relative test
- Any dependent with an ITIN

ODC also requires that the dependent is a U.S. citizen, U.S. national, or U.S. resident alien and has an SSN, ITIN, or ATIN issued on or before the due date (2025 Instructions for Schedule 8812, p.2). A dependent who fails these counts on neither line 4 nor line 6.

See [`references/qualifying-child-test.md`](./references/qualifying-child-test.md) and [`references/qualifying-relative-test.md`](./references/qualifying-relative-test.md) for the full tests. When in doubt, ASK the user the specific facts (age, SSN status, residency).

### Step 2 — Count qualifying children and other dependents

Build the table:

```
| Dependent name  | Relationship | Age 12/31 | SSN before due date | Classification |
|-----------------|--------------|-----------|------------------|----------------|
| Sophia Carter   | Daughter     | 9         | Yes              | Qualifying child (CTC) |
| Liam Carter     | Son          | 17        | Yes              | Other dependent (ODC; qualifying child for dependency, but 17) |
| Maria Carter    | Mother       | 71        | Yes              | Qualifying relative (ODC) |
```

Count:
- **N_CTC** = number of qualifying children (Schedule 8812 line 4 = number of "Child tax credit" boxes checked in row (7) of the Form 1040 Dependents section)
- **N_ODC** = number of other dependents (line 6 = number of "Credit for other dependents" boxes in row (7))

### Step 3 — Compute the tentative credit

For tax years 2025 and 2026 ($2,200 per child: 2025 Schedule 8812 line 5; Rev. Proc. 2025-32 §4.05(1)):

```
Line 5  Tentative CTC = N_CTC × $2,200
Line 7  Tentative ODC = N_ODC × $500
Line 8  Tentative total = line 5 + line 7
```

### Step 4 — Apply the MAGI phase-out

The credit phases out at higher incomes (IRC §24(b)(1), §24(h)(3)):

- Threshold (line 9): **$200,000** (single, HoH, MFS, QSS) or **$400,000** (MFJ). Not indexed for inflation.
- Phase-out rate: **$50 reduction per $1,000** (or fraction thereof) of MAGI **above** the threshold — line 11 is 5% of line 10.

```
Line 3   MAGI = line 1 (Form 1040 line 11a) + line 2d
Line 10  Excess = max(0, line 3 − line 9), rounded UP to the next multiple of $1,000
Line 11  Phase-out reduction = line 10 × 5%   (i.e., $50 per $1,000 of rounded excess)
```

Note: the $1,000 increment is the IRS rounding rule — any amount above the threshold rounds **up** to the next $1,000. So MAGI of $400,500 (MFJ) produces line 10 of $1,000 (rounded up from $500), and a reduction of $50.

```
Line 12  If line 8 is not more than line 11: STOP — no CTC, ODC or ACTC.
         Otherwise: Allowed credit = line 8 − line 11
```

### Step 5 — Limit by tax liability (non-refundable portion)

The CTC and ODC are non-refundable up to the filer's pre-credit tax liability. Compute:

```
Line 13  Credit Limit Worksheet A = Form 1040 line 18 − Schedule 3 lines 1, 2, 3, 4, 5b, 6d, 6f, 6l, 6m
         − Credit Limit Worksheet B amount (only if Form 8396, 8839, 5695 Part I or 8859 credits are claimed)
Line 14  Non-refundable credit = min(line 12, line 13)
```

Line 14 becomes **Form 1040 line 19** ("Child tax credit or credit for other dependents from Schedule 8812").

### Step 6 — Compute the refundable Additional Child Tax Credit (ACTC)

If line 12 is more than line 14 AND the filer has at least one qualifying child on line 4, the leftover may be refundable as the ACTC. Complete Form 1040 through line 27a and Schedule 3 line 11 first. Filers who file Form 2555 cannot claim the ACTC.

Refundable cap: **$1,700 per qualifying child** for 2025 and 2026 (IRC §24(h)(5) as indexed by §24(i)(1); Rev. Proc. 2025-32 §4.05(2)).

```
Line 15  Reserved for future use
Line 16a Leftover = line 12 − line 14. If zero, stop (ACTC = $0).
Line 16b Per-child cap = N_CTC × $1,700. If zero, stop.
Line 17  smaller of line 16a or line 16b
Line 18a Earned income (Earned Income Chart / Worksheet); line 18b nontaxable combat pay
Line 19  If line 18a > $2,500: line 18a − $2,500; otherwise blank and line 20 = 0
Line 20  line 19 × 15%
         If line 16b < $5,100 (fewer than 3 children): line 27 = smaller of line 17 or line 20
         (bona fide Puerto Rico residents go to Part II-B instead).
         If line 16b ≥ $5,100 and line 20 ≥ line 17: line 27 = line 17.
         Otherwise go to Part II-B (lines 21–26):
Line 21  W-2 boxes 4 + 6 (both spouses if MFJ; Additional Medicare/RRTA worksheet if applicable)
Line 22  Schedule 1 line 15 + Schedule 2 lines 5, 6, 13
Line 23  line 21 + line 22
Line 24  Form 1040 line 27a (EIC) + Schedule 3 line 11
Line 25  max(0, line 23 − line 24)
Line 26  larger of line 20 or line 25
Line 27  ACTC = smaller of line 17 or line 26
```

See [`references/actc-refundability.md`](./references/actc-refundability.md). Line 27 becomes **Form 1040 line 28** ("Additional child tax credit (ACTC) from Schedule 8812").

### Step 7 — Run validation checks

See **Validation** below.

### Step 8 — Produce the deliverable

See **Output format** below.

### Step 9 — Hand off downstream

State the next forms the user will need:

- Form 1040 line 19 ← Schedule 8812 line 14 (non-refundable CTC + ODC)
- Form 1040 line 28 ← Schedule 8812 line 27 (ACTC)
- Form 1040 Dependents section row (7): "Child tax credit" box for each child counted on line 4, "Credit for other dependents" box for each dependent counted on line 6 (never both)
- If filing late, confirm the SSN-before-the-due-date requirement is still met for the filer and each child
- If a dependent's SSN was issued after the due date (including extensions), that dependent is not eligible for CTC — only ODC if an SSN/ITIN/ATIN was issued (or applied for) on or before the due date
- If the CTC/ACTC/ODC was denied or reduced for a year after 2015 for a reason other than math or clerical error, Form 8862 must be attached (2025 Instructions for Schedule 8812, p.2)

### Step 10 — File the return (optional, if the user wants the agent to file)

If the agent has browser-automation tooling and the user explicitly authorizes filing, follow [`filing.md`](./filing.md). It contains:

- Decision tree to pick a filing channel (IRS Free File, Free File Fillable Forms, paid software, paper)
- Field-by-field mapping from this skill's draft to FFFF Schedule 8812 fields
- Pre-flight checklist
- Security/consent rules

If the user only wants the worksheet, skip this step.

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Schedule 8812 structure

The 2025 Schedule 8812 has four parts:

- **Part I — Child Tax Credit and Credit for Other Dependents (lines 1–14)** — MAGI (lines 1–3), counts and tentative credit (lines 4–8), phase-out (lines 9–12), tax-liability limit (line 13, Credit Limit Worksheet A) and the non-refundable credit (line 14 → Form 1040 line 19)
- **Part II-A — Additional Child Tax Credit for All Filers (lines 15–20)** — line 15 reserved, leftover and per-child cap (16a, 16b, 17), earned income method (18a–20)
- **Part II-B — Certain Filers Who Have Three or More Qualifying Children and Bona Fide Residents of Puerto Rico (lines 21–26)** — social security and Medicare tax method
- **Part II-C — Additional Child Tax Credit (line 27)** → Form 1040 line 28

Each filing year, the IRS may renumber lines. Reference the current-year [Schedule 8812](https://www.irs.gov/pub/irs-pdf/f1040s8.pdf) for the exact line numbers when filing.

### The two-page summary

```
Step 1. Count qualifying children with the required SSN (line 4)
Step 2. Count other dependents (line 6)
Step 3. Tentative CTC = N_CTC × $2,200 (line 5); Tentative ODC = N_ODC × $500 (line 7)
Step 4. MAGI phase-out (above $200K / $400K MFJ — $50 per $1,000 over, rounded up) (lines 9–12)
Step 5. Non-refundable credit (min of line 12 and Credit Limit Worksheet A) → line 14 → 1040 line 19
Step 6. Refundable ACTC (earned income > $2,500, 15% method, $1,700/child cap, Part II-B for 3+) → line 27 → 1040 line 28
```

### What's NOT on Schedule 8812

- Dependent care expenses (Form 2441)
- The Earned Income Tax Credit (Schedule EIC)
- The Adoption Credit (Form 8839)
- The American Opportunity / Lifetime Learning Credits (Form 8863)
- Premium tax credit reconciliation (Form 8962)

If a user has multiple credits, each is computed on its own form/schedule, then totaled on Form 1040.

---

## Validation

Run every check before declaring the worksheet ready.

### Math checks

- [ ] Every dependent on Form 1040 is counted on line 4, line 6, or neither (with the reason stated); no dependent on both lines
- [ ] Line 8 = N_CTC × $2,200 + N_ODC × $500
- [ ] Line 10 is the **rounded-up** excess MAGI (next $1,000); line 11 = line 10 × 5%
- [ ] Line 12 ≥ 0 (if line 8 ≤ line 11, stop: no credit)
- [ ] Line 14 ≤ line 13 (Credit Limit Worksheet A)
- [ ] Line 27 ≤ line 16b (N_CTC × $1,700)
- [ ] Line 27 ≤ line 16a = line 12 − line 14
- [ ] Line 14 + line 27 ≤ line 12 (any excess is lost, not carried)
- [ ] If line 11 ≥ line 8 (MAGI more than threshold + line 8 / 5%, before rounding), no CTC/ODC/ACTC

### Sanity checks

Surface as warnings, do not block:

- [ ] User has dependents but no SSN information collected → ask explicitly for each dependent
- [ ] Filer (or both spouses on a joint return) lacks an SSN valid for employment issued before the due date → no CTC/ACTC; ODC only if the filer has an SSN or ITIN
- [ ] Filer files Form 2555 → ACTC not allowed (Part II-A caution)
- [ ] Prior-year CTC/ACTC/ODC disallowance (other than math error) → Form 8862 required
- [ ] User has a child age 17+ classified as qualifying child → reclassify as other dependent (ODC, not CTC)
- [ ] User has a child with ITIN classified as qualifying child → reclassify as ODC (no CTC for ITIN children)
- [ ] User has earned income > $2,500 but ACTC computed as $0 → verify the user has at least one qualifying child (ACTC requires CTC eligibility)
- [ ] User has 3+ qualifying children, line 20 < line 17, but Part II-B was not computed → complete lines 21–26 and use the larger of line 20 or line 25
- [ ] Phase-out fully eliminates the credit — verify MAGI is correct and that the user understands they're above the phase-out
- [ ] Filer is MFS and claims CTC — MFS may file Schedule 8812 but must coordinate with the other spouse to avoid double-claiming the same child; ASK
- [ ] Filer's dependent is a U.S. resident alien but lived in Mexico/Canada more than half the year — residency rules apply differently

### Cross-form checks

- [ ] Each qualifying child listed on Schedule 8812 must be listed as a dependent on Form 1040
- [ ] Each "Other Dependent" listed on Schedule 8812 must be listed as a dependent on Form 1040
- [ ] If filer also claims EITC, the same children may be qualifying children for both (no double-claim issue, but verify name+SSN matches)
- [ ] If filer also claims Childcare Credit (Form 2441), the same children may be qualifying for both
- [ ] If filer's MAGI ≥ phase-out fully-eliminated point, the agent should warn that none of the CTC/ODC is available — different from "I owe no tax so I don't need it"
- [ ] Line 1 equals Form 1040 line 11a; line 13 starts from Form 1040 line 18

---

## Output format

The deliverable is a worksheet showing every step of the computation, plus the line-entries for Form 1040. Format:

```markdown
# Schedule 8812 — DRAFT WORKSHEET for tax year YYYY

## Filing facts
- Filing status: <Single | MFJ | MFS | HoH | QSS>
- Filer's MAGI: $XXX,XXX
- Earned income: $XXX,XXX
- Tax before credits (1040 line 18): $XXX,XXX
- Credit Limit Worksheet A (line 13): $XXX,XXX
- Filer SSN valid for employment before due date (one spouse if MFJ): Yes | No
- Phase-out threshold (line 9): $200,000 (single, HoH, QSS, MFS) or $400,000 (MFJ)

## Dependents classified
| Dependent | Relationship | Age 12/31 | SSN/ITIN | Classification |
|-----------|--------------|-----------|----------|----------------|
| <name>    | <rel>        | <age>     | SSN/ITIN | Qualifying child / Qualifying relative |
| ...       | ...          | ...       | ...      | ...            |

- Line 4 N_CTC (qualifying children): X
- Line 6 N_ODC (other dependents):    Y

## Part I — lines 1–14
- Line 1  AGI (1040 line 11a):        $XXX,XXX
- Line 2a–2d exclusions added back:   $X
- Line 3  MAGI:                       $XXX,XXX
- Line 5  CTC tentative: X × $2,200 = $X,XXX
- Line 7  ODC tentative: Y ×   $500 = $X,XXX
- Line 8  **Tentative total**:        $X,XXX
- Line 9  Threshold:                  $XXX,XXX
- Line 10 Excess (rounded up to next $1,000): $X,XXX
- Line 11 Phase-out reduction (line 10 × 5%): $X,XXX
- Line 12 **Allowed credit** (line 8 − line 11): $X,XXX
- Line 13 Credit Limit Worksheet A:   $X,XXX
- Line 14 Non-refundable credit = min(line 12, line 13): $X,XXX → **1040 line 19**

## Part II-A / II-B / II-C — lines 15–27
- Line 15 Reserved
- Line 16a Leftover (line 12 − line 14): $X,XXX
- Line 16b Per-child cap (X × $1,700):   $X,XXX
- Line 17 smaller of 16a or 16b:         $X,XXX
- Line 18a Earned income:                $XX,XXX
- Line 18b Nontaxable combat pay:        $X
- Line 19 Earned income over $2,500:     $XX,XXX
- Line 20 15% of line 19:                $X,XXX
- Lines 21–26 (only if line 16b ≥ $5,100 and line 20 < line 17, or Puerto Rico): $X,XXX each
- Line 27 **ACTC**:                      $X,XXX → **1040 line 28**

## Verification
- Line 14 + line 27 ≤ line 12: ✓ | <off by $X>
- Each dependent classified once: ✓
- SSN-before-due-date verified for the filer and each qualifying child: ✓ | <list issues>

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list warnings>
- Next steps: <hand-off items>

## Sources cited in this draft
- IRS Schedule 8812 (Form 1040) (tax year YYYY)
- IRS Instructions for Schedule 8812 (tax year YYYY)
- IRC §24(b)(1), §24(h)(3) — phase-out ($50 per $1,000 above $200,000 / $400,000)
- IRC §24(h)(2), §24(i)(2) — $2,200 credit amount (indexed after 2025)
- IRC §24(h)(4) — Credit for Other Dependents
- IRC §24(h)(5), §24(i)(1) — Refundable cap (indexed; $1,700 for 2025 and 2026)
- IRC §24(h)(7) — SSN requirement for the taxpayer and the qualifying child
- Rev. Proc. 2025-32 §4.05 (2026 amounts)
```

---

## References

Loaded on demand based on the user's situation.

- [`references/line-by-line.md`](./references/line-by-line.md) — Every line of Schedule 8812 with examples
- [`references/qualifying-child-test.md`](./references/qualifying-child-test.md) — All 7 tests for CTC qualifying children
- [`references/qualifying-relative-test.md`](./references/qualifying-relative-test.md) — All 4 tests for ODC qualifying relatives
- [`references/actc-refundability.md`](./references/actc-refundability.md) — Earned income method vs. SS-tax method, 3+ children rule
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Audit-trip mistakes with citations
- [`filing.md`](./filing.md) — How an agent files Schedule 8812 via IRS Free File, FFFF, paid software, or paper

## Examples

End-to-end worked personas. Use these when the user's situation is similar.

- [`examples/mfj-two-kids.md`](./examples/mfj-two-kids.md) — MFJ couple with 2 qualifying children, AGI $150K, full $4,400 CTC, no ACTC
- [`examples/single-parent-mixed.md`](./examples/single-parent-mixed.md) — Single parent (HoH) with 1 qualifying child + 1 elderly parent dependent, modest income, ACTC kicks in
- [`examples/high-income-phaseout.md`](./examples/high-income-phaseout.md) — MFJ with 3 children at AGI $450,000, phase-out cuts the $6,600 credit by $2,500

## Sources

Authoritative sources used. Re-verify each year — IRS revises forms and figures annually.

- [Schedule 8812 (Form 1040), 2025](https://www.irs.gov/pub/irs-pdf/f1040s8.pdf) — the form itself (line map in this skill)
- [Instructions for Schedule 8812, 2025](https://www.irs.gov/pub/irs-pdf/i1040s8.pdf) — What's New ($2,200, SSN rule), Credit Limit Worksheets A/B, Earned Income Chart/Worksheet
- [About Schedule 8812](https://www.irs.gov/forms-pubs/about-schedule-8812-form-1040) — IRS landing page; check for the next revision and post-release updates
- [Form 1040, 2025](https://www.irs.gov/pub/irs-pdf/f1040.pdf) — lines 19 and 28 receive the Schedule 8812 totals; Dependents row (7) checkboxes
- [Instructions for Form 1040, 2025](https://www.irs.gov/pub/irs-pdf/i1040gi.pdf) — Who Qualifies as Your Dependent, Steps 1–5 (pp.17–22)
- [Publication 501, 2025](https://www.irs.gov/pub/irs-pdf/p501.pdf) — dependency tests; qualifying relative gross income under $5,200
- Publication 972 — obsolete; the IRS stopped issuing it for tax year 2021 and moved its content into the Schedule 8812 instructions
- [Rev. Proc. 2024-40](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) — 2025 inflation adjustments; [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) §4.05 — 2026 CTC $2,200, refundable $1,700
- IRC §24(a), §24(h)(2), §24(i)(2) — credit amount ($2,200; indexed after 2025)
- IRC §24(b)(1), §24(h)(3) — MAGI phase-out ($50 per $1,000 above $200K/$400K)
- IRC §24(c) — Qualifying child definition (cross-references §152(c))
- IRC §24(d) — refundable portion (15% over $2,500 per §24(h)(6); 3+ children social security tax alternative)
- IRC §24(h)(4) — Credit for Other Dependents
- IRC §24(h)(5), §24(i)(1) — Refundable cap (indexed)
- IRC §24(h)(7) — SSN requirement for the taxpayer and the qualifying child
- IRC §152 — Dependent definition (qualifying child + qualifying relative tests)
- One Big Beautiful Bill Act (P.L. 119-21) §70104 — made the post-2017 CTC rules permanent and set $2,200 for 2025

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms, publications, and statute. It is not tax advice. Edge cases — such as divorced/separated parents, multiple support agreements (Form 2120), kiddie tax interactions, dependents who file their own return, and Puerto Rico residents — warrant a licensed tax professional's review.
