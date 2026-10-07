# Worked Example — Multi-Jurisdiction Alert with Filtering

This example demonstrates Action Items from Client Alert handling an alert covering multiple jurisdictions, with filtering applied based on the user's `applicable_jurisdictions` input. The skill extracts items from all jurisdictions but flags applicability based on the user's actual operational footprint.

## Input

**Alert date:** 2026-03-22
**Review date:** 2026-05-07
**Document:** Law firm client alert titled "AI Governance Update Q1 2026: New Requirements in EU, US, UK, and California"

**Optional inputs:**
- organization_context: "B2B SaaS company headquartered in Delaware. Customers primarily in US (40 states); some EU customers; no UK customers. We use AI/ML in our products. Approximately 200 employees, ~$50M ARR."
- relevant_business_areas: "AI/ML product use, customer-facing"
- applicable_jurisdictions: "US (federal and California; NOT other state-specific overlays); EU"

**Document (excerpts — actual alert is 8 pages):**

> **CLIENT ALERT — AI Governance Update Q1 2026**
>
> **March 22, 2026**
>
> The first quarter of 2026 has seen significant AI-governance developments across multiple jurisdictions. This alert summarizes the key changes and identifies key compliance dates for affected companies.
>
> **EU AI Act — Phased Compliance Continuing**
>
> The EU AI Act, in force since August 2024, continues its phased compliance roadmap:
>
> - **General-purpose AI model obligations (Article 52, applicable since August 2025):** providers of general-purpose AI models must comply with transparency, technical documentation, and copyright obligations. *Effective since August 2, 2025; ongoing.*
>
> - **High-risk AI system obligations (Article 6, fully applicable from August 2, 2026):** high-risk AI systems (defined in Annex III) must meet conformity assessment, risk management, data governance, technical documentation, and human oversight requirements. *Effective: August 2, 2026.*
>
> - **General product compliance for AI systems (Article 6(2), fully applicable from August 2, 2027):** AI systems integrated into products subject to other EU product safety legislation. *Effective: August 2, 2027.*
>
> Companies should also note the European Commission's Q1 2026 publication of detailed guidance on Article 52 transparency obligations.
>
> **US Federal — Continued Patchwork**
>
> At the federal level, no comprehensive AI legislation has been enacted, but the following developments warrant attention:
>
> - **Executive Order 14XXX (issued February 2026)** directs federal agencies to develop AI risk management practices. While the EO itself does not impose direct private-sector obligations, federal contractors may face flow-down requirements. *No specific deadline; monitor for agency guidance.*
>
> - **NIST AI Risk Management Framework v1.5 (released January 2026)** updates the original framework with additional guidance on generative AI and AI red-teaming. While voluntary, NIST AI RMF is increasingly cited as a benchmark in regulatory and litigation contexts. *Recommended for adoption by AI-using companies.*
>
> **California — New State Law**
>
> California has enacted three AI-related laws effective in 2026:
>
> - **Cal. Civ. Code § XXXX (AI Disclosure Law, effective March 1, 2026):** requires businesses providing AI-based services to consumers in California to provide specific disclosures about AI use, the data used to train the AI, and the process for human review. *Effective: March 1, 2026.*
>
> - **Cal. Health & Safety Code § XXXX (AI Healthcare Law, effective July 1, 2026):** specific to healthcare AI; not applicable to general SaaS providers. *Effective: July 1, 2026.*
>
> - **Cal. Civ. Code § XXXX (Bot Disclosure Update, effective January 1, 2027):** updates existing bot disclosure law to clarify applicability to large language models and conversational AI. *Effective: January 1, 2027.*
>
> **United Kingdom — Regulatory Roadmap**
>
> The UK has continued its sector-led regulatory approach. The ICO has issued updated guidance on AI accountability for data controllers (March 2026), focusing on existing UK GDPR obligations. *Ongoing; no specific deadline.*
>
> The CMA has flagged AI in competition contexts; expect further enforcement focus in 2026. *No specific compliance deadlines from the CMA at this time.*
>
> **New York — Pending Legislation**
>
> New York's AI Act is pending in the legislature; if enacted in current form, would impose obligations similar to the EU AI Act for AI systems used in employment and consumer contexts. Watch for legislative developments in late Q2 2026. *No effective date until enacted.*
>
> **Texas — Sector-Specific**
>
> Texas has enacted sector-specific AI regulations applicable to healthcare and financial services. Not applicable to general SaaS providers. *Sector-specific; effective March 1, 2026 for healthcare, July 1, 2026 for financial services.*
>
> *This alert is for general informational purposes only and is not legal advice.*

## Output

# Action Items from Client Alert: AI Governance Update Q1 2026

**Source document:** Client Alert dated March 22, 2026 — "AI Governance Update Q1 2026: New Requirements in EU, US, UK, and California"
**Alert date:** March 22, 2026
**Organization context:** B2B SaaS, Delaware-based, primarily US (40 states) and some EU customers, no UK customers, AI/ML in products, ~200 employees, ~$50M ARR
**Relevant business areas:** AI/ML product use, customer-facing
**Applicable jurisdictions:** US federal, California, EU

## Context summary

The alert covers AI governance developments across multiple jurisdictions in Q1 2026. For the user (B2B SaaS with EU and US customers, AI/ML in products, no UK customers), the most consequential items are EU AI Act high-risk AI obligations (effective August 2, 2026) and California's new AI Disclosure Law (effective March 1, 2026 — potentially already missed). Items relating to UK, Texas, New York, and healthcare-specific regulations are noted but not applicable to the user.

## Mandatory action items

### Past-deadline items

#### 1. California AI Disclosure Law compliance (effective March 1, 2026)

**What:** if the user provides AI-based services to California consumers, comply with disclosure requirements about AI use, training data, and human review process.

**Deadline:** March 1, 2026 (passed approximately 2 months ago at review date).

**Owner:** Legal (regulatory, privacy) coordinated with Product, Marketing.

**Source citation:** alert's California section, citing Cal. Civ. Code § XXXX (AI Disclosure Law).

**Applicability:** Conditionally applicable. The user is a B2B SaaS provider with US customers across 40 states; California consumer applicability depends on whether the user's services are "provided to consumers" (B2C) versus B2B-only. If B2B-only, the law may not apply directly; flow-through obligations to the user's customers (who in turn provide services to California consumers) are a separate question.

**Recommended remediation:**
- Confirm whether the user's services are B2B-only or include B2C / consumer-facing components.
- If consumer-facing: assess current AI disclosures; remediate gaps; document the assessment given the missed deadline.
- If B2B: confirm with customers whether they require flow-through compliance documentation from the user.
- Document compliance posture given the missed deadline; if non-compliance is identified, consider whether voluntary disclosure to the California AG is appropriate (consult outside counsel).

### Imminent (within 30 days)

None. Nearest applicable mandatory deadlines are several months out.

### Near-term (30 days to 6 months)

#### 2. EU AI Act high-risk AI obligations (effective August 2, 2026)

**What:** if the user's AI systems are classified as "high-risk" under EU AI Act Annex III (used in employment decisions, education, essential services, law enforcement, etc.), comply with conformity assessment, risk management, data governance, technical documentation, and human oversight requirements.

**Deadline:** August 2, 2026 (approximately 3 months from review date).

**Owner:** Legal (regulatory) coordinated with Product, Engineering, Data Science / ML, Compliance.

**Source citation:** alert's EU AI Act section, citing Article 6 of the EU AI Act.

**Applicability:** Conditionally applicable. Depends on whether the user's AI systems fall within Annex III high-risk categories. For typical B2B SaaS, this is often "no" — but it depends on what the user's customers use the AI for. If the user's AI is used by customers in employment decisions or other Annex III contexts, the user may have obligations as a "provider" of the high-risk AI system. Assessment required.

### Future (beyond 6 months)

#### 3. EU AI Act general product compliance (effective August 2, 2027)

**What:** for AI systems integrated into products subject to other EU product safety legislation, additional conformity requirements apply.

**Deadline:** August 2, 2027.

**Owner:** Legal (regulatory) coordinated with Product, Engineering.

**Source citation:** alert's EU AI Act section, citing Article 6(2).

**Applicability:** Conditionally applicable. Depends on whether the user's AI is integrated into products subject to EU product safety legislation. For typical B2B SaaS, likely "no" — but verify based on user's actual deployments.

#### 4. California Bot Disclosure Update (effective January 1, 2027)

**What:** comply with updated California bot disclosure requirements as they apply to LLMs and conversational AI.

**Deadline:** January 1, 2027.

**Owner:** Legal (regulatory) coordinated with Product.

**Source citation:** alert's California section, citing Cal. Civ. Code § XXXX (Bot Disclosure Update).

**Applicability:** Conditionally applicable. Depends on whether the user's AI includes LLM-based or conversational AI features available to California consumers. If yes, applicable; if not (e.g., AI features are not consumer-facing), not applicable.

### Ongoing obligations

#### 5. EU AI Act general-purpose AI model obligations

**What:** if the user provides a "general-purpose AI model" within the meaning of EU AI Act Article 52, comply with transparency, technical documentation, and copyright obligations.

**Periodicity:** Ongoing since August 2, 2025.

**Owner:** Legal (regulatory), Product, Engineering, Compliance.

**Source citation:** alert's EU AI Act section, citing Article 52.

**Applicability:** Conditionally applicable. "General-purpose AI model" has a specific definition under the AI Act (a model trained on broad data using self-supervision at scale, displaying generality). Most B2B SaaS providers using foundation models are not themselves "providers of general-purpose AI models" but may be "deployers" of such models — different obligations. Verify role.

## Recommended action items (no specific deadline)

#### 6. Adopt NIST AI Risk Management Framework v1.5 (recommended)

**What:** evaluate and adopt NIST AI RMF v1.5 (January 2026) as a benchmark for the user's AI risk management practices.

**Why recommended:** while voluntary, NIST AI RMF is increasingly cited as a benchmark in regulatory and litigation contexts. Adoption supports defensibility of AI governance posture.

**Owner:** Compliance / Legal (regulatory) coordinated with Engineering, Data Science / ML.

**Source citation:** alert's US Federal section.

**Applicability:** Applicable to user given AI/ML use.

## Informational items

- **EU Commission Q1 2026 guidance on Article 52 transparency obligations:** monitor for the published guidance; relevant if Item 5 above is applicable.
- **Executive Order 14XXX (February 2026) on federal AI:** does not impose private-sector obligations; relevant only if user is or becomes a federal contractor.
- **New York pending AI Act legislation:** monitor for enactment; New York is one of the user's 40 states. If enacted, would warrant supplementary review.

## Items where applicability is unclear

The conditionally-applicable items above (#1, #2, #3, #4, #5) require fact-finding to confirm applicability:

- Item 1 (California AI Disclosure Law): is the user providing AI-based services to California consumers (B2C), or B2B-only?
- Item 2 (EU AI Act high-risk AI): are the user's AI systems used by customers in Annex III contexts?
- Item 3 (EU AI Act product safety integration): are the user's AI systems integrated into EU product-safety-regulated products?
- Item 4 (California Bot Disclosure Update): does the user offer LLM or conversational AI features to California consumers?
- Item 5 (EU AI Act Article 52): is the user a "provider" of a general-purpose AI model, or a "deployer" of one provided by another?

These are fact questions the user can answer; the skill cannot.

## Items not applicable to user's organization

The user has indicated `applicable_jurisdictions` does not include UK; the alert's UK section (ICO guidance, CMA enforcement) is not applicable. The skill notes this for completeness.

The alert's Texas section (sector-specific AI regulation in healthcare and financial services) is not applicable — the user is B2B SaaS, not healthcare or financial services per `organization_context`.

The alert's California Healthcare AI Law (Cal. Health & Safety Code § XXXX, effective July 1, 2026) is not applicable for the same reason.

## Source references and follow-ups

- **EU AI Act:** Regulation (EU) 2024/1689. Obtain for compliance file.
- **California AI Disclosure Law:** Cal. Civ. Code § XXXX. Obtain for compliance file.
- **NIST AI RMF v1.5:** publicly available; obtain for the legal team.
- **Suggested follow-ups:**
  - Conduct fact-finding on the conditionally-applicable items (above) to confirm applicability.
  - For California AI Disclosure Law (Item 1), consider whether the missed deadline warrants outside counsel consultation.
  - For EU AI Act high-risk AI assessment, this is typically a multi-functional exercise (Legal, Product, Engineering, Compliance); plan accordingly given the August 2026 deadline.
  - Consider a centralized AI governance program if not already in place; the regulatory landscape is enough fragmented that ad-hoc compliance is operationally inefficient.

## Notes on this extraction

The alert covers multiple jurisdictions; applicability filtering against the user's `applicable_jurisdictions` (US federal, California, EU; not UK or other state-specific) and `organization_context` (B2B SaaS, no healthcare or financial services) eliminated several items as not applicable. Most extracted items are conditionally applicable — the user's specific facts (B2B vs. B2C; AI use cases; customer industry mix) determine final applicability. The skill flags the conditions; the user resolves them.

The California AI Disclosure Law deadline (March 1, 2026) has passed at review time. This is a meaningful finding even though applicability is conditional — if the user is providing consumer-facing AI services in California, the missed deadline warrants prompt attention.

---

## What this example demonstrates

- **Jurisdiction filtering does meaningful work.** The alert covered EU, US federal, California, UK, New York, Texas; applying the user's `applicable_jurisdictions` filter eliminated UK, NY-pending, Texas-sector-specific items. The "Items not applicable" section explicitly notes what was filtered out so the user knows nothing was silently dropped.
- **Conditional applicability is preserved.** Most extracted items are flagged as conditionally applicable because the alert's applicability conditions (B2B vs. B2C; AI use cases; high-risk classification) require fact-finding the skill cannot do. The "Items where applicability is unclear" section captures these for user resolution.
- **Past-deadline finding is prominent.** The California AI Disclosure Law deadline has passed; the report calls this out at the top of mandatory items, with recommended remediation. Even when applicability is conditional, a missed deadline warrants prominent treatment.
- **Multi-jurisdiction structure is visible in extraction.** The user can see how items map to different jurisdictions (EU AI Act items vs. California items vs. NIST recommendation), supporting jurisdiction-by-jurisdiction prioritization.
- **Source references include both jurisdiction-specific and cross-cutting materials.** EU AI Act, California laws, NIST framework — all flagged for compliance file building.
- **Follow-up suggestions are specific.** "Centralized AI governance program" recommendation reflects the operational reality that fragmented multi-jurisdiction compliance benefits from coordination.
- **Notes on extraction makes the filtering transparent.** The user knows the filtering was applied and on what basis, and can override if the assumptions don't match.
