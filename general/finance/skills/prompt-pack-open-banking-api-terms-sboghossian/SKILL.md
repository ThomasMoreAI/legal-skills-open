---
name: prompt-pack-open-banking-api-terms-sboghossian
title: Open Banking API Terms
description: 'Use when drafting API terms of service for a bank or fintech offering open banking APIs to third-party providers (TPPs), developers, or payment initiation services. Covers access credentials, rate limits, data usage restrictions, security requirements, liability, SLA commitments, and compliance with applicable open banking regulations. MENA-focused: UAE Central Bank open finance framework, SAMA open banking framework (KSA), and EU PSD2 as a reference standard.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-open-banking-api-terms
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: finance
language: en
---

# Open Banking API Terms

## When to use this

Use this skill when a bank, financial institution, or fintech company needs to draft the API terms of service governing third-party access to its open banking APIs. The document is addressed to third-party providers (TPPs) — developers, payment initiation service providers (PISPs), account information service providers (AISPs), or other authorized partners.

Triggers:
- "Draft API terms for our open banking platform."
- "We need terms of service for third-party developers accessing our banking APIs."
- "Draft a developer agreement for our open finance sandbox."

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| API Provider (bank/fintech) name | Identifies the issuing institution | Ask user |
| Jurisdiction / regulatory framework | Determines compliance obligations (SAMA, UAE CBUAE, PSD2, etc.) | Ask user |
| API types offered | Account information, payment initiation, card issuance — different regulatory treatments | Ask user |
| TPP eligibility requirements | Who may apply — licensed entities only vs open to all developers | Ask user |
| Commercial model | Free / freemium / paid API access — determines billing terms | Ask user |

## Optional inputs

- Sandbox vs production environment distinction
- Whether OAuth 2.0 / OpenID Connect is the authentication standard
- Rate limiting parameters (calls per second, daily limits)
- Insurance requirements for TPPs (cyber liability, professional indemnity)
- Data residency requirements

## Document structure

### 1. Introduction and Acceptance
- Provider identity and regulatory status
- What these terms govern: the right to access and use [Provider's] APIs
- How acceptance occurs: registering for developer access, or executing a separate API licence agreement for production access
- Who may accept: only eligible entities (see eligibility section)

### 2. Eligibility and Registration

**Eligibility**:
- TPPs must be licensed or authorized under applicable law to provide the relevant services (AISP, PISP, fintech licence)
- In KSA: authorization from SAMA's Open Banking Lab required
- In UAE: compliance with UAE Central Bank Open Finance regulation
- In EU: PSD2-compliant authorization from home-country competent authority (or exemption)

**Registration process**:
- Create a developer account at [Developer Portal URL]
- Submit required documents: company registration, regulatory licence, data protection policy, cyber security questionnaire
- Agree to these API Terms
- Provider reviews and approves; issues API credentials (client ID, client secret) upon approval
- Separate production access approval required after successful sandbox testing

### 3. API Access and Credentials

**Access grant**:
> "Subject to these Terms, Provider grants TPP a limited, non-exclusive, non-transferable, revocable licence to access and use the APIs solely for [building licensed TPP services for Provider's customers / developing and testing applications in the sandbox environment]."

**Credential obligations**:
- TPP must keep API credentials (client ID, client secret, certificates) secure and confidential
- Credentials must not be shared with sub-contractors or embedded in client-facing code
- Immediate notification to Provider if credentials are compromised
- Each application or service must use separate API credentials (no credential sharing across products)

**No data scraping**: APIs must not be used to scrape, index, or aggregate data beyond the permitted scope; screen-scraping of Provider's interfaces is prohibited even if technically possible.

### 4. Permitted and Prohibited Uses

**Permitted uses**:
- Account information services (AIS): accessing account balance, transaction history with customer consent
- Payment initiation services (PIS): initiating payments from customer accounts with customer consent
- Card-based payment instrument issuance (CBPII): confirming availability of funds for card transactions with consent
- Application development and testing in the sandbox environment

**Prohibited uses**:
- Using API data for purposes not authorized by the customer's consent
- Selling, sublicensing, or sharing API data with third parties without express customer and Provider authorization
- Using APIs in applications that facilitate illegal activity, money laundering, or terrorist financing
- Automated bulk data collection or harvesting
- Reverse engineering the APIs or Provider's systems
- Any use that would violate applicable data protection law

### 5. Rate Limits and Technical Standards

- API rate limits: [X] calls per second per TPP; [Y] calls per day per customer; [Z] calls per month in total
- Exceeding rate limits: requests above the limit will receive a 429 (Too Many Requests) response; sustained excess may result in suspension
- Authentication: OAuth 2.0 with PKCE; OpenID Connect for identity; FAPI (Financial-grade API) profile mandatory for production access
- Transport security: TLS 1.2 minimum; TLS 1.3 preferred
- API versioning: Provider will maintain APIs for [12 months] after a new version is released; advance notice of [90 days] for breaking changes

### 6. Data Protection and Privacy

- TPP must have a compliant privacy policy and data processing agreement in place with each end customer before accessing their data via the APIs
- Customer consent must be obtained in the form required by applicable law (PSD2 explicit consent; UAE CBUAE consent framework; SAMA consent framework)
- TPP must not process customer data for any purpose beyond what is authorized by the customer's consent
- Data retention: TPP must delete customer API data within [90 days] of consent withdrawal or customer request
- **Data processing agreement (DPA)**: a DPA between Provider and TPP is required for production access where Provider acts as data processor on behalf of TPP (or vice versa, depending on data flows) — attach as Annex [X]

### 7. Security Requirements

TPP must implement and maintain:
- ISO 27001 or equivalent information security management
- Annual penetration testing with reports available to Provider on request
- Vulnerability disclosure program
- Encryption of all customer data at rest (AES-256) and in transit (TLS 1.3)
- Multi-factor authentication for all access to API management systems
- Incident response plan covering API-related security incidents
- Notification to Provider of any security incident involving API access within [24 hours] of discovery

### 8. Service Level Agreement (Provider's Obligations)

| Metric | Target |
|---|---|
| API availability (production) | ≥ 99.5% per calendar month |
| API availability (sandbox) | Best efforts |
| Scheduled maintenance notice | ≥ 72 hours advance notice |
| Critical security patch deployment | Within [24 hours] of known exploit |
| API response time (95th percentile) | ≤ [500 ms] for account information endpoints |
| Support response time (critical issues) | ≤ [4 hours] during business hours |

Service credits for SLA breaches: [state credit mechanism or say "not applicable"].

### 9. Liability

**Provider's limitation of liability**:
- Provider is not liable for: failure of TPP's applications; customer losses arising from TPP's use of APIs; incorrect or incomplete API data arising from errors in customer records
- Provider's total liability to TPP in any 12-month period is limited to [EUR 500,000 / USD 500,000 / or fees paid in the period, whichever is lower]

**TPP's indemnity**:
- TPP indemnifies Provider against claims arising from: TPP's breach of these Terms; TPP's unauthorized use of customer data; TPP's non-compliance with applicable regulatory requirements

**Carve-outs from Provider's limitation**: fraud, gross negligence, willful misconduct, data protection breach (subject to applicable regulatory maximum).

### 10. Compliance Obligations

TPP represents and warrants on a continuing basis:
- It holds all required licences and authorizations to provide the services it offers using the APIs
- It complies with applicable AML/CFT law (FATF 40 Recommendations; UAE AML Cabinet Decision; KSA AML Law; EU AMLD)
- It complies with applicable data protection law (GDPR, UAE PDPL, KSA PDPL)
- Its use of the APIs does not violate applicable payment systems rules (Mastercard, Visa, local payment network rules)
- It has a documented information security policy reviewed at least annually

### 11. Certification and Audit

- Provider may require TPP to provide third-party audit reports (SOC 2, ISO 27001 certificate) annually
- Provider has the right to audit TPP's API usage logs on [30-day] notice to verify compliance
- Provider may conduct technical testing of TPP's API integration to verify security compliance

### 12. Term and Termination

- These Terms remain in effect for as long as TPP has active API credentials
- Provider may suspend or terminate API access immediately for: breach of security requirements; regulatory compliance failure; unauthorized data use; Provider required to do so by its regulator
- TPP may terminate by written notice and deregistering its applications
- Upon termination: TPP must delete all API data and certify deletion; outstanding API calls will be rejected

### 13. Governing Law and Regulatory Compliance
- MENA-jurisdiction APIs: governing law should match Provider's regulator (UAE CBUAE → UAE law; SAMA → KSA law)
- Cross-border APIs: consider DIFC or ADGM as neutral forum for international TPPs
- Nothing in these Terms limits the authority of any competent regulator

## Jurisdictional notes

| Jurisdiction | Framework |
|---|---|
| **UAE** | UAE Central Bank Open Finance Regulation (2023); phased rollout; banks required to offer open banking APIs in prescribed formats; TPPs require CBUAE licence. |
| **KSA** | SAMA Open Banking Framework (2022); Open Banking Lab for TPP onboarding; Fintech Saudi support; API standards aligned with Berlin Group NextGenPSD2 framework. |
| **EU (PSD2)** | Strong Customer Authentication (SCA) mandatory; banks must offer dedicated API interface; XS2A (Access to Accounts) rights for licensed TPPs; RTS on SCA sets technical standards. |
| **UK (post-Brexit)** | Open Banking Implementation Entity (OBIE) standards; CMA9 banks must offer open banking APIs; FCA authorizes AISPs and PISPs. |

## Common mistakes

- **Not requiring TPP regulatory licence verification at onboarding**: allowing any developer to access production APIs without verifying licence status exposes Provider to regulatory and reputational risk.
- **No rate limiting**: without rate limits, a single TPP can overload the API and cause service degradation for all other TPPs and customers.
- **Weak data deletion obligation**: MENA data protection laws require specific deletion timelines; vague retention language creates compliance risk.
- **No DPA**: where the API involves processing of personal data on behalf of customers, a formal DPA between Provider and TPP is legally required under GDPR, UAE PDPL, and KSA PDPL.

## Related skills

- [[prompt-pack-lending-platform-terms]]
- [[prompt-pack-payment-services-agreement]]
- [[prompt-pack-payment-facilitator-agreement]]
- [[prompt-pack-privacy-impact-assessment]]
- [[heuristic-always-state-jurisdiction-first]]
