---
name: az-hearings-codearranger
title: Arizona Hearings
description: 'Use when preparing for or conducting a hearing in an Arizona court (Superior Court or Justice Court). Triggers: "Arizona motion hearing", "Rule 7.1 oral argument Arizona", "request oral argument Arizona", "remote hearing Arizona", "telephonic hearing Arizona", "scheduling conference Rule 16 Arizona", "Arizona case management conference", "compulsory arbitration hearing Arizona", "Rule 72 arbitration Arizona", "courtroom etiquette Arizona", "hearing-day checklist Arizona", "how do I argue a motion in Arizona". Covers motion practice and oral argument under Ariz. R. Civ. P. 7.1 (critical: court may decide on briefs without oral argument even if requested), remote/telephonic appearances, Rule 16 scheduling and case-management conferences, compulsory-arbitration hearings under Rules 72-77, courtroom etiquette, and hearing-day packet.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/az-court-docs/skills/az-hearings
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Arizona Hearings

> **NOT LEGAL ADVICE.** Hearing-preparation aid only. Verify against the
> assigned judge's procedures, the court's local rules, and the court's
> current remote-appearance instructions before any hearing.

Use this skill alongside `az-statewide-format` and the specific venue
skill (`az-maricopa`, `az-pima`, `az-superior-courts`,
`az-justice-courts`) when preparing for, attending, or following up on a
hearing.

## Motion practice and oral argument — Ariz. R. Civ. P. 7.1

Civil motion practice is governed statewide by **Ariz. R. Civ. P. 7.1**.
Key mechanics (see `az-law-references` for current text, day counts, and
page limits):

- **Motion, response, reply** — Rule 7.1(a): a motion states the relief
  sought and the grounds, and is supported by a memorandum where required.
  The opposing party files a **response** within the rule's window
  (generally **10 days** after service of the motion under Rule 7.1(a)(3);
  add time for service by mail under **Rule 6(c)**), and the movant may
  file a **reply**. Compute every date with `az-deadlines`.
- **Request for oral argument** — a party may **request oral argument**,
  typically by including the request in the caption or in the
  motion/response. The request is a request, not a guarantee.
- **Court may decide on the briefs** — under **Rule 7.1(d)** the court
  **may decide motions without oral argument, even if oral argument is
  requested** (subject to Rule 56(c)(1)). Do not assume you will
  be heard live; many civil motions are submitted on the briefs. Check the
  assigned judge's procedures and watch the docket for either a hearing
  notice or a ruling under advisement.
- **Accelerated / expedited rulings** — the court may shorten time where
  grounds exist; confirm whether the matter is set on shortened time.

> Agent behavior: do **not** state that oral argument will occur. Frame it
> as requested and contingent on the court setting it; under Rule 7.1(d)
> the court may decide on the briefs even if oral argument is requested.

## Remote and telephonic appearances

Arizona courts broadly adopted **video and telephonic proceedings**
following the 2020 Arizona Supreme Court administrative orders, and remote
appearances remain widely available at the court's discretion. Many
Superior Court and Justice Court matters — status conferences, oral
argument, some evidentiary hearings — proceed by **two-way video** (often
a court-hosted platform) or by telephone.

> Agent behavior: do **not** assume a platform or a meeting ID. Whether a
> hearing is in-person, video, or telephonic is set by the court's current
> practice and the assigned judge. **Confirm the court's current
> remote-appearance practice** and pull the link/dial-in from the court's
> website or the most recent notice. Meeting IDs change — never cache or
> guess them.

If the hearing is remote, the general etiquette holds:

- Join **early** (10-15 minutes) using the court's published link/number.
- Use your **full legal name** as the display name.
- **Mute** on entry; unmute only when addressed.
- **Camera on** unless the court directs otherwise.
- **Quiet, professional background**; test audio and video first.

## Scheduling and case-management conferences — Rule 16

**Ariz. R. Civ. P. 16** governs the **scheduling conference** and
**case-management conference**. The court typically enters a **scheduling
order** fixing discovery deadlines, disclosure obligations, ADR/arbitration
status, dispositive-motion cutoffs, and trial. Come prepared to discuss the
Rule 16 agenda items (the proposed case-management plan, discovery scope,
ADR, and a realistic trial timeframe).

- **Comprehensive pretrial conference** — Rule 16 also provides for a
  **comprehensive (final) pretrial conference** before trial, where the
  court addresses the joint pretrial statement, exhibits, witnesses,
  motions in limine, and trial logistics. Arrive with the pretrial
  statement complete and exhibits pre-marked.
- Confirm whether each Rule 16 conference is in person, by video, or
  telephonic.

## Compulsory arbitration — Rules 72-77

Civil cases at or below the county's jurisdictional threshold are subject
to **compulsory arbitration** under **Ariz. R. Civ. P. 72-77**. The
threshold is set by **local rule per county** (commonly $50,000 in the
larger counties) — confirm the current figure for the venue via
`az-law-references` / the local rule before assuming a case is in or out.

- **Arbitrator appointment** — Rule 73: the court appoints an arbitrator
  from the county list (members of the State Bar of Arizona).
- **Hearing window** — the arbitration **hearing** is set within the
  rule's window after the arbitrator's appointment (generally **not fewer
  than 60 nor more than 120 days**). The **Arizona Rules of Evidence apply**
  at the hearing (Rule 75).
- **Award and appeal de novo** — the arbitrator issues a written award; any
  party may **appeal for a trial de novo** in Superior Court within the
  rule's deadline, after which the case proceeds as an ordinary lawsuit
  (discovery and jury trial available). Note the rule's **cost/sanction
  consequences** for an appellant who fails to improve on the award.

Settlement conferences and other ADR (mediation) may also be ordered;
arrive with settlement authority and a current exposure analysis.

## In-person hearings — etiquette

- Arrive **early** (30 minutes) to clear security.
- **Dress** in business attire; self-represented filers should wear
  business-casual at minimum (no shorts, hats, or athletic wear).
- **Phones** silenced and put away.
- **Stand** when addressing the court ("May it please the Court, Your
  Honor").
- Address the judge as **"Your Honor"**; refer to opposing counsel and
  parties by **"Mr./Ms. [surname]"** from the podium.

## Hearing-day packet — what to bring

| Item | Purpose |
|---|---|
| 2 paper copies of each filing (court + opposing party) | Even in e-filed (AZTurboCourt) cases, have hard copies at the podium |
| Judge's copy (if local rule / procedures require one) | Some courts want a courtesy copy in advance |
| The relevant Ariz. R. Civ. P. / Ariz. R. Evid. excerpts (printed, tabbed) | Have the governing rule text at hand (see `az-law-references`) |
| Key cases (printed; flagged published vs. depublished) | Flag the dispositive authorities |
| Witness outlines (if evidentiary) | One per witness; sequential exam outline |
| Exhibit list + copies | Original + court copy + opposing-party copy of each exhibit |
| Proposed order / form of judgment (1 copy + 1 spare) | The court may sign at the hearing; see `az-submit-order` |
| Notepad + 2 pens | Notes during the hearing |

## Oral argument — structure

A workable structure for an Arizona civil motion:

1. **Opening** (~30 sec). "May it please the Court, [Name] for the
   [Plaintiff / Defendant]. This is [Movant]'s Motion to [Dismiss /
   Compel / for Summary Judgment]. We respectfully ask the Court to
   [grant / deny] for [N] reasons."
2. **Roadmap** (~30 sec). "First... Second... Third..."
3. **Substantive argument** — lead with the strongest point; cite the
   governing Ariz. R. Civ. P., Ariz. R. Evid., or case; tie back to the
   record.
4. **Address counter-arguments candidly** — answer the court's questions
   directly; do not duck weaknesses.
5. **Reserve rebuttal** if you are the movant.
6. **Closing** (~15 sec). "For these reasons, [Movant] respectfully asks
   the Court to [grant / deny]. Thank you, Your Honor."

## Evidentiary hearings — special considerations

For evidentiary hearings (injunctions, contempt, post-judgment debtor
exams, disputed-fact motions, arbitration hearings under Rules 72-77):

- **Subpoena witnesses** in advance under Ariz. R. Civ. P. 45.
- **Pre-mark exhibits** per the court's numbering convention.
- **Witness exclusion** — request under Ariz. R. Evid. 615 if helpful.
- **Stipulations** — confer beforehand to stipulate to undisputed facts and
  to authentication of routine business records under Ariz. R. Evid.
  803(6) / 902 (see `az-law-references`).
- **Record** — confirm with the clerk how the proceeding is recorded (and
  how the record is made for a remote/telephonic hearing).

## Adjournments / continuances

- **Confer with the opposing party first** — stipulated or unopposed
  motions to continue are far more likely to be granted.
- File the motion / stipulation **before** the setting, stating the current
  date, the reason, whether opposing counsel agrees, and proposed new
  dates. Many courts want a proposed order.

## Composition

- For format: `az-statewide-format`
- For courthouse logistics (location, security, division): `az-maricopa`,
  `az-pima`, `az-superior-courts`, `az-justice-courts`
- For scheduling / noticing the hearing: `az-schedule-hearing`
- For drafting the motion and supporting papers: `az-draft-motion`,
  `az-draft-declaration`, `az-draft-note`
- For the post-hearing order: `az-submit-order`
- For deadline arithmetic (response/reply windows): `az-deadlines`
- For canonical Ariz. R. Civ. P. / Ariz. R. Evid. text and local rules:
  `az-law-references`
