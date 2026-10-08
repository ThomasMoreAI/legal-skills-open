---
name: wa-submit-order-codearranger
title: Post-Hearing Order Submission
description: Use this skill after a hearing, when the judge has ruled and the prevailing party needs to submit the proposed order for signature. Triggers include "the judge granted the motion — let's submit the order", "prepare the signed order", "post-hearing order", "apply bench modifications", "order for signature", "the court ruled in my favor — what do I do with the proposed order". Strips the `[PROPOSED]` bracket from the title, applies bench modifications (tracked), adds an approved-as-to-form or notice-of-presentation block, prepares the chambers transmittal or e-filing submission, and tracks compliance deadlines set by the order. Composes with `wa-statewide-format`, `wa-kcdc`, `wa-quality-check`, and `wa-deadlines`. For the initial pre-hearing proposed order, use `wa-draft-order`.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/wa-court-docs/skills/wa-submit-order
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Post-Hearing Order Submission

After the judge rules from the bench, the prevailing party typically
submits the proposed order for signature — with any modifications the
court ordered at the hearing. This skill handles the post-hearing
workflow: apply bench modifications, update the caption and title,
prepare a transmittal / presentation, and file + serve the final
order.

> **NOT LEGAL ADVICE.** This skill is a procedural and drafting
> aid, not legal advice. Verify the bench ruling against the
> court's order or recording, and verify current rules and
> deadlines before transmitting. Pair with substantive review by
> counsel where stakes warrant.

## Inputs to gather

Ask the user:

1. **Case folder** — default: workspace folder
2. **Motion ruled on** — "Motion to Compel", "Motion for Default
   Judgment on Counterclaim", etc.
3. **Hearing date** — the date of the ruling
4. **Existing proposed order** — path to the version that was filed
   with the motion (or that was presented at the hearing)
5. **Ruling outcome**:
   - Granted in full (proposed order stands)
   - Granted in part / denied in part (specify what changed)
   - Taken under advisement (deferred — don't submit yet)
6. **Bench modifications** — the user's notes / recollection of what
   the judge said to add, remove, or change (ask for a plain-language
   list; the agent will translate into order language)
7. **Presentation method** — common options:
   - KCDC / district court: e-file through the portal as a signed-
     order submission
   - Superior court: working copies to chambers (varies by judge)
   - Ex parte presentation: by appointment, in person
8. **Opposing counsel approval** — will opposing counsel sign
   "approved as to form"? Required for some orders, optional for
   most.

## Steps

1. **Load the companion skills.** Read:
   - `skills/wa-statewide-format/SKILL.md`
   - `skills/wa-statewide-format/references/templates/proposed-order.md`
   - If KCDC: `skills/wa-kcdc/SKILL.md` and
     `skills/wa-kcdc/references/civil-motion-docket.md`

2. **Read the filed proposed order.** Identify:
   - Caption (court, cause number, parties)
   - Title — currently "[PROPOSED] ORDER ..."
   - Findings
   - Relief paragraphs
   - Signature block
   - Presenter block

3. **Update the title** — remove `[PROPOSED]` from the title line.
   The signed order is no longer proposed; it is the **Order**
   itself.

4. **Apply bench modifications** — for each change the user
   describes, update the relevant finding or relief paragraph. Track
   the changes:

   ```
   BENCH MODIFICATIONS APPLIED:

   - Finding ¶C — "within 14 days" changed to "within 21 days"
     (bench modification)
   - Relief ¶2 — added: "Plaintiff shall produce a privilege log
     for any withheld documents in the format set forth in CR 26(b)(5)."
   - Relief ¶6 — struck: "and shall pay reasonable attorney's fees
     as the prevailing pro se party" (court reserved this for fee
     briefing)
   - Relief ¶7 — added: "The fee-and-expense request is reserved.
     Defendant may submit a declaration and affidavit of fees
     within 14 days. Plaintiff may respond within 7 days of
     receipt."
   ```

   Show the user the tracked list; ask them to confirm each
   modification matches what the judge said.

5. **Check for inconsistencies** — after applying modifications,
   verify:
   - Findings still justify the relief granted (some relief may have
     been struck; make sure the corresponding finding is either
     struck or re-scoped)
   - Dates in the relief paragraphs are internally consistent (e.g.,
     if supplementation is due in 21 days and a bill-of-sale
     preclusion follows in "10 days thereafter," the preclusion date
     is day 31, not day 24)
   - No orphaned paragraphs referencing relief that was denied

6. **Signature block** — verify:
   - Judge's signature line is blank; do **not** pre-fill the date
   - Presenter block lists the submitting party's name, pro se
     designation (if applicable), address, phone, email
   - If opposing counsel approved as to form, add:
     ```
     Approved as to form; notice of presentation waived:

     _______________________________
     [Opposing counsel name], WSBA No. [____]
     Counsel for Plaintiff
     ```
   - If opposing counsel did **not** approve, add a notice of
     presentation block:
     ```
     NOTICE OF PRESENTATION

     PLEASE TAKE NOTICE that the undersigned will present the
     foregoing Order to Judge [name] for signature on [date] at
     [time], [courtroom / chambers / ex parte]. Opposing counsel
     was served with this Order on [date].

     DATED this ___ day of __________, 20__.
     _______________________________
     [Name], pro se
     ```

7. **Generate the final .docx.** Filename convention:
   `Order_[Short_Motion_Name]_FINAL.docx` or similar.

8. **Quality check.** Run the `wa-quality-check` skill on the .docx
   before submission.

9. **Prepare the transmittal.**

   **If KCDC (e-file)**:
   - E-file the signed-order submission through the portal
   - Document code for order submission: confirm on the current KCDC
     documents-allowed-at-portal list (commonly 460680 Proposed
     Order; post-hearing signed-order submissions may have a
     different code — check the current list at
     https://kingcounty.gov/en/court/district-court/courts-jails-legal-system/civil-filings
     before filing)
   - Include a brief transmittal cover letter OR use the portal's
     comment field to note "Order for signature — motion granted
     [hearing date]; bench modifications applied"

   **If superior court (working copies to chambers)**:
   - Prepare a cover letter to the judge's chambers
   - Deliver per the judge's standing order (email the PDF to
     chambers for most King County Superior Court judges;
     hand-deliver or mail for some judges)

   **If ex parte presentation**:
   - Schedule an appointment through the judge's bailiff
   - Bring: clean .docx + PDF + two paper copies + proof of service
     + original signed declarations if the order references them

10. **Cover letter template** (for chambers submissions):

    ```
    [Date]

    Hon. [Judge Name]
    [Court], [Courtroom / Department]
    [Address]

        Re:  Order on Motion — [Case Short Title]
             Cause No. [number]
             Hearing: [date, time]

    Dear Judge [name]:

    Enclosed for Your Honor's signature is the Order on
    [Defendant's / Plaintiff's] [Motion Title], which Your Honor
    granted [in full / in part] at the hearing on [date]. The
    Order reflects the bench modifications stated on the record:

      - [summary of modification 1]
      - [summary of modification 2]

    [If applicable: Opposing counsel has approved the Order as to
    form.] [Or: Opposing counsel was served with this Order on
    [date]; the 5-day notice of presentation has run. No objection
    to form has been received.]

    Thank you for Your Honor's time and attention.

    Respectfully,
    [Name][, pro se]
    [Phone]
    [Email]
    ```

11. **Service.** Serve opposing counsel with the signed-order
    submission per CRLJ 5 / CR 5 on the same day:
    - Email (if the parties have agreed or it's an established
      method in the case)
    - U.S. Mail (add 3 days to any response deadline)
    - Personal delivery

    Attach a Certificate of Service to the filing.

12. **After the judge signs.** Once the court enters the signed
    order:
    - Download the signed, entered order from the portal (or pick up
      from the clerk)
    - Save as `Order_[Short_Motion_Name]_SIGNED.pdf`
    - Serve the **signed, entered** order on opposing counsel (some
      judges require this as a separate step; always safer to do it)
    - Update the case calendar (via `wa-deadlines`) with any
      compliance deadlines set by the order (e.g., "Plaintiff
      supplementation due in 21 days")

13. **Final delivery.** Output:
    - Final order .docx path (with `computer://` link)
    - Cover letter .docx path (if chambers submission)
    - Filing instructions summary
    - Deadline updates to record via `wa-deadlines`

## Common pitfalls

- **Submitting a [PROPOSED] order after the hearing** — remove the
  bracket from the title; the signed order isn't proposed
- **Pre-filling the signature date** — never. The judge dates the
  order when signing
- **Forgetting opposing counsel's approval line** — even when they
  didn't appear for argument, if they were served and declined to
  object, document it
- **Missing bench modifications** — if the judge said "21 days not
  14," the order needs to say 21; the clerk won't catch this
- **Relief exceeding what was granted** — if the court reserved
  fees, don't include the fee amount; reserve it expressly
- **Title / caption drift** — use exactly the same caption as the
  motion; do not abbreviate party names or case number

## Notes

- **Under advisement**: if the judge did not rule at the hearing,
  don't submit. Wait for the written ruling. The court will usually
  direct who drafts the order after issuing the written ruling
- **Ex parte vs. presentation**: most civil-motion orders do not
  require a separate presentation appearance — the order is
  presented for signature with the post-hearing submission. Some
  judges require a five-day notice of presentation before the order
  is signed if the order was not signed at the bench
- **Competing orders**: if opposing counsel submits their own
  version of the order, the court usually expects the prevailing
  party to object in writing. Do not let opposing counsel's version
  be signed without review
- **KCDC specific**: the calendar clerks will typically not sign
  orders; orders are signed by the judge in chambers post-hearing or
  emailed back to chambers after portal filing. Confirm the judge's
  standing practice
