---
name: ny-draft-order-codearranger
title: Draft a New York Proposed Order
description: 'Scaffold a proposed order for a New York court. Triggers include ''draft a New York proposed order'', ''settle order New York'', ''22 NYCRR § 202.48'', ''order on submission'', ''NY decision and order'', ''60-day rule for settling order'', ''so-ordered stipulation'', ''short-form order'', ''long-form order'', ''counter-order''. Produces a proposed order conformed to NY conventions: caption + decretal paragraphs + signature line + entry date. Distinguishes the short-form order (Justice''s decretal only) from the long-form order (with detailed factual findings) and explains the settle- order procedure under 22 NYCRR § 202.48 with the 60-day submission window.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ny-court-docs/skills/ny-draft-order
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft a New York Proposed Order

> **NOT LEGAL ADVICE.** The proposed order is what the
> Justice signs after granting a motion. Errors are caught
> at signing time, so accuracy matters.

## Order types in NY practice

| Type | Use |
|------|-----|
| **Short-form order** | Justice writes decision on the proposed-order document itself ("Decision and Order"); typical for routine motion decisions |
| **Long-form order / Decision and Order** | Justice issues a separate written decision with detailed reasoning; the order is a separate document |
| **Order on Submission** | Order proposed by counsel after a motion is granted, submitted for signature |
| **Settle Order** | Court directs counsel to "settle order" — submit a proposed order within 60 days (22 NYCRR § 202.48) |
| **So-ordered Stipulation** | Parties' agreement signed by the Justice as an order |
| **Counter-Order** | Submitted by the opposing party in response to a settle-order |

## Proposed-order template

```
SUPREME COURT OF THE STATE OF NEW YORK
COUNTY OF [COUNTY]
----------------------------------------- X
[CAPTION]
                                           Index No. [#####/YYYY]
                                           Hon. [JUSTICE NAME]
                                           Part [##]
                          [Plaintiff(s),]
                                           DECISION AND ORDER
            -against-
                          [Defendant(s).]
----------------------------------------- X

[NAME OF JUSTICE], J.S.C.:

Upon the [Notice of Motion / Order to Show Cause] of
Defendant [NAME], dated [DATE], the affirmation of [NAME]
in support thereof, the memorandum of law in support
thereof, the exhibits attached, [Plaintiff's affirmation
in opposition dated [DATE], memorandum of law in
opposition, exhibits attached,] the [reply affirmation of
[NAME] dated [DATE],] [oral argument heard on [DATE],]
and all prior pleadings and proceedings, it is hereby

ORDERED that Defendant's motion is GRANTED to the extent
of [SPECIFIC RELIEF]; and it is further

ORDERED that [ADDITIONAL DECRETAL PARAGRAPH IF ANY]; and
it is further

ORDERED that this constitutes the decision and order of
the Court.

Dated: [CITY], New York
       [Month Day, Year]

                              _______________________________
                              HON. [JUSTICE NAME], J.S.C.
```

### Conventions

- **Decretal paragraphs**: each "ORDERED that..." is one
  paragraph; chain with "and it is further" between them;
  end the last with "and it is further ORDERED that this
  constitutes the decision and order of the Court"
- **Capitalize** the decretal phrase ("GRANTED", "DENIED")
- **Title**: "J.S.C." for Supreme Court Justice; "J." for
  trial-court judge in other courts
- **Date**: leave a blank for the Justice's signing date

## Settle-order procedure — 22 NYCRR § 202.48

When the Justice's decision says "Settle order on notice":

1. **Within 60 days** of the date of the decision, the
   prevailing party must submit a proposed order
2. **On notice** means: serve the proposed order on the
   opposing party at least 10 days before submission
3. **Opposing party** may serve a counter-order within 5
   days of receipt
4. Both proposed orders are submitted to chambers, who
   signs the appropriate one

Missing the **60-day deadline** is **fatal** — the right to
settle the order is **deemed abandoned** unless the court
extends. *Funk v. Barry*, 89 NY2d 364 (1996). This is a
recurring trap for pro se prevailing parties.

## Short-form order — Justice writes on the proposed order

When the Justice signs the proposed-order document itself
(rather than issuing a separate decision):

- Submit the proposed order with **blank decretal
  paragraphs** in the form expected
- Justice fills in or modifies the language
- The "Decision and Order" stamp is applied at the foot

## So-ordered stipulation

A stipulation signed by all parties + "So Ordered" by the
Justice. Used for:

- Discovery extensions
- Stipulated case-management changes
- Settlement on the record
- Adjournments of pending motions

Format:

```
SO ORDERED STIPULATION

WHEREAS [recitals];

IT IS HEREBY STIPULATED AND AGREED, by and between the
undersigned parties, that:

   1. [Stipulated term]
   2. [Stipulated term]

Dated: [...]
[Plaintiff signature]
[Defendant signature]

SO ORDERED:

_______________________________
HON. [JUSTICE NAME], J.S.C.
Date: ___________
```

## Order on submission (no oral argument)

If the motion was decided on the papers and the Justice
issued a written decision directing submission of an
order, the proposed-order title is **"Order on Submission"**
to distinguish from a decision-on-argument:

```
                                           ORDER ON SUBMISSION
```

## Tips for pro se litigants

- **Use the Justice's exact phrasing** from the decision —
  if the decision says "Defendant's motion is granted," the
  order says "Defendant's motion is granted" — not "the
  Court finds for defendant"
- **Avoid additional ruling beyond what the decision granted**
  — a proposed order seeking more than the decision
  authorized will be rejected
- **Number paragraphs** if multiple decretal items
- **Format**: 8.5×11, 1-inch margins, double-spaced, 12-pt
- **Signature line**: leave space for the Justice; do not
  pre-sign or pre-date

## Composition with other ny- skills

- `ny-statewide-format` — format baseline
- `ny-submit-order` — post-hearing submission procedure
  (settle order, counter-order, 60-day rule)
- `ny-draft-motion` — proposed order is the fourth document
  in the motion packet
- `ny-quality-check` — pre-submission QC
