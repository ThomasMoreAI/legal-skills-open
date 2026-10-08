---
name: tx-draft-motion-codearranger
title: Draft a Texas Motion
description: This skill should be used to scaffold a Texas civil motion with its supporting argument, the relief sought, a Notice of Hearing, and a proposed order. Triggers include "draft a Texas motion", "TRCP 21 motion", "Rule 21 motion Texas", "draft a Texas motion for summary judgment", "no-evidence motion for summary judgment Texas", "Rule 166a motion", "motion to dismiss Texas Rule 91a", "Rule 91a motion no basis in law", "special exceptions motion Texas", "set my motion on submission", "Texas motion for hearing". Produces a motion plus the relief sought plus a Notice of Hearing plus a proposed order in Texas format, applying the pro-se drafting framework (state the relief, cite the rule, state supporting facts, apply controlling Texas authority, conclude). Composes with `tx-statewide-format`, `tx-draft-declaration` for sworn facts (affidavit or CPRC § 132.001 declaration), `tx-draft-note`, `tx-draft-order`, and the venue overlay.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tx-court-docs/skills/tx-draft-motion
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft a Texas Motion

> **NOT LEGAL ADVICE.** This skill scaffolds a draft motion as a
> drafting aid. The user — not the skill — chooses the motion
> type, the theory of relief, and the strategy. Verify every rule,
> deadline, and citation against the current Texas Rules of Civil
> Procedure and controlling case law before filing.

Use this skill to produce a **motion + the relief sought + a Notice
of Hearing + a proposed order** in Texas format. The filing and form
of motions are governed by **Tex. R. Civ. P. 21** and **21a**. The
caption, signature block (with the **State Bar of Texas** bar number
where counsel signs, per Tex. R. Civ. P. 57), and certificate of
service follow `tx-statewide-format`.

## Tex. R. Civ. P. 21 / 21a — filing and service of motions

**Rule 21** governs how an application to the court for an order
(a motion) is made and served; **Rule 21a** governs the methods of
service and the service add-on days. Confirm the current text in
`tx-law-references` before relying on the points below:

- **Tex. R. Civ. P. 21** — a motion (other than one made during a
  hearing or trial) must be **in writing**, state the **grounds**
  and the **relief or order sought**, be **filed with the clerk**,
  and be **served on all other parties**. A certificate of service
  is required.
- **Tex. R. Civ. P. 21(b)** — unless otherwise required, a motion
  and notice of any hearing on it must be **served at least three
  days before the time specified for the hearing** (confirm the
  current floor in `tx-law-references`).
- **Tex. R. Civ. P. 21(f)** — electronic filing is **mandatory**
  for those required to e-file and e-service is the default method
  for e-filers (see `tx-file-packet` for eFileTexas mechanics).
- **Tex. R. Civ. P. 21a** — sets the service methods (e-service,
  mail, commercial delivery, fax, in person) and the **service
  add-on days** (the +3-day add-on for service by mail / commercial
  delivery / fax / email; the exact triggers are drift-prone —
  point to `tx-law-references` and compute with `tx-deadlines`).

## How a Texas motion gets decided — submission vs. oral hearing

A Texas trial court may decide many motions in one of two ways, and
the **assigned court's local rules and the judge's practice control**
which:

- **By submission** — the court rules on the papers without an oral
  hearing. The Notice of Hearing sets a **submission date** by which
  responses are due and after which the court may rule. Most routine,
  non-evidentiary motions are decided on submission.
- **By oral hearing** — the court sets the motion for argument on a
  date and time. Dispositive and evidentiary motions are commonly set
  for an oral hearing.

Either way, the moving party prepares and serves a **Notice of
Hearing** (see `tx-draft-note`) that states the submission date or
the hearing date, time, and location. Reserve the setting through the
court coordinator before noticing it — see `tx-schedule-hearing`.

## Caption and party designations

In a general civil action the parties are **Plaintiff** and
**Defendant**; in a family-law matter they are **Petitioner** and
**Respondent**. The initiating pleading is the **Original Petition**
and the responsive pleading is the **Original Answer**. The caption
gives the names of the parties, the court (e.g., "In the [Nth]
Judicial District Court of [County] County, Texas"), the cause
number, and the document title. See `tx-statewide-format` for the
caption recipe and `tx-family-court` for family-matter designations.

## Page formatting and line numbering

Each generated document uses line-numbered pleading paper and a
footer carrying the document title and "Page X of Y". Defer the full
recipe (margins, font, spacing) to `tx-statewide-format`; do not
hard-code measurements here.

## Motion + relief + Notice + proposed-order structure

```
                  [Caption — see tx-statewide-format]

         [DOCUMENT TITLE IN ALL CAPS, e.g.,
     DEFENDANT'S MOTION FOR SUMMARY JUDGMENT]

TO THE HONORABLE JUDGE OF SAID COURT:

[Movant], [Plaintiff / Defendant] in the above-styled and numbered
cause, files this [Motion Title] pursuant to Tex. R. Civ. P. [rule]
and respectfully shows the Court as follows:

                  I. INTRODUCTION / SUMMARY
[1-2 paragraph summary of the case, the relief sought, and the
grounds in headline form.]

                  II. FACTS
[Numbered factual paragraphs. Each material fact gets a record
citation — Affidavit/Declaration ¶ X, Original Petition ¶ X,
Exhibit X, deposition page/line, or admission. Sworn facts belong
in an affidavit or unsworn declaration; see tx-draft-declaration.]

                  III. ARGUMENT & AUTHORITIES
A. [Headline of first argument.]
[Lead with the rule/statute citation; state the controlling
standard; apply it to the facts; cite controlling Texas authority.]

B. [Headline of second argument.]

                  IV. PRAYER
WHEREFORE, [Movant] respectfully requests that the Court [grant the
specific relief], and grant such other and further relief to which
[Movant] is justly entitled.

                                     [Signature block —
                                      see tx-statewide-format]
                                     [Certificate of service]
```

The **Notice of Hearing** is a separate document (see
`tx-draft-note`); the **proposed order** is a separate document (see
`tx-draft-order`).

## Summary judgment — Tex. R. Civ. P. 166a

Texas recognizes **two** summary-judgment vehicles, and the timing
track **overrides** the ordinary 3-day motion notice — confirm the
current figures in `tx-law-references` and compute with
`tx-deadlines`:

- **Traditional summary judgment, Tex. R. Civ. P. 166a(c)** — the
  movant shows there is **no genuine issue of material fact** and it
  is **entitled to judgment as a matter of law**. The motion and any
  supporting affidavits are **served at least 21 days before** the
  hearing or submission date; the **response is due 7 days before**
  the hearing (with leave for late filing). Supporting evidence is
  presented by **affidavit or unsworn declaration** made on personal
  knowledge (see `tx-draft-declaration`).
- **No-evidence summary judgment, Tex. R. Civ. P. 166a(i)** — after
  an adequate time for discovery, the movant asserts that there is
  **no evidence** of one or more essential elements of a claim or
  defense on which the **non-movant** bears the burden of proof. The
  motion must **state the specific elements** as to which there is no
  evidence; the non-movant must then produce **more than a scintilla**
  of summary-judgment evidence raising a genuine fact issue. The same
  21-day / 7-day timing track applies.

> A traditional 166a(c) motion is supported by **affidavits or
> unsworn declarations made on personal knowledge** and documentary
> exhibits (see `tx-draft-declaration`). A no-evidence 166a(i) motion
> is built on pointing to the absence of evidence and need not attach
> evidence. Confirm the current Rule 166a text in `tx-law-references`.

## Rule 91a — dismissal of a baseless cause of action

**Tex. R. Civ. P. 91a** authorizes a **motion to dismiss a cause of
action that has no basis in law or fact**. Key features (confirm the
current text in `tx-law-references`):

- The motion must **identify each challenged cause of action** and
  state specifically why it has no basis in law and/or no basis in
  fact.
- It must be filed **within 60 days after the first pleading
  containing the challenged cause of action** is served.
- The court rules on the motion based **solely on the pleading** of
  the challenged cause of action, together with any pleading
  exhibits — **not** on evidence outside the pleadings.
- A fee-shifting provision applies; whether the award is mandatory
  or discretionary turns on the current statutory text — point to
  `tx-law-references`.

Rule 91a is the Texas vehicle for a pure pleadings-stage dismissal.
For a defect in the **form or particularity** of a pleading (rather
than a claim with no basis), the device is **special exceptions
under Tex. R. Civ. P. 91** — Texas has **no general demurrer**.

## Common motion types

| Motion | Rule / authority | Notes |
|---|---|---|
| Traditional Motion for Summary Judgment | Tex. R. Civ. P. 166a(c) | 21-day / 7-day timing track; supporting affidavits/declarations and exhibits |
| No-Evidence Motion for Summary Judgment | Tex. R. Civ. P. 166a(i) | State the specific no-evidence elements; same 21/7 timing track |
| Motion to Dismiss (no basis in law/fact) | Tex. R. Civ. P. 91a | File within 60 days of the challenged pleading; decided on the pleadings |
| Special Exceptions | Tex. R. Civ. P. 91 | Challenges defects/vagueness in a pleading; no general demurrer in Texas |
| Motion to Compel Discovery | Tex. R. Civ. P. 215 | Attach the deficient responses; satisfy any meet-and-confer requirement |
| Motion for New Trial | Tex. R. Civ. P. 320–329b | Due within 30 days after the judgment is signed (Rule 329b); plenary-power implications |
| Motion to Transfer Venue | Tex. R. Civ. P. 86–87 | File before or with the answer; verify the timing requirement |

## The pro-se drafting framework — applied to motions

Self-represented filers should follow the **pro-se drafting
framework** (see `tx-pro-se`):

1. **State the relief clearly** in the opening sentence.
2. **Cite the rule** (Tex. R. Civ. P. ____) or statute that grants
   the court power to award that relief, and state the grounds.
3. **State the facts** that satisfy each element of the standard,
   with record citations to a supporting affidavit or unsworn
   declaration (see `tx-draft-declaration`).
4. **Apply the controlling Texas case law** to those facts.
5. **Conclude with a PRAYER** for the specific order sought, and
   tender a proposed order (see `tx-draft-order`).

## Filing checklist

- [ ] Caption matches the assigned court and county; cause number correct
- [ ] Title in ALL CAPS centered below the caption
- [ ] Grounds and relief stated; "TO THE HONORABLE JUDGE" opener; PRAYER closes
- [ ] Decision mode chosen (submission vs. oral hearing) per the court's local rules
- [ ] Notice of Hearing prepared; served at least the required days before the setting (Rule 21(b)) — see `tx-draft-note`
- [ ] Questions of fact supported by affidavit / unsworn declaration / evidence (`tx-draft-declaration`)
- [ ] For Rule 166a: traditional vs. no-evidence chosen; 21-day / 7-day timing track confirmed; no-evidence motion states the specific elements
- [ ] For Rule 91a: filed within 60 days of the challenged pleading; rests on the pleadings only
- [ ] All cited rules and authorities correct (run `tx-fact-check`)
- [ ] Proposed order drafted as a **separate** document (`tx-draft-order`)
- [ ] Hearing/submission and response deadlines computed (`tx-deadlines`)
- [ ] Certificate of service complete (Tex. R. Civ. P. 21a)
- [ ] Format check passes (`scripts/format-check.py`)

## Composition

- For format, caption, and signature block: `tx-statewide-format`
- For the supporting affidavit / unsworn declaration: `tx-draft-declaration`
- For the Notice of Hearing: `tx-draft-note`, `tx-schedule-hearing`
- For the proposed order: `tx-draft-order`
- For the venue overlay: `tx-hcdc`, `tx-dcdc`, `tx-county-courts`,
  `tx-family-court`
- For pre-filing QC: `tx-quality-check`, `tx-fact-check`
- For deadline math: `tx-deadlines`
- For pro se conventions: `tx-pro-se`
- For the court-rules and statute corpus: `tx-law-references`

## References to author

- `references/motion-template.md` — annotated motion + Notice of
  Hearing + proposed-order template
- `references/summary-judgment-standard.md` — Tex. R. Civ. P. 166a
  traditional vs. no-evidence standards and the 21-day / 7-day track
- `references/argument-structure.md` — pro-se drafting framework
  applied to a Texas motion
