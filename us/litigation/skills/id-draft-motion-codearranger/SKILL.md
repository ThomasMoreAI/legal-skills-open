---
name: id-draft-motion-codearranger
title: Draft an Idaho Motion
description: This skill should be used to scaffold an Idaho civil motion with its supporting Memorandum, a Notice of Hearing, and a proposed order. Triggers include "draft an Idaho motion", "I.R.C.P. 7(b) motion", "Rule 7(b) motion Idaho", "draft an Idaho motion for summary judgment", "motion for summary judgment Rule 56 Idaho", "Idaho memorandum in support", "supporting memorandum Idaho motion", "notice of hearing for my Idaho motion", and "draft a proposed order for an Idaho motion". Produces a motion plus supporting Memorandum plus a Notice of Hearing plus a proposed order in Idaho format, applying the pro-se drafting framework (state the relief, cite the rule, state supporting facts, apply controlling Idaho authority, conclude). Composes with `id-statewide-format` for the caption and signature, `id-draft-declaration` for sworn facts, `id-draft-note` for the Notice of Hearing, `id-draft-order` for the proposed order, and the relevant venue overlay.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/id-court-docs/skills/id-draft-motion
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Argument Structure
  path: references/argument-structure.md
- title: Motion Template
  path: references/motion-template.md
- title: Summary Judgment Standard
  path: references/summary-judgment-standard.md
---

# Draft an Idaho Motion

> **NOT LEGAL ADVICE.** This skill scaffolds a draft motion as a
> drafting aid. The user — not the skill — chooses the motion
> type, the theory of relief, and the strategy. Verify every
> rule, deadline, and citation against the current Idaho Rules
> of Civil Procedure and controlling case law before filing.

Use this skill to produce a **motion + supporting Memorandum +
Notice of Hearing + proposed order** in Idaho format. The form of
motions is governed by **I.R.C.P. 7(b)**. The caption, signature
block (with the Idaho State Bar number where counsel signs), and
certificate of service follow `id-statewide-format`.

## I.R.C.P. 7(b) — form of motions

**Rule 7(b)** governs how a written motion is made and supported.
Confirm the current subdivision text in `id-law-references`
before relying on the points below:

- **I.R.C.P. 7(b)(1)** — a motion must be **in writing** (unless
  made during a hearing or trial), state with **particularity the
  grounds** on which it is based, and state the **relief or order
  sought**. The motion is presented with a **supporting
  Memorandum** (the brief stating points and authorities).
- **I.R.C.P. 7(b)(3)** — the moving party files and serves a
  **Notice of Hearing** that sets the motion for hearing. The
  notice and the motion must be **served and filed at least 14
  days before the hearing** (confirm the current day count and
  any service add-on in `id-law-references`; compute the actual
  dates with `id-deadlines`).

A motion that turns on a question of fact must be supported by an
**affidavit or declaration** or other evidence (see
`id-draft-declaration`).

## Caption and party designations

In a civil action the parties are **Plaintiff** and **Defendant**;
in a family-law or special proceeding they are **Petitioner** and
**Respondent**. The caption gives the names of the parties, the
title of the court, the case number, and the document title. See
`id-statewide-format` for the caption recipe and for whether the
matter is heard in the **Magistrate Division** or the **District
Court**.

## Page formatting and line numbering

Each generated document uses line-numbered pleading paper and a
footer carrying the document title and "Page X of Y", with the
**document title printed at the bottom of each page** per the
I.R.C.P. 2 form requirements. Defer the full recipe (margins,
font, spacing, title-of-court placement) to `id-statewide-format`;
do not hard-code measurements here.

## Motion + Memorandum + Notice + proposed-order structure

```
                  [Caption — see id-statewide-format]

         [DOCUMENT TITLE IN ALL CAPS, e.g.,
     DEFENDANT'S MOTION FOR SUMMARY JUDGMENT]

[Movant], [Plaintiff / Defendant], by [counsel / appearing
pro se] and pursuant to I.R.C.P. 7(b) and [specific rule, e.g.,
I.R.C.P. 56], moves the Court for [specific relief]. The grounds
for this Motion are stated with particularity below and in the
supporting Memorandum that follows.

         MEMORANDUM IN SUPPORT OF MOTION

                       I. INTRODUCTION
[1-2 paragraph summary of the case, the relief sought, and the
reasons in headline form.]

                  II. STATEMENT OF FACTS
[Numbered factual paragraphs. Each material fact gets a record
citation — Affidavit/Declaration ¶ X, Complaint ¶ X, Exhibit X,
deposition page/line, or admission in the pleadings. Sworn facts
belong in an affidavit or declaration; see id-draft-declaration.]

                  III. ARGUMENT
A. [Headline of first argument.]
[Lead with the rule citation; state the controlling standard;
apply it to the facts; cite controlling Idaho authority.]

B. [Headline of second argument.]

                  IV. CONCLUSION
For the foregoing reasons, [Movant] respectfully requests that the
Court [grant the relief sought] and sign the accompanying proposed
Order.

                                     [Signature block —
                                      see id-statewide-format]
                                     [Certificate of service]
```

The **Notice of Hearing** is a separate document (see
`id-draft-note`); the **proposed order** is a separate document
(see `id-draft-order`).

## Summary judgment — I.R.C.P. 56

The most common dispositive motion is the **motion for summary
judgment under I.R.C.P. 56**. Summary judgment is granted when
there is **no genuine dispute as to any material fact** and the
moving party is **entitled to judgment as a matter of law**; the
court liberally construes the record in the light most favorable
to the party opposing the motion and draws all reasonable
inferences in that party's favor.

Rule 56 sets a **distinct timing track** that overrides the
ordinary 14-day notice rule — confirm the current figures in
`id-law-references`:

- the **motion is served at least 28 days before the hearing**;
- the **answering brief (and opposing affidavits) are served at
  least 14 days before the hearing**;
- the **reply brief** is served within the period the rule sets.

> A Rule 56 motion is supported by **affidavits or declarations
> made on personal knowledge** and documentary exhibits (see
> `id-draft-declaration`). Confirm the current Rule 56 text,
> including the affidavit/declaration content requirements of
> I.R.C.P. 56(c), in `id-law-references`.

## Common motion types

| Motion | Rule | Notes |
|---|---|---|
| Motion for Summary Judgment | I.R.C.P. 56 | 28-day / 14-day timing track; supporting affidavits/declarations and exhibits |
| Motion to Dismiss | I.R.C.P. 12(b) | Including 12(b)(6) failure to state a claim |
| Motion to Compel Discovery | I.R.C.P. 37 | Attach the deficient responses; satisfy any meet-and-confer requirement |
| Motion for New Trial / to Alter or Amend | I.R.C.P. 59 | Verify the current time limit and grounds |
| Motion for Relief from Judgment | I.R.C.P. 60 | Mistake, newly discovered evidence, fraud, void judgment, etc. |

## The pro-se drafting framework — applied to motions

Self-represented filers should follow the **pro-se drafting
framework** (see `id-pro-se`):

1. **State the relief clearly** in the opening sentence.
2. **Cite the rule** (I.R.C.P. ____) that grants the court power
   to award that relief, stating the grounds with particularity
   per Rule 7(b)(1).
3. **State the facts** that satisfy each element of the standard,
   with record citations to a supporting affidavit or declaration.
4. **Apply the controlling Idaho case law** to those facts.
5. **Conclude** with the specific order sought, and lodge a
   proposed order (see `id-draft-order`).

## Filing checklist

- [ ] Caption matches the assigned court (District Court or Magistrate Division) and county
- [ ] Title in ALL CAPS centered below the caption
- [ ] Grounds stated with particularity; relief stated; supporting Memorandum included (Rule 7(b)(1))
- [ ] Notice of Hearing prepared; served/filed at least 14 days before the hearing (Rule 7(b)(3)) — see `id-draft-note`
- [ ] Questions of fact supported by affidavit/declaration/evidence
- [ ] For Rule 56: no-genuine-dispute showing; 28-day / 14-day timing track confirmed; supporting affidavits/declarations and exhibits attached
- [ ] All cited rules and authorities correct (run `id-fact-check`)
- [ ] Proposed order drafted as a **separate** document (`id-draft-order`)
- [ ] Hearing and response deadlines computed (`id-deadlines`)
- [ ] Certificate of service complete (I.R.C.P. 5)
- [ ] Format check passes (`scripts/format-check.py`)

## Composition

- For format, caption, and signature block: `id-statewide-format`
- For the supporting affidavit/declaration: `id-draft-declaration`
- For the Notice of Hearing: `id-draft-note`, `id-schedule-hearing`
- For the proposed order: `id-draft-order`
- For the venue overlay: `id-ada`, `id-bonneville`,
  `id-county-courts`, `id-family-court`
- For pre-filing QC: `id-quality-check`, `id-fact-check`
- For deadline math: `id-deadlines`
- For pro se conventions: `id-pro-se`
- For the court-rules corpus: `id-law-references`

## References to author

- `references/motion-template.md` — annotated motion + Memorandum
  + Notice of Hearing + proposed-order template
- `references/summary-judgment-standard.md` — I.R.C.P. 56 standard
  and the 28-day / 14-day timing track
- `references/argument-structure.md` — pro-se drafting framework
  applied to an Idaho motion
