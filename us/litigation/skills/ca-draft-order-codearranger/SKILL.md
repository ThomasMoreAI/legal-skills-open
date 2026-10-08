---
name: ca-draft-order-codearranger
title: Draft a California Proposed Order
description: Use this skill when the user asks to draft a proposed order for a California superior court. Triggers include "draft a proposed order California", "proposed order granting", "order on motion California", "order for the judge to sign", "prepare the order CRC 3.1312", "discovery order California", "order compelling production", "order granting summary judgment", "order sustaining demurrer". Scaffolds findings, recitals, operative relief paragraphs, and a judicial signature block ready for submission per CRC 3.1312. Keeps "[PROPOSED]" in the title until the judge signs. Composes with `ca-statewide-format` (always) and the relevant court skill (`ca-lasc`, `ca-sfsc`, or `ca-county-courts`). For post-hearing signed-order transmission with bench modifications applied, use `ca-submit-order` instead.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ca-court-docs/skills/ca-draft-order
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft a California Proposed Order

Scaffold a proposed order with recitals and relief paragraphs
pre-filled, so the judge needs only to review and sign.

## What this skill produces

A proposed order with:

1. **Caption** with "[PROPOSED]" in the document title
2. **Recitals paragraph** ("This matter came before the Court
   on...") identifying what the court has considered
3. **Findings** (numbered, if the order rests on factual
   determinations)
4. **Operative order** ("IT IS SO ORDERED" / "THE COURT ORDERS
   AS FOLLOWS")
5. **Numbered relief paragraphs** (1, 2, 3, ...)
6. **Judicial signature block**: date line + judge signature
   line
7. **Submitting-party block** (attorney or In Pro Per)
8. **Approval-as-to-form / Notice-of-Presentation block**

## Inputs to ask the user

- **Caption**: court / county / parties / case number
- **Motion decided**: title and filing date
- **Outcome**: granted, denied, granted in part / denied in
  part
- **Specific relief**: the operative orders (produce by X
  date, pay Y, sustain/overrule the demurrer, etc.)
- **Findings**: factual findings, if needed (especially for
  SJ, contempt, default, sanctions)
- **Fee award**: if fees are awarded, identify the statute
  and amount (or that it will be set by later motion)
- **Submitting party**: counsel or In Pro Per

## CRC 3.1312 — submission mechanics

California Rules of Court, rule 3.1312 governs proposed
order submission:

- **(a) Preparation**: the **prevailing party** prepares the
  proposed order
- **(a) Service**: served on all other parties within **5
  court days** of the ruling
- **(b) Objection period**: other parties have **5 court days**
  after service to submit objections as to form (not
  substance — the ruling is settled)
- **(c) Submission**: after the objection period (or after
  objections are resolved), the order is submitted to the
  court for signature
- **Bench signature option**: if the judge is willing to sign
  on the day of the hearing, the Proposed Order should be
  brought to the hearing in hard copy (or emailed to chambers
  in advance per department standing orders)

"[PROPOSED]" stays in the title until the judge signs. When
the judge signs, the clerk (or the prevailing party per the
court's practice) strikes the bracket.

## Template — Order Granting Motion to Compel

```
[UPPER-LEFT: In Pro Per / attorney info per CRC 2.111]

[UPPER-RIGHT: Case number, hearing date, dept., judge]

          SUPERIOR COURT OF THE STATE OF CALIFORNIA
                    COUNTY OF LOS ANGELES

VELOCITY CAPITAL, LLC,               )
                                     )   Case No. 25STCV12345
          Plaintiff,                 )
                                     )   [PROPOSED] ORDER
     v.                              )   GRANTING DEFENDANT'S
                                     )   MOTION TO COMPEL
JANE DOE,                            )   FURTHER RESPONSES TO
                                     )   REQUESTS FOR PRODUCTION,
          Defendant.                 )   SET ONE, UNDER CCP
                                     )   § 2031.310
                                     )
                                     )   Hearing:
                                     )   Date:   [DATE]
                                     )   Time:   [TIME]
                                     )   Dept.:  [DEPT.]
                                     )   Judge:  Hon. [NAME]


    [PROPOSED] ORDER GRANTING DEFENDANT'S MOTION TO COMPEL
   FURTHER RESPONSES TO REQUESTS FOR PRODUCTION, SET ONE,
             AND FOR MONETARY SANCTIONS

This matter came before the Court on [DATE] on Defendant Jane
Doe's Motion to Compel Further Responses to Requests for
Production, Set One, Nos. 3, 5, and 6, under CCP § 2031.310.
The Court has considered the Motion, the Memorandum of Points
and Authorities, the Declaration of Jane Doe with Exhibits A
through C, the Separate Statement of Items in Dispute, any
opposition filed by Plaintiff, any reply, and all other
pleadings and papers on file in this action.

THE COURT FINDS as follows:

    1.  Defendant served Requests for Production, Set One,
        on Plaintiff on April 1, 2025.

    2.  Plaintiff served Responses on May 1, 2025,
        interposing boilerplate objections to Requests Nos.
        3, 5, and 6, and producing no responsive documents.

    3.  Defendant met and conferred with Plaintiff per CCP
        § 2031.310(b) on May 10, 2025 (letter) and May 15,
        2025 (telephone conference). The parties were unable
        to resolve the disputes as to Requests Nos. 3, 5,
        and 6.

    4.  Plaintiff's objections to Requests Nos. 3, 5, and
        6 are without merit and do not justify the failure
        to produce responsive documents.

    5.  Plaintiff's failure to comply was without
        substantial justification within the meaning of
        CCP § 2023.030(a).

IT IS SO ORDERED:

    1.  Defendant's Motion to Compel is GRANTED.

    2.  Plaintiff shall serve verified further responses to
        Requests for Production, Set One, Nos. 3, 5, and 6,
        without objection, within 10 days of the date of
        this Order.

    3.  Plaintiff shall produce all documents responsive to
        Requests for Production, Set One, Nos. 3, 5, and 6,
        within 10 days of the date of this Order, or by
        _________________, 20__, whichever is sooner.

    4.  Plaintiff's objections to Requests Nos. 3, 5, and 6
        are OVERRULED.

    5.  Monetary sanctions are awarded to Defendant and
        against Plaintiff [and Plaintiff's counsel of record,
        jointly and severally,] in the amount of
        $____________, pursuant to CCP § 2023.030(a).
        Sanctions shall be paid within 30 days of the date
        of this Order.


DATED: _______________


                        _________________________________
                        JUDGE OF THE SUPERIOR COURT


Submitted by:

_________________________________________
JANE DOE
Defendant, In Pro Per
[Address]
[Phone]
[Email]
```

## Template — Order Denying Motion

```
[Caption with "[PROPOSED] ORDER DENYING DEFENDANT'S MOTION
TO COMPEL"]

...

THE COURT FINDS as follows:

    [Findings supporting denial]

IT IS SO ORDERED:

    1.  Defendant's Motion to Compel is DENIED.

    2.  [Conditions, if any]
```

## Template — Order Granted in Part / Denied in Part

```
IT IS SO ORDERED:

    1.  Defendant's Motion to Compel is GRANTED IN PART and
        DENIED IN PART as follows:

        a.  As to Requests Nos. 3 and 5: GRANTED. Plaintiff
            shall serve further verified responses and produce
            all responsive documents within 10 days.

        b.  As to Request No. 6: DENIED. Plaintiff's
            objection on grounds of [GROUND] is SUSTAINED.

    2.  [Fee ruling, if any]
```

## Template — Order Sustaining Demurrer

```
[Caption with "[PROPOSED] ORDER SUSTAINING DEFENDANT'S
DEMURRER TO COMPLAINT [WITH/WITHOUT LEAVE TO AMEND]"]

...

This matter came before the Court on [DATE] on Defendant's
Demurrer to Plaintiff's Complaint. ...

THE COURT FINDS:

    Plaintiff's Complaint fails to state facts sufficient
    to constitute a cause of action on the [FIRST/SECOND/ALL]
    cause(s) of action, under CCP § 430.10(e), for the
    reasons stated on the record at the hearing.

IT IS SO ORDERED:

    1.  Defendant's Demurrer to Plaintiff's Complaint is
        SUSTAINED [WITH LEAVE TO AMEND / WITHOUT LEAVE TO
        AMEND].

    2.  [If leave to amend:] Plaintiff shall file and serve
        an amended complaint within [30] days of the date
        of this Order.

    3.  [If no leave to amend:] Judgment of dismissal shall
        enter in favor of Defendant. Defendant may file a
        proposed judgment.
```

## Template — Order Granting Summary Judgment

Orders granting summary judgment under CCP § 437c must
state the undisputed material facts:

```
[Caption with "[PROPOSED] ORDER GRANTING PLAINTIFF'S MOTION
FOR SUMMARY JUDGMENT UNDER CCP § 437c"]

...

THE COURT FINDS that there is no triable issue as to any
material fact and that [Moving Party] is entitled to
judgment as a matter of law on the following undisputed
material facts (CCP § 437c(c)):

    1.  [Undisputed Fact 1]. [Evidence citation]
    2.  [Undisputed Fact 2]. [Evidence citation]
    3.  [Undisputed Fact 3]. [Evidence citation]

IT IS SO ORDERED:

    1.  [Moving Party]'s Motion for Summary Judgment is
        GRANTED.

    2.  [Moving Party] is entitled to judgment against
        [Opposing Party] on [all claims / the following
        claims: ___].

    3.  Judgment shall enter as set forth in the concurrently
        filed [Proposed Judgment / Notice of Entry of
        Judgment].
```

## Key drafting elements

### "[PROPOSED]" bracket

Keep `[PROPOSED]` in the title until the judge signs. Do
not use "PROPOSED ORDER" as a document title without the
brackets — the brackets signal that it has not yet been
signed. When the judge signs, the brackets (and the word
"PROPOSED") are struck.

Some departments specifically require `[PROPOSED]` in the
document title (e.g., LASC Civil Division). Others prefer
`PROPOSED ORDER` without brackets. Check the department's
standing orders.

### Recitals paragraph

The recitals identify:
- What motion was heard
- When it was heard
- What the court considered

The standard California form:

```
This matter came before the Court on [DATE] on [Party]'s
[Motion Title]. The Court has considered the Motion, the
Memorandum of Points and Authorities, the Declaration of
[Name] with Exhibits [X] through [Y], any opposition filed
by [Opposing Party], any reply, and all other pleadings and
papers on file in this action.
```

If there was no opposition filed, note that:

```
... any opposition filed by Plaintiff (none was filed),
any reply, and all other papers on file.
```

### Findings

Include findings when:
- The order rests on disputed factual determinations
- Appellate review may follow (findings help the appellate
  court understand the basis of the ruling)
- The relief is contingent on findings (sanctions orders;
  SJ orders)
- Required by statute (CCP § 437c(c) mandates statement of
  undisputed facts)

Skip findings for purely procedural orders where the grounds
are straightforward (e.g., a simple discovery extension).

### "IT IS SO ORDERED" vs. "THE COURT ORDERS"

Both formulations are standard in California. "IT IS SO
ORDERED" is the traditional form and is widely used across
superior court departments. Some courts use "THE COURT
HEREBY ORDERS" or "IT IS HEREBY ORDERED." All are
acceptable; use the form the judge's standing orders
prefer, if specified.

### Numbered relief paragraphs

Each numbered paragraph in the ORDER section is **one
operative instruction**. If a paragraph needs explanation,
the explanation goes in the FINDINGS section, not the
ORDER section.

### Date-certain deadlines

Avoid open-ended deadlines:

Wrong: "Plaintiff shall produce promptly"

Right: "Plaintiff shall produce all documents responsive
to Requests Nos. 3, 5, and 6 within 10 days of the date
of this Order, or by _________________, 20__, whichever
is sooner."

The blank is filled in when the judge signs (typically by
computing the deadline from the signature date).

### Fee awards

When the order awards fees or sanctions:

- **Reference the statute**: CCP § 2023.030(a) for discovery
  sanctions; CCP § 425.16(c)(1) for anti-SLAPP; CCP
  § 1021.5 for private attorney general fee awards
- **State the amount** if known at time of signing; or
  state "to be determined by noticed motion"
- **Payment deadline**: 30 days from the order is standard;
  adjust if the court specifies otherwise

## Department-specific submission practices

The method for getting the judge's signature varies by
court and department:

| Court / Dept. | Common submission method |
|---|---|
| LASC (most depts.) | E-file through LACOUNTY.GOV eFiling portal; or email chambers per dept. standing order |
| SFSC Dept. 302 | Email proposed order to dept. clerk per Dept. 302 standing order |
| Other CA superior courts | Check local rules; some courts still accept drop-box delivery to clerk's office |

When bringing an order to a hearing for bench signature:

- Bring a **clean signed hard copy** and an unsigned copy
- Offer the signed copy to the clerk after the ruling
- If the judge makes bench modifications, they will be
  marked on the copy at the hearing

For post-hearing submission after CRC 3.1312 circulation:
see `ca-submit-order`.

## Approval as to Form

After circulating the proposed order under CRC 3.1312, the
submitting party typically includes an approval block:

```
APPROVED AS TO FORM:

_________________________________________
[Opposing Counsel Name, Bar No. XXXXXX]
Attorney for [Party]
DATED: _______________
```

If the opposing party objects to **form** (not substance —
the ruling is final), the objection must be submitted within
5 court days. The submitting party can then either revise or
submit with a note explaining the dispute.

If the opposing party does not respond within 5 court days,
the order may be submitted without approval.

## Pre-hearing vs. post-hearing orders

This skill drafts the **pre-hearing** proposed order — the
one filed with the motion packet and brought to the hearing
for possible bench signature.

For the **post-hearing** version (with bench modifications
applied, circulated under CRC 3.1312, and then submitted
to chambers), see `ca-submit-order`. The post-hearing
workflow:

1. Apply bench modifications to the pre-hearing proposed
   order
2. Strike "[PROPOSED]" from the title
3. Serve on all other parties (CRC 3.1312(a): within 5
   court days)
4. Allow 5-court-day objection period (CRC 3.1312(b))
5. Submit to chambers via the department's preferred method

## Layered composition

This skill ALWAYS composes with:

- **`ca-statewide-format`** — caption, format, line numbers
- **The relevant court skill** — for court header and
  department-specific submission preferences

It typically follows:

- **`ca-draft-motion`** — the motion this order would grant
- **`ca-draft-declaration`** — the supporting declaration
- **`ca-draft-note`** — the Notice of Motion

## Quality checks

Before filing or circulating:

- **`ca-fact-check`** — verifies that the relief tracks what
  the motion requests; that dates, amounts, and party names
  are consistent
- **`ca-quality-check`** — CRC 2.100–2.119 format pass

## Common pitfalls

| Pitfall | Consequence |
|---|---|
| Missing "[PROPOSED]" in title | Order looks signed; clerk may reject or judge may be confused |
| No "IT IS SO ORDERED" phrase | Document reads as a memorandum; not operative as an order |
| Open-ended deadlines | Invites enforcement disputes and contempt motion practice |
| Relief broader than what was noticed | Court cannot grant relief not noticed; order may be challenged |
| Missing statutory basis for fee award | Award may be reversed on appeal for lack of authority |
| Forgetting CRC 3.1312 circulation | Violates rule; opposing party may object on appeal |
| SJ order without undisputed-facts statement | Missing CCP § 437c(c) requirement; appealable error |
| Wrong judge's name in signature block | Must match the assigned judge |

## Cross-references

- `ca-statewide-format/references/templates/proposed-order.md`
  — full template
- `ca-submit-order` — post-hearing signed-order submission
  and CRC 3.1312 circulation
- `ca-draft-motion` — companion motion
- `ca-law-references/references/fees-and-costs.md` — fee
  award statutes and mechanics

**NOT LEGAL ADVICE.** Generated content is a drafting aid;
verify against current rules and case law before filing.
