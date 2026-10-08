# Credit Catalog

Ordered by how often they are missed in an owner-operator / startup context.
Dollar figures marked `[constants]` come from the `constants` binding.

## Business credits (§38 general business credit)

### §41 — Research credit  ★ the most commonly under-claimed credit for a software company
- **Test**: qualified research must satisfy the **four-part test** —
  (1) permitted purpose (new/improved function, performance, reliability, quality),
  (2) technological in nature (hard sciences, incl. computer science),
  (3) elimination of uncertainty, (4) process of experimentation.
- **QREs**: in-house wages for qualified services (§41(b)(2)), supplies, cloud
  computing/rental of computer time, and **contract research at 65%** (75% for
  qualified research consortia).
- **Two computation methods**:
  - Regular: 20% of QREs over a base amount.
  - **Alternative Simplified Credit (ASC)**: 14% of QREs over 50% of the prior
    three years' average QREs. If no QREs in any of the prior 3 years, **6% of
    current-year QREs**. Use ASC — the regular method's base-period computation
    is impractical for a young company.
- **§280C(c) election**: reduce the credit by 21% (the corporate rate) to keep
  the full §174A deduction, or take the full credit and reduce the deduction.
  Election made on a timely-filed return.
- **§41(h) payroll offset — critical for pre-revenue companies**: a qualified
  small business (gross receipts < $5M in the credit year, and **no gross
  receipts before the 5-tax-year period ending with the credit year**) may elect
  to apply up to **$500,000** of credit against the **employer share of Social
  Security tax, then Medicare tax** (§3111(f); for tax years beginning after 2022 the first $250,000 offsets Social Security and the rest Medicare), claimed on Form 8974 with Form 941. This turns a
  useless credit carryforward into cash for a company with no income tax
  liability.
- **Forms**: Form 6765. Payroll election requires the election *on the timely
  filed original return* — cannot be made on an amended return.
- **The structural trap**: a company claiming this credit with **zero wage QREs**
  under-claims it by construction. Development labor performed by an owner is a
  QRE only to the extent it is **compensated as wages**. No payroll → no wage QREs
  → the credit collapses to supplies and 65% of contractor spend. Fixing it
  requires reasonable owner compensation on a W-2 first, justified on its own
  terms — not manufactured to produce a credit. See `tax-strategies` →
  `reference/entity-playbook.md`.

### §45S — Paid family and medical leave credit
- 12.5%–25% of wages paid during leave, scaling with the replacement rate.
- Requires a **written policy** meeting §45S(c) before the leave is taken.
- Made permanent by OBBBA.

### §45F — Employer-provided child care
- Percentage of qualified child care facility and resource/referral expenditures.
  From 2026 the annual cap is $500,000 ($600,000 for an eligible small business),
  indexed after 2026 (verified 2026-09-23, Rev. Proc. 2025-32 §2.06); confirm the
  new credit rates before use.
- 10-year recapture if the facility ceases to operate as such.

### §51 — Work opportunity credit
- 25–40% of first-year wages for hires from targeted groups (veterans, long-term
  unemployed, SNAP recipients, ex-felons, designated community residents).
- **Hard deadline**: Form 8850 must be filed with the state workforce agency
  **within 28 days of the employee's start date**. Miss it and the credit is gone.
- **Status — confirm before use.** §51 authorization ended for individuals who
  begin work after **2025-12-31** (CRS R43729, May 2026) and no extension had
  been enacted as of 2026-09-23. Do not count WOTC for a 2026 hire unless an
  extension has been enacted. Filing Form 8850 within 28 days still preserves the
  claim if Congress extends retroactively.

### §44 — Disabled access credit
- 50% of eligible access expenditures between $250 and $10,250 → max $5,000.
- Eligible small business: ≤ $1M gross receipts or ≤ 30 full-time employees.
- Pairs with the §190 deduction for barrier removal.

### §38 / §39 — Ordering and carryover
- Credits combine into the general business credit, limited to net income tax
  minus the greater of tentative minimum tax or 25% of regular tax over $25,000.
- **Carryback 1 year, carryforward 20 years.** Unused credits are not lost, but
  they are dead money — prefer the §41(h) payroll election when eligible.

## Individual credits

### §24 — Child tax credit
- `[constants]` 2026: $2,200 per qualifying child, $1,700 refundable (verified
  2026-09-23, Rev. Proc. 2025-32 §4.05).
- Phase-out $50 per $1,000 of MAGI over $200,000 / $400,000 MFJ.
- Child must be under 17 at year end and have an **SSN valid for employment**.
- $500 nonrefundable credit for other dependents (§24(h)(4)).

### §25A — Education credits
- **AOTC**: 100% of first $2,000 + 25% of next $2,000 = **$2,500 max**, per
  student, first 4 years of postsecondary, at least half-time, no felony drug
  conviction. **40% refundable** (up to $1,000).
- **Lifetime Learning**: 20% of up to $10,000 = **$2,000 max**, per return,
  unlimited years, non-refundable, covers job-skill courses.
- Cannot claim both for the same student in the same year.
- Requires Form 1098-T. Phase-out $80k–$90k MAGI ($160k–$180k MFJ), statutory and
  not indexed since 2021 — confirm before use.

### §21 — Child and dependent care credit
- Expense base $3,000 (one qualifying person) / $6,000 (two or more).
- Rate: 20–35% through 2025. **From 2026 (OBBBA): 50%**, less 1 point per $2,000
  of AGI over $15,000 (floor 35%), then less 1 point per $2,000 ($4,000 MFJ)
  over $75,000 ($150,000 MFJ), floor 20%. Statutory, not indexed (verified
  2026-09-23, 26 U.S.C. §21(a)(2)).
- Requires **earned income by both spouses** (or student/disabled status).
- Provider TIN required on Form 2441 — a common failure point.
- Coordinates with §129 dependent care FSA (same $ can't be used twice). The §129
  exclusion rises from $5,000 to **$7,500** ($3,750 MFS) for 2026+, not indexed
  (verified 2026-09-23, IRS OBBB family-provisions guidance).

### §25D — Residential clean energy — TERMINATED after 2025
- **Not available for expenditures made after 2025-12-31** (OBBBA; verified
  2026-09-23, IRS FAQs on OBBB modification of §§25C/25D and Form 5695
  instructions). Relevant only to a 2025-or-earlier return or to a §25D
  carryforward from a prior year.
- Historic rule: 30% of solar, solar water heating, fuel cell, wind, geothermal,
  and battery storage ≥3 kWh; personal residence only; nonrefundable, carries
  forward.

### §25C — Energy efficient home improvement — TERMINATED after 2025
- **Not available for property placed in service after 2025-12-31** (OBBBA; same
  sources). Historic rule: 30% up to $3,200/yr for heat pumps, insulation,
  windows, doors. Do not present it for a 2026 return.

### §30D / §25E / §45W — Clean vehicle credits
- Up to $7,500 new (§30D), $4,000 used (§25E), commercial (§45W).
- Subject to MSRP caps, income caps, North American final assembly, and critical
  mineral / battery component sourcing.
- **TERMINATED for vehicles acquired after 2025-09-30** (OBBBA). "Acquired" = a
  binding written contract plus a payment (including a nominal downpayment or
  trade-in) on or before that date; such a vehicle may still qualify when placed
  in service later (verified 2026-09-23, IRS FAQs on OBBB modification of §§25E,
  30D, 45W). Not available for a 2026 purchase.

### §32 — Earned income credit
- `[constants]` phase-out tables by dependent count.
- **Investment income limit** disqualifies at a low threshold — screen this first
  for anyone with a brokerage account.
- Due-diligence requirements under §6695(g) apply to the preparer: Form 8867,
  $665 per failure for returns filed in 2027 (verified 2026-09-23, Rev. Proc.
  2025-32 §4.54).

### §901 — Foreign tax credit
- Relevant if any app revenue has foreign withholding (App Store / Stripe payouts
  from non-US jurisdictions).
- Form 1116; de minimis exception under $300/$600 MFJ allows claiming without the
  form.

## Screening checklist

```
[ ] Any wages paid?              → §41(h), §45S, §45F, §51 (lapsed for post-2025 hires — confirm)
[ ] Any R&D or software dev?     → §41 (+ §174A deduction)
[ ] Children under 17?           → §24
[ ] Anyone in school?            → §25A
[ ] Paid for child care?         → §21, §129
[ ] Solar / battery / EV?        → §25C/§25D ended 2025-12-31; §30D/§25E/§45W ended
                                   for vehicles acquired after 2025-09-30 — prior-year
                                   carryforwards only
[ ] Foreign tax withheld?        → §901
[ ] Accessibility improvements?  → §44 + §190
[ ] Unused credits from prior yr?→ §39 carryforward — check the schedule
```
