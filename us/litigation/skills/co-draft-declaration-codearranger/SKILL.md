---
name: co-draft-declaration-codearranger
title: Draft a Colorado Declaration
description: This skill should be used to scaffold a Colorado declaration or affidavit. Triggers include "draft a Colorado declaration", "draft an affidavit in Colorado", "declaration under C.R.S. § 13-27-104", "sworn statement Colorado", "draft a supporting affidavit", "verification under penalty of perjury Colorado". Produces a declaration (or affidavit) compliant with C.R.S. § 13-27-104 (the Colorado declaration-in-lieu-of-affidavit statute), with a proper personal-knowledge foundation, numbered paragraphs, exhibit references, and the required verification language. Colorado permits unsworn declarations under § 13-27-104 in lieu of notarized affidavits in most contexts, mirroring 28 U.S.C. § 1746.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/co-court-docs/skills/co-draft-declaration
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft a Colorado Declaration

> **NOT LEGAL ADVICE.** This skill scaffolds a declaration or
> affidavit. The signer is personally responsible for the truth of
> every statement; a declaration knowingly false in a material respect
> is perjury under C.R.S. § 18-8-502.

Use this skill in addition to `co-statewide-format` when the filing
requires sworn factual support. Colorado treats **declarations** and
**affidavits** as legally equivalent for most purposes under C.R.S.
§ 13-27-104 (Colorado's analog to 28 U.S.C. § 1746), which permits
**unsworn declarations under penalty of perjury** in lieu of
notarized affidavits.

## Declaration vs. affidavit — which to use

| | Declaration | Affidavit |
|---|---|---|
| Notarization | **None required** | Notary required |
| Authority | C.R.S. § 13-27-104 | C.R.S. § 13-90-119 (in part) |
| Verification language | "I declare under penalty of perjury pursuant to the laws of the State of Colorado that the foregoing is true and correct" | "Sworn to and subscribed before me" — notarial certificate |
| When to use | Default for most filings; fastest for pro se | When statute / rule specifically requires an affidavit (some probate, some real-property recording) |

For most district-court and county-court filings, a **declaration**
suffices. Use an affidavit only when a specific rule or statute
requires it (rare in modern Colorado practice).

## Required components

Every declaration must include:

1. **Caption** identical to the motion / pleading
2. **Document title**: e.g., `DECLARATION OF JANE DOE IN SUPPORT OF DEFENDANT'S MOTION TO COMPEL`
3. **Opening verification**: identify the declarant and the basis
   for personal knowledge
4. **Numbered paragraphs** of factual content
5. **Exhibit references** as needed
6. **Closing verification clause** (penalty-of-perjury language
   per § 13-27-104)
7. **Date and place of execution**
8. **Signature** (no notary needed for a declaration)

## Standard scaffold

```
                  [Caption — see co-statewide-format]

   DECLARATION OF JANE DOE IN SUPPORT OF DEFENDANT'S MOTION TO COMPEL

I, Jane Doe, declare as follows:

1. I am the Defendant in this action and am over 18 years of age.
   I make this Declaration based on my personal knowledge of the
   facts stated herein, except where stated on information and
   belief, in which case I believe the statements to be true.

2. On [date], Plaintiff served upon me a set of [DOCUMENT TYPE], a
   true and correct copy of which is attached hereto as Exhibit A.

3. On [date], I responded to Plaintiff's [requests / demands],
   producing the documents attached hereto as Exhibits B-D.

4. On [date], Plaintiff's counsel emailed me regarding [...]. A true
   and correct copy of the email is attached as Exhibit E.

[...]

I declare under penalty of perjury pursuant to the laws of the State
of Colorado that the foregoing is true and correct.

Executed on [date] at [city], Colorado.

                                        ____________________________
                                        Jane Doe
                                        [Address]
                                        [City, CO ZIP]
                                        [Phone]
                                        [Email]
                                        Defendant (Self-Represented)

                          EXHIBIT LIST

Exhibit A:    [Description]
Exhibit B:    [Description]
[...]
```

## Personal-knowledge foundation

Each paragraph must rest on the declarant's **personal knowledge**.
Common foundation phrases:

- "I am the [role] in this matter and personally [participated in /
  witnessed / received] the events described."
- "I have personal knowledge of the matters stated herein and could
  testify competently to them if called as a witness."
- "I reviewed the [document type] in the regular course of [my
  business / my personal records] and am familiar with its contents."

When a fact rests on **information and belief** (e.g., a fact the
declarant did not personally witness but learned from a reliable
source), say so explicitly:

> "Upon information and belief, [fact]. The basis for this belief is
> [my review of the [account statement / written contract / etc.]
> attached as Exhibit X]."

## Exhibits

Reference each exhibit in the relevant paragraph and attach exhibits
in order at the back of the declaration. Each exhibit needs:

- A **cover page** labeling it (`EXHIBIT A` centered and bold)
- A one-line italic caption describing what it is
- The exhibit content itself

Page numbering of the declaration **continues** through the exhibits
(do not restart the pagination). See `co-statewide-format` for
exhibit-handling rules.

## Sworn vs. argued — the cardinal rule

The declaration's job is to **state facts**. The motion's job is to
**argue law**. Resist the urge to argue in a declaration ("Plaintiff
is wrong because the statute of limitations bars its claim"). That
sentence belongs in the brief, not the declaration.

For each factual paragraph in the declaration, the corresponding
motion or brief should cite the paragraph as record support:
`(Doe Decl. ¶ 4)`. Run `co-fact-check` to audit sworn-vs-argued
alignment before filing.

## Verification clause — § 13-27-104

The mandatory closing verification language under C.R.S. § 13-27-104
reads:

> "I declare under penalty of perjury pursuant to the laws of the
> State of Colorado that the foregoing is true and correct."

Followed by:

> "Executed on [date] at [city], [state]."

Both lines are required. The "Executed on ... at ..." identifies
**when and where** the declaration was signed, which is sometimes
material (e.g., in capacity / jurisdiction disputes).

## When notarization is required

A handful of Colorado contexts still require **notarized affidavits**
rather than declarations:

- Some probate proofs (C.R.S. § 15-12-303 — self-proving wills)
- Recording of certain real-property instruments under C.R.S.
  art. 30 of title 38
- Certain quasi-judicial administrative hearings

For these, use a notarial certificate ("Sworn to and subscribed
before me on this ___ day of ___, 20__") and engage a Colorado
notary public (any document service center, bank, or UPS-style
store can typically notarize).

## Composition

- For format: `co-statewide-format`
- For the supported motion: `co-draft-motion`
- For the proposed order: `co-draft-order`
- For pre-filing QC: `co-quality-check`, `co-fact-check`
- For court overlay: `co-denver`, `co-arapahoe`, `co-county-courts`
- For pro se conventions: `co-pro-se`

## References

- `references/declaration-template.md` — annotated template
- `references/affidavit-template.md` — notarized-affidavit variant
- `references/crs-13-27-104.md` — full text of the declaration
  statute
- `references/personal-knowledge.md` — foundation conventions
