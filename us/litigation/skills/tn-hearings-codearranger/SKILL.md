---
name: tn-hearings-codearranger
title: Tennessee Hearings
description: Use when preparing for or conducting a hearing in a Tennessee court (Circuit, Chancery, or General Sessions). Triggers include "Tennessee oral argument", "Tennessee motion hearing", "motion day Tennessee", "docket call Tennessee", "General Sessions court date", "remote hearing Tennessee", "Zoom hearing Tennessee court", "courtroom etiquette Tennessee", "hearing-day checklist Tennessee", "how do I argue a motion in Tennessee". Covers oral-argument preparation, motion-day and docket-call dynamics (especially the informal General Sessions setting), remote-appearance practice (which varies by court — defer to local rules and standing orders), courtroom etiquette before Tennessee judges, and the hearing-day packet.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tn-court-docs/skills/tn-hearings
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Tennessee Hearings

> **NOT LEGAL ADVICE.** Hearing-preparation aid only. Verify against
> the assigned judge's standing orders, the venue's local rules, and
> the court's current remote-appearance instructions before any
> hearing.

Use this skill alongside `tn-statewide-format` and the specific court
skill (`tn-davidson`, `tn-shelby`, `tn-knox`, `tn-hamilton`,
`tn-county-courts`, `tn-general-sessions`) when preparing for,
attending, or following up on a hearing.

## Hearing settings in Tennessee — the basics

Hearing mechanics differ sharply by court type:

| Court | Typical hearing posture |
|---|---|
| **Circuit / Chancery** | Motions set for a **motion docket** or by special setting; the court may rule on the briefs or hear oral argument. Evidentiary hearings and bench trials are scheduled settings. |
| **General Sessions** | **Informal**, high-volume **docket call** at the assigned court date; the warrant is set for a date and the parties appear; matters are often heard and decided the same day. Continuances are common. See `tn-general-sessions`. |

> **General Sessions is a court-date model, not a briefing model.**
> When served with a civil warrant, the most important step is to
> **appear on the date stated** (or arrange a continuance). There is
> no formal motion-briefing track and no formal discovery as of right.

## Motion-day / docket-call dynamics

- **Circuit / Chancery motion dockets** — many counties hear civil
  motions on a recurring **motion day**. Confirm whether the venue
  requires the motion to be **set / noticed** for a specific motion
  day, whether the judge wants **chambers copies** in advance, and
  whether oral argument is expected or the matter is decided on the
  papers. These are **local-rule and standing-order** questions —
  check tncourts.gov for the venue's local rules and the assigned
  judge's standing order. See `tn-schedule-hearing`.
- **General Sessions docket call** — expect a crowded courtroom and a
  roll call of cases. Be present and ready when your case is called;
  know whether you are seeking a continuance, announcing for trial, or
  resolving the matter.

## Remote appearances — varies by court

There is **no single statewide remote-appearance rule** in Tennessee.
Many courts conduct some hearings by **Zoom** or another platform, but
whether a given hearing is in-person, remote, or hybrid is set by the
**venue's local rule or the assigned judge's standing order**.

> Agent behavior: do **not** assume a platform or a meeting ID. Pull
> the assigned judge's current remote-appearance instructions from the
> venue's website or the most recent notice / standing order. Meeting
> IDs change — never cache or guess them.

If the hearing is remote, the general etiquette holds:

- Join **early** (10-15 minutes).
- Use your **full legal name** as the display name.
- **Mute** on entry; unmute only when addressed.
- **Camera on** unless the court orders otherwise.
- **Quiet, professional background**; test audio and video first.

## In-person hearings — etiquette

- Arrive **early** (30 minutes) to clear security.
- **Dress** in business attire; pro se filers should wear
  business-casual at minimum (no shorts, hats, or athletic wear).
- **Phones** silenced and put away.
- **Stand** when addressing the court ("May it please the Court, Your
  Honor").
- Address the judge as **"Your Honor"**; refer to opposing counsel and
  parties as **"Mr./Ms. [surname]"** — not first names — from the
  podium.

## Hearing-day packet — what to bring

| Item | Purpose |
|---|---|
| 2 paper copies of each filing (court + opposing party) | Even in e-filed cases, have hard copies at the podium |
| Chambers copy (if the judge's standing order requires one) | Delivered in advance for longer motions |
| The relevant rules / statutes (printed, tabbed) | Have Tenn. R. Civ. P. and Tenn. R. Evid. excerpts at hand |
| Key cases (printed; Bluebooked, with published/unpublished noted) | Flag the dispositive authorities |
| Witness outlines (if evidentiary) | One per witness; sequential exam outline |
| Exhibit list + copies | Original + court copy + opposing-party copy of each exhibit |
| Proposed order (1 copy + 1 spare) | The court may sign in chambers; see `tn-submit-order` |
| Notepad + 2 pens | Notes during the hearing |

## Oral argument — structure

A workable structure for a Tennessee civil motion:

1. **Opening** (~30 sec). "May it please the Court, [Name] for the
   [Plaintiff / Defendant / Petitioner / Respondent]. This is
   [Movant]'s Motion to [Dismiss / Compel / for Summary Judgment]. We
   respectfully ask the Court to [grant / deny] for [N] reasons."
2. **Roadmap** (~30 sec). "First... Second... Third..."
3. **Substantive argument** — lead with the strongest point; cite the
   governing Tenn. R. Civ. P., Tenn. R. Evid., or case; tie back to
   the record.
4. **Address counter-arguments candidly** — answer the court's
   questions directly; do not duck weaknesses.
5. **Reserve rebuttal** if you are the movant.
6. **Closing** (~15 sec). "For these reasons, [Movant] respectfully
   asks the Court to [grant / deny]. Thank you, Your Honor."

## Evidentiary hearings — special considerations

For evidentiary hearings (a Rule 56 motion with disputed material
facts, injunctions, contempt, post-judgment debtor exams):

- **Subpoena witnesses** well in advance under Tenn. R. Civ. P. 45.
- **Pre-mark exhibits** per the division's numbering convention.
- **Witness sequestration** — request under Tenn. R. Evid. 615 if
  helpful.
- **Stipulations** — confer beforehand to stipulate to undisputed
  facts and to authentication of routine business records under Tenn.
  R. Evid. 803(6) / 902 (see `tn-law-references`).
- **Record** — confirm with the clerk whether the proceeding is
  recorded by the court system or by an outside court reporter.

## Continuances

- **Confer with the opposing party first** — joint or unopposed
  motions to continue are far more likely to be granted.
- File the motion to continue **before** the setting, stating the
  current date, the reason, whether opposing party agrees, and
  proposed new dates. Many divisions want a proposed order.
- In **General Sessions**, a continuance is often requested by
  appearing on the court date and asking for a reset; follow the
  court's practice. See `tn-general-sessions`.

## Composition

- For format: `tn-statewide-format`
- For courthouse logistics (parking, security, division): `tn-davidson`,
  `tn-shelby`, `tn-knox`, `tn-hamilton`, `tn-county-courts`,
  `tn-general-sessions`
- For scheduling / noticing the hearing: `tn-schedule-hearing`
- For drafting the motion and supporting papers: `tn-draft-motion`,
  `tn-draft-declaration`
- For the post-hearing order: `tn-submit-order`
- For deadline arithmetic (motion-service windows): `tn-deadlines`

## References

- `references/oral-argument-structure.md`
- `references/remote-hearing-protocol.md` — platform-agnostic remote
  etiquette; defers platform choice to local rules
- `references/courtroom-etiquette.md`
- `references/general-sessions-docket-call.md`
- `references/evidentiary-hearing-prep.md`
