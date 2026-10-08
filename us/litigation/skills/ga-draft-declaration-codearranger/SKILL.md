---
name: ga-draft-declaration-codearranger
title: Draft a Georgia Affidavit / Declaration
description: This skill should be used to scaffold a Georgia affidavit or declaration. Triggers include "draft a Georgia affidavit", "sworn declaration Georgia", "draft a supporting affidavit Georgia", "notarized affidavit for a Georgia motion", "affidavit in support of summary judgment Georgia", "unsworn declaration Georgia". Produces a sworn affidavit (the Georgia default for evidentiary use) or an unsworn declaration where permitted, with a proper personal-knowledge foundation, numbered paragraphs, exhibit references, and the correct jurat or verification language.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ga-court-docs/skills/ga-draft-declaration
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft a Georgia Affidavit / Declaration

> **NOT LEGAL ADVICE.** This skill scaffolds a court document
> as a drafting aid. The user — not the skill — is the
> declarant, chooses what facts to swear to, and signs the
> declaration. Verify every rule, deadline, and citation
> against current law before filing. Pair with substantive
> review by counsel where stakes warrant.

Use this skill in addition to `ga-statewide-format` when a filing
requires sworn factual support. Georgia practice **favors a sworn,
notarized affidavit** for evidentiary use (e.g., affidavits supporting
or opposing summary judgment under O.C.G.A. § 9-11-56(e), which must be
made on personal knowledge and set out facts admissible in evidence).
An **unsworn declaration** is available in the limited contexts
permitted by the O.C.G.A. § 9-10-111 / § 24-1-2 framework, and a
**federal-style unsworn declaration under 28 U.S.C. § 1746** is used
in federal filings.

## Affidavit vs. declaration — which to use

| | Affidavit | Unsworn declaration |
|---|---|---|
| Notarization | Required — "personally appeared … being duly sworn" | None |
| Authority | Sworn before a notary or officer authorized to administer oaths | O.C.G.A. § 9-10-111 / § 24-1-2 framework (state); 28 U.S.C. § 1746 (federal) |
| Closing | Jurat: "Sworn to and subscribed before me this ___ day of ___, 20__." | "I declare under penalty of perjury that the foregoing is true and correct." |
| When to use | **Default** for Georgia evidentiary use — summary-judgment affidavits, default-judgment proof, most motion support | Where a rule permits an unsworn statement, or in federal court under § 1746 |

For most Georgia state-court evidentiary purposes, use a **notarized
affidavit**. Confirm the specific rule before substituting an unsworn
declaration.

## Required components

1. **Caption** identical to the motion / pleading (O.C.G.A. § 9-11-10(a))
2. **Document title**: e.g.,
   `AFFIDAVIT OF JANE DOE IN SUPPORT OF DEFENDANT'S MOTION FOR SUMMARY JUDGMENT`
3. **Opening recital**: identify the affiant and the basis for
   personal knowledge
4. **Numbered paragraphs** of factual content (O.C.G.A. § 9-11-10(b))
5. **Exhibit references** as needed
6. **Closing**: jurat (affidavit) or penalty-of-perjury verification
   (declaration)
7. **Signature** of the affiant/declarant; notary block for an affidavit

## Standard affidavit scaffold

```
                  [Caption — see ga-statewide-format]

   AFFIDAVIT OF JANE DOE IN SUPPORT OF DEFENDANT'S MOTION FOR
                     SUMMARY JUDGMENT

STATE OF GEORGIA
COUNTY OF __________

PERSONALLY APPEARED before the undersigned officer duly authorized to
administer oaths, Jane Doe, who, being first duly sworn, deposes and
states as follows:

1. I am the Defendant in the above-styled action and am over 18 years
   of age. I make this Affidavit upon my personal knowledge of the
   facts stated herein, and I am competent to testify to them.

2. On [date], Plaintiff served upon me a set of [DOCUMENT TYPE], a
   true and correct copy of which is attached hereto as Exhibit "A".

3. On [date], I [describe the event within personal knowledge]. A
   true and correct copy of [the document] is attached as Exhibit "B".

[...]

FURTHER AFFIANT SAYETH NAUGHT.

                                        _____________________________
                                        Jane Doe, Affiant

Sworn to and subscribed before me
this ___ day of __________, 20__.

_____________________________
Notary Public
My commission expires: __________
                                        [Notary Seal]

                          EXHIBIT LIST

Exhibit "A":   [Description]
Exhibit "B":   [Description]
```

## Unsworn declaration variant

When an unsworn declaration is permitted (or in federal court under
28 U.S.C. § 1746), replace the jurat with:

```
I declare under penalty of perjury that the foregoing is true and
correct.

Executed on [date].

                                        _____________________________
                                        Jane Doe
```

## Personal-knowledge foundation

Every paragraph must rest on **personal knowledge**; affidavits offered
on summary judgment must so state and set out facts admissible in
evidence (O.C.G.A. § 9-11-56(e)). Common foundation phrases:

- "I am the [role] in this matter and personally [participated in /
  witnessed / received] the events described."
- "I have personal knowledge of the matters stated herein and am
  competent to testify to them."
- "I reviewed the [document type] in the regular course of [my
  business / my personal records] and am familiar with its contents."

When a fact rests on **information and belief**, say so and give the
basis:

> "Upon information and belief, [fact]. The basis for this belief is
> [my review of the account statement attached as Exhibit "C"]."

## Sworn vs. argued — the cardinal rule

The affidavit's job is to **state facts**; the motion's job is to
**argue law**. Resist the urge to argue in an affidavit. For each
factual paragraph, the motion or brief should cite it as record
support: `(Doe Aff. ¶ 4)`. Run `ga-fact-check` to audit
sworn-vs-argued alignment before filing.

## Exhibits

Reference each exhibit in the relevant paragraph and attach exhibits in
order at the back. Each exhibit needs a cover page labeling it
(`EXHIBIT "A"` centered and bold) and a one-line caption describing it.
Pagination of the affidavit **continues** through the exhibits; see
`ga-statewide-format` for exhibit-handling rules.

## Composition

- For format: `ga-statewide-format`
- For the supported motion: `ga-draft-motion`
- For the proposed order: `ga-draft-order`
- For the venue overlay: `ga-fulton`, `ga-cobb`, `ga-gwinnett`,
  `ga-state-court`, `ga-magistrate`, `ga-county-courts`
- For subject matter: `ga-consumer-debt`, `ga-family-law`
- For pre-filing QC: `ga-quality-check`, `ga-fact-check`
- For pro se conventions: `ga-pro-se`

## References

- `references/affidavit-template.md` — annotated notarized-affidavit template
- `references/declaration-template.md` — unsworn-declaration variant
- `references/personal-knowledge.md` — foundation conventions
