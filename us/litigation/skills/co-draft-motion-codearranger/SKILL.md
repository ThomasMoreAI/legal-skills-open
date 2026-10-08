---
name: co-draft-motion-codearranger
title: Draft a Colorado Motion
description: This skill should be used to scaffold a Colorado civil motion with its supporting memorandum. Triggers include "draft a motion in Colorado", "draft a Colorado motion to compel", "draft a C.R.C.P. 12(b)(5) motion to dismiss", "Colorado motion for summary judgment", "draft a motion under C.R.C.P. 60(b)", "draft a Colorado motion in limine", "draft a C.R.C.P. 121 § 1-15 motion". Produces a motion plus supporting memorandum in the Colorado statewide format applying the pro-se drafting framework (clear relief, cite the rule or statute, state supporting facts, conclude with signature and required certificates). Composes with `co-statewide-format` for format, `co-draft-declaration` for sworn facts, `co-draft-order` for the proposed order, and the relevant court overlay.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/co-court-docs/skills/co-draft-motion
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft a Colorado Motion

> **NOT LEGAL ADVICE.** This skill scaffolds a draft motion. The
> filer is responsible for verifying the underlying law and the
> rule's applicability to the facts of the case.

Use this skill to produce a motion + supporting memorandum in
Colorado format. Most Colorado motions follow C.R.C.P. 121 § 1-15
(motion practice generally) plus the rule under which the motion is
filed (12(b)(5), 56, 60(b), 37(a), etc.).

## Page limits — C.R.C.P. 121 § 1-15(1)(a)

| Document | Limit |
|----------|-------|
| Motion / response | 15 pages |
| Reply | 10 pages |

Excess pages require **leave of court**, sought by separate motion.
Many divisions require a **chambers copy** for motions exceeding 20-25
pages — check the assigned judge's practice standards.

## Standard motion structure

```
                    [Caption — see co-statewide-format]

           [DOCUMENT TITLE IN ALL CAPS, e.g.,
       DEFENDANT'S MOTION TO DISMISS UNDER C.R.C.P. 12(b)(5)]

[Movant], [Plaintiff / Defendant], by and through [counsel /
self-represented], respectfully moves the Court for [specific
relief], and in support states:

                       I. INTRODUCTION

[1-2 paragraph summary of the case, the relief sought, and the
reasons in headline form]

                  II. STATEMENT OF FACTS

[Numbered factual paragraphs. Each material fact gets its own
paragraph, with a citation to the record — declaration ¶ X,
Complaint ¶ X, Exhibit X, or admission in pleadings.]

                       III. ARGUMENT

A. [Headline of first argument]

[Argument body. Lead with the rule or statute citation; state the
controlling standard; apply to the facts; cite the controlling case
authority.]

B. [Headline of second argument]

[...]

                       IV. CONCLUSION

For the foregoing reasons, [Movant] respectfully requests that the
Court [grant the motion / grant the relief sought] and [enter the
attached Proposed Order].

                  CERTIFICATE OF CONFERRAL
                  (C.R.C.P. 121 § 1-15(8))

Pursuant to C.R.C.P. 121 § 1-15(8), the undersigned conferred with
[opposing counsel / opposing party] on [date] regarding the relief
requested in this Motion. [Opposing counsel] [opposes / does not
oppose / takes no position on] this Motion.

[OR for dispositive motions — exempt:]
Pursuant to C.R.C.P. 121 § 1-15(8)(b), conferral is not required for
motions under C.R.C.P. 12(b) and C.R.C.P. 56.

Respectfully submitted this ___ day of __________, 20__.

                                        [Signature block]
                                        [Reg. No. if attorney /
                                         "Self-Represented" if pro se]

                   CERTIFICATE OF SERVICE
[Date], method, recipients — per co-statewide-format]
```

## Filing checklist

When the motion is finalized:

- [ ] Caption matches the assigned court, division, courtroom
- [ ] Title in ALL CAPS centered between caption and body
- [ ] All cited rules and statutes correct (run `co-fact-check`)
- [ ] Affirmative defenses and counter-arguments addressed
- [ ] Within page limit (15 pages for motion / response)
- [ ] Certificate of Conferral included (or exempt-citation invoked)
- [ ] Proposed Order drafted as **separate** document (see
      `co-draft-order`)
- [ ] Supporting Declaration(s) drafted (see `co-draft-declaration`)
- [ ] Certificate of Service complete
- [ ] Format check passes (`scripts/format-check.py`)

## Common motion types

| Motion | Rule | Notes |
|---|---|---|
| Motion to Dismiss | C.R.C.P. 12(b)(5) | Plausibility standard under *Warne v. Hall*, 2016 CO 50; no conferral required |
| Motion for Summary Judgment | C.R.C.P. 56 | Must be filed >= 91 days before trial; affidavits showing no genuine issue of material fact |
| Motion to Compel | C.R.C.P. 37(a) | Conferral required (C.R.C.P. 121 § 1-15(8)); attach the deficient responses |
| Motion to Set Aside Default | C.R.C.P. 55(c) / 60(b) | Within 182 days for 60(b)(1)-(3); show good cause + meritorious defense |
| Motion for Reconsideration | C.R.C.P. 59 | Within 14 days of judgment |
| Motion in Limine | (inherent) | Pre-trial; addresses anticipated evidentiary disputes |
| Motion for Protective Order | C.R.C.P. 26(c) | Discovery-shielding |
| Motion for Extension of Time | C.R.C.P. 6(b) | Conferral required; typically routine |

## Argument structure — the Parker approach

Pro se filers should follow the **pro-se drafting framework**:

1. **State the relief clearly** in the opening sentence
2. **Cite the rule or statute** that grants the court power to award
   that relief
3. **State the facts** that satisfy each element of the standard
4. **Apply the controlling case law** to those facts
5. **Conclude** with the specific order sought

A motion that hides the relief, buries the rule citation, or omits a
clear element-by-element factual showing is the kind of filing the
court will struggle to engage with — Parker requires liberal
construction, but the court will not draft the argument for you.

## Composition

- For format: `co-statewide-format`
- For the supporting declaration: `co-draft-declaration`
- For the proposed order: `co-draft-order`
- For setting the hearing: `co-schedule-hearing`, `co-draft-note`
- For the court overlay: `co-denver`, `co-arapahoe`,
  `co-county-courts`
- For pre-filing QC: `co-quality-check`, `co-fact-check`
- For deadline math: `co-deadlines`

## References

- `references/motion-template.md` — annotated template
- `references/121-1-15-motion-practice.md` — full text of the rule
- `references/argument-structure.md` — pro-se drafting framework applied
