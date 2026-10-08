---
name: id-post-judgment-codearranger
title: Idaho Post-Judgment Procedure
description: Use when navigating post-judgment procedure in an Idaho civil case. Triggers include "Idaho garnishment", "continuing wage garnishment Idaho", "set aside Idaho default judgment", "vacate Idaho judgment", "relief from judgment Idaho Rule 60(b)", "motion for new trial Idaho Rule 59", "alter or amend judgment Idaho", "motion for reconsideration Idaho Rule 11.2", "Idaho exemptions", "homestead exemption Idaho", "Idaho judgment lien renewal", "renew Idaho judgment", "writ of execution Idaho", "claim of exemption Idaho", "debtor exam Idaho", "satisfaction of judgment Idaho". Covers post-judgment motions (I.R.C.P. 59, 11.2, 60(b), 55), enforcement of money judgments (execution, continuing wage garnishment, judgment liens), the Idaho exemption framework, satisfaction of judgment, and the 11-year judgment SOL and renewal.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/id-court-docs/skills/id-post-judgment
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Execution And Liens
  path: references/execution-and-liens.md
- title: Exemptions
  path: references/exemptions.md
- title: Garnishment
  path: references/garnishment.md
- title: Post Judgment Motions
  path: references/post-judgment-motions.md
- title: Satisfaction Of Judgment
  path: references/satisfaction-of-judgment.md
---

# Idaho Post-Judgment Procedure

> **NOT LEGAL ADVICE.** This skill addresses procedure once an Idaho
> judgment has been entered. Verify every step — and every dollar figure
> and day count — against current law before filing or responding.

Use this skill alongside `id-statewide-format` when the case is **past
judgment** — whether you are attacking the judgment, defending against
collection, or collecting on it. Pull verbatim rule and statute text from
`../id-law-references/references/`.

## Two paths after judgment

1. **Attack the judgment** — a motion for new trial / to alter or amend
   (I.R.C.P. 59), a motion for reconsideration (I.R.C.P. 11.2), relief
   from judgment (I.R.C.P. 60(b)), or setting aside a default (I.R.C.P.
   55).
2. **Collect or resist collection** — writ of execution, **continuing
   wage garnishment** (Idaho Code Title 11, ch. 7), judgment liens and
   renewal (Idaho Code § 10-1111), exemptions (Idaho Code §§ 11-605,
   11-207, 55-1003), and satisfaction.

## Attacking the judgment

### New trial / alter or amend — I.R.C.P. 59

Move for a **new trial** under **I.R.C.P. 59(a)** (grounds include
irregularity in the proceedings, misconduct, excessive or insufficient
damages, a verdict against the weight of the evidence, newly discovered
evidence, and error of law). A motion to **alter or amend the judgment**
runs under **I.R.C.P. 59(e)**.

> ⚠ **Timing — 14 days.** A Rule 59 motion for new trial (Rule 59(b)) or
> to alter or amend (Rule 59(e)) must be filed **no later than 14 days
> after entry of judgment**, and the window is **not extendable**.
> Calendar it the moment judgment is entered — see `id-deadlines`.

### Reconsideration — I.R.C.P. 11.2

Idaho provides a distinct **motion for reconsideration** of a final
judgment under **I.R.C.P. 11.2**, which must be filed **within 14 days
after entry of the final judgment** (Rule 11.2(b)). A motion to
reconsider an interlocutory order may be made at any time before entry of
final judgment. Confirm the current intervals in the corpus.

### Relief from judgment — I.R.C.P. 60(b)

**I.R.C.P. 60(b)** grounds: (1) mistake, inadvertence, surprise, or
excusable neglect; (2) newly discovered evidence; (3) fraud,
misrepresentation, or misconduct of an opposing party; (4) the judgment
is **void**; (5) satisfied/released or no longer equitable to apply
prospectively; (6) any other reason justifying relief.

> **Timing.** A Rule 60(b) motion must be made within a **reasonable
> time**, and for grounds **(1)-(3)** no more than the rule's **outer
> limit** (a set number of months after entry — confirm the current
> figure under **I.R.C.P. 60(c)** in the corpus). A void-judgment attack
> under (b)(4) is not bound by the same fixed window.

### Setting aside a default — I.R.C.P. 55

**I.R.C.P. 55** governs **entry of default** and **default judgment**,
and setting them aside for **good cause** (Rule 55(c)). Setting aside a
default *judgment* is governed by **Rule 60(b)** and is a demanding
standard. A movant generally must show good cause and a **meritorious
defense**; a void-for-defective-service attack (Rule 60(b)(4)) does not
need the meritorious-defense showing. Pair with the substantive defense —
chain of title, statute of limitations — see `id-consumer-debt`.

### Costs and fees after judgment

- **Memorandum of costs — 14 days.** The prevailing party files a
  memorandum of costs within **14 days** after entry of judgment
  (**I.R.C.P. 54(d)**).
- **Attorney fees** are claimed under **Idaho Code § 12-120** (certain
  contract / commercial claims) or **§ 12-121** (frivolous actions), per
  the rule's procedure. Confirm the current procedure in the corpus.

## Collecting / resisting collection

### Writ of execution

A **writ of execution** directs the sheriff to levy on and sell the
debtor's **non-exempt** property to satisfy the judgment. The writ must
issue while the judgment remains enforceable — see the judgment SOL and
renewal below.

### Continuing wage garnishment — Idaho Code Title 11, ch. 7

Idaho provides a **continuing wage garnishment** that reaches successive
pay periods:

- The garnishment is **continuing** subject to the statutory cap under
  **Idaho Code § 11-712**, so a single garnishment can capture earnings
  over multiple pay periods.
- The sheriff's **returns** and the mechanics of service and accounting
  are governed by **Idaho Code § 11-705**.
- **Earnings exemption — § 11-207.** The amount subject to garnishment is
  limited to the **lesser of 25% of disposable weekly earnings or the
  amount by which disposable weekly earnings exceed 30 times the federal
  minimum wage** (Idaho Code § 11-207, tracking the federal CCPA floor,
  15 U.S.C. §§ 1671-1677). Confirm the current computation in the corpus.

### Judgment liens and renewal — Idaho Code § 10-1111

Recording a judgment with the county recorder creates a **judgment lien
on the debtor's real property** in that county. The lien has a statutory
life and must be **renewed** to remain effective — the renewal mechanism
is **Idaho Code § 10-1111**. Verify the current lien term and the renewal
requirements in the corpus.

> ⚠ **The judgment itself has an 11-year statute of limitations.** An
> action upon a judgment must be brought within **11 years** under
> **Idaho Code § 5-215**. A creditor must renew the judgment lien (§
> 10-1111) and bring any action on the judgment within that period; a
> debtor facing collection on an **old** judgment should check whether
> the lien lapsed or the 11-year period has run. See `id-deadlines`.

### Debtor's examination / supplemental proceedings

To **locate assets**, the creditor may compel the judgment debtor (or a
third party) to appear and answer under oath about income, property, and
accounts. Failure to appear after proper service can expose the debtor to
**contempt**. Confirm the current procedure and notice requirement in the
corpus.

### Exemptions from execution

A debtor may protect property through statutory **exemptions**:

- **Personal property** — **Idaho Code § 11-605** (household furnishings,
  clothing, tools of the trade, a motor-vehicle value, and prescribed
  benefits).
- **Homestead** in the residence — **Idaho Code § 55-1003**.
- **Earnings** — the § 11-207 garnishment limit (above).
- Categorically protected funds — **Social Security** (42 U.S.C. § 407),
  certain public benefits and retirement accounts.

> ⚠ **Do not rely on an exemption dollar amount from memory.** Idaho's
> homestead figure (§ 55-1003) and the § 11-605 personal-property amounts
> are set and periodically adjusted by statute. **Look up the current
> amounts in `../id-law-references/references/` and verify current
> figures** before asserting them.

To claim an exemption, the debtor files a written **claim of exemption**
with the issuing court within the period the garnishment or levy papers
specify; the court then resolves it. Act promptly — see `id-deadlines`.

### Satisfaction of judgment

When a judgment is paid in full, the **satisfaction** should be entered
of record. The creditor ordinarily files and (where a lien was recorded)
records a **satisfaction of judgment**; if the creditor refuses after
payment, the debtor may move the court to enter satisfaction with proof.
Verify any statutory duty or penalty for failure to acknowledge
satisfaction after demand in the corpus.

## Common pro se scenarios

1. **Debt-buyer default judgment** — Rule 60(b) motion to set aside on
   defective service / excusable neglect plus a meritorious defense
   (chain of title, SOL). See `id-consumer-debt`.
2. **Bank account holding Social Security garnished** — assert the 42
   U.S.C. § 407 exemption and any Idaho Code § 11-605 exemption; file the
   claim of exemption within the writ window.
3. **Continuing wage garnishment** — confirm withholding is within the §
   11-207 cap (lesser of 25% of disposable earnings or excess over 30×
   the federal minimum wage).
4. **Old judgment surfaces** — check whether the 11-year SOL (§ 5-215)
   has run and whether the judgment lien was renewed (§ 10-1111).
5. **Creditor demands a debtor exam** — appear and answer to avoid
   contempt.

## Composition

- Format baseline: `id-statewide-format`
- Drafting the motion / supporting affidavit or declaration:
  `id-draft-motion`, `id-draft-declaration`
- Noticing a post-judgment motion for hearing: `id-schedule-hearing`,
  `id-hearings`
- Debt-buyer defenses: `id-consumer-debt`
- Deadline arithmetic (the Rule 59 / 11.2 14-day windows, garnishment
  objection clock, 11-year judgment SOL): `id-deadlines`
- Venue: `id-ada`, `id-bonneville`, `id-county-courts`

## References

- `references/post-judgment-motions.md` — I.R.C.P. 59, 11.2, 60(b), 55
- `references/garnishment.md` — continuing wage garnishment (Idaho Code
  Title 11, ch. 7; §§ 11-712, 11-705) + the § 11-207 earnings exemption
- `references/execution-and-liens.md` — writ of execution + judgment
  liens and renewal (Idaho Code § 10-1111)
- `references/exemptions.md` — Idaho Code § 11-605 personal property +
  § 55-1003 homestead (verify current figures)
- `references/satisfaction-of-judgment.md` — entering satisfaction
