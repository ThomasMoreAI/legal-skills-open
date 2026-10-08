---
name: mi-draft-motion-codearranger
title: Draft a Michigan Motion
description: This skill should be used to scaffold a Michigan civil motion with its notice of hearing and supporting brief. Triggers include "draft a Michigan motion", "MCR 2.119 motion", "draft a Michigan motion for summary disposition", "motion for summary disposition MCR 2.116", "draft an MCR 2.116(C)(8) motion", "draft an MCR 2.116(C)(10) motion", "Michigan brief in support", "draft a Michigan motion to compel", and "draft a notice of hearing for a Michigan motion". Produces a motion plus notice of hearing plus supporting brief in Michigan format, applying the pro-se drafting framework (state the relief, cite the rule, state supporting facts, apply controlling Michigan authority, conclude). Composes with `mi-statewide-format` for the caption and signature, `mi-draft-declaration` for sworn facts, `mi-draft-order` for the proposed order, `mi-draft-note` for the notice of hearing, and the relevant venue overlay.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/mi-court-docs/skills/mi-draft-motion
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft a Michigan Motion

> **NOT LEGAL ADVICE.** This skill scaffolds a draft motion as a
> drafting aid. The user — not the skill — chooses the motion
> type, the theory of relief, and the strategy. Verify every
> rule, deadline, and citation against the current Michigan Court
> Rules and controlling case law before filing.

Use this skill to produce a **motion + notice of hearing +
supporting brief** in Michigan format. The form and content of
motions is governed by **MCR 2.119**. The caption, signature
block (with the attorney's State Bar **P-number**), and proof of
service follow `mi-statewide-format`.

## MCR 2.119 — form and content of motions

**MCR 2.119(A)** governs the motion itself:

- **MCR 2.119(A)(1)** — a motion must be in writing (unless made
  during a hearing or trial), state with particularity the grounds
  and authority on which it is based, and state the relief or
  order sought.
- **MCR 2.119(A)(2)** — a **separate brief** supporting a motion
  or response is **required** for certain motions (notably motions
  brought under MCR 2.116 — summary disposition), and the brief
  must be filed and served with the motion or response. For other
  motions a brief may be filed but is not required. Verify the
  current text of MCR 2.119(A)(2) for which motion types require
  the separate brief.
- **MCR 2.119(A)(3)** — a motion or response that presents an
  issue of fact must be supported by an **affidavit** or other
  evidence (see `mi-draft-declaration`).

**MCR 2.119(C)** sets the timing for serving and filing a written
motion and any response (the standard notice period and the
response deadline) — confirm the current periods and compute the
dates with `mi-deadlines`.

**MCR 2.119(E)** addresses hearings on motions and when a court
may dispense with oral argument.

## Page limits and typography

Michigan does not set a single universal motion page limit in MCR
2.119; **page limits, line spacing, and chambers-copy or
courtesy-copy requirements are commonly set by LOCAL court rules
(LCR) and the assigned judge's practice guidelines**. Check the
local rules of the filing court and the judge's standing orders
before finalizing. Do not hard-code a page count here — see
`mi-statewide-format` and the venue overlay, and consult
`mi-law-references` for the corpus of court rules.

## Motion + notice of hearing + brief structure

```
                  [Caption — see mi-statewide-format]

         [DOCUMENT TITLE IN ALL CAPS, e.g.,
     DEFENDANT'S MOTION FOR SUMMARY DISPOSITION
     PURSUANT TO MCR 2.116(C)(10)]

[Movant], [Plaintiff / Defendant], by [counsel / in propria
persona], pursuant to MCR 2.119 and MCR [specific rule, e.g.,
2.116(C)(10)], moves the Court for [specific relief]. The grounds
and authority for this Motion are stated with particularity below
and in the accompanying Brief in Support:

1. [Ground one — particular statement of fact + authority.]

2. [Ground two.]

WHEREFORE, [Movant] respectfully requests that the Court [grant
the relief sought] and enter the accompanying proposed Order.

                                     [Signature block —
                                      see mi-statewide-format]
```

### Notice of hearing

```
                  [Caption — see mi-statewide-format]

                       NOTICE OF HEARING

TO: [opposing party / counsel]
PLEASE TAKE NOTICE that the foregoing Motion will be brought on
for hearing before the Honorable [Judge] on [date] at [time], or
as soon thereafter as counsel may be heard.
                                     [Signature block]
```
See `mi-draft-note` and `mi-schedule-hearing` for the notice and
date-setting mechanics.

### Brief in support

```
                  [Caption — see mi-statewide-format]

     BRIEF IN SUPPORT OF DEFENDANT'S MOTION FOR
     SUMMARY DISPOSITION

                       I. INTRODUCTION
[1-2 paragraph summary of the case, the relief sought, and the
reasons in headline form.]

                  II. STATEMENT OF FACTS
[Numbered factual paragraphs. Each material fact gets a record
citation — Affidavit ¶ X, Complaint ¶ X, Exhibit X, deposition
page/line, or admission in pleadings. Sworn facts belong in an
affidavit; see mi-draft-declaration.]

                  III. STANDARD OF REVIEW
[State the governing standard for the motion type — e.g., the
applicable MCR 2.116 subrule standard described below.]

                       IV. ARGUMENT
A. [Headline of first argument.]
[Lead with the rule citation; state the controlling standard;
apply it to the facts; cite controlling Michigan authority.]

B. [Headline of second argument.]

                       V. RELIEF REQUESTED
For the foregoing reasons, [Movant] respectfully requests that the
Court [grant the motion] and enter the accompanying proposed Order.
                                     [Signature block]
```

## Summary disposition — MCR 2.116 and the *Maiden* standard

The most common dispositive motion in Michigan is the **motion for
summary disposition under MCR 2.116(C)**, with the ground
identified by subrule:

- **MCR 2.116(C)(7)** — the claim is barred (e.g., release, prior
  judgment, statute of limitations, immunity, prior pending
  action). The court considers the pleadings plus any affidavits,
  depositions, admissions, or documentary evidence; well-pleaded
  factual allegations are accepted as true unless contradicted by
  the documentary evidence.
- **MCR 2.116(C)(8)** — failure to state a claim on which relief
  can be granted. Tested on the **pleadings alone**; the motion is
  granted only if the claim is so clearly unenforceable that no
  factual development could justify recovery.
- **MCR 2.116(C)(10)** — no genuine issue of material fact and the
  moving party is entitled to judgment as a matter of law. Tested
  on the pleadings **and the documentary evidence** submitted; the
  evidence is viewed in the light most favorable to the nonmoving
  party.

The governing standard is set out in **Maiden v Rozwood, 461 Mich
109; 597 NW2d 817 (1999)** (verify the citation and the current
case law refining it before relying on it). *Maiden* describes the
distinct evidentiary tests for (C)(8) vs. (C)(10): a (C)(8) motion
is decided on the pleadings, while a (C)(10) motion requires the
court to consider the substantively admissible evidence and,
where the moving party meets its initial burden, shifts to the
nonmovant to set forth specific facts showing a genuine issue for
trial — the nonmovant may not rest on mere allegations.

> A (C)(10) motion is typically accompanied by supporting
> **affidavits** and documentary exhibits (see
> `mi-draft-declaration`); MCR 2.116(G) governs the supporting and
> opposing materials and the timing. Confirm the current subrule
> text.

## Common motion types

| Motion | Rule | Notes |
|---|---|---|
| Motion for Summary Disposition | MCR 2.116(C)(7)/(8)/(10) | *Maiden* standard; separate brief required (MCR 2.119(A)(2)); (C)(8) on pleadings, (C)(10) on evidence |
| Motion to Compel Discovery | MCR 2.313 | Attach the deficient responses; check the local-rule meet-and-confer / concurrence requirement |
| Motion for Reconsideration | MCR 2.119(F) | Within **21 days** of the order; must show palpable error (verify current text) |
| Motion for Relief from Judgment | MCR 2.612 | Mistake, newly discovered evidence, fraud, void judgment, etc. |
| Motion in Limine | (inherent / MRE) | Pre-trial; anticipated evidentiary disputes |

## The pro-se drafting framework — applied to motions

Self-represented filers should follow the **pro-se drafting
framework** (see `mi-pro-se`):

1. **State the relief clearly** in the opening sentence.
2. **Cite the rule** (MCR ____) that grants the court power to
   award that relief, with particularity per MCR 2.119(A)(1).
3. **State the facts** that satisfy each element of the standard,
   with record citations to a supporting affidavit.
4. **Apply the controlling Michigan case law** to those facts.
5. **Conclude** with the specific order sought, and attach a
   proposed Order (see `mi-draft-order`).

## Filing checklist

- [ ] Caption matches the assigned court and county
- [ ] Title in ALL CAPS centered below the caption
- [ ] Grounds, authority, and relief stated with particularity (MCR 2.119(A)(1))
- [ ] Separate Brief in Support filed where required (MCR 2.119(A)(2))
- [ ] Issues of fact supported by affidavit/evidence (MCR 2.119(A)(3))
- [ ] For MCR 2.116: correct (C) subrule identified; supporting evidence attached for (C)(10)
- [ ] All cited rules and authorities correct (run `mi-fact-check`)
- [ ] Within any applicable local-rule page limit
- [ ] Proposed Order drafted as a **separate** document (`mi-draft-order`)
- [ ] Notice of Hearing prepared (`mi-draft-note`, `mi-schedule-hearing`)
- [ ] Proof of Service complete (MCR 2.107)
- [ ] Format check passes (`scripts/format-check.py`)

## Composition

- For format, caption, and signature block: `mi-statewide-format`
- For the supporting affidavit: `mi-draft-declaration`
- For the proposed order: `mi-draft-order`
- For the notice of hearing / setting the hearing: `mi-draft-note`,
  `mi-schedule-hearing`
- For the venue overlay: `mi-wayne`, `mi-oakland`,
  `mi-circuit-courts`, `mi-district-courts`, `mi-36th-district`
- For pre-filing QC: `mi-quality-check`, `mi-fact-check`
- For deadline math: `mi-deadlines`
- For pro se conventions: `mi-pro-se`
- For the court-rules corpus and page-limit lookups:
  `mi-law-references`

## References to author

- `references/motion-template.md` — annotated motion + notice +
  brief template
- `references/summary-disposition-standard.md` — MCR 2.116(C)
  subrules + the *Maiden v Rozwood* standard
- `references/argument-structure.md` — pro-se drafting framework
  applied to a Michigan motion
