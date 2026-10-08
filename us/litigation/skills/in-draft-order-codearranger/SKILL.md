---
name: in-draft-order-codearranger
title: Draft an Indiana Proposed Order
description: 'This skill should be used when the user asks to "draft a proposed order Indiana", "Indiana proposed order template", "Indiana order granting motion", "Indiana order denying motion", "Indiana order setting hearing", "Indiana judgment entry", "Indiana proposed order Marion", "Marion CPC proposed order", "Indiana agreed order", or any related proposed-order request. Scaffolds a proposed order for judge signature. Marion CPC § II.A and most Indiana county local rules require a proposed order to accompany every motion — without one, the court may decline to rule. Trigger phrases: "Indiana proposed order", "Indiana order granting", "Marion CPC proposed order", "Indiana agreed order", "Indiana judgment proposed order".'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/in-court-docs/skills/in-draft-order
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft an Indiana Proposed Order

A proposed order is the document the judge signs to grant (or
deny) the relief sought in a motion. Indiana practice requires
a proposed order to accompany every motion — without one, the
court typically will not rule.

Two formats:

- **Proposed Order** — drafted by the movant, attached to the
  motion, with signature blank for the judge
- **Agreed Order** — signed by both parties, submitted to the
  court for the judge's countersignature

> **NOT LEGAL ADVICE.** Generated content is a drafting aid;
> the proposed order MUST match the relief sought in the motion
> exactly. Verify alignment before filing.

## Proposed Order — basic structure

The proposed order:

- Carries the same caption as the motion
- States the procedural posture (motion filed, hearing held)
- Recites findings (if necessary) — usually 1-3 short paragraphs
- States the order — what the court is ordering
- Provides a signature line for the judge
- May provide a distribution list for service

## Scaffolded proposed order

```
                     STATE OF INDIANA
                  IN THE [COURT NAME] COURT
              [COUNTY NAME] COUNTY, INDIANA

[PLAINTIFF NAME],                   )
                                    )
            Plaintiff,              )    Cause No. [###]
                                    )
        v.                          )
                                    )
[DEFENDANT NAME],                   )
                                    )
            Defendant.              )

         ORDER GRANTING DEFENDANT'S MOTION TO [RELIEF]

   This matter comes before the Court on Defendant's Motion to
[RELIEF], filed [date]. Having reviewed the motion, the
supporting memorandum, the declaration in support, any response,
and being duly advised in the premises:

   IT IS HEREBY ORDERED that Defendant's Motion to [RELIEF] is
GRANTED.

   IT IS FURTHER ORDERED that [specific relief — e.g., "the
Complaint is dismissed with prejudice as to Defendant"].

   SO ORDERED this _____ day of ____________, 20__.



                              _______________________________
                              Hon. [JUDGE NAME] / Judge
                              [COURT NAME]

Distribution:
   [Plaintiff's counsel / pro se]
   [Defendant's counsel / pro se]
```

## Findings — when to include them

For routine procedural motions (T.R. 12(B), T.R. 37(A) motion to
compel, motion to continue), the proposed order typically does
NOT include findings of fact — it simply grants or denies.

For substantive motions (T.R. 56 summary judgment, T.R. 60(B)
relief from judgment, preliminary injunction), the proposed order
SHOULD include findings:

```
   The Court finds:

   1. Plaintiff filed its Complaint on [date] seeking [relief].

   2. Defendant was served with the Complaint on [date].

   3. Defendant timely filed an Answer on [date] denying the
      material allegations.

   4. Defendant moved for summary judgment under Trial Rule 56
      on [date], supported by [evidentiary basis].

   5. Under the standard of *Jarboe v. Landmark Cmty.
      Newspapers*, 644 N.E.2d 118 (Ind. 1994), Defendant has
      affirmatively negated the [element] of Plaintiff's claim
      with admissible evidence by showing [specific finding].

   6. Plaintiff has failed to designate evidence creating a
      genuine issue of material fact on the [element].
```

Findings should be sufficient to allow appellate review under
Ind. App. R. 7. Conclusory findings ("the motion is well taken")
invite reversal.

## Order types — pattern variations

### Order Granting Motion to Dismiss

```
ORDER GRANTING DEFENDANT'S MOTION TO DISMISS
UNDER TRIAL RULE 12(B)(6)

This matter comes before the Court on Defendant's Motion to
Dismiss under Trial Rule 12(B)(6), filed [date]. ...

IT IS HEREBY ORDERED that Defendant's Motion to Dismiss is
GRANTED.

IT IS FURTHER ORDERED that Plaintiff's Complaint is DISMISSED
WITHOUT PREJUDICE [or "WITH PREJUDICE" — match what was sought]
as to Defendant.

[Optional: "Plaintiff is granted leave to file an Amended
Complaint within [#] days from entry of this Order."]
```

### Order Granting Summary Judgment

```
ORDER GRANTING DEFENDANT'S MOTION FOR SUMMARY JUDGMENT

[Findings as above]

IT IS HEREBY ORDERED that Defendant's Motion for Summary
Judgment is GRANTED.

IT IS FURTHER ORDERED that Judgment is entered in favor of
Defendant on [Plaintiff's claim(s) for ...]. The Clerk is
directed to enter Judgment accordingly.

[Optional: "Costs are awarded to Defendant under IC 34-52-1-1."]
```

### Order Granting Motion to Compel

```
ORDER GRANTING DEFENDANT'S MOTION TO COMPEL

This matter comes before the Court on Defendant's Motion to
Compel Responses to Requests for Production, filed [date],
supported by a Trial Rule 37(E) meet-and-confer certificate.
The Court finds Defendant complied with the meet-and-confer
requirement.

IT IS HEREBY ORDERED that Plaintiff shall serve full and
complete responses to Defendant's [Requests for Production /
Interrogatories] dated [date] within [#] days from entry of
this Order.

IT IS FURTHER ORDERED that Plaintiff shall pay reasonable
expenses and attorney fees incurred in making the Motion to
Compel in the amount of $______ within 30 days of entry,
pursuant to Trial Rule 37(A)(4).
```

### Order Granting Motion to Vacate Default (T.R. 60(B)(1))

```
ORDER GRANTING DEFENDANT'S MOTION FOR RELIEF FROM JUDGMENT
UNDER TRIAL RULE 60(B)(1)

This matter comes before the Court on Defendant's Motion for
Relief from Judgment under Trial Rule 60(B)(1), filed [date].
The Court finds:

   1. The default judgment was entered on [date].

   2. Defendant has shown excusable neglect by [reason], filed
      within 1 year of the default.

   3. Defendant has alleged a meritorious defense by [defense
      allegation], satisfying the requirement under *Smith v.
      Johnson*, 711 N.E.2d 1259 (Ind. 1999).

IT IS HEREBY ORDERED that the Default Judgment entered on
[date] is SET ASIDE.

IT IS FURTHER ORDERED that Defendant shall file an Answer to
Plaintiff's Complaint within 20 days of entry of this Order.

IT IS FURTHER ORDERED that the case shall proceed under the
Court's Civil Pretrial Practice and Procedure.
```

### Order Denying Motion (rare for movant's proposed order, but
provided for completeness)

```
ORDER DENYING DEFENDANT'S MOTION TO [RELIEF]

This matter comes before the Court on Defendant's Motion to
[RELIEF], filed [date]. Having reviewed the motion and the
response thereto:

IT IS HEREBY ORDERED that Defendant's Motion is DENIED.
```

## Agreed Order — bilateral

When the parties have reached agreement (e.g., on a discovery
schedule, a continuance, a stipulated protective order), they
draft an **Agreed Order**:

```
                  AGREED ORDER ON [SUBJECT]

The undersigned parties, by counsel / pro se, having agreed
that:

   1. [Term 1]
   2. [Term 2]
   3. [Term 3]

THE PARTIES JOINTLY REQUEST the Court enter the following
Order.

Agreed to:

_______________________________      _______________________________
[Plaintiff's counsel / pro se]       [Defendant's counsel / pro se]

                            ORDER

The Court, having reviewed the parties' agreement and finding
it appropriate, ORDERS as set forth above. SO ORDERED.

                              _______________________________
                              Hon. [JUDGE NAME] / Judge
```

## Distribution list

Every proposed order should include a distribution list at the
end so the clerk can serve the entered order on all parties:

```
Distribution:
   [Plaintiff's counsel name + email + Atty. No.]
   [Defendant's counsel name + email + Atty. No.]
   [Pro se party name + email + address]
```

For pro se parties, list the email address registered with
Odyssey Service Contacts. The court will serve via Odyssey
automatically once the order is entered.

## Marion Civil Division proposed-order convention

Marion CPC § II.A requires every proposed order to:

- Be filed as a separate Odyssey document (document code 12000
  for "Proposed Order")
- NOT be combined with the motion as a single PDF
- Include a "signature block" for the judge with date line
- Include the distribution list

The court enters proposed orders by stamping the original signed
proposed order with the judge's signature; the entered order
becomes the final order without further drafting.

## Composition

- `in-statewide-format` for T.R. 5(E) format + T.R. 10 caption
- `in-marion` / `in-lake` / `in-county-courts` for venue
- `in-pro-se` for self-represented signature
- `in-draft-motion` for the motion that the order resolves
- `in-submit-order` for post-hearing signed-order transmittal

## References

- `references/proposed-order-template.md` — fully scaffolded
  proposed order
- `references/agreed-order-template.md` — bilateral agreed order
- `references/findings-templates.md` — findings of fact templates
  by motion type
- `references/distribution-list.md` — Odyssey distribution
  convention

**NOT LEGAL ADVICE.** Generated content is a drafting aid; verify
against current rules and case law before filing.
