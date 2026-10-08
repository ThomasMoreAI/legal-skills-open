---
name: or-submit-order-codearranger
title: Post-Hearing Order Submission — Oregon
description: Use this skill after a hearing, when the judge has ruled and the prevailing party needs to submit the proposed order for signature. Triggers include "the judge granted the motion — let's submit the order", "prepare the signed order", "post- hearing order", "apply bench modifications", "order for signature", "the court ruled in my favor — what do I do with the proposed order". Strips the `[PROPOSED]` bracket from the title, applies bench modifications (tracked), adds an approved-as-to-form or notice-of-presentation block, prepares the chambers transmittal or File and Serve "Order — Proposed" submission, and tracks compliance deadlines set by the order. Composes with `or-statewide-format`, the relevant court skill (`or-multcc`, `or-wccc`, `or-county-courts`), `or-quality-check`, and `or-deadlines`. For the initial pre- hearing proposed order, use `or-draft-order`.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/or-court-docs/skills/or-submit-order
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Post-Hearing Order Submission — Oregon

After the judge rules from the bench (or by written order),
the prevailing party typically submits the proposed order for
signature — with any modifications the court ordered at the
hearing. This skill handles the post-hearing workflow.

> **NOT LEGAL ADVICE.** This skill is a procedural and drafting
> aid, not legal advice. Verify the bench ruling against the
> court's order or recording, and verify current rules and
> deadlines before transmitting. Pair with substantive review
> by counsel where stakes warrant.

## Three post-hearing scenarios

### Scenario 1: Judge rules from the bench

The judge announces the ruling during the hearing, sometimes
with specific modifications to the proposed order ("I'm
granting this, but I want the production deadline at 21 days,
not 14"). The prevailing party:

1. Notes the bench modifications carefully
2. Applies them to the proposed order (tracked changes if
   sharing with opposing for approval as to form)
3. Removes the "[PROPOSED]" bracket from the title
4. Re-serves the modified order on opposing under UTCR 5.100
5. After 3 court days without objection, submits to chambers
   for signature

### Scenario 2: Court takes under advisement

The court will rule by written order, typically 2–6 weeks
later. The prevailing party (once the ruling issues):

1. Reviews the court's written order
2. If the order is fully self-executing (the court drafted
   it), no further submission required
3. If the order directs the prevailing party to submit a
   proposed order, drafts the order matching the court's
   reasoning and submits

### Scenario 3: Stipulated outcome

The parties stipulated before or during the hearing. The
prevailing party (or the parties jointly):

1. Drafts the order reflecting the stipulation
2. Title: "[STIPULATED] ORDER..." (the bracket comes off when
   the judge signs)
3. Both parties sign in the "Approved as to Form" line
4. Submitted to chambers

## Step-by-step (Scenario 1 — most common)

### Step 1: Capture bench modifications

During the hearing, write down the specific modifications the
court directed. Examples:

- "Production deadline extended to 21 days, not 14"
- "Plaintiff's objection to RFP 6 sustained; production
  required only for RFPs 3 and 5"
- "Fee award reduced to $1,500 from the requested $2,400"
- "Defendant's request for protective order denied without
  prejudice"

If unclear, ask the court for clarification before leaving the
hearing.

### Step 2: Apply modifications

Edit the proposed order:

- Update the relevant relief paragraphs (A, B, C ...)
- Remove the `[PROPOSED]` bracket from the title
- Update the date line — leave blank for the judge's
  signature date (the judge writes in the date when signing)
- Update the findings if the court's reasoning was different
  from the original draft

### Step 3: Re-serve under UTCR 5.100

UTCR 5.100 requires that opposing parties have **3 court
days** to object to the form of the order before submission to
the court.

Send the modified order:

```
To:      [Opposing counsel]
Subject: Proposed Order — Case No. 25CV12345, Motion to
         Compel

Counsel:

Attached is the proposed Order on Defendant's Motion to
Compel, modified to reflect the Court's rulings from the
[date] hearing:

  - [List the specific modifications applied]

If you have objections to the form, please respond within 3
court days. If we do not hear from you by [date], we will
submit the Order to chambers as drafted.

Best,
[Name][, pro se]
```

If opposing objects to the form (not the substance), negotiate
the language; if no agreement, submit with a Notice of
Presentation explaining the dispute.

### Step 4: Submit to chambers

After the 3-court-day window:

#### Multnomah / Lane / counties with JA email

Email the assigned judge's JA:

```
To:      [JA email]
Subject: Order for Signature — Case No. 25CV12345

Dear [JA Name]:

Attached is the proposed Order on Defendant's Motion to
Compel, heard on [date]. The Order has been served on
opposing counsel for 3 court days under UTCR 5.100; no
objections to form were raised (or: objections noted in the
attached Notice of Presentation).

Please present to Judge [Name] for signature at the Court's
convenience.

Both the .docx and PDF formats are attached. Once signed,
please file in the case.

Thank you,
[Name][, pro se]
```

#### File and Serve (alternative)

In some counties, the order is filed in File and Serve under
"Order — Proposed" rather than emailed to chambers. Check
the assigned judge's standing order and the local SLR.

#### Washington Co (Civil Division)

For Washington Co (Oregon), submit through Civil Division
either via email (per the assigned judge's standing order) or
File and Serve.

### Step 5: Track compliance with the signed order

Once the judge signs and the order is filed:

- **Calendar all deadlines** the order sets (production
  deadlines, payment deadlines, etc.)
- **Calendar the 14-day ORCP 68 C(2) Statement of Attorney
  Fees deadline** if fees were awarded
- **Calendar follow-up dates** — e.g., status conference, next
  motion deadline

The signed order is the operative judgment for the issue
ruled upon. Comply with the deadlines; failure to comply
exposes the non-complying party to contempt or further
motions.

## Template — modified post-hearing order

```
            IN THE CIRCUIT COURT OF THE STATE OF OREGON
                  FOR THE COUNTY OF MULTNOMAH

VELOCITY INVESTMENTS, LLC,      │   Case No. 25CV12345
                                │
     Plaintiff,                 │   ORDER GRANTING DEFENDANT'S
                                │   MOTION TO COMPEL
     v.                         │   PRODUCTION OF DOCUMENTS
                                │   UNDER ORCP 46 A
JOHN DOE,                       │
                                │
     Defendant.                 │
────────────────────────────────────────────────────────────

This matter came before the Court on Defendant's Motion to
Compel Production of Documents Under ORCP 46 A, filed
[date]. A hearing was held on [date] before the Hon.
[Judge Name]. The Court [granted / denied / granted in
part] the Motion.

THEREFORE, IT IS HEREBY ORDERED that:

A.  Defendant's Motion to Compel is GRANTED;

B.  Plaintiff shall produce all documents responsive to
    Requests for Production Nos. 3 and 5 within **21**
    calendar days of the date of this Order, or by
    ____________, 20__, whichever is sooner; [modified
    from the original 14-day proposal per the Court's
    ruling from the bench on [date]]

C.  Plaintiff's objection to Request No. 6 is sustained;

D.  Defendant is awarded reasonable expenses, including
    attorney fees, in the amount of **$1,500** [modified
    from the original $2,400 request per the Court's
    ruling]; payable within 30 days of the date of this
    Order;

E.  Defendant's Statement of Attorney Fees and Costs
    requirement under ORCP 68 C(2) is waived in light of
    the Court's specific award above.

DATED this ____ day of __________, 20__.


                            _______________________________
                            CIRCUIT COURT JUDGE


Presented by:
______________________________________
JOHN DOE
Defendant, pro se
[Address]
[Phone]
[Email]


Notice of Presentation:
This Order tracks the Court's ruling at the [date] hearing.
A copy was served on Plaintiff's counsel on [date]; the 3
court days under UTCR 5.100 have elapsed without form
objection [or: objections received and addressed as
follows: ...].
```

The key changes from the pre-hearing version:

- `[PROPOSED]` bracket removed from the title
- 14-day deadline changed to 21 (and noted as modified)
- $2,400 fee request reduced to $1,500 (and noted)
- Fee award is now specific, so ORCP 68 C(2) waived
- Notice of Presentation reflects the 3-court-day service

## Working with opposing counsel on form

For cooperative opposing counsel, "Approval as to Form" is the
clean alternative to a Notice of Presentation:

```
Approval as to Form:
______________________________________
[Plaintiff's Counsel Name, OSB # ______]
Attorney for Plaintiff Velocity Investments, LLC
```

Plaintiff's counsel signs in the "Approval as to Form" line
before submission. This eliminates any form objections and
speeds chambers' processing.

## UTCR 5.100 — Order submission timing

| Step | Timing |
|------|--------|
| Re-serve modified order on opposing | Day 0 |
| Opposing has 3 court days to object | Days 1–3 |
| Submit to chambers (if no objection) | Day 4+ |
| Judge signs | Variable (1 day to several weeks) |
| Signed order entered on docket | Same day as signing |

## Common post-hearing mistakes

| Mistake | Consequence |
|---------|-------------|
| Forgetting to remove `[PROPOSED]` from title | Order looks pre-hearing; clerk may reject |
| Not applying bench modifications | Order doesn't match ruling; judge may reject |
| Skipping the 3-court-day re-serve | UTCR 5.100 violation; opposing can move to set aside |
| Submitting via wrong route (clerk vs. chambers) | Delay; possible loss in the system |
| No Notice of Presentation when there's no Approval as to Form | UTCR 5.100(2) violation |
| Missing deadlines set by the signed order | Contempt; further motions |
| Forgetting to file the ORCP 68 C(2) Statement | Waives fee claim |

## Pro se considerations

- Drafting tone in the modified order should match the
  pre-hearing draft — clear, precise, neutral
- Be conservative in applying bench modifications — when in
  doubt, capture what the judge said and stop
- The judge's signature is on the date they signed; the
  effective date of the order is the date of entry
- Read the signed order when it's filed — if the judge made
  further modifications on the bench at signing, those bind

## Cross-references

- `or-draft-order` — pre-hearing proposed order (predecessor)
- `or-statewide-format` — caption / format
- `or-hearings` — the hearing itself
- `or-deadlines` — calendaring post-hearing deadlines
- `or-law-references/references/civil-rules.md` — UTCR 5.100
  text
