---
name: ga-state-court-codearranger
title: Georgia State Court — O.C.G.A. § 15-7-4
description: 'Use for any Georgia State Court matter — the county-level limited- jurisdiction trial court that is the principal forum for debt- collection and tort suits. State Court has concurrent civil jurisdiction with the Superior Court over civil actions of ANY amount (no dollar ceiling) plus misdemeanors and traffic, but NO equity, divorce, title to land, or felonies (those are Superior Court exclusive). Triggers: "answer a State Court complaint", "State Court of [county]", "sued in State Court Georgia", "where are debt suits filed in Georgia", "does my county have a State Court", "State Court vs Superior Court Georgia", "Civil Action File No.", "30 days to answer Georgia complaint", "default judgment Georgia State Court". CRITICAL QUIRK: the State/Superior split is by SUBJECT, not by dollar amount; not every county has a State Court (created by local act). Layers on top of `ga-statewide-format`.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ga-court-docs/skills/ga-state-court
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Georgia State Court — O.C.G.A. § 15-7-4

> **NOT LEGAL ADVICE.** These notes describe the venue's procedural
> mechanics as a drafting aid, not legal advice. Local rules and
> judge-specific standing orders change; verify with the clerk and the
> current Uniform State Court Rules before relying on anything here. A
> default judgment under O.C.G.A. § 9-11-55 has real, fast
> consequences — answer within the deadline and consider consulting a
> licensed Georgia attorney or a legal-aid clinic.

Use this skill in addition to `ga-statewide-format` when the matter is
in a Georgia **State Court** — the county-level trial court of
**limited jurisdiction** created county-by-county by local act of the
General Assembly. The State Court is the everyday civil forum for
money disputes: it is where most **consumer-debt collection** suits
and most **tort** (personal-injury) suits are filed.

## CRITICAL QUIRK: the State/Superior split is by SUBJECT, not dollar amount

This is the defining feature and the most common point of confusion.
The State Court's jurisdiction (**O.C.G.A. § 15-7-4**) is
**concurrent** with the Superior Court over civil actions **of any
amount** — there is **no dollar ceiling** in State Court. What the
State Court **cannot** hear is a list of **subject matters** reserved
exclusively to the **Superior Court** (Ga. Const. art. VI):

- **equity** (injunctions and other equitable relief);
- **divorce and domestic-relations** matters;
- **title to land**;
- **felonies**.

So a $5,000 case and a $5,000,000 case can both sit in State Court,
while a $500 equity or title-to-land claim cannot. Do **not** decide
the State-vs-Superior question by amount in controversy; decide it by
**subject**. A case mixing a money claim with an equitable or
title-to-land claim belongs in **Superior Court** — see
`ga-county-courts` for the per-county Superior/State routing and
transfer practice.

## CRITICAL QUIRK: not every county has a State Court

A State Court exists only where the General Assembly has created one by
**local act**. **Fewer than half of Georgia's 159 counties** have a
State Court; the large metro counties (including Fulton, Cobb, and
Gwinnett) do. **Before assuming State Court is the forum, confirm the
filing county actually has one.** If it does not, civil actions of any
amount that would otherwise go to State Court are filed in that
county's **Superior Court** instead. The per-county check lives in
`ga-county-courts`.

## What the State Court hears

- **Civil actions of any amount** (O.C.G.A. § 15-7-4) — concurrent
  with Superior Court, except the four superior-exclusive subjects
  above. This is where the consumer-debt bundle's suits typically
  land.
- **Misdemeanors and traffic** offenses.

It does **not** hear equity, divorce, title to land, or felonies.

## Rules that apply

State Court civil practice runs on the **Georgia Civil Practice Act**
(**O.C.G.A. Title 9, Chapter 11** — the "CPA") exactly as in Superior
Court, together with the **Uniform State Court Rules** (which parallel
the Uniform Superior Court Rules). There is no separate, simplified
procedure here — full CPA pleading, discovery, motion, and
summary-judgment practice applies. The pleading-format baseline is
**O.C.G.A. § 9-11-10** (caption, numbered paragraphs, separate
counts) — see `ga-statewide-format`.

## Commencement, the answer, and default

- **Commencement / service** — the plaintiff files a complaint and the
  clerk issues a summons; service follows **O.C.G.A. § 9-11-4**.
- **Answer deadline (O.C.G.A. § 9-11-12(a))** — the defendant's answer
  is generally due **within 30 days after service of the summons and
  complaint**. **Confirm the current § 9-11-12(a) period** and the
  service-method nuances before calendaring. Defenses under
  § 9-11-12(b) (including a 12(b)(6) motion) may be raised by motion.
  See `ga-first-30-days`.
- **Counterclaims (O.C.G.A. § 9-11-13)** — a counterclaim arising from
  the same transaction is **compulsory**; raise it with the answer.
- **Default judgment (O.C.G.A. § 9-11-55)** — if no answer is filed by
  the deadline, the case goes into default. A defendant may **open the
  default as a matter of right within 15 days** by answering and
  paying costs (subd. (a)), and afterward only on the (b) showing
  (providential cause / excusable neglect / a proper case, with the
  rule's conditions). **Verify the current § 9-11-55 windows** — act
  fast; the as-of-right window is short. See `ga-first-30-days`.

## Summary judgment and discovery

- **Summary judgment (O.C.G.A. § 9-11-56)** — the motion is served at
  least the rule's number of days before the hearing; under Georgia
  law a movant may prevail by pointing to the **absence of evidence**
  on an essential element (*Lau's Corp. v. Haskins*, 261 Ga. 491
  (1991)). Confirm the current § 9-11-56 timing.
- **Discovery** — full CPA discovery applies: interrogatories
  (O.C.G.A. § 9-11-33, with a cap on the number — verify the current
  § 9-11-33 limit), requests for production (§ 9-11-34), requests for
  admission (§ 9-11-36, deemed admitted if not timely answered), and
  depositions (§ 9-11-30). The discovery period is set by the Uniform
  State Court Rules. See `ga-discovery`.

## Caption — State Court variant

```
                  STATE COURT OF [COUNTY] COUNTY
                        STATE OF GEORGIA

[PLAINTIFF],                        )
                                    )
        Plaintiff,                  )   Civil Action File No. _________
                                    )
v.                                  )
                                    )
[DEFENDANT],                        )
                                    )
        Defendant.                  )

                  [DOCUMENT TITLE IN ALL CAPS]
```

The caption reads **"STATE COURT OF [COUNTY] COUNTY / STATE OF
GEORGIA"** and the case number is styled **"Civil Action File No.
____"**. See `ga-statewide-format` for the full pleading paper
(margins, line numbering, footer), the numbered-paragraph body
(O.C.G.A. § 9-11-10), the certificate of service, and the pro se
signature block.

**Agent behavior:** before drafting, confirm (1) the filing **county
actually has a State Court** (else route to Superior Court via
`ga-county-courts`), (2) that the claim is **not** equity / divorce /
title-to-land / felony (those are Superior-exclusive regardless of
amount), (3) the **30-day answer deadline (O.C.G.A. § 9-11-12(a))**
and the **§ 9-11-55** default/open-default windows, and (4) the
county's **e-filing platform** (PeachCourt vs. Odyssey eFileGA) and
local State Court rules — see `ga-county-courts`.

## Composition

- For statewide format and the Georgia caption: `ga-statewide-format`
- For the small-claims layer below State Court and de novo appeals up
  from it: `ga-magistrate`
- For per-county routing, Superior/State split, and e-filing platform:
  `ga-county-courts`
- For the answer, defenses, counterclaims, and default avoidance:
  `ga-first-30-days`
- For interrogatories, RFPs, RFAs, and the discovery period:
  `ga-discovery`
- For consumer-debt defenses (chain of title, account-stated, SOL):
  `ga-consumer-debt`
- For deadline computation and Georgia legal holidays: `ga-deadlines`
- For assembling and e-filing a packet: `ga-file-packet`
- For citation verification: `ga-fact-check`

## References

- `references/state-court-jurisdiction.md` — O.C.G.A. § 15-7-4 scope,
  the subject-matter (not dollar) split with Superior Court, and the
  local-act creation requirement
- `references/cpa-answer-default.md` — O.C.G.A. § 9-11-12 answer,
  § 9-11-13 counterclaims, § 9-11-55 default and opening default
- `references/state-court-caption.md` — the "STATE COURT OF [COUNTY]
  COUNTY / STATE OF GEORGIA" caption and "Civil Action File No."
  conventions
