---
name: tn-submit-order-codearranger
title: Post-Hearing Proposed-Order Submission (Tennessee)
description: 'This skill should be used after a Tennessee hearing, when the judge has ruled and the prevailing party needs to prepare and submit the proposed order for signature, or when the court directs a party to submit an order reflecting an in-court ruling. Triggers include "submit a proposed order in Tennessee", "the judge told me to draft the order", "Tennessee order after hearing", "approved as to form Tennessee", "circulate the order to opposing counsel for approval", "submit signed order Tennessee", "Tennessee post-hearing order protocol", "draft the final decree after my divorce hearing". Covers the common Tennessee practice: the prevailing party prepares the order, circulates it to opposing counsel for approval as to form, transmits it to the judge with a cover letter, and handles entry and clerk distribution after signature.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tn-court-docs/skills/tn-submit-order
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Post-Hearing Proposed-Order Submission (Tennessee)

> **NOT LEGAL ADVICE.** This skill helps draft and submit the
> proposed order. The wording must reflect the judge's actual ruling.
> Verify the filing court's local rules on order submission.

Use this skill after a Tennessee court hearing when:

1. The judge **ruled from the bench** and directed a party (usually
   the prevailing party) to prepare the order; or
2. The court issued a ruling **conditioned** on a proposed order being
   submitted; or
3. The parties **agreed** to a result and need to memorialize it in
   an order or decree.

## The common Tennessee practice: prepare, circulate for approval, submit

In Tennessee, the customary workflow is:

1. **The prevailing party prepares the order** reflecting the
   ruling.
2. **Circulates it to opposing counsel for "approval as to form"**
   before it goes to the judge. Many Tennessee judges and local rules
   expect the order to bear opposing counsel's **"APPROVED AS TO
   FORM"** signature (or a notation that it was circulated and
   counsel did not respond / objected to form).
3. **Transmits the order to the judge** (per the court's practice —
   chambers, the Clerk & Master in Chancery, or through the e-filing
   platform) with a brief cover letter.
4. **The judge signs**, and the order is **entered** by the clerk.
5. **The clerk distributes** the entered order; the submitting party
   confirms service on all parties.

Confirm the specific court's local rule on order submission — some
courts require a set number of days to circulate for approval, some
require a specific transmittal form, and some entered-order
mechanics differ between Circuit, Chancery, and General Sessions.

## Cardinal rule — the order reflects the ruling

The proposed order must reflect exactly what the judge said. If the
ruling is ambiguous:

- **Review the record** of the hearing (request the recording or
  transcript from the clerk / court reporter)
- **Confer with opposing counsel** on the proper wording
- **Do not embellish** — if the court did not address a sub-issue, do
  not slip a finding in

## "Approved as to form" — what it means

"Approved as to form" means opposing counsel agrees the **language
accurately reflects the ruling**, *not* that opposing counsel agrees
with the **substance** of the ruling. Make this distinction explicit
in the cover letter if opposing counsel objects on substance but
agrees on form.

```
                                        ENTER:

                                        _____________________________
                                        [Judge's Name]
                                        [Circuit / Chancery] Judge
                                        [County] County, Tennessee

APPROVED AS TO FORM:

____________________________
[Opposing Counsel Name]
BPR No. #####
Attorney for [Party]
```

If opposing counsel will not respond within the time the local rule
allows, note in the transmittal that the order was circulated on
[date], counsel was given [N] days, and no objection to form was
received — then submit. Verify the local rule's exact circulation
period.

## Standard transmittal letter

```
[Date]

The Honorable [Judge Name]
[Circuit / Chancery] Court for [County] County
[Courthouse address]
[Or: via eFileTN / eFlex / Tybera per the court's practice]

RE:  [Case Short Title], Docket No. [Number]
     Proposed [Order / Final Decree] re: [Motion / matter heard]

Dear Judge [Name]:

Enclosed is a proposed [Order / Final Decree] reflecting the Court's
ruling at the hearing on [date] on [Motion title / matter]. The
proposed order has been circulated to opposing [counsel / party],
who [has approved it as to form (signature below) / was given [N]
days and did not object to its form / objects to its form on the
following grounds: ...].

Please let me know if any revisions are required before entry.

Respectfully submitted,

[Name]
[BPR # if attorney / "Pro Se" if self-represented]
[Address / Phone / Email]

cc: [Opposing counsel / party]
```

## After the order is entered

Once the judge signs and the clerk **enters** the order, it becomes
the operative document. Steps:

1. **Obtain the entered order** from the clerk / e-filing docket and
   confirm the **date of entry** — many deadlines run from entry.
2. **Verify the entered order matches** the proposed order — judges
   sometimes interlineate changes.
3. **Calendar deadlines that run from entry**, including:
   - the **non-extendable 30-day** window for a Tenn. R. Civ. P. 59
     motion to alter or amend (which tolls the appeal time);
   - the **10-day** de novo appeal window from a General Sessions
     judgment to Circuit Court (Tenn. Code Ann. § 27-5-108); and
   - any compliance deadline the order itself imposes.
4. **Confirm service** on all parties; serve any party not reached by
   the e-filing platform under Tenn. R. Civ. P. 5.
5. **Track compliance** — if the other side does not comply, prepare
   the next step (motion to enforce, motion for contempt,
   post-judgment proceedings — see `tn-post-judgment`).

## Special case — orders after a bench trial / evidentiary hearing

An order following a bench trial typically includes **findings of
fact and conclusions of law**. Draft:

- **Findings of fact** — numbered, neutrally stated, each supported
  by the record
- **Conclusions of law** — separately numbered, citing the
  controlling rule or statute
- **Order** — the actual disposition

The court is not bound by either party's proposed findings, but
clean, record-supported findings make adoption easier.

## Special case — final decree of divorce

For a family-law decree, the order must address the matters the
governing statutes require — grounds (or irreconcilable differences
under Tenn. Code Ann. § 36-4-103 with the waiting period satisfied),
equitable division of marital property under § 36-4-121, child
support per the income-shares Guidelines (Tenn. Comp. R. & Regs. ch.
1240-02-04) where children are involved, alimony under § 36-5-121 if
awarded, and any permanent parenting plan under § 36-6-401 et seq.
See `tn-family-law` for the substantive content.

## Special case — agreed order

For a result the parties have **agreed** to, the order is signed by
all parties / counsel (not merely "approved as to form") and
transmitted to the judge for entry. Make clear in the transmittal
that it is an **agreed order**.

## Composition

- For drafting the proposed order structure: `tn-draft-order`
- For filing the order through the venue's platform: `tn-file-packet`
- For court-specific submission channels and local rules:
  `tn-davidson`, `tn-shelby`, `tn-knox`, `tn-hamilton`,
  `tn-county-courts`, `tn-general-sessions`
- For family-law decrees: `tn-family-law`, `tn-family-court`
- For deadlines that run from entry (Rule 59; § 27-5-108):
  `tn-deadlines`
- For enforcement after entry: `tn-post-judgment`
- For hearing prep: `tn-hearings`

## References

- `tn-law-references` for Tenn. R. Civ. P. 58 (entry of judgment),
  Rule 59, and Tenn. Code Ann. § 27-5-108 text
- The filing court's local rules on order circulation, approval as to
  form, and transmittal — verify the circulation period and any
  required transmittal form before submitting.
