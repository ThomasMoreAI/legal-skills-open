# Worked Example — Buyer Perspective, Quick Triage Mode

This example shows the skill applied to a supplier-prepared purchase MSA from the buyer's perspective in `quick_triage` mode. The scenario: a manufacturing company is evaluating a new supplier of specialty components and wants a fast bottom-line read on whether the proposed MSA is signable, before committing to deeper review.

## Input

**Perspective:** buyer
**Review depth:** quick_triage
**Jurisdiction:** Delaware (governing law)
**Goods or services:** "Specialty machined components for incorporation into our finished products. Single supplier qualified for these components; multi-year supply contemplated."
**Industry context:** "general commercial — no specific industry overlay" (manufacturing, but not in a regulated industry)
**Deal context:** "First-time supplier qualification; single-source critical supply; multi-year deal contemplated."
**Order Form provided:** no
**Prior agreements:** none

**Document (excerpts — actual document is 18 pages):**

> **§3.1 Pricing.** Prices for the Goods are as set forth in the Price List attached as Exhibit A. Supplier may adjust prices upon ninety (90) days' written notice to Buyer; provided that price adjustments shall not exceed the supplier's reasonable estimate of cost increases as determined by Supplier.
>
> **§4.2 Delivery.** Supplier shall use commercially reasonable efforts to deliver Goods within the lead times set forth in the applicable Purchase Order. Risk of loss and title pass to Buyer upon Supplier's tender of the Goods to the carrier at Supplier's facility (FOB Origin).
>
> **§5.1 Acceptance.** Buyer shall inspect the Goods within fifteen (15) days of receipt and shall be deemed to have accepted the Goods if Buyer does not provide written notice of rejection within such period.
>
> **§6.1 Warranty.** Supplier warrants that the Goods will conform to the specifications set forth in the applicable Purchase Order at the time of shipment. THIS WARRANTY IS IN LIEU OF ALL OTHER WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT. Supplier's sole obligation under this warranty is to repair or replace, at Supplier's option, any non-conforming Goods returned to Supplier within ninety (90) days of receipt by Buyer. This warranty constitutes Buyer's sole and exclusive remedy.
>
> **§7.1 Indemnification.** Buyer shall defend, indemnify, and hold harmless Supplier from and against any claims arising out of or relating to Buyer's use of the Goods. Supplier has no indemnification obligations to Buyer.
>
> **§8.1 Limitation of Liability.** SUPPLIER'S TOTAL LIABILITY UNDER THIS AGREEMENT SHALL NOT EXCEED THE PURCHASE PRICE OF THE SPECIFIC GOODS GIVING RISE TO THE CLAIM. IN NO EVENT SHALL SUPPLIER BE LIABLE FOR INDIRECT, INCIDENTAL, CONSEQUENTIAL, OR PUNITIVE DAMAGES.
>
> **§9.1 Term.** The initial term is one (1) year, with automatic renewals for successive one-year periods unless either party provides notice of non-renewal at least sixty (60) days prior to the end of the then-current term.
>
> **§9.4 Discontinuation.** Supplier may discontinue any Goods upon thirty (30) days' written notice to Buyer.
>
> **§10.1 Force Majeure.** Neither party shall be liable for any delay or failure to perform due to events beyond such party's reasonable control, including without limitation supply chain disruptions, labor disputes, equipment failures, or other operational issues. Force majeure does not excuse Buyer's payment obligations.
>
> *(Other excerpts truncated.)*

## Output

# MSA Review — Commercial Purchase: [Supplier] Master Supply Agreement

**Perspective:** Buyer
**Review depth:** Quick triage (Tier 1 issues only)
**Document type:** Master Supply Agreement
**Goods or services:** Specialty machined components, single-source critical supply
**Industry context:** General commercial
**Governing law:** Delaware
**Term:** 1 year initial, auto-renews 1 year, 60-day non-renewal notice
**Order Form / PO provided:** No
**Prior agreements considered:** None

## Bottom line

**Materially unfavorable to buyer; not signable as drafted.** The MSA contains six critical Tier 1 issues that, individually, each warrant negotiation, and that, collectively, make the document substantially below market for a single-source critical supply relationship. The most consequential issues are: (1) no supplier IP indemnification, with one-sided buyer indemnity (§7.1); (2) "AS IS" warranty effectively eliminated by remedy limitations (§6.1); (3) liability cap at the affected goods value with no IP indemnity carve-out (§8.1); (4) 30-day discontinuation right with no last-time-buy or end-of-life protections (§9.4); (5) open-ended pricing adjustments based on supplier's "reasonable estimate" (§3.1); and (6) force majeure broad enough to swallow supply commitments (§10.1). For a single-source critical supply relationship, this combination is fundamentally inadequate. Recommend either substantial negotiation across these six items or proposing buyer's own template instead. Tier 2 and Tier 3 issues not reviewed in detail per quick_triage scope; see DE-072 for full review recommendation.

## Critical issues

### §7.1 — No supplier IP indemnification; one-sided buyer indemnity

**What the document says:** buyer indemnifies supplier for any claims arising out of or relating to buyer's use of the goods. Supplier has no indemnification obligations to buyer.

**Why it's a problem:** for component-supply where buyer integrates supplier's goods into buyer's finished products, supplier IP indemnity is a baseline expectation. Without it, buyer faces the risk that supplier's goods infringe third-party IP and that buyer is held responsible for the resulting damages and litigation. The one-sided buyer indemnity compounds the problem — buyer indemnifies supplier for claims arising from "buyer's use," which is so broad it could capture claims arising from supplier's own design choices.

**Recommended language for §7.1:**

> "**§7.1 Supplier IP Indemnification.** Supplier shall defend, indemnify, and hold harmless Buyer and its affiliates, officers, directors, employees, and agents from and against any third-party claims, damages, losses, and expenses (including reasonable attorneys' fees) arising out of or relating to any actual or alleged infringement of any third-party intellectual property right by the Goods, except to the extent such claims arise from (a) buyer's modifications to the Goods, (b) combinations of the Goods with products not provided by Supplier, (c) buyer-furnished specifications, or (d) buyer's use of the Goods in violation of this Agreement.
>
> **§7.2 Buyer Indemnification.** Buyer shall defend, indemnify, and hold harmless Supplier from and against any third-party claims, damages, losses, and expenses arising out of (a) buyer-furnished specifications, (b) buyer's modifications to the Goods, (c) combinations of the Goods with products not provided by Supplier, or (d) buyer's violation of applicable laws in connection with buyer's use of the Goods.
>
> **§7.3 Procedural Provisions.** Each party's indemnification obligations are conditioned on (i) prompt written notice of the claim from the indemnified party, (ii) the indemnifying party's right to control the defense and settlement (subject to indemnified party's right to participate at its own expense), and (iii) reasonable cooperation by the indemnified party."

### §6.1 — "AS IS" warranty effectively eliminated by remedy limitations

**What the document says:** supplier warrants conformance to specifications at time of shipment, in lieu of all implied warranties; remedy is repair or replace at supplier's option for goods returned within 90 days of receipt; warranty is sole and exclusive remedy.

**Why it's a problem:** the express warranty — conformance to specifications at time of shipment — is the floor, not the ceiling. The 90-day claim window is short for goods incorporated into buyer's products (defects in components may not appear until buyer's product is in use); it likely won't satisfy UCC §2-725's reasonable-time standard for revoking acceptance under §2-608. Repair-or-replace at supplier's option, with no right to refund or rescission, locks buyer into ineffective remedy cycles for repeated defects. "Sole and exclusive remedy" combined with disclaimer of implied warranties would, if the exclusive remedy fails of essential purpose under UCC §2-719(2), leave buyer with reduced or no remedy. The disclaimer of warranty of non-infringement is consistent with the no-IP-indemnification position in §7 — both must be addressed together.

**Recommended language for §6.1:**

> "**§6.1 Express Warranties.** Supplier warrants that the Goods will: (a) conform to the specifications set forth in the applicable Purchase Order; (b) be free from defects in material and workmanship; (c) be free from any liens or encumbrances; (d) comply with all applicable laws, regulations, and industry standards; and (e) not infringe any third-party intellectual property rights (subject to the exceptions in Section 7.1). The warranty period is twelve (12) months from delivery to Buyer or, for Goods incorporated into Buyer's finished products, twelve (12) months from Buyer's first commercial sale of the finished product, whichever is longer.
>
> **§6.2 Remedies.** If Goods fail to conform to the warranties in Section 6.1, Buyer may, at Buyer's option, (a) require Supplier to repair or replace the non-conforming Goods at Supplier's expense, (b) reject the Goods and receive a refund of the purchase price plus reasonable inspection and handling costs, or (c) accept the non-conforming Goods at a reduced price agreed by the parties. If Supplier fails to repair or replace within thirty (30) days of Buyer's notice, Buyer may source replacement Goods from an alternate supplier and recover the difference in price plus reasonable cover costs from Supplier. Repaired or replaced Goods carry the full warranty period set forth in Section 6.1. The remedies in this Section 6.2 are in addition to any other remedies available at law or in equity, and the limitation in Section 8.1 shall not apply to claims for breach of warranty resulting from Supplier's repeated failure to provide non-defective Goods."

If the supplier resists removing the implied-warranty disclaimer, the fallback position is to retain the disclaimer but ensure express warranties cover everything buyer would otherwise rely on (conformance, defects, title, legal compliance, non-infringement) — in which case the disclaimer becomes less consequential.

### §8.1 — Liability cap at affected goods value with no IP indemnity carve-out

**What the document says:** supplier's total liability capped at the purchase price of the specific goods giving rise to the claim; mutual exclusion of indirect, incidental, consequential, and punitive damages.

**Why it's a problem:** capping supplier's liability at the affected goods value is below market for component-supply MSAs, particularly in a single-source critical-supply context. Standard commercial cap is at least 12 months of purchases or the affected goods value (whichever is greater); enterprise deals run higher. More critically, no carve-out for IP indemnification (which §7.1 redline above introduces), confidentiality, gross negligence, willful misconduct, or bodily injury — all standard carve-outs from cap. The consequential-damages exclusion is mutual but doesn't carve out indemnification obligations, so the carve-outs to the cap don't function effectively.

**Recommended language for §8.1:**

> "**§8.1 Limitation of Liability.** EXCEPT FOR LIABILITY ARISING FROM (A) A PARTY'S BREACH OF CONFIDENTIALITY OBLIGATIONS, (B) A PARTY'S INDEMNIFICATION OBLIGATIONS, (C) BUYER'S PAYMENT OBLIGATIONS, (D) A PARTY'S GROSS NEGLIGENCE, WILLFUL MISCONDUCT, OR FRAUD, (E) BODILY INJURY OR DEATH, OR (F) BUYER'S WARRANTY REMEDIES UNDER SECTION 6.2, EACH PARTY'S TOTAL AGGREGATE LIABILITY ARISING OUT OF OR RELATING TO THIS AGREEMENT SHALL NOT EXCEED THE GREATER OF (X) THE PURCHASE PRICE OF GOODS PURCHASED IN THE TWELVE (12) MONTHS PRECEDING THE EVENT GIVING RISE TO LIABILITY OR (Y) THE PURCHASE PRICE OF THE GOODS DIRECTLY GIVING RISE TO THE CLAIM.
>
> **§8.2 Exclusion of Damages.** Except for liability arising from the matters in Section 8.1(a)-(f), in no event shall either party be liable for any indirect, incidental, consequential, special, or punitive damages, including loss of profits or revenue, whether arising under contract, tort, or any other theory of liability."

### §9.4 — 30-day discontinuation with no last-time-buy or end-of-life protections

**What the document says:** supplier may discontinue any goods upon 30 days' written notice.

**Why it's a problem:** for single-source critical supply, 30 days is grossly inadequate to qualify a replacement supplier, redesign components, or transition production. Combined with no last-time-buy rights and no spare-parts obligation, buyer faces a transition crisis when supplier exits any line.

**Recommended language for §9.4:**

> "**§9.4 Product Discontinuation and End-of-Life.** Supplier shall provide Buyer with at least eighteen (18) months' written notice of any planned discontinuation of any Good or any modification to any Good that would render the Good materially incompatible with Buyer's then-current finished product. Within sixty (60) days of such notice, Buyer may submit a Last-Time-Buy purchase order in a quantity not to exceed three (3) times Buyer's average annual purchases of the affected Good over the preceding three (3) years; Supplier shall fulfill such order in accordance with Supplier's then-current pricing and lead times. For Goods that have been incorporated into Buyer's finished products, Supplier shall continue to provide spare parts at commercially reasonable pricing for at least seven (7) years after the date of discontinuation."

### §3.1 — Open-ended pricing adjustments

**What the document says:** supplier may adjust prices upon 90 days' notice; adjustments not to exceed supplier's reasonable estimate of cost increases as determined by supplier.

**Why it's a problem:** "supplier's reasonable estimate, as determined by supplier" is supplier's unilateral discretion. There is no index reference, no buyer audit right, and no cap on the adjustment magnitude. Over a multi-year supply relationship, prices can drift substantially with no contractual constraint.

**Recommended language for §3.1:**

> "**§3.1 Pricing.** Prices for the Goods are as set forth in the Price List attached as Exhibit A. Prices are firm for the first twelve (12) months of the Term. Thereafter, Supplier may propose price adjustments at the end of each twelve-month period, provided that any such adjustment shall not exceed the percentage increase in the Producer Price Index for the relevant industry sector (as published by the U.S. Bureau of Labor Statistics) over the prior twelve months, capped at five percent (5%) per year. Supplier shall provide at least ninety (90) days' written notice of any proposed adjustment, with documentation supporting the adjustment. If Buyer disputes the adjustment, Buyer may terminate this Agreement upon written notice without penalty before the effective date of the proposed adjustment."

### §10.1 — Force majeure swallowing supply commitments

**What the document says:** force majeure includes "supply chain disruptions, labor disputes, equipment failures, or other operational issues."

**Why it's a problem:** equipment failures and operational issues are within supplier's control or directly attributable to supplier's operational choices. Including them in FM means supplier's commitments are excused whenever supplier's own operations fail — which is precisely when buyer needs the commitment to be enforceable.

**Recommended language for §10.1:**

> "**§10.1 Force Majeure.** Neither party shall be liable for any delay or failure to perform (other than payment obligations) due to events beyond such party's reasonable control, including without limitation acts of God, natural disasters, war, terrorism, government action, and pandemic-related restrictions imposed by governmental authority. For the avoidance of doubt, Force Majeure does not include: (a) supplier's equipment failures or other operational issues within supplier's control; (b) labor disputes affecting only the affected party; (c) supply chain disruptions affecting only the affected party's tier-1 supplier (such disruptions are within the affected party's responsibility for supply chain management); (d) financial difficulties of either party; or (e) any event the affected party could have reasonably foreseen and mitigated.
>
> The party affected by a Force Majeure event shall (i) promptly notify the other party, (ii) use commercially reasonable efforts to mitigate the effects, and (iii) keep the other party informed of progress. Either party may terminate this Agreement upon written notice if a Force Majeure event continues for more than ninety (90) days. During Force Majeure affecting Supplier's ability to deliver, Supplier shall allocate available production capacity pro rata among Supplier's customers."

## Material issues

[Per `quick_triage` mode: not reviewed in detail. Several Tier 2 issues likely warrant attention; recommend `comprehensive` review for full coverage.]

Tier 2 issues that the user should consider in any subsequent review:
- **Confidentiality** (§ not shown): verify present, mutual, and adequate.
- **Audit rights** for supplier's quality system (especially relevant in single-source critical supply).
- **Insurance requirements** (verify supplier carries adequate products-liability and commercial-general-liability coverage).
- **Recall obligations** (consider whether buyer's finished products carry recall risk that should flow back to supplier).
- **Order of precedence** between MSA and POs (verify that conflicts default to MSA controlling).

## Minor issues and observations

[Not reviewed in detail per quick_triage scope.]

## Missing standard protections

Beyond the critical issues addressed above:
- **No supplier obligation to maintain BC/DR or alternate sourcing** for single-source critical supply.
- **No tooling provisions** (if buyer-paid tooling is involved, this is a critical gap).
- **No quality-agreement reference or quality system requirement.**

## Operational red flags

Each of the six critical issues addressed above is an operational red flag in itself. No additional flags identified in the Tier 1 scope reviewed.

## Recommended next steps

1. **Do not sign as-is.** The combination of six critical issues is incompatible with a single-source critical supply relationship.
2. **Decide whether to negotiate or replace.** Six critical issues plus likely Tier 2 gaps suggests this template may not be salvageable through redlining. If buyer has its own purchase MSA template, present that instead.
3. **If negotiating:** the recommended language above for §3.1, §6.1, §7.1, §8.1, §9.4, §10.1 reflects market-standard buyer positions and should be non-negotiable on a critical-supply deal.
4. **Run comprehensive review.** This was a quick_triage covering Tier 1 issues only. Before signing any version of this MSA, run a `comprehensive` review covering Tier 2 issues (confidentiality, audit, insurance, recall, change orders, set-off rights, assignment, dispute resolution) and Tier 3 issues (drafting cleanliness, order of precedence).
5. **Add Quality Agreement.** For single-source critical supply, a separate Quality Agreement defining quality standards, audit rights, non-conformance handling, change control, and supplier qualification requirements is industry standard and should be required.
6. **Consider supplier qualification process.** Beyond the contract, single-source critical supply warrants supplier qualification including financial-stability assessment, BC/DR plan review, and on-site quality audit.

## Items requiring human judgment

- **Whether single-source qualification is the right strategy.** Six critical contract issues plus inherent single-source risk may warrant qualifying a second source in parallel to de-risk supply continuity. This is a strategic / supply-chain call, not a legal one.
- **Tooling ownership.** Not addressed in the excerpts; for specialty components, tooling investment may be substantial. If buyer pays for tooling, ownership and access on supplier failure must be addressed.
- **Liability cap level appropriate to deal value.** 12 months of purchases is the recommended floor; higher caps may be appropriate depending on potential damages (especially if buyer's finished products carry product-liability exposure to end consumers).
- **Whether the supplier is willing to negotiate.** With six critical issues to address, the negotiation cost is significant. Whether this supplier is the right partner depends on factors the skill cannot assess.

---

## What this example demonstrates

- **Quick triage is a real capability, not a watered-down version.** The six critical issues are fully developed; recommended language is concrete and lawyer-grade. Tier 2/3/4 issues are explicitly flagged as not-yet-reviewed with a clear recommendation to upgrade to comprehensive.
- **Severity calibration responds to deal context.** "Single-source critical supply" elevates issues that would be material in a multi-supplier commodity context — the discontinuation provision (§9.4) is critical because of single-source context; in a multi-supplier context it might be material.
- **The skill correctly notes when issues compound.** The "AS IS" warranty (§6.1) and the liability cap (§8.1) and the no-IP-indemnification (§7.1) are individually problematic but collectively eliminate buyer's contractual recourse. The bottom line treats them as a system, not as independent findings.
- **Recommended language is genuinely usable.** Each critical-issue redline can be pasted into a counter-draft. The user is not just told "negotiate this" but given the specific position to propose.
- **The skill recommends process steps, not just contract changes.** Quality Agreement, supplier qualification process, BC/DR review — these are recommendations beyond the document itself, appropriate to the deal context.
- **Items requiring human judgment defers strategic calls.** Whether to single-source vs. multi-source, whether to negotiate vs. walk, what cap level matches buyer's risk tolerance — all routed to the user.
