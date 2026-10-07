# Schedule 8812 — Line-by-Line Reference

Complete lookup for every line of Schedule 8812. Use when the agent needs to confirm what each line means or how it interacts with the user's return.

**Revision**: verified against the **2025 Schedule 8812 (Form 1040)** (created 7/30/25) and the **2025 Instructions for Schedule 8812** (Jan 23, 2026), filed in 2026. The IRS renumbers lines from time to time; before using this map for a later tax year, re-check the current revision at [About Schedule 8812](https://www.irs.gov/forms-pubs/about-schedule-8812-form-1040).

Source: [Schedule 8812 (2025)](https://www.irs.gov/pub/irs-pdf/f1040s8.pdf), [Instructions for Schedule 8812 (2025)](https://www.irs.gov/pub/irs-pdf/i1040s8.pdf), IRC §24. (Pub 972 is obsolete: the IRS stopped issuing it for tax year 2021 and moved its content into the Schedule 8812 instructions.)

---

## Part I — Child Tax Credit and Credit for Other Dependents

**Line 1 — Amount from Form 1040 (or 1040-SR, 1040-NR) line 11a**

Adjusted gross income.

**Line 2a — Income from Puerto Rico that you excluded**

**Line 2b — Amounts from Form 2555 lines 45 and 50**

Foreign earned income exclusion and foreign housing exclusion.

**Line 2c — Amount from Form 4563 line 15**

Income excluded by bona fide residents of American Samoa.

**Line 2d — Add lines 2a through 2c**

**Line 3 — Add lines 1 and 2d**

This is modified AGI for the CTC and ODC (instructions, "Modified AGI"; IRC §24(b)(1) adds back amounts excluded under §§911, 931, 933). If none of lines 2a–2c apply, line 3 = AGI.

**Line 4 — Number of qualifying children under age 17 with the required social security number**

Count the "Child tax credit" boxes checked in row (7) of the Dependents section of Form 1040 or 1040-SR (row (6) on Form 1040-NR). Each child must be a qualifying child under IRC §24(c) (cross-references §152(c)), under 17 at the end of the year, and have an SSN valid for employment issued before the due date of the return including extensions (IRC §24(h)(7); instructions p.1). Starting with 2025 returns, the taxpayer (or at least one spouse on a joint return) must also have such an SSN; the other spouse needs an SSN or ITIN issued on or before the due date. ITIN and ATIN children do NOT count here. See [`qualifying-child-test.md`](./qualifying-child-test.md).

**Line 5 — Multiply line 4 by $2,200**

$2,200 per qualifying child for 2025 (form line 5; IRC §24(h)(2) as amended by P.L. 119-21 §70104). For 2026 the amount is also $2,200 (Rev. Proc. 2025-32 §4.05(1)); it is indexed for inflation after 2025 under IRC §24(i)(2), rounded down to a multiple of $100.

**Line 6 — Number of other dependents, including any qualifying children who are not under age 17 or who do not have the required SSN**

Count the "Credit for other dependents" boxes checked in row (7). Do not include yourself, your spouse, anyone who is not a U.S. citizen, U.S. national, or U.S. resident alien, or anyone included on line 4 (form caution). The dependent must have an SSN, ITIN, or ATIN issued on or before the due date (including extensions); an ITIN/ATIN applied for by the due date and later issued counts (instructions p.1). See [`qualifying-relative-test.md`](./qualifying-relative-test.md).

**Line 7 — Multiply line 6 by $500**

The Credit for Other Dependents (ODC), IRC §24(h)(4). Not indexed.

**Line 8 — Add lines 5 and 7**

Tentative total credit before phase-out and tax-liability limit.

**Line 9 — Threshold by filing status**

- Married filing jointly: $400,000
- All other filing statuses: $200,000

IRC §24(h)(3). Not indexed for inflation.

**Line 10 — Subtract line 9 from line 3**

```
If zero or less: 0
If more than zero and not a multiple of $1,000: round UP to the next multiple of $1,000
```

The form's own examples: a result of $425 is entered as $1,000; $1,025 as $2,000. So MAGI of $400,500 (MFJ) gives line 10 = $1,000, not $500.

**Line 11 — Multiply line 10 by 5% (0.05)**

The phase-out reduction: $50 for each $1,000 (or fraction) of MAGI over the threshold (IRC §24(b)(1)). $1,000 of excess → $50; $10,000 → $500; $44,000 of excess fully eliminates the $2,200 credit for one child.

**Line 12 — Is line 8 more than line 11?**

- No: stop. No CTC, ODC, or ACTC.
- Yes: line 8 − line 11. This is the credit allowed before the tax-liability limit.

**Line 13 — Amount from Credit Limit Worksheet A**

Credit Limit Worksheet A (instructions p.4):

```
1. Form 1040 line 18 (tax + Schedule 2 line 3)
2. Schedule 3 lines 1 + 2 + 3 + 4 + 5b + 6d + 6f + 6l + 6m
3. Line 1 − line 2
4. Credit Limit Worksheet B amount, or 0 if not required
5. Line 3 − line 4 → Schedule 8812 line 13
```

Credit Limit Worksheet B is required only if all three apply: (1) the filer claims the mortgage interest credit (Form 8396), adoption credit (Form 8839), residential clean energy credit (Form 5695 Part I), or DC first-time homebuyer credit (Form 8859); (2) the filer is not filing Form 2555; (3) line 4 is more than zero. It runs a preliminary ACTC computation (Earned Income Worksheet, Part II-B equivalents) and enters on CLW A line 4 the total of Schedule 3 lines 5a, 6c, 6g and 6h (instructions pp.4–6).

**Line 14 — Smaller of line 12 or line 13**

The non-refundable CTC + ODC. Enter on **Form 1040, 1040-SR, or 1040-NR line 19**.

If line 12 is more than line 14, the filer may be able to take the ACTC. Complete Form 1040 or 1040-SR through line 27a (Form 1040-NR through line 26) and Schedule 3 line 11 before Part II-A (form note under line 14).

---

## Part II-A — Additional Child Tax Credit for All Filers

Caution printed on the form: if you file Form 2555, you cannot claim the ACTC.

**Line 15 — Reserved for future use**

**Line 16a — Subtract line 14 from line 12**

If zero, stop: no ACTC.

**Line 16b — Number of qualifying children under age 17 with the required SSN × $1,700**

Same number of children as line 4 (form tip). $1,700 per child for 2025 (instructions, Reminders) and 2026 (Rev. Proc. 2025-32 §4.05(2)); IRC §24(h)(5) as indexed by §24(i)(1). If zero, stop.

**Line 17 — Smaller of line 16a or line 16b**

**Line 18a — Earned income**

Use the Earned Income Chart (instructions p.7). If the filer uses an optional method for net SE earnings, or does not claim the EIC, use the Earned Income Worksheet (p.8):

```
1a  Form 1040 line 1z
1b  Nontaxable combat pay (also entered on line 18b)
2a  Statutory employee income (Schedule C line 1)
2b  Net profit or (loss): Schedule C line 31, K-1 (1065) box 14 code A (non-farm)
2c–2e Net farm profit or (loss) (farm optional method limit)
3   Combine 1a, 1b, 2a, 2b, 2e (if zero or less, enter 0 on line 18a)
4   Medicaid waiver payments excluded on Schedule 1 line 8s that the filer chooses NOT to include
5   Schedule 1 line 15 (deductible part of SE tax)
7   Line 3 − (line 4 + line 5) → line 18a
```

Filers who claim the EIC and completed EIC Worksheet B take line 4b of that worksheet plus nontaxable combat pay not elected for the EIC (clergy adjustments apply). Income excluded under a tax treaty is not earned income (instructions, line 18a caution). Bona fide residents of Puerto Rico exclude income earned in Puerto Rico.

**Line 18b — Nontaxable combat pay**

Total for the filer and spouse (Form 1040 line 1i or W-2 box 12 code Q). For the ACTC, combat pay is always included in earned income (IRC §24(d)(1) flush language); the election to include combat pay applies only to the EIC.

**Line 19 — Is line 18a more than $2,500?**

- No: leave blank, enter 0 on line 20.
- Yes: line 18a − $2,500. (IRC §24(h)(6).)

**Line 20 — Multiply line 19 by 15% (0.15)**

Then the form's routing question: "On line 16b, is the amount $5,100 or more?" ($5,100 = 3 children × $1,700.)

- **No** (fewer than 3 qualifying children): if a bona fide resident of Puerto Rico, go to line 21; otherwise skip Part II-B and enter the smaller of line 17 or line 20 on line 27.
- **Yes**: if line 20 ≥ line 17, skip Part II-B and enter line 17 on line 27; otherwise go to line 21.

---

## Part II-B — Certain Filers Who Have Three or More Qualifying Children and Bona Fide Residents of Puerto Rico

**Line 21 — Withheld social security, Medicare, and Additional Medicare taxes from Form(s) W-2 boxes 4 and 6**

Include the spouse's amounts if MFJ. If the employer withheld or the filer paid Additional Medicare Tax or tier 1 RRTA taxes, use the instructions' Additional Medicare Tax and RRTA Tax Worksheet (p.9). Bona fide residents of Puerto Rico include Puerto Rico Forms 499R-2/W-2PR boxes 21 and 23.

**Line 22 — Schedule 1 line 15 + Schedule 2 line 5 + Schedule 2 line 6 + Schedule 2 line 13**

Deductible half of SE tax; SS/Medicare tax on unreported tips (Form 4137); on wages from Form 8919; uncollected SS/Medicare tax on tips or group-term life insurance.

**Line 23 — Add lines 21 and 22**

**Line 24 — Form 1040/1040-SR filers: Form 1040 line 27a (EIC) + Schedule 3 line 11 (excess social security and tier 1 RRTA withheld). Form 1040-NR filers: Schedule 3 line 11.**

**Line 25 — Line 23 − line 24; if zero or less, 0**

**Line 26 — Larger of line 20 or line 25**

Then enter the smaller of line 17 or line 26 on line 27.

---

## Part II-C — Additional Child Tax Credit

**Line 27 — Additional child tax credit**

Enter on **Form 1040, 1040-SR, or 1040-NR line 28**. A filer who does not want to claim the ACTC checks the box on Form 1040 line 28.

---

## Where Schedule 8812 totals go on Form 1040 (2025)

| Schedule 8812 line | Form 1040 line | Description |
|--------------------|----------------|-------------|
| Line 1 | ← line 11a | AGI |
| Line 14 | → line 19 | "Child tax credit or credit for other dependents from Schedule 8812" |
| Line 27 | → line 28 | "Additional child tax credit (ACTC) from Schedule 8812" |
| Lines 4 and 6 | ← Dependents row (7) | "Child tax credit" / "Credit for other dependents" boxes |

Line 14 + line 27 can never exceed line 12; any part of line 12 that is neither absorbed by tax nor refundable is lost.

---

## Bona fide residents of Puerto Rico

A bona fide resident of Puerto Rico with at least one qualifying child may claim the ACTC on Schedule 8812 (completing Part II-A and Part II-B even with fewer than 3 children) or, if not required to file Form 1040, in Part II of Form 1040-SS (instructions p.3; Pub 570 for residency). Out of scope for this skill beyond these line rules: refer to a tax professional.

---

## What's NOT on Schedule 8812

The agent should NOT compute or include on Schedule 8812:

- **Earned Income Tax Credit (EITC)** — Schedule EIC, Form 1040 line 27a
- **Child and Dependent Care Credit** — Form 2441, Schedule 3 line 2
- **Adoption Credit** — Form 8839: nonrefundable part on Schedule 3 line 6c, refundable part (up to $5,000 per child for 2025) on Form 1040 line 30
- **American Opportunity / Lifetime Learning Credits** — Form 8863 (Schedule 3 line 3; refundable AOTC on Form 1040 line 29)
- **Premium Tax Credit reconciliation** — Form 8962

If the user mentions any of these, redirect to the appropriate form (no skills in this repo yet for EITC, Form 2441, Form 8839, or Form 8863; see [`../../form-8962/SKILL.md`](../../form-8962/SKILL.md) for the PTC).

---

## A note on prior-year ARPA expansion

For tax year 2021 only, the American Rescue Plan Act expanded CTC to $3,000-$3,600 per child, made it fully refundable, and provided for advance payments. Those rules **expired** at the end of 2021. For 2025 and 2026 the rules in this reference apply: $2,200 per child, $1,700 refundable cap, MAGI phase-out starting at $200K/$400K.

If the user has a 2021 amended return question, this skill does NOT apply — refer to the 2021 instructions.

---

## Validation table (for cross-checking the worksheet)

| Field | Formula | Example |
|-------|---------|---------|
| Line 5 | N_CTC × $2,200 | 2 children × $2,200 = $4,400 |
| Line 7 | N_ODC × $500 | 1 ODC × $500 = $500 |
| Line 8 | line 5 + line 7 | $4,400 + $500 = $4,900 |
| Line 9 (single/HoH/MFS/QSS) | $200,000 | — |
| Line 9 (MFJ) | $400,000 | — |
| Line 10 | ceiling((line 3 − line 9) / 1,000) × 1,000 | $410,500 MFJ → $11,000 (rounded up from $10,500) |
| Line 11 | line 10 × 0.05 | $11,000 × 0.05 = $550 |
| Line 12 | line 8 − line 11 (stop if ≤ 0) | $4,900 − $550 = $4,350 |
| Line 14 | min(line 12, line 13) | min($4,350, $X) |
| Line 16a | line 12 − line 14 | $4,350 − $X |
| Line 16b | N_CTC × $1,700 | 2 × $1,700 = $3,400 |
| Line 19 | max(0, line 18a − $2,500) | $50,000 − $2,500 = $47,500 |
| Line 20 | line 19 × 15% | $47,500 × 15% = $7,125 |
| Line 27 (fewer than 3 children) | min(line 17, line 20) | min(min($4,350 − $X, $3,400), $7,125) |
