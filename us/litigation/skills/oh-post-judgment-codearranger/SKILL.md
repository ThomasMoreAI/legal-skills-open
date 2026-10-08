---
name: oh-post-judgment-codearranger
title: Ohio Post-Judgment Procedure
description: Use for Ohio post-judgment procedure — motion to vacate, motion for new trial, judgment enforcement, garnishment, debtor's exam, exemptions, satisfaction of judgment. Triggers include 'Ohio motion to vacate Civ. R. 60', 'Ohio motion for new trial Civ. R. 59', 'Ohio garnishment', 'Ohio debtor's exam', 'R.C. 2329 exemptions', 'Ohio judgment renewal R.C. 2329.07', 'Ohio satisfaction of judgment'. Covers Civ. R. 59/60 motions, R.C. Chapter 2329 enforcement, R.C. 2329.66 exemptions schedule, R.C. Chapter 2333 supplemental proceedings, and the 5-year SOL on judgment enforcement at R.C. 2329.07.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/oh-court-docs/skills/oh-post-judgment
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Ohio Post-Judgment Procedure

> **NOT LEGAL ADVICE.** Post-judgment relief in Ohio is
> deadline-strict. Verify the specific clock that applies
> to your motion (Civ. R. 59 vs. 60(B); 28-day vs. 1-year).

## Motion to vacate / for new trial

### Civ. R. 60(B) — relief from judgment

Five grounds, with strict deadlines:

- **(1) Mistake, inadvertence, surprise, or excusable
  neglect** — must be filed within a **reasonable time but
  not more than 1 year** after the judgment
- **(2) Newly discovered evidence** — 1-year cap; must
  show evidence could not have been discovered earlier with
  due diligence
- **(3) Fraud, misrepresentation, or other misconduct of
  an adverse party** — 1-year cap
- **(4) The judgment is void** — reasonable-time only (no
  1-year cap); typically jurisdictional defects
- **(5) Any other reason justifying relief** — catch-all;
  reasonable-time only

### Civ. R. 59 — new trial

- **28 days** from entry of judgment under Civ. R. 59(B)
- Grounds at Civ. R. 59(A) include irregularity in
  proceedings, misconduct of jury, accident or surprise,
  excessive or inadequate damages, error of law, judgment
  not sustained by the weight of evidence

## Judgment enforcement — R.C. Chapter 2329

### Statute of limitations

- **R.C. 2329.07** — 5 years to enforce a money judgment
  (Ohio judgments dormant after 5 years unless renewed by
  motion). Compare to NY's 20-year SOL — Ohio's enforcement
  window is much shorter and requires active renewal.

### Common enforcement mechanisms

- **Execution on personal property** — Civ. R. 64 + R.C.
  2329.06 et seq.; writ of execution from court clerk;
  county sheriff serves
- **Garnishment of wages** — R.C. 2716.01 et seq.; 30-day
  notice + hearing right
- **Garnishment of bank accounts** — R.C. 2716.11 et seq.;
  affidavit of judgment-creditor + service on bank
- **Lien on real property** — recording the certificate of
  judgment in the county where the property is located
  (R.C. 2329.02)
- **Foreign-judgment registration** — R.C. 2329.022
  (Uniform Enforcement of Foreign Judgments Act)

## Exemptions — R.C. 2329.66

Ohio is a **debtor-protective** state with statutory
exemptions:

- **Homestead** — $182,625 (2024-25 figure; adjusts every
  3 years per R.C. 2329.66(B))
- **Motor vehicle** — $4,850 (2024-25)
- **Household goods + furnishings** — $725 per item up to
  $14,825 aggregate
- **Wages** — 75% of disposable earnings exempt under R.C.
  2329.66(A)(13)
- **Pension + retirement accounts** — exempt under R.C.
  2329.66(A)(10) (federal-law-protected: ERISA, IRA, 401(k))
- **Tools of trade** — $2,825
- **Wild-card exemption** — $1,475 in any property

Exemption amounts adjust every three years per R.C.
2329.66(B) — verify current figures.

## Debtor's examination (supplemental proceedings)

- **R.C. Chapter 2333** — debtor's examination procedure
- Judgment creditor moves for examination; debtor served
  and ordered to appear at the court for sworn testimony
  about assets
- Failure to appear can result in contempt + bench warrant

## Satisfaction of judgment

- **R.C. 2329.31** — satisfaction recorded with the court
  clerk after judgment paid
- Judgment creditor has 30 days to file satisfaction after
  payment; failure to file can trigger statutory damages
- Pro-se debtors who pay should demand a written
  satisfaction of judgment in writing as a condition of
  payment

## Composition with other oh- skills

- `oh-deadlines` — Civ. R. 59 (28 days) vs. Civ. R. 60
  (1 year vs. reasonable time); R.C. 2329.07 (5 years)
- `oh-draft-motion` — Civ. R. 60(B) motion to vacate
  scaffolder
- `oh-consumer-debt` — debt-collector enforcement defenses
- `oh-fact-check` — case-citation verification
