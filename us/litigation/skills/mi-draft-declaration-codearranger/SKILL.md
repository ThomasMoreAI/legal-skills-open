---
name: mi-draft-declaration-codearranger
title: Draft a Michigan Affidavit
description: This skill should be used to scaffold a sworn factual statement for a Michigan court filing. Michigan practice defaults to a notarized AFFIDAVIT for motion support; Michigan also recognizes verification by a signed declaration "under the penalties of perjury" under MCR 1.109(D)(3) in lieu of a separate oath for many documents. Triggers include "draft a Michigan affidavit", "MCR 2.119(B) affidavit", "verification MCR 1.109(D)(3)", "sworn statement Michigan", "notarize affidavit Michigan", "affidavit in support of a Michigan motion", "verify a Michigan pleading". Produces a notarized affidavit (the default) with a personal-knowledge foundation, numbered paragraphs, exhibit references, a jurat, and a notary block, plus an MCR 1.109(D)(3) verification block as the alternative. Composes with `mi-statewide-format` for the caption, `mi-draft-motion` for the supported motion, and `mi-draft-order` for the proposed order.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/mi-court-docs/skills/mi-draft-declaration
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft a Michigan Affidavit

> **NOT LEGAL ADVICE.** This skill scaffolds a sworn factual statement.
> The declarant/affiant is personally responsible for the truth of every
> statement; a statement sworn before a notary that is knowingly false in
> a material respect can constitute perjury, and a knowingly false
> declaration "under the penalties of perjury" can be punished as
> perjury and as contempt of court. Verify the current rules before
> filing.

Use this skill in addition to `mi-statewide-format` when a filing
requires sworn factual support — most commonly an affidavit supporting
or opposing a motion (including a motion for summary disposition under
MCR 2.116), an affidavit of account in a debt matter, or a verification
attached to a pleading.

## Two sworn-statement forms in Michigan

Michigan recognizes two distinct mechanisms; pick the right one for the
document at hand.

**1. Notarized affidavit (the default for motion support).** A written
statement of facts the affiant swears (or affirms) to be true, signed in
the presence of a notary who administers the oath and completes a
**jurat** ("Sworn to and subscribed before me..."). The oath is
administered under **MCL 600.2102**. When an affidavit supports or
opposes a *motion*, **MCR 2.119(B)** governs its content (see below).
Default the scaffold to this form.

**2. Verification by declaration under MCR 1.109(D)(3) (the
alternative).** Where a document is required or permitted to be
*verified*, the rule allows verification — **except as to an
affidavit** — by a signed and dated declaration in this form:

> "I declare under the penalties of perjury that this ________ has been
> examined by me and that its contents are true to the best of my
> information, knowledge, and belief."

This needs **no notary**. A person who knowingly makes a false
declaration under this subrule may be found in contempt of court, in
addition to other sanctions.

**Which to use.** Use a **notarized affidavit** to supply sworn facts in
support of or opposition to a **motion** (MCR 2.119(B) requires an
affidavit there — the (D)(3) declaration is unavailable "as to an
affidavit"). Use the **MCR 1.109(D)(3) verification** to verify a
**pleading** or other document where the rule or statute calls for
verification rather than a supporting affidavit.

## MCR 2.119(B) — affidavit content requirements

An affidavit filed in support of or in opposition to a motion must:

- **(a)** be **made on personal knowledge**;
- **(b)** state **with particularity** facts **admissible as evidence**
  establishing or denying the grounds stated in the motion; and
- **(c)** show affirmatively that the affiant, **if sworn as a witness,
  can testify competently** to the facts stated.

Keep each averment to facts the affiant could competently testify to at
trial. An affidavit that buries hearsay, argument, or conclusions inside
a "personal knowledge" averment invites a motion to strike.

## Standard affidavit scaffold (default)

```
                    [Caption — see mi-statewide-format]

       AFFIDAVIT OF JANE DOE IN SUPPORT OF
       DEFENDANT'S MOTION FOR SUMMARY DISPOSITION

STATE OF MICHIGAN       )
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
                                        Notary Public, State of Michigan
                                        County of __________
My commission expires: ____________     Acting in the County of ________
                                        [Notary seal]
```

## MCR 1.109(D)(3) verification block (alternative)

Append this to a verified pleading or document where a declaration is
permitted in lieu of an oath — **no notary required**:

```
                              VERIFICATION

I declare under the penalties of perjury that this [Complaint /
Answer / pleading] has been examined by me and that its contents are
true to the best of my information, knowledge, and belief.

Dated: __________                       ____________________________
                                        Jane Doe, Declarant
```

## Personal-knowledge foundation

Each averment must rest on the affiant's **personal knowledge**. Common
foundation phrasing:

- "I am the [role] in this matter and personally [participated in /
  witnessed / received] the events described below."
- "In the regular course of my [business / personal recordkeeping], I
  maintain and am familiar with the records described herein."

When a fact rests on **information and belief** rather than direct
knowledge, say so explicitly and give the basis:

> "Upon information and belief, [fact]. The basis for this belief is my
> review of [the account statement / written contract] attached as
> Exhibit B."

## Numbered paragraphs and exhibits

State each averment in a **separately numbered paragraph** limited so far
as practicable to a single set of circumstances, so the motion or brief
can cite a precise paragraph as record support — e.g., `(Doe Aff. ¶ 3)`.
When the affidavit relies on a written instrument, **attach a copy as an
exhibit**, label it (`EXHIBIT A`, centered and bold) with a one-line
caption, and refer to it by letter in the body. See `mi-statewide-format`
for exhibit handling and pagination.

## Sworn vs. argued — the cardinal rule

The affidavit's job is to **state facts**; the motion and brief's job is
to **argue law**. Resist arguing in an affidavit ("Plaintiff's claim is
barred by the statute of limitations") — that belongs in the brief (see
`mi-draft-motion`), not the affidavit. For each averment, the supporting
brief should cite the paragraph as record support. Run `mi-fact-check`
to audit sworn-vs-argued alignment before filing.

## When the document is notarized

A Michigan notary completes the **jurat** by watching the affiant sign
(or acknowledge a prior signature), administering the oath or affirmation
under MCL 600.2102, then signing and sealing with the commission
expiration date and the county of commission. Bring valid photo
identification and do **not** sign the affidavit until you are in front
of the notary.

## Composition

- For format and caption: `mi-statewide-format`
- For the supported motion and brief: `mi-draft-motion`
- For the proposed order: `mi-draft-order`
- For pro se conventions and signature block: `mi-pro-se`
- For pre-filing QC: `mi-quality-check`, `mi-fact-check`

## References

- `references/affidavit-template.md` — annotated notarized-affidavit
  template with jurat and notary block
- `references/mcr-2119b-affidavit.md` — MCR 2.119(B) personal-knowledge
  and admissibility requirements
- `references/mcr-1109d3-verification.md` — declaration-under-penalties
  verification form and when it may replace an oath
- `references/personal-knowledge.md` — foundation conventions
