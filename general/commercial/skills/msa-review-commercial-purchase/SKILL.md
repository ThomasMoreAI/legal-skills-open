---
name: msa-review-commercial-purchase
title: MSA Review — Commercial Purchase
description: Use when the user uploads or pastes a Master Purchase Agreement, Master Supply Agreement, Master Goods Agreement, or commercial purchase MSA covering the procurement of physical goods, equipment, components, or non-software services and asks for review, redline, risk assessment, or recommendation on whether to sign. Conducts a structured review of MSA framework terms (price and payment, delivery and acceptance, warranties, indemnification, liability, IP, term and termination, force majeure, supply continuity, and others), calibrated to the user's perspective (buyer or supplier), with severity-rated findings, redline language for material gaps, and clause-level citations.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-ai/tree/main/skills/msa-review-commercial-purchase
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: commercial
language: en
---

# MSA Review — Commercial Purchase

Conduct a structured review of a commercial purchase Master Services Agreement from the user's stated perspective and produce a report that an in-house lawyer can act on without redoing the analysis. The output is a draft for human review, not a final word; treat it accordingly.

This skill is calibrated to commercial-grade purchase MSAs — agreements covering the procurement of physical goods, equipment, components, materials, or non-software services. It is not designed for: SaaS subscription agreements (use MSA Review — SaaS), professional-services-only agreements without physical deliverables (treat as a separate skill candidate; see DE-071 in the project PRD), construction agreements (significantly different structure and lien/payment-bond regime), real estate transactions, or government procurement (FAR-driven, distinct overlay).

## When this skill applies

Apply when the user provides a Master Purchase Agreement, Master Supply Agreement, Master Goods Agreement, Master Procurement Agreement, or substantively similar commercial-procurement MSA and asks for review or redline guidance. The user's perspective — buyer or supplier — fundamentally changes the analysis; require it before proceeding if not supplied.

Do not apply this skill to:

- **SaaS or software subscription agreements.** Use MSA Review — SaaS.
- **Construction agreements.** Construction has a distinct regime (mechanic's liens, payment bonds, prevailing wage, retention) that this skill does not cover.
- **Government procurement.** FAR-driven federal procurement and many state procurements have substantial overlays; recommend external counsel familiar with the procurement regime.
- **Real estate purchase or lease.** Different instruments entirely.
- **Pure professional-services agreements without physical deliverables.** The structural shape differs enough from goods-purchase MSAs that a separate skill is appropriate (DE-071 candidate).
- **Purchase Orders or Statements of Work alone.** Those reference an MSA; review them in conjunction with the MSA (use the optional `order_form` input) or via a dedicated PO Review skill (DE-070 candidate).
- **NDAs or Quality Agreements accompanying the supply deal.** Use NDA Review for confidentiality; quality agreements are typically reviewed in tandem with the MSA but are a distinct instrument warranting their own treatment.

## Inputs

The skill requires the document and perspective. If perspective is not provided:

> "Before I review, which side are you on? Buyer (you're purchasing the goods or services) or supplier (you're providing them)?"

Optional inputs refine the analysis:

- **`review_depth`** controls thoroughness. Default `comprehensive` (all issues with detailed findings); `quick_triage` covers Tier 1 issues only.
- **`jurisdiction`** affects findings on UCC-sensitive provisions (warranty disclaimers, acceptance and revocation, perfect-tender, statute of limitations) and common-law force majeure interpretation.
- **`goods_or_services`** changes severity calibration. A capital-equipment purchase warrants different scrutiny than a commodity-component purchase; field-installed equipment warrants installation-services attention; professional-services-only warrants different warranty and delivery treatment.
- **`industry_context`** triggers industry-specific analysis. Automotive (PPAP, traceability), medical device (QSR / ISO 13485), aerospace / defense (ITAR, AS9100), food / pharma (FDA traceability) — each adds substantive considerations beyond the general commercial baseline.
- **`deal_context`** changes severity calibration. Single-source critical supply warrants more attention to supply-continuity and termination than multi-supplier commodity purchases.
- **`order_form`** triggers MSA-vs-PO conflict analysis (Pass 6).
- **`prior_agreements`** triggers conflict-with-prior-agreement analysis.
- **`standard_positions`** replaces the skill's generic benchmarks with the user's own.

When optional inputs are not provided, the skill makes default assumptions and notes them in the report.

## Workflow

Produce the review in six passes. Earlier passes inform later ones.

### Pass 1: Document orientation

Before substantive review:

- Confirm the document is a commercial purchase MSA. If it is a different instrument (SaaS, construction, real estate, government procurement, professional services without deliverables), stop and tell the user.
- Identify the parties; confirm buyer and supplier roles match the user's stated perspective.
- Note governing law and venue. UCC applicability is implicit in US sales of goods (Article 2); note the governing state's UCC variations where they affect findings.
- Identify the underlying transaction structure. Common patterns:
  - **Pure goods sale** — supplier sells finished goods to buyer; UCC Article 2 governs.
  - **Goods + installation** — supplier sells equipment plus installation services; predominant-purpose test determines whether UCC or common-law governs the mixed contract.
  - **Components for incorporation** — supplier sells components that buyer integrates into buyer's own products; warranty pass-through and IP indemnity are particularly important.
  - **Tooling and inventory** — agreement allocates ownership of tooling, masters, and consigned inventory; supply-continuity issues are heightened.
  - **Long-term supply** — multi-year framework with recurring orders; supply-continuity, force majeure, and price-adjustment provisions are central.
- Note the contract length and complexity. Commercial purchase MSAs typically run 10-40 pages; over 50 pages typically signals enterprise-grade complexity or industry-specific overlay (medical device, automotive, aerospace).
- Identify any annexes, schedules, exhibits, quality agreements, or referenced standards.

### Pass 2: Standard-issue check

Walk through the standard commercial purchase MSA issue checklist in `reference/issue_checklist.md`. The checklist groups issues into four tiers, calibrated for purchase-MSA priorities:

- **Tier 1 — Always reviewed in detail (covered in both `comprehensive` and `quick_triage`):** price and payment, delivery and shipping (including risk of loss and title), acceptance and rejection, warranties (express and implied), warranty remedies, IP and infringement indemnification, liability, term and termination, supply continuity and end-of-life.
- **Tier 2 — Reviewed in detail in `comprehensive` only:** confidentiality, change orders and modifications, force majeure, insurance requirements, audit and inspection rights, governing law and venue, dispute resolution, assignment, set-off rights, recall obligations, packaging and labeling.
- **Tier 3 — Reviewed in detail in `comprehensive` only:** notice mechanics, integration / entire-agreement, amendment requirements, severability, waiver, counterparts, electronic signatures, definitions completeness, headings, order of precedence among MSA / PO / Quality Agreement / Specifications.
- **Tier 4 — Industry-specific provisions (when `industry_context` indicates):** sub-tier supplier flow-downs (automotive), traceability (food / pharma / medical), regulatory compliance certifications (FDA, FAA, ITAR), quality system requirements (ISO 9001, ISO 13485, AS9100, IATF 16949), serialization, country-of-origin marking, conflict minerals reporting, REACH / RoHS compliance, Prop 65, FCPA / UK Bribery Act compliance.

For each item, classify: **Present and standard** / **Present but unusual** / **Missing** / **N/A**.

### Pass 3: Perspective and asymmetry analysis

Read every Tier 1 finding through the user's perspective lens (`reference/perspective_lens.md`). Buyer and supplier perspectives differ substantially on most provisions:

- **Buyer perspective:** wants firm supplier commitments on quality and delivery, broad warranty scope with substantive remedies, robust supply-continuity protections (especially for single-source items), reasonable price stability, ownership of buyer's specifications and tooling, broad IP indemnification, controllable termination rights, set-off rights against supplier's invoices.
- **Supplier perspective:** wants firm buyer payment obligations, reasonable warranty scope with capped remedies, controlled change-order processes, predictable production schedules, IP protections for supplier's pre-existing IP, limited liability appropriate to deal margins, and exit rights when buyer's volume falls below committed levels.

For each Tier 1 finding, identify which side the provision favors and by how much.

### Pass 4: Operational and red-flag check

Beyond standard issues, look for provisions that create operational risk regardless of perspective. The full list is in `reference/red_flags.md`; key categories specific to purchase agreements:

- **Open-ended price-adjustment rights** (raw-material indexed pricing without caps; cost-plus structures without audit rights).
- **Forecast-based commitments without firm-PO conversion mechanics.**
- **Single-source dependencies with no supply-continuity protections** (no escrow of tooling; no second-source qualification rights; no end-of-life notice).
- **Asymmetric force majeure** (excuses supplier's delivery but not buyer's payment; or vice versa).
- **Implied warranty disclaimers that exceed UCC §2-316 safe-harbor language.**
- **Acceptance windows that effectively force buyer to accept defective goods** (very short inspection periods; "deemed acceptance" on receipt).
- **Liquidated damages provisions** (penalty vs. genuine pre-estimate).
- **Tooling ownership conflicts** (buyer-paid tooling vested in supplier; tooling residing with supplier without escrow or return rights).
- **Spare parts and service obligations after end-of-production** (often needed by buyer, often missing from supplier templates).
- **Recall obligations and cost allocation** (especially in regulated industries).
- **Sub-tier supplier flow-downs** (whether supplier must impose buyer's terms on its own suppliers).
- **Most-favored-customer pricing** (uncommon but flag whenever present).
- **Exclusivity provisions** (buyer's commitment to source exclusively; supplier's commitment to sell exclusively in defined territories or applications).
- **Non-compete provisions limiting supplier's ability to sell similar products** (sometimes appropriate in design-and-build engagements; often overreach).
- **IP assignments hidden in tooling-design or improvements clauses.**
- **Buyer-furnished material accounting and accountability.**

### Pass 5: Conflicts with prior agreements

If `prior_agreements` was provided, examine the document for conflicts with named prior agreements. If `prior_agreements` was not provided, this pass is skipped.

### Pass 6: MSA-vs-PO conflict analysis

If `order_form` was provided, examine the Purchase Order against the MSA. Common conflicts in purchase agreements:

- **Buyer's standard PO terms vs. supplier's MSA.** Many buyers' POs incorporate "buyer's standard terms and conditions" that may contradict the negotiated MSA. The MSA should specify the order of precedence; if it doesn't, this is itself a finding.
- **Quantity, delivery date, and price specified in PO** that conflict with MSA frameworks (volume commitments, blanket order minimums, price grids).
- **PO-specific quality, packaging, or shipping terms** that vary from the MSA's defaults.
- **Buyer's PO acceptance terms** that purport to override MSA terms ("any conflicting terms in supplier's acknowledgment are rejected; this PO governs").
- **Battle of the forms scenarios.** Where the parties exchange a buyer's PO and supplier's order acknowledgment with conflicting terms, the resolution depends on UCC §2-207 unless the MSA explicitly governs. The MSA should foreclose battle-of-the-forms outcomes by stating that the MSA controls.

The general interpretive rule (in most purchase MSAs) is that the MSA frames the relationship and POs supply order-specific terms (quantity, price, delivery date) without modifying MSA terms; verify the MSA's order-of-precedence provision and apply it. If no order-of-precedence provision exists, flag as material — this is a critical structural protection.

### Pass 7: Compile the report

Compile findings from prior passes into the report structure. **Use the report structure inherited from MSA Review — SaaS** (see Output section below) for consistency across the contract-review skill family. The severity rubric is also inherited; see Severity calibration in `reference/severity_rubric.md`.

## Output

This skill uses the report structure shared with MSA Review — SaaS. The structure is reproduced here for completeness; future versions of the project may hoist this to shared infrastructure (see DE-080 in the project PRD).

```markdown
# MSA Review — Commercial Purchase: [Document name or counterparty]

**Perspective:** [buyer | supplier]
**Review depth:** [comprehensive | quick_triage]
**Document type:** [Master Purchase Agreement | Master Supply Agreement | etc.]
**Goods or services:** [user-provided context, or inferred from document]
**Industry context:** [user-provided context, or "general commercial"]
**Governing law:** [jurisdiction or "not specified"]
**Term:** [duration / renewal mechanism summary]
**Order Form / PO provided:** [yes / no]
**Prior agreements considered:** [list or "none"]

## Bottom line

[Two to four sentences. State the overall posture (favorable / balanced / unfavorable / materially unfavorable). State whether signable as-is, signable with minor edits, requires negotiation, or should be rejected. Identify the single most important issue.]

## Critical issues

[Issues rated "critical." Each has its own subsection with: clause reference, what the document says, why it's a problem, suggested redline. Omit if none.]

## Material issues

[Issues rated "material." Same subsection structure.]

## Minor issues and observations

[Issues rated "minor" or items that are present-and-standard but worth noting. In quick_triage mode, condensed; in comprehensive mode, covers Tier 2 and Tier 3 issues.]

## Missing standard protections

[Standard purchase MSA elements that are absent and should be added.]

## Operational red flags

[Items from Pass 4 that didn't rise to critical/material but warrant awareness.]

## Conflicts with PO / Order Form

[If Order Form was provided. Each conflict with: MSA's position, PO's position, which controls per order-of-precedence, operative effect. Omit if none.]

## Conflicts with prior agreements

[If prior_agreements was provided. Each conflict similar to above. Omit if not applicable.]

## Recommended next steps

[Short bulleted list.]

## Items requiring human judgment

[Items the skill cannot resolve.]
```

In `quick_triage` mode, "Minor issues and observations" and "Missing standard protections" are condensed; the focus is Tier 1 issues with full treatment.

## Edge cases and refusals

- **Document is not a commercial purchase MSA.** Stop and tell the user. Common confusion: SaaS contracts (different skill); professional services with no physical deliverables (different skill candidate); equipment leases (related but distinct — different transfer-of-title and tax treatment).
- **Document is a goods-and-services hybrid where the predominant purpose is unclear.** Apply the skill but note that some findings depend on whether UCC Article 2 or common-law contract principles govern; recommend confirmation by counsel for the user's jurisdiction.
- **Document is from a non-US jurisdiction or in a non-English language.** Apply the skill but note the limitation: the skill is calibrated for US commercial purchase MSAs governed by UCC Article 2; civil-law jurisdictions and CISG (UN Convention on Contracts for the International Sale of Goods) introduce different rules on warranty, risk of loss, and remedies.
- **Document references industry-specific terms the skill does not cover** (e.g., specific automotive PPAP requirements; medical device design history files; aerospace AS9102 first article inspection). Flag in "Items requiring human judgment" and recommend industry-specialist counsel review.
- **Document includes professional-services components that materially change the contract's character** (e.g., a design-build agreement where supplier designs and manufactures a custom solution). Flag mixed-contract considerations; predominant-purpose test may apply.

## What this skill does not do

- Give a final legal opinion. The output is a draft for human review.
- Apply CISG, civil-law, or non-US warranty regimes with confidence. Flags issues; the user determines applicability with their jurisdiction expertise.
- Conduct quality, regulatory, or technical assessments of the supplier or the goods. The skill reviews the contract, not the supplier.
- Replace specialty counsel for unusual deal structures (M&A involving supplier acquisition; sole-source critical supply with national security implications; pharmaceutical supply with chain-of-custody requirements).
- Assess specific industry compliance (FDA, FAA, FAR, ITAR, REACH) beyond flagging the regulatory overlay; these warrant specialist review.

## Reference materials

- `reference/issue_checklist.md` — the full commercial purchase MSA issue checklist organized by tier.
- `reference/perspective_lens.md` — how to read each provision through buyer or supplier eyes.
- `reference/red_flags.md` — operational and red-flag list used in Pass 4.
- `reference/severity_rubric.md` — the rubric for rating issues critical, material, minor. Inherited from MSA Review — SaaS for consistency across the contract-review skill family.
- `examples/example_buyer_review.md` — worked example: buyer reviewing a supplier-prepared purchase MSA.
- `examples/example_supplier_review.md` — worked example: supplier reviewing a buyer-prepared purchase MSA template.
