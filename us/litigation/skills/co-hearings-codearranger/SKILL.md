---
name: co-hearings-codearranger
title: Colorado Hearings
description: This skill should be used when preparing for or conducting a hearing in a Colorado court. Triggers include "Colorado oral argument", "Colorado motion hearing", "Webex Colorado courts", "courtroom etiquette Colorado", "judge's chambers practice standards", "hearing-day checklist Colorado", "tentative ruling Colorado". Covers oral-argument preparation, Webex remote-hearing protocol (Colorado Judicial Branch uses Cisco Webex statewide for remote appearances), courtroom etiquette in front of Colorado judges, the hearing-day packet, and the judge's-chambers-copy conventions that vary by JD and division.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/co-court-docs/skills/co-hearings
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Colorado Hearings

> **NOT LEGAL ADVICE.** Hearing preparation aid only. Verify against
> the assigned judge's practice standards and the Colorado Judicial
> Branch's current remote-appearance instructions before any hearing.

Use this skill in addition to `co-statewide-format` and the specific
court skill (`co-denver`, `co-arapahoe`, `co-county-courts`) when
preparing for, attending, or following up on a hearing.

## Hearings in Colorado civil practice — the basics

Most Colorado civil motions are **decided on the briefs** without
oral argument. The court will issue a **Notice of Setting** when it
decides to set a hearing. Common hearing types:

| Hearing | Typical length | Triggered by |
|---|---|---|
| Status / case-management conference | 15-30 min | C.R.C.P. 16(b); court-initiated |
| Motion hearing | 30-60 min | Court sets after briefing closes |
| Evidentiary hearing | 1+ hours / half-day / day | Court orders after motion practice |
| Trial — bench | Variable | Final stage |
| Trial — jury | Variable | C.R.C.P. 38 jury demand; jury fee under C.R.C.P. 38(b) |

## Remote appearances — Webex

The Colorado Judicial Branch standardized on **Cisco Webex** for
remote appearances statewide. The court's Notice of Setting will
specify whether the hearing is in-person, by Webex, or hybrid, and
will include the Webex meeting URL, meeting number, and password.

**Statewide Webex landing page**: https://www.coloradojudicial.gov/courts/access-court-hearings

Agent behavior: when preparing for a hearing, fetch the assigned
judge's current Webex room ID from the JD's website or from the most
recent Notice of Setting. **Do not cache or guess Webex meeting IDs**
— they change.

Hearing-day Webex protocol:

- Join **15 minutes early**
- Use your **full legal name** as the display name (no nicknames,
  initials, or "iPhone")
- **Mute** on entry; unmute only when the court calls your name
- **Camera on** unless the court orders otherwise — Colorado courts
  generally require video for evidentiary hearings
- **Quiet, professional background** — virtual backgrounds permitted
  but should be neutral
- **Test audio and video** before joining the production hearing

## In-person hearings

For in-person hearings:

- Arrive **30 minutes early** to allow time for security screening
- **Dress code**: business attire (suit/dress) for attorneys; pro se
  filers should wear business-casual at minimum (no shorts, hats,
  athletic gear)
- **Phones off** or silenced and put away (not on the counsel table)
- **Stand when addressing the court** ("May it please the court,
  Your Honor")
- Use **"Your Honor"** for judges and magistrates; **"Mr./Ms.
  [surname]"** for opposing counsel; **"Mr./Ms. [surname]"** for
  parties (do not use first names from the podium)

## Hearing-day packet — what to bring

| Item | Purpose |
|---|---|
| 2 paper copies of each filing (one for court, one for opposing party) | Even in e-filed cases, judges expect counsel to have hard copies at the podium |
| 1 chambers copy (if judge's practice standards require) | Delivered to chambers in advance for motions exceeding the page threshold |
| The relevant rules and statutes (printed or annotated) | Have C.R.C.P. and CRE excerpts at hand for citation |
| Key cases (printed; Bluebooked) | Have the dispositive authorities flagged with hand-written tabs |
| Witness outlines (if evidentiary) | One per witness; sequential exam outline |
| Exhibit list and copies | Original + court copy + opposing party copy of each exhibit |
| Proposed order (1 copy + 1 spare) | The judge may sign in chambers immediately |
| Notepad + 2 pens | For taking notes during the hearing |

## Oral argument — structure

Standard oral-argument structure for Colorado civil motions:

1. **Opening** — 30 seconds.
   "May it please the court, [Name] for the [Plaintiff / Defendant /
   Petitioner / Respondent]. I am here on [Movant]'s Motion to
   [Dismiss / Compel / for Summary Judgment]. We respectfully ask
   the Court to [grant / deny] for three principal reasons..."

2. **Roadmap** — 30 seconds.
   "First, [issue 1]. Second, [issue 2]. Third, [issue 3]."

3. **Substantive argument** — bulk of the time.
   Lead with the strongest point; cite the rule or case; tie back to
   facts in the record.

4. **Anticipate and address counter-arguments** — be candid about
   weaknesses; do not duck the court's questions.

5. **Reserve rebuttal** if you are the moving party.

6. **Closing** — 15 seconds.
   "For the reasons stated, [Movant] respectfully asks the Court to
   [grant / deny] the Motion. Thank you, Your Honor."

## Tentative rulings — judge-by-judge

Some Colorado judges (especially in larger JDs) post **tentative
rulings** prior to motion hearings. The tentative is the court's
preliminary view, and oral argument is the chance to persuade the
court to change it. Check the judge's practice standards or call
chambers to confirm whether tentatives are posted and where (e.g.,
courthouse bulletin board, JD website, emailed to counsel).

If a tentative is posted: read it, identify the points on which it
is adverse to your position, and structure argument around those
points specifically. Acknowledge the tentative ("Your Honor, I
understand the Court's tentative ruling and am here to address point
[X]"), then proceed.

## Evidentiary hearings — special considerations

For evidentiary hearings (Rule 56 with disputed material facts,
preliminary injunctions, contempt, post-judgment debtor exams):

- **Subpoena witnesses well in advance** (10-14 days customary;
  C.R.C.P. 45 allows reasonable notice)
- **Pre-mark exhibits** with the assigned division's exhibit-list
  numbering convention
- **Witness sequestration** — request under CRE 615 if helpful
- **Stipulations** — confer with opposing counsel beforehand to
  stipulate to undisputed facts and authentication of routine
  documents
- **Court reporter** — appear in front of a court reporter or court
  recording system. Confirm with the courtroom clerk in advance
  whether the hearing will be recorded by JTRS (Judicial Tracking
  & Recording System) or by an outside court reporter

## Continuances

Continuances are governed by **C.R.C.P. 121 § 1-11**. To continue a
set hearing:

- **Confer with opposing party** first — joint motions to continue
  are routine grants
- File a **Motion to Continue** stating: the current setting, the
  reason for continuance, whether opposing party agrees, proposed
  new dates
- Many divisions also require a **Proposed Order** that the court
  can sign in chambers
- File **before** the hearing date. Day-of motions to continue are
  disfavored and typically denied absent emergency

## Composition

- For format: `co-statewide-format`
- For the specific court (in-person courthouse logistics, parking,
  security): `co-denver`, `co-arapahoe`, `co-county-courts`
- For scheduling the hearing in the first place: `co-schedule-hearing`
- For drafting the motion and supporting papers: `co-draft-motion`,
  `co-draft-declaration`
- For the post-hearing order: `co-submit-order`

## References

- `references/oral-argument-structure.md`
- `references/webex-protocol.md` — Cisco Webex usage in Colorado
  state courts
- `references/courtroom-etiquette.md`
- `references/evidentiary-hearing-prep.md`
- `references/tentative-ruling-practice.md`
