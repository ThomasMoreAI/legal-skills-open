---
name: tx-post-judgment-codearranger
title: Texas Post-Judgment Procedure
description: Use when navigating post-judgment procedure in a Texas civil case. Triggers include "Texas garnishment", "can they garnish my wages in Texas", "bank account garnishment Texas", "set aside Texas default judgment", "Craddock Texas default", "motion for new trial Texas Rule 329b", "Texas plenary power", "bill of review Texas", "abstract of judgment Texas", "turnover order Texas CPRC 31.002", "writ of execution Texas", "Texas homestead exemption", "Texas personal property exemption Chapter 42", "dormant judgment Texas". Covers post-judgment motions (TRCP 320–329b; the 30-day window and plenary power), restricted appeal / bill of review, abstracts of judgment and judgment liens, the CPRC § 31.002 turnover proceeding, writ of execution, the Texas exemption framework (Prop. Code Ch. 41 homestead and Ch. 42 personal property), the Texas prohibition on wage garnishment for ordinary consumer debt, judgment dormancy and revival (CPRC § 34.001), and setting aside a default under the Craddock
  standard.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tx-court-docs/skills/tx-post-judgment
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Texas Post-Judgment Procedure

> **NOT LEGAL ADVICE.** This skill addresses procedure once a Texas
> judgment has been entered. Verify every step — and every dollar
> figure, acreage, and day count — against current law before filing
> or responding.

Use this skill alongside `tx-statewide-format` when the case is **past
judgment** — whether you are attacking the judgment, defending against
collection, or collecting on it. Pull verbatim rule and statute text
from `../tx-law-references/references/`.

## Two paths after judgment

1. **Attack the judgment** — a motion for new trial or to modify,
   correct, or reform (TRCP 320–329b), a restricted appeal or bill of
   review (after plenary power lapses), or setting aside a default under
   the **Craddock** standard.
2. **Collect or resist collection** — abstract of judgment and judgment
   lien, **turnover order (CPRC § 31.002)**, writ of execution, and the
   exemptions (Prop. Code Ch. 41 / Ch. 42) that protect the debtor.

## Attacking the judgment

### Motion for new trial / to modify, correct, or reform — TRCP 320–329b

- **Motion for new trial — TRCP 320, 324.** Grounds include newly
  discovered evidence, a verdict against the great weight of the
  evidence, jury misconduct, and error. A motion for new trial is a
  prerequisite to complaining of certain matters on appeal (TRCP 324).
- **Motion to modify, correct, or reform the judgment — TRCP 329b(g).**
  Asks the trial court to change the judgment itself.

> ⚠ **Timing — 30 days from signing.** A motion for new trial or to
> modify, correct, or reform must be filed **within 30 days after the
> judgment is signed** (**TRCP 329b(a), (g)**). Calendar it the moment
> the judgment is signed — see `tx-deadlines`.

> **★ Plenary power — TRCP 329b(d).** The trial court keeps **plenary
> power** to vacate, modify, correct, or reform its judgment for **30
> days after signing**. A **timely** motion for new trial or to modify
> **extends** plenary power (up to the limits in TRCP 329b(e)–(g)). Once
> plenary power expires, the trial court generally **loses authority**
> to change the judgment — the remaining routes are appeal, restricted
> appeal, or a bill of review. Track this clock carefully.

### Setting aside a default — the Craddock standard

A defendant hit with a **no-answer or post-answer default** may move for
new trial to set it aside under **Craddock v. Sunshine Bus Lines, Inc.**,
133 S.W.2d 124 (Tex. 1939): the movant must show (1) the failure to
answer / appear was **not intentional or the result of conscious
indifference** but accident or mistake; (2) a **meritorious defense**;
and (3) that a new trial will **not cause delay or injury** to the
plaintiff. The motion is bound by the **30-day** TRCP 329b clock — file
within plenary power. Pair with the substantive defense (chain of
title, statute of limitations) — see `tx-consumer-debt` and
`tx-first-30-days`.

### After plenary power — restricted appeal and bill of review

- **Restricted appeal (Tex. R. App. P. 30).** Available to a party who
  did **not participate** in the hearing that led to the judgment and
  did not timely file a post-judgment motion or appeal — filed within
  **6 months** of the judgment, requiring error apparent on the face of
  the record. Confirm the current window and requirements against the
  corpus.
- **Bill of review.** An independent equitable suit to set aside a
  judgment no longer appealable, requiring a meritorious defense
  prevented by fraud, accident, or wrongful act unmixed with the
  movant's own negligence. A demanding remedy — confirm the elements
  and limitations period against current law.

### Findings of fact and conclusions of law — TRCP 296–299

After a bench trial, a party may **request findings of fact and
conclusions of law** under TRCP 296 within the rule's window; they
sharpen the record for appeal. Confirm the request and reminder
intervals in the corpus.

## Collecting / resisting collection

### Abstract of judgment and judgment liens

Recording an **abstract of judgment** with the county clerk creates a
**judgment lien on the debtor's non-exempt real property** in that
county (Tex. Prop. Code Ch. 52). **The lien does not attach to exempt
homestead property.** Confirm the abstract contents, recording
mechanics, and lien duration / renewal against the corpus.

### Writ of execution

A **writ of execution** (TRCP 621 et seq.) directs the constable or
sheriff to levy on and sell the debtor's **non-exempt** property to
satisfy the judgment. Execution may issue while the judgment remains
enforceable (not dormant — below).

### ★ Turnover proceeding — CPRC § 31.002

> **The turnover statute is the workhorse Texas post-judgment remedy.**
> Under **Tex. Civ. Prac. & Rem. Code § 31.002**, a judgment creditor
> may obtain a **turnover order** reaching non-exempt property that
> cannot readily be attached or levied on by ordinary process (e.g.,
> accounts receivable, business interests, rights to payment). The
> court may order the debtor to turn over property, appoint a receiver,
> and enjoin transfers. **A turnover order may not reach exempt
> property.** A debtor served with a turnover motion should assert
> applicable exemptions promptly. Confirm the current text and any fee
> provision against the corpus.

### ★ Wage garnishment is generally prohibited for consumer debt

> **★ A signature Texas debtor protection.** The Texas Constitution,
> **art. XVI, § 28**, prohibits garnishment of **current wages for
> personal service** except for court-ordered child support and spousal
> maintenance (and certain federal debts like taxes and student loans).
> **An ordinary consumer-debt or contract creditor generally CANNOT
> garnish a Texas debtor's wages.** This is a meaningful protection for
> a debtor.
>
> **But bank-account garnishment IS allowed.** Once wages are
> **deposited and are no longer "current wages,"** funds in a bank
> account can be reached by **garnishment** (TRCP 657–679; CPRC Ch. 63)
> or by a turnover order — subject to any exemption (e.g., federally
> protected Social Security under 42 U.S.C. § 407, certain retirement
> funds, and the Texas personal-property exemptions). Verify the
> current scope and procedure against the corpus.

### ★ Exemptions from execution — Prop. Code Ch. 41 and Ch. 42

A debtor protects property through Texas's **generous statutory
exemptions**:

- **Homestead — Tex. Prop. Code Ch. 41.** Texas's famously broad
  homestead exemption protects the homestead from forced sale for most
  debts **regardless of value** — it is **limited by acreage**, not by
  dollar value (urban vs. rural, single adult vs. family). **Do not
  rely on an acreage figure from memory** — look up the current
  urban/rural and single/family acreage caps in
  `../tx-law-references/references/` (Prop. Code §§ 41.001–41.002).
- **Personal property — Tex. Prop. Code Ch. 42.** Protects designated
  personal property up to an **aggregate fair-market-value cap** that
  differs for a **family** versus a **single adult**, plus categorically
  exempt items (certain home furnishings, tools of the trade, a motor
  vehicle, livestock, and prescribed benefits). **The aggregate cap
  drifts and is periodically adjusted — verify the current figures in
  the corpus** before asserting them.
- **Earnings** — current wages for personal service are exempt (art.
  XVI, § 28, above).
- **Categorically protected funds** — **Social Security** (42 U.S.C.
  § 407), certain public benefits, and qualified retirement accounts.

> ⚠ **Do not rely on an exemption dollar amount or acreage from
> memory.** The Ch. 41 acreage caps and the Ch. 42 aggregate cap are
> set and periodically adjusted by statute. **Look up the current
> figures in `../tx-law-references/references/` and verify** before
> asserting them.

To claim an exemption against a garnishment or levy, the debtor files a
written claim / response in the issuing court within the period the
garnishment or turnover papers specify; the court then resolves it.
Act promptly — see `tx-deadlines`.

### ★ Dormancy and revival of judgment — CPRC § 34.001

> **A Texas money judgment goes DORMANT if no writ of execution issues
> within the statutory period.** Under **Tex. Civ. Prac. & Rem. Code
> § 34.001**, a judgment becomes **dormant** (and execution may not
> issue on it) if a writ of execution is not issued within **10 years**
> after rendition (or within 10 years of the last writ). A dormant
> judgment may be **revived by scire facias or an action of debt**
> brought within the period set by **CPRC § 31.006** (confirm the
> current revival window against the corpus). A debtor facing
> collection on an **old** judgment should check whether the judgment
> went dormant and was never revived. See `tx-deadlines`.

### Post-judgment discovery / debtor's examination

To **locate assets**, the creditor may serve post-judgment discovery
(TRCP 621a) or seek the debtor's appearance to answer under oath about
income, property, and accounts; turnover proceedings (above) are
commonly paired with this. Failure to appear after proper service can
expose the debtor to **contempt**. Confirm the current procedure and
notice in the corpus.

### Satisfaction / release of judgment

When a judgment is paid in full, a **release of judgment** should be
filed and (where an abstract was recorded) recorded. If the creditor
refuses after payment, the debtor may move the court for an order; some
statutes impose a duty and penalty for failure to release after demand
— verify against the corpus.

## Common pro se scenarios

1. **Debt-buyer default judgment** — motion for new trial under the
   **Craddock** standard within the 30-day TRCP 329b window, plus a
   meritorious defense (chain of title, SOL). After plenary power,
   consider restricted appeal / bill of review. See `tx-consumer-debt`.
2. **Bank account holding wages or Social Security garnished** — assert
   that current wages are constitutionally exempt and that deposited
   Social Security is exempt under 42 U.S.C. § 407; file the exemption
   claim within the writ window.
3. **Creditor seeks a turnover order** — assert applicable Ch. 41 / Ch.
   42 exemptions; the order cannot reach exempt property.
4. **Old judgment surfaces** — check whether it went **dormant** (no
   writ within 10 years, CPRC § 34.001) and was never revived.
5. **Homestead threatened** — confirm the Ch. 41 acreage protection;
   the homestead is generally beyond forced sale for ordinary debts.

## Composition

- Format baseline: `tx-statewide-format`
- Drafting the motion / supporting affidavit or unsworn declaration:
  `tx-draft-motion`, `tx-draft-declaration`
- Noticing a post-judgment motion for hearing or submission:
  `tx-schedule-hearing`, `tx-hearings`
- Debt-buyer defenses: `tx-consumer-debt`; family-law enforcement:
  `tx-family-law`
- Deadline arithmetic (the TRCP 329b 30-day window, plenary power, the
  garnishment objection clock, the § 34.001 dormancy period):
  `tx-deadlines`
- Venue: `tx-hcdc`, `tx-dcdc`, `tx-county-courts`

## References

- `references/post-judgment-motions.md` — TRCP 320–329b, plenary power,
  restricted appeal / bill of review, and the Craddock test
- `references/turnover-and-execution.md` — CPRC § 31.002 turnover +
  writ of execution + bank-account garnishment (TRCP 657–679, CPRC
  Ch. 63)
- `references/judgment-liens.md` — abstract of judgment + Prop. Code
  Ch. 52 lien mechanics
- `references/exemptions.md` — Prop. Code Ch. 41 homestead (acreage)
  + Ch. 42 personal property (aggregate cap) — verify current figures
- `references/dormancy-and-revival.md` — CPRC § 34.001 dormancy +
  § 31.006 revival
