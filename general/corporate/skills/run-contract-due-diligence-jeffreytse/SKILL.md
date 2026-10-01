---
name: run-contract-due-diligence-jeffreytse
title: Run Contract Due Diligence
description: Use when reviewing contracts systematically for M&A transactions, investment rounds, vendor onboarding, or any situation requiring comprehensive risk identification across a contract portfolio
author: jeffreytse
author_url: https://github.com/jeffreytse/grimoire-core/tree/main/skills/law/contracts/skills/run-contract-due-diligence
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
tags: [due-diligence, contracts, m-and-a, legal-review, risk-assessment, vendor-management]
---

# Run Contract Due Diligence

Systematically identify, categorize, and assess contractual risks across a contract portfolio using structured review methodology so that material risks are surfaced before closing, investment, or onboarding.

> **Disclaimer:** This skill provides a due diligence methodology framework, not legal advice. Contract review findings and risk classifications must be validated by qualified legal counsel before being relied upon for transaction decisions.

## Why This Is Best Practice

**Adopted by:** The ABA Due Diligence Checklist is used by major law firms including Sullivan & Cromwell, Skadden, and Latham & Watkins. IACCM research shows that World Commerce & Contracting members using structured review processes reduce post-signature disputes by 54% and renegotiation costs by 38%.

**Impact:** Undetected contract risks are the leading cause of M&A value destruction — McKinsey estimates 30% of M&A deals fail to meet value targets partly due to undiscovered contractual liabilities. Structured due diligence reduces material discovery surprises by 60–70% compared to ad-hoc review (ABA Survey, 2021).

**Why best:** Issue-by-issue systematic checklists beat narrative review because they ensure nothing is omitted, create defensible audit trails, and allow parallel review by multiple reviewers. Categorizing findings by risk tier (material, moderate, administrative) enables executives to focus attention where it matters.

Sources: ABA Due Diligence Checklist (2022); IACCM Benchmark Report (2021); Adams (2017); Freund "Anatomy of a Merger" (1975, still canonical); Practical Law Company; Westlaw Practical Guidance.

## Steps

1. **Scope the review and build the contract inventory** — Request and organize all contracts from the counterparty. Categorize by type: customer contracts, supplier/vendor agreements, IP licenses, employment agreements, real estate leases, financing documents, regulatory consents, and joint venture agreements. Use a tracking spreadsheet with status columns. Never begin substantive review without a complete inventory.

2. **Prioritize by materiality threshold** — Define a materiality threshold (e.g., contracts >$500K annual value, all IP licenses, all customer agreements representing >1% of revenue). Full review applies to material contracts; streamlined review for below-threshold contracts. Confirm prioritization with the deal team.

3. **Extract key commercial terms** — For each material contract, extract: parties, effective date, term and renewal provisions, pricing and payment terms, minimum volume or revenue commitments, exclusivity provisions, most-favored-nation clauses, and benchmarking rights. Use a standardized extraction template so outputs are comparable across contracts.

4. **Review assignment and change-of-control provisions** — Identify whether contracts require counterparty consent to assignment or trigger on change of control. Flag all consent requirements and anti-assignment clauses. Assess whether obtaining consents is feasible within the transaction timeline. Change-of-control clauses are among the most frequent M&A deal-breakers.

5. **Assess termination and exit rights** — Review termination for convenience rights, termination for cause triggers, notice periods, cure periods, and consequences of termination (wind-down obligations, data return, IP reversion). Identify contracts where the counterparty could exit on short notice and assess the operational impact.

6. **Identify liability and indemnification exposure** — Extract liability caps, exclusions of consequential damages, mutual vs. unilateral indemnities, IP indemnification obligations, and environmental or data breach indemnities. Quantify the maximum exposure in each agreement and aggregate across the portfolio.

7. **Review IP ownership and licensing provisions** — Confirm that all IP used in the business is either owned outright or properly licensed. Identify work-for-hire provisions, open-source license obligations, restrictions on sublicensing, and any IP that reverts on contract termination. IP gaps discovered post-close can be uncurable.

8. **Assess regulatory compliance and consent requirements** — Review regulatory approvals embedded in contracts, data processing agreements (GDPR Article 28 / CCPA), export control obligations, and sector-specific regulatory compliance provisions. Flag any regulatory consents that must transfer or be re-obtained.

9. **Summarize findings by risk tier** — Classify each finding as: Red (material risk requiring remediation or renegotiation before close), Amber (moderate risk requiring disclosure or monitoring), Green (administrative/informational). Prepare a risk summary memo with findings, deal impact, and recommended actions for each red and amber issue.

10. **Track consents and remediation through close** — Maintain a live remediation tracker logging each required consent, responsible party, deadline, and status. Update daily during the final pre-close period. Ensure all red items are resolved or accepted by the deal team in writing before signing.

## Rules

- Never begin substantive review without a complete contract inventory — gaps discovered after close create liability
- All material contracts must be reviewed by a qualified lawyer; paralegal or AI-assisted review of material contracts must be attorney-supervised
- Change-of-control and assignment provisions must be reviewed in every material contract without exception
- Every red finding must have a documented resolution or a written acceptance of residual risk from the authorized decision-maker
- Do not rely solely on counterparty representations about contract terms — primary source review of the actual documents is required

## Common Mistakes

- **Skipping below-threshold contracts as a category** — Low-value contracts can contain high-impact provisions (IP assignment, perpetual exclusivity); always review a sample of below-threshold contracts and all IP-related agreements regardless of value.
- **Missing evergreen renewal clauses** — Contracts that auto-renew without notice create unexpected long-term obligations; flag all renewal provisions and calculate the maximum extension exposure.
- **Treating consent as automatic** — Assuming counterparties will grant change-of-control consents quickly leads to closing delays; initiate consent requests as early as legally permissible.
- **Aggregating liability caps incorrectly** — Reporting each contract's cap in isolation without summing total portfolio exposure understates risk; aggregate all indemnities and caps into a total exposure figure.
- **No post-close integration of findings** — Handing over a due diligence report without ensuring findings are incorporated into the integration plan means identified risks are never mitigated.

## Examples

**SaaS acquisition:** A $200M SaaS acquisition due diligence team reviews 340 customer contracts, identifying 12 contracts with anti-assignment clauses and 3 with MFN pricing that would reset post-acquisition. The team initiates consent requests 30 days before close and renegotiates 2 MFN provisions, avoiding $8M in post-close price reductions.

**Vendor onboarding:** A financial services firm reviews a new cloud provider's contract, identifying unlimited data processing rights granted to the vendor. The finding triggers renegotiation of data processing terms and addition of GDPR Article 28 compliant DPA provisions before onboarding proceeds.

## When NOT to Use

- When reviewing a single, straightforward commercial agreement in isolation — a focused single-contract review using a standard checklist is more efficient than full due diligence methodology
- When the contract portfolio is fewer than 10 agreements of similar type — a simplified checklist approach without the full tiering and tracking infrastructure is proportionate
