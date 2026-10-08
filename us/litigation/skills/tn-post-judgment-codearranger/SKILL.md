---
name: tn-post-judgment-codearranger
title: Tennessee Post-Judgment Procedure
description: Use when navigating post-judgment procedure in a Tennessee civil case. Triggers include "Tenn. R. Civ. P. 59", "motion to alter or amend Tennessee", "Rule 59.04", "Tenn. R. Civ. P. 60", "Rule 60.02", "set aside default judgment Tennessee", "vacate judgment Tennessee", "Tennessee garnishment", "wage garnishment exemption Tennessee", "claim of exemption", "Tennessee exemptions Title 26", "satisfaction of judgment Tennessee", "execution on a judgment", "appeal General Sessions to Circuit", "10 days to appeal Tennessee". Covers the Rule 59 post-trial motions (30-day non-extendable window) and Rule 60.02 relief from judgment, execution and garnishment with the exemption framework under Tenn. Code Ann. Title 26, satisfaction of judgment, and the 10-day de novo appeal from General Sessions to Circuit Court under Tenn. Code Ann. § 27-5-108.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tn-court-docs/skills/tn-post-judgment
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Tennessee Post-Judgment Procedure

> **NOT LEGAL ADVICE.** This skill addresses procedure once a
> Tennessee judgment has been entered. Verify every step — and every
> dollar figure and day count — against current law before filing or
> responding.

Use this skill alongside `tn-statewide-format` when the case is
**past judgment** — whether you are attacking the judgment, defending
against collection, or collecting on it.

## Two paths after judgment

1. **Attack the judgment** — Tenn. R. Civ. P. 59 post-trial motions,
   Tenn. R. Civ. P. 60.02 relief from judgment, or appeal (including
   the **10-day de novo appeal** from General Sessions to Circuit).
2. **Collect or resist collection** — execution and garnishment,
   exemptions under Tenn. Code Ann. Title 26, and satisfaction of
   judgment.

## Attacking the judgment

### Tenn. R. Civ. P. 59 — post-trial motions

Rule 59 motions (new trial, to alter or amend the judgment under
**59.04**, for additur/remittitur, etc.) must be filed within **30
days after entry** of the judgment.

> ⚠ **The 30-day Rule 59 window is NON-extendable.** Tenn. R. Civ. P.
> 6.02 cannot enlarge it. A **timely** Rule 59 motion **tolls** the
> time to file a notice of appeal; a late one does not. Calendar this
> deadline the moment judgment enters — see `tn-deadlines`.

### Tenn. R. Civ. P. 60.02 — relief from final judgment

When the Rule 59 window has closed, **Tenn. R. Civ. P. 60.02** is the
vehicle to seek relief from a final judgment. Grounds include:

- **60.02(1)** mistake, inadvertence, surprise, or excusable neglect
- **60.02(2)** newly discovered evidence
- **60.02(3)** fraud, misrepresentation, or other misconduct of an
  adverse party
- **60.02(4)** the judgment is **void**
- **60.02(5)** the judgment is satisfied / released, or it is no
  longer equitable that it have prospective application, or any other
  reason justifying relief

> **Timing.** A 60.02 motion must be made within a **reasonable
> time**, and for grounds **(1)** and **(2)** not more than **one year**
> after entry. Confirm the current rule and the case law on the
> reasonable-time standard.

- **Setting aside a default judgment** is the most common post-judgment
  use, especially in consumer debt-buyer cases where service was
  defective or the defendant did not receive notice. Tenn. R. Civ. P.
  55.02 incorporates the 60.02 standard for setting aside a default.
  Pair the motion with a showing of a **meritorious defense** (chain
  of title, statute of limitations, the Tenn. Code Ann. § 20-6-104
  debt-buyer documentation requirement — see `tn-consumer-debt`).

### Notice of appeal

A notice of appeal from a final Circuit / Chancery judgment to the
Court of Appeals is governed by the Tennessee Rules of Appellate
Procedure (Tenn. R. App. P.). The deadline runs from entry of the
final judgment, or from disposition of a timely Rule 59 motion.
**Verify the current appellate-rule deadline** and where to file
before relying on any number.

## Appeal from General Sessions — Tenn. Code Ann. § 27-5-108

A party dissatisfied with a **General Sessions** civil judgment may
appeal **de novo to Circuit Court within 10 days** of entry of the
judgment (Tenn. Code Ann. § 27-5-108). Key points:

- The appeal is a **trial de novo** — the Circuit Court hears the case
  anew under the full Tenn. R. Civ. P. (so formal discovery becomes
  available; see `tn-discovery`).
- The **10-day window is short** — calendar it immediately. See
  `tn-deadlines` and `tn-general-sessions`.
- In a **detainer (eviction)** appeal, a possession bond may be at
  issue under Tenn. Code Ann. § 29-18-130(b); case law has held a
  tenant's appeal is not automatically dismissed for failure to post a
  possessory bond — verify current authority. See `tn-landlord-tenant`.

## Collecting / resisting collection

### Execution and garnishment

A money judgment is enforced by **execution** and by **garnishment**
of wages or non-wage assets (bank accounts, etc.). Garnishment
procedure, the garnishee's duty to answer, and the service-on-the-debtor
requirements are statutory. **Verify the current garnishment procedure
and the wage-withholding formula** before relying on any figure — the
federal Consumer Credit Protection Act garnishment cap (15 U.S.C.
§§ 1671-1677) sets a floor of protection that applies in Tennessee.

### Exemptions — Tenn. Code Ann. Title 26

A judgment debtor may protect certain property from execution and
garnishment through statutory **exemptions** found generally in **Tenn.
Code Ann. Title 26** (with related provisions elsewhere in the Code and
in federal law). The framework includes:

- A **personal-property exemption** the debtor may claim.
- A **homestead exemption** in the debtor's residence.
- **Wage / earnings** protection (with the CCPA federal floor).
- Categorically protected funds (e.g., **Social Security** under 42
  U.S.C. § 407, and certain public benefits and retirement accounts).

> ⚠ **Do not rely on a specific exemption dollar amount from memory.**
> Tennessee's Title 26 exemption figures are set and periodically
> adjusted by statute. **Look up the current Tenn. Code Ann. Title 26
> amounts** for the homestead, personal-property, and wage exemptions
> before advising on or asserting them.

**Claiming an exemption** generally requires the debtor to file a
written claim with the issuing court within the period the garnishment
papers specify, after which the court resolves the claim. Confirm the
current procedure and the deadline for the venue, and act promptly —
the window is short.

### Satisfaction of judgment

When a judgment is paid in full, the **satisfaction** should be
entered of record so the judgment no longer encumbers the debtor.
- The judgment creditor ordinarily files a **Satisfaction of
  Judgment** with the clerk.
- If the creditor refuses after payment, the debtor may move the court
  to enter satisfaction with proof of payment.
- Verify any statutory penalty for a creditor's failure to enter
  satisfaction after demand.

## Common pro se post-judgment scenarios

1. **Default judgment in a debt-buyer case** — file a Tenn. R. Civ. P.
   60.02 (and 55.02) motion to set aside, asserting defective service
   or excusable neglect plus a meritorious defense (chain of title,
   SOL, the § 20-6-104 documentation requirement). See
   `tn-consumer-debt`.
2. **General Sessions judgment you want to challenge** — if within 10
   days, the de novo appeal to Circuit (§ 27-5-108) is usually the
   better route than a post-judgment motion in General Sessions.
3. **Bank account garnished that holds Social Security** — assert the
   42 U.S.C. § 407 exemption and any applicable Title 26 exemption;
   file the claim within the window stated on the garnishment papers.
4. **Wage garnishment** — confirm the withholding does not exceed the
   CCPA federal cap and check the current Title 26 wage exemption.

## Composition

- For statewide format: `tn-statewide-format`
- For drafting the motion to set aside / to alter or amend:
  `tn-draft-motion`
- For the supporting affidavit / declaration: `tn-draft-declaration`
- For debt-buyer-specific defenses and the § 20-6-104 documentation
  requirement: `tn-consumer-debt`
- For eviction / detainer appeals: `tn-landlord-tenant`,
  `tn-general-sessions`
- For deadline arithmetic (the 30-day Rule 59 and 10-day appeal
  windows): `tn-deadlines`

## References

- `references/rule-59-60.md` — Tenn. R. Civ. P. 59 and 60.02 with notes
- `references/general-sessions-appeal.md` — the 10-day de novo appeal
  under Tenn. Code Ann. § 27-5-108
- `references/garnishment.md` — execution and garnishment workflow
- `references/exemptions.md` — Tenn. Code Ann. Title 26 framework
  (verify current figures)
- `references/satisfaction-of-judgment.md` — entering satisfaction
