---
name: in-submit-order-codearranger
title: Submit a Proposed Order After Hearing (Indiana)
description: 'This skill should be used after an Indiana hearing concludes and the judge has ruled — when the user asks to "submit a proposed order Indiana", "Indiana post-hearing order", "send Marion judge proposed order Word", "Indiana submit order chambers", "Indiana order email JA", "Indiana judgment entry submission", "Indiana order after hearing", "Indiana taking matter under advisement order submission". Drafts the cover email and finalizes the proposed order for chambers submission. Marion / Lake judges typically prefer Word-format orders for internal editing; final entry is via Odyssey. Trigger phrases: "Indiana post-hearing order", "submit order Indiana", "Marion proposed order to chambers", "Indiana order in Word format", "judgment entry after hearing Indiana".'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/in-court-docs/skills/in-submit-order
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Submit a Proposed Order After Hearing (Indiana)

After the judge rules at a hearing (orally or by minute entry),
the prevailing party typically submits a finalized proposed
order for the judge's signature. This skill scaffolds:

1. The finalized proposed order (incorporating the judge's oral
   ruling)
2. The cover email or letter to the courtroom (with the order in
   Word format for chambers editing)
3. The post-entry follow-up (verifying Odyssey entry, calendaring
   subsequent deadlines)

> **NOT LEGAL ADVICE.** Generated content is a drafting aid;
> verify the submitted order matches the judge's oral ruling
> verbatim before submitting.

## When does post-hearing order submission apply?

The pattern applies when:

- The judge ruled orally at the hearing AND directed a party
  (typically the prevailing party) to prepare a proposed order
- The judge took the matter "under advisement" and later issued
  a ruling instructing a party to prepare a proposed order
- The parties reached a settlement or stipulation that requires
  a court-entered order

Common scenarios:

- T.R. 56 summary judgment: "I'm going to grant the motion;
  prevailing party draft the order."
- T.R. 60(B) motion granted: "Order setting aside default; draft
  it and circulate to opposing counsel."
- Stipulated dismissal under T.R. 41(A): "Submit an Agreed Order
  of Dismissal."
- T.R. 65 preliminary injunction granted: "Draft the order with
  the bond amount we discussed."

If the judge issues a written order from chambers without
involving counsel, this skill does NOT apply — the order is
entered directly by the court.

## Step 1 — Capture the ruling verbatim

Immediately after the hearing:

- Note the judge's exact language from the bench (consult the
  court reporter's record if available)
- Note any specific findings the judge made on the record
- Note any deadlines or conditions the judge imposed
- Note any objection from opposing counsel that should be
  reflected in the order

If the order is to be circulated to opposing counsel first
(typical for substantive orders), send a draft within 3-5
business days of the hearing.

## Step 2 — Finalize the proposed order

Use the proposed order from `in-draft-order` as the starting
point, then update to reflect the judge's actual ruling:

- Change "ORDER GRANTING [or DENYING]" to the actual disposition
- Update findings to match the judge's oral findings
- Insert any specific conditions the judge imposed
- Update the date line to the entry date (or leave blank for
  the court to fill)

## Step 3 — Circulate to opposing counsel (if appropriate)

For substantive orders, the convention is to circulate the
proposed order to opposing counsel before submitting to
chambers. Marion Civil Division CPC § II.B.4 encourages this
practice. Cover email:

```
To: [Opposing counsel email]
Subject: [Cause No.] — Proposed Order following [Date] hearing

[Counsel / Pro Se Name],

Attached is the proposed order on Defendant's Motion to
[RELIEF], reflecting [JUDGE NAME]'s ruling from the [DATE]
hearing. Please advise within 3 business days if you have
objections to form (not substance — substance was resolved at
the hearing).

If I do not hear from you by [DATE + 3 BUSINESS DAYS], I will
submit the order to chambers as drafted.

Best,
[Name]
```

If opposing counsel objects to form, work to resolve; if
irreconcilable, submit the order to chambers with a cover
explaining the dispute.

## Step 4 — Submit to chambers

Marion / Lake / Hamilton civil practice: most judges prefer the
proposed order submitted by:

1. **Email to the JA** — Word format (`.docx`) so chambers can
   edit if needed
2. **CC to opposing counsel** — for transparency
3. **Subject line**: `[Cause No.] — Proposed Order for
   [JUDGE]'s Signature`

Email template:

```
To: [JA email]
CC: [Opposing counsel email]
Subject: [Cause No.] — Proposed Order for Hon. [JUDGE]'s
         Signature Following [Date] Hearing

Dear [Judicial Assistant Name],

Attached please find the proposed order on Defendant's Motion
to [RELIEF], reflecting Hon. [JUDGE]'s ruling from the [date]
hearing. The order has been circulated to opposing counsel,
who [has approved as to form / has not responded as of this
filing / objects to form, see attached].

The order is submitted in Word format for the Court's
convenience. I have also filed a PDF version via Odyssey
(document code 12000) at [Odyssey timestamp].

Thank you,
[Name]
```

The judge will sign the order (in Word, with electronic
signature, or by printing and signing) and direct the court
clerk to enter it on Odyssey.

## Step 5 — File on Odyssey

In parallel with the email submission to chambers:

1. Log into Odyssey
2. Upload the PDF version of the proposed order (Pattern A)
3. Use document code 12000 ("Proposed Order")
4. Pay any filing fee (typically free for proposed orders)
5. Save the confirmation receipt

The court will enter the signed order on Odyssey under document
code 13000 ("Order") — the "Order" code is distinct from
"Proposed Order" 12000. Once 13000 appears, the order is final
and effective.

## Step 6 — Calendar subsequent deadlines

After the order is entered, calendar:

- **T.R. 59 motion to correct error**: 30 days from entry (if
  the order is a final judgment)
- **Notice of Appeal**: 30 days from entry (if the order is
  appealable)
- **Compliance deadline**: any specific date set by the order
  (e.g., "Plaintiff shall respond to discovery within 14 days")
- **Satisfaction of judgment**: if monetary, when paid

Use `case-calendar.py` to compute these deadlines.

## Agreed Orders — bilateral submission

When the parties have stipulated to the order (e.g., agreed
protective order, agreed scheduling order, agreed dismissal):

1. Both parties sign the order
2. Both parties' signatures appear ABOVE the judge's signature
   line
3. The order is submitted to the JA with a cover email signed
   by both
4. Opposing counsel is CC'd on every communication

Sample agreed-order cover:

```
To: [JA email]
CC: [Opposing counsel email]
Subject: [Cause No.] — AGREED Order on [SUBJECT] for Signature

Dear [JA],

The parties have stipulated to the attached Agreed Order on
[subject]. Both counsel / pro se parties have signed. We
respectfully request the Court enter the order.

Thank you,
[Names of both parties / counsel]
```

## Composition

- `in-statewide-format` for format baseline
- `in-marion` / `in-lake` / `in-county-courts` for venue
  chambers-submission conventions
- `in-pro-se` for self-represented submission
- `in-draft-order` for the starting proposed order template
- `in-hearings` for the upstream hearing that produced the
  ruling
- `in-deadlines` for post-entry deadline computation
- `in-post-judgment` for any T.R. 59 / T.R. 60(B) post-entry
  motion that may follow

## References

- `references/post-hearing-order-email.md` — JA cover email
  templates
- `references/agreed-order-template.md` — bilateral order
  scaffold
- `references/order-circulation-protocol.md` — opposing-counsel
  circulation conventions
- `references/order-vs-proposed-order-docs.md` — Odyssey 12000
  vs. 13000 document-code distinction

**NOT LEGAL ADVICE.** Generated content is a drafting aid; verify
against current rules and case law before filing.
