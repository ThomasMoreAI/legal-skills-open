---
name: tn-draft-declaration-codearranger
title: Draft a Tennessee Affidavit
description: Use to scaffold a sworn factual statement for Tennessee court filings. Tennessee's default is a notarized affidavit (sworn before a notary public). Produces an affidavit with personal-knowledge foundation, numbered paragraphs under Tenn. R. Civ. P. 10.02, exhibit references under Rule 10.03, jurat, and notary block. Commonly used for summary-judgment support under Rule 56, affidavit of account in debt matters, or fact affidavits supporting motions. Notes that unsworn declarations under penalty of perjury may be accepted in limited contexts — verify before relying. Composes with `tn-statewide-format` for the caption, `tn-draft-motion` for the supported motion, and `tn-draft-order` for the proposed order.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tn-court-docs/skills/tn-draft-declaration
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft a Tennessee Affidavit

> **NOT LEGAL ADVICE.** This skill scaffolds a sworn factual statement.
> The affiant is personally responsible for the truth of every
> statement; a statement sworn before a notary that is knowingly false
> in a material respect can constitute perjury or aggravated perjury
> under Tennessee law. Verify the current rules before filing.

Use this skill in addition to `tn-statewide-format` when a filing
requires sworn factual support — most commonly an affidavit supporting
or opposing a motion for summary judgment under **Tenn. R. Civ. P. 56**,
an affidavit of account in a debt matter, or a fact affidavit
accompanying any motion.

## The default in Tennessee is a notarized affidavit

In Tennessee practice, the standard sworn support document is an
**affidavit sworn before a notary public** — a written statement of
facts the affiant swears (or affirms) to be true, signed in the
presence of a notary who completes a **jurat** ("Sworn to and
subscribed before me...").

> **Verify before using an unsworn declaration.** Some jurisdictions
> and contexts accept an *unsworn declaration under penalty of perjury*
> in lieu of a notarized affidavit. Whether Tennessee accepts one for
> your specific filing depends on the matter type and the court's local
> rules — **do not assume it.** Default to a **notarized affidavit**,
> and only use an unsworn declaration if you have confirmed the court
> and matter accept it. When in doubt, get the document notarized.

## Required components

Every affidavit should include:

1. **Caption** identical to the motion or pleading it supports (see
   `tn-statewide-format`)
2. **Document title** in ALL CAPS, e.g.,
   `AFFIDAVIT OF JANE DOE IN SUPPORT OF DEFENDANT'S MOTION FOR SUMMARY JUDGMENT`
3. **Venue / commencement line** identifying the state and county where
   the affidavit is sworn
4. **Opening averment**: identify the affiant, that the affiant is
   competent, and the basis for personal knowledge
5. **Numbered paragraphs** of factual content (Tenn. R. Civ. P. 10.02)
6. **Exhibit references** as needed (Tenn. R. Civ. P. 10.03)
7. **Affiant's signature line**
8. **Jurat and notary block** (notary signature, commission expiration,
   seal)

## Standard affidavit scaffold

```
                    [Caption — see tn-statewide-format]

       AFFIDAVIT OF JANE DOE IN SUPPORT OF
       DEFENDANT'S MOTION FOR SUMMARY JUDGMENT

STATE OF TENNESSEE      )
                        )
COUNTY OF [COUNTY]      )

I, Jane Doe, after being first duly sworn, depose and state as
follows:

1. I am the Defendant in this action. I am over eighteen (18) years
   of age and competent to testify to the matters stated herein. I
   make this Affidavit based on my own personal knowledge.

2. On [date], Plaintiff [fact stated in one set of circumstances].

3. A true and correct copy of [the written instrument / statement /
   correspondence] is attached hereto as Exhibit A and incorporated
   by reference.

4. [Continue with one material fact per numbered paragraph.]

FURTHER AFFIANT SAYETH NAUGHT.

                                        ____________________________
                                        Jane Doe, Affiant

                              JURAT

Sworn to and subscribed before me this ___ day of __________, 20__.

                                        ____________________________
                                        Notary Public
My commission expires: ____________     [Notary seal]
```

## Personal-knowledge foundation

Each averment must rest on the affiant's **personal knowledge** — a
Rule 56 affidavit in particular "shall be made on personal knowledge,
shall set forth such facts as would be admissible in evidence, and
shall show affirmatively that the affiant is competent to testify to
the matters stated." Common foundation phrasing:

- "I am the [role] in this matter and personally [participated in /
  witnessed / received] the events described below."
- "In the regular course of my [business / personal recordkeeping], I
  maintain and am familiar with the records described herein."

When a fact rests on **information and belief** rather than direct
knowledge, say so explicitly and give the basis:

> "Upon information and belief, [fact]. The basis for this belief is my
> review of [the account statement / written contract] attached as
> Exhibit B."

A summary-judgment affidavit that buries hearsay or conclusions inside
a "personal knowledge" averment invites a motion to strike. Keep each
averment to facts the affiant could competently testify to at trial.

## Numbered paragraphs — Tenn. R. Civ. P. 10.02

State each averment in a **separately numbered paragraph**, with each
paragraph limited "as far as practicable to a statement of a single set
of circumstances." This lets the motion or memorandum cite a precise
paragraph as record support — e.g., `(Doe Aff. ¶ 3)`.

## Exhibits — Tenn. R. Civ. P. 10.03

When the affidavit relies on a written instrument, **attach a copy as
an exhibit** and refer to it in the relevant paragraph. Each exhibit
should have a cover page labeling it (`EXHIBIT A`, centered and bold)
with a one-line caption describing it. Reference exhibits in the body
by letter ("attached hereto as Exhibit A"). See `tn-statewide-format`
for exhibit handling and pagination.

## Sworn vs. argued — the cardinal rule

The affidavit's job is to **state facts**; the motion and memorandum's
job is to **argue law**. Resist arguing in an affidavit ("Plaintiff's
claim is barred by the six-year statute of limitations"). That sentence
belongs in the memorandum of law (see `tn-draft-motion`), not the
affidavit. For each factual averment, the supporting memorandum should
cite the paragraph as record support. Run `tn-fact-check` to audit
sworn-vs-argued alignment before filing.

## Affidavit of account in debt matters

In a consumer-debt matter, a plaintiff often files an **affidavit of
account** to lay a business-records foundation under Tenn. R. Evid.
803(6). Note the recent statutory development at **Tenn. Code Ann.
§ 20-6-104** (added 2024): a "subsequent creditor" / debt-buyer
plaintiff must, before any default judgment, present documentation
sufficient to show **authority to collect the debt** and **at least one
document showing the debt's existence**, irrespective of any affidavit.
This does not apply to original creditors. See `tn-consumer-debt` for
the substantive framework; an affidavit alone may not carry a
debt-buyer's burden.

## When the document is notarized

A Tennessee notary completes the **jurat** by watching the affiant sign
(or acknowledge a prior signature) and administering the oath or
affirmation, then signing and sealing with the commission expiration
date. Notaries are widely available at banks, courthouse clerk's
offices, shipping stores, and many libraries. Bring valid photo
identification and do **not** sign the affidavit until you are in front
of the notary.

## Composition

- For format and caption: `tn-statewide-format`
- For the supported motion and memorandum: `tn-draft-motion`
- For the proposed order: `tn-draft-order`
- For the consumer-debt foundation rules: `tn-consumer-debt`
- For pro se conventions and signature block: `tn-pro-se`
- For pre-filing QC: `tn-quality-check`, `tn-fact-check`
- For the venue overlay: `tn-davidson`, `tn-shelby`, `tn-knox`,
  `tn-hamilton`, `tn-county-courts`

## References

- `references/affidavit-template.md` — annotated notarized-affidavit
  template with jurat and notary block
- `references/rule-56-affidavit.md` — Rule 56 personal-knowledge and
  admissibility requirements
- `references/personal-knowledge.md` — foundation conventions
- `references/affidavit-of-account.md` — debt-matter affidavit and the
  § 20-6-104 documentation requirement
