---
name: purchase-agreement-summary
title: Purchase Agreement Summary
description: Produces structured operational summaries from fully executed residential purchase agreements for title closers and processors. Extracts parties, property identifiers, price/EMD, financing, contingencies, title/survey, HOA, closing costs, prorations, possession, and critical deadlines into scannable tables with source pointers. Flags missing data, document conflicts, unusual clauses, tight deadlines, and state-form-specific issues. Use when summarizing a purchase agreement, opening a title file, preparing escrow instructions, or reviewing contract terms for closing. For whole-transaction summaries that include closing documents and financing, use real-estate-transaction-summary instead.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/purchase-agreement-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
tags: [transactional, summary, summarization]
---

# Purchase Agreement Summary

Extracts deal-critical terms from a fully executed residential purchase agreement package into a structured operational summary for title closers and processors. The skill describes the *work*; the 15-section deliverable spec lives in `references/OUTPUT-STRUCTURE.md`, and state-form-specific watch items in `references/STATE-OVERLAYS.md`.

---

## Related skills

**Scope boundary against `real-estate-transaction-summary`:** Use **this skill** when the deliverable scope is the executed agreement plus addenda only, prepared for a title closer or processor. Use `real-estate-transaction-summary` when the scope spans the whole transaction — purchase agreement plus closing documents, financing, title, and disclosures, prepared for an attorney or matter team.

Other siblings:

- `residential-purchase-agreement`, `commercial-psa`, `commercial-real-estate-loi` — drafting equivalents.
- `closing-disclosure` — when the deal is a financed residential transaction with an issued CD.
- `closing-checklist`, `ma-closing-checklist`, `alta-settlement-statement` — downstream closing skills.
- `seller-disclosure`, `seller-disclosure-statement`, `title-commitment` — companion documents commonly in scope.
- `repair-request-addendum` — when an inspection has produced a repair request.
- `notice-to-perform-real-estate` — when a contingency deadline is approaching and the other party has not performed.
- `breach-of-purchase-agreement-complaint`, `purchase-agreement-breach-complaint` — escalation siblings if the matter pivots to litigation.

---

## Checkpoint A: pre-summary intake (mandatory)

Confirm before drafting:

1. **Fully executed purchase agreement.** All pages, all exhibits, all riders, all signatures.
2. **All addenda, amendments, and counteroffers.** Each labeled and dated.
3. **Effective date.** The date of the last signature or acceptance. If absent or ambiguous, treat as the first item in Flags & Follow-Up and run all date calculations as `[VERIFY pending effective date confirmation]`.
4. **State.** Drives form-specific watch items in `references/STATE-OVERLAYS.md`.
5. **Sub-form version.** "TREC 20-17," "C.A.R. RPA-CA Rev 12/22," etc. Required field in deliverable header.
6. **Day-count convention.** Calendar vs. business days for deadline computation. Required for status determination on the deadlines table.

If any required document is missing, flag immediately and **do not proceed**. If effective date is unavailable, ask the user; flag deadline calculations as unconfirmed.

---

## The work

**1. Normalize documents.** State scope boundary explicitly: operational extraction only, not legal advice. Label each instrument with a reference tag (e.g., "Amendment #2"). Preserve page numbers; use "PDF page X of Y" if absent. Flag amendments that modify previously extracted terms. Verify signatures and initials on all required pages; flag "execution incomplete" for any blanks.

**2. Extract parties.** Buyer(s) and seller(s) exactly as written — middle initials, suffixes, entity designations, "and/or assigns," trust names + trustee identifiers, contact info, broker / agent info.

Flag: spouse missing in a community-property state; corporate signer without officer title; name discrepancies between documents; marital or vesting language ("Confirm deed vesting instructions").

**3. Extract property identifiers.** Required: street address (with unit/city/state/zip), parcel ID / APN / PIN, legal description or exhibit reference. Flag each if missing — address-only identification is a title-search risk. Also capture: county, additional parcels / outlots / common elements, personal property included or excluded (may require Bill of Sale).

**4. Extract financial terms.**

- **Price & EMD:** current controlling purchase price, price history if amended (each price + source), each EMD deposit (amount, holder, deadline, method), escalation-clause terms.
- **Financing:** type (Cash / Conventional / FHA / VA / Other), loan amount or maximum LTV, down payment, application deadline, commitment / approval deadline.
- **Credits & concessions:** seller concessions / closing-cost credits, repair credits (separate from general — lenders treat differently), rate buy-down credits, TX option fee (paid to seller, not escrow — do not conflate with EMD). Flag any seller credit with "Confirm lender acceptability."

**5. Map critical deadlines.** Build the chronological table:

| Item | Deadline (as written) | Computed Date | Status | Source |
|---|---|---|---|---|

**Status values** (only when effective date and day-count convention are clear): Passed / Due within 48 hrs / Due within 7 days / Future / Unknown.

Cover: effective date, EMD deposits, inspection period, repair request and resolution, appraisal contingency, financing application and commitment, title commitment delivery / objection / cure, survey, HOA document delivery / review, closing date, possession date.

Flag closing on Sunday or federal holiday; "Time is of the Essence" provisions; amendments resetting deadlines; undefined day-count convention; ambiguous effective date.

**6. Title, survey, HOA, special assessments, home warranty.**

- **Title & survey:** who selects title company, owner's policy (required? who pays?), survey type / cost / deadline, title standards, permitted exceptions, commitment / objection / cure timelines, termination rights on title objections.
- **HOA / condo:** association name and contact, required disclosures, transfer-fee allocation, buyer review / termination period. Flag if documents or fees unclear.
- **Special assessments:** allocation of pending / existing. If silent: "Not stated — confirm local custom."
- **Home warranty:** cost / provider for the settlement statement.

**7. Closing costs, prorations, possession, special provisions.**

- **Cost allocations:** owner's / lender's policy, escrow / closing fee, recording fees, transfer taxes, survey, pest inspection, home warranty.
- **Prorations:** tax method (calendar vs. fiscal, current vs. last available) — verbatim. HOA dues, rents, utilities.
- **Possession:** date, time, rent-back terms, per diem, holdback / deposit, utility transfer. Flag post-closing possession as heightened risk requiring an occupancy agreement.
- **Special provisions to flag for review:** handwritten terms, tenant in property, solar lease, sale contingency, arbitration / mediation clauses, builder addenda, any non-standard clause ("Attorney or underwriter review recommended").

**8. Apply state overlays** from `references/STATE-OVERLAYS.md`. If the state is not in the overlay table, add a "State not in overlay table — local-counsel review recommended" note to Flags.

**9. Produce the 15-section deliverable** per `references/OUTPUT-STRUCTURE.md`. Every section appears, even if "Not stated" or "None identified."

---

## Checkpoint B: post-summary alignment (mandatory)

Before delivering:

1. Every term has a source pointer (document label + section / page)?
2. Every Critical and High flag has a recommended action and an owner?
3. **"Closing Day test":** if a closer would be surprised by anything missing, the summary is incomplete.
4. Disclaimer present, verbatim, at end?
5. Form version named in the header (e.g., "TREC 20-17")?
6. State overlays applied?

---

## Guardrails

- **Never fabricate.** Use "Not stated" + a follow-up flag for missing values.
- **Never resolve conflicts.** Display side-by-side with source pointers; flag for human resolution.
- **Never offer legal conclusions.** Use "Contract states…" or "Agreement provides…" — not "Buyer must…" or "This is enforceable."
- **Mask sensitive data.** Redact SSNs and account numbers; flag "Sensitive data present."
- **Never fabricate legal citations.** Use web search for verifiable sources or flag for attorney verification.
- **TRID timing.** On a financed transaction within 5 days of closing, flag "TRID timing risk" and route to `closing-disclosure`.
- **Every term needs a source pointer** (document label + section / page).

---

## Quality checklist

- [ ] Form version named in deliverable header (e.g., "TREC 20-17")
- [ ] Effective date stated explicitly; relative dates converted
- [ ] Every party name written exactly as in the documents (entity designation, suffixes, "and/or assigns")
- [ ] Every dollar amount sourced and exact
- [ ] Critical deadlines computed and status-coded
- [ ] State overlays applied or out-of-table state flagged
- [ ] All 15 deliverable sections present, in order
- [ ] Every flag categorized by severity with action and owner
- [ ] Source Map (Section 15) covers every value in the summary
- [ ] Disclaimer present verbatim
- [ ] Memo labeled AI-generated, attorney/closer review required

---

## Troubleshooting

- **Amendment conflicts with primary agreement.** Show both readings side-by-side in the affected section. Note "Amendment #N supersedes" if the amendment is properly executed and clearly modifies the term. If the amendment's modification is ambiguous, flag in Section 14 (Critical) for attorney resolution.
- **Ambiguous effective date.** Flag as the first Critical item in Section 14. Run all deadline calculations with a `[VERIFY pending effective date confirmation]` marker on the Status column.
- **Blank initials on a clause requiring separate initials** (e.g., C.A.R. liquidated damages and arbitration). Flag as Critical: clause may not be enforceable as written; closer/attorney to obtain initials.
- **Redacted financial fields.** Note the redaction in Section 14; do not fabricate the value. Some closers redact for client privacy in early file review — confirm whether unredacted version is available.
- **State form not in overlay table.** Continue with the 15-section structure; add Critical/High flag "State not in overlay table — local-counsel review recommended"; route to `real-estate-transaction-summary` if the deal scope is broader than the agreement alone.
- **Agreement references an addendum not in the file.** Section 12 lists every referenced addendum; mark missing addenda Critical. Do not extrapolate the addendum's content.
- **TX option fee mistakenly aggregated with EMD.** Option fee is paid to seller, not escrow — keep separate. Treating as EMD distorts EMD totals and refundability analysis.
- **Closing on a Sunday or federal holiday.** Flag Critical; many lenders / county recorders cannot fund or record. Closer to confirm with all parties.

---

## Required disclaimer (verbatim, end of every output)

> Operational summary for title and escrow processing only. Not legal advice. Verify all terms against the fully executed purchase agreement, counteroffers, amendments, and addenda. Flagged items require human review before reliance.

---

## References

- `references/OUTPUT-STRUCTURE.md` — full 15-section deliverable spec
- `references/STATE-OVERLAYS.md` — state-form-specific watch items

## Assets

- `assets/examples/purchase-agreement-summary-example.md` — finished summary of a synthetic TREC 20-17 transaction
