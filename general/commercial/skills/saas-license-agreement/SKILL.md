---
name: saas-license-agreement
title: SaaS License Agreement
description: Drafts SaaS License Agreements for cloud-based software subscriptions covering access-based licensing, fees, SLAs, IP, data protection, indemnification, and liability caps. Triggers when the user needs a SaaS agreement, software subscription contract, cloud service license, or technology subscription terms.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/saas-license-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: commercial
language: en
tags: [agreement, drafting, transactional]
---

# SaaS License Agreement

Draft a commercially balanced SaaS License Agreement governing cloud-based software access, data custody, service performance, and subscription payment.

## Quick Start

1. Gather party names, jurisdictions, addresses (licensor + licensee)
2. Confirm deal terms: pricing model (per-user/tiered/consumption), fees, billing cycle, term length
3. Identify technical scope: platform description, modules, API access, usage limits
4. Note SLA commitments (uptime, support tiers) and data/privacy requirements (GDPR, CCPA, HIPAA)
5. Search uploaded documents for term sheets, SOWs, or prior drafts — use concrete terms over placeholders

## Core Sections

### 1. Title Block & Preamble

- Title: "Software as a Service License Agreement"
- Parties with full legal names, jurisdiction, addresses
- Effective Date (specific or "date last signed below")
- Recitals establishing access-based (not ownership) relationship

### 2. Definitions

Define each term self-contained (no circular references):

- **Software/Platform** — SaaS app(s), features, interfaces, updates; browser/mobile/API delivery
- **Services** — access + hosting, maintenance, support, implementation, training
- **Subscription Term** — Initial + Renewal Terms; distinguish from Effective Date
- **Authorized Users** — employees, contractors, affiliates tied to pricing limits
- **Customer Data** — all licensee-uploaded/input/generated info; remains licensee property
- **Confidential Information** — both parties' non-public business/technical/financial info
- **Subscription Fees** — recurring charges, distinct from one-time fees

### 3. License Grant & Restrictions

**Grant:** Non-exclusive, non-transferable, non-sublicensable access right during Subscription Term for internal business purposes. Frame as access license, not sale.

**Scope controls** — match to pricing model:
- Per-user: max count, unique credentials, no sharing
- Usage-based: metrics, allowances, overage rates
- Module-based: included features, add-on process

**Restrictions:** No reverse engineering; no modification outside config; no resale/rental/service bureau use; no unlawful use; API subject to specs and rate limits; affiliate access requires separate terms; all rights not granted are reserved.

### 4. Fees & Payment

- Fee structure per deal (flat/per-user/tiered/consumption)
- Billing cycle (monthly/annual in advance)
- Payment terms: Net 30 (enterprise) or immediate (SMB)
- Price adjustments: 30–90 days notice; cap annual increases if negotiated
- Taxes: licensee responsible except licensor's income taxes
- Late payment: 1.5%/month or max legal rate; suspension after notice + 5–7 day cure
- Fees non-refundable except as expressly provided

### 5. Term & Termination

- **Initial Term:** specific dates or duration from Effective Date
- **Auto-renewal:** successive periods; non-renewal notice 30 days (monthly) / 60–90 days (annual)
- **Termination for cause:** material breach + notice + 15–30 day cure; immediate for non-payment (post-cure), security threats, IP violations
- **Suspension vs. termination:** suspension = temporary; termination = permanent
- **Post-termination:** cease access; return/destroy confidential info (with certification); 30-day data retrieval window then deletion; surviving provisions (payment, confidentiality, IP, liability, indemnification, disputes)

### 6. Intellectual Property

| Category | Owner | Notes |
|---|---|---|
| Software, updates, derivatives | Licensor | Includes features from licensee feedback |
| Customer Data | Licensee | Licensor gets limited processing license |
| Custom code by licensor | Licensor | Licensee gets use license within Services |
| Licensee-specific configs | Negotiable | Default: licensee property |
| Feedback/suggestions | Licensor | Unrestricted use, no compensation |

Require preservation of proprietary notices. Licensee must report known third-party infringement.

### 7. Confidentiality & Data Protection

**Confidentiality:** Same-degree-of-care standard (never less than reasonable); need-to-know only; standard exceptions (public knowledge, prior possession, independent development, compelled disclosure with notice). Survival: 3–5 years; indefinite for trade secrets.

**Data protection:** Reasonable administrative/physical/technical safeguards; define controller/processor roles; address data subject rights, cross-border transfers (SCCs), breach notification (24–72 hrs). Reference DPA as exhibit if GDPR/CCPA/HIPAA applies.

### 8. Warranties & Disclaimers

**Affirmative:**
- Licensor: authority to license; no third-party conflicts; software performs per documentation; professional service standards
- Licensee: authority to contract; rights to uploaded data; legal compliance

**Disclaimers (CONSPICUOUS FORMAT):** Disclaim all implied warranties (merchantability, fitness, title, non-infringement). No guarantee of uninterrupted/error-free operation.

### 9. Limitation of Liability

Draft in **CONSPICUOUS FORMAT**.

1. **Consequential exclusion:** Neither party liable for indirect, incidental, consequential, special, or punitive damages regardless of theory
2. **Aggregate cap:** Fees paid/payable in 12 months preceding claim
3. **Carve-outs:** Payment obligations (excluded); confidentiality breach (2× annual fees); indemnification (own terms); gross negligence/willful misconduct/fraud (unlimited); statutory minimums (unlimited)

### 10. Indemnification

**Licensor indemnifies for:** third-party IP infringement claims from authorized use.
- Remedies: (a) obtain continued-use rights; (b) modify/replace non-infringing; (c) terminate + pro-rata refund
- Exclusions: unauthorized modifications/combinations; non-compliant use; continued use after fix provided

**Licensee indemnifies for:** Customer Data claims (IP, privacy, unlawful content); use violating agreement/law; compromised credentials.

**Procedure (both):** Prompt written notice; reasonable cooperation; indemnitor controls defense/settlement (no fault admission without consent).

### 11. Service Levels & Support (if applicable)

**Uptime SLA:**

| Availability | Credit |
|---|---|
| 99.0–99.5% | 5% monthly fees |
| 98.0–99.0% | 10% monthly fees |
| Below 98.0% | 25% monthly fees |

- Measure monthly; exclude scheduled maintenance (24–48 hrs notice), force majeure, ISP/DDoS, licensee issues
- Credits: request within 30 days; applied to future invoices; sole remedy
- Persistent failure (3+ consecutive months below target) may be material breach

**Support tiers:** Sev 1 Critical (1 hr) → Sev 2 High (4 business hrs) → Sev 3 Medium (1 business day) → Sev 4 Low (2 business days). Excludes custom development, on-site assistance, third-party integrations.

### 12. Compliance & Audit

- Licensee complies with applicable laws (export controls, data protection, anti-corruption)
- Audit: max 1×/year; 10–15 business days notice; primarily via system logs
- Non-compliance: retroactive payment at current rates; overage >5% → licensee reimburses audit costs

### 13. Governing Law & Disputes

- Governing law: licensor's home state; exclude conflict-of-law and CISG
- Choose litigation (exclusive jurisdiction) OR arbitration (AAA/JAMS, single arbitrator, binding)
- Pre-dispute: 30-day good-faith executive negotiation
- Equitable relief available for IP/trade secret/confidentiality without waiving arbitration

### 14. General Provisions

| Provision | Terms |
|---|---|
| Assignment | Consent required (not unreasonably withheld); M&A exception; unauthorized = void |
| Amendments | Written, signed by both |
| Severability | Court modifies to minimum extent; sever if not possible |
| Notices | Email (delivery confirmed), courier, or certified mail |
| Entire agreement | Supersedes prior understandings; establish exhibit precedence |
| Relationship | Independent contractors |
| Force majeure | Excuses performance; terminate if persists 30–60 days |
| Counterparts | Electronic signatures valid |

### 15. Signature Blocks & Exhibits

Signature blocks (name, title, date) for each party. Attach labeled exhibits with order of precedence: SLA, Pricing Schedule, DPA, Acceptable Use Policy.

## Pitfalls & Checks

- Frame as **access-based license** throughout — never imply sale or ownership transfer
- Disclaimers and liability caps must use **CONSPICUOUS FORMAT** (bold/caps) for enforceability
- Adapt data protection to the specific regime (GDPR/CCPA/HIPAA) — avoid generic language
- Mark uncertain legal citations with [VERIFY]
- Maintain defined-term consistency: capitalize throughout; verify every defined term is used and vice versa
- US-focused template — flag jurisdiction-specific enforceability concerns
- Use plain language; avoid archaic legalese ("witnesseth," "hereinafter")
