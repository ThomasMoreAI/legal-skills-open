---
name: tx-hearings-codearranger
title: Texas Hearings
description: Use when preparing for or conducting a hearing or submission in a Texas court (District Court, County Court at Law, or Justice Court). Triggers include "Texas motion hearing", "Notice of Hearing Texas", "decide my motion by submission Texas", "submission docket Texas", "do I need an oral hearing in Texas", "set a hearing in Texas", "Zoom hearing Texas", "remote hearing Texas", "telephonic hearing Texas", "courtroom etiquette Texas", "hearing-day checklist Texas", "21-day summary judgment notice Texas", "how do I argue a motion in Texas". Covers Texas motion practice and the choice between an oral hearing and decision "by submission," the Notice of Hearing / setting, remote (Zoom) appearance practice, the TRCP 166a 21-day summary-judgment notice pointer, courtroom etiquette, oral-argument structure, and the hearing-day packet.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tx-court-docs/skills/tx-hearings
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Texas Hearings

> **NOT LEGAL ADVICE.** Hearing-preparation aid only. Verify against
> the assigned court's procedures, the court's local rules, and the
> court's current remote-appearance instructions before any hearing.

Use this skill alongside `tx-statewide-format` and the specific venue
skill (`tx-hcdc`, `tx-dcdc`, `tx-county-courts`) when preparing for,
attending, or following up on a hearing. Pull verbatim rule text from
`../tx-law-references/references/court-rules/`.

## ★ Oral hearing vs. submission — a Texas signature

A defining feature of Texas motion practice: **many motions can be
decided "by submission" — on the papers, with no oral hearing.** Most
Texas trial courts run a **submission docket** alongside their oral
hearing docket. A movant sets a motion either:

- **For oral hearing** on a date coordinated with the court
  coordinator, or
- **By submission**, giving the opponent the local minimum notice
  (commonly stated as a number of days, e.g., a submission date some
  days out) to file a written response, after which the court rules on
  the briefing without argument.

> **Confirm the court's mechanics before you set anything.** Whether a
> given motion type requires oral argument, may be submitted, and what
> minimum notice each path needs is set by **local rules and the
> assigned court's procedures** — not by a single statewide number.
> Some motions (e.g., summary judgment) carry their own statutory
> notice (below). Check the venue skill and the court's local rules,
> and reserve the date / submission setting with the court coordinator
> first (see `tx-schedule-hearing`).

## The motion and Notice of Hearing — TRCP 21

A motion (other than one that may be heard ex parte) is filed and
served under **TRCP 21**, with at least the rule's minimum notice
before the hearing or submission, and served under **TRCP 21a**. The
scheduling document is a **Notice of Hearing** (or Notice of
Submission). Support a motion with the grounds stated with
particularity and any **affidavit or unsworn declaration** evidence
(`tx-draft-declaration`); a response and any reply follow. Confirm the
briefing intervals and any page limits in the corpus and the local
rules.

```
                       NOTICE OF HEARING

   TO: [Opposing party / counsel]

   PLEASE TAKE NOTICE that [Movant]'s [Motion to ___] is set for
   hearing before the [Court], [County] County, Texas, on [DATE] at
   [TIME] [or: is set for SUBMISSION on [DATE]], at the [County]
   Courthouse, [address] [or by the court's remote platform].

   [Signature block per tx-statewide-format]
```

## Summary judgment — the 21-day notice — TRCP 166a

> **Summary judgment runs on its own timeline.** Under **TRCP 166a**,
> the motion (whether traditional **166a(c)** or **no-evidence
> 166a(i)**) and its supporting proof must be **served at least 21 days
> before the time specified for the hearing or submission**, and the
> non-movant's response is generally due **not later than 7 days before**
> the hearing (except on leave of court). Calendar both with
> `tx-deadlines`; the substance of traditional vs. no-evidence summary
> judgment lives in `tx-draft-motion` and `tx-first-30-days`.

## Remote and telephonic appearances

Texas courts conduct many proceedings by **video (Zoom) or telephone**
at the court's discretion; remote appearances are widely available for
status conferences, oral argument on motions, and some evidentiary
hearings.

> Agent behavior: do **not** assume a platform or a meeting ID. Whether
> a hearing is in-person, video, or telephonic is set by the court's
> current practice and the assigned court. **Confirm the court's
> current remote-appearance practice** and pull the link / dial-in from
> the court's website or the most recent notice. Meeting IDs change —
> never cache or guess them.

If the hearing is remote, the general etiquette holds:

- Join **early** (10–15 minutes) using the court's published link /
  number.
- Use your **full legal name** as the display name.
- **Mute** on entry; unmute only when addressed.
- **Camera on** unless the court directs otherwise.
- **Quiet, professional background**; test audio and video first.

## In-person hearings — etiquette

- Arrive **early** (30 minutes) to clear security.
- **Dress** in business attire; self-represented filers should wear
  business-casual at minimum (no shorts, hats, or athletic wear).
- **Phones** silenced and put away.
- **Stand** when addressing the court ("May it please the Court, Your
  Honor").
- Address the judge as **"Your Honor"**; refer to the opposing party by
  **"Mr./Ms. [surname]"** from the podium.

## Hearing-day packet — what to bring

| Item | Purpose |
|---|---|
| 2 paper copies of each filing (court + opposing party) | Even in e-filed (eFileTexas) cases, have hard copies at the podium |
| Judge's courtesy copy (if local rule / procedures require one) | Some courts want a courtesy copy in advance |
| The relevant TRCP / Tex. R. Evid. excerpts (printed, tabbed) | Have the governing rule text at hand (see `tx-law-references`) |
| Key cases (printed; note the court-of-appeals district + petition history) | Flag the dispositive authorities |
| Witness outlines (if evidentiary) | One per witness; sequential exam outline |
| Exhibit list + copies | Original + court copy + opposing-party copy of each exhibit |
| Proposed order / form of judgment (1 copy + 1 spare) | The court may sign at the hearing; see `tx-submit-order` |
| Notepad + 2 pens | Notes during the hearing |

## Oral argument — structure

A workable structure for a Texas civil motion:

1. **Opening** (~30 sec). "May it please the Court, [Name] for the
   [Plaintiff / Defendant]. This is [Movant]'s Motion to [Dismiss /
   Compel / for Summary Judgment]. We respectfully ask the Court to
   [grant / deny] for [N] reasons."
2. **Roadmap** (~30 sec). "First... Second... Third..."
3. **Substantive argument** — lead with the strongest point; cite the
   governing TRCP, Tex. R. Evid., or case; tie back to the record.
4. **Address counter-arguments candidly** — answer the court's
   questions directly; do not duck weaknesses.
5. **Reserve rebuttal** if you are the movant.
6. **Closing** (~15 sec). "For these reasons, [Movant] respectfully
   asks the Court to [grant / deny]. Thank you, Your Honor."

## Evidentiary hearings — special considerations

For evidentiary hearings (temporary injunctions, contempt,
post-judgment debtor exams, disputed-fact motions):

- **Subpoena witnesses** in advance under TRCP 176.
- **Pre-mark exhibits** per the court's numbering convention.
- **Witness exclusion** — request under Tex. R. Evid. 614 if helpful.
- **Stipulations** — confer beforehand to stipulate to undisputed facts
  and to authentication of routine business records under Tex. R. Evid.
  803(6) / 902(10) (see `tx-law-references`).
- **Record** — confirm with the court reporter / clerk how the
  proceeding is recorded (and how the record is made for a remote
  hearing).

## Continuances

- **Confer with the opposing party first** — agreed or unopposed
  motions to continue are far more likely to be granted.
- File the motion **before** the setting, stating the current date, the
  reason, whether the opposing party agrees, and proposed new dates.
  Many courts want a proposed order.

## Composition

- For format: `tx-statewide-format`
- For courthouse logistics (location, security, court coordinator):
  `tx-hcdc`, `tx-dcdc`, `tx-county-courts`
- For reserving / noticing the hearing or submission:
  `tx-schedule-hearing`
- For drafting the motion and supporting papers: `tx-draft-motion`,
  `tx-draft-declaration`, `tx-draft-note`
- For the post-hearing order: `tx-submit-order`
- For deadline arithmetic (the local notice clock and the TRCP 166a
  21-day / 7-day summary-judgment windows): `tx-deadlines`
- For canonical TRCP / Tex. R. Evid. text and local rules:
  `tx-law-references`

## References

- `references/notice-of-hearing.md` — Notice of Hearing / Notice of
  Submission scaffold
- `references/hearing-day-checklist.md` — packet checklist
- `references/oral-argument-outline.md` — argument structure template
- `references/remote-appearance.md` — Zoom / telephonic etiquette
- `references/submission-vs-oral.md` — choosing the submission docket
  vs. an oral setting
