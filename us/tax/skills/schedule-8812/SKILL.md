---
name: schedule-8812
title: Schedule 8812 — Credits for Qualifying Children and Other Dependents
description: 'Use this skill when an individual taxpayer needs to claim the Child Tax Credit (CTC), the refundable Additional Child Tax Credit (ACTC), or the Credit for Other Dependents (ODC) on Form 1040 by completing Schedule 8812. Triggers on phrases like "Child Tax Credit", "CTC", "qualifying child credit", "Schedule 8812", "Credit for Other Dependents", "ODC", "ACTC", "refundable child credit", "credit for elderly parent dependent", "claim $2,000 per child", "kid tax credit". Do NOT use for: dependent care expenses (use Form 2441 skill), Earned Income Tax Credit (use Schedule EIC skill), Adoption Credit (use Form 8839 skill), or the Child and Dependent Care Credit. The Child Tax Credit and the Child and Dependent Care Credit are two different credits — this skill is only for the former.'
author: jupid-tax
author_url: https://github.com/jupid-tax/jupid-skills/tree/main/forms/schedule-8812
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: tax
language: en
---

# Schedule 8812 — Credits for Qualifying Children and Other Dependents

This skill computes three closely-related credits on a single schedule:

1. **Child Tax Credit (CTC)** — non-refundable credit of up to $2,000 per qualifying child under 17
2. **Additional Child Tax Credit (ACTC)** — the refundable portion of the CTC, up to $1,700 per qualifying child for tax year 2025 (2026 figure inflation-adjusted; verify before filing)
3. **Credit for Other Dependents (ODC)** — non-refundable credit of $500 per qualifying relative or other dependent who doesn't meet CTC age/relationship tests

The skill walks through each of the three credits, applies the MAGI-based phase-out, computes the refundable portion using the earned income test, and produces an audit-grade worksheet showing every line including zeros.

The arithmetic is mechanical. The judgment is in (1) which children count as "qualifying children" for CTC vs. "qualifying relatives" for ODC, (2) whether the SSN-by-due-date requirement is met (no SSN = no CTC, only ODC), and (3) how the phase-out interacts with the refundable cap.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Schedule 8812, the Child Tax Credit, CTC, ACTC, or the Credit for Other Dependents
- The user asks "how much credit do I get for my kids?", "is my child still eligible at age 17?", "can I claim my mother as a dependent for the credit?", or similar
- The user has dependents on their Form 1040 and is computing total tax (Schedule 8812 reduces tax on Form 1040 Line 19 + Line 28)
- The user's tax software is returning a CTC amount the user wants to verify

Do **not** engage this skill when:

- The user is asking about the **Child and Dependent Care Credit** (Form 2441) — different credit, for childcare expenses while parent is working. The two are often confused.
- The user is asking about the Earned Income Tax Credit (EITC) — use Schedule EIC skill (forthcoming)
- The user is asking about the Adoption Credit — use Form 8839 skill (forthcoming)
- The user wants to know how to claim a dependent on their return at all — that's a Form 1040 question; this skill assumes dependent eligibility is established and the question is the credit value

For users with multiple credits (CTC + EITC + Childcare), run this skill for the CTC/ODC portion only; the other credits go through their own skills, and Form 1040 totals them all.

---

## Prerequisites

Before producing anything, the agent must collect the following. If any are missing, **ASK** with a tight question and stop.

1. **Tax year** the return covers. CTC/ACTC parameters change yearly (refundable cap is inflation-adjusted; phase-out thresholds have been static since TCJA but post-OBBBA verify). For tax year 2025: refundable cap $1,700/child. For tax year 2026: verify the inflation-adjusted refundable cap; the per-child non-refundable amount of $2,000 was made permanent under OBBBA.

2. **Filer's filing status**. Single, MFJ, MFS, HoH, QSS. The MAGI phase-out thresholds depend on this.

3. **Filer's MAGI** for the year. For most filers, MAGI = AGI (Form 1040 Line 11). For some, it's AGI + foreign earned income exclusion + foreign housing exclusion/deduction + certain Puerto Rico/territories income (Schedule 8812 instructions Worksheet B). Confirm with the user.

4. **Earned income for the year**. Specifically: wages (1040 Line 1a) + self-employment income net of half-of-SE-tax + nontaxable combat pay (if elected to include). Required for the ACTC refundability test ($2,500 minimum earned income threshold).

5. **List of every dependent**. For each, collect:
   - Legal name
   - SSN or ITIN or ATIN
   - Relationship to filer
   - Birthdate
   - Whether they lived with the filer for more than half the year
   - Whether the filer (or filer's spouse if MFJ) provided more than half of their support
   - Whether they're a U.S. citizen, U.S. national, or U.S. resident alien
   - Whether they file their own joint return (disqualifies them as dependent unless filing only to claim refund)
   - For children: whether they have an SSN issued by the due date of the return
   - For each: dependent classification ("qualifying child" or "qualifying relative" — see [`references/qualifying-child-test.md`](./references/qualifying-child-test.md))

6. **Tax before credits**. From Form 1040 Line 18 (after Schedule 2 Line 3 alternative minimum tax). The CTC + ODC are limited to this amount (non-refundable portion).

7. **Other tax credits already computed** that go above CTC on Form 1040 (e.g., Foreign Tax Credit on Schedule 3 Line 1). The ordering matters because CTC is limited by remaining tax after upper credits.

For the refundable ACTC computation, additionally ask:

- Filer's Social Security tax + Medicare tax + half of self-employment tax for the year (used in the alternative ACTC test for 3+ qualifying children)

---

## Workflow

Execute these steps in order.

### Step 1 — Classify each dependent

For each dependent on the user's 1040, determine whether they are:

**(a) A qualifying child for CTC purposes** — must satisfy ALL of:

- Relationship: filer's son, daughter, stepchild, foster child, brother, sister, half-brother/sister, stepbrother/sister, or descendant of any of these (e.g., grandchild, niece, nephew)
- Age: under 17 at the end of the tax year (so 16 or younger as of December 31)
- Residency: lived with filer more than half the year (with exceptions for temporary absence, divorce, etc.)
- Support: did not provide more than half of their own support
- Joint return: did not file a joint return for the year (other than to claim a refund)
- Citizenship: U.S. citizen, U.S. national, or U.S. resident alien
- **SSN by due date**: must have an SSN issued by the due date of the return (including extensions). ITIN or ATIN does NOT qualify for CTC. (Per IRC §24(h)(7).)

**(b) A qualifying relative or other dependent for ODC purposes** — anyone who can be claimed as a dependent on the 1040 but does NOT meet (a). Examples:

- The filer's child who is 17 or older
- The filer's parent or other relative claimed as a dependent
- A child without an SSN (has an ITIN or ATIN) — qualifies for ODC, not CTC
- A non-relative living with the filer who meets the qualifying-relative test
- Any dependent with an ITIN

See [`references/qualifying-child-test.md`](./references/qualifying-child-test.md) and [`references/qualifying-relative-test.md`](./references/qualifying-relative-test.md) for the full tests. When in doubt, ASK the user the specific facts (age, SSN status, residency).

### Step 2 — Count qualifying children and other dependents

Build the table:

```
| Dependent name  | Relationship | Age 12/31 | SSN by due date | Classification |
|-----------------|--------------|-----------|------------------|----------------|
| Sophia Carter   | Daughter     | 9         | Yes              | Qualifying child (CTC) |
| Liam Carter     | Son          | 17        | Yes              | Qualifying relative (ODC) |
| Maria Carter    | Mother       | 71        | Yes              | Qualifying relative (ODC) |
```

Count:
- **N_CTC** = number of qualifying children
- **N_ODC** = number of other dependents

### Step 3 — Compute the tentative credit

For tax year 2025 / 2026 (post-OBBBA, $2,000 made permanent — verify 2026 figure):

```
Tentative CTC = N_CTC × $2,000
Tentative ODC = N_ODC × $500
Tentative total = Tentative CTC + Tentative ODC
```

This is the Schedule 8812 Line 8 (or the equivalent — verify line numbers against the current revision of the form).

### Step 4 — Apply the MAGI phase-out

The credit phases out at higher incomes. Phase-out under IRC §24(b):

- Threshold: **$200,000** (single, HoH, MFS, QSS) or **$400,000** (MFJ). These thresholds were set by TCJA 2017 and made permanent for purposes of the $2,000 base by OBBBA — verify current.
- Phase-out rate: **$5 reduction per $1,000** (or fraction thereof) of MAGI **above** the threshold.

```
Excess MAGI = max(0, MAGI − threshold)
Excess (rounded up to nearest $1,000) = ceiling(Excess MAGI / 1000) × 1000
Phase-out reduction = Excess × $5 / $1,000  (i.e., $50 per $1,000 of rounded excess)
```

Note: the $1,000 increment is the IRS rounding rule — any amount above the threshold rounds **up** to the next $1,000 for the calculation. So MAGI of $400,500 (MFJ) produces excess of $1,000 (rounded up from $500), and phase-out reduction = $5.

```
Allowed credit = max(0, Tentative total − Phase-out reduction)
```

### Step 5 — Limit by tax liability (non-refundable portion)

The CTC and ODC are non-refundable up to the filer's pre-credit tax liability. Compute:

```
Pre-credit tax = Form 1040 Line 18 (income tax + AMT) − certain prior credits per Schedule 3
Non-refundable credit = min(Allowed credit, Pre-credit tax)
```

This becomes **Form 1040 Line 19** ("Child Tax Credit or Credit for Other Dependents").

### Step 6 — Compute the refundable Additional Child Tax Credit (ACTC)

If the non-refundable credit was capped by tax liability (i.e., Allowed credit > Pre-credit tax) AND the filer has qualifying children, the leftover may be refundable as the ACTC.

For tax year 2025 (verify 2026 inflation adjustment): refundable cap is **$1,700 per qualifying child**. Source: IRC §24(h)(5), inflation-indexed.

```
Step 6a — Earned income test:
  Earned income > $2,500? → Continue
  Earned income ≤ $2,500? → ACTC = $0 (no refundable credit)

Step 6b — Earned income excess:
  Earned income excess = max(0, Earned income − $2,500)
  Earned income method ACTC = Earned income excess × 15%

Step 6c — Per-child cap:
  Per-child cap = N_CTC × $1,700 (verify 2026)

Step 6d — Cap by leftover credit:
  Leftover = Allowed credit − Non-refundable credit
  ACTC tentative = min(Leftover, Earned income method ACTC, Per-child cap)

Step 6e — Alternative method (3+ qualifying children only):
  Some filers benefit from the "Social Security tax method" — uses SS+Medicare+half-SE
  if more than the earned income method and the filer has 3+ qualifying children.
  Use the larger of the two methods.

  See [`references/actc-refundability.md`](./references/actc-refundability.md).
```

The result becomes **Form 1040 Line 28** ("Refundable child tax credit or additional child tax credit").

### Step 7 — Run validation checks

See **Validation** below.

### Step 8 — Produce the deliverable

See **Output format** below.

### Step 9 — Hand off downstream

State the next forms the user will need:

- Form 1040 Line 19 ← non-refundable CTC + ODC from Step 5
- Form 1040 Line 28 ← ACTC from Step 6
- If MFJ and filing late, confirm SSN-by-due-date requirement is still met
- If a dependent's SSN was issued after the due date (including extensions), that dependent is not eligible for CTC — only ODC

### Step 10 — File the return (optional, if the user wants the agent to file)

If the agent has browser-automation tooling and the user explicitly authorizes filing, follow [`filing.md`](./filing.md). It contains:

- Decision tree to pick a filing channel (FFFF, paid software, paper, IRS Direct File)
- Field-by-field mapping from this skill's draft to FFFF Schedule 8812 fields
- Pre-flight checklist
- Security/consent rules

If the user only wants the worksheet, skip this step.

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Schedule 8812 structure

Schedule 8812 is divided into multiple parts (verify current revision):

- **Part I-A — Computation of CTC and ODC** — head count of qualifying children and other dependents, tentative credit, MAGI phase-out
- **Part I-B / I-C — Refundable / Non-refundable allocation** — apply the tax-liability limit, compute leftover for ACTC
- **Part II-A — ACTC (most filers)** — earned income method, per-child refundable cap
- **Part II-B — ACTC (3+ qualifying children alternative)** — SS+Medicare tax method
- **Part II-C — Additional ACTC for Puerto Rico residents** (specialized; out of scope for this skill except by reference)

Each filing year, the IRS may renumber lines. The agent should reference the current-year [Form Schedule 8812](https://www.irs.gov/pub/irs-pdf/f1040s8.pdf) for the exact line numbers when filing.

### The two-page summary

```
Step 1. Count qualifying children with SSN by due date (line varies)
Step 2. Count other dependents (line varies)
Step 3. Tentative CTC = N_CTC × $2,000; Tentative ODC = N_ODC × $500
Step 4. MAGI phase-out (above $200K single / $400K MFJ — $5 per $1,000 over)
Step 5. Non-refundable credit (min of allowed credit, tax liability) → 1040 Line 19
Step 6. Refundable ACTC (earned income > $2,500, 15% method, $1,700/child cap) → 1040 Line 28
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

- [ ] N_CTC + N_ODC = total dependents on Form 1040 (every dependent must be classified as one or the other; no dependent in both categories)
- [ ] Tentative total = N_CTC × $2,000 + N_ODC × $500
- [ ] Phase-out reduction is computed using **rounded-up** excess MAGI (next $1,000)
- [ ] Allowed credit ≥ 0 (cannot be negative)
- [ ] Non-refundable credit ≤ Tax liability before credits
- [ ] ACTC ≤ Per-child refundable cap (N_CTC × $1,700 for 2025)
- [ ] ACTC ≤ Leftover = Allowed credit − Non-refundable credit
- [ ] Non-refundable credit + ACTC = Allowed credit (total credit used)
- [ ] If MAGI ≥ threshold + (Tentative total / $5 × $1,000), Allowed credit = $0

### Sanity checks

Surface as warnings, do not block:

- [ ] User has dependents but no SSN information collected → ask explicitly for each dependent
- [ ] User has a child age 17+ classified as qualifying child → reclassify as qualifying relative (ODC, not CTC)
- [ ] User has a child with ITIN classified as qualifying child → reclassify as ODC (no CTC for ITIN children)
- [ ] User has earned income > $2,500 but ACTC computed as $0 → verify the user has at least one qualifying child (ACTC requires CTC eligibility)
- [ ] User has 3+ qualifying children but the alternative SS-tax method was not computed → run both methods and use the higher
- [ ] Phase-out fully eliminates the credit — verify MAGI is correct and that the user understands they're above the phase-out
- [ ] Filer is MFS and claims CTC — MFS may file Schedule 8812 but must coordinate with the other spouse to avoid double-claiming the same child; ASK
- [ ] Filer's dependent is a U.S. resident alien but lived in Mexico/Canada more than half the year — residency rules apply differently

### Cross-form checks

- [ ] Each qualifying child listed on Schedule 8812 must be listed as a dependent on Form 1040
- [ ] Each "Other Dependent" listed on Schedule 8812 must be listed as a dependent on Form 1040
- [ ] If filer also claims EITC, the same children may be qualifying children for both (no double-claim issue, but verify name+SSN matches)
- [ ] If filer also claims Childcare Credit (Form 2441), the same children may be qualifying for both
- [ ] If filer's MAGI ≥ phase-out fully-eliminated point, the agent should warn that none of the CTC/ODC is available — different from "I owe no tax so I don't need it"

---

## Output format

The deliverable is a worksheet showing every step of the computation, plus the line-entries for Form 1040. Format:

```markdown
# Schedule 8812 — DRAFT WORKSHEET for tax year YYYY

## Filing facts
- Filing status: <Single | MFJ | MFS | HoH | QSS>
- Filer's MAGI: $XXX,XXX
- Earned income: $XXX,XXX
- Tax before credits (1040 Line 18): $XXX,XXX
- Phase-out threshold: $200,000 (single, HoH, QSS, MFS) or $400,000 (MFJ)

## Dependents classified
| Dependent | Relationship | Age 12/31 | SSN/ITIN | Classification |
|-----------|--------------|-----------|----------|----------------|
| <name>    | <rel>        | <age>     | SSN/ITIN | Qualifying child / Qualifying relative |
| ...       | ...          | ...       | ...      | ...            |

- N_CTC (qualifying children): X
- N_ODC (other dependents):    Y

## Step 3 — Tentative credit
- CTC tentative:   X × $2,000 = $X,XXX
- ODC tentative:   Y ×  $500  = $X,XXX
- **Tentative total**:           $X,XXX

## Step 4 — MAGI phase-out
- MAGI:                    $XXX,XXX
- Threshold:               $XXX,XXX
- Excess (rounded up to next $1,000): $X,XXX
- Phase-out reduction:     $X,XXX  (Excess × $5 / $1,000)
- **Allowed credit**:      $X,XXX  (Tentative total − Phase-out reduction)

## Step 5 — Non-refundable credit (1040 Line 19)
- Tax before credits:      $X,XXX
- Non-refundable credit:   $X,XXX  (min of Allowed credit and Pre-credit tax)
- **1040 Line 19**:        $X,XXX

## Step 6 — Refundable ACTC (1040 Line 28)
- Leftover (Allowed credit − Non-refundable credit): $X,XXX
- Earned income:                       $XX,XXX
- Earned income excess (over $2,500):  $XX,XXX
- Earned income method (15%):          $X,XXX
- Per-child refundable cap (X × $1,700): $X,XXX
- Alternative SS-tax method (if 3+ qualifying children): $X,XXX
- **ACTC** = min(Leftover, max(EI method, SS method), Per-child cap): $X,XXX
- **1040 Line 28**:        $X,XXX

## Verification
- Allowed credit = Non-refundable + ACTC: ✓ | <off by $X>
- Each dependent classified once: ✓
- SSN-by-due-date verified for each qualifying child: ✓ | <list issues>

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list warnings>
- Next steps: <hand-off items>

## Sources cited in this draft
- IRS Schedule 8812 (Rev. YYYY-MM)
- IRS Instructions for Schedule 8812 (Rev. YYYY-MM)
- IRC §24 — Child Tax Credit
- IRC §24(h)(4) — Credit for Other Dependents
- IRC §24(h)(5) — Refundable cap (inflation-adjusted)
- IRC §24(h)(7) — SSN-by-due-date requirement
- Pub 972 (historical CTC reference; verify currency)
```

---

## References

Loaded on demand based on the user's situation.

- [`references/line-by-line.md`](./references/line-by-line.md) — Every line of Schedule 8812 with examples
- [`references/qualifying-child-test.md`](./references/qualifying-child-test.md) — All 7 tests for CTC qualifying children
- [`references/qualifying-relative-test.md`](./references/qualifying-relative-test.md) — All 4 tests for ODC qualifying relatives
- [`references/actc-refundability.md`](./references/actc-refundability.md) — Earned income method vs. SS-tax method, 3+ children rule
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Audit-trip mistakes with citations
- [`filing.md`](./filing.md) — How an agent files Schedule 8812 via FFFF, paid software, paper, or IRS Direct File

## Examples

End-to-end worked personas. Use these when the user's situation is similar.

- [`examples/mfj-two-kids.md`](./examples/mfj-two-kids.md) — MFJ couple with 2 qualifying children, AGI $150K, full $4,000 CTC + $1,400 ACTC if needed
- [`examples/single-parent-mixed.md`](./examples/single-parent-mixed.md) — Single parent with 1 qualifying child + 1 elderly parent dependent, modest income, ACTC kicks in
- [`examples/high-income-phaseout.md`](./examples/high-income-phaseout.md) — MFJ with 3 children at AGI $450,000, partial phase-out reducing the CTC

## Sources

Authoritative sources used. Re-verify each year — IRS revises forms and figures annually; OBBBA 2025 made some changes permanent.

- [Schedule 8812 (Form 1040)](https://www.irs.gov/pub/irs-pdf/f1040s8.pdf) — the form itself
- [Instructions for Schedule 8812](https://www.irs.gov/pub/irs-pdf/i1040s8.pdf) — line-by-line IRS guidance
- [About Schedule 8812](https://www.irs.gov/forms-pubs/about-schedule-8812-form-1040) — IRS landing page
- [Form 1040](https://www.irs.gov/pub/irs-pdf/f1040.pdf) — Lines 19 and 28 receive the Schedule 8812 totals
- [Publication 972](https://www.irs.gov/pub/irs-pdf/p972.pdf) — Child Tax Credit (historical reference; verify currency)
- IRC §24(a) — Child Tax Credit base
- IRC §24(b) — MAGI phase-out ($5 per $1,000 above $200K/$400K)
- IRC §24(c) — Qualifying child definition (cross-references §152(c))
- IRC §24(h)(4) — Credit for Other Dependents
- IRC §24(h)(5) — Refundable cap (inflation-adjusted; verify annual figure)
- IRC §24(h)(7) — SSN by due date requirement (TCJA)
- IRC §152 — Dependent definition (qualifying child + qualifying relative tests)
- One Big Beautiful Bill Act (OBBBA) of 2025 — made $2,000 base CTC permanent

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms, publications, and statute. It is not tax advice. Edge cases — such as divorced/separated parents, multiple support agreements (Form 2120), kiddie tax interactions, dependents who file their own return, and Puerto Rico residents — warrant a licensed tax professional's review.
