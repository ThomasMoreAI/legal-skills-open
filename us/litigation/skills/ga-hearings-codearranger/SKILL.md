---
name: ga-hearings-codearranger
title: Georgia Hearings
description: This skill should be used when preparing for or conducting a motion hearing or oral argument in a Georgia court. Triggers include "Georgia motion hearing", "oral argument Georgia", "summary judgment hearing", "rule nisi hearing", "Georgia courtroom etiquette", "appearing pro se at a hearing in Georgia". Covers Georgia motion practice under USCR 6 (30-day response under USCR 6.2, request for oral hearing under USCR 6.3, the court setting the hearing by Rule Nisi under USCR 6.4), how summary- judgment hearings work under O.C.G.A. § 9-11-56, evidentiary hearings, courtroom etiquette, appearing pro se, the per-judge standing case-management orders in Fulton, the domestic standing orders in family cases, and how State and Magistrate court hearing practice differs.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ga-court-docs/skills/ga-hearings
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Georgia Hearings

> **NOT LEGAL ADVICE.** This skill is a procedural and
> drafting aid, not legal advice. Verify current rules,
> deadlines, and venue-specific practices before filing.
> Pair with substantive review by counsel where stakes
> warrant.

Use this skill in addition to `ga-statewide-format` and the specific
court skill (`ga-fulton`, `ga-cobb`, `ga-gwinnett`) when preparing
for, attending, or following up on a hearing.

## Motion practice and hearings — the basics

Under **USCR 6**, motions in Georgia civil practice run on a fixed
rhythm:

| Step | Authority | Detail |
|---|---|---|
| Motion filed and served | USCR 6.1 | Motion stated with particularity; cite authority |
| Response | USCR 6.2 | **30 days** after service of the motion |
| Request for oral hearing | USCR 6.3 | A party must **request** oral argument; for summary-judgment motions oral argument is a matter of right if timely requested |
| Court sets the hearing | USCR 6.4 | The court schedules the hearing by **Rule Nisi** (a proposed order setting date/time, signed by the judge) |

Many motions are **decided on the briefs**. Oral argument is held
only when a party requests it under USCR 6.3 (and the court grants
it), or when the court orders it on its own. The court memorializes
the setting in a **Rule Nisi**.

Common hearing types:

| Hearing | Typical length | Triggered by |
|---|---|---|
| Motion hearing | 20-60 min | USCR 6.3 request granted, or court-set |
| Summary-judgment hearing | 30-60 min | O.C.G.A. § 9-11-56; oral argument on request |
| Evidentiary hearing | 1+ hours | Court orders after motion practice |
| Status / case-management conference | 15-30 min | Court-initiated; USCR 5 |
| Bench / jury trial | Variable | Final stage |

## Summary-judgment hearings — O.C.G.A. § 9-11-56

Summary-judgment hearings have a hard timing rule built into the
statute:

- The motion must be **served at least 30 days before the hearing**
  (O.C.G.A. § 9-11-56(c)); the adverse party may serve opposing
  affidavits prior to the day of hearing.
- The standard: under **_Lau's Corp. v. Haskins_, 261 Ga. 491
  (1991)**, a defendant moving for summary judgment may prevail by
  **pointing to an absence of evidence** in the record to support an
  essential element of the plaintiff's case; the movant need not
  affirmatively disprove the claim. If the movant carries that
  burden, the nonmovant cannot rest on the pleadings and must point
  to specific record evidence creating a genuine issue of material
  fact.
- At the hearing, the court construes the evidence and all reasonable
  inferences in the light most favorable to the nonmovant.

Prepare to argue from the **record** — cite the specific
depositions, affidavits, and discovery responses by page and line,
not the allegations in the pleadings.

## Standing orders — read them before you appear

Georgia hearing practice is heavily shaped by **standing orders**
that attach automatically or by judge:

- **Fulton per-judge Civil Standing Case Management Orders.** Many
  Superior Court of Fulton County judges enter their own civil
  standing case-management order governing conferral, motion
  formatting, courtesy copies, and hearing logistics. Read the
  **assigned judge's** standing order before drafting or appearing —
  requirements differ judge to judge.
- **Domestic standing orders in family cases.** In divorce and other
  domestic matters, a domestic relations standing order (and, in
  several counties, a co-parenting / parenting-seminar standing order
  under USCR 24.8) attaches automatically at filing. It restrains
  conduct (asset disposal outside the ordinary course, insurance
  changes, child removal) and sets pre-hearing filing duties — e.g.,
  the Domestic Relations Financial Affidavit (USCR 24.2) and the
  Child Support Worksheet must be on file before the hearing.
  Violations are punishable as **contempt**.

## In-person hearings — etiquette

- Arrive **30 minutes early** for security screening.
- **Dress code**: business attire for attorneys; pro se filers should
  wear business-casual at minimum (no shorts, hats, athletic gear).
- **Phones silenced** and put away.
- **Stand when addressing the court** ("May it please the Court, Your
  Honor").
- Address the bench as **"Your Honor"**; address opposing counsel and
  parties as **"Mr./Ms. [surname]"** — no first names from the
  podium.

## Hearing-day packet — what to bring

| Item | Purpose |
|---|---|
| 2 paper copies of each filing | Even in e-filed cases, judges expect hard copies at the podium |
| Courtesy / chambers copy if the standing order requires | Per the assigned judge's standing order |
| Printed rules and statutes (USCR, O.C.G.A.) | Have the operative sections at hand |
| Key cases, flagged | The dispositive authorities tabbed |
| Witness outlines (if evidentiary) | One per witness |
| Exhibit list and copies | Original + court copy + opposing-party copy |
| Proposed order + Rule Nisi | The judge may sign in court immediately |
| Notepad and pens | For notes during the hearing |

## Oral argument — structure

1. **Opening** — 30 seconds. "May it please the Court, [Name] for the
   [Plaintiff / Defendant / Petitioner / Respondent]. I am here on
   [Movant]'s Motion to [Dismiss / Compel / for Summary Judgment]."
2. **Roadmap** — 30 seconds. "First, [issue 1]. Second, [issue 2]."
3. **Substantive argument** — lead with the strongest point; cite the
   rule or case; tie back to the record.
4. **Address counter-arguments** — be candid; answer the court's
   questions directly.
5. **Reserve rebuttal** if you are the movant.
6. **Closing** — 15 seconds. "For the reasons stated, [Movant]
   respectfully asks the Court to [grant / deny] the Motion."

## Evidentiary hearings — special considerations

For evidentiary hearings (disputed material facts, interlocutory
injunctions, contempt, post-judgment exams):

- **Subpoena witnesses well in advance** (O.C.G.A. § 24-13-21
  et seq.).
- **Pre-mark exhibits** with the division's numbering convention.
- **Witness sequestration** under O.C.G.A. § 24-6-615 if helpful.
- **Confer with opposing counsel** beforehand to stipulate to
  undisputed facts and authentication of routine documents.
- **Confirm the record method** with the courtroom clerk — court
  reporter or court recording — in advance.

## State and Magistrate court hearing practice

- **State Court** practice tracks Superior Court closely: the Uniform
  State Court Rules parallel the USCR, motions follow the USCR 6
  rhythm, and hearings are set by Rule Nisi. Most debt-collection and
  tort suits are heard here.
- **Magistrate Court is informal.** Under O.C.G.A. §§ 15-10-40
  through 15-10-53, the Civil Practice Act and the rules of evidence
  are **relaxed** for the small-claims civil docket (cap $15,000,
  O.C.G.A. § 15-10-2). Hearings are short, parties commonly appear
  pro se (a corporation may appear through an officer or employee),
  and the magistrate develops the facts conversationally. A losing
  party may appeal **de novo** to State or Superior Court under
  O.C.G.A. § 15-10-41(b). Bring your documents and witnesses — there
  is no second chance at the magistrate level on the same record.

## Appearing pro se

Pro se filers are held to the same procedural rules as attorneys.
Read the assigned judge's standing order, file and serve on time
under USCR 6, request oral argument under USCR 6.3 if you want it,
and bring organized copies. In Magistrate Court the relaxed procedure
makes pro se appearance routine.

## Composition

- For format: `ga-statewide-format`
- For drafting the motion and supporting papers: `ga-draft-motion`,
  `ga-draft-note`
- For drafting the proposed order and Rule Nisi: `ga-draft-order`
- For getting the motion set in the first place: `ga-schedule-hearing`
- For the post-hearing signed order: `ga-submit-order`
- For deadlines and timing: `ga-deadlines`
- For the specific court (logistics, standing orders, e-filing):
  `ga-fulton`, `ga-cobb`, `ga-gwinnett`
- For assembling the filing: `ga-file-packet`

## References

- `references/oral-argument-structure.md`
- `references/summary-judgment-hearing.md` — O.C.G.A. § 9-11-56 and
  the _Lau's Corp._ standard
- `references/courtroom-etiquette.md`
