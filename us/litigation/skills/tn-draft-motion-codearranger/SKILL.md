---
name: tn-draft-motion-codearranger
title: Draft a Tennessee Motion
description: This skill should be used to scaffold a Tennessee civil motion with its supporting memorandum of law. Triggers include "draft a motion in Tennessee", "draft a Tennessee motion to compel", "draft a Tenn. R. Civ. P. 12.02(6) motion to dismiss", "Tennessee motion for summary judgment", "draft a Rule 56 motion in Tennessee", "draft a motion to alter or amend under Rule 59.04", "draft a Tennessee motion in limine", "draft a memorandum of law for a Tennessee motion". Produces a motion plus supporting memorandum in the Tennessee statewide format applying the pro-se drafting framework (clear relief, cite the rule or statute, state supporting facts, conclude with signature and certificate of service). Composes with `tn-statewide-format` for the caption and signature, `tn-draft-declaration` for sworn facts, `tn-draft-order` for the proposed order, `tn-draft-note` for the Notice of Hearing, and the relevant venue overlay.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tn-court-docs/skills/tn-draft-motion
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft a Tennessee Motion

> **NOT LEGAL ADVICE.** This skill scaffolds a draft motion. The
> filer is responsible for verifying the underlying law and the
> rule's applicability to the facts of the case before filing.

Use this skill to produce a motion + supporting memorandum of law in
Tennessee format. Most Tennessee motions follow **Tenn. R. Civ. P.
7.02** (form of motions — state the grounds and the relief sought)
plus the specific rule under which the motion is filed (Rule 12.02,
Rule 56, Rule 37, Rule 59, Rule 60, etc.). The caption, signature
block, and certificate of service follow `tn-statewide-format`.

These conventions apply in **Circuit** and **Chancery** courts, where
the Tennessee Rules of Civil Procedure govern. **General Sessions**
courts are informal and the Rules of Civil Procedure do not apply
there except where specifically made applicable — do not assume formal
written motion practice in General Sessions (see `tn-general-sessions`).

## Page limits and typography

Tennessee has **no single statewide page-limit, margin, or font rule**.
Form is governed by Tenn. R. Civ. P. 10 (caption, numbered paragraphs,
exhibits) and Rule 11 (signature). **Page limits, margins, font, and
chambers-copy requirements are set by per-county LOCAL RULES** — check
the local rules of the filing court (indexed on the AOC "Local Rules
of Practice" page at tncourts.gov) and the assigned judge's standing
orders before finalizing. See `tn-statewide-format`.

## Motion + memorandum structure

Tennessee practice commonly pairs a short **motion** (stating the
relief and grounds per Rule 7.02) with a separate or appended
**memorandum of law** (the legal argument). Some courts permit a
combined document; many local rules expect a discrete memorandum.
Verify the local rule of the filing court.

```
                    [Caption — see tn-statewide-format]

           [DOCUMENT TITLE IN ALL CAPS, e.g.,
       DEFENDANT'S MOTION TO DISMISS PURSUANT TO
       TENN. R. CIV. P. 12.02(6)]

[Movant], [Plaintiff / Defendant], pursuant to Tenn. R. Civ. P.
[rule], respectfully moves the Court for [specific relief]. The
grounds for this Motion are as follows and are more fully set out in
the accompanying Memorandum of Law:

1. [Ground one — short, particular statement.]

2. [Ground two.]

WHEREFORE, [Movant] respectfully requests that the Court [grant the
relief sought] and enter the accompanying proposed Order.

                                        [Signature block —
                                         see tn-statewide-format]

                       CERTIFICATE OF SERVICE
[Date, method, recipients — per tn-statewide-format and Rule 5]
```

### Supporting memorandum of law

```
                    [Caption — see tn-statewide-format]

       MEMORANDUM OF LAW IN SUPPORT OF DEFENDANT'S
       MOTION TO DISMISS

                       I. INTRODUCTION

[1-2 paragraph summary of the case, the relief sought, and the
reasons in headline form.]

                  II. STATEMENT OF FACTS

[Numbered factual paragraphs. Each material fact gets a record
citation — Affidavit ¶ X, Complaint ¶ X, Exhibit X, or admission in
pleadings. Sworn facts belong in an affidavit; see
tn-draft-declaration.]

                  III. STANDARD OF REVIEW

[State the governing standard for this motion type — e.g., the Rule
12.02(6) failure-to-state-a-claim standard, or the Rule 56 / Rye
summary-judgment standard described below.]

                       IV. ARGUMENT

A. [Headline of first argument.]

[Lead with the rule or statute citation; state the controlling
standard; apply it to the facts; cite controlling Tennessee
authority.]

B. [Headline of second argument.]

                       V. CONCLUSION

For the foregoing reasons, [Movant] respectfully requests that the
Court [grant the motion] and enter the accompanying proposed Order.

                                        [Signature block]

                       CERTIFICATE OF SERVICE
[Per tn-statewide-format and Rule 5]
```

## Summary judgment — Rule 56 and the *Rye* standard

A motion for summary judgment is governed by **Tenn. R. Civ. P. 56**
and the standard in **Rye v. Women's Care Center of Memphis, MPLLC,
477 S.W.3d 235 (Tenn. 2015)**. In *Rye* the Tennessee Supreme Court
restored the federal *Celotex*-style standard (overruling the earlier
plaintiff-friendly *Hannan* standard), consistent with the legislative
influence of **Tenn. Code Ann. § 20-16-101**. Under *Rye*, a moving
party who does not bear the burden of proof at trial may obtain summary
judgment by either:

1. **Affirmatively negating an essential element** of the nonmoving
   party's claim or defense; **OR**
2. **Demonstrating that the nonmoving party's evidence is
   insufficient** as a matter of law to establish an essential
   element of its claim or defense.

Once the movant makes this showing, the burden shifts: the nonmoving
party must, by affidavit or other Rule 56 materials, set forth
specific facts showing a genuine dispute for trial — it cannot rest on
the pleadings.

**Timing — Rule 56.04**: the summary-judgment motion must be **served
at least 30 days before the time fixed for the hearing**, and the
adverse party may serve a response no later than **5 days before the
hearing** (verify the current rule text and any local-rule variation,
and use `tn-deadlines` to compute the dates). Rule 56 also requires the
order granting summary judgment to **state the legal grounds** on which
the court grants the motion.

> A Rule 56 motion is typically accompanied by a **statement of
> undisputed material facts** with citations to the record (verify the
> local rule's exact format) and supporting affidavits (see
> `tn-draft-declaration`).

## Motion to dismiss — Rule 12.02(6) and the § 20-12-119(c) fee cap

A motion to dismiss for failure to state a claim is brought under
**Tenn. R. Civ. P. 12.02(6)** (one of the eight Rule 12.02 defenses).
If matters outside the pleadings are presented and not excluded by the
court, a 12.02(6) motion is **converted to a Rule 56 summary-judgment
motion** and the parties get a reasonable opportunity to present Rule
56 materials.

> ⚠ **Fee-and-cost exposure — Tenn. Code Ann. § 20-12-119(c).** When a
> trial court grants a motion to dismiss under Rule 12.02(6) for
> failure to state a claim, the prevailing party may be awarded
> reasonable costs and **attorney's fees, capped at $10,000**, against
> the non-prevailing party. A pro se filer considering a 12.02(6)
> motion — or defending against one — should be aware of this
> Tennessee-specific fee-shifting exposure. Verify the statute's
> current text and the case law construing its scope before relying on
> it.

## Common motion types

| Motion | Rule | Notes |
|---|---|---|
| Motion to Dismiss | Tenn. R. Civ. P. 12.02(6) | Failure to state a claim; converts to Rule 56 if outside matter considered; § 20-12-119(c) $10,000 fee cap |
| Motion for Summary Judgment | Tenn. R. Civ. P. 56 | *Rye* standard; serve >= 30 days before hearing (Rule 56.04); order must state legal grounds |
| Motion to Compel | Tenn. R. Civ. P. 37 | Attach the deficient responses; check local-rule meet-and-confer requirement |
| Motion to Alter or Amend | Tenn. R. Civ. P. 59.04 | Within **30 days** of entry, **non-extendable**; tolls the time to appeal |
| Motion for Relief from Judgment | Tenn. R. Civ. P. 60.02 | Mistake / excusable neglect / newly discovered evidence / fraud / void / satisfied; (1)-(2) within a reasonable time, not more than one year |
| Motion in Limine | (inherent / Tenn. R. Evid.) | Pre-trial; anticipated evidentiary disputes |
| Motion for Extension of Time | Tenn. R. Civ. P. 6.02 | Typically routine; note Rule 59 motions are non-extendable |

## The pro-se drafting framework — applied to motions

Self-represented filers should follow the **pro-se drafting framework**
(see `tn-pro-se`):

1. **State the relief clearly** in the opening sentence.
2. **Cite the rule or statute** (Tenn. R. Civ. P. ____ / Tenn. Code
   Ann. § ____) that grants the court power to award that relief.
3. **State the facts** that satisfy each element of the standard,
   with record citations to a supporting affidavit.
4. **Apply the controlling Tennessee case law** to those facts.
5. **Conclude** with the specific order sought, and attach a proposed
   Order (see `tn-draft-order`).

## Filing checklist

- [ ] Caption matches the assigned court (Circuit / Chancery) and county
- [ ] Title in ALL CAPS centered below the caption
- [ ] Grounds and relief stated per Rule 7.02
- [ ] All cited rules and statutes correct (run `tn-fact-check`)
- [ ] For Rule 56: served >= 30 days before hearing; statement of
      undisputed facts; supporting affidavit(s)
- [ ] Within any applicable local-rule page limit
- [ ] Proposed Order drafted as a **separate** document (`tn-draft-order`)
- [ ] Supporting affidavit(s) drafted (`tn-draft-declaration`)
- [ ] Notice of Hearing prepared if required (`tn-draft-note`,
      `tn-schedule-hearing`)
- [ ] Certificate of Service complete (Rule 5)
- [ ] Format check passes (`scripts/format-check.py`)

## Composition

- For format, caption, and signature block: `tn-statewide-format`
- For the supporting affidavit: `tn-draft-declaration`
- For the proposed order: `tn-draft-order`
- For setting the hearing: `tn-draft-note`, `tn-schedule-hearing`
- For the venue overlay: `tn-davidson`, `tn-shelby`, `tn-knox`,
  `tn-hamilton`, `tn-county-courts`, `tn-general-sessions`
- For pre-filing QC: `tn-quality-check`, `tn-fact-check`
- For deadline math: `tn-deadlines`
- For pro se conventions: `tn-pro-se`

## References

- `references/motion-template.md` — annotated motion + memorandum template
- `references/rule-56-rye-standard.md` — *Rye* summary-judgment standard
- `references/argument-structure.md` — pro-se drafting framework applied
