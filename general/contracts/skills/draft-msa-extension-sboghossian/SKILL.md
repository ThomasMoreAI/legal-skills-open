---
name: draft-msa-extension-sboghossian
title: MSA Variants by Industry
description: Use when a standard MSA needs to be tailored for a specific industry vertical or delivery model — SaaS, consulting, manufacturing, or marketing services. Provides the delta from the base MSA skill, covering the additional provisions, modified clauses, and industry-specific schedules (DPA, SLA, quality standards, performance metrics) that each variant requires. Triggers after [[draft-msa]] when the user specifies an industry type (SaaS, IT consulting, manufacturing, marketing, professional services).
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-msa-extension
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# MSA Variants by Industry

## When to use this

After producing the base [[draft-msa]], use this skill to apply the industry-specific overlay that the engagement requires. Do not start from scratch — describe the variant to the client, then add the relevant schedule or modify the applicable clauses.

The four core variants are:

---

## Variant 1 — SaaS MSA

### What changes from the base MSA

A SaaS MSA governs a software-as-a-service engagement where the Provider operates the software and the Client accesses it remotely. The key differences from a professional-services MSA:

#### Add: Data Processing Addendum (DPA)
The DPA is mandatory when the Provider processes personal data on the Client's behalf:
- Processor / Controller designation (typically: Client = Controller; Provider = Processor)
- Subject-matter, nature, purpose, and duration of processing
- Categories of personal data and data subjects
- Client's instructions; Provider may only process per instructions
- Provider's obligations: sub-processor approval; security measures; breach notification (72 hours for GDPR); deletion/return on termination
- Transfer mechanisms for cross-border processing (SCCs, adequacy, KSA PDPL equivalent)
- Reference skill: [[draft-dpa-gdpr]] (EU/UK), [[draft-dpa-ksa-pdpl]] (KSA), [[draft-dpa-uae-pdpl]] (UAE)

#### Add: Service Level Agreement (SLA) Schedule
- **Availability commitment**: e.g., 99.5% uptime per month (calculated excluding planned maintenance)
- **Planned maintenance window**: typically nights/weekends; advance notice required (48 hours minimum)
- **Incident severity and response times**:
  - P1 (Critical — service unavailable): response 15 minutes; resolution target 4 hours
  - P2 (Major — significant feature unavailable): response 1 hour; resolution target 24 hours
  - P3 (Minor — degraded performance): response 4 hours; resolution target 72 hours
- **Service credits**: Provider credits Client's account for breach of availability SLA (typically 5-25% of monthly fee per hour/day of downtime, capped at 30% of monthly fee)
- Service credits are the sole and exclusive remedy for availability failures (unless caused by fraud or gross negligence)

#### Add: Security Schedule
- Minimum security standards (ISO 27001, SOC 2 Type II, or equivalent)
- Encryption standards (in transit and at rest)
- Access controls, authentication requirements (MFA for admin access)
- Penetration testing frequency; report sharing
- Vulnerability management and patching timelines
- Incident notification: security breach notification to Client within 24-48 hours of confirmation

#### Modify: Termination
Add data portability obligation: on termination, Provider exports Client's data in a standard format (CSV, JSON, or API) within 30 days at no charge. Provider retains data for 30 days post-termination then deletes; certified deletion notice to Client.

#### Modify: IP
The software itself remains Provider's property; Client receives a subscription license during the term only. On termination, all access rights cease.

---

## Variant 2 — Consulting / Professional Services MSA

### What changes from the base MSA

A consulting MSA governs time-and-materials or fixed-fee engagements where the output is advice, analysis, or embedded expertise rather than software.

#### Add: Rate Card Schedule
- Named rates per consultant category (Partner / Senior Manager / Manager / Analyst / Support Staff)
- Rate basis (per day / per hour)
- Annual escalation (CPI or agreed fixed % per year)
- Travel policy (class of travel, expense reimbursement policy)
- Currency of invoicing

#### Modify: IP — deliverables ownership
Consulting output (reports, analysis, strategy documents) is more commonly client-owned than in software MSAs. Negotiate:
- **Full assignment**: report, analysis, and all deliverables assigned to Client on payment
- **Background IP carve-out**: Provider's methodologies, frameworks, proprietary tools, and pre-existing materials are explicitly carved out as Provider's Background IP; Provider grants Client a license to use them only as incorporated in the Deliverables

#### Add: Staffing provisions
- Key persons schedule: named consultants the Client is counting on
- Substitution notice: Provider gives [10] business days' notice of key-person substitution; Client may object; Provider provides consultant of equivalent or better seniority
- Non-solicitation: Client may not solicit, hire, or engage Provider's personnel for [12] months after their last service date under the MSA

#### Modify: Liability
For consulting engagements involving regulated advice (financial, legal, medical): regulatory or professional-liability provisions may need to be added. Verify whether the Provider is operating as an adviser to the Client or as an independent contractor — this affects implied duties and confidentiality obligations.

---

## Variant 3 — Manufacturing / Supply MSA

### What changes from the base MSA

A manufacturing MSA governs the ongoing supply of goods or manufactured products, often with quality requirements, inspections, and supply-chain provisions.

#### Add: Quality Schedule
- Specifications: reference to product specifications, drawings, standards (ISO, industry standards)
- Testing and inspection: right of Client to inspect at production facility; third-party testing
- Acceptance inspection on delivery; rejection and cure process
- Defect remedies: repair, replacement, or credit; time limits for latent defect claims

#### Add: Force Majeure — Supply Chain Specifics
Standard force majeure expanded to include: supplier insolvency, natural disasters affecting supply chain, port closure, logistics disruption. Mitigation obligation: Provider must maintain buffer stock, identify alternative suppliers.

#### Modify: Covenants
- Minimum order quantities (MOQ): Client commits to minimum purchase volume over the term
- Lead times: Provider commits to lead times per order; penalties for late delivery (liquidated damages per day; cap)
- Forecast obligations: Client provides rolling X-month forecasts; Provider may rely on forecasts for procurement
- Product liability indemnification: Provider indemnifies Client for product liability arising from manufacturing defects

#### Modify: IP
- Client typically owns the product specifications, tooling designs, and Client-provided dies/molds
- Provider may not use Client's IP for any other customer
- Provider's manufacturing process know-how remains Provider's IP

---

## Variant 4 — Marketing Services MSA

### What changes from the base MSA

A marketing services MSA governs ongoing creative, digital marketing, media buying, and campaign management services.

#### Add: IP ownership — Content
- Client owns all campaign deliverables (creative assets, copy, videos, photos, ad materials, social content) immediately upon creation (work-for-hire assignment)
- Provider retains no rights to use Client's brand or campaign materials for portfolio or promotional purposes without Client's written approval
- Third-party content (licensed stock images, music): Provider obtains licenses and passes them to Client; list licensed content in each SOW

#### Add: Performance Metrics
- KPIs per campaign defined in each SOW (impressions, clicks, conversion rate, ROAS — Return on Ad Spend, CPL — Cost Per Lead)
- Reporting frequency (weekly dashboard; monthly review)
- Performance remedy: if defined KPIs are missed for [2 consecutive months], Client may terminate the relevant SOW without penalty
- Measurement tools: agreed analytics platform (Google Analytics, Meta Ads Manager, etc.)

#### Modify: Media Buying provisions
- If Provider buys media on Client's behalf: separate media buying authority
- Client pre-approves media budgets; Provider acts as disclosed agent on Client's behalf
- Rebates and volume discounts: Provider passes through any rebates received from media outlets
- Financial controls: Provider maintains segregated media client account; Client's media budget is not mixed with Provider's own funds

#### Add: Brand Guidelines compliance
- Provider must follow Client's brand guidelines at all times
- Client approves all creative before publication
- Unauthorized publication is a material breach triggering immediate termination rights

---

## How to use these variants

1. Start with [[draft-msa]] for the base document.
2. Identify the variant(s) applicable to the engagement.
3. Add the applicable schedules (DPA, SLA, Rate Card, Quality, etc.) as numbered appendices to the MSA.
4. Identify which base MSA clauses need modification (note the change and why in a cover note to the client).
5. If the engagement spans multiple variants (e.g., a SaaS platform with a consulting implementation component), stack the applicable schedules.

## Related skills

- [[draft-msa]]
- [[draft-licensing-agreement-software]]
- [[draft-dpa-gdpr]]
- [[draft-ip-licensing]]
- [[review-msa-deep-review]]
