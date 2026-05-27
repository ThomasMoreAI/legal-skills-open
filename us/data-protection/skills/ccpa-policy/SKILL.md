---
name: ccpa-policy
title: CCPA/CPRA Privacy Policy
description: Drafts a CCPA/CPRA-compliant privacy policy covering all required statutory disclosures under Cal. Civil Code §§ 1798.100–1798.199. Use when drafting or updating a California privacy policy, CCPA compliance notice, or consumer privacy disclosure for a business meeting CCPA applicability thresholds.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/ccpa-policy
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: data-protection
language: en
---

# CCPA/CPRA Privacy Policy

Generates a California Consumer Privacy Act / California Privacy Rights Act compliant privacy policy with all required statutory disclosures.

## Quick Start

Gather before drafting:

- **Applicability trigger** — ≥$25M revenue, ≥100K consumer records bought/sold/shared, or ≥50% revenue from selling/sharing PI
- **Data inventory** — categories collected (per § 1798.140), sources, retention periods
- **Purpose map** — business/commercial purpose per data category
- **Third-party sharing** — service providers, contractors, ad networks, affiliates; distinguish business-purpose disclosure from sale/sharing
- **SPI flag** — whether sensitive personal information (§ 1798.121) is collected and right-to-limit applies
- **Children's data** — actual knowledge of collection from consumers under 16
- **Request channels** — minimum two methods (toll-free number + web URL required)
- **Contact details** — legal name, mailing address, privacy contact, DPO/CPO if appointed

## Policy Sections

Draft each section in order:

### 1. Introduction
Effective date, scope (California residents), applicable threshold, governing law (CCPA as amended by CPRA + CPPA regulations).

### 2. Personal Information Collected

| Statutory Category (§ 1798.140) | Examples | Sources |
|---|---|---|
| Identifiers | Name, email, IP, account ID | Direct, automated |
| Commercial information | Purchase history, preferences | Direct, transaction systems |
| Internet/network activity | Browsing, search, interactions | Automated (cookies, pixels) |
| Geolocation | Precise physical location | App/device |
| Professional/employment | Job title, employer | Direct |
| Inferences | Profiles, characteristics | Internal analytics |
| Sensitive PI | SSN, financial, health, biometric | Per § 1798.121 |

Populate from data inventory. Omit inapplicable rows.

### 3. Use Purposes
Map each purpose to its data categories:
- Transaction fulfillment and services
- Customer service / account management
- Payment processing
- Fraud detection and security
- Debugging and error repair
- Research, analytics, improvement
- First-party marketing
- Cross-context behavioral advertising *(triggers sale/sharing opt-out)*
- Legal compliance

### 4. Sharing Disclosures

| Recipient Type | Categories Shared | Purpose |
|---|---|---|
| Service providers / contractors | [list] | Business purposes; contractually restricted |
| Ad networks | [list] | Behavioral advertising (= "sharing" under CPRA) |
| Analytics providers | [list] | Performance analytics |
| Affiliates | [list] | [specify] |
| Government / law enforcement | [list] | Legal process |

If selling/sharing for cross-context behavioral advertising: include conspicuous "Do Not Sell or Share My Personal Information" link (§ 1798.135). State whether business has actual knowledge of selling/sharing PI of consumers under 16.

### 5. Consumer Rights

| Right | Basis | Key Detail |
|---|---|---|
| Know | § 1798.110 | Categories + specific pieces; 12-month lookback |
| Delete | § 1798.105 | Subject to statutory exceptions |
| Correct | § 1798.106 | Inaccurate PI |
| Opt-Out of Sale/Sharing | § 1798.120 | Cross-context behavioral advertising |
| Limit SPI Use | § 1798.121 | Sensitive PI only |
| Data Portability | § 1798.110(d) | Machine-readable format |
| Non-Discrimination | § 1798.125 | No denial/differential pricing |

### 6. Request Procedures
- **Methods** (≥2 required): toll-free number, web form, email (optional)
- **Verification**: match consumer-provided info against records; no account creation required
- **Timelines**: acknowledge within 10 business days; respond within 45 calendar days (extendable +45 with notice)
- **Authorized agents**: signed written permission or POA; may verify directly with consumer
- **Frequency**: two free Right-to-Know requests per 12 months

### 7. Children's Privacy

| Age | Requirement |
|---|---|
| Under 13 | Parent/guardian opt-in (§ 1798.120(d)) |
| 13–15 | Consumer opt-in |

If no knowing collection from under-16 consumers, state explicitly with safeguards.

### 8. Policy Updates
Specify revision triggers, notice method for material changes, effective date, and version archiving commitment.

### 9. Contact Information
Legal name, mailing address, privacy email, toll-free number, DPO/CPO (if applicable), request portal URL.

## Pitfalls

- **Accuracy over aspiration** — policy must reflect actual practices; material discrepancies risk Cal. Bus. & Prof. Code § 17200 liability
- **Statutory terms of art** — use "service provider," "sell," "share" exactly as CCPA defines them; plain language everywhere else
- **CPRA alignment** — right to correct, right to limit SPI, and CPPA rulemaking must be current; verify latest CPPA regulations
- **Conspicuous posting** — homepage-accessible, accessibility-compliant
- **Cross-document coordination** — align with cookie policy, employee privacy notice, vendor DPAs
- **Annual review** — minimum annually and upon material practice or legal changes
- **Legal review required** — qualified California privacy counsel must review before publishing
