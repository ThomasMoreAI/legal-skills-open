---
name: tn-draft-order-codearranger
title: Draft a Tennessee Proposed Order
description: This skill should be used to scaffold a Tennessee proposed order for a judge's or chancellor's signature. Triggers include "draft a Tennessee proposed order", "draft an order in Tennessee", "proposed order granting motion to dismiss", "proposed order on summary judgment", "default judgment order Tennessee", "draft an order for the chancellor to sign", "order approved as to form". Produces a proposed order with the caption replicated, discrete findings, and an "IT IS THEREFORE ORDERED" decretal block, plus the judge-signature line at the foot. Notes the common Tennessee practice of circulating the proposed order to opposing counsel for approval as to form before submission, and the Rule 56 requirement that a summary-judgment order state the legal grounds for the ruling. Composes with `tn-statewide-format` for the caption, `tn-draft-motion` for the underlying motion, and `tn-submit-order` for the transmittal workflow.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tn-court-docs/skills/tn-draft-order
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft a Tennessee Proposed Order

> **NOT LEGAL ADVICE.** This skill scaffolds a proposed order. The
> filer is responsible for ensuring the order mirrors the relief the
> court actually granted and contains nothing the court did not rule
> on. Verify the current rules and local practice before submitting.

Use this skill in addition to `tn-statewide-format` when a motion,
stipulation, or hearing outcome requires a **proposed order** for the
judge's or chancellor's signature. In Tennessee, the prevailing party
typically prepares the proposed order after the court announces its
ruling; the court enters the order, and the **date of entry** (the date
the signed order is filed with the clerk) starts post-judgment clocks
such as the 30-day periods under Tenn. R. Civ. P. 59.

## Cardinal rule — the order mirrors the ruling

The proposed order's relief should **mirror exactly** what the court
ordered. Two failure modes:

- **Over-reaching**: ordering something the court did not grant —
  judges strike or modify these, and opposing counsel will object on
  "approval as to form."
- **Under-reaching**: omitting relief the court actually granted —
  leaves the order incomplete and may require a corrective order.

Cross-check the prayer for relief in the motion (`WHEREFORE...`) and
the court's oral ruling against the order's decretal block (`IT IS
THEREFORE ORDERED...`) one item at a time.

## Standard proposed-order structure

```
                [Caption — exactly matching the motion;
                 see tn-statewide-format]

           [DOCUMENT TITLE: ORDER ON DEFENDANT'S
              MOTION TO DISMISS]

This cause came before the Court on [date] upon Defendant's [Motion
Title], filed [date]. Upon consideration of the Motion, the response
(if any), the supporting affidavits and exhibits, the argument of the
parties, and the record as a whole, the Court FINDS as follows:

1. [Finding 1 — stated neutrally.]

2. [Finding 2.]

3. [Finding 3.]

Based upon the foregoing, IT IS THEREFORE ORDERED, ADJUDGED, AND
DECREED that:

A. [Defendant's Motion to Dismiss is GRANTED / DENIED.]

B. [Specific consequential relief, e.g., "Plaintiff's Complaint is
   dismissed with prejudice."]

C. [Costs are taxed to ____.]

ENTERED this ___ day of __________, 20__.

                                        ____________________________
                                        [Honorable Judge / Chancellor
                                         Name]
                                        [Circuit / Chancery] Court Judge
                                        [Judicial District]

APPROVED FOR ENTRY:

____________________________            ____________________________
[Counsel / Self-Represented Party       [Opposing counsel / party]
 for Movant; see tn-statewide-format     APPROVED AS TO FORM
 signature block]
```

## Findings vs. decretal language — keep them separate

Tennessee judges expect a clear separation between **findings** (what
the court determined, stated neutrally and numbered) and the
**decretal clause** (the lettered or numbered commands following "IT
IS THEREFORE ORDERED"). Conflating the two makes it harder for the
court to edit a finding without disturbing an order.

## Rule 56 orders must state the legal grounds

For a **summary-judgment** order under Tenn. R. Civ. P. 56, the rule
requires the order granting the motion to **state the legal grounds**
upon which the court relied. A bare "Motion granted" is insufficient.
Recite which essential element was negated, or that the nonmoving
party's evidence was insufficient as a matter of law under **Rye v.
Women's Care Center of Memphis, MPLLC, 477 S.W.3d 235 (Tenn. 2015)**
(see `tn-draft-motion`).

## Default judgment order

For a default judgment, the proposed order should recite the
predicate findings:

```
This cause came before the Court on Plaintiff's Motion for Default
Judgment. The Court FINDS:

1. Defendant was served with the Summons and Complaint on [date] as
   shown by the return of service filed [date].

2. Defendant has failed to answer or otherwise respond within the
   thirty (30) days allowed by Tenn. R. Civ. P. 12.01.

3. Plaintiff is entitled to judgment in the amount of $______,
   consisting of:
     a. Principal: $______
     b. Pre-judgment interest: $______ (state the rate and basis)
     c. Court costs: $______

IT IS THEREFORE ORDERED that judgment is entered in favor of
Plaintiff and against Defendant in the amount of $______.
```

> ⚠ **Debt-buyer default judgments — Tenn. Code Ann. § 20-6-104.** In
> a matter where the plaintiff is a "subsequent creditor" / debt-buyer
> (not the original creditor), the court may not enter a default
> judgment unless the plaintiff has presented documentation sufficient
> to show **authority to collect the debt** and **at least one document
> showing the debt's existence**. A default-judgment order in such a
> matter should reflect that this showing was made. See
> `tn-consumer-debt`.

## Approval as to form — a common Tennessee practice

It is common Tennessee practice to **circulate the proposed order to
opposing counsel for "approval as to form"** before submitting it to
the court. Opposing counsel signs an "APPROVED AS TO FORM" or
"APPROVED FOR ENTRY" line to confirm the order accurately reflects the
court's ruling — this is **not** an agreement with the result, only
with the form. Some courts and local rules require this circulation;
others permit submission with a certificate that the order was served
on the other side with an opportunity to object. Build the signature
block with an approval line, and verify the filing court's procedure.

The full transmittal workflow — circulating, collecting form approval,
and submitting the signed order to the judge or chancellor — is in
`tn-submit-order`.

## Composition

- For format and caption: `tn-statewide-format`
- For the underlying motion: `tn-draft-motion`
- For the supporting affidavit: `tn-draft-declaration`
- For circulating and submitting the signed order: `tn-submit-order`
- For the consumer-debt default-judgment requirement: `tn-consumer-debt`
- For family-law decree structure: `tn-family-law`
- For the venue overlay: `tn-davidson`, `tn-shelby`, `tn-knox`,
  `tn-hamilton`, `tn-county-courts`

## References

- `references/proposed-order-template.md` — annotated template with
  findings, decretal block, and approval-as-to-form line
- `references/default-judgment-order.md` — default-judgment findings
  and the § 20-6-104 debt-buyer note
- `references/findings-vs-decretal.md` — separating findings from
  ordering language
