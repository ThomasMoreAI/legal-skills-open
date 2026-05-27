---
name: real-estate-transaction-summary
title: Real Estate Transaction Summary
description: Generates structured summaries of real estate transactions from purchase agreements, addenda, disclosures, financing documents, title commitments, and closing documents. Extracts property details, financial terms, parties, key dates, contingencies, title matters, risk allocation, and regulatory compliance into a self-contained executive summary plus thirteen-section memo. Use when summarizing a real estate deal end-to-end, creating a transaction overview, onboarding to a new matter, preparing a closing checklist, or assembling a due-diligence package. Covers residential and commercial; for agreement-only summaries prepared for title closers, defer to purchase-agreement-summary.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/real-estate-transaction-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
tags: [summarization, summary, transactional]
---

# Real Estate Transaction Summary

Produces a structured, self-contained overview of a real estate transaction — purchase agreement plus closing documents, financing, title, and disclosures — so the reader does not need to consult underlying documents for material terms.

---

## Related skills

**Scope boundary against `purchase-agreement-summary`:** Use `purchase-agreement-summary` when the deliverable scope is the executed agreement plus addenda only, prepared for a title closer or processor. Use **this skill** when the scope spans the whole transaction — purchase agreement plus closing documents, financing, title, and disclosures, prepared for an attorney or matter team.

Other siblings:

- `closing-disclosure` — for the TRID Closing Disclosure on a financed residential transaction.
- `closing-checklist` and `ma-closing-checklist` — when the deliverable is an action checklist rather than a memo.
- `alta-settlement-statement` — when the file includes an ALTA Settlement Statement to be reviewed.
- `title-commitment` — for review of the title commitment itself (exceptions, requirements, endorsements).
- `seller-disclosure`, `seller-disclosure-statement` — companion disclosure documents.
- `residential-purchase-agreement`, `commercial-psa`, `commercial-real-estate-loi` — drafting equivalents.
- `repair-request-addendum`, `notice-to-perform-real-estate` — escalation documents commonly attached.
- `breach-of-purchase-agreement-complaint`, `purchase-agreement-breach-complaint` — escalation siblings if the matter pivots to litigation.

---

## Checkpoint A: pre-summary intake (mandatory)

Confirm before drafting:

1. **Residential or commercial.** The 13-section outline applies to both, but emphasis shifts. See `references/SECTION-OUTLINE.md` "Residential vs commercial — section deltas."
2. **Jurisdiction.** State (and county/municipality if relevant). Drives transfer taxes, disclosures, statutory cancellation rights, attorney-closing rules.
3. **Document inventory.** Purchase agreement and all amendments? Addenda? Disclosures? Title commitment and any updates? Financing documents (note, mortgage / deed of trust, riders)? Closing Disclosure or ALTA Settlement Statement? HOA estoppel? Survey?
4. **Effective date.** The date that anchors all relative deadlines. If absent or ambiguous, surface as the first item in Matters Requiring Attention.
5. **Deliverable purpose.** Matter onboarding, closing prep, due diligence package, post-closing audit. Affects emphasis (e.g., closing prep weights deadlines and contingencies; due diligence weights title and compliance).
6. **Scope of summary.** Cradle-to-grave (intake through post-closing) or a phase (e.g., pre-closing only)?

If the document inventory has gaps, do not silently proceed — list missing categories in Matters Requiring Attention.

---

## The work

**1. Inventory and label.** Tag each instrument with a reference label (e.g., "PA", "Amendment #1", "Inspection Addendum", "Title Commitment dated 2024-08-12"). Preserve page numbers for citation; use "PDF page X of Y" when source pages are unnumbered. Verify executions and flag any blanks.

**2. Build the Executive Summary table** (always first).

| Field | Detail |
|-------|--------|
| Property | Legal description, address, parcel ID |
| Parties | Buyer / Seller (legal names, entity types) |
| Purchase Price | Exact dollar amount |
| Closing Date | MM/DD/YYYY |
| Key Contingencies | List critical ones |
| High-Risk Items | Unusual or time-sensitive provisions |

**3. Produce the 13 sections** per `references/SECTION-OUTLINE.md`, in order. Every section appears, even if its content is "None identified."

**4. Convert relative dates** to calendar dates throughout. "30 days after execution" must become a specific MM/DD/YYYY value (with `[VERIFY]` if the effective date is itself ambiguous).

**5. Use exact dollar amounts.** Never round. Never substitute estimates for source figures.

**6. Flag conflicts; do not resolve.** When source documents disagree, show both readings side-by-side with citations and route to "Matters Requiring Attention."

---

## Checkpoint B: post-summary alignment (mandatory)

Before delivering:

1. Every section in the 13-section outline present (including "None identified" where applicable)?
2. Every relative date converted to a calendar date?
3. Every dollar amount sourced and exact?
4. Every conflict between documents flagged in "Matters Requiring Attention" — not silently resolved?
5. Every routed deliverable (e.g., "this is a TRID transaction; CD review belongs to `closing-disclosure`") explicitly named?
6. Disclaimer present, attorney review required?

---

## What this skill does not do

- It does not give legal advice or opine on deal quality or fairness. It reports terms neutrally.
- It does not replace a title commitment review (route to `title-commitment`) or a TRID compliance review (route to `closing-disclosure`).
- It does not draft, redline, or negotiate. It summarizes the executed record.
- It does not replace attorney review of the final memo. Always label AI-generated and require sign-off.

---

## Quality checklist

- [ ] All 13 sections present, in order, with "None identified" used in lieu of silent omission
- [ ] Executive Summary table at top
- [ ] Effective date stated explicitly; relative dates converted
- [ ] Every dollar amount sourced and exact
- [ ] Every party name written exactly as in the documents (entity designation, suffixes, "and/or assigns")
- [ ] Document conflicts flagged side-by-side, not silently reconciled
- [ ] Residential vs commercial emphasis correct (per `references/SECTION-OUTLINE.md`)
- [ ] Routed downstream skills explicitly named
- [ ] Memo labeled AI-generated, attorney review required

---

## Pitfalls

- **Relative dates.** Always convert to calendar. Effective date ambiguity is a Critical flag, not a footnote.
- **Approximate amounts.** Use exact dollar figures from the documents; never round.
- **Silent conflicts.** When source documents conflict or are silent on a term, flag explicitly in Matters Requiring Attention. Showing only the most recent value silently is unsafe.
- **Editorializing.** Report terms neutrally — no commentary on deal quality, price reasonableness, or fairness.
- **Jargon balance.** Write for both attorneys and lay parties — precise language, minimal unnecessary legal jargon.
- **Closing Disclosure overlap.** This skill summarizes the transaction; it does not perform the TRID compliance review. Route detailed CD review to `closing-disclosure`.

---

## Troubleshooting

- **Source documents conflict.** Most common case is amendments that supersede earlier terms. State both readings with citations; in "Matters Requiring Attention," note "amendment #N supersedes" and identify the controlling version. Where the conflict is not clearly an amendment-supersession (e.g., disclosure says one thing, agreement says another), flag for attorney resolution.
- **Missing addenda referenced in the agreement.** The agreement says "see Inspection Addendum" and the addendum is not in the file. Surface as a Critical flag. Do not extrapolate the addendum's contents.
- **Ambiguous effective date.** Where the agreement is silent on effective date or has conflicting signature dates, flag as the first item in Matters Requiring Attention and run all date calculations as `[VERIFY pending effective date confirmation]`.
- **Post-closing rent-back unstated.** Common closing-day surprise. If buyer's possession date differs from closing date, the agreement should have a rent-back / use-and-occupancy provision; flag if missing.
- **Commercial deal, residential template.** Commercial transactions need additional emphasis on environmental, ADA, zoning, due diligence, and tenant estoppel. Use the residential/commercial deltas in `references/SECTION-OUTLINE.md`; do not omit.
- **State not in any related-skill state-overlay table.** Continue with federal-floor analysis; flag for local-counsel review of state-specific items (transfer taxes, statutory cancellation, attorney-closing rules).

---

## References

- `references/SECTION-OUTLINE.md` — full content spec for the 13 sections, plus residential/commercial deltas

## Assets

- `assets/examples/transaction-summary-example.md` — finished transaction summary for a synthetic residential SFR resale
