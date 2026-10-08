---
name: prompt-pack-embedded-finance-partnership-agreement-sboghossian
title: Embedded Finance Partnership Agreement
description: Use when drafting an embedded finance partnership agreement between a regulated financial institution (FinTech or bank) and a non-financial platform that will offer financial services through its application. Covers API integration, revenue sharing, regulatory responsibilities, customer ownership, data sharing, and liability allocation. Relevant for fintech deals in UAE (CBUAE, DIFC, ADGM), KSA (SAMA), LB, EG, UK (FCA), and EU. Trigger when a platform and a licensed financial partner need to structure their embedded banking, lending, or payments arrangement.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-embedded-finance-partnership-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: finance
language: en
---

# Embedded Finance Partnership Agreement

## When to use this

Use this skill when drafting the commercial and regulatory framework agreement for an embedded finance arrangement — where a licensed financial institution (the FinTech or "program manager") provides regulated financial services (banking, lending, payments, e-money, insurance) through a non-financial platform's application. The end customer interacts with the platform's branded experience; the financial product is powered by the FinTech's license and infrastructure.

Typical structures:
- E-commerce platform offering buy-now-pay-later (BNPL) powered by a licensed lender
- Ride-hailing or food-delivery app offering a digital wallet powered by an e-money institution
- B2B SaaS platform offering integrated expense management and corporate cards via a bank API
- Digital marketplace offering merchant acquiring services through a licensed acquirer

The agreement must address both commercial terms and the regulatory dimension: in most jurisdictions, the FinTech is the regulated entity and the platform acts as its distribution partner; the allocation of regulatory obligations must be explicit.

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| FinTech / licensed entity name, license type, and jurisdiction | Determines what regulated services can be offered and which regime applies | Ask |
| Platform name and business description | Defines the distribution channel | Ask |
| Financial services to be embedded (banking, lending, wallet, cards, insurance) | Each service type has different regulatory requirements | Ask |
| Target customer segment (retail consumer, SME, enterprise) | Affects KYC/CDD obligations, consumer protection rules | Ask |
| Revenue model | Revenue share, margin on float, fee per transaction — must be agreed | Ask |
| Governing law and dispute resolution | Must be clear for a regulated contract | Ask |

## Optional inputs

- Exclusivity (can the platform work with other FinTech partners for competing services?)
- White-label branding arrangements (whose brand on the product?)
- Data ownership and portability on termination
- Regulatory change mechanism (what happens if the FinTech's license is revoked or conditions change?)
- Customer migration plan on termination

## Document structure

### 1. Parties and Definitions

Define key terms precisely:
- **FinTech Services**: the specific regulated financial products and APIs being provided
- **Platform Application**: the non-financial software through which services are embedded
- **End Customers**: the users who access the financial services through the Platform
- **Transaction**: each use of the FinTech Services by an End Customer
- **Program Manager** (optional): if the FinTech delegates day-to-day program operations to the Platform

### 2. Scope of Services

- Description of each embedded financial service (wallet, card issuance, lending, payment initiation, etc.)
- API specifications: reference to API documentation; the FinTech's SLA obligations for API availability (99.9% uptime typical)
- Geographic scope of services
- Customer segment restrictions (retail only? SME? licensed activities only in specified jurisdictions)

### 3. Regulatory Responsibilities

This is the most critical section from a compliance perspective:

**FinTech's obligations**:
- Maintain the license(s) required to offer the financial services
- Bear primary responsibility for AML/KYC compliance for End Customers it onboards
- File STRs with the applicable Financial Intelligence Unit
- Implement sanctions screening
- Maintain adequate capital and safeguarding obligations for customer funds
- Report to the regulator as required; provide the Platform with compliance guidance

**Platform's obligations**:
- Only present the FinTech's services as authorized by this agreement
- Not make representations about the financial services that misstate the FinTech's regulatory status
- Implement the KYC/CDD front-end as specified by the FinTech (document collection, liveness checks, etc.)
- Notify the FinTech immediately of any actual or suspected fraud, AML events, or regulatory enquiries
- Maintain IT security standards as specified
- Comply with applicable consumer protection and data protection laws in its own right

**Shared responsibilities** (to be allocated explicitly):
- Customer complaints handling: first line (Platform or FinTech?); escalation path
- Regulatory enquiries: who responds to the regulator when the enquiry touches both parties?
- Financial promotions / marketing: who signs off on marketing materials referencing the financial product?

### 4. Customer Ownership and Data

- **Customer relationship**: Who is the customer's principal counterparty for the financial product? In a regulated sense, the FinTech is the regulated entity and owns the regulatory relationship.
- **Data ownership**: End Customer personal and transaction data — who owns it? Common position: FinTech owns data required for regulatory compliance; Platform owns commercial relationship data; both have rights in aggregate analytics.
- **Data sharing**: Define what data flows between the parties; GDPR / UAE PDPL / KSA PDPL compliance for cross-border data flows.
- **Post-termination data**: Customer records must be retained by the FinTech for regulatory purposes (typically 5–10 years); customer access to their data.

### 5. Revenue Sharing

- **Model 1 — Interchange / fee split**: The FinTech collects interchange or service fees; splits a percentage with the Platform based on transaction volume
- **Model 2 — Gross margin share**: Platform charges end customers; remits a percentage to the FinTech for the regulated service
- **Model 3 — Platform fee**: Platform pays the FinTech a per-user or per-transaction API fee; Platform retains all revenue from end customers
- Include a payment schedule, invoice process, and dispute resolution for revenue calculations
- Specify withholding tax allocation and VAT treatment

### 6. Technology and API

- API terms: reference to separate API documentation and developer agreement
- Change management: FinTech cannot change API in a way that breaks Platform integration without [90]-day notice and migration support
- Downtime: SLA, service credits for downtime exceeding threshold
- Security standards: PCI-DSS compliance (if card data involved); penetration testing obligations; incident reporting timeline (typically 24–72 hours for security incidents)

### 7. Liability and Indemnification

- **FinTech indemnifies Platform** for: losses caused by FinTech's negligence, license failure, or regulatory breach
- **Platform indemnifies FinTech** for: losses caused by Platform's misrepresentation of the financial products, Platform-side fraud, or Platform's data protection breach
- **Consequential loss exclusion**: neither party liable for lost profits, lost data, or indirect losses (subject to carve-outs for gross negligence and willful misconduct)
- **Cap on liability**: typically [12 months' aggregate fees] per incident

### 8. Term and Termination

- Initial term (commonly 2–3 years with auto-renewal)
- Termination for convenience: [90–180] days' notice (longer than a typical SaaS contract because of the operational complexity of migrating end customers)
- Termination for cause: material breach (with [30]-day cure period); insolvency; license revocation
- Consequences of termination: wind-down period; customer transition obligations; data portability; run-off for existing customer balances

## Jurisdictional notes

| Jurisdiction | Regulatory framework for embedded finance | Key considerations |
|---|---|---|
| **UAE (CBUAE)** | Retail Payment Services and Card Schemes Regulation; stored value facility rules | FinTech must hold a licensed payment service provider status; Platforms acting as distribution agents may need registration as "payment facilitators" under CBUAE rules |
| **DIFC (DFSA)** | DFSA Rulebook; Arranging or Providing Money Services authorization required | DFSA distinguishes between a licensed firm (FinTech) and its appointed representatives; Platform may act as appointed representative if properly documented |
| **ADGM (FSRA)** | FSRA Financial Services and Markets Regulations 2015 | Similar to DIFC; FSRA RegLab sandbox available for novel embedded finance models |
| **KSA (SAMA)** | Payment Services Provider Regulations | SAMA requires SAMA-licensed entity to be the primary service provider; Platform must not perform any licensed activity without SAMA approval |
| **UK (FCA)** | E-Money Regulations 2011; Payment Services Regulations 2017 | Platform acting as distributor of e-money may need to be an appointed representative of the FinTech or hold its own FCA authorization; financial promotion rules strictly apply |
| **EU (EMD2 / PSD2)** | Second E-Money Directive (EMD2); Second Payment Services Directive (PSD2) | Platform may act as agent of the EMI; agent registration required with NCA; GDPR governs data sharing |

## Common mistakes

- **Treating the platform as merely a technology provider**: Regulators look through the structure; if the Platform is performing regulated activities (onboarding, marketing, holding funds), it may need its own license.
- **Ambiguous regulatory responsibility allocation**: When a regulator enquires about an AML failure and both parties point to each other, the FinTech — as the licensed entity — bears primary liability regardless of contract.
- **No customer migration plan**: When the partnership terminates, End Customers with funds in the Platform's wallet need a migration path; failure to address this creates stranded customer risk and regulatory exposure.
- **Financial promotions without approval**: In UK, EU, UAE, and KSA, any communication that promotes a financial product must be approved by the licensed entity; the Platform's marketing team cannot draft and publish unapproved financial promotions.
- **Missing PCI-DSS obligations**: If card data is processed through the Platform's application, PCI-DSS compliance obligations must be allocated explicitly; the risk of a card data breach is significant.

## Related skills

- [[prompt-pack-e-money-license-application-memo]]
- [[prompt-pack-distribution-agreement]]
- [[prompt-pack-full-contract-risk-review]]
- [[prompt-pack-independent-contractor-agreement]]
