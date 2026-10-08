---
name: draft-terms-of-service-sboghossian
title: Terms of Service
description: Use when drafting Terms of Service, Terms of Use, or Terms and Conditions for a website, app, SaaS platform, or marketplace. Covers all standard sections including acceptance, eligibility, user content licensing, IP ownership, disclaimers, limitation of liability, indemnification, termination, and modification. Addresses jurisdiction-specific consumer protection overlays including EU Directive 2011/83, CCPA arbitration mechanics, and UAE Federal Law 4/2022 and KSA Consumer Protection Law for MENA operators. Always pair with a Privacy Policy.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-terms-of-service
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Terms of Service

Terms of Service (ToS) — also called Terms of Use or Terms and Conditions — is the contract between an operator and its users governing access to and use of a digital product. For B2C products especially, the ToS must navigate a patchwork of consumer-protection laws that override forum-selection and limitation clauses; drafting as if only one jurisdiction applies is a common and expensive mistake.

## When to use this

- Launching a new website, app, SaaS platform, marketplace, or digital service
- Updating an existing ToS to address a new product feature, jurisdiction, or legal requirement
- Reviewing a third-party platform's ToS before integration
- Converting an informal "by using this site you agree" notice into a proper binding agreement

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Service description | What the product is; determines applicable regulations | Must provide |
| Operator entity + jurisdiction of incorporation | Whose law governs; regulatory obligations | Must provide |
| User base (B2C, B2B, mixed) | Determines consumer protection overlay | Must specify; B2C triggers significantly more consumer law |
| Payment handling | Free, paid, freemium, subscription | Must specify; auto-renewal has specific disclosure requirements |
| User-generated content | Whether users can post content | Must specify; UGC requires a license grant clause and a takedown policy |
| Data processing | Must cross-reference the Privacy Policy | Always link to a current Privacy Policy |
| Age requirement | Minimum age for users (COPPA in US, GDPR Art 8 in EU for under-16s) | 18 (adjustable by jurisdiction) |
| Disputes mechanism | Courts or arbitration; class action waiver for US B2C | Must specify |

## Document Structure

### 1. Introduction and Acceptance

Start with clear acceptance mechanics:
- "By accessing or using [Service], you agree to be bound by these Terms."
- State effective date
- Indicate how users accept: (a) click-through "I Accept" during signup — binding in all major jurisdictions; (b) continued use after notice of updated terms (for modifications)

### 2. Eligibility

- Minimum age requirement
- Geographic restrictions (if the service is not available in certain countries, state this — blocks "I didn't know" defenses)
- Capacity: users must have legal capacity to enter into contracts
- For B2B: user must be authorized to bind the organization they represent

### 3. Account Creation and Security

- Username/password obligations
- User responsibility for account security and all activity under the account
- Obligation to notify operator of unauthorized access
- Operator's right to suspend or terminate accounts for:
  - Violation of these Terms
  - Fraudulent or illegal conduct
  - Risk of harm to users, operator, or third parties
  - Regulatory requirement

### 4. Acceptable Use

Prohibited conduct:
- Any illegal, fraudulent, or harmful use
- Infringement of third-party IP
- Posting of prohibited content (define: hate speech, harassment, spam, malware, child exploitation material)
- Circumventing access controls or security features
- Commercial use of the service without authorization (for B2C products that prohibit API scraping)
- Reverse engineering, decompiling, or extracting source code (subject to applicable law limitations on this prohibition)

### 5. User Content

If the service allows users to post, upload, or submit content:
- **License grant to operator**: "By posting content, you grant [Operator] a worldwide, royalty-free, sub-licensable, perpetual [or: for the duration of your account] license to use, reproduce, modify, display, distribute, and publish your content for the purposes of operating and promoting the Service."
- **Retention of ownership**: "You retain ownership of your content subject to the above license."
- **Representations**: User warrants that: (a) they own or have the right to grant this license; (b) the content does not infringe any third party's rights; (c) the content does not violate these Terms
- **Takedown**: operator may remove content that violates these Terms or applicable law; see also [[draft-takedown-dmca]] for the DMCA counter-notice process

### 6. Intellectual Property

- **Operator's IP**: service, software, design, trademarks, and all other IP are owned by the operator (or its licensors); no license except to use the service as permitted by these Terms
- **Feedback**: if users submit feedback or suggestions, operator has a royalty-free license to use feedback without restriction (avoids a user claiming ownership of a feature idea)
- **Restrictions**: users may not: (a) sublicense access to the service; (b) use operator's trademarks without written permission; (c) remove copyright or proprietary notices

### 7. Payment and Subscriptions (if applicable)

- **Pricing**: current pricing available at [pricing page]; operator may change pricing with [30-day] notice
- **Billing cycle**: monthly/annual; payment by [accepted payment methods]
- **Auto-renewal**: subscriptions auto-renew unless cancelled before the renewal date; renewal notice must be sent in advance (specific requirements in EU, US states)
- **Refunds**: state the refund policy clearly; B2C platforms in EU have a 14-day withdrawal right for distance contracts that may apply to digital services depending on the service type and whether the user has consented to immediate performance
- **Taxes**: user is responsible for applicable taxes; operator adds VAT/GST where required by law
- **Failed payments**: service may be suspended on failed payment after [X] days

### 8. Disclaimers

- **"AS IS" / "AS AVAILABLE"**: the service is provided without warranties, express or implied, to the maximum extent permitted by applicable law
- **Disclaim**: merchantability, fitness for a particular purpose, non-infringement, accuracy, completeness of information
- **Note on consumer law**: in EU and UK, implied terms in consumer contracts (satisfactory quality, fitness for purpose) cannot be fully disclaimed; the disclaimer applies only to the extent permitted by law — say this explicitly to avoid the entire disclaimer being void

### 9. Limitation of Liability

- **Cap**: operator's liability is limited to the greater of: (a) the amount the user paid in the 12 months preceding the claim, or (b) [USD 100 / EUR 100]
- **Excluded losses**: in no event is operator liable for: indirect, incidental, consequential, special, or punitive damages; loss of revenue, data, goodwill, or business; even if advised of the possibility of such damages
- **Consumer law carve-out**: nothing limits liability for death or personal injury caused by negligence, fraud, or any other liability that cannot be limited by law (EU / UK mandatory)
- **Mutual limitation (for B2B)**: apply the same cap to user's liability to the operator

### 10. Indemnification (B2B or for breach-related claims in B2C)

User indemnifies operator against third-party claims arising from:
- User's violation of these Terms
- User's content (IP infringement, defamation)
- User's use of the service in violation of applicable law

For B2C: indemnification clauses are generally unenforceable in EU consumer contracts; limit to cases where the consumer has acted illegally or outside the scope of the ToS.

### 11. Termination

- **By operator**: with notice (30 days) or immediately for material breach
- **By user**: by closing account at any time
- **Effect**: surviving obligations (IP ownership, confidentiality, dispute resolution, limitation of liability, indemnification) continue after termination
- **Data on termination**: state clearly what happens to user data after termination; cross-reference Privacy Policy

### 12. Modification of Terms

- Operator may modify the ToS at any time with [30-day] advance notice (by email or in-app notification)
- Continued use after the effective date of modified terms constitutes acceptance
- For material changes, consider requiring active re-acceptance (click-through) rather than passive consent; some jurisdictions may require this for significant changes

### 13. Governing Law and Forum

State the governing law and the exclusive forum (court or arbitration) for disputes.

**Key conflicts with consumer law:**
| Jurisdiction | Issue | Rule |
|---|---|---|
| EU | Forum selection and governing law | Consumer may always sue in the courts of their habitual residence; EU law governs consumer contracts with EU users regardless of forum selection |
| UK | Same post-Brexit | UK Consumer Rights Act; courts of England/Wales or user's local courts |
| US — California | Arbitration with class-action waiver | Enforceable if properly drafted (AAA / JAMS rules, opt-out right, cost allocation); see CFPB rules |
| US — other states | Varies | Some states restrict arbitration clauses for consumer contracts |
| MENA | Less developed consumer overlay | UAE Federal Law 4/2022 on consumer protection; KSA Consumer Protection Law — specific B2C protections increasingly enforced |

### 14. Dispute Resolution

**Option A — Courts (B2B or simple B2C)**: exclusive jurisdiction of [courts]; waiver of jury trial (US)

**Option B — Arbitration (US B2C)**: disputes resolved by binding arbitration under [AAA Consumer Rules / JAMS]; individual claims only (no class arbitration); small claims court exception; 30-day opt-out right from arbitration clause for new users; operator pays arbitration fees above [X]; operator cannot require users to travel to a distant location for hearings

### 15. Contact

- Company name, address, email for legal notices
- Separate contact for DMCA/copyright: DMCA designated agent
- Separate contact for data privacy inquiries (link to Privacy Policy)

## Jurisdiction-Specific Sections to Add

### EU / UK — Consumer Rights
Add a section on statutory rights: "Nothing in these Terms affects your statutory rights as a consumer. If you are located in the EU or UK, you may have additional rights under local consumer protection laws."

### EU — Right of Withdrawal
For certain digital content / services: "If you are a consumer in the EU, you have a 14-day right to withdraw from these Terms after conclusion of the contract, unless you have consented to immediate performance of the digital content / service and acknowledged that your right of withdrawal will be lost. By clicking 'Start using [Service]' you provide this consent and acknowledgment."

### US — California Residents
Add a California-specific section: California Consumer Privacy Act rights; do-not-sell; Shine the Light Act (if applicable); specific arbitration language.

### MENA — UAE
UAE Federal Law 4/2022 on Consumer Protection applies to all consumer-facing products offered in the UAE (whether operator is onshore or offshore to the extent they target UAE users). Key requirements: transparent pricing, no hidden charges, right to information in Arabic, specific protections for digital services.

## Common Mistakes

- **One ToS for all jurisdictions** — EU consumers cannot waive statutory rights; a US-style ToS full of unenforceable provisions damages trust and may be struck down
- **No auto-renewal disclosure** — CCPA (US), EU e-Commerce Directive, and UK consumer regulations all require specific auto-renewal disclosures; courts and regulators take enforcement action
- **UGC license perpetual without user benefit** — "royalty-free, perpetual, irrevocable" license to all user content is standard but sometimes overbroad; consider a term-limited license (for the duration of the user's account plus [6 months]) for user-generated personal content
- **Limitation of liability incompatible with EU consumer law** — if you disclaim all consequential loss for consumer-facing digital services without a carve-out for statutory minimums, the entire limitation clause may be void in the EU
- **Missing DMCA agent** — for US-accessible platforms, designate a DMCA agent with the US Copyright Office

## Related skills

- [[draft-privacy-policy]]
- [[draft-cookie-policy]]
- [[draft-saas-agreement]]
- [[review-tos-platform]]
