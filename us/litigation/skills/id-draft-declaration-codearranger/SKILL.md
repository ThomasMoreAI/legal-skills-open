---
name: id-draft-declaration-codearranger
title: Draft an Idaho Affidavit or Declaration
description: 'This skill should be used to scaffold a sworn factual statement supporting an Idaho court motion or filing. Idaho recognizes two forms: a notarized AFFIDAVIT, and an unsworn DECLARATION under penalty of perjury that, under Idaho Code § 9-1406, has the same force and effect as a notarized affidavit. Triggers include "draft an Idaho affidavit", "Idaho declaration under penalty of perjury", "I.C. 9-1406", "unsworn declaration Idaho", "sworn statement Idaho", "notarize affidavit Idaho", "Rule 56(c) affidavit Idaho", "affidavit in support of an Idaho motion". Produces either a notarized affidavit (personal-knowledge foundation, numbered paragraphs, exhibit references, jurat, and notary block) or an Idaho Code § 9-1406 declaration block as the no-notary alternative. Composes with `id-statewide-format` for the caption, `id-draft-motion` for the supported motion, and `id-draft-order` for the proposed order.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/id-court-docs/skills/id-draft-declaration
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Affidavit Template
  path: references/affidavit-template.md
- title: Declaration Template
  path: references/declaration-template.md
- title: Personal Knowledge
  path: references/personal-knowledge.md
---

# Draft an Idaho Affidavit or Declaration

> **NOT LEGAL ADVICE.** This skill scaffolds a sworn factual
> statement. You, the affiant/declarant, are personally
> responsible for the truth of every statement. A statement sworn
> before a notary that is knowingly false in a material respect
> can constitute perjury; a knowingly false unsworn declaration
> subscribed "under penalty of perjury" is itself punishable as
> perjury. Verify the current rules before filing.

Use this skill in addition to `id-statewide-format` when an Idaho
filing requires sworn factual support — most commonly an affidavit
or declaration supporting or opposing a motion (including a motion
for summary judgment under I.R.C.P. 56), an affidavit of account
in a debt matter, or a verification of facts where a rule or
statute calls for sworn support.

## Two sworn-statement forms in Idaho

Idaho recognizes two interchangeable mechanisms; either is
acceptable supporting evidence under **I.R.C.P. 56(c)**. Pick the
one that fits the document and the filer's access to a notary.

**1. Notarized affidavit.** A written statement of facts the
affiant swears (or affirms) to be true, signed in the presence of
a notary who administers the oath and completes a **jurat**
("Subscribed and sworn to before me ..."). Requires a notary.

**2. Unsworn declaration under penalty of perjury (Idaho Code
§ 9-1406).** Idaho law permits an **unsworn declaration** in lieu
of a notarized affidavit wherever a matter is required or
permitted to be supported, evidenced, established, or proved by a
sworn affidavit, declaration, verification, or oath. If the
statement is **dated and signed** by the person and subscribed as
true **under penalty of perjury**, it carries the **same force and
effect** as a notarized affidavit. The standard subscription is:

> "I declare under penalty of perjury under the laws of the State
> of Idaho that the foregoing is true and correct."

This needs **no notary**. Confirm the current text and any form
requirements of **Idaho Code § 9-1406** in `id-law-references`.

**Which to use.** Either is acceptable under I.R.C.P. 56(c). Use
the **§ 9-1406 declaration** to avoid the notary bottleneck. Use a
**notarized affidavit** where a specific rule, statute, or local
practice expects a notarized oath, or where the matter must be
sworn before a particular official.

## I.R.C.P. 56(c) — affidavit/declaration content requirements

An affidavit or declaration used to support or oppose a motion for
summary judgment must:

- be **made on personal knowledge**;
- **set out facts that would be admissible in evidence**; and
- **show that the affiant or declarant is competent to testify**
  on the matters stated.

Keep each averment to facts the affiant could competently testify
to at trial. An affidavit that buries hearsay, argument, or legal
conclusions inside a "personal knowledge" averment invites a
motion to strike. Confirm the current Rule 56(c) text in
`id-law-references`.

## Standard affidavit scaffold (notarized)

```
                    [Caption — see id-statewide-format]

       AFFIDAVIT OF JANE DOE IN SUPPORT OF
       DEFENDANT'S MOTION FOR SUMMARY JUDGMENT

STATE OF IDAHO          )
                        ) ss.
COUNTY OF [COUNTY]      )

Jane Doe, being first duly sworn, deposes and states as follows:

1. I am the Defendant in this action. I am over eighteen (18) years
   of age and competent to testify to the matters stated herein,
   and I make this Affidavit on my own personal knowledge.

2. On [date], [fact stated with particularity].

3. A true and correct copy of [the written instrument / statement /
   correspondence] is attached hereto as Exhibit A and incorporated
   by reference.

4. [Continue with one material, admissible fact per numbered
   paragraph.]

                                        ____________________________
                                        Jane Doe, Affiant

Subscribed and sworn to before me this ___ day of __________, 20__.

                                        ____________________________
                                        Notary Public for Idaho
                                        Residing at: ______________
                                        My commission expires: _____
                                        [Notary seal]
```

## Idaho Code § 9-1406 declaration block (no notary)

Use this in place of the jurat and notary block. Open with the same
personal-knowledge averments (paragraphs 1–4 above), then close:

```
                              DECLARATION

I declare under penalty of perjury under the laws of the State of
Idaho that the foregoing is true and correct.

Executed on __________, 20__.        ____________________________
                                     Jane Doe, Declarant
```

## Personal-knowledge foundation

Each averment must rest on the affiant/declarant's **personal
knowledge**. Common foundation phrasing:

- "I am the [role] in this matter and personally [participated in /
  witnessed / received] the events described below."
- "In the regular course of my [business / personal recordkeeping],
  I maintain and am familiar with the records described herein."

When a fact rests on **information and belief** rather than direct
knowledge, say so explicitly and give the basis:

> "Upon information and belief, [fact]. The basis for this belief is
> my review of [the account statement / written contract] attached
> as Exhibit B."

An information-and-belief averment may be insufficient to carry a
fact at summary judgment, where I.R.C.P. 56(c) demands personal
knowledge.

## Numbered paragraphs and exhibits

State each averment in a **separately numbered paragraph** limited
so far as practicable to a single set of circumstances, so the
motion or Memorandum can cite a precise paragraph as record support
— e.g., `(Doe Aff. ¶ 3)`. When the statement relies on a written
instrument, **attach a copy as an exhibit**, label it (`EXHIBIT A`,
centered and bold) with a one-line caption, and refer to it by
letter in the body. See `id-statewide-format` for exhibit handling
and pagination.

## Sworn vs. argued — the cardinal rule

The affidavit/declaration's job is to **state facts**; the motion
and Memorandum's job is to **argue law**. Resist arguing in a sworn
statement ("Plaintiff's claim is barred by the statute of
limitations") — that belongs in the Memorandum (see
`id-draft-motion`), not the affidavit. For each averment, the
supporting Memorandum should cite the paragraph as record support.
Run `id-fact-check` to audit sworn-vs-argued alignment before
filing.

## When the document is notarized

An Idaho notary completes the **jurat** by watching the affiant
sign (or acknowledge a prior signature), administering the oath or
affirmation, then signing and sealing with the commission
expiration date. Bring valid photo identification and do **not**
sign the affidavit until you are in front of the notary.

## Composition

- For format and caption: `id-statewide-format`
- For the supported motion and Memorandum: `id-draft-motion`
- For the proposed order: `id-draft-order`
- For pro se conventions and signature block: `id-pro-se`
- For pre-filing QC: `id-quality-check`, `id-fact-check`
- For the current text of Idaho Code § 9-1406 and I.R.C.P. 56(c):
  `id-law-references`

## References to author

- `references/affidavit-template.md` — annotated notarized
  affidavit scaffold
- `references/declaration-template.md` — Idaho Code § 9-1406
  unsworn-declaration scaffold
- `references/personal-knowledge.md` — foundation and
  sworn-vs-argued guidance
