---
name: id-hearings-codearranger
title: Idaho Hearings
description: 'Use when preparing for or conducting a hearing in an Idaho court (District Court or Magistrate Division). Triggers: "Idaho motion hearing", "Notice of Hearing Idaho", "I.R.C.P. 7(b) hearing notice", "14-day notice of hearing Idaho", "oral argument Idaho", "remote hearing Idaho", "Zoom hearing Idaho", "telephonic hearing Idaho", "courtroom etiquette Idaho", "hearing-day checklist Idaho", "how do I argue a motion in Idaho", "magistrate division hearing". Covers motion practice and the Notice of Hearing under I.R.C.P. 7(b) (a written motion and notice served at least 14 days before the hearing), remote/Zoom appearances, oral argument, courtroom etiquette in the District Court and Magistrate Division, and the hearing-day packet.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/id-court-docs/skills/id-hearings
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Hearing Day Checklist
  path: references/hearing-day-checklist.md
- title: Notice Of Hearing
  path: references/notice-of-hearing.md
- title: Oral Argument Outline
  path: references/oral-argument-outline.md
- title: Remote Appearance
  path: references/remote-appearance.md
---

# Idaho Hearings

> **NOT LEGAL ADVICE.** Hearing-preparation aid only. Verify against the
> assigned judge's procedures, the court's local rules, and the court's
> current remote-appearance instructions before any hearing.

Use this skill alongside `id-statewide-format` and the specific venue
skill (`id-ada`, `id-bonneville`, `id-county-courts`) when preparing for,
attending, or following up on a hearing. Pull verbatim rule text from
`../id-law-references/references/court-rules/`.

## Motion practice and the Notice of Hearing — I.R.C.P. 7(b)

Civil motion practice is governed by **I.R.C.P. 7(b)**. Key mechanics:

- **Written motion + Notice of Hearing.** A motion states the relief
  sought and the grounds with particularity. To get the motion heard,
  serve a **written motion and a Notice of Hearing**.
- **★ 14-day notice.** Under **I.R.C.P. 7(b)(3)**, a written motion and
  notice of the hearing must be **served at least 14 days before the
  time specified for the hearing**, unless the rule or an order shortens
  the time. Compute that date with `id-deadlines` (add the I.R.C.P. 2.2
  mail add-on where the period runs from service by mail).
- **Reserve the date first.** Unlike a self-set motion day, the hearing
  date is typically coordinated with the court or the assigned judge's
  clerk before the Notice of Hearing issues — see `id-schedule-hearing`.
- **Supporting papers.** Support a motion with a **Memorandum** and any
  **Affidavit** or declaration; the opposing party files a responsive
  memorandum and the movant may reply. Confirm the briefing intervals and
  any page limits in the corpus.

> Summary-judgment motions run on a distinct timeline under I.R.C.P. 56
> (motion at least 90 days before trial; motion + brief served at least
> 28 days before the hearing; answering brief at least 14 days before the
> hearing). See `id-draft-motion` and `id-deadlines`.

```
                       NOTICE OF HEARING

   TO: [Opposing party / counsel]

   PLEASE TAKE NOTICE that the undersigned will bring the foregoing
   [Motion to ___] on for hearing before the above-entitled Court at
   the [County] Courthouse, [address], on [DATE] at [TIME], or as soon
   thereafter as counsel may be heard.

   DATED this ___ day of __________, 20__.
                                          ___________________________
                                          [Name], [Pro Se / Attorney]
```

## Remote and telephonic appearances

Idaho courts conduct many proceedings by **video (Zoom) or telephone** at
the court's discretion; remote appearances are widely available for
status conferences, oral argument, and some evidentiary hearings.

> Agent behavior: do **not** assume a platform or a meeting ID. Whether a
> hearing is in-person, video, or telephonic is set by the court's
> current practice and the assigned judge. **Confirm the court's current
> remote-appearance practice** and pull the link / dial-in from the
> court's website or the most recent notice. Meeting IDs change — never
> cache or guess them.

If the hearing is remote, the general etiquette holds:

- Join **early** (10-15 minutes) using the court's published link/number.
- Use your **full legal name** as the display name.
- **Mute** on entry; unmute only when addressed.
- **Camera on** unless the court directs otherwise.
- **Quiet, professional background**; test audio and video first.

## In-person hearings — etiquette

The District Court is presided over by a **district judge**; the
Magistrate Division by a **magistrate judge**. Etiquette is the same in
both:

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
| 2 paper copies of each filing (court + opposing party) | Even in e-filed (iCourt / Odyssey) cases, have hard copies at the podium |
| Judge's courtesy copy (if local rule / procedures require one) | Some courts want a courtesy copy in advance |
| The relevant I.R.C.P. / I.R.E. excerpts (printed, tabbed) | Have the governing rule text at hand (see `id-law-references`) |
| Key cases (printed; note Court of Appeals "(Ct. App. YEAR)" cites) | Flag the dispositive authorities |
| Witness outlines (if evidentiary) | One per witness; sequential exam outline |
| Exhibit list + copies | Original + court copy + opposing-party copy of each exhibit |
| Proposed order / form of judgment (1 copy + 1 spare) | The court may sign at the hearing; see `id-submit-order` |
| Notepad + 2 pens | Notes during the hearing |

## Oral argument — structure

A workable structure for an Idaho civil motion:

1. **Opening** (~30 sec). "May it please the Court, [Name] for the
   [Plaintiff / Defendant]. This is [Movant]'s Motion to [Dismiss /
   Compel / for Summary Judgment]. We respectfully ask the Court to
   [grant / deny] for [N] reasons."
2. **Roadmap** (~30 sec). "First... Second... Third..."
3. **Substantive argument** — lead with the strongest point; cite the
   governing I.R.C.P., I.R.E., or case; tie back to the record.
4. **Address counter-arguments candidly** — answer the court's questions
   directly; do not duck weaknesses.
5. **Reserve rebuttal** if you are the movant.
6. **Closing** (~15 sec). "For these reasons, [Movant] respectfully asks
   the Court to [grant / deny]. Thank you, Your Honor."

## Evidentiary hearings — special considerations

For evidentiary hearings (injunctions, contempt, post-judgment debtor
exams, disputed-fact motions):

- **Subpoena witnesses** in advance under I.R.C.P. 45.
- **Pre-mark exhibits** per the court's numbering convention.
- **Witness exclusion** — request under I.R.E. 615 if helpful.
- **Stipulations** — confer beforehand to stipulate to undisputed facts
  and to authentication of routine business records under I.R.E. 803(6) /
  902 (see `id-law-references`).
- **Record** — confirm with the clerk how the proceeding is recorded (and
  how the record is made for a remote/telephonic hearing).

## Continuances

- **Confer with the opposing party first** — stipulated or unopposed
  motions to continue are far more likely to be granted.
- File the motion / stipulation **before** the setting, stating the
  current date, the reason, whether the opposing party agrees, and
  proposed new dates. Many courts want a proposed order.

## Composition

- For format: `id-statewide-format`
- For courthouse logistics (location, security, division): `id-ada`,
  `id-bonneville`, `id-county-courts`
- For reserving / noticing the hearing: `id-schedule-hearing`
- For drafting the motion and supporting papers: `id-draft-motion`,
  `id-draft-declaration`, `id-draft-note`
- For the post-hearing order: `id-submit-order`
- For deadline arithmetic (the 14-day notice and briefing windows):
  `id-deadlines`
- For canonical I.R.C.P. / I.R.E. text and local rules:
  `id-law-references`

## References

- `references/notice-of-hearing.md` — I.R.C.P. 7(b) Notice of Hearing
  scaffold
- `references/hearing-day-checklist.md` — packet checklist
- `references/oral-argument-outline.md` — argument structure template
- `references/remote-appearance.md` — Zoom / telephonic etiquette
