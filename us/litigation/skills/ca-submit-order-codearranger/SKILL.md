---
name: ca-submit-order-codearranger
title: Post-Hearing Order Submission (California)
description: Use after a California superior court hearing when the judge has ruled and the prevailing party needs to submit the proposed order for signature. Triggers include "judge granted my motion", "submit a proposed order California", "CRC 3.1312", "5 court days proposed order California", "approve as to form proposed order", "judge wants Word version of order", "submit order to chambers LASC", "Department 302 proposed order submission", "Notice of Ruling California", "Notice of Entry of Order CRC 8.104". Walks the prevailing party through the CRC 3.1312 5-court-day service rule, the 5-court-day objection window for the opposing party, the per-department submission method (LASC eFiling, SFSC Dept. 302 chambers email, county variations), and the post-signature Notice of Ruling / Notice of Entry workflow that triggers the CRC 8.104 appeal clock. Layers on top of `ca-draft-order` for the order body and `ca-statewide-format` for caption / footer compliance.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ca-court-docs/skills/ca-submit-order
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Post-Hearing Order Submission (California)

> **NOT LEGAL ADVICE.** Generated content is a drafting aid;
> verify against current rules and case law before filing.

## When to use

When the user has obtained a ruling at a hearing and needs to
finalize the written order. CA practice puts the burden of
drafting and submitting the order on the **prevailing party**
unless the court orders otherwise.

If the order has not yet been drafted, use `ca-draft-order`
first.

## The CRC 3.1312 framework

California Rules of Court, rule 3.1312, governs the proposed-
order submission process for civil motions:

| Step | Deadline | Who |
|---|---|---|
| Prepare proposed order | After the ruling | Prevailing party (or as court orders) |
| Serve proposed order on other parties | **5 court days** after ruling | Prevailing party |
| Other parties may serve written objections (form only) | **5 court days** after service | Opposing parties |
| Submit to court with statement re: objections | After the 5-court-day window | Prevailing party |
| Judge signs (or revises and signs) | Court timeline | Court |
| Serve filed order on parties | Reasonable time | Prevailing party (typically) |

The 5-court-day windows use court days under CCP § 12c — exclude
weekends and judicial holidays. The first day after the ruling
is **excluded** under CCP § 12.

### Counting example

If the judge rules on Wednesday, May 13, 2026:

- Day 1 (Thursday May 14) → first court day after ruling
- Day 5 (Wednesday May 20) → 5th court day; proposed order
  must be served on parties by this day
- Opposing parties have until Wednesday May 27 (5 court days
  after service) to object to form

## Substantive vs. form objections

CRC 3.1312(a) limits objections to **form only**, not substance.
The judge's ruling is fixed at the hearing; the proposed order
must accurately reflect what the judge ruled. Objections might
be:

- The order omits a specific term the judge announced
- The order includes terms the judge did not order
- The order describes the relief incorrectly
- Specific factual recitations don't match the record

Objections are NOT a chance to relitigate the ruling.

## Submission methods (court-by-court)

### LASC

- **Method**: e-file the proposed order via Odyssey eFileCA
  with the document type "Proposed Order" or "Order After
  Hearing".
- **Working copy**: many LASC departments require a paper
  working copy delivered to chambers; check the department's
  standing order.
- **Word version**: some departments request a Microsoft Word
  copy emailed to the courtroom email address so the judge can
  edit before signing. Verify the department's preference.
- **After signature**: the signed order is filed in the case
  and served via the e-filing system; the prevailing party
  typically prepares the Notice of Entry of Order.

### SFSC

- **Method**: SFSC Department 302 has its own process —
  typically a Word version emailed to the Department 302
  email address with the proposed order attached. Verify
  the current Dept. 302 standing order.
- **Working copy**: typically not required separately from
  the e-filing.
- **After signature**: order is filed in the case docket;
  prevailing party prepares Notice of Entry.

### Orange County (OCSC)

- **Method**: each civil department has its own submission
  protocol; some accept e-filing through One Legal, others
  require email to the courtroom address. Check the
  department's website.

### Other counties

Verify the courtroom-specific submission protocol. The most
common patterns are:

1. **E-filing**: upload the proposed order through the county's
   e-filing portal with the document type "Proposed Order".
2. **Email**: send the proposed order (PDF + Word) to the
   courtroom's official email address.
3. **Hand delivery**: deliver the working copy to the clerk at
   the start of the next court day after service expires.

## The proposed-order document

See `ca-draft-order` for the full scaffold. In brief:

- **Caption**: CRC 2.111 format; title prefixed "[PROPOSED]"
  per CA practice (e.g., "[PROPOSED] ORDER GRANTING DEFENDANT'S
  MOTION TO COMPEL FURTHER RESPONSES TO REQUESTS FOR
  PRODUCTION").
- **Recitals**: date of hearing, appearances, papers
  considered.
- **Order body**: "IT IS HEREBY ORDERED that...." with specific
  operative language. For discovery orders, specify which
  items, by when. For SJ orders, include the CCP § 437c(c)
  statement of undisputed facts.
- **Signature line**: "DATED: ________ / _________, JUDGE OF
  THE SUPERIOR COURT".
- **Approval-as-to-form block** (optional but common): each
  party's signature acknowledging form (NOT substance).

## Post-signature: Notice of Entry of Order

After the judge signs the order, the prevailing party typically
prepares and serves a **Notice of Entry of Order** under CRC
8.104. This triggers the appeal clock:

- Notice of entry of judgment **served by court**: 60 days
  from service to file Notice of Appeal (CRC 8.104(a)(1)(A)).
- Notice of entry **served by a party**: 60 days from service
  by that party (CRC 8.104(a)(1)(B)).
- Otherwise: 180 days from entry of judgment (CRC 8.104(a)(1)(C)).

For a final judgment, the 60-day clock is short — serving (or
not serving) the Notice of Entry is a strategic decision.

For non-final orders (most discovery / motion-in-limine orders),
Notice of Entry is generally not required to start an appeal
clock because the orders are not appealable until final
judgment.

## CRC 2.110 footer compliance

The proposed order, like every other paper, must include a
footer per CRC 2.110 — title of the paper + page number. After
the judge signs, the title of the paper is no longer "[PROPOSED]
ORDER GRANTING..." but simply "ORDER GRANTING...". Update the
title in the footer for the Notice of Entry transmittal.

## Strategic considerations

### When you lose

You do not have to draft the order. The prevailing party drafts
it. Your role is to:

1. **Review the proposed order within the 5-court-day window**
   for form objections.
2. **Decide whether to preserve appellate issues** — the order's
   recital of "papers considered" and findings can affect
   appellate review.
3. **Consider whether the order requires Notice of Entry to
   start the appeal clock**.

### When you win

1. **Draft promptly** — getting the proposed order out in 1-2
   court days, well within the 5-day window, prevents opposing
   party delay tactics.
2. **Stay faithful to the ruling** — if you slip in language
   the judge did not actually order, opposing party will
   object (validly) and the court will revise.
3. **For monetary sanctions** — recite the amount, the
   sanctionable conduct, and the payee.
4. **Consider Notice of Entry timing** — for an appealable
   final judgment, serving Notice of Entry starts the 60-day
   clock. For ongoing litigation, you may not want to start
   it.

## Common pitfalls

- Missing the 5-court-day service window (CRC 3.1312(a)) —
  many CA judges deem the right to submit a proposed order
  forfeited if the deadline lapses, and order the opposing
  party to draft it.
- Drafting the proposed order broader than the ruling — opposing
  party will object and the court may strike or revise.
- Failing to serve the proposed order on every party of
  record (CRC 1.21).
- Importing Oregon's UTCR 5.100 3-court-day rule for transmittal
  of signed orders — California's CRC 3.1312 5-court-day rule
  is different.
- Importing Washington's order-presentment procedure (which
  varies by county).
- Forgetting the Notice of Entry of Order on a final judgment
  — opposing party may serve their own Notice of Entry first,
  potentially shortening your appeal clock.
- Not updating "[PROPOSED]" to "ORDER" in the title and footer
  of the signed version when serving Notice of Entry.

## Cross-references

- `ca-draft-order` — proposed-order body scaffold and worked
  examples
- `ca-statewide-format` — CRC 2.111 caption + CRC 2.110 footer
  compliance
- `ca-hearings` — what to expect at the hearing that produces
  the ruling
- `ca-file-packet` — assembling the post-signature transmittal
  packet including Notice of Entry
- `ca-deadlines` — CCP § 12c court-day arithmetic and CRC 8.104
  appeal-clock computation
- `scripts/case-calendar.py --rule proposed-order-serve` and
  `--rule proposed-order-object` — concrete deadline arithmetic
