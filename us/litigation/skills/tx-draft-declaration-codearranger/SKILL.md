---
name: tx-draft-declaration-codearranger
title: Draft a Texas Affidavit or Unsworn Declaration
description: 'This skill should be used to scaffold a sworn factual statement supporting a Texas court motion or filing. Texas recognizes two forms: a notarized AFFIDAVIT, and an UNSWORN DECLARATION under Tex. Civ. Prac. & Rem. Code § 132.001 that may be used in lieu of a written sworn declaration, verification, certificate, statement, oath, or affidavit. Triggers include "draft a Texas affidavit", "Texas unsworn declaration", "CPRC 132.001 declaration", "unsworn declaration under penalty of perjury Texas", "sworn statement Texas", "notarize affidavit Texas", "Rule 166a affidavit Texas", "affidavit in support of a Texas motion", "business records affidavit Texas Rule 902(10)". Produces either a notarized affidavit (personal-knowledge foundation, numbered paragraphs, exhibit references, jurat, and notary block) or a CPRC § 132.001 unsworn-declaration block as the no-notary alternative. Composes with `tx-statewide-format`, `tx-draft-motion`, and `tx-draft-order`.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tx-court-docs/skills/tx-draft-declaration
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft a Texas Affidavit or Unsworn Declaration

> **NOT LEGAL ADVICE.** This skill scaffolds a sworn factual
> statement. You, the affiant/declarant, are personally responsible
> for the truth of every statement. A statement sworn before a
> notary that is knowingly false in a material respect can
> constitute perjury; a knowingly false unsworn declaration
> subscribed "under penalty of perjury" is itself punishable as
> perjury. Verify the current rules before filing.

Use this skill in addition to `tx-statewide-format` when a Texas
filing requires sworn factual support — most commonly an affidavit
or unsworn declaration supporting or opposing a motion (including a
motion for summary judgment under Tex. R. Civ. P. 166a), a verified
pleading, an affidavit on a sworn account (Tex. R. Civ. P. 185), or
a business-records affidavit (Tex. R. Evid. 902(10)). The
**declarant is the user.**

## Two sworn-statement forms in Texas

Texas recognizes two mechanisms. Pick the one that fits the document
and the filer's access to a notary.

**1. Notarized affidavit.** A written statement of facts the affiant
swears (or affirms) to be true, signed in the presence of a notary
who administers the oath and completes a **jurat** ("Subscribed and
sworn to before me ..."). Requires a notary.

**2. Unsworn declaration under penalty of perjury (Tex. Civ. Prac.
& Rem. Code § 132.001).** Texas law permits an **unsworn
declaration** to be used **in lieu of** a written sworn declaration,
verification, certification, oath, or affidavit required by statute
or required by a rule, order, or requirement adopted as provided by
law (with the limited exclusions the statute names — confirm the
current exclusions in `tx-law-references`). The declaration must be:

- **in writing**, and
- **subscribed by the person making it as true under penalty of
  perjury**.

Under **§ 132.001** the declaration must include a **jurat in
substantially the prescribed form**, stating the declarant's printed
name, date of birth, and address, and closing with the penalty-of-
perjury statement and the county and state of execution:

> "I, [printed name], declare under penalty of perjury that the
> foregoing is true and correct.
>
> Executed in ______ County, State of ______, on the ___ day of
> ________, 20__.
>
> _______________________________
> [Declarant signature]"

This needs **no notary**. Confirm the **exact current jurat form and
the required declarant identifiers** (the statute also calls for the
declarant's date of birth and address in the prescribed jurat) and
any document types excluded from § 132.001 in `tx-law-references`.

**Which to use.** Use the **§ 132.001 unsworn declaration** to avoid
the notary bottleneck wherever a sworn statement is merely required
or permitted. Use a **notarized affidavit** where a specific rule,
statute, or local practice expects a notarized oath, or where the
matter is excluded from § 132.001.

## Tex. R. Civ. P. 166a — affidavit/declaration content requirements

An affidavit or unsworn declaration used to support or oppose a
motion for summary judgment must:

- be **made on personal knowledge**;
- **set forth facts that would be admissible in evidence**; and
- **affirmatively show that the affiant or declarant is competent to
  testify** to the matters stated.

Keep each averment to facts the affiant could competently testify to
at trial. An affidavit that buries hearsay, argument, or legal
conclusions inside a "personal knowledge" averment invites an
objection and a motion to strike. Confirm the current Rule 166a(f)
text in `tx-law-references`.

## Standard affidavit scaffold (notarized)

```
                    [Caption — see tx-statewide-format]

       AFFIDAVIT OF JANE DOE IN SUPPORT OF
       DEFENDANT'S MOTION FOR SUMMARY JUDGMENT

STATE OF TEXAS          §
                        §
COUNTY OF [COUNTY]      §

BEFORE ME, the undersigned notary, on this day personally appeared
Jane Doe, who, being by me duly sworn, deposed and stated as follows:

1. "My name is Jane Doe. I am the Defendant in this cause. I am over
   eighteen (18) years of age, of sound mind, and fully competent to
   make this Affidavit, and I have personal knowledge of the facts
   stated herein, each of which is true and correct.

2. On [date], [fact stated with particularity].

3. A true and correct copy of [the written instrument / statement /
   correspondence] is attached hereto as Exhibit A and incorporated
   by reference.

4. [Continue with one material, admissible fact per numbered
   paragraph.]"

                                        ____________________________
                                        Jane Doe, Affiant

SUBSCRIBED AND SWORN TO before me on this ___ day of __________, 20__.

                                        ____________________________
                                        Notary Public, State of Texas
                                        My commission expires: ______
                                        [Notary seal]
```

## CPRC § 132.001 unsworn-declaration block (no notary)

Use this in place of the jurat and notary block. Open with the same
personal-knowledge averments (paragraphs 1–4 above), then close with
the § 132.001 jurat:

```
                              DECLARATION

"My name is Jane Doe, my date of birth is __________, and my address
is _________________________, _______ County, _______, U.S.A. I
declare under penalty of perjury that the foregoing is true and
correct.

Executed in ______ County, State of Texas, on the ___ day of
__________, 20__.

                                     ____________________________
                                     Jane Doe, Declarant"
```

> Confirm the **exact § 132.001 jurat language and required
> identifiers** in `tx-law-references` — the statute prescribes the
> form, and a declaration that omits a required element (e.g., the
> date of birth or address in the prescribed jurat) may be
> challenged.

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
fact at summary judgment, where Tex. R. Civ. P. 166a demands personal
knowledge.

## Business-records affidavit — Tex. R. Evid. 902(10)

Texas allows **self-authentication of business records by affidavit**
under **Tex. R. Evid. 902(10)**, which supplies the affidavit form
and the pretrial **notice and filing** mechanics. In a debt or
account matter, scrutinize the affiant's foundation: a custodian who
lacks knowledge of the **original creditor's** records may be unable
to authenticate them. Confirm the current 902(10) affidavit form and
the notice/filing deadline in `tx-law-references`; pair with
`tx-consumer-debt` when the records are an assigned account.

## Verified pleadings and sworn accounts

- **Verified pleas (Tex. R. Civ. P. 93)** — certain matters (lack of
  capacity, defect of parties, denial of a sworn account, etc.) must
  be **denied under oath / by verified pleading**. The verification
  can be supplied by a § 132.001 unsworn declaration or a notarized
  affidavit.
- **Sworn account (Tex. R. Civ. P. 185)** — a properly verified
  account is prima facie proof unless the defendant files a **sworn
  denial** under Rule 93(10) / Rule 185. See `tx-consumer-debt`.

## Numbered paragraphs and exhibits

State each averment in a **separately numbered paragraph** limited so
far as practicable to a single set of circumstances, so the motion
can cite a precise paragraph as record support — e.g., `(Doe Aff.
¶ 3)`. When the statement relies on a written instrument, **attach a
copy as an exhibit**, label it (`EXHIBIT A`, centered and bold) with
a one-line caption, and refer to it by letter in the body. See
`tx-statewide-format` for exhibit handling and pagination.

## Sworn vs. argued — the cardinal rule

The affidavit/declaration's job is to **state facts**; the motion's
job is to **argue law**. Resist arguing in a sworn statement
("Plaintiff's claim is barred by limitations") — that belongs in the
motion's Argument & Authorities section (see `tx-draft-motion`), not
the affidavit. Run `tx-fact-check` to audit sworn-vs-argued alignment
before filing.

## When the document is notarized

A Texas notary completes the **jurat** by watching the affiant sign
(or acknowledge a prior signature), administering the oath or
affirmation, then signing and sealing with the commission expiration
date. Bring valid photo identification and do **not** sign the
affidavit until you are in front of the notary.

## Composition

- For format and caption: `tx-statewide-format`
- For the supported motion: `tx-draft-motion`
- For the proposed order: `tx-draft-order`
- For pro se conventions and signature block: `tx-pro-se`
- For sworn-account / 902(10) records context: `tx-consumer-debt`
- For pre-filing QC: `tx-quality-check`, `tx-fact-check`
- For the current text of CPRC § 132.001, Tex. R. Civ. P. 166a(f),
  and Tex. R. Evid. 902(10): `tx-law-references`

## References to author

- `references/affidavit-template.md` — annotated notarized affidavit
  scaffold
- `references/declaration-template.md` — CPRC § 132.001 unsworn-
  declaration scaffold with the prescribed jurat
- `references/personal-knowledge.md` — foundation and
  sworn-vs-argued guidance
