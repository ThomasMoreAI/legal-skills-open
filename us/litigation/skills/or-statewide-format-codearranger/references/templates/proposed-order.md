# Proposed Order Template (Oregon)

A proposed order is the document the prevailing party submits for
the judge's signature after the ruling. In Oregon practice, the
proposed order is **filed with the motion** (so the judge can sign
on the bench at the hearing) and then re-submitted with any bench
modifications post-hearing.

## Structure

1. Caption (court header + parties + case number + title with
   "[PROPOSED]" bracket)
2. Findings (if the order rests on factual determinations)
3. Conclusions / Rulings (numbered)
4. ORDER text ("IT IS HEREBY ORDERED")
5. Date and signature line for the judge
6. Notice of Presentation / Approval as to Form lines (for
   opposing party)
7. Submitting attorney/party block

## Scaffolded markdown

```
            IN THE CIRCUIT COURT OF THE STATE OF OREGON
                  FOR THE COUNTY OF MULTNOMAH

[PARTY A],                      │   Case No. 25CV12345
                                │
     Plaintiff,                 │   [PROPOSED] ORDER GRANTING
                                │   DEFENDANT'S MOTION TO
     v.                         │   COMPEL PRODUCTION OF
                                │   DOCUMENTS UNDER ORCP 46 A
[PARTY B],                      │
                                │
     Defendant.                 │
────────────────────────────────────────────────────────────

This matter came before the Court on Defendant's Motion to
Compel Production of Documents Under ORCP 46 A, filed [date].
The Court has considered the Motion, the Memorandum in support,
the Declaration of [Name] and the Exhibits thereto, the
Plaintiff's response (if any), and the records and files of this
action. The Court being fully advised in the premises,

FINDS that:

1.  Defendant served First Requests for Production on [date].
2.  Plaintiff served Responses on [date] objecting on the
    grounds of [grounds] without producing responsive documents.
3.  Defendant met and conferred with Plaintiff on [date] under
    ORCP 46 A and the parties' attempt to resolve the discovery
    dispute was unsuccessful.
4.  The documents requested are within the scope of ORCP 36
    B(1) — relevant to a claim or defense and proportional to
    the needs of the case.

THEREFORE, IT IS HEREBY ORDERED that:

A.  Defendant's Motion to Compel is GRANTED;

B.  Plaintiff shall produce all documents responsive to
    Requests for Production Nos. 1 through 8 within 14
    calendar days of the date of this Order, or by
    ____________, 20__, whichever is sooner;

C.  Plaintiff's objections to Requests Nos. 1 through 8 are
    OVERRULED;

D.  Defendant is awarded $___________ in reasonable expenses,
    including attorney fees, incurred in making this Motion,
    pursuant to ORCP 46 A(4)(a), to be paid within 30 calendar
    days of the date of this Order.

DATED this ____ day of __________, 20__.



                            _______________________________
                            CIRCUIT COURT JUDGE


Submitted by:
______________________________________
[FULL NAME]
[Defendant, pro se / Attorney for Defendant, OSB # ______]
[Street Address]
[City, OR ZIP]
[Phone]
[Email]


Notice of Presentation:
This Order is being submitted to the Court without the
opportunity for opposing counsel to approve as to form, pursuant
to UTCR 5.100(2), because [reason — e.g., "the order tracks
the Court's ruling at the hearing on [date]"].

— OR —

Approval as to Form:
______________________________________
[Plaintiff's Counsel Name, OSB # ______]
Attorney for Plaintiff
```

## Bracket convention — "[PROPOSED]"

Oregon practice (and UTCR 5.100) keeps the "[PROPOSED]" bracket
in the title until the judge signs. When the judge signs, the
clerk (or the prevailing party in some courts) strikes the
"[PROPOSED]" from the title. The same convention applies for
"[STIPULATED]" orders.

If you are drafting an order before the hearing, the title
includes the bracket. After the hearing, when re-submitting the
signed order, the bracket comes out — that's `or-submit-order`'s
job.

## UTCR 5.100 — Submission of orders

UTCR 5.100 governs the mechanics:

- (1) The party preparing the order must serve all parties (or
  their counsel) at least 3 days before submitting to the court
  for signature, unless service is excused
- (2) The submitting party must state in a Notice of Presentation
  whether opposing parties have had the opportunity to approve as
  to form
- (3) The opposing party has 3 court days (in most courts) to
  object to the form
- (4) After 3 court days without objection, the order may be
  signed
- (5) Approval as to form is not required when the order tracks
  the court's ruling exactly; the submitting party must state
  this on the Notice of Presentation

Local SLRs may vary the timeline — Multnomah SLR 5.100 is the
controlling local version.

## Common drafting mistakes

1. **Forgetting "IT IS HEREBY ORDERED"**. The court needs to see
   the operative phrase to recognize this as an order rather than
   a memorandum.
2. **Burying the relief in a long narrative**. Each numbered
   relief paragraph (A, B, C) should be one sentence. If you
   need to explain *why* relief is granted, do it in the Findings
   section, not in the ORDER section.
3. **Open-ended deadlines**. "Plaintiff shall produce promptly"
   is enforceable but invites disputes. Use a date certain
   ("within 14 calendar days of the date of this Order, or by
   [specific date], whichever is sooner") so the court has a
   clean enforcement date.
4. **Missing the OSB number**. If the submitting party is an
   attorney, the Oregon State Bar number is required on the
   signature block. Pro se filers omit the OSB # (and write "pro
   se" instead).
5. **Wrong fee-shifting authority**. ORCP 46 A(4)(a) is mandatory
   for motions to compel. ORS 20.105 is for objectively
   unreasonable positions. ORS 20.075 / 20.077 are general fee-
   shifting factors. Cite the exact subsection.

## Re-submitting after the ruling

After the hearing, the prevailing party:

1. Applies any bench modifications the court announced (revising
   the proposed order in tracked changes)
2. Removes the "[PROPOSED]" bracket from the title
3. Updates the date in the "DATED this..." line to be blank for
   the judge to write
4. Re-serves the revised order on opposing counsel (giving them
   the 3 court days under UTCR 5.100 to object to form)
5. After 3 court days, submits to the court for signature via
   the assigned judge's chambers (typically by emailing the
   judicial assistant a `.docx` attached to a short cover note,
   plus a PDF — practice varies by court)

See `or-submit-order` for the post-hearing transmission workflow.
