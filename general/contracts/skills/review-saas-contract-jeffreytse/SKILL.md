---
name: review-saas-contract-jeffreytse
title: Review SaaS Contract
description: Use when reviewing a SaaS vendor or customer contract for legal and commercial risk
author: jeffreytse
author_url: https://github.com/jeffreytse/grimoire-core/tree/main/skills/law/contracts/skills/review-saas-contract
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
tags: [law, saas, software, legal-review, sla, liability]
---

# Review SaaS Contract

Systematically review a SaaS agreement to identify legal, commercial, and operational risks before signing.

## Why This Is Best Practice

**Adopted by:** ABA Technology Law Committee, Gartner IT legal risk frameworks, enterprise procurement legal teams globally
**Impact:** IACCM research shows 9% of contract value is lost to poorly negotiated terms; SaaS contracts introduce unique risks (data ownership, SLA credits, vendor lock-in) absent in traditional software licenses that require specialized review checklists.

**Why best:** SaaS contracts transfer operational dependency to a third party. Unlike on-premise software, the customer cannot access the underlying code if the vendor fails. Contract terms around data portability, SLA remedies, security obligations, and limitation of liability directly determine business continuity risk and legal exposure.

## Steps

1. **Review service level agreement (SLA)** — Confirm: uptime commitment (99.9% = ~8.7 hrs/year downtime; 99.99% = ~52 min/year); measurement methodology (is planned maintenance excluded?); credit structure and credit caps; escalation process; ensure credits are proportionate to actual business impact.
2. **Audit data ownership and portability** — Confirm: customer owns all customer data; vendor has no right to use customer data for training AI models or analytics without explicit consent; data export format is machine-readable (JSON/CSV, not PDF); export available within 30 days of termination.
3. **Review the data processing agreement (DPA)** — Confirm presence of a DPA if the contract involves personal data; verify: processor vs. controller classification, sub-processor list and notification rights, data breach notification timeline (72 hours for GDPR compliance), security standards (SOC 2 Type II, ISO 27001).
4. **Assess limitation of liability** — Standard vendor position: cap at 12 months of fees paid; negotiate for carve-outs (uncapped liability for: data breach, IP indemnification, death/bodily injury, gross negligence, fraud). Mutual limitation is fairer than one-sided cap.
5. **Review IP and license grant** — Confirm: customer retains ownership of all customer data and any configurations or customizations; vendor indemnifies customer against IP infringement claims (if vendor software infringes a third-party patent, vendor defends and pays).
6. **Check termination and exit provisions** — Review: notice period (30–90 days is standard); termination for convenience (critical for customers, often absent in vendor templates); post-termination data access period; wind-down service obligations.
7. **Review pricing and renewal terms** — Identify: auto-renewal clauses (and required cancellation notice — often buried); price escalation caps (limit to CPI + X%); true-up mechanisms for seat counts; payment terms and late payment interest.
8. **Assess security and compliance obligations** — Confirm vendor commits to: specific security standards (SOC 2, ISO 27001); audit rights or third-party audit reports on request; penetration testing frequency; security incident notification; compliance with applicable regulations (GDPR, HIPAA if applicable).

## Rules

- Never sign a contract with a DPA that permits the vendor to use customer personal data for purposes beyond service delivery.
- Always require uncapped indemnification for IP infringement and data breaches; these are existential risks, not ordinary business losses.
- Negotiate a survival clause specifying which provisions survive termination (confidentiality, data return obligations, IP ownership).
- Require a 30–90 day post-termination data return period with accessible export functionality before data deletion.
- Do not accept SLA credits as the sole remedy for data loss; credits are commercially inadequate compensation for a data breach.

## Examples

**Red flag found in review:** Vendor contract states "Company may use aggregated and anonymized Customer Data to improve its products and services." Risk: aggregated/anonymized data derived from customer data could reconstitute sensitive business information. Negotiation: revise to "Vendor may use only fully anonymized, non-customer-identifiable telemetry data, subject to customer opt-out, and shall not share such data with third parties."

## Common Mistakes

- **Accepting vendor template without redline** — Every vendor template is optimized for the vendor; any contract accepted without negotiation leaves commercial and legal value on the table.
- **Ignoring force majeure clauses post-COVID** — Broad force majeure (including "pandemic" or "government action") can excuse vendor SLA obligations for extended periods; negotiate narrow definitions.
- **Missing auto-renewal cancellation windows** — Auto-renewal notice periods as short as 30 days before the renewal date mean missing the window locks you in for another full year.

---

> **Law disclaimer:** This skill encodes professional best practices for educational purposes. It is not legal advice. Consult a licensed attorney before making legal decisions.
