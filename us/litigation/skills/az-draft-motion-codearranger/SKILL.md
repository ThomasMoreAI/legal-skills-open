---
name: az-draft-motion-codearranger
title: Draft an Arizona Motion
description: This skill should be used to scaffold an Arizona civil motion with its supporting memorandum and a proposed form of order. Triggers include "draft an Arizona motion", "Ariz. R. Civ. P. 7.1 motion", "Rule 7.1 motion", "draft an Arizona motion for summary judgment", "motion for summary judgment Rule 56 Arizona", "Arizona memorandum in support", "Arizona memorandum of points and authorities", "request oral argument Arizona", and "draft a proposed form of order for an Arizona motion". Produces a motion plus supporting memorandum plus a proposed form of order in Arizona format, applying the pro-se drafting framework (state the relief, cite the rule, state supporting facts, apply controlling Arizona authority, conclude). Composes with `az-statewide-format` for the caption and signature, `az-draft-declaration` for sworn facts, `az-draft-order` for the proposed form of order, and the relevant venue overlay.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/az-court-docs/skills/az-draft-motion
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft an Arizona Motion

> **NOT LEGAL ADVICE.** This skill scaffolds a draft motion as a
> drafting aid. The user — not the skill — chooses the motion
> type, the theory of relief, and the strategy. Verify every
> rule, deadline, and citation against the current Arizona Rules
> of Civil Procedure and controlling case law before filing.

Use this skill to produce a **motion + supporting memorandum +
proposed form of order** in Arizona format. The form and
presentation of motions is governed by **Ariz. R. Civ. P. 7.1**.
The caption, signature block (with the State Bar of Arizona bar
number), and certificate of service follow `az-statewide-format`.

## Ariz. R. Civ. P. 7.1 — form and presentation of motions

**Rule 7.1** governs how a written motion is made, supported, and
briefed. Confirm the current subdivision text in
`az-law-references` before relying on the points below:

- **Rule 7.1(a)** — a motion must be in writing (unless made
  during a hearing or trial), state the grounds on which it is
  based and the relief or order sought, and be **accompanied by a
  supporting memorandum** (memorandum of points and authorities)
  unless the motion type is exempt. The motion and its memorandum
  are typically presented as a single combined document.
- **Rule 7.1(d)** — oral argument. A party may include a
  **request for oral argument** at the foot of the motion or
  response (commonly "Oral argument requested"), but under Rule
  7.1(d) the court — subject to Rule 56(c)(1) — may decide the
  motion **without** oral argument even if argument is requested.
  Verify the current text and any local-rule or division practice
  on oral-argument requests.
- **Response and reply sequence** — Rule 7.1 sets the time to file
  a **response** and a **reply**, and the standard notice periods.
  Confirm the current day counts and compute the dates with
  `az-deadlines` (which applies Ariz. R. Civ. P. 6 time
  computation and the service add-ons).

A motion that presents an issue of fact must be supported by an
**affidavit or declaration** or other evidence (see
`az-draft-declaration`).

## Page limits and typography

Arizona sets motion **page limits by rule and by local rule** —
the limit and any chambers-copy or courtesy-copy requirement are
not embedded here. Check the applicable Ariz. R. Civ. P.
provision, the local rules of the filing Superior Court, and the
assigned division's procedures before finalizing. See
`az-statewide-format` and the venue overlay, and consult
`az-law-references` for the corpus of court rules and the
page-limit lookup. Do not hard-code a page count in a draft.

## Motion + memorandum + proposed-order structure

```
                  [Caption — see az-statewide-format]

         [DOCUMENT TITLE IN ALL CAPS, e.g.,
     DEFENDANT'S MOTION FOR SUMMARY JUDGMENT
     (Oral Argument Requested)]

[Movant], [Plaintiff / Defendant], by [counsel / in propria
persona] and pursuant to Ariz. R. Civ. P. 7.1 and [specific rule,
e.g., Ariz. R. Civ. P. 56], moves the Court for [specific relief].
The grounds for this Motion are stated below and in the supporting
Memorandum of Points and Authorities that follows.

         MEMORANDUM OF POINTS AND AUTHORITIES

                       I. INTRODUCTION
[1-2 paragraph summary of the case, the relief sought, and the
reasons in headline form.]

                  II. STATEMENT OF FACTS
[Numbered factual paragraphs. Each material fact gets a record
citation — Declaration/Affidavit ¶ X, Complaint ¶ X, Exhibit X,
deposition page/line, or admission in the pleadings. Sworn facts
belong in a declaration or affidavit; see az-draft-declaration.]

                  III. LEGAL ARGUMENT
A. [Headline of first argument.]
[Lead with the rule citation; state the controlling standard;
apply it to the facts; cite controlling Arizona authority.]

B. [Headline of second argument.]

                  IV. CONCLUSION AND RELIEF
For the foregoing reasons, [Movant] respectfully requests that the
Court [grant the relief sought] and sign the accompanying proposed
form of Order.

Oral argument requested. [Rule 7.1(d) — include if desired.]

                                     [Signature block —
                                      see az-statewide-format]
                                     [Certificate of service]
```

The **proposed form of order** is drafted as a **separate**
document and lodged with the motion — see `az-draft-order`.

## Summary judgment — Ariz. R. Civ. P. 56 and the *Orme School* standard

The most common dispositive motion in Arizona is the **motion for
summary judgment under Ariz. R. Civ. P. 56**. Summary judgment is
granted when there is **no genuine dispute as to any material
fact** and the moving party is entitled to **judgment as a matter
of law**; the court views the evidence in the light most favorable
to the party opposing the motion.

The governing Arizona standard is set out in **Orme School v.
Reeves, 166 Ariz. 301, 802 P.2d 1000 (1990)** (verify the citation
and the current case law refining it before relying on it).
*Orme School* holds that summary judgment is appropriate where the
facts produced in opposition to the motion have **so little
probative value, given the quantum of evidence required, that
reasonable people could not agree** with the conclusion advanced
by the proponent of the claim or defense — i.e., a mere "scintilla"
of evidence is not enough to defeat the motion. Once the movant
shows the absence of a genuine dispute, the nonmovant must come
forward with specific facts (not mere allegations) showing a
genuine issue for trial.

> A Rule 56 motion is typically accompanied by supporting
> **declarations or affidavits** and documentary exhibits (see
> `az-draft-declaration`), and many courts require a separately
> filed **statement of facts**. Confirm the current Rule 56 text
> and the filing court's statement-of-facts and separate-statement
> practice in `az-law-references`.

## Common motion types

| Motion | Rule | Notes |
|---|---|---|
| Motion for Summary Judgment | Ariz. R. Civ. P. 56 | *Orme School* standard; supporting declarations/exhibits; check statement-of-facts practice |
| Motion to Dismiss | Ariz. R. Civ. P. 12(b) | Including 12(b)(6) failure to state a claim |
| Motion to Compel Discovery | Ariz. R. Civ. P. 37 | Attach the deficient responses; satisfy the good-faith-consultation / Rule 7.1 requirement |
| Motion for New Trial / to Alter or Amend | Ariz. R. Civ. P. 59 | Verify the current time limit and grounds |
| Motion for Relief from Judgment | Ariz. R. Civ. P. 60 | Mistake, newly discovered evidence, fraud, void judgment, etc. |

## The pro-se drafting framework — applied to motions

Self-represented filers should follow the **pro-se drafting
framework** (see `az-pro-se`):

1. **State the relief clearly** in the opening sentence.
2. **Cite the rule** (Ariz. R. Civ. P. ____) that grants the court
   power to award that relief, per Rule 7.1(a).
3. **State the facts** that satisfy each element of the standard,
   with record citations to a supporting declaration.
4. **Apply the controlling Arizona case law** to those facts.
5. **Conclude** with the specific order sought, and lodge a
   proposed form of order (see `az-draft-order`).

## Filing checklist

- [ ] Caption matches the assigned court and county
- [ ] Title in ALL CAPS centered below the caption
- [ ] Grounds and relief stated; supporting memorandum included (Rule 7.1(a))
- [ ] Oral-argument request included if desired (Rule 7.1(d))
- [ ] Issues of fact supported by declaration/affidavit/evidence
- [ ] For Rule 56: no-genuine-dispute showing; supporting evidence and any required statement of facts attached
- [ ] All cited rules and authorities correct (run `az-fact-check`)
- [ ] Within any applicable rule / local-rule page limit
- [ ] Proposed form of Order drafted as a **separate** document (`az-draft-order`)
- [ ] Response/reply deadlines computed (`az-deadlines`)
- [ ] Certificate of service complete
- [ ] Format check passes (`scripts/format-check.py`)

## Composition

- For format, caption, and signature block: `az-statewide-format`
- For the supporting declaration/affidavit: `az-draft-declaration`
- For the proposed form of order: `az-draft-order`
- For the scheduling document / setting the hearing: `az-draft-note`,
  `az-schedule-hearing`
- For the venue overlay: `az-maricopa`, `az-pima`,
  `az-superior-courts`, `az-justice-courts`
- For pre-filing QC: `az-quality-check`, `az-fact-check`
- For deadline math: `az-deadlines`
- For pro se conventions: `az-pro-se`
- For the court-rules corpus and page-limit lookups:
  `az-law-references`

## References to author

- `references/motion-template.md` — annotated motion + memorandum
  + proposed-order template
- `references/summary-judgment-standard.md` — Ariz. R. Civ. P. 56
  + the *Orme School v. Reeves* standard
- `references/argument-structure.md` — pro-se drafting framework
  applied to an Arizona motion
