---
name: or-draft-order-codearranger
title: Draft an Oregon Proposed Order
description: Use this skill when the user asks to draft a proposed order for an Oregon circuit court. Triggers include "draft a proposed order", "proposed order granting", "order on motion", "order for the judge to sign", "prepare the order". Scaffolds findings, relief paragraphs, and a signature block ready for judicial signature. Keeps the `[PROPOSED]` bracket in the title (removed when the judge signs). Composes with `or-statewide-format` (always) and the relevant court skill (`or-multcc`, `or-wccc`, or `or-county-courts`). For post- hearing signed-order submission with bench modifications applied, use `or-submit-order` instead.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/or-court-docs/skills/or-draft-order
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft an Oregon Proposed Order

Scaffold a proposed order with findings and relief pre-filled,
so the judge only needs to sign.

> **NOT LEGAL ADVICE.** This skill scaffolds a court document
> as a drafting aid. The user — not the skill — chooses the
> findings, the relief, and the form of the order. Only a
> judge signs an order; this skill prepares the proposed form
> for the judge's consideration. Verify every rule, deadline,
> and citation against current law before filing. Pair with
> substantive review by counsel where stakes warrant.

## What this skill produces

A proposed order with:

1. **Caption** with `[PROPOSED]` bracket in the title
2. **Preamble** identifying the motion and what the court has
   considered
3. **Findings** (numbered, if appropriate)
4. **Order text** ("IT IS HEREBY ORDERED")
5. **Numbered relief paragraphs** (A, B, C, ...)
6. **Date and judge signature line**
7. **Submitting attorney/party block**
8. **Notice of Presentation or Approval as to Form**

## Inputs to ask the user

- **Caption**: court / county / parties / case number
- **Motion being decided**: title and filing date of the
  motion this order will resolve
- **Outcome**: granted, denied, granted in part / denied in
  part, taken under advisement
- **Specific relief**: the operative orders (produce by X,
  award fees of Y, vacate Z, etc.)
- **Findings**: factual findings, if the order rests on
  factual determinations
- **Fee award**: if a fee request, identify the statute and
  amount (or "to be determined by ORCP 68 C(2)
  Statement")
- **Submitting party**: counsel or pro se

## Template — Order Granting Motion

```
            IN THE CIRCUIT COURT OF THE STATE OF OREGON
                  FOR THE COUNTY OF MULTNOMAH

VELOCITY INVESTMENTS, LLC,      │   Case No. 25CV12345
                                │
     Plaintiff,                 │   [PROPOSED] ORDER GRANTING
                                │   DEFENDANT'S MOTION TO
     v.                         │   COMPEL PRODUCTION OF
                                │   DOCUMENTS UNDER ORCP 46 A
JOHN DOE,                       │
                                │
     Defendant.                 │
────────────────────────────────────────────────────────────

This matter came before the Court on Defendant's Motion to
Compel Production of Documents Under ORCP 46 A, filed
[date]. The Court has considered the Motion, the Memorandum
in support, the Declaration of John Doe and the Exhibits
thereto, Plaintiff's response (if any), and the records and
files of this action. The Court being fully advised in the
premises,

FINDS that:

1.  Defendant served First Requests for Production on April
    1, 2025.

2.  Plaintiff served Responses on May 1, 2025 objecting on
    grounds of "relevance, burden, and possession" without
    producing responsive documents to Requests Nos. 3, 5,
    and 6.

3.  Defendant met and conferred with Plaintiff on May 10
    and May 14, 2025 under ORCP 46 A and Multnomah SLR
    5.045. The parties were unable to resolve the discovery
    dispute.

4.  The documents requested in Requests Nos. 3, 5, and 6
    are within the scope of ORCP 36 B(1) — relevant to
    Plaintiff's claim and proportional to the needs of the
    case.

5.  Plaintiff's failure to produce was not substantially
    justified within the meaning of ORCP 46 A(4)(a).

THEREFORE, IT IS HEREBY ORDERED that:

A.  Defendant's Motion to Compel is GRANTED;

B.  Plaintiff shall produce all documents responsive to
    Requests for Production Nos. 3, 5, and 6 within 14
    calendar days of the date of this Order, or by
    ____________, 20__, whichever is sooner;

C.  Plaintiff's objections to Requests Nos. 3, 5, and 6 are
    OVERRULED;

D.  Defendant is awarded reasonable expenses, including
    attorney fees, incurred in making this Motion, pursuant
    to ORCP 46 A(4)(a). The amount of expenses and fees shall
    be determined upon Defendant's Statement of Attorney
    Fees and Costs filed under ORCP 68 C(2) within 14 days
    of this Order.

DATED this ____ day of __________, 20__.


                            _______________________________
                            CIRCUIT COURT JUDGE


Submitted by:
______________________________________
JOHN DOE
Defendant, pro se
[Address]
[Phone]
[Email]


Notice of Presentation:
This Order is being submitted to the Court without the
opportunity for opposing counsel to approve as to form,
pursuant to UTCR 5.100(2), because the Order tracks the
Court's [anticipated] ruling on this Motion.

— OR —

Approval as to Form:
______________________________________
[Plaintiff's Counsel Name, OSB # ______]
Attorney for Plaintiff Velocity Investments, LLC
```

## Template — Order Denying Motion

```
[Caption with "[PROPOSED] ORDER DENYING DEFENDANT'S MOTION
TO COMPEL"]

This matter came before the Court on Defendant's Motion to
Compel...

FINDS that [findings supporting denial]:

THEREFORE, IT IS HEREBY ORDERED that:

A.  Defendant's Motion to Compel is DENIED;

B.  [Conditions, if any]
```

## Template — Order Granting in Part / Denying in Part

```
A.  Defendant's Motion to Compel is GRANTED IN PART and
    DENIED IN PART as follows:

    1.  As to Requests Nos. 3 and 5, the Motion is GRANTED.
        Plaintiff shall produce within 14 days.

    2.  As to Request No. 6, the Motion is DENIED. Plaintiff's
        objection is sustained.

B.  ...
```

## UTCR 5.100 — Order submission

UTCR 5.100 governs the mechanics of submitting orders:

- **(1)** The party preparing the order must serve all parties
  at least 3 days before submission, unless service is excused
- **(2)** The submitting party must state in a Notice of
  Presentation whether opposing parties have had the
  opportunity to approve as to form
- **(3)** Opposing parties have 3 court days (in most courts)
  to object to the form
- **(4)** After 3 court days without objection, the order may
  be signed
- **(5)** Approval as to form is not required when the order
  tracks the court's ruling; the submitting party states this

Local SLRs (Multnomah SLR 5.100, Washington Co SLR 5.101) may
modify the procedure.

## Key drafting elements

### "[PROPOSED]" bracket

Keep `[PROPOSED]` in the title until the judge signs. The
clerk (or the prevailing party) strikes the bracket at
signature time. Same convention for `[STIPULATED]` orders.

### "IT IS HEREBY ORDERED"

The operative phrase. Without it, the document reads like a
memorandum, not an order.

### Numbered relief (A, B, C)

Each relief paragraph is **one sentence**. If a paragraph needs
explanation, the explanation goes in the Findings section, not
the ORDER section.

### Date certain

Avoid open-ended deadlines:

❌ "Plaintiff shall produce promptly"

✅ "Plaintiff shall produce within 14 calendar days of the date
of this Order, or by ____________, 20__, whichever is sooner"

The blank for the specific date is filled in when the judge
signs (typically by adding 14 calendar days to the signature
date).

### Findings

If the order rests on factual determinations (default vacation,
SJ, contempt, etc.), include findings. Findings let an appellate
court understand the basis of the ruling.

If the order is purely procedural (e.g., compelling discovery),
findings are optional but often helpful.

### Fee award

When the order awards fees:

- **Reference the statute or rule** (ORCP 46 A(4)(a), ORS
  20.105, ORS 20.096, etc.)
- **State that the amount will be determined under ORCP 68
  C(2)** — the procedural mechanism for fee statements
- **Calendar the 14-day window** for filing the Statement of
  Attorney Fees and Costs (ORCP 68 C(2))

## Oregon-specific notes

### OSB# on the submitting block

Counsel includes the OSB# (e.g., "OSB # 091234"). Pro se filers
omit — they don't have an OSB#.

### "v." between parties

In the caption. Not "vs."

### Numbered exhibits

If the order references an exhibit, use the number (Exhibit 1,
2, 3 ...).

## Pre-hearing vs. post-hearing orders

This skill drafts the **pre-hearing** proposed order — the one
filed with the motion so the judge can sign on the bench.

For the **post-hearing** version (signed by the judge with bench
modifications applied), see `or-submit-order`. The post-hearing
workflow:

1. Apply bench modifications to the proposed order (the agent
   strikes the `[PROPOSED]` bracket)
2. Re-serve under UTCR 5.100 (3 days)
3. Submit to chambers via the assigned judge's JA email

## Composition

This skill ALWAYS composes with:

- **`or-statewide-format`** — caption, format
- **The relevant court skill** — for the court header and any
  local-rule particulars

It typically follows:

- **`or-draft-motion`** — the motion this order would grant
- **`or-draft-declaration`** — the supporting declaration

## Quality checks

Before submitting:

- **`or-fact-check`** — verifies the relief tracks what the
  motion requests; that dates, amounts, and party names are
  consistent
- **`or-quality-check`** — UTCR 2.010 format pass

## Common pitfalls

| Pitfall | Consequence |
|---------|-------------|
| Missing "[PROPOSED]" in title | Order looks signed; clerk may reject |
| No "IT IS HEREBY ORDERED" phrase | Court treats as memorandum |
| Open-ended deadlines | Invites enforcement disputes |
| Inconsistent relief vs. motion | Court won't grant relief not requested |
| Missing fee authority | Award has no basis; may be reversed |
| Forgetting Notice of Presentation | UTCR 5.100 violation; possible delay |
| Wrong judge's signature line | Different from the assigned judge |

## Cross-references

- `or-statewide-format/references/templates/proposed-order.md`
  — full template
- `or-submit-order` — post-hearing signed-order submission
- `or-draft-motion` — companion motion
- `or-law-references/references/fees-and-costs.md` — fee
  award statutes and ORCP 68 mechanics
