---
name: msa-review-saas
title: MSA Review — SaaS
description: Use when the user uploads or pastes a Software-as-a-Service Master Services Agreement (MSA), Master Subscription Agreement, SaaS Agreement, or Cloud Services Agreement and asks for review, redline, risk assessment, or recommendation on whether to sign. Conducts a structured review of MSA framework terms (liability, indemnification, IP, data protection, warranties, term and termination, payment, and others), calibrated to the user's perspective (vendor or customer), with severity-rated findings, redline language for material gaps, and clause-level citations. Optionally surfaces conflicts between the MSA and a provided Order Form or SOW.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-ai/tree/main/skills/msa-review-saas
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: commercial
language: en
---

# MSA Review — SaaS

Conduct a structured review of a SaaS Master Services Agreement from the user's stated perspective and produce a report that an in-house lawyer can act on without redoing the analysis. The output is a draft for human review, not a final word; treat it accordingly.

This skill is calibrated to commercial-grade SaaS MSAs. It is not designed for: enterprise software license agreements (perpetual licenses), professional services agreements without a software component, hosted-but-not-SaaS arrangements (managed hosting, IaaS), or government / public-sector SaaS contracts (which have additional FedRAMP, FAR, and procurement-specific overlays).

## When this skill applies

Apply when the user provides a SaaS MSA, Master Subscription Agreement, SaaS Agreement, Cloud Services Agreement, or substantively similar instrument and asks for review or redline guidance. The user's perspective — vendor or customer — fundamentally changes the analysis; require it before proceeding if not supplied.

Do not apply this skill to:

- **Non-SaaS software agreements.** Perpetual license agreements, on-premises software agreements, and managed-hosting agreements have different fundamental structures (license vs. subscription, on-premises vs. cloud, software-only vs. service). Tell the user this is the wrong skill.
- **Order Forms or SOWs alone.** Those documents reference an MSA; review them in conjunction with the MSA (use the optional `order_form` input) or via a dedicated Order Form Review skill (deferred — see DE-070).
- **DPAs / Privacy Addenda.** Use DPA Checklist Review for those.
- **NDAs accompanying the SaaS deal.** Use NDA Review for those.
- **Government / public-sector SaaS.** Federal and state procurement requirements layer additional terms (FedRAMP, FAR clauses, procurement statutes) that this skill does not cover.

## Inputs

The skill requires the document and perspective. If perspective is not provided:

> "Before I review, which side are you on? Vendor (you're providing the SaaS service) or customer (you're subscribing to it)?"

Optional inputs refine the analysis:

- **`review_depth`** controls thoroughness. Default is `comprehensive` (all issues with detailed findings); `quick_triage` covers core issues only.
- **`jurisdiction`** affects findings on enforceability-sensitive provisions (limitation of liability, non-competes if any, choice of forum).
- **`deal_context`** changes severity calibration. A small-dollar SMB deal warrants different scrutiny than a high-value enterprise deal; an existing-relationship renewal warrants different scrutiny than a first-time vendor evaluation.
- **`order_form`** triggers MSA-vs-Order-Form conflict analysis (Pass 6, below).
- **`prior_agreements`** triggers conflict-with-prior-agreement analysis.
- **`standard_positions`** replaces the skill's generic benchmarks with the user's own — when the user's organization has its own fallback positions, those are the operative standard.

When optional inputs are not provided, the skill makes default assumptions and notes them in the report.

## Workflow

Produce the review in six passes. Earlier passes inform later ones; do not collapse them.

### Pass 1: Document orientation

Before substantive review:

- Confirm the document is a SaaS MSA. If it is a different instrument (perpetual license, professional services without SaaS, managed-hosting), stop and tell the user.
- Identify the parties; confirm vendor and customer roles match the user's stated perspective.
- Note the document structure: does it have clean section/article numbering, defined-terms section, integration with referenced documents (Order Form, DPA, AUP)?
- Note governing law, jurisdiction/venue, and any specified dispute-resolution mechanism (court, arbitration, JAMS, AAA).
- Note the contract length and complexity. SaaS MSAs typically run 8–30 pages; over 35 pages typically signals enterprise-grade complexity that warrants extra attention.
- Identify any annexes, schedules, exhibits, or service-specific terms.

### Pass 2: Standard-issue check

Walk through the standard SaaS MSA issue checklist in `reference/issue_checklist.md`. The checklist groups issues into four tiers:

- **Tier 1 — Always reviewed in detail (covered in both `comprehensive` and `quick_triage`):** liability, indemnification, IP and data ownership, data protection (DPA reference), warranties and disclaimers, term and termination, payment, key SLAs.
- **Tier 2 — Reviewed in detail in `comprehensive` only:** confidentiality, assignment, governing law and venue, dispute resolution, force majeure, change-of-terms mechanics, suspension and acceleration rights, professional services scope, third-party components.
- **Tier 3 — Reviewed in detail in `comprehensive` only:** notice mechanics, integration / entire-agreement, amendment requirements, severability, waiver, counterparts, electronic signatures, definitions completeness, headings.
- **Tier 4 — SaaS-specific provisions:** acceptable use policy reference, customer data definition, data residency and localization, sub-processor management (typically by reference to DPA), audit rights, security incident response, business continuity / disaster recovery, support / maintenance windows, third-party authentication and SSO, API rate limits and overage handling.

For each item, classify:

- **Present and standard:** the document addresses this issue and the addressing falls within the normal range for SaaS MSAs.
- **Present but unusual:** the document addresses this issue with non-standard scope, severity, or carve-outs.
- **Missing:** the document does not address this issue.
- **N/A:** this issue does not apply given the document type or specific facts.

### Pass 3: Perspective and asymmetry analysis

Read every Tier 1 finding through the user's perspective lens (`reference/perspective_lens.md`). The same provision reads very differently from each side:

- **Vendor perspective:** wants broad limitations of liability, narrow warranties, broad disclaimers, limited service commitments, customer-friendly payment obligations (auto-renewal, billing in advance, late fees, suspension rights), broad data-use rights for service operation, broad acceptable-use restrictions on customers, narrow customer indemnities, and operational flexibility (right to modify service, sub-processor changes, terms amendments).
- **Customer perspective:** wants strong service commitments backed by SLA credits, narrow disclaimers and reasonable warranties, controllable termination rights (especially for cause), reasonable liability allocation (super-caps for security and IP issues), strong data protection and ownership of customer data, customer-friendly IP indemnities, predictable pricing and renewal terms, and stability (limits on vendor's right to unilaterally change service or terms).

For each Tier 1 finding, identify which side the provision favors and by how much. For "present but unusual" findings, characterize the deviation: favorable / unfavorable / extreme.

### Pass 4: Operational and red-flag check

Beyond standard issues, look for provisions that create operational risk regardless of perspective. The full list is in `reference/red_flags.md`; key categories:

- **Unilateral amendment rights** that allow vendor to change terms without customer consent.
- **Acceleration clauses** that allow vendor to demand all remaining contract value on breach (especially when paired with broad breach definitions).
- **Suspension rights** that allow vendor to suspend service for non-payment without notice or cure.
- **IP assignments hidden in feedback or improvements clauses.**
- **Customer-data uses for vendor's own purposes** (model training, benchmarking, anonymized resale) without explicit customer consent.
- **Auto-renewal with long opt-out windows** (60+ days) and price-increase rights at renewal.
- **One-sided audit rights** (vendor's right to audit customer's usage but not customer's right to audit vendor's compliance).
- **Forum selection that creates significant disadvantage** to one side (especially Delaware Chancery or vendor's home court).
- **Mass arbitration provisions** that prohibit class actions and limit consolidation.
- **Termination for convenience without proportionate refund mechanics.**
- **Most-favored-nation clauses** on pricing or terms (uncommon but flag whenever present).
- **Source code escrow** absent or inadequate for the deal size.
- **Force majeure clauses** that excuse vendor's service failure but not customer's payment obligation.
- **Material conflicts with industry-standard SLAs** (e.g., 95% uptime in an enterprise contract).

### Pass 5: Conflicts with prior agreements

If `prior_agreements` was provided, examine the document for:

- Express references to the named prior agreements; confirm references are accurate.
- Integration / entire-agreement clauses that would extinguish prior agreement protections.
- Provisions that conflict with terms in the prior agreements.
- Term provisions that don't account for existing relationships (e.g., MSA term running concurrently with an existing services engagement).

If `prior_agreements` was not provided, this pass is skipped.

### Pass 6: MSA-vs-Order-Form conflict analysis

If `order_form` was provided, examine the Order Form against the MSA. Common conflicts:

- **Term length conflicts:** Order Form specifies a different subscription term than the MSA framework contemplates.
- **Pricing inconsistencies:** Order Form pricing references rates not in the MSA, or contradicts MSA pricing terms.
- **Service-level conflicts:** Order Form's stated SLA differs from the MSA's referenced SLA.
- **Data-protection conflicts:** Order Form references different data categories or data-residency commitments than the MSA's DPA contemplates.
- **Termination-right conflicts:** Order Form's termination provisions modify or contradict MSA termination provisions.
- **Indemnification or warranty mods:** Order Form modifies MSA indemnification or warranty terms (typically vendor-favorable; sometimes substantial).
- **Governing-law conflicts:** Order Form specifies different governing law or venue (occasionally happens with multi-jurisdictional vendors).

The general interpretive rule (in most SaaS MSAs) is that Order Form-specific terms override MSA framework terms for that order; verify the MSA's "order of precedence" or "conflict" provision and apply it. If no conflict provision exists, flag — that itself is a deficiency.

If `order_form` was not provided, this pass is skipped.

### Pass 7: Compile the report

Compile findings from prior passes into the report structure (see Output section). Calibrate severity using `reference/severity_rubric.md`. Cite specific section/clause numbers for every finding.

## Output

Produce the report in markdown with this structure (long, but proportional to the document — clean MSAs produce shorter reports; problematic MSAs produce longer ones):

```markdown
# MSA Review — SaaS: [Document name or counterparty]

**Perspective:** [vendor | customer]
**Review depth:** [comprehensive | quick_triage]
**Document type:** [SaaS MSA | Master Subscription Agreement | Cloud Services Agreement | etc.]
**Governing law:** [jurisdiction or "not specified"]
**Term:** [duration / renewal mechanism summary]
**Order Form provided:** [yes / no]
**Prior agreements considered:** [list or "none"]

## Bottom line

[Two to four sentences. State the overall posture (favorable / balanced / unfavorable / materially unfavorable to user). State whether it is signable as-is, signable with minor edits, requires negotiation, or should be rejected. Identify the single most important issue.]

## Critical issues

[Issues rated "critical." Each has its own subsection with: clause reference, what the document says (verbatim quote where short enough), why it's a problem from the user's perspective, suggested redline language. Omit this section if there are no critical issues.]

## Material issues

[Issues rated "material." Same subsection structure.]

## Minor issues and observations

[Issues rated "minor" or items that are present-and-standard but worth noting. May be a bulleted list rather than full subsections. In quick_triage mode, this section is brief; in comprehensive mode, it covers Tier 2 and Tier 3 issues that did not warrant detailed treatment.]

## Missing standard protections

[Standard SaaS MSA elements that are absent and should be added. Each with suggested language or a reference.]

## Operational red flags

[Items from Pass 4 — even where they don't rise to critical/material, the user should be aware.]

## Conflicts with Order Form

[If Order Form was provided. Each identified conflict with: what the MSA says, what the Order Form says, which controls per the order-of-precedence provision, and the operative effect. Omit this section entirely if no Order Form was provided.]

## Conflicts with prior agreements

[If prior_agreements was provided. Each identified conflict similar to above. Omit if not applicable.]

## Recommended next steps

[Short bulleted list. Common options: sign as-is, sign with the redlines proposed above, send back with negotiation, escalate specific issues to outside counsel, decline to proceed.]

## Items requiring human judgment

[Items the skill cannot resolve and that need the user's business judgment or jurisdiction-specific expertise.]
```

In `quick_triage` mode, the "Minor issues and observations" and "Missing standard protections" sections are condensed; the focus is Tier 1 issues with full treatment. In `comprehensive` mode, all sections are populated.

If the document is signable as-is or with only minor changes, the report should be short. Do not pad. A two-page report on a clean MSA is correctly two pages; do not stretch it to ten.

## Edge cases and refusals

- **Document is not a SaaS MSA.** Stop and tell the user. Common adjacent documents that get confused for SaaS MSAs: perpetual software licenses, on-premises agreements, professional services agreements, IaaS / managed-hosting agreements, hardware-as-a-service agreements.
- **Document is a SaaS MSA but covers a non-standard service category.** Examples: AI/ML model providers (which often have data-use and output-IP terms unique to ML), payment processors (which have additional regulatory overlay), telehealth platforms (which have HIPAA overlay), educational platforms (which may have FERPA/COPPA overlay). Apply the skill but note in the posture that category-specific terms (e.g., "AI training data carve-outs") may warrant additional review beyond the standard MSA framework.
- **Document is missing pages, sections, or referenced exhibits.** Note explicitly and review what is present; do not speculate about absent content.
- **Document is from an unfamiliar jurisdiction or in a non-English language.** Apply the skill but note the limitation: the skill is calibrated for US commercial SaaS MSAs; jurisdiction-specific issues (especially EU-style consumer protection mandatory rules, civil-law jurisdiction interpretation rules) may not be fully addressed.
- **Document has unusual provisions outside the skill's coverage** (e.g., complex multi-tenant data-segregation requirements, novel AI training and output IP terms, escrow arrangements with detailed release mechanics). Flag in "Items requiring human judgment" rather than producing potentially-wrong analysis.
- **Perspective is "customer" but the document is clearly written by the customer's outside counsel** (i.e., on a customer-friendly template). Note the asymmetry; the customer-perspective review may surface fewer issues because the document already reflects customer positions.

## What this skill does not do

- Give a final legal opinion. The output is a draft for human review.
- Predict enforceability with confidence. Flags issues; the user determines enforceability with their own jurisdiction expertise.
- Negotiate. Suggests redlines but does not draft side letters or counter-proposals.
- Replace counsel for unusual deal structures (M&A involving SaaS targets, multi-party joint-venture SaaS deals, sovereign-immunity issues with public-sector customers). Recommend escalation.
- Review the underlying SaaS service for technical adequacy. The skill reviews the contract, not the product.
- Replace a security review. The MSA may reference the vendor's security program; the skill checks that the references exist but does not assess the security program itself.

## Reference materials

- `reference/issue_checklist.md` — the full SaaS MSA issue checklist organized by tier.
- `reference/perspective_lens.md` — how to read each provision through vendor or customer eyes.
- `reference/red_flags.md` — operational and red-flag list used in Pass 4.
- `reference/severity_rubric.md` — the rubric for rating issues critical, material, minor.
- `examples/example_customer_review.md` — worked example: customer reviewing a vendor-prepared SaaS MSA.
- `examples/example_vendor_review.md` — worked example: vendor reviewing a customer-prepared MSA template.
