---
name: az-draft-declaration-codearranger
title: Draft an Arizona Affidavit or Declaration
description: This skill should be used to scaffold a sworn factual statement supporting an Arizona court motion or filing. Arizona practice defaults to a notarized AFFIDAVIT for motion support; Arizona also recognizes an unsworn DECLARATION under penalty of perjury that, under Ariz. R. Civ. P. 80(c), has the same force and effect as a sworn affidavit. Triggers include "draft an Arizona affidavit", "Arizona declaration under penalty of perjury", "A.R.S. 12-2222", "sworn statement Arizona", "notarize affidavit Arizona", "Rule 56(c) affidavit", "affidavit in support of an Arizona motion", "unsworn declaration Arizona". Produces a notarized affidavit (the default) with a personal-knowledge foundation, numbered paragraphs, exhibit references, a jurat, and a notary block, plus a Rule 80(c) declaration-under-penalty-of-perjury block as the alternative. Composes with `az-statewide-format` for the caption, `az-draft-motion` for the supported motion, and `az-draft-order` for the proposed order.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/az-court-docs/skills/az-draft-declaration
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft an Arizona Affidavit or Declaration

> **NOT LEGAL ADVICE.** This skill scaffolds a sworn factual statement.
> You, the declarant/affiant, are personally responsible for the truth of
> every statement. A statement sworn before a notary that is knowingly
> false in a material respect can constitute perjury; a knowingly false
> unsworn declaration subscribed "under penalty of perjury" is itself
> punishable as perjury under A.R.S. § 13-2702. Verify the current rules
> before filing.

Use this skill in addition to `az-statewide-format` when an Arizona
filing requires sworn factual support — most commonly an affidavit
supporting or opposing a motion (including a motion for summary judgment
under Ariz. R. Civ. P. 56), an affidavit of account in a debt matter, or
a declaration verifying facts where a rule or statute calls for sworn
support.

## A note on the citation

A common shorthand points to "A.R.S. § 12-2222" for declarations under
penalty of perjury. That statute is actually titled *Officers authorized
to administer oaths* and governs **who** may administer an oath (judges,
clerks, notaries). The rule that makes an **unsworn declaration carry the
same force and effect as a sworn affidavit** is
**Ariz. R. Civ. P. 80(c)**. Cite Rule 80(c) for the substitution and
A.R.S. § 13-2702 for the perjury backstop; this skill uses those.

## Two sworn-statement forms in Arizona

Arizona recognizes two distinct mechanisms; pick the right one for the
document at hand.

**1. Notarized affidavit (the default for motion support).** A written
statement of facts the affiant swears (or affirms) to be true, signed in
the presence of a notary who administers the oath and completes a
**jurat** ("Subscribed and sworn to before me..."). When an affidavit
supports or opposes a *motion for summary judgment*,
**Ariz. R. Civ. P. 56(c)** governs its content (see below). Default the
scaffold to this form.

**2. Unsworn declaration under penalty of perjury (the alternative).**
Under **Ariz. R. Civ. P. 80(c)**, wherever a rule requires or permits a
matter to be supported, evidenced, established, or proved by a sworn
written declaration, verification, certificate, statement, oath, or
affidavit, the same may instead be made **unsworn** — with the **same
force and effect** — if it is **dated and signed** by the person as true
**under penalty of perjury**. The standard subscription is:

> "I declare under penalty of perjury that the foregoing is true and
> correct."

This needs **no notary**. Rule 80(c) does **not** apply to a deposition,
an oath of office, or an oath required to be taken before a specified
official other than a notary public — use a notarized affidavit there.

**Which to use.** Default to a **notarized affidavit** for summary-
judgment support and for any matter that, by rule or local practice,
expects a notarized oath. Use the **Rule 80(c) declaration** when you
want to avoid the notary bottleneck and no rule requires an oath before a
specified official.

## Ariz. R. Civ. P. 56(c) — affidavit/declaration content requirements

An affidavit or declaration used to support or oppose a motion for
summary judgment must:

- be **made on personal knowledge**;
- **set out facts that would be admissible in evidence**; and
- **show that the affiant or declarant is competent to testify** on the
  matters stated.

Keep each averment to facts the affiant could competently testify to at
trial. An affidavit that buries hearsay, argument, or legal conclusions
inside a "personal knowledge" averment invites a motion to strike.

## Standard affidavit scaffold (default)

```
                    [Caption — see az-statewide-format]

       AFFIDAVIT OF JANE DOE IN SUPPORT OF
       DEFENDANT'S MOTION FOR SUMMARY JUDGMENT

STATE OF ARIZONA        )
                        ) ss.
COUNTY OF [COUNTY]      )

Jane Doe, being first duly sworn, deposes and states as follows:

1. I am the Defendant in this action. I am over eighteen (18) years of
   age and competent to testify to the matters stated herein, and I make
   this Affidavit on my own personal knowledge.

2. On [date], [fact stated with particularity].

3. A true and correct copy of [the written instrument / statement /
   correspondence] is attached hereto as Exhibit A and incorporated by
   reference.

4. [Continue with one material, admissible fact per numbered paragraph.]

Further affiant sayeth not.

                                        ____________________________
                                        Jane Doe, Affiant

Subscribed and sworn to before me this ___ day of __________, 20__.

                                        ____________________________
                                        Notary Public
                                        My commission expires: ________
                                        [Notary seal]
```

## Ariz. R. Civ. P. 80(c) declaration block (alternative)

Use this in place of the jurat and notary block when no oath before a
specified official is required — **no notary**. Open with the same
personal-knowledge averments (paragraphs 1–4 above), then close:

```
                              DECLARATION

I declare under penalty of perjury that the foregoing is true and
correct.

Executed on __________, 20__.        ____________________________
                                     Jane Doe, Declarant
```

## Personal-knowledge foundation

Each averment must rest on the affiant/declarant's **personal
knowledge**. Common foundation phrasing:

- "I am the [role] in this matter and personally [participated in /
  witnessed / received] the events described below."
- "In the regular course of my [business / personal recordkeeping], I
  maintain and am familiar with the records described herein."

When a fact rests on **information and belief** rather than direct
knowledge, say so explicitly and give the basis:

> "Upon information and belief, [fact]. The basis for this belief is my
> review of [the account statement / written contract] attached as
> Exhibit B."

Note that an information-and-belief averment may be insufficient to carry
a fact at summary judgment, where Rule 56(c) demands personal knowledge.

## Numbered paragraphs and exhibits

State each averment in a **separately numbered paragraph** limited so far
as practicable to a single set of circumstances, so the motion or brief
can cite a precise paragraph as record support — e.g., `(Doe Aff. ¶ 3)`.
When the statement relies on a written instrument, **attach a copy as an
exhibit**, label it (`EXHIBIT A`, centered and bold) with a one-line
caption, and refer to it by letter in the body. See `az-statewide-format`
for exhibit handling and pagination.

## Sworn vs. argued — the cardinal rule

The affidavit/declaration's job is to **state facts**; the motion and
brief's job is to **argue law**. Resist arguing in a sworn statement
("Plaintiff's claim is barred by the statute of limitations") — that
belongs in the brief (see `az-draft-motion`), not the affidavit. For each
averment, the supporting brief should cite the paragraph as record
support. Run `az-fact-check` to audit sworn-vs-argued alignment before
filing.

## When the document is notarized

An Arizona notary completes the **jurat** by watching the affiant sign
(or acknowledge a prior signature), administering the oath or affirmation,
then signing and sealing with the commission expiration date. Bring valid
photo identification and do **not** sign the affidavit until you are in
front of the notary.

## Composition

- For format and caption: `az-statewide-format`
- For the supported motion and brief: `az-draft-motion`
- For the proposed order: `az-draft-order`
- For pro se conventions and signature block: `az-pro-se`
- For pre-filing QC: `az-quality-check`, `az-fact-check`
