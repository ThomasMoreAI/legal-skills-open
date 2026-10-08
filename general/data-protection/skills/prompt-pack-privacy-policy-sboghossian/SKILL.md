---
name: prompt-pack-privacy-policy-sboghossian
title: Privacy Policy
description: Use when a lawyer or compliance officer needs to draft a comprehensive privacy policy for a company operating across one or more jurisdictions. Covers data collection, legal bases, retention, individual rights, international transfers, cookies, and privacy contact information. Particularly useful for MENA-operating businesses navigating UAE Federal Decree-Law No. 45 of 2021, Saudi PDPL, Lebanese data-protection norms, DIFC/ADGM Data Protection Law, and EU GDPR as applicable.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-privacy-policy
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
---

# Privacy Policy

## When to use this

Use this skill when a client needs to publish or update a privacy policy for:
- A new product, website, or mobile application going live in one or more jurisdictions.
- An existing company responding to a new data-protection law (e.g., UAE PDPL, Saudi PDPL, DIFC DP Law 2020) that creates a fresh compliance obligation.
- A cross-border SaaS or fintech platform whose users are spread across MENA, EU, and UK and whose policy must satisfy multiple regulators simultaneously.
- An internal compliance gap: the company already processes personal data but has no adequate public-facing notice.

Do **not** use this skill as a substitute for full legal advice on complex data-sharing arrangements, data breach notification obligations, or regulatory registration requirements — it generates a strong first draft; a qualified privacy lawyer must review before publication.

## Required inputs

| Input | Why it matters | Sensible default if omitted |
|---|---|---|
| **Company name and entity type** | Determines the legal controller identity and any local registration obligations | Ask before drafting |
| **Description of the business and data flows** | Defines what categories of personal data are collected, from whom, and why | Ask: "What data do you collect, from which individuals, and what do you do with it?" |
| **Jurisdictions of operation** | Each jurisdiction triggers different legal bases, rights, and disclosure obligations | If omitted, draft for UAE (onshore) + DIFC as the minimum MENA baseline |
| **Data retention periods** | Required by GDPR Art. 13, UAE PDPL, and DIFC DP Law | Default: "as long as necessary for the stated purpose, and no longer than [X years]" with a note to specify |
| **Contact details for privacy inquiries** | Required disclosure in every major data-protection law | Ask; placeholder "[privacy@company.com]" if not provided |

## Optional inputs

- **Cookie and tracking technologies inventory** — if present, enables a dedicated cookies section; otherwise use a high-level notice.
- **Third-party processors list** — allows naming key processors (cloud hosts, analytics, payment processors) rather than generic reference.
- **Data Protection Officer (DPO) identity** — mandatory for certain GDPR and DIFC-regulated entities.
- **Age restrictions / children's data** — triggers COPPA-style or DIFC/UAE age-verification language.
- **Cross-border transfer mechanisms** — Standard Contractual Clauses, adequacy decisions, DIFC Art. 27 approved transfers, KSA PDPL rules.

## Document structure

1. **Introduction and controller identity** — who is responsible for the data, registered address, regulatory context.
2. **Scope** — what personal data, which individuals (customers, employees, website visitors), which services.
3. **Categories of personal data collected** — identification data, contact data, financial data, usage/behavioral data, special categories (health, biometrics) if applicable.
4. **Purposes and legal bases for processing** — table pairing each purpose with its legal basis (consent, contract, legitimate interests, legal obligation). This section is the most jurisdiction-sensitive.
5. **Data retention** — specific periods per category, or criteria used to determine them.
6. **Disclosure to third parties** — categories of recipients, processor vs. controller distinction.
7. **International data transfers** — mechanisms used; specific language for each applicable jurisdiction (see Jurisdictional notes).
8. **Individual rights** — access, rectification, erasure, portability, objection, restriction, withdrawal of consent; how to exercise them and response timescales.
9. **Cookies and tracking** — types used, purposes, how to opt out; link to cookie policy if separate.
10. **Security** — technical and organizational measures (keep general to avoid commitment to specific controls).
11. **Children's data** — if the service is not directed at minors, a brief disclaimer; if it is, specific consent and parental approval language.
12. **Changes to this policy** — how users will be notified of material changes.
13. **Contact and complaints** — privacy team contact, right to lodge complaints with the applicable supervisory authority.

## Jurisdictional notes

### UAE — onshore (Federal Decree-Law No. 45 of 2021 on Personal Data Protection)
- Applies to processing of personal data of UAE residents by entities in the UAE.
- Requires a clear legal basis; consent must be explicit, informed, and withdrawable.
- Cross-border transfers allowed only to countries with adequate protection or with specific safeguards (regulations still evolving as of 2026 — verify current status of the UAE Data Office implementing decisions).
- Sensitive data (health, biometric, financial, genetic, etc.) requires additional protections.
- Individual rights include access, correction, erasure, and restriction.

### DIFC (Data Protection Law, DIFC Law No. 5 of 2020 as amended)
- Applies to controllers and processors established in the DIFC.
- Closely modeled on GDPR; six lawful bases; DPO mandatory for certain controllers.
- Cross-border transfers under Art. 27: adequacy decision by the Commissioner, or contractual safeguards, or explicit consent.
- 72-hour breach notification to the DIFC Commissioner of Data Protection.

### ADGM (Data Protection Regulations 2021)
- Administered by the ADGM Registration Authority; GDPR-equivalent structure.
- DPO required for large-scale processing or special-category data.
- Follows adequacy decisions closely aligned with UK GDPR post-Brexit list.

### KSA — Saudi PDPL (Personal Data Protection Law, Royal Decree M/19 of 2021, effective September 2023)
- Arabic-language policy copy may be required when directed at Saudi residents.
- Requires explicit consent for sensitive data; purpose limitation strictly enforced.
- Cross-border transfers require SDAIA approval or adequacy finding.
- Penalties: up to SAR 5 million for violation; imprisonment for aggravated breaches.

### Lebanon
- No comprehensive data protection law in force as of 2026 (draft law pending); fallback to general privacy principles in Civil Code and specific sector rules (banking, telecom).
- For MENA-facing businesses, DIFC or GDPR standards are recommended as the practical compliance baseline.

### EU / GDPR (Regulation 2016/679)
- Applies extraterritorially when targeting or monitoring EU residents.
- Legal bases: Art. 6 (general), Art. 9 (special categories).
- Data subject rights response: one month standard, extendable to three months.
- SCCs (2021 version) or BCRs for transfers to third countries lacking adequacy.

### UK GDPR (post-Brexit)
- Substantially equivalent to EU GDPR; UK SCCs (IDTA) for transfers out of UK.
- ICO is the supervisory authority.

## Drafting standards

- Write in plain language accessible to a non-lawyer reader; avoid unexplained legal jargon.
- Use active voice and short sentences for the rights and contact sections — these are the parts users actually read.
- Do **not** use `[INSERT X]` placeholders in the published draft; resolve every placeholder before handing to the client.
- State the effective date and "last updated" date prominently.
- Where multiple jurisdictions apply, structure the policy so the jurisdiction-specific supplement is clearly demarcated (e.g., an addendum for EU/UK users, another for DIFC users).
- Avoid overly broad retention language ("we keep data as long as necessary") without tying it to specific periods — regulators treat vagueness as non-compliance.

## Common mistakes

- **Asserting "legitimate interests" as a legal basis without a balancing test.** In GDPR and DIFC contexts, document the balancing test separately; don't just cite the basis in the policy.
- **Ignoring the UAE PDPL cross-border transfer requirements.** Companies often replicate GDPR SCCs wholesale without checking whether UAE-specific conditions are met.
- **No Arabic version for KSA-directed services.** SDAIA expects a policy accessible to Arabic-speaking data subjects.
- **Children's data handled silently.** Even if minors aren't the target audience, the policy must state the minimum age and what happens if an underage user is identified.
- **Generic "security measures" language.** Avoid listing specific technical controls in the policy itself — this creates liability if controls change; say "appropriate technical and organizational measures" and point to your security documentation.

## Related skills

- [[prompt-pack-saas-terms-of-service]]
- [[prompt-pack-data-processing-agreement]]
- [[prompt-pack-regulatory-change-impact-assessment]]
- [[prompt-pack-regulatory-filing-checklist]]
- [[heuristic-always-state-jurisdiction-first]]
- [[heuristic-no-us-style-boilerplate-in-civil-law-jx]]
