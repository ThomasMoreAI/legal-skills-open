---
name: ga-submit-order-codearranger
title: Post-Hearing Order Submission (Georgia)
description: This skill should be used after a Georgia hearing, when the judge has ruled and a party needs to submit a proposed order for signature, or when the court directs a party to draft the order. Triggers include "submit a proposed order Georgia", "judge signed my order", "transmit order to chambers", "Georgia post-hearing order", "draft the order after hearing Georgia". In Georgia an order is entered when it is signed by the judge and filed with the clerk (entry equals filing under O.C.G.A. § 9-11-58). Covers preparing the proposed order to conform to the court's oral ruling, transmitting it to chambers (e-filing, lead sheet, or Word copy to the staff attorney per local practice), circulating to opposing counsel "as to form" where required, the certificate of service, and confirming the signed and entered order.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ga-court-docs/skills/ga-submit-order
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Post-Hearing Order Submission (Georgia)

> **NOT LEGAL ADVICE.** This skill is a procedural and
> drafting aid, not legal advice. Verify current rules,
> deadlines, and venue-specific practices before filing.
> Pair with substantive review by counsel where stakes
> warrant.

Use this skill after a Georgia court hearing when:

1. The judge **ruled from the bench** and directed a party to draft
   the order; or
2. The court issued a ruling and directed the prevailing party to
   submit a proposed order; or
3. The parties **agreed** to a result and need to memorialize it.

## Entry of an order in Georgia — O.C.G.A. § 9-11-58

In Georgia, an order or judgment is **entered when it is signed by
the judge and filed with the clerk** — under **O.C.G.A. § 9-11-58**,
"entry" means filing. The signed-and-filed date is what starts
post-judgment clocks (motions, appeals). The proposed order you
submit is not operative until the judge signs it and it is filed by
the clerk.

## Cardinal rule — conform the order to the ruling

The proposed order must reflect **exactly** what the judge ruled. If
the oral ruling is ambiguous:

- **Listen to the record** (court recording or reporter; obtain
  through the clerk).
- **Confer with opposing counsel** on the proper wording.
- **Do not embellish** — if the court did not address a sub-issue, do
  not slip a finding into the order.

## Standard post-hearing workflow

1. **Promptly** (per the court's directive, or within a few days)
   prepare the proposed order in `.docx`. Use `ga-draft-order` for the
   structure.
2. **Circulate to opposing counsel "as to form"** where the assigned
   judge's standing order or local practice requires it — opposing
   counsel approves that the language reflects the ruling (not the
   substance) before submission.
3. **Transmit the proposed order to chambers** by the method local
   practice requires: e-file the proposed order, attach a lead sheet,
   and/or email a Word copy to the assigned judge's **staff attorney**
   so chambers can edit and route it for signature.
4. **The judge signs** the order.
5. **The clerk files (enters) the order** under O.C.G.A. § 9-11-58 —
   this is the operative event.
6. **Serve all parties** with a certificate of service under O.C.G.A.
   § 9-11-5; registered e-filers are served through the system, any
   party not on the system by mail or hand delivery.

## Transmittal cover email — Word copy to staff attorney

```
To:      [Staff Attorney / Chambers — assigned judge]
CC:      [Opposing counsel]
Subject: Proposed Order — [Case Short Title], Case No. [Number]

Dear [Staff Attorney / Chambers]:

Pursuant to the Court's ruling at the [hearing date] hearing on
[Motion Title], I am submitting the attached proposed Order
reflecting the Court's ruling.

I circulated the proposed Order to [opposing counsel name] on
[date]. [Opposing counsel] [has approved it as to form / objects
on the following grounds: ...].

A Word-format copy is attached; the proposed Order [has been / will
be] e-filed under the case today.

Please let me know if any revisions are required before signature.

Respectfully,
[Name]
[Georgia Bar No. or "Pro Se"]
[Phone]
[Email]
```

## "As to form" approval

Where the judge requires it, opposing counsel signs or initials at
the foot of the proposed order:

```
                                   SO ORDERED, this ____ day of
                                   __________, 20__.

                                   ___________________________
                                   Judge, [Superior / State] Court
                                   [Circuit] Judicial Circuit

APPROVED AS TO FORM:

___________________________
[Opposing Counsel Name]
Georgia Bar No. ######
Attorney for [Party]
```

"As to form" means opposing counsel agrees the language **reflects
the ruling**, not that opposing counsel agrees with the substance of
the ruling. If opposing counsel objects on substance but agrees on
form, say so explicitly in the transmittal email.

## After the order is entered

Once the judge signs and the clerk files (enters) the order:

1. **Download the entered order** from the e-filing docket.
2. **Verify it matches** the proposed order — judges sometimes
   interlineate changes before signing.
3. **Calendar any deadlines** the order imposes (e.g., "Defendant
   shall serve supplemental responses within 14 days") and note that
   appeal/post-judgment clocks run from entry under O.C.G.A.
   § 9-11-58.
4. **Serve all parties** with a certificate of service; mail any
   party not on the e-filing system.
5. **Track compliance** — if the other side does not comply, prepare
   the next step (motion to compel, motion for contempt, motion to
   enforce judgment).

## Special case — orders following a bench trial or evidentiary hearing

Orders after a bench trial or evidentiary hearing typically include
**findings of fact and conclusions of law** under **O.C.G.A.
§ 9-11-52**. Draft them carefully:

- **Findings of fact** — numbered, neutrally stated, each supported
  by record evidence.
- **Conclusions of law** — separately numbered, citing the
  controlling rule or statute.
- **Order / decree** — the actual disposition.

The court is not bound by either party's proposed findings, but
well-drafted findings make it easier for the judge to adopt them.

## Special case — family-law final orders

A final divorce or other domestic order is a Superior Court judgment.
Confirm the order resolves every required issue (equitable division,
support, custody/parenting time, and child support with the worksheet
attached) and that all pre-judgment standing-order filings are on
file before the court enters the decree.

## Composition

- For drafting the proposed order: `ga-draft-order`
- For drafting any accompanying notice: `ga-draft-note`
- For getting the order before the court / chambers channels:
  `ga-fulton`, `ga-cobb`, `ga-gwinnett`
- For hearing prep and the oral ruling itself: `ga-hearings`
- For getting the matter heard in the first place:
  `ga-schedule-hearing`
- For deadlines that run from entry: `ga-deadlines`
- For format: `ga-statewide-format`
- For e-filing the entered order: `ga-file-packet`

## References

- `references/post-hearing-protocol.md` — entry under O.C.G.A.
  § 9-11-58 and chambers transmittal
- `references/proposed-order-transmittal.md` — Word copy / lead sheet
  to staff attorney; "as to form" circulation
- `references/findings-of-fact-conclusions-of-law.md`
