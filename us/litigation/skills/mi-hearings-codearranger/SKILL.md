---
name: mi-hearings-codearranger
title: Michigan Hearings
description: Use when preparing for or conducting a hearing in a Michigan court (Circuit Court, District Court, or a specialized division). Triggers include "Michigan motion hearing", "MCR 2.119 oral argument", "motion day Michigan", "Zoom hearing Michigan", "remote hearing Michigan", "scheduling conference MCR 2.401", "courtroom etiquette Michigan", "case evaluation Michigan", "Michigan settlement conference", "hearing-day checklist Michigan", "how do I argue a motion in Michigan". Covers motion practice and oral argument under MCR 2.119 (including when the court may dispense with oral argument under MCR 2.119(E)), remote video proceedings under MCR 2.407, scheduling and pretrial conferences under MCR 2.401, the ADR / case-evaluation track (MCR 2.403 / 2.410 / 2.411), courtroom etiquette, and the hearing-day packet.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/mi-court-docs/skills/mi-hearings
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Michigan Hearings

> **NOT LEGAL ADVICE.** Hearing-preparation aid only. Verify against
> the assigned judge's practice guidelines, the court's local
> administrative order, and the court's current remote-appearance
> instructions before any hearing.

Use this skill alongside `mi-statewide-format` and the specific venue
skill (`mi-wayne`, `mi-oakland`, `mi-36th-district`,
`mi-circuit-courts`, `mi-district-courts`) when preparing for,
attending, or following up on a hearing.

## Motion practice and oral argument — MCR 2.119

Civil motion practice is governed statewide by **MCR 2.119**. Key
mechanics (see `mi-law-references` for current text, day counts, and
page rules):

- **Form and content** — MCR 2.119(A): a motion must state the relief
  sought and the grounds, and (with limited exceptions) be accompanied
  by a brief. The motion and any response must comply with the MCR
  1.109 document standards (see `mi-statewide-format`).
- **Notice of hearing** — MCR 2.119(C) sets the service-before-hearing
  windows (the standard pre-hearing notice period, with the longer
  period when served by mail). Confirm the current day counts and
  compute the date with `mi-deadlines`.
- **Oral argument** — MCR 2.119(E)(1)-(2): a party may request oral
  argument; many courts hear civil motions on a recurring **motion
  day** or motion-call docket.
- **Court may dispense with oral argument** — **MCR 2.119(E)(3)**
  expressly permits the court to **dispense with or limit oral
  argument** and decide the motion on the briefs. Do not assume you
  will be heard live — check the venue's local administrative order
  and the judge's practice guidelines.

> **Praecipe / notice-of-hearing practice varies by court.** Some
> Michigan courts require a **praecipe** or a separately scheduled
> motion-day slot, others let you notice the hearing directly.
> Confirm the local procedure before noticing. See
> `mi-schedule-hearing`.

## Motion day / motion-call dynamics

- Many Circuit and District courts hear civil motions on a recurring
  **motion-call docket**. Confirm whether the venue requires the
  motion to be **praeciped / set** for a specific motion day, whether
  the judge wants a **judge's copy** delivered in advance, and whether
  oral argument is expected or the matter is submitted on the briefs.
  These are **local-administrative-order and practice-guideline**
  questions — check the court's website and the assigned judge's
  guidelines.
- Be present and ready when your case is called; know whether you are
  arguing, stipulating, or seeking an adjournment.

## Remote proceedings — MCR 2.407

Michigan adopted broad **video and remote-participation** practice
following the 2020 emergency administrative orders, now codified in
**MCR 2.407** (video proceedings). Under MCR 2.407 the court has broad
discretion to allow or require participation by **two-way
interactive video** (commonly Zoom via the court's MiCourt / virtual
courtroom infrastructure), subject to the rule's standards and the
parties' due-process rights.

> Agent behavior: do **not** assume a platform or a meeting ID.
> Whether a given hearing is in-person, remote, or hybrid is set by
> the court's local practice and the assigned judge under MCR 2.407.
> Pull the current remote-appearance instructions and the judge's
> Zoom/virtual-courtroom link from the court's website or the most
> recent notice. Meeting IDs change — never cache or guess them.

If the hearing is remote, the general etiquette holds:

- Join **early** (10-15 minutes); use the court's published link.
- Use your **full legal name** as the display name.
- **Mute** on entry; unmute only when addressed.
- **Camera on** unless the court orders otherwise.
- **Quiet, professional background**; test audio and video first.

## Scheduling and pretrial conferences — MCR 2.401

**MCR 2.401** governs pretrial and **scheduling conferences**. The
court typically enters a **scheduling order** fixing discovery
cutoffs, case-evaluation/ADR dates, motion-completion dates, and
trial. Come prepared to discuss the issues in MCR 2.401(C) (discovery
plan, ADR, witness/exhibit timing). Confirm whether the conference is
in person, by phone, or remote under MCR 2.407.

## ADR — case evaluation and mediation (MCR 2.403 / 2.410 / 2.411)

Most Michigan civil cases pass through an **ADR** step set in the MCR
2.401 scheduling order:

- **MCR 2.410** — general ADR rule; the court selects the ADR process.
- **MCR 2.403** — **case evaluation** (a panel evaluates the case and
  renders an award the parties may accept or reject). Note that the
  former mandatory case-evaluation-sanctions regime was amended;
  confirm the **current** sanction rules in MCR 2.403 via
  `mi-law-references` before relying on them.
- **MCR 2.411** — **mediation** (facilitative mediation before a
  neutral). Settlement and pretrial settlement conferences are common;
  arrive with settlement authority and an updated damages/exposure
  analysis.

## In-person hearings — etiquette

- Arrive **early** (30 minutes) to clear security.
- **Dress** in business attire; pro se filers should wear
  business-casual at minimum (no shorts, hats, or athletic wear).
- **Phones** silenced and put away.
- **Stand** when addressing the court ("May it please the Court, Your
  Honor").
- Address the judge as **"Your Honor"**; refer to opposing counsel and
  parties by **"Mr./Ms. [surname]"** from the podium.

## Hearing-day packet — what to bring

| Item | Purpose |
|---|---|
| 2 paper copies of each filing (court + opposing party) | Even in e-filed (MiFILE) cases, have hard copies at the podium |
| Judge's copy (if practice guidelines require one) | Delivered in advance for longer motions |
| The relevant MCR / MRE excerpts (printed, tabbed) | Have the governing rule text at hand (see `mi-law-references`) |
| Key cases (printed; flagged published vs. unpublished) | Flag the dispositive authorities |
| Witness outlines (if evidentiary) | One per witness; sequential exam outline |
| Exhibit list + copies | Original + court copy + opposing-party copy of each exhibit |
| Proposed order (1 copy + 1 spare) | The court may sign in chambers; see `mi-submit-order` |
| Notepad + 2 pens | Notes during the hearing |

## Oral argument — structure

A workable structure for a Michigan civil motion:

1. **Opening** (~30 sec). "May it please the Court, [Name] for the
   [Plaintiff / Defendant]. This is [Movant]'s Motion to [Dismiss /
   Compel / for Summary Disposition]. We respectfully ask the Court to
   [grant / deny] for [N] reasons."
2. **Roadmap** (~30 sec). "First... Second... Third..."
3. **Substantive argument** — lead with the strongest point; cite the
   governing MCR, MRE, or case; tie back to the record.
4. **Address counter-arguments candidly** — answer the court's
   questions directly; do not duck weaknesses.
5. **Reserve rebuttal** if you are the movant.
6. **Closing** (~15 sec). "For these reasons, [Movant] respectfully
   asks the Court to [grant / deny]. Thank you, Your Honor."

## Evidentiary hearings — special considerations

For evidentiary hearings (injunctions, contempt, post-judgment
creditor exams, disputed-fact motions):

- **Subpoena witnesses** in advance under MCR 2.506.
- **Pre-mark exhibits** per the court's numbering convention.
- **Witness sequestration** — request under MRE 615 if helpful.
- **Stipulations** — confer beforehand to stipulate to undisputed
  facts and to authentication of routine business records under
  MRE 803(6) / 902 (see `mi-law-references`).
- **Record** — confirm with the clerk whether the proceeding is
  recorded by the court (and how the remote record is made if under
  MCR 2.407).

## Adjournments

- **Confer with the opposing party first** — stipulated or unopposed
  motions to adjourn are far more likely to be granted.
- File the motion / stipulation to adjourn **before** the setting,
  stating the current date, the reason, whether opposing counsel
  agrees, and proposed new dates. Many courts want a proposed order.

## Composition

- For format: `mi-statewide-format`
- For courthouse logistics (parking, security, division): `mi-wayne`,
  `mi-oakland`, `mi-36th-district`, `mi-circuit-courts`,
  `mi-district-courts`
- For scheduling / noticing the hearing: `mi-schedule-hearing`
- For drafting the motion and supporting papers: `mi-draft-motion`,
  `mi-draft-declaration`, `mi-draft-note`
- For the post-hearing order: `mi-submit-order`
- For deadline arithmetic (motion-service windows): `mi-deadlines`
- For canonical MCR / MRE text and local rules: `mi-law-references`

## References

- `references/oral-argument-structure.md`
- `references/remote-hearing-protocol.md` — MCR 2.407 video-proceedings
  etiquette; defers the platform and link to the court's instructions
- `references/courtroom-etiquette.md`
- `references/motion-day-practice.md` — MCR 2.119 motion-call dynamics
- `references/evidentiary-hearing-prep.md`
