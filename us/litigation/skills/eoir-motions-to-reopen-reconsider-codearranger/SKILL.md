---
name: eoir-motions-to-reopen-reconsider-codearranger
title: EOIR — Motions to Reopen and Motions to Reconsider
description: 'Use this skill to assemble a motion to reopen or motion to reconsider a removal decision before EOIR (immigration judge or BIA), including in-absentia rescission and ineffective-assistance-of-counsel (Lozada) motions. Triggers: "motion to reopen", "motion to reconsider", "reopen my removal order", "in absentia order", "ordered removed in absentia", "missed my hearing", "didn''t get notice", "changed country conditions", "Lozada", "90 day motion to reopen", "new evidence in my case". Produces motion-to-reopen scaffold, motion- to-reconsider scaffold, in-absentia-rescission variant, Lozada checklist. Flags: **90-day and 30-day deadlines are short and often uncurable** (8 CFR § 1003.23 / § 1003.2). Composes with eoir-removal-defense, bia-appeals, immigration-deadlines, and immigration-fact-check.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/claude-legal-immigration-laws/skills/eoir-motions-to-reopen-reconsider
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# EOIR — Motions to Reopen and Motions to Reconsider

> **NOT LEGAL ADVICE.** Drafting aids and checklists only — not legal advice, no
> attorney-client relationship. **These deadlines are short, numerically limited, and often
> uncurable.** A missed or mis-filed motion is frequently the last chance to act, and the
> wrong forum (IJ vs. Board) defeats the filing outright. Verify the controlling 8 CFR
> provision, the current deadline, and your court's standing orders before filing, and
> strongly consider a licensed immigration attorney or EOIR-accredited representative.

## Two motions, two jobs — do not conflate them

A **motion to reconsider** says the prior decision *got the law or facts wrong on the record
that already existed.* A **motion to reopen** says *there are new facts or evidence the
adjudicator never saw.* They have different standards, deadlines, and limits.

| | **Motion to RECONSIDER** | **Motion to REOPEN** |
|---|---|---|
| **Standard** | Specify the **errors of fact or law** in the prior decision, supported by **pertinent authority** | Present **new, material facts/evidence** that **was not available and could not have been discovered or presented** at the prior hearing; attach affidavits + the relief application |
| **Deadline** | **30 days** from the final administrative order | **90 days** from the final administrative order |
| **Limit** | One per proceeding | **One** per proceeding (numerically limited) |
| **Authority** | INA § 240(c)(6) / 8 U.S.C. § 1229a(c)(6); 8 CFR § 1003.23(b)(2) (IJ) / § 1003.2(b) (Board) | INA § 240(c)(7) / 8 U.S.C. § 1229a(c)(7); 8 CFR § 1003.23(b)(3) (IJ) / § 1003.2(c) (Board) |

A motion to reconsider **may not** seek reconsideration of an order denying a prior motion to
reconsider (8 CFR § 1003.23(b)(2)). New evidence belongs in a reopen motion, not a reconsider
motion. Run the clock through `immigration-deadlines` before drafting — the 30/90-day periods
run from the **final administrative order**, which can be the IJ's decision or the Board's.

## Where to file — IJ or Board

File where the body that **last had jurisdiction** rendered the decision under review:

- **Before the immigration judge — 8 CFR § 1003.23** — when the IJ entered the final order and
  no appeal was taken to the Board (or the appeal was withdrawn). File with the immigration
  court that has administrative control over the Record of Proceeding; serve the **ICE Office
  of the Principal Legal Advisor (OPLA)** for that location; include an EOIR-28 if represented.
- **Before the Board — 8 CFR § 1003.2** — when the Board issued the last decision (it decided
  an appeal, or summarily affirmed). A motion directed at a decision the Board reviewed goes to
  the Board, not back to the IJ.

If unsure which body holds jurisdiction, resolve it first — filing in the wrong forum wastes a
single-use motion. See `eoir-immigration-courts` for the jurisdictional map and `bia-appeals`
for Board mechanics.

## Exceptions that escape the time / number limits

The 30/90-day deadlines and the one-motion cap do **not** apply in these postures. Plead the
exception explicitly and cite it:

- **In-absentia removal orders (INA § 240(b)(5)(C); 8 CFR § 1003.23(b)(4)(ii)).** A removal
  order entered in absentia may be **rescinded** by a motion to reopen filed within **180 days**
  if the failure to appear was due to **"exceptional circumstances"** (§ 240(e)(1) — e.g.,
  serious illness, death of an immediate relative; "not less compelling circumstances"). There
  is **NO time limit** if the respondent **did not receive notice** under INA § 239(a)(1)/(2)
  or was **in Federal or State custody** and the failure to appear was through no fault of their
  own. Filing this motion **does** stay removal pending disposition (§ 1003.23(b)(4)(ii)).
- **Changed country conditions for asylum / withholding / CAT (INA § 240(c)(7)(C)(ii);
  8 CFR § 1003.23(b)(4)(i)).** No time or number limit where the motion seeks asylum,
  withholding, or CAT protection based on **changed conditions in the country of removal**, the
  evidence is **material**, and it could not have been discovered or presented before. (Note: a
  prior **frivolous-application** finding bars this route.)
- **Jointly filed motions (8 CFR § 1003.23(b)(4)(iv)).** Time/number limits do not apply to a
  motion agreed to by all parties and filed jointly (often used after DHS agreement).
- **Agency sua sponte authority (8 CFR § 1003.23(b)(1) / § 1003.2(a)).** The IJ or Board may
  reopen or reconsider **on its own motion at any time** — a request invoking this authority is
  discretionary and not a substitute for a timely motion, but it is the only path once the
  deadlines and exceptions are exhausted.

## Ineffective-assistance-of-counsel reopening — the Lozada checklist

A motion to reopen premised on **ineffective assistance of prior counsel** must satisfy the
threshold requirements of **Matter of Lozada** (verify the exact case name and citation via
`immigration-fact-check` before filing). Treat this as a gating checklist — incomplete
compliance is a common ground for denial:

- [ ] **Affidavit** from the respondent setting out the agreement with former counsel — what
      was retained for, what counsel was told, and what counsel did or failed to do.
- [ ] **Notice to former counsel** of the allegations, with a **chance to respond**, and the
      response (or a statement that none was received) attached.
- [ ] **Bar complaint** filed against former counsel with the appropriate disciplinary
      authority — or a reasoned explanation why no complaint was filed.
- [ ] Showing of **prejudice** — how the deficient performance affected the outcome.
- [ ] If filed after the 90-day reopen deadline, a basis for **equitable tolling** of the
      deadline (verify the controlling circuit's tolling standard via `immigration-fact-check`).

## Stays — filing a motion does NOT pause removal (mostly)

By regulation, the filing of a motion to reopen or reconsider **does not automatically stay
the execution of the removal decision** (8 CFR § 1003.23(b)(1)(v) / § 1003.2(f)). Removal
proceeds unless a stay is **specifically granted** by the IJ, the Board, or an authorized DHS
officer. **Exception:** the in-absentia rescission motion under § 1003.23(b)(4)(ii) **does**
stay removal pending disposition. In every other posture, request a stay expressly and, where
removal is imminent or a final order is under judicial review, route stay relief to
`circuit-petition-for-review` (a petition for review plus a motion for stay in the court of
appeals). A departure from the U.S. after filing is treated as **withdrawal** of the motion
(§ 1003.23(b)(1)).

## Artifacts this skill drafts

- A **motion-to-reopen scaffold** — caption + A-number, statement of jurisdiction and forum,
  the **new/previously-unavailable/material** facts with affidavits and the relief application,
  exception pled if applicable, certificate of service on OPLA, proposed order.
- A **motion-to-reconsider scaffold** — the enumerated **errors of fact or law** with pertinent
  authority keyed to the prior decision, 30-day timeliness statement, service, proposed order.
- An **in-absentia-rescission variant** — the § 240(b)(5)(C) / § 1003.23(b)(4)(ii) motion
  (exceptional circumstances within 180 days, **or** lack-of-notice / custody with no time
  limit), with the automatic-stay note.
- A **Lozada compliance checklist** for an ineffective-assistance reopening.

## Related authority

- **8 CFR § 1003.23** (reopening / reconsideration before the immigration court) and
  **§ 1003.2** (before the Board) —
  [`../../references/immigration-regulations/8CFR-1003-eoir-bia.md`](../../references/immigration-regulations/8CFR-1003-eoir-bia.md).
- **INA § 240** (removal proceedings — (b)(5)(C) in-absentia, (c)(6) reconsider, (c)(7) reopen) /
  **8 U.S.C. § 1229a** —
  [`../../references/immigration-statutes/INA-II-immigration.md`](../../references/immigration-statutes/INA-II-immigration.md),
  with the INA ↔ 8 U.S.C. crosswalk in
  [`../../references/immigration-statutes/README.md`](../../references/immigration-statutes/README.md).

## Composition

Pairs with `eoir-removal-defense` (the underlying proceeding and the relief application a
reopen motion carries) and `bia-appeals` (when the Board held last jurisdiction or to appeal a
denial). `immigration-deadlines` computes the 30 / 90 / 180-day clocks; `circuit-petition-for-
review` handles judicial review and stays of removal; `immigration-fact-check` verifies every
citation — especially the **Matter of Lozada** name and any equitable-tolling authority — before
filing.
