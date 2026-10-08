---
name: prompt-pack-saas-terms-of-service-sboghossian
title: SaaS Terms of Service
description: Use when a SaaS company needs to draft terms of service governing customer access to its platform. Covers account setup, acceptable use, service levels, data ownership, subscription and billing, limitation of liability, dispute resolution, and termination. Especially relevant for MENA-facing SaaS platforms that must navigate UAE e-commerce law, DIFC/ADGM contract law, consumer protection requirements, and data protection obligations, as well as the interplay between clickwrap enforceability across civil-law and common-law jurisdictions.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-saas-terms-of-service
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# SaaS Terms of Service

## When to use this

Use this skill when:
- A SaaS provider needs a clickwrap or browsewrap ToS governing B2B or B2C customer use of its platform.
- A company is launching a new digital product in MENA or internationally and needs a foundational ToS.
- An existing ToS needs to be updated for a new jurisdiction, a new product feature, or regulatory compliance (e.g., UAE e-commerce law, EU DSA/DMA, consumer protection).
- A platform is adding a marketplace or user-generated content function and the existing ToS must be expanded.

**B2B vs. B2C note:** The structure and legal constraints differ significantly. B2C ToS must comply with consumer protection laws that restrict or void certain clauses (unfair terms, exclusions of statutory rights). B2B ToS have more freedom but DIFC and ADGM consumer protection rules extend to small business customers in some contexts.

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| **Description of the SaaS platform and services** | Defines scope; the ToS must describe what is (and is not) provided | Ask |
| **Target customer type** | B2B enterprise / B2B SME / B2C consumer | Ask; consumer-facing ToS need significantly different liability and dispute resolution treatment |
| **Jurisdiction(s) of operation** | Determines mandatory consumer protection rules, choice of law, and e-commerce disclosure requirements | Ask; default: UAE + DIFC |
| **Subscription model** | Monthly/annual; tiered plans; free trial; freemium | Ask |
| **Data handling model** | Does the platform process personal data on behalf of customers (DPA required)? Does it use customer data for its own purposes? | Ask |

## Optional inputs

- **Service Level Agreements (SLAs)** — uptime commitments, response times; if specific SLAs exist, reference them as a separate Schedule or SLA document.
- **Acceptable Use Policy (AUP)** — if detailed AUP is needed (common for platforms that could be misused), draft as a separate linked document.
- **Marketplace / user content rules** — if the platform hosts user-generated content, content moderation and IP licensing rules are essential.
- **API terms** — if developers can access via API, separate API terms or an addendum is recommended.

## Document structure

1. **Acceptance and agreement formation**
   - How the customer accepts: clicking "I Agree," creating an account, using the service.
   - Enforceability of clickwrap: in UAE, DIFC, and most MENA jurisdictions, electronic acceptance is recognized (UAE e-Transactions Law, Federal Decree-Law No. 46 of 2021; DIFC Electronic Transactions Law).
   - Age requirement: minimum age to contract.
   - Entity customers: the person accepting warrants authority to bind the entity.

2. **Account terms**
   - Account creation requirements.
   - Customer's responsibility to keep credentials secure.
   - Responsibility for all activity under the account.
   - Account sharing restrictions (per-seat vs. concurrent user licensing).
   - Suspension for suspected unauthorized access or AUP violation.

3. **License and access rights**
   - Grant: non-exclusive, non-transferable, limited license to access and use the platform during the subscription term.
   - Scope: authorized users, number of seats, permitted features.
   - Restrictions: no reverse engineering, decompiling, sublicensing, or use to build competing products.

4. **Acceptable use policy**
   - Prohibited content and conduct (spam, malware, fraud, IP infringement, illegal activity).
   - Compliance with applicable laws in customer's jurisdiction.
   - Consequences of AUP violation: suspension, termination, withholding of refund.

5. **Service levels and availability**
   - Uptime commitment (e.g., 99.5% monthly); how measured.
   - Scheduled downtime: excluded from uptime calculation.
   - Service credits: sole remedy for SLA breach (not termination right unless breach is persistent).
   - **Avoid guaranteeing specific uptime in the ToS body** — reference an SLA document that can be updated.

6. **Data ownership and processing**
   - **Customer data:** customer retains ownership; provider holds a license to process customer data to deliver the service.
   - **Provider's use of customer data:** limited to service delivery; no selling or advertising use without consent.
   - **Data processing agreement:** for B2B customers in GDPR/DIFC/UAE PDPL scope, a DPA must be included as a schedule or separate document.
   - **Aggregated/anonymized data:** provider may use aggregated, anonymized data derived from service use for product improvement; this is standard but must be genuinely anonymized.
   - **Data return/deletion on termination:** customer has [30/60] days post-termination to export data; after that, provider may delete.

7. **Subscription and billing**
   - Subscription plans, pricing.
   - Billing cycle: monthly/annual; auto-renewal.
   - Payment methods; handling of failed payments (suspension after X days).
   - Price changes: notice period (30/60 days); customer's right to cancel within notice period.
   - Refunds policy: generally no refunds for SaaS (state explicitly); pro-rata refunds for annual plans on cancellation (decide).
   - Taxes: prices exclusive of VAT/GST/tax; customer responsible for applicable taxes.

8. **Intellectual property**
   - Platform IP: all rights in the platform, software, documentation owned by provider.
   - Customer IP: customer retains all rights in its data and any customizations.
   - Feedback: if customer provides feedback, provider may use it without restriction or compensation (standard).

9. **Confidentiality**
   - Mutual confidentiality; what is excluded (public domain, independently developed, required by law).
   - For B2B enterprise ToS, the confidentiality provisions should be robust; for mass-market B2C ToS, can be lighter.

10. **Representations and warranties**
    - Provider warrants: service will perform materially as documented; no known malware or security vulnerabilities at launch.
    - Customer warrants: will use the service lawfully; data submitted does not infringe third-party rights.
    - Disclaimer: service provided "as is" except for express warranties above; no warranty of fitness for a particular purpose.

11. **Limitation of liability**
    - Mutual exclusion of indirect, consequential, special, punitive, and incidental damages.
    - Cap on direct damages: typically 12 months of fees paid in the 12 months before the claim.
    - **Consumer protection trap:** In UAE (Federal Consumer Protection Law), DIFC, and EU, liability exclusion clauses in consumer contracts may be void if they limit liability for death, personal injury, or fraudulent misrepresentation. State the jurisdictions clearly; do not apply a consumer-unfriendly cap to B2C contracts without legal review.

12. **Indemnification**
    - Customer indemnifies provider against third-party claims arising from customer's use of the service, customer data, or AUP violation.
    - Provider indemnifies customer for IP infringement claims alleging that the platform itself infringes a third-party IP right (standard IP indemnity with carve-outs for customer modifications, third-party integrations, and misuse).

13. **Term and termination**
    - Initial term; renewal terms.
    - Termination for cause (breach, insolvency).
    - Termination for convenience: customer may cancel at end of billing cycle.
    - Effect of termination: access ceases; data export window; payment obligations for current period.

14. **Dispute resolution and governing law**
    - **B2B:** Arbitration or DIFC/ADGM courts preferred for MENA-facing platforms.
    - **B2C:** Consumer may have the right to sue in their local courts regardless of choice-of-law clause in many jurisdictions (EU Consumer Rights Directive, UK CRA 2015, UAE Consumer Protection Law).
    - Class action waiver (US practice) — not valid in MENA or EU; do not include for MENA-facing B2C terms.

15. **Changes to terms**
    - Right to update ToS with notice (30 days for material changes).
    - Continued use after notice period = acceptance.
    - Consumer protection note: in some jurisdictions, unilateral changes to consumer contracts are restricted.

16. **General provisions** — severability, entire agreement, no waiver, force majeure, assignment (no assignment by customer without consent).

## Jurisdictional notes

### UAE — E-commerce and Consumer Protection
- Federal Decree-Law No. 46 of 2021 on Electronic Transactions: electronic contracts and clickwrap are recognized; ToS must be made accessible before acceptance.
- Federal Decree-Law No. 5 of 2023 on Consumer Protection: unfair contract terms in B2C contracts may be void; liability exclusions for provider negligence are particularly vulnerable.
- Arabic version: while not mandatory for all platforms, having an Arabic version is advisable for UAE-resident consumers and is required for filings in UAE courts.

### KSA
- E-Commerce Law (Royal Decree M/126 of 2019): disclosure requirements before contract formation; right of return for consumers.
- Consumer Protection Law: void terms include those restricting consumer's legal rights.

### EU
- EU Consumer Rights Directive, Unfair Contract Terms Directive: broad restrictions on unfair terms in B2C ToS.
- Digital Services Act (DSA): new obligations for very large online platforms.
- GDPR: ToS and privacy policy must be complementary; DPA required for B2B data processing.

## Drafting standards

- Keep the ToS readable — long unreadable ToS create enforcement risk because courts may hold that onerous terms were not adequately communicated.
- Use a layered approach for B2C: a summary of key terms at the top ("what you need to know") followed by the full legal text.
- Avoid US-only statutory references (e.g., "DMCA takedown notices," "CAN-SPAM") in MENA-facing ToS; use jurisdiction-appropriate equivalents.
- Make the limitation of liability cap commercially sensible — a cap of "fees paid in the last 12 months" may be near-zero for a new customer; consider a floor (e.g., "not less than USD 1,000").

## Common mistakes

- **No data processing agreement for B2B.** GDPR, DIFC, and UAE PDPL all require a DPA when the provider processes personal data on behalf of the customer; the ToS alone is insufficient.
- **Liability cap lower than the SLA credit.** If service credits under the SLA can exceed the liability cap, there is a conflict.
- **Auto-renewal without adequate consumer notice.** In UAE, EU, and KSA, auto-renewal of consumer subscriptions requires clear disclosure and may require opt-in consent.
- **Overly broad IP assignment of feedback.** "You assign all IP in feedback to us" — an assignment of IP requires specific formalities in civil-law jurisdictions; a license is safer.

## Related skills

- [[prompt-pack-privacy-policy]]
- [[prompt-pack-service-agreement]]
- [[prompt-pack-software-license-agreement]]
- [[heuristic-always-state-jurisdiction-first]]
- [[heuristic-no-us-style-boilerplate-in-civil-law-jx]]
