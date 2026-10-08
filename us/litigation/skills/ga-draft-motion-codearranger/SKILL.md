---
name: ga-draft-motion-codearranger
title: Draft a Georgia Motion
description: This skill should be used to scaffold a Georgia civil motion with its supporting brief. Triggers include "draft a Georgia motion", "write a motion to dismiss Georgia", "draft a Georgia motion to compel", "draft a motion for summary judgment Georgia", "draft a motion to set aside default Georgia", "draft a motion under O.C.G.A. § 9-11-56". Produces a motion plus supporting brief in the Georgia format, applying the pro-se drafting framework (clear relief, cite the rule or statute, state supporting facts, conclude with the signature block and required certificate of service). Composes with `ga-statewide-format` for the format baseline, `ga-draft-declaration` for sworn facts, `ga-draft-order` for the proposed order, and the relevant venue and subject-matter skills.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ga-court-docs/skills/ga-draft-motion
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft a Georgia Motion

> **NOT LEGAL ADVICE.** This skill scaffolds a court document
> as a drafting aid. The user — not the skill — chooses the
> motion type, theory of relief, and strategy. Verify every
> rule, deadline, and citation against current law before
> filing. Pair with substantive review by counsel where stakes
> warrant.

Use this skill to produce a motion plus supporting brief in Georgia
format. Georgia motion practice is governed by the Civil Practice Act
(O.C.G.A. Title 9, Ch. 11), the rule under which the motion is filed
(e.g., O.C.G.A. § 9-11-12(b)(6), § 9-11-56, § 9-11-37(a),
§ 9-11-55(b)), and the Uniform Superior Court Rules (USCR 6 governs
motion practice; the parallel Uniform State Court Rules apply in State
Court).

## Motion timing under USCR 6

| Event | Timing |
|---|---|
| Response to a motion | 30 days after service (USCR 6.2) |
| Request for oral hearing | Within the response period; must be requested or it may be waived (USCR 6.3) |
| Summary-judgment motion | Served at least 30 days before the hearing (O.C.G.A. § 9-11-56(c)) |

When a hearing is sought, prepare a **Rule Nisi / Notice of Hearing**
under USCR 6.3 (see `ga-draft-note`) for the judge to set the date.

## Standard motion structure

```
                    [Caption — see ga-statewide-format,
                     per O.C.G.A. § 9-11-10(a): court, county,
                     title of action, file number, designation]

           [DOCUMENT TITLE IN ALL CAPS, e.g.,
       DEFENDANT'S MOTION TO DISMISS UNDER O.C.G.A. § 9-11-12(b)(6)]

COMES NOW [Movant], the [Plaintiff / Defendant] in the above-styled
action, [appearing pro se / by and through undersigned counsel], and
respectfully moves this Court for [specific relief], and in support
shows the Court as follows:

                       I. INTRODUCTION

[1-2 paragraph summary of the case, the relief sought, and the
grounds in headline form.]

                  II. STATEMENT OF FACTS

[Numbered factual paragraphs, each stating a single material fact
with a citation to the record — Affidavit ¶ X, Complaint ¶ X,
Exhibit X, or an admission in the pleadings.]

                       III. ARGUMENT AND CITATION OF AUTHORITY

A. [Headline of first argument]

[Lead with the rule or statute; state the controlling standard;
apply it to the facts; cite Georgia authority — Supreme Court of
Georgia and Court of Appeals of Georgia decisions.]

B. [Headline of second argument]

[...]

                       IV. CONCLUSION (PRAYER FOR RELIEF)

WHEREFORE, [Movant] respectfully prays that this Court [grant the
motion / grant the relief sought] and enter the attached proposed
Order.

Respectfully submitted, this ___ day of __________, 20__.

                                        _____________________________
                                        [Name]
                                        [Address]
                                        [City, GA ZIP]
                                        [Phone]
                                        [Email]
                                        Pro Se
                                        [OR: Georgia Bar No. ______,
                                         Attorney for ____  —
                                         O.C.G.A. § 9-11-11]

                   CERTIFICATE OF SERVICE
[Date, method, recipients — per O.C.G.A. § 9-11-5 and
ga-statewide-format]
```

## Signature and certificate requirements

- **Signature** — every motion must be signed (O.C.G.A. § 9-11-11). A
  pro se filer signs and adds name, address, phone, and email with the
  designation **Pro Se**. An attorney adds the **Georgia Bar No.**
- **Certificate of service** — subsequent papers are served and the
  service certified under O.C.G.A. § 9-11-5; place the certificate of
  service at the foot of the motion.
- **Rule Nisi / Notice of Hearing** — when a hearing is sought, attach
  or file the scheduling document under USCR 6.3 (see `ga-draft-note`).
- **Format defaults** — line numbering down the left margin and a
  footer "Page X of Y" are marketplace format defaults applied through
  `ga-statewide-format`.

## Common motion types

| Motion | Authority | Notes |
|---|---|---|
| Motion to Dismiss | O.C.G.A. § 9-11-12(b)(6) | Failure to state a claim |
| Motion for Summary Judgment | O.C.G.A. § 9-11-56 | Served at least 30 days before hearing; *Lau's Corp. v. Haskins*, 261 Ga. 491 (1991) (movant may point to absence of evidence) |
| Motion to Compel | O.C.G.A. § 9-11-37(a) | Attach the deficient responses |
| Motion to Set Aside Default | O.C.G.A. § 9-11-55(b) | Open as of right within 15 days plus costs under § 9-11-55(a); otherwise providential/excusable/proper case + four conditions |
| Motion for Protective Order | O.C.G.A. § 9-11-26(c) | Discovery-shielding |
| Motion to Amend | O.C.G.A. § 9-11-15 | As of right before entry of the pretrial order |

## Argument structure — the pro-se drafting framework

1. **State the relief clearly** in the opening sentence.
2. **Cite the rule or statute** that grants the court power to award it.
3. **State the facts** that satisfy each element of the standard.
4. **Apply controlling Georgia case law** to those facts.
5. **Conclude** with the specific order sought.

A motion that hides the relief, buries the statute citation, or omits
a clear element-by-element factual showing is the kind of filing the
court will struggle to engage with.

## Filing checklist

- [ ] Caption matches the assigned court and county (O.C.G.A. § 9-11-10(a))
- [ ] Title in ALL CAPS centered between caption and body
- [ ] All cited rules and statutes correct (run `ga-fact-check`)
- [ ] Affirmative defenses and counter-arguments addressed
- [ ] Signature block complete (Pro Se / Georgia Bar No.)
- [ ] Certificate of Service complete (O.C.G.A. § 9-11-5)
- [ ] Rule Nisi / Notice of Hearing prepared if a hearing is sought
- [ ] Proposed Order drafted as a **separate** document (`ga-draft-order`)
- [ ] Supporting Affidavit(s) drafted (`ga-draft-declaration`)
- [ ] Format check passes (`scripts/format-check.py`)

## Composition

- For format: `ga-statewide-format`
- For the supporting affidavit/declaration: `ga-draft-declaration`
- For the proposed order: `ga-draft-order`
- For setting the hearing: `ga-schedule-hearing`, `ga-draft-note`
- For the venue overlay: `ga-fulton`, `ga-cobb`, `ga-gwinnett`,
  `ga-state-court`, `ga-magistrate`, `ga-county-courts`,
  `ga-family-court`
- For subject matter: `ga-consumer-debt`, `ga-family-law`
- For pre-filing QC: `ga-quality-check`, `ga-fact-check`
- For deadline math: `ga-deadlines`
- For pro se conventions: `ga-pro-se`

## References

- `references/motion-template.md` — annotated template
- `references/uscr-6-motion-practice.md` — USCR 6 motion-practice notes
- `references/argument-structure.md` — pro-se drafting framework applied
