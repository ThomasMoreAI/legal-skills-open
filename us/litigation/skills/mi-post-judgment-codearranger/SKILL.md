---
name: mi-post-judgment-codearranger
title: Michigan Post-Judgment Procedure
description: Use when navigating post-judgment procedure in a Michigan civil case. Triggers include "Michigan garnishment", "writ of garnishment Michigan MCR 3.101", "periodic garnishment Michigan", "MC 12 MC 13", "set aside Michigan judgment MCR 2.612", "vacate Michigan judgment", "relief from judgment Michigan", "motion for reconsideration MCR 2.119(F)", "new trial JNOV Michigan MCR 2.610", "Michigan exemptions MCL 600.6023", "creditor exam Michigan", "judgment lien Michigan", "writ of execution Michigan MCR 3.106", "installment payment order Michigan", "satisfaction of judgment Michigan". Covers post-judgment motions, enforcement of money judgments (garnishment, execution, judgment liens, creditor's examination, installment orders), the MCL 600.6023 exemption framework, and satisfaction of judgment.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/mi-court-docs/skills/mi-post-judgment
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Michigan Post-Judgment Procedure

> **NOT LEGAL ADVICE.** This skill addresses procedure once a Michigan
> judgment has been entered. Verify every step — and every dollar
> figure and day count — against current law before filing or
> responding.

Use this skill alongside `mi-statewide-format` when the case is **past
judgment** — whether you are attacking the judgment, defending against
collection, or collecting on it.

## Two paths after judgment

1. **Attack the judgment** — post-trial motions (MCR 2.610-2.611),
   reconsideration (MCR 2.119(F)), or relief from judgment (MCR 2.612).
2. **Collect or resist collection** — garnishment (MCR 3.101),
   execution (MCR 3.106), judgment liens (MCL 600.2801 et seq.),
   creditor's examination (MCR 2.621), installment-payment orders (MCL
   600.6201 et seq.), exemptions (MCL 600.6023), and satisfaction.

## Attacking the judgment

### New trial / amend / JNOV — MCR 2.610-2.611

After trial, move for a **new trial** under **MCR 2.611** (grounds:
irregularity, jury misconduct, excessive/inadequate damages, verdict
against the great weight of the evidence, legal error). **JNOV** or a
motion to **amend the judgment** runs under **MCR 2.610**.

> ⚠ **Timing.** A motion for new trial or to amend the judgment is due
> **21 days after entry** (MCR 2.611(B) / MCR 2.610(A)). A motion for
> **reconsideration** under **MCR 2.119(F)** is also due within **21
> days** of entry of the order. Confirm the current day counts in the
> corpus; calendar them at entry — see `mi-deadlines`.

### Reconsideration — MCR 2.119(F)

The standard under **MCR 2.119(F)(3)** is demanding: show a **"palpable
error"** by which the court and parties were misled **and** that a
different disposition must result. A motion that merely re-presents the
same issues already ruled on will not be granted. Verify the rule text.

### Relief from judgment — MCR 2.612

**MCR 2.612** is Michigan's FRCP-60 analog. Grounds under **MCR
2.612(C)(1)**: (a) mistake, inadvertence, surprise, or excusable
neglect; (b) newly discovered evidence; (c) fraud, misrepresentation, or
other misconduct of an adverse party; (d) the judgment is **void**; (e)
satisfied/released or no longer equitable to apply prospectively; (f)
any other reason justifying relief.

> **Timing.** A 2.612 motion must be made within a **reasonable time**,
> and for grounds **(a)-(c)** **not more than one year** after entry
> (MCR 2.612(C)(2)). Confirm the reasonable-time case law.

- **Setting aside a default / default judgment** is the most common use,
  especially in consumer debt-buyer cases with defective service. **MCR
  2.603(D)** generally requires both **good cause** and a **verified
  statement of facts showing a meritorious defense** (a lack-of-
  jurisdiction / bad-service attack does not need the meritorious-defense
  showing). Pair with the
  substantive defense — chain of title, SOL — see `mi-consumer-debt`.

## Collecting / resisting collection

### Writ of garnishment — MCR 3.101 / MCL 600.4011 et seq.

A money judgment reaches funds held by a third party (garnishee) via a
**writ of garnishment** under **MCR 3.101** / **MCL 600.4011 et seq.**:

- **Periodic** garnishment reaches **wages** and other periodic
  payments — writ on form **MC 12**, garnishee answers on the **MC 13**
  disclosure.
- **Non-periodic** garnishment reaches a single obligation (**bank
  account**, tax refund).

> **Process.** Plaintiff files the writ; the clerk issues it; it is
> served on the garnishee with a copy to the defendant. The garnishee
> files the **MC 13 disclosure** within the rule's period; the defendant
> may file **objections** within the time on the writ. **Verify the
> current service mechanics, disclosure deadline, and objection window**
> in the corpus. The federal CCPA garnishment cap (15 U.S.C.
> §§ 1671-1677) sets a wage-protection floor in Michigan.

### Execution and judgment liens

- **Writ of execution — MCR 3.106 / MCL 600.6001 et seq.**: directs a
  court officer/sheriff to levy on and sell the debtor's **non-exempt**
  property to satisfy the judgment.
- **Judgment liens — MCL 600.2801 et seq.**: record a notice of
  judgment lien against the debtor's **real property** with the register
  of deeds. Note the statutory **homestead carve-out** and the lien
  **duration / renewal** rules — verify the current term in the corpus.

### Creditor's examination — MCR 2.621

To **locate assets**, **MCR 2.621** authorizes post-judgment discovery
and a **creditor's examination** compelling the debtor (or a third
party) to answer under oath about income, property, and accounts.
Failure to appear can expose the debtor to **contempt**.

### Installment-payment orders — MCL 600.6201 et seq.

The court may order the debtor to pay the judgment in **installments**
under **MCL 600.6201 et seq.** A compliant installment order can **bar
concurrent wage garnishment** — verify the current interplay in the
corpus.

### Exemptions from execution — MCL 600.6023

A debtor may protect property through statutory **exemptions**,
principally **MCL 600.6023** (plus related Code and federal provisions):

- **Personal-property** exemptions (household goods, tools of the trade,
  motor-vehicle value) under MCL 600.6023.
- A **homestead** exemption in the residence.
- **Head-of-household / wage** protection (with the CCPA federal floor).
- Categorically protected funds — **Social Security** (42 U.S.C. § 407),
  certain public benefits and retirement accounts.
- The **federal-vs-state exemption choice** where the matter touches
  bankruptcy; confirm the current rule.

> ⚠ **Do not rely on an exemption dollar amount from memory.** Michigan's
> MCL 600.6023 figures (and homestead/wage amounts) are set and
> periodically **adjusted / inflation-indexed by statute**. **Look up
> the current MCL 600.6023 amounts** before asserting them.

To claim an exemption, the debtor files the written **objection / claim
of exemption** with the issuing court within the period the garnishment
papers specify; the court then resolves it. Confirm the current
procedure and deadline — act promptly. See `mi-deadlines`.

### Satisfaction of judgment

When a judgment is paid in full, the **satisfaction** should be entered
of record. The creditor ordinarily files a **satisfaction of judgment**
and discharges any recorded judgment lien; if the creditor refuses after
payment, the debtor may move the court to enter satisfaction with proof.
Verify any statutory penalty for failure to enter satisfaction after
demand.

## Common pro se scenarios

1. **Debt-buyer default judgment** — MCR 2.612 (and MCR 2.603(D)) motion
   to set aside on defective service / excusable neglect plus a
   meritorious defense (chain of title, SOL). See `mi-consumer-debt`.
2. **Bank account holding Social Security garnished** — assert the 42
   U.S.C. § 407 exemption and any MCL 600.6023 exemption; file the
   objection within the writ's window.
3. **Wage garnishment** — confirm withholding is within the CCPA cap,
   check the current MCL 600.6023 / head-of-household protection, and
   consider an installment order (MCL 600.6201) to bar it.
4. **Creditor demands a debtor exam** — respond under MCR 2.621; appear
   and answer to avoid contempt.

## Composition

- Format baseline: `mi-statewide-format`
- Drafting the motion / supporting affidavit: `mi-draft-motion`,
  `mi-draft-declaration`
- Debt-buyer defenses: `mi-consumer-debt`
- Deadline arithmetic (21-day windows, garnishment objection clock):
  `mi-deadlines`
- Venue: `mi-wayne`, `mi-oakland`, `mi-district-courts`,
  `mi-circuit-courts`, `mi-circuit-courts`

## References

- `references/post-judgment-motions.md` — MCR 2.610-2.611, MCR 2.119(F),
  MCR 2.612
- `references/garnishment.md` — MCR 3.101 periodic + non-periodic (MC 12
  / MC 13)
- `references/execution-and-liens.md` — MCR 3.106 execution, MCL 600.2801
  judgment liens
- `references/exemptions.md` — MCL 600.6023 framework (verify figures)
- `references/satisfaction-of-judgment.md` — entering satisfaction
