---
name: closing-disclosure
title: Closing Disclosure
description: Drafts and reviews TRID-compliant U.S. residential Closing Disclosures, assembling all five pages of CFPB Form H-25, comparing to Loan Estimates, classifying tolerance buckets, flagging re-disclosure triggers, and producing a compliance review memo. Use when working with closing disclosures, CDs, TRID, Regulation Z, LE comparison, tolerance cures, cash-to-close reconciliation, settlement statements, or pre-consummation closing compliance review. Defers tolerance math to closing-disclosure-tolerance and timing math to closing-disclosure-timing-reference.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/closing-disclosure
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: finance
language: en
tags: [transactional, regulatory, drafting, analysis]
---

# Closing Disclosure

Produce a complete five-page Closing Disclosure per CFPB Form H-25 and a compliance review memo. The skill describes the *work*; specialized math and timing rules live in dedicated sibling skills.

---

## Related skills

- `closing-disclosure-tolerance` — full TRID tolerance bucket math (zero / 10% cumulative / unlimited), changed-circumstance gating, cure calculation. **Defer here for tolerance computations.**
- `closing-disclosure-timing-reference` — 3-business-day waiting period rules, deemed-receipt math, federal-holiday exclusion. **Defer here for timing computations.**
- `cd-tolerance-reference` and `trid-tolerance` — supporting reference material on tolerance edge cases.
- `alta-settlement-statement` — when the deal also produces an ALTA Settlement Statement (cash, commercial, certain assumptions); reconcile both.
- `closing-checklist` and `ma-closing-checklist` — broader pre-closing deliverables; the CD plugs into these.
- `loan-modification-agreement` — when the matter is a modification rather than a purchase or refinance.
- `seller-disclosure`, `title-commitment` — companion documents commonly in scope when reviewing the file.

---

## Checkpoint A: pre-draft intake (mandatory)

Confirm before drafting or reviewing:

1. **Role.** Lender, settlement agent, borrower's counsel, seller's counsel — the deliverable shape differs by role. Attorney roles produce an issue list and client summary, not a lender-signed CD.
2. **Deal type.** Purchase / refinance / construction-perm / assumption / modification. TRID coverage and CD requirements vary.
3. **State.** Pulls in state overlays (transfer taxes, attorney-closing rules, doc stamps). See `references/STATE-OVERLAYS.md`.
4. **Loan Estimate(s).** All LEs issued, with issue dates. The most recent valid LE is the comparison baseline.
5. **Closing timeline.** Rate-lock date and expiration, intended consummation date, CD issue/delivery dates.
6. **Source documents.** Title commitment, payoff letters, insurance binder, tax bill, HOA estoppel (if applicable), survey (if required).
7. **Jurisdiction-specific overlays.** State and county-level disclosures, fee structures, and attorney involvement rules.

If any of items 4–6 is unavailable, do not finalize — produce a partial draft with `MISSING` markers and surface the gaps in the review memo.

---

## The loop

**1. Page-by-page data intake.** Walk all five pages of Form H-25, populating each field from source documents. Flag missing fields as `MISSING`. The complete page-by-page checklist is in `references/CD-PAGES.md`.

**2. LE comparison.** The most recent valid LE is the baseline. For each fee on the CD, identify the corresponding LE line, classify into the appropriate tolerance bucket, and compute variance. **Defer all tolerance math to `closing-disclosure-tolerance`** — its workflow covers fee classification, zero/10%/unlimited testing, changed-circumstance gating, and cure calculation.

A one-paragraph orientation:

| Bucket | Rule | Typical items |
|---|---|---|
| Zero tolerance | No increase over LE without valid changed-circumstance reset | Lender/broker fees, transfer taxes, non-shoppable services, affiliate services |
| 10% cumulative | Aggregate increase ≤ 10% across the bucket | Recording fees; shoppable services from lender's list |
| Unlimited | May change if good faith | Prepaids, escrow, services from non-list providers, owner's title |

**3. Re-disclosure triggers.** A new 3-business-day waiting period before consummation is required if any of:

- APR increases > 0.125% (fixed-rate) or > 0.25% (ARM)
- Loan product changes (fixed/ARM, term, IO, neg-am)
- Prepayment penalty added

**Defer to `closing-disclosure-timing-reference`** for the full business-day counting rules, deemed-receipt computation, and federal-holiday list.

**4. State overlays.** Apply the state-specific overlay items from `references/STATE-OVERLAYS.md`. Out-of-table states get a "local-counsel review recommended" note.

**5. Cross-document reconciliation.** Cash-to-close, payoffs, recording fees, escrows, and APR/TIP each must reconcile against another document in the file. See `references/CD-PAGES.md` "Cross-document reconciliation" for the specific pairings.

**6. Produce deliverables.**

- **Lender/settlement-agent role:** the finalized CD plus a short reviewer's note attaching the LE comparison, tolerance findings, re-disclosure analysis, and any state overlay flags.
- **Attorney role:** a compliance review memo (no lender-signed CD). The example in `assets/examples/cd-review-memo.md` shows the shape.

---

## Checkpoint B: post-draft alignment (mandatory)

Before delivering:

1. Tolerance violations: cured (with `closing-disclosure-tolerance` cure-amount methodology) or explicitly flagged as outstanding for the responsible party?
2. Re-disclosure window: required, and if so, honored? Earliest consummation date stated explicitly?
3. State overlays: applied; any out-of-table state flagged for local-counsel review?
4. Cash-to-close: reconciles against transaction summary, payoffs, and wire instructions?
5. APR/TIP: reconciles against truth-in-lending math?
6. Attorney review: required before signing where role is non-lender?

---

## What this skill does not do

- It does not value the deal or opine on loan terms. Tolerance and timing are mechanical; pricing is between borrower and lender.
- It does not resolve title issues. It identifies them on Page 3 / Page K and routes to `title-commitment`.
- It does not replace attorney review when the role is borrower's or seller's counsel. Always label the deliverable AI-generated and require sign-off.

---

## Quality checklist

- [ ] All five pages of Form H-25 populated; missing fields explicitly marked `MISSING`
- [ ] LE comparison baseline is the most recent **valid** LE
- [ ] Tolerance review run via `closing-disclosure-tolerance` methodology; cure amount stated where applicable
- [ ] Re-disclosure trigger analyzed; if triggered, earliest consummation date stated
- [ ] State overlay items applied (or out-of-table state flagged)
- [ ] Cash-to-close reconciles to transaction summary and payoffs
- [ ] APR / TIP reconcile to truth-in-lending math
- [ ] Memo labels itself AI-generated and requires attorney/closer review

---

## Troubleshooting

- **No prior LE in the file.** Cannot complete the LE-CD comparison. Surface as a Critical flag; do not proceed past Step 2 without the LE or a valid changed-circumstance record establishing why no LE exists.
- **Multiple LEs and the agent is unsure which is the baseline.** The baseline is the most recent LE that was either (a) the original LE for an unchanged product or (b) a revised LE issued under a valid changed-circumstance trigger within the timing window. See `closing-disclosure-tolerance` for the changed-circumstance gate; if unresolvable from the record, treat the earliest LE as baseline and flag the ambiguity.
- **Tolerance violation discovered post-consummation.** Cure deadline is 60 calendar days after consummation per 12 CFR 1026.19(f)(2)(v) `[VERIFY]`. Produce a corrected CD or itemized cure disclosure; document the cure method (refund / escrow application / principal reduction).
- **State overlay item references a fee not in the file.** Two cases: (a) the fee was waived or doesn't apply — note "N/A" with reason; (b) the fee should appear and doesn't — flag as a Critical-tier missing line and route to settlement agent.
- **APR computation in the file does not match recomputation.** Most common cause is missing or extra finance charges. Reconcile finance-charge inclusions against 12 CFR 1026.4 `[VERIFY]`; treat divergence > 0.125% (fixed) or > 0.25% (ARM) as a redisclosure trigger.
- **Form H-25 layout differs from a state addendum.** Use Form H-25 structure as the federal floor; do not rewrite statutory disclosure text. Append the state addendum without altering H-25 layout. See `references/STATE-OVERLAYS.md`.

---

## Citations

- 12 CFR 1026.38 — CD form requirements (Form H-25) `[VERIFY]`
- 12 CFR 1026.19(e)(3) — LE good-faith determination `[VERIFY]`
- 12 CFR 1026.19(f) — CD timing and delivery `[VERIFY]`
- 12 CFR 1026.19(f)(2)(v) — Excess refund / cure deadline `[VERIFY]`
- TILA, RESPA — underlying authority

---

## References

- `references/CD-PAGES.md` — page-by-page intake checklist
- `references/STATE-OVERLAYS.md` — state-specific overlay items

## Assets

- `assets/examples/cd-review-memo.md` — finished compliance review memo for a synthetic purchase-money first-lien deal
