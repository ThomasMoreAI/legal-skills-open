---
name: deductions-and-credits-cure-consulting-group
title: Deductions, Credits & Exclusions
description: Qualifies deductions, credits, and exclusions against IRC tests. Use when asked whether something is deductible, which credits apply, or what a return is leaving unclaimed.
author: Cure-Consulting-Group
author_url: https://github.com/Cure-Consulting-Group/ProductEngineeringSkills/tree/main/skills/tax/deductions-and-credits
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: tax
language: en
---

# Deductions, Credits & Exclusions

The benefit catalog: what is claimable on a return given facts that already
exist (`tax-strategies` covers moves that need planning). **Done when** every
candidate benefit has the output row below, with its limit computed and its
verification flag shown.

## Disclaimer
This skill produces draft analysis and workpapers, not tax, legal, or accounting advice. Nothing it produces is filing-ready until a licensed CPA, enrolled agent, or tax attorney has reviewed it. Model output is not authority and does not establish reasonable cause (see `cpa-standards`).

## The three benefit types — never confuse them

| Type | Effect | Worth per \$1 at 24% |
|---|---|---|
| **Exclusion** | Never enters gross income (§61) | \$0.24 + keeps AGI down, which protects phase-outs |
| **Deduction** | Reduces taxable income | \$0.24 |
| **Credit** | Reduces tax dollar-for-dollar | \$1.00 |

A credit is worth roughly 4x a deduction at a 24% marginal rate, so screen
credits first: they are more valuable and more often missed.

Within deductions, the ranking is:
1. **Above-the-line** (§62 adjustments) — reduce AGI itself, so they also unlock
   AGI-sensitive benefits. Best.
2. **Business deductions** (§162, on Schedule C / 1120 / 1065) — reduce income
   *and* self-employment tax. Best of all for a sole proprietor.
3. **Schedule 1-A / OBBBA deductions** — available on top of standard or itemized.
4. **Itemized** (§63(d)) — only worth anything above the standard deduction.

## Workflow

1. **Establish the year and filing status.** Pull every limit from the project's
   `constants` binding, never from memory. If the project has no engine, take the
   figures from `irc-lookup` and cite the Rev. Proc. they come from.
2. **Classify every dollar of spend** as: business (§162), personal (§262),
   mixed (allocate), or capital (§263 — depreciate instead).
3. **Run the screens**: read `reference/credits-catalog.md` first, then
   `reference/deductions-catalog.md`. Both are ordered by how often an item is
   missed.
4. **Apply the limitation stack** in order — see below. Deductions die in this
   stack far more often than they fail the underlying test.
5. **Check substantiation** for each claimed item against
   `reference/substantiation-by-deduction.md` (read at this step). A deduction
   you cannot prove is lost, plus a §6662 penalty.
6. **Compare itemized vs standard**, including the OBBBA Schedule 1-A items that
   are additive to both.

## The limitation stack (order matters)

A business loss must survive all four gates, in this sequence:

```
§262/§263  Is it deductible at all, or personal/capital?
   ↓
§704(d)/§1366(d)  Basis — do you have enough to absorb it?
   ↓
§465  At-risk — is the money genuinely at risk?
   ↓
§469  Passive activity — do you materially participate?
   ↓
§461(l)  Excess business loss — is it over the annual cap?
   ↓
Deductible this year (excess carries forward as NOL under §172)
```

Additional gates that kill otherwise-valid deductions:
- **§183 hobby loss** — no profit motive, no deduction. *Screen any activity with
  consecutive loss years: it fails the 3-of-5 presumption.*
- **§280E** — trafficking in a Schedule I/II substance disallows everything but
  COGS. Since 2026-04-23, FDA-approved and state-licensed *medical* marijuana
  products are Schedule III and outside §280E (DOJ order; verified 2026-09-23,
  justice.gov). Adult-use marijuana stayed Schedule I pending a broader
  rescheduling hearing — confirm its status before use.
- **§274(d)** — no substantiation, no deduction, regardless of merit.
- **§267** — related-party payment not deductible until includible by the payee.

## Screening heuristics

Ask these, in this order, when hunting for missed benefit:

- **Is there a business?** If yes, a large class of otherwise-personal spend
  (phone, internet, home office, vehicle, education, travel, health insurance)
  becomes partially deductible.
- **Is there payroll?** Payroll unlocks §41(h) payroll offset, §45S, §45F, §51 (lapsed for post-2025 hires — confirm before use),
  retirement plan deductions, and the §199A W-2 wage limit. *A company with no
  payroll has zero wage QREs, which is the most common reason an R&D credit comes
  out a fraction of what the work was worth.*
- **Are there children, education, or dependents?** §24, §25A, §21, §129.
  (OBBBA raised §21 and §129 from 2026 — see `reference/credits-catalog.md`.)
- **Home energy or EV purchases?** §25C and §25D terminated after 2025-12-31;
  §30D/§25E/§45W ended for vehicles acquired after 2025-09-30. None is available
  for 2026 spending — only carryforwards from earlier years.
- **Is there equipment, software, or a vehicle?** §179, §168(k), §179A, §168(n).
- **Is there R&D or software development?** §174A + §41. Frequently missed by
  founders who think "we're not a lab."
- **Is there retirement capacity?** The largest single deduction available to a
  profitable owner-operator — see the `tax-strategies` skill (retirement-plan
  design) and `tax-recommendations` for sizing.
- **Is there health insurance?** §162(l) above-the-line, or an HRA/ICHRA.
- **Did anything get sold, lost, or abandoned?** §165, §1244, §1231.

## Output shape

For each benefit identified:

| Field | Content |
|---|---|
| Benefit | Name and IRC section |
| Test | The elements, as a checklist with pass/fail against actual facts |
| Amount | Computed, showing the limit calculation |
| Where | Form and line |
| Substantiation | What must exist in the file |
| Confidence | Per `irc-lookup` conventions: VERIFIED / CATALOG / RECALL |

Flag anything claimed on `RECALL` numbers before it reaches a return.

## Related skills

`irc-lookup` (verify any cite), `tax-strategies` (structural moves),
`audit-risk-substantiation` (defending what you claim),
`tax-recommendations` (ranking and presenting findings).
