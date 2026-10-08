---
name: public-tool-terms-generator-public-sboghossian
title: Terms of Service Generator (Public Tool)
description: Use when a business needs to generate Terms of Service, an Acceptable Use Policy, and (for e-commerce) a Refund Policy and DMCA notice procedure through a guided form — specifying business type, account model, payment model, user-generated content presence, jurisdiction, and disclaimer requirements. Free lead-generation tool outputting DOCX and PDF; nudges users to upgrade for negotiated terms with enterprise customers or additional customization.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/public-tool/public-tool-terms-generator-public
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Terms of Service Generator (Public Tool)

## What it does

The Terms of Service Generator produces a set of foundational legal documents that any business operating a website, app, or online service needs before launching. The documents are generated through a short guided form and calibrated to the business type, jurisdiction, and specific features of the service.

Terms of Service are not optional — they define the contractual relationship between the business and its users, limit liability, govern user-generated content, and set out dispute resolution. Operating without them exposes the business to uncapped liability and removes the contractual framework for user management.

---

## Inputs (guided form)

### Business information

| Field | Options / description |
|---|---|
| Business name | Free text |
| Business URL / app name | Free text |
| Business type | SaaS / marketplace / content platform / e-commerce / professional services / mobile app / other |
| Account model | Registration required / guest checkout / both |
| Payment model | Subscription (monthly/annual) / one-off purchase / freemium / no payment / marketplace commission |
| User-generated content | Yes (users can post, upload, or share content) / No |
| Jurisdiction | Select from list (see below) |
| Disclaimers needed | Medical ("not a substitute for professional medical advice") / Legal ("not a substitute for legal advice") / Financial ("not investment advice") / General ("for informational purposes only") |

---

## Output documents

| Document | Triggered by |
|---|---|
| Terms of Service | Always generated |
| Acceptable Use Policy (AUP) | Always generated as a companion; incorporated by reference in the ToS |
| Refund Policy | Generated if payment model = subscription or one-off purchase |
| DMCA Notice and Counter-Notice Procedure | Generated if jurisdiction includes US AND user-generated content = Yes |
| Arabic ToS (bilingual) | Generated if jurisdiction = UAE or KSA; Arabic version governs for consumer-facing services |

All documents: DOCX + PDF; free tier is watermarked.

---

## Terms of Service structure (generated document)

### 1. Acceptance of terms
How the user accepts the terms (clicking "I agree," creating an account, using the service); state clearly that continued use constitutes acceptance of any future amendments (with notice period).

### 2. Description of service
What the service does; what it does not do; any service availability / uptime commitments (or disclaimer of any guaranteed uptime in the free tier).

### 3. Account registration and security
Registration requirements; user's obligation to maintain accurate account information; password security; prohibited account sharing; business's right to suspend or terminate accounts for violation.

### 4. Acceptable use (incorporates AUP)
Prohibited conduct: illegal activity, harassment, spam, scraping, circumventing security, infringing third-party IP, impersonation, spreading malware; reference to the full AUP.

### 5. User-generated content (if applicable)
- License grant: user grants the business a non-exclusive, worldwide, royalty-free license to display, store, and distribute the content in connection with the service
- Responsibility: user is responsible for their content; business does not pre-screen content but has the right to remove content that violates the AUP
- DMCA / copyright: reference to the DMCA Notice procedure (US); for MENA, reference to applicable IP laws
- Content that includes personal data of others: user responsibility and consent obligations

### 6. Intellectual property
Business retains all IP in the service, interface, and underlying technology; user receives only a limited license to use the service; no scraping, reverse engineering, or unauthorized API access.

### 7. Payment and subscription terms (if applicable)
- Subscription fees, payment cycles, and payment methods
- Auto-renewal: clear disclosure of auto-renewal with notice-to-cancel period
- Refund policy: incorporated by reference; summary of key terms (e.g., 14-day cooling off right under EU Consumer Rights Directive if applicable)
- Fee changes: how and when fees can be changed; notice period
- Taxes: fees exclusive or inclusive of VAT/GST; where applicable, VAT registration number and consumer's obligation

### 8. Disclaimers and limitation of liability
- Service provided "as is" and "as available" without warranty of fitness for a particular purpose
- Limitation of liability: business's aggregate liability capped at [fees paid in the preceding 12 months / USD 100 for free services]
- Consequential damages exclusion (mutual)
- Professional disclaimer (if selected): not a substitute for professional medical / legal / financial / other advice; always consult a qualified professional

### 9. Privacy
Short statement incorporating the Privacy Policy by reference; confirmation that data processing is governed by the Privacy Policy.

### 10. Term and termination
Term (service continues until terminated by either party); user's right to terminate by deleting account; business's right to terminate for violation of ToS; effect of termination (data deletion; outstanding payment obligations); survival of provisions after termination (IP, liability, dispute resolution).

### 11. Governing law and dispute resolution
Calibrated to the selected jurisdiction (see table below); consumer law mandatory provisions cannot be overridden.

### 12. Changes to the terms
Right to modify; notification method (email, in-app notice, website posting); deemed acceptance if user continues to use the service after the notice period.

### 13. Contact information
Business contact details for legal notices; DPO contact (if applicable per privacy policy); copyright / DMCA contact (if applicable).

---

## Acceptable Use Policy (AUP) structure

The AUP enumerates prohibited uses in plain language:

1. No illegal activity
2. No harassment, threats, or abuse of other users or business staff
3. No spam (unsolicited commercial messages)
4. No automated scraping, crawling, or bulk data extraction without authorization
5. No circumventing authentication or security features
6. No uploading malware, viruses, or harmful code
7. No infringing third-party copyright, trademark, or other IP
8. No impersonating another person or organization
9. No sharing login credentials
10. No using the service to harm minors (mandatory child protection provisions)
11. Sector-specific prohibitions (e.g., no financial advice for a non-licensed platform; no medical diagnosis for a health content platform)

---

## Jurisdictional calibration

| Jurisdiction | Key adjustment |
|---|---|
| UAE (onshore) | Arabic bilingual; references UAE Federal Law on Consumer Protection (Law No. 15/2020); mandatory complaint channel |
| KSA | Arabic bilingual; references Saudi Consumer Protection Law; CITC (e-commerce) regulations; non-compete on user content restrictions |
| DIFC | Common-law; DIFC Contract Law; DIFC data protection compliance cross-reference |
| EU (GDPR + Consumer Rights Directive + DSA) | Mandatory 14-day cooling off right for consumers; EU consumer forum (EU ODR platform) link; DSA content moderation obligations for platforms with 10M+ users |
| UK | UK consumer rights; ICO-compliant privacy cross-reference; DMCA equivalent: Copyright, Designs and Patents Act 1988 takedown procedure |
| US | DMCA safe harbor (17 U.S.C. § 512) for platforms with user-generated content; COPPA compliance if children's data may be involved; CAN-SPAM for email; Section 230 limitation of liability for platforms |

---

## Usage limits and conversion

| Tier | Features |
|---|---|
| Free (no login) | Single jurisdiction ToS + AUP; watermarked PDF + DOCX |
| Registered | Multi-jurisdiction output; Refund Policy; cookie policy; editable online |
| Pro | DMCA procedure; API access; enterprise negotiation clauses; custom header/footer; team collaboration |

**Lead-gen nudge:** Free-tier output includes an in-document note: *"This terms document was generated for standard consumer use. For SaaS enterprise agreements, marketplace terms, or contracts with corporate customers, upgrade to Louis Pro or consult with a commercial lawyer."*

---

## Behavior rules

- **Consumer law mandatory provisions cannot be excluded.** EU and UK consumer rights (right of withdrawal, implied warranties) are mandatory and must be included even if the user's selected terms attempt to exclude them; the generator enforces this.
- **Children's content.** If the business type is content platform or app and the target audience might include children, add COPPA language (US) and applicable MENA child protection provisions.
- **AI-generated content disclaimer.** If the platform generates AI content, include a disclaimer that content may be AI-generated; reference applicable AI regulations (EU AI Act labeling requirements for AI-generated content for EU-facing services).
- **Always include legal disclaimer.** *"These terms were generated by Louis (louis.haqq.ai) as a starting point. They do not constitute legal advice. Have these terms reviewed by qualified legal counsel before publishing, especially if your service handles personal data, financial transactions, or operates in regulated sectors."*

---

## Failure modes

| Failure mode | Response |
|---|---|
| User's business description suggests a regulated activity (banking, insurance, healthcare, legal services) | Generate standard ToS and include a prominent warning: "Your business may require a licence and sector-specific terms and conditions. A generic Terms of Service is insufficient — consult a specialist lawyer." |
| Multi-jurisdiction selection (> 3 jurisdictions) | Generate a base ToS with EU/GDPR as the most restrictive standard, plus jurisdiction-specific addenda; note that local counsel review is recommended for each jurisdiction |
| User selects "marketplace" with user-generated content | Include full platform liability provisions and content moderation obligations; for EU-facing marketplaces with significant user numbers, reference DSA compliance requirements |

---

## Related skills

- [[public-tool-privacy-policy-generator-public]]
- [[public-tool-nda-generator-public]]
- [[public-tool-contract-summarizer-public]]
- [[prompt-pack-saas-subscription-agreement]]
