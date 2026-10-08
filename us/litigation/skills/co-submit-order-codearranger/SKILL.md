---
name: co-submit-order-codearranger
title: Post-Hearing Proposed-Order Submission
description: 'This skill should be used after a Colorado hearing, when the judge has ruled and the prevailing party needs to submit the proposed order for signature, or when the court directs the parties to submit an order reflecting an in-court ruling. Triggers include "submit a proposed order in Colorado", "judge ordered me to draft the order", "Colorado post-hearing order", "submit signed order Colorado", "Colorado order after hearing protocol". Covers the post-hearing protocol: draft the order reflecting the ruling exactly, email a Word copy to chambers per practice standards (common in 18th JD and several Denver divisions), file the PDF through CCEFS, and serve the resulting signed order on all parties.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/co-court-docs/skills/co-submit-order
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Post-Hearing Proposed-Order Submission

> **NOT LEGAL ADVICE.** This skill helps draft and submit the
> proposed order. The wording must reflect the judge's actual
> ruling.

Use this skill after a Colorado court hearing when:

1. The judge **ruled from the bench** and directed a party to draft
   the order; or
2. The court issued a written ruling **conditioned** on a proposed
   order being submitted; or
3. The parties **stipulated** to a result and need to memorialize
   it.

## Cardinal rule — the order reflects the ruling

The proposed order must reflect exactly what the judge said. If the
ruling is ambiguous:

- **Listen back to the recording** (Colorado courtrooms use JTRS —
  Judicial Tracking & Recording System; recordings are available
  through the clerk)
- **Confer with opposing counsel** on the proper wording
- **Do not embellish** — if the court did not address a sub-issue,
  do not slip a finding in

## Standard post-hearing workflow

1. **Within ~5-7 days** of the hearing (or per the court's directive
   if shorter), prepare the proposed order in `.docx` format. Use
   `co-draft-order` for the structure.
2. **Confer with opposing counsel** under C.R.C.P. 121 § 1-15(8) on
   the order's form. Many judges require **agreed-form orders** —
   that is, opposing counsel signs off on the form (not the
   substance) before submission.
3. **Email the Word copy** to chambers per the judge's practice
   standards (common in many JDs and divisions). Subject:
   `Proposed Order — [Case Short Title], Case No. [Number]`. Body
   should note the hearing date and the substantive ruling.
4. **File the PDF** through CCEFS as a Proposed Order (doc code
   "PROP" or similar). Include a brief cover paragraph noting the
   hearing date and that the order is being submitted per the
   court's directive.
5. **The judge signs** (electronically through CCEFS' bench tool
   or by physical signature in chambers).
6. **The signed order is e-served** to all parties through CCEFS;
   the filer should also **serve any pro se parties** without CCEFS
   by mail.

## Standard cover email — Word-format chambers copy

```
To:      [Division ## Chambers / JA email per judge's practice standards]
CC:      [Opposing counsel]
Subject: Proposed Order — [Case Short Title], Case No. [Number]

Dear [Division ## Judicial Assistant / Chambers]:

Pursuant to the Court's directive at the [hearing date] hearing on
[Motion Title], I am submitting the attached proposed Order
reflecting the Court's ruling.

I conferred with [opposing counsel name] regarding the form of the
proposed Order on [date]. [Opposing counsel] [agrees as to form /
objects on the following grounds: ...].

A Word-format copy is attached to this email; a PDF copy will be
e-filed through CCEFS today.

Please let me know if any revisions are required before signature.

Respectfully,
[Name]
[Reg. No. if attorney / "Self-Represented" if pro se]
[Phone]
[Email]
```

## Agreed-form orders

For **agreed-form orders**, opposing counsel signs (or initials) at
the foot:

```
                                        BY THE COURT:

                                        _____________________________
                                        [Judge's Name]
                                        District Court Judge
                                        Division ##

APPROVED AS TO FORM:

____________________________
[Opposing Counsel Name]
Reg. No. #####
Attorney for [Party]
```

"As to form" means opposing counsel agrees the language reflects the
ruling, **not** that opposing counsel agrees with the substance of
the ruling. Make this distinction explicit in the email if
opposing counsel objects on substance but agrees on form.

## After the order is signed

Once the judge signs the order, the signed order becomes the
operative document. Steps:

1. **Download the signed order** from CCEFS (it will appear as a
   new entry on the case docket within hours of signing)
2. **Verify the signed order matches** the proposed order — judges
   sometimes interlineate changes
3. **Calendar any deadlines** the order imposes (e.g., "Plaintiff
   shall serve supplemental discovery responses within 14 days")
4. **Serve pro se parties** without CCEFS by mail; CCEFS-registered
   parties are served automatically
5. **Track compliance** — if the order imposes a duty on the other
   side and they do not comply, prepare for the next step (motion
   for sanctions, motion for contempt, motion to enforce judgment)

## Special case — orders following bench trial / evidentiary hearing

Orders following a bench trial or evidentiary hearing typically
include **findings of fact and conclusions of law** under C.R.C.P.
52. Draft these carefully:

- **Findings of fact** — numbered, neutrally stated, each supported
  by record evidence
- **Conclusions of law** — separately numbered, citing the
  controlling rule or statute
- **Order** — the actual disposition

The court is **not bound** by either party's proposed findings, but
well-drafted findings make it easier for the judge to adopt them
verbatim.

## Special case — decree of dissolution

For family-law decrees, use **JDF 1116** as the starting form. The
decree must include findings on:

- Jurisdiction (residency + 91-day requirement met)
- Validity of the marriage and date
- Whether the marriage is irretrievably broken
- Division of marital property and debts
- Spousal maintenance (if any)
- Allocation of parental responsibilities (decision-making and
  parenting time)
- Child support per the C.R.S. § 14-10-115 guideline (with
  worksheet attached)
- Name restoration if requested

See `co-family-law` for the full substantive content.

## Special case — proposed order for default judgment

After a defendant fails to answer (C.R.C.P. 55(a)), the plaintiff
moves for default judgment under C.R.C.P. 55(b) and submits a
proposed order. See the default-judgment template in
`co-draft-order`.

## Composition

- For drafting the proposed order: `co-draft-order`
- For filing through CCEFS: `co-file-packet`
- For court overlay (chambers email channels): `co-denver`,
  `co-arapahoe`, `co-county-courts`
- For family-law decrees: `co-family-law`
- For hearing prep / oral argument: `co-hearings`

## References

- `references/post-hearing-protocol.md`
- `references/word-chambers-copy-email-template.md`
- `references/agreed-form-orders.md`
- `references/findings-of-fact-conclusions-of-law.md`
- `references/decree-template-dissolution.md`
