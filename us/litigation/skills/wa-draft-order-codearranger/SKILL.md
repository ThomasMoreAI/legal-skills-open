---
name: wa-draft-order-codearranger
title: Draft a Proposed Order
description: Use this skill when the user asks to draft a proposed order for a Washington State court. Triggers include "draft a proposed order", "proposed order granting", "order on motion", "order for the judge to sign", "prepare the order". Scaffolds findings, relief paragraphs, and a signature block ready for judicial signature. Keeps the `[PROPOSED]` bracket in the title (removed when the judge signs). Composes with `wa-statewide-format` (always) and `wa-kcdc` (if KCDC). For post-hearing signed-order submission with bench modifications applied, use `wa-submit-order` instead.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/wa-court-docs/skills/wa-draft-order
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft a Proposed Order

Scaffold a proposed order with findings and relief pre-filled, so the
judge only needs to sign.

> **NOT LEGAL ADVICE.** This skill scaffolds a court document as
> a drafting aid. The user — not the skill — chooses the findings,
> the relief, and the form of the order. Only a judge signs an
> order; this skill prepares the proposed form for the judge's
> consideration. Verify every rule, deadline, and citation against
> current law before filing. Pair with substantive review by
> counsel where stakes warrant.

## Inputs to gather

1. **Motion** — Which motion does the order grant?
2. **Court** — Which court? Load `wa-kcdc` if KCDC.
3. **Case caption** — Party names and case number
4. **Movant** — Who presents the order?
5. **Findings** — 2–5 specific factual findings supporting relief,
   each tied to the record
6. **Relief** — Specific, enforceable relief (what, when, conditions,
   consequences)
7. **Reservation** — Does the court reserve jurisdiction to enforce?

## Steps

1. **Load the companion skills.** Read:
   - `skills/wa-statewide-format/SKILL.md`
   - `skills/wa-statewide-format/references/templates/proposed-order.md`
   - If KCDC: `skills/wa-kcdc/SKILL.md`

2. **Title the document** as "[PROPOSED] ORDER GRANTING [MOTION
   NAME]". The bracketed word is removed when the judge signs (handled
   by `wa-submit-order` post-hearing).

3. **Draft findings that are specific and record-cited.** Each
   finding should:
   - Be a complete sentence
   - State a fact (not argument)
   - Implicitly tie to a declaration paragraph or exhibit
   - Justify the relief that follows

4. **Draft relief that is enforceable and clear.** Every ordered act
   should specify:
   - Who must do it
   - What they must do
   - When it must be done
   - What happens if they fail

   Good: "Plaintiff shall produce the complete chain-of-title
   documentation for account #8795 within 14 days of this order."

   Bad: "Plaintiff shall comply with discovery."

5. **Include signature block:**
   - Judge signature line (blank date — the judge dates when signing)
   - "Presented by" block with movant's info
   - Optional "Copy received / approved as to form" line for opposing
     counsel

6. **Generate the .docx** and **deliver** via `computer://` link.

7. **Pair with** the Note for Motion Docket (use the `wa-draft-note`
   skill) so the order is listed among the filed documents.

## Notes

- Label "[PROPOSED]" — the bracket is removed on entry
- Findings justify relief; relief should be enforceable
- Never pre-fill the date
- For discovery sanctions orders, include the fee-shifting amount or
  the process for setting it
- For default judgments, include the damages amount with declaration
  citation
- After the hearing, hand off to `wa-submit-order` to strip
  `[PROPOSED]`, apply bench modifications, and submit for signature
