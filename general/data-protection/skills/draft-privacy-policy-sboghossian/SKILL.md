---
name: draft-privacy-policy-sboghossian
title: Privacy Policy
description: Use when drafting a public-facing privacy policy — the notice to users and data subjects explaining how personal data is collected, used, shared, retained, and protected. Covers GDPR (EU/UK), KSA PDPL, UAE PDPL (Federal Decree-Law 45/2021), and EG PDPL (Law 151/2020), with jurisdiction-specific legal-basis requirements, DPO obligations, international-transfer mechanisms, and subject-rights disclosures. Triggers on "privacy policy", "data protection notice", "data privacy statement", "cookie policy", or "personal data disclosure" requests.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-privacy-policy
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
---

# Privacy Policy

## When to use this

A privacy policy is the public-facing notice an organization provides to individuals (data subjects) explaining how it processes their personal data. It is legally required under GDPR, UK GDPR, KSA PDPL, UAE PDPL, and analogous laws in Egypt and elsewhere.

Use this skill when:
- Launching a new website, app, or service that collects personal data
- An existing privacy policy needs to be updated to reflect new laws (PDPL, UAE PDPL) or new processing activities
- A client operating across multiple jurisdictions needs a single policy that covers all applicable laws
- A regulatory review or audit requires a compliant, up-to-date privacy policy

**Key principle**: the privacy policy must describe what you actually do, not what you would like to do or a generic best-case scenario. Inaccurate policies create dual liability: regulatory enforcement for the mismatch plus the policies themselves being used as evidence of non-compliance.

## Required inputs

| Input | Why it matters |
|-------|---------------|
| Data controller / operator (entity name, registration) | Who is legally responsible for the processing |
| Applicable laws | GDPR / UK GDPR / KSA PDPL / UAE PDPL / EG PDPL — determines structure and required disclosures |
| Categories of personal data collected | Must be specific — "contact information" is not enough |
| Data sources | User-provided / automatically collected / from third parties |
| Processing purposes + legal bases | Purpose-by-purpose with GDPR-style legal-basis disclosure |
| Sharing: subprocessors, group entities, third parties | Names or categories depending on jurisdiction requirements |
| International data transfers | Mechanisms used (SCCs, adequacy decisions, BCRs, equivalence determinations) |
| Retention periods per category | Specific periods — "we keep data as long as necessary" fails GDPR |
| Subject rights mechanism | How users exercise rights (email, form, portal) |

## Document structure

### 1. Who we are (Controller / Operator identity)
```
This Privacy Policy describes how [Company Full Legal Name], a company incorporated in [jurisdiction] with registration number [X] ("we", "us", "our"), processes personal data.

Data Protection Officer: [Name / Title] — [contact email]
(Include DPO contact if you are required to appoint one under GDPR, UAE PDPL, or KSA PDPL)

Contact for privacy matters: [email address]
Postal address: [full address]
```

**DPO requirement**:
- **GDPR**: mandatory if processing at large scale, if processing sensitive data, or if a public authority
- **UAE PDPL**: recommended for large-scale processing; some sectors require it
- **KSA PDPL**: Personal Data Protection Regulations require a data officer for regulated entities

### 2. What personal data we collect

Itemize by category with examples. Do not use vague categories.

| Category | Examples |
|---|---|
| Identity data | Full name, username, date of birth, government ID number |
| Contact data | Email address, phone number, postal address |
| Financial data | Payment card details, bank account, billing address |
| Technical data | IP address, browser type, device identifiers, cookies |
| Usage data | Page views, clicks, session duration, feature usage |
| Location data | GPS coordinates (if requested), general location from IP |
| Communications | Support tickets, chat logs, email correspondence |
| Marketing preferences | Opt-in/opt-out status, communication channel preferences |
| Sensitive data | Health data, biometric data, religious beliefs, political opinions |

Note: "Sensitive" (GDPR "special category") data requires explicit consent or another heightened legal basis. Process it only if strictly necessary. Separate disclosure is required.

### 3. How we collect personal data

- **Directly from you**: when you register, complete a form, make a purchase, contact us, apply for a job
- **Automatically**: through cookies, pixels, analytics tools, server logs — reference the Cookie Policy
- **From third parties**: social login providers, business partners, credit bureaus, marketing platforms
- **From public sources**: public registries, LinkedIn (for B2B prospecting), press coverage

### 4. Why we process your data — purpose and legal basis

This is the most legally significant section. For each purpose, state:
- The purpose
- The legal basis under the applicable law

**GDPR / UK GDPR legal bases** (Art. 6 GDPR):
| Legal basis | When to use |
|---|---|
| Consent | Freely given, specific, informed, and unambiguous; revocable at any time; default for marketing |
| Contract | Processing necessary to perform a contract with the individual |
| Legal obligation | Processing required by law |
| Legitimate interests | Operator's or third party's interests override the individual's, with a documented balancing test |
| Vital interests | Emergency/life-threatening situations only |
| Public task | Public authorities only |

**KSA PDPL** (Royal Decree M/19, updated 2023): consent-first approach; legitimate-interest processing narrower than GDPR; sensitive data requires explicit consent; sector-specific exemptions.

**UAE PDPL** (Federal Decree-Law 45/2021 and Cabinet Decision 33/2022): consent or balancing test; defined legitimate purposes; sensitive data requires consent or applicable necessity.

Example disclosure:
> "We process your contact data to send you marketing emails about our products and services. **Legal basis**: your consent, which you may withdraw at any time by clicking 'Unsubscribe' in any email or by contacting us."

### 5. Who we share your data with

Be specific about categories and, where required, names:

- **Group companies**: for internal administration and shared IT infrastructure — list entities or confirm a group-companies section
- **Service providers (sub-processors)**: hosting, payment processing, analytics, customer support tools — list by category; GDPR requires a processor agreement with each
- **Professional advisors**: lawyers, accountants, auditors — under confidentiality
- **Government and regulatory authorities**: where required by law or court order
- **Business partners**: only where users have consented or it is necessary for the service they requested
- **Corporate transactions**: in connection with a merger, acquisition, or asset sale — data may be transferred; provide notice if this occurs

For international transfers (see Section 6).

### 6. International data transfers

If personal data is transferred outside the originating jurisdiction:

**GDPR / UK GDPR**: transfers to non-adequate countries require:
- Standard Contractual Clauses (SCCs) — EC 2021/914 (GDPR) or UK IDTA
- Binding Corporate Rules (BCRs) for intra-group transfers
- Adequacy decision (data flows to adequate country are unrestricted)
- Derogations (explicit consent for specific transfers; contract performance; public interest)

**KSA PDPL**: cross-border transfer requires:
- Data processing does not endanger national security
- Transfer is to a country with adequate protection or with contractual safeguards
- SDAIA (Saudi Data and AI Authority) approval for transfers of sensitive data

**UAE PDPL**: cross-border transfer requires:
- Destination country has an adequate level of data protection, or
- Appropriate safeguards (contractual clauses meeting Federal law requirements)

Disclosure format:
> "Your data may be transferred to [country / region], which [has been found adequate / is protected by Standard Contractual Clauses / is protected by [specific safeguard]]."

### 7. Retention periods

Never use "as long as necessary" alone — this fails GDPR and is challenged by regulators. State specific periods per category:

| Category | Retention period | Basis |
|---|---|---|
| Customer account data | Duration of account + [3 years] | Contractual / legitimate interest |
| Transaction records | [7 years] from transaction date | Legal obligation (commercial record-keeping) |
| Marketing consent records | [3 years] from last interaction | Legal compliance (GDPR accountability) |
| Security logs | [12 months] rolling | Legitimate interest (fraud detection) |
| Job application data (unsuccessful) | [6 months] from rejection | Legitimate interest |
| Support/complaint records | [3 years] from closure | Legal compliance / legitimate interest |

### 8. Your rights

Under GDPR (and to varying degrees under PDPL laws), individuals have:

| Right | Description |
|---|---|
| **Access** | Right to know what data we hold about you |
| **Rectification** | Right to correct inaccurate data |
| **Erasure ("right to be forgotten")** | Right to request deletion (subject to overriding legal obligations) |
| **Restriction** | Right to limit processing in certain circumstances |
| **Portability** | Right to receive your data in machine-readable format (GDPR; consent or contract basis only) |
| **Objection** | Right to object to processing based on legitimate interests or for direct marketing |
| **Withdraw consent** | Right to withdraw consent at any time without affecting prior lawful processing |
| **Complaint** | Right to lodge a complaint with the supervisory authority |

Supervisory authorities by jurisdiction:
- **EU**: national DPA (CNIL - France; BfDI - Germany; ICO - UK for UK GDPR; etc.)
- **UAE**: UAE Data Office (UDO) for Federal PDPL matters
- **KSA**: Saudi Data and AI Authority (SDAIA)
- **EG**: NCPD (National Center for Personal Data Protection — Law 151/2020)

### 9. Cookies

Brief reference: "We use cookies and similar tracking technologies on our website. Please see our [Cookie Policy] for detailed information about the cookies we use, their purposes, and how to manage your preferences."

### 10. Children

- **GDPR**: age of consent for data processing is 16 (lower in some member states); under-13s require parental consent
- **UAE PDPL**: under-18 requires parent/guardian consent for data processing
- **KSA PDPL**: sensitive data for minors requires heightened protection; parental consent required

State: "Our services are not intended for individuals under [16/18] years of age. We do not knowingly collect personal data from children. If we become aware that we have inadvertently collected personal data from a child, we will delete it promptly."

### 11. Security measures

High-level statement:
> "We implement appropriate technical and organizational measures to protect your personal data against unauthorized access, disclosure, alteration, or destruction. These measures include encryption of data in transit and at rest, access controls, regular security assessments, and staff training."

Do not specify security controls in detail in a public-facing document — this creates a target.

### 12. Changes to this policy

> "We may update this Privacy Policy from time to time. Material changes will be communicated by [email notice / prominent notice on our website / in-app notification] before taking effect. The effective date at the top of this policy indicates when it was last updated."

### 13. Contact us

> "To exercise your rights, submit a privacy inquiry, or make a complaint, please contact: [email] [postal address]."

## Jurisdiction-specific sections

For multi-jurisdiction policies, add jurisdiction-specific addenda:

**For KSA residents (KSA PDPL)**:
- Consent withdrawal mechanism
- Local data residency commitments for sensitive data (if applicable)
- SDAIA complaint procedure

**For UAE residents (UAE PDPL)**:
- UAE Data Office complaint procedure
- Cross-border transfer safeguards applicable to UAE residents

**For EU/UK residents (GDPR / UK GDPR)**:
- Legal bases per processing purpose (must be explicit)
- DPO contact (if applicable)
- EU/UK supervisory authority complaint rights

## Critical compliance points

- **Be specific**: vague catch-all language ("we may use your data for various purposes") fails regulatory scrutiny
- **Match your reality**: only disclose practices you actually perform; disclose all practices you do perform
- **Update frequency**: review the policy at least annually and whenever you change processing activities
- **Accountability documentation**: maintain a Record of Processing Activities (ROPA) — the privacy policy is the public-facing summary; the ROPA is the internal record

## Related skills

- [[draft-dpa-gdpr]]
- [[draft-dpa-ksa-pdpl]]
- [[draft-dpa-uae-pdpl]]
- [[draft-cookie-policy]]
- [[review-data-privacy-audit]]
