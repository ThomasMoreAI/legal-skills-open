---
name: immigration-deadlines-codearranger
title: Immigration — Deadline Catalog & Computation
description: 'Use this skill to identify, catalog, and compute the controlling deadline in any U.S. immigration matter; produce a deadline-triage worksheet before filing. The immigration analog of state *-deadlines skills. Triggers: "what''s my deadline", "how long do I have to appeal", "30 days to appeal", "BIA appeal deadline", "EOIR-26 deadline", "petition for review deadline", "motion to reopen deadline", "90 days to reopen", "motion to reconsider", "in absentia order deadline", "1-year asylum deadline", "voluntary departure period", "RFE due date", "NOID response time", "continuous physical presence", "10 years cancellation", "is my deadline jurisdictional", "can I still file". Warns: **immigration has NO universal mailbox rule; each forum sets its own receipt/filing rules**. Many deadlines are **jurisdictional and uncurable**. Produces deadline-triage worksheet with authority and flag for each clock.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/claude-legal-immigration-laws/skills/immigration-deadlines
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Immigration — Deadline Catalog & Computation

> **NOT LEGAL ADVICE.** This skill produces a deadline-triage worksheet and computation
> notes — **not legal advice**, and no attorney-client relationship is created. Immigration
> deadlines are short, vary by forum, and are frequently **jurisdictional and uncurable**:
> a missed BIA-appeal or petition-for-review deadline usually cannot be fixed by any later
> motion. Verify every date, form edition, and citation against current law and the actual
> notice in hand, and **strongly consider consulting a licensed immigration attorney or an
> EOIR-accredited representative** before relying on any computed date.

## What this skill does

It maps a matter's posture to the clock(s) that control it, ties each clock to its statutory
or regulatory authority, and computes candidate dates. Run it immediately after
`immigration-pro-se` identifies the forum — the deadline often decides which downstream skill
even matters. Cite from the **INA → 8 U.S.C. crosswalk** in
[`../../references/immigration-statutes/`](../../references/immigration-statutes/), not from memory.

## Deadline catalog

| Clock | Length | Authority | Notes |
|---|---|---|---|
| **Asylum one-year filing bar** | 1 year from arrival | INA § 208(a)(2)(B) / 8 U.S.C. § 1158 | Exceptions for **changed circumstances** materially affecting eligibility or **extraordinary circumstances** explaining the delay (§ 1158(a)(2)(D)). |
| **Appeal IJ → BIA** | **30 days** from the IJ decision | 8 CFR § 1003.38 (filing) / § 1003.3 | Form **EOIR-26**, received (not mailed) at the Board. **Not extendable.** |
| **Petition for review → U.S. Court of Appeals** | **30 days** from the final order of removal | INA § 242(b)(1) / 8 U.S.C. § 1252 | **Jurisdictional; no tolling, no extension.** Filed in the circuit where the IJ completed proceedings. |
| **Motion to reopen** | **90 days** from the final administrative decision | 8 CFR § 1003.23(b) (before IJ) / § 1003.2(c) (before BIA) | Generally **one** motion; number/time limits. Exceptions below. |
| **Motion to reconsider** | **30 days** from the final administrative decision | 8 CFR § 1003.23(b) (before IJ) / § 1003.2(b) (before BIA) | Generally **one** motion; states an error of law or fact in the prior decision. |
| **Reopen in-absentia (exceptional circumstances)** | **180 days** from the in-absentia order | INA § 240(b)(5)(C) / 8 U.S.C. § 1229a | Time-limited motion to reopen the in-absentia removal order. |
| **Reopen in-absentia (lack of notice)** | **No time limit** | INA § 240(b)(5)(C) / 8 U.S.C. § 1229a | Filed "at any time" if the NTA / hearing notice was not received. |
| **Reopen — changed country conditions (asylum)** | **No time / number limit** | 8 CFR § 1003.23(b)(4) / § 1003.2(c)(3) | Materially changed conditions in the country of removal; evidence must be previously unavailable. |
| **Voluntary departure — post-conclusion** | up to **60 days** | INA § 240B(b) / 8 U.S.C. § 1229c | Granted at the conclusion of proceedings; bond required. |
| **Voluntary departure — pre-conclusion** | up to **120 days** | INA § 240B(a) / 8 U.S.C. § 1229c | Granted before/at master calendar, before merits. |
| **NTA → first hearing** | **at least 10 days** notice | INA § 239 / 8 U.S.C. § 1229 | Minimum time between NTA service and the first removal hearing (waivable by the respondent). |
| **Cancellation — continuous presence** | **10 years** (non-LPR) / **7 years** continuous residence + **5 years** LPR | INA § 240A / 8 U.S.C. § 1229b | Subject to the **stop-time rule**: presence ends at NTA service or certain offenses (§ 1229b(d)). |
| **USCIS RFE response** | set on the notice (commonly up to **~87 days**) | 8 CFR § 103.2(b)(8) | **Read the notice** — the date printed there controls, not this estimate. |
| **USCIS NOID response** | set on the notice (commonly **~33 days**) | 8 CFR § 103.2(b)(8) | **Read the notice** — the printed date controls. |
| **Naturalization — continuous residence / physical presence** | **5 yr** residence + **30 mo** physical presence (3 yr / 18 mo for § 319 spouses) | INA §§ 316 / 319 — 8 U.S.C. §§ 1427 / 1430 | Continuous-residence and physical-presence are distinct tests; long absences may break continuity. |

## How to compute (read this before computing anything)

- **There is NO universal mailbox rule in immigration.** Do not assume a filing is "timely if
  mailed." **Each forum sets its own receipt/filing rules:** the BIA and immigration courts
  generally count the day the filing is **received** (8 CFR § 1003.38 / § 1003.3); a circuit
  petition for review must be **filed** with the court within 30 days; USCIS counts receipt of
  the response. Confirm the rule for the specific forum before you compute.
- **Jurisdictional vs. curable.** Treat the **petition-for-review** (INA § 242(b)(1)) and the
  **30-day BIA appeal** (8 CFR § 1003.38) as hard, uncurable deadlines — there is no tolling and
  no "good cause" extension. Statutory filing bars (the asylum one-year bar) have narrow,
  enumerated exceptions only. Flag any near-miss loudly in the worksheet.
- **Anchor to the right trigger date.** Identify what starts the clock — date of the IJ oral
  decision, date the written decision was served, date of the final order, date the notice was
  *issued* vs. *received*. The trigger, not "today," controls.
- **Count carefully and conservatively.** When a forum's day-counting rule is unclear, compute
  the **earliest** plausible due date and treat it as the deadline. Never round in the filer's
  favor on a jurisdictional clock.
- **Always reconcile against the actual notice.** RFE/NOID windows, hearing dates, and voluntary-
  departure periods are stated on the paper the person holds; the catalog above gives only typical
  ranges. The notice wins.

## Artifacts this skill drafts

- A **deadline-triage worksheet**: each applicable clock, its trigger date, its authority, the
  computed due date, and a **jurisdictional / curable** flag.
- A **forum-rule note** stating how the controlling forum counts time (receipt vs. filing; no
  mailbox rule) for the specific filing contemplated.
- A **near-miss alert** when any computed date is within a short window or already passed,
  routing to the appropriate motion or review skill.

## Related authority

- Asylum one-year bar + exceptions: INA § 208(a)(2) / 8 U.S.C. § 1158; removal proceedings and
  in-absentia reopening: INA § 240 / 8 U.S.C. § 1229a; voluntary departure: INA § 240B /
  8 U.S.C. § 1229c; cancellation + stop-time: INA § 240A / 8 U.S.C. § 1229b; judicial review:
  INA § 242 / 8 U.S.C. § 1252 — all in
  [`../../references/immigration-statutes/INA-II-immigration.md`](../../references/immigration-statutes/INA-II-immigration.md),
  with the INA ↔ 8 U.S.C. crosswalk in
  [`../../references/immigration-statutes/`](../../references/immigration-statutes/) (README).
- Naturalization residence / physical-presence: INA §§ 316 / 319 / 8 U.S.C. §§ 1427 / 1430 —
  [`../../references/immigration-statutes/INA-III-nationality.md`](../../references/immigration-statutes/INA-III-nationality.md).
- BIA appeals (§ 1003.38), reopening/reconsideration before the BIA (§ 1003.2) and before the
  immigration court (§ 1003.23) —
  [`../../references/immigration-regulations/8CFR-1003-eoir-bia.md`](../../references/immigration-regulations/8CFR-1003-eoir-bia.md).
- USCIS RFE/NOID windows (§ 103.2(b)(8)) —
  [`../../references/immigration-regulations/8CFR-103-powers-fees.md`](../../references/immigration-regulations/8CFR-103-powers-fees.md).

## Composition

Runs right after `immigration-pro-se` and feeds every drafting skill. Hands off to
`eoir-removal-defense` (hearing and relief deadlines, voluntary departure),
`bia-appeals` (the 30-day EOIR-26 clock), `circuit-petition-for-review` (the jurisdictional
30-day § 1252(b)(1) clock), and `eoir-motions-to-reopen-reconsider` (the 90-/30-day motion clocks
and the in-absentia and changed-country-conditions exceptions). Verify any computed date with
`immigration-fact-check` before filing.
