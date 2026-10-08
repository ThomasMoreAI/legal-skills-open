---
name: co-draft-order-codearranger
title: Draft a Colorado Proposed Order
description: This skill should be used to scaffold a Colorado proposed order for a judge's signature. Triggers include "draft a Colorado proposed order", "draft an order Colorado", "Colorado order under C.R.C.P. 121", "proposed order granting motion to compel", "decree of dissolution Colorado", "writ of garnishment order", "default judgment order Colorado". Produces a proposed order with the caption replicated, mirroring the relief sought in the underlying motion, with discrete numbered findings and a separate ordering clause; includes the judge-signature block at the foot and (for Colorado practice) a courtesy Word-format version commonly emailed separately to chambers.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/co-court-docs/skills/co-draft-order
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft a Colorado Proposed Order

> **NOT LEGAL ADVICE.** This skill scaffolds a proposed order. The
> filer is responsible for ensuring the order mirrors the relief
> sought in the underlying motion and contains nothing the court did
> not actually rule on.

Use this skill in addition to `co-statewide-format` when a motion or
stipulation requires a **Proposed Order** for the judge's signature.
Most Colorado motions must be accompanied by a proposed order under
C.R.C.P. 121 § 1-15(7).

## Cardinal rule — the proposed order mirrors the motion

The proposed order's relief should **mirror exactly** the relief
requested in the motion. Two failure modes:

- **Over-reaching**: ordering something the motion did not request —
  judges strike or modify these
- **Under-reaching**: omitting something the motion requested but
  the court might want to grant — leaves the order incomplete

Cross-check the prayer for relief in the motion (`WHEREFORE...`)
against the proposed order's ordering clause (`IT IS HEREBY
ORDERED...`) one item at a time.

## Standard proposed-order structure

```
                [Caption — exactly matching the motion]

           [DOCUMENT TITLE: ORDER ON DEFENDANT'S
              MOTION TO COMPEL DISCOVERY]

THIS MATTER comes before the Court on Defendant's Motion to Compel
Discovery (the "Motion"), filed [date]. The Court has reviewed the
Motion, the Response (if any), the Reply (if any), the supporting
declarations and exhibits, and the case file.

The Court FINDS as follows:

1. [Finding 1, e.g., "Defendant timely served Plaintiff with its
   First Set of Interrogatories and Requests for Production on
   [date]."]

2. [Finding 2, e.g., "Plaintiff did not timely respond to
   Interrogatories Nos. 3, 5, and 7 or to Requests for Production
   Nos. 2 and 8."]

3. [Finding 3, e.g., "Defendant's counsel conferred with Plaintiff's
   counsel on [date] in compliance with C.R.C.P. 121 § 1-15(8)."]

4. [Finding 4, e.g., "Plaintiff's objections are without merit
   under C.R.C.P. 26(b)(5) because they lack the required
   particularity."]

The Court CONCLUDES that good cause exists to grant the Motion.

                            ORDER

IT IS HEREBY ORDERED that:

A. Defendant's Motion to Compel Discovery is GRANTED.

B. Plaintiff shall serve, within 14 days of this Order, full and
   complete responses to Defendant's Interrogatories Nos. 3, 5, and
   7 and Requests for Production Nos. 2 and 8, without objection.

C. Pursuant to C.R.C.P. 37(a)(5), Defendant is awarded its
   reasonable expenses incurred in bringing this Motion, including
   attorneys' fees, in the amount of $______. Defendant shall
   submit a fee affidavit within 14 days of this Order.

D. The Case Management Order entered [date] is amended as follows:
   [if applicable].

DATED this ___ day of __________, 20__.

                                        BY THE COURT:

                                        _____________________________
                                        [Judge's Name]
                                        District Court Judge
                                        [Division ##]
```

## Findings vs. order — keep them separate

Colorado judges expect a clear separation between **factual findings**
(numbered, neutrally stated) and **the ordering clause** (lettered
or numbered list of specific commands). Conflating the two — e.g.,
"Because Plaintiff failed to respond and Defendant is therefore
entitled to attorneys' fees, the Court orders..." — makes it harder
for the judge to delete a finding without invalidating an order.

## Default judgment order

For default judgments under C.R.C.P. 55(b), the proposed order
must include specific findings:

```
THIS MATTER comes before the Court on Plaintiff's Motion for
Entry of Default Judgment under C.R.C.P. 55(b)(2). Having reviewed
the file, the Court FINDS:

1. Defendant was personally served with the Summons and Complaint
   on [date] per the Return of Service filed [date].

2. Defendant has not filed an answer or other responsive pleading
   within the time allowed by C.R.C.P. 12(a).

3. The Clerk entered default under C.R.C.P. 55(a) on [date].

4. Plaintiff is entitled to judgment in the amount of $_____
   consisting of:
     a. Principal: $_____
     b. Pre-judgment interest at the statutory rate of [8% under
        C.R.S. § 5-12-102 / contract rate]: $_____
     c. Filing fee: $_____
     d. Service of process: $_____
     e. Other costs: $_____

5. Post-judgment interest will accrue at the statutory rate of 8%
   per annum under C.R.S. § 5-12-102 from the date of entry until
   paid.

IT IS HEREBY ORDERED that judgment is entered in favor of Plaintiff
and against Defendant in the amount of $_____.
```

## Decree-form orders (family law)

Decrees of dissolution, legal separation, and declarations of
invalidity follow a longer structure with detailed findings on
jurisdiction, marriage, residency, marital property, debts,
maintenance, parental responsibilities, and child support. Use
**JDF 1116** (decree template) as the starting point. See
`co-family-law` for the substantive structure.

## Word-format chambers copy

In many Colorado JDs (especially the 18th JD and some Denver
divisions), the assigned judge requests an **editable Word-format**
proposed order emailed directly to chambers in addition to the PDF
filed through CCEFS. The Word copy lets the judge:

- Edit findings before signing
- Insert specific date or dollar fills
- Strike portions the court declines to grant

When the judge's practice standards call for a Word copy:

1. Save the proposed order as `.docx`
2. Email to chambers at `[division-name].chambers@judicial.state.co.us`
   or the address listed in the judge's practice standards
3. Subject line: `Proposed Order — [Case Short Title], Case No.
   [Number]`
4. Body: brief reference to the underlying motion and the CCEFS
   filing date

## Composition

- For format: `co-statewide-format`
- For the supporting motion: `co-draft-motion`
- For the supporting declaration: `co-draft-declaration`
- For the post-hearing signed-order workflow: `co-submit-order`
- For court overlay: `co-denver`, `co-arapahoe`, `co-county-courts`
- For dispositive-order specifics: `co-post-judgment`
- For family-law decrees: `co-family-law`

## References

- `references/proposed-order-template.md`
- `references/default-judgment-order.md`
- `references/findings-vs-order.md`
- `references/word-chambers-copy-protocol.md`
