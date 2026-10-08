---
name: kb-fintech-licensing-cma-ksa-sboghossian
title: Knowledge Pack — KSA Fintech Licensing (CMA + SAMA)
description: Use when a matter involves financial services licensing, fintech regulation, payment services, open banking, equity crowdfunding, robo-advisory, or establishing a regulated financial entity in Saudi Arabia. Covers the dual-regulator framework (SAMA for banking/payments, CMA for capital markets/investment), SAMA Fintech Sandbox, capital requirements, Sharia-compliance expectations, Saudization obligations for fintech entities, and Vision 2030 alignment. Triggers on KSA fintech license, SAMA payment license, CMA equity crowdfunding, BNPL KSA, open banking Saudi, or Saudi fintech questions.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/kb/kb-fintech-licensing-cma-ksa
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: sa
practice: finance
language: en
---

# Knowledge Pack — KSA Fintech Licensing (CMA + SAMA)

## Regulatory Architecture

Saudi Arabia's fintech sector is regulated by multiple authorities with distinct mandates:

| Regulator | Full Name | Primary Domain |
|---|---|---|
| **SAMA** | Saudi Central Bank (مصرف الإسلامي) | Banking; payment services; money exchange; e-money; BNPL |
| **CMA** | Capital Market Authority | Securities; equity crowdfunding; robo-advisory; investment management; crypto-securities |
| **ZATCA** | Zakat, Tax, and Customs Authority | Tax compliance; e-invoicing (FATOORAH) |
| **MOC** | Ministry of Commerce | Consumer protection; e-commerce licensing |
| **CITC** | Communications and Information Technology Commission | Telecom + digital infrastructure; data flows |
| **MISA** | Ministry of Investment | Foreign entity establishment; investment license |

Most fintech companies require SAMA **and/or** CMA licenses depending on their specific activities, plus MISA establishment approval for foreign investors.

---

## SAMA-Regulated Activities and License Types

### Payment Services

| License Type | Scope | Min Capital |
|---|---|---|
| Tier 1 Payment Service Provider | Domestic payment initiation only; low-risk services | SAR 5,000,000 |
| Tier 2 Payment Service Provider | Full payment services including e-wallets, POS acquiring | SAR 10,000,000 |
| Tier 3 Payment Service Provider | Cross-border payments + full acquiring + issuing | SAR 50,000,000 |

### E-Money Institutions

- License to issue e-money (stored value in electronic accounts).
- Capital: SAR 5,000,000 – 10,000,000 depending on scale.
- User fund safeguarding: funds held in segregated trust accounts at SAMA-approved bank.
- Consumer limits on balances and transactions.

### Money Exchange and Remittance

- Exchange house license (maktab sarafa).
- Capital: SAR 10,000,000+ (depends on scope).
- Requires SAMA approval; brick-and-mortar or digital.

### Buy-Now-Pay-Later (BNPL)

- SAMA-supervised; treated as a form of consumer credit.
- Providers need SAMA approval; consumer-protection rules apply.
- Sharia compliance expected: murabaha-structured BNPL widely used.
- Disclosure obligations to consumers.

### Digital Banking

- Full digital bank license (no branches): SAR 500,000,000 minimum capital.
- Two digital banks licensed as of 2024 (STC Bank, Saudi Digital Bank).

---

## CMA-Regulated Activities and License Types

### Equity Crowdfunding

- Platform license for investment-based crowdfunding.
- CMA Equity Crowdfunding Regulations (2021+).
- Capital: SAR 5,000,000 minimum.
- Maximum raise per issuer: SAR 15,000,000 (per campaign per platform).
- Investor limits: professional investors have higher thresholds; retail investors capped per investment.
- Issuer eligibility: Saudi-incorporated companies (mostly SMEs).

### Robo-Advisory (Automated Investment Advice)

- Registered Investment Adviser (RIA) license from CMA with digital/automated activity endorsement.
- Capital: SAR 5,000,000+.
- Algorithm disclosure and governance requirements.
- Sharia-compliant portfolios common; halal screening required for many retail products.

### Investment Management

- Full Investment Manager license.
- Capital: SAR 10,000,000+.
- Portfolio management for retail and institutional clients.

### Securities Broker / Dealer

- CMA broker-dealer license.
- Capital: SAR 25,000,000+.
- Custody, execution, prime brokerage.

### Crypto-Securities (Limited)

- CMA has not issued a comprehensive crypto-asset framework as of 2025.
- Securities tokens (STOs) may fall under CMA jurisdiction if meeting securities definition.
- Utility tokens and payment tokens: SAMA jurisdiction; limited licensing available.
- Crypto is generally restricted for retail consumers; institutional participation via specific licenses only.

---

## Open Banking

KSA's **Open Banking Framework** is jointly governed by **SAMA + CMA + ZATCA**:

- **Phase 1** (read-only): account information services — financial aggregators can access consumer bank data with consent.
- **Phase 2** (read-write): payment initiation services; third-party providers can initiate payments from customer accounts.
- **API standards**: Saudi Open Banking Framework (SOBF) — SAMA-published technical standards.
- **Provider licensing**: Open Banking Service Providers (OBSPs) require SAMA registration.
- **Consumer consent**: explicit user consent required per PDPL (see [[kb-data-privacy-ksa-pdpl]]).

---

## SAMA Fintech Sandbox

SAMA's **Fintech Saudi Sandbox** allows companies to test products before full licensing:

| Feature | Detail |
|---|---|
| Duration | 12–24 months |
| Activities | Any SAMA-regulated fintech activity |
| Customer limits | Restricted number and transaction volumes |
| Capital relief | Reduced capital requirements during testing |
| Sandbox graduation | Must apply for full SAMA license within or at end of sandbox period |
| Application process | Submit application via SAMA portal; business plan required |

SAMA has funded and supported numerous cohorts; sandbox is actively used by startups and established fintech players.

---

## Vision 2030 Alignment

Fintech is a **priority sector** under Vision 2030's Financial Sector Development Program (FSDP):

- Target: reduce cash transactions to 70% non-cash by 2030 (from ~18% in 2016 — nearly achieved by 2024).
- **Fintech Saudi** initiative: national fintech hub; events, ecosystem support, SAMA-CMA coordination.
- Regulatory fast-track for qualifying fintech companies.
- Saudi Central Bank innovation offices (dedicated fintech engagement teams).

---

## Sharia Compliance Expectations

Most consumer-facing fintech products in KSA must be Sharia-compliant:

| Product Type | Sharia Structure |
|---|---|
| Personal loans | Murabaha or Tawarruq (commodity Murabaha) |
| BNPL | Murabaha (bank buys goods; sells at markup on deferred payment) |
| Investment products | Mudaraba or Musharaka (profit-sharing); no guaranteed interest |
| Insurance (takaful) | Wakala or Mudaraba takaful model |
| Home finance | Diminishing Musharaka (bank gradually transfers ownership share) |

- Products require a **Sharia Supervisory Board (SSB)** fatwa (opinion) for certification.
- AAOIFI standards widely referenced (see [[kb-shariah-finance-aaoifi]]).
- Non-Sharia products may be permitted for non-Muslim expatriates in some cases; market practice favors Sharia-compliant default.

---

## Foreign Ownership

- 100% foreign ownership permitted in most fintech activities through **MISA license**.
- MISA establishes the Saudi legal entity (Limited Liability Company or Branch).
- **Regional Headquarters (RHQ) Program**: companies with MENA-wide operations may establish KSA as their RHQ — preferential treatment for government contracts.
- Minimum investment thresholds apply for certain license categories.

---

## Saudization (Nitaqat) for Fintech

- Fintech companies must meet Saudi national hire quotas per Nitaqat system.
- Financial services sector has specific Saudization targets.
- Higher Saudization = "Green" or "Platinum" tier = preferred treatment on government services, visa quotas.
- Technology and engineering roles: a grace period or exemption may apply in early stages for genuinely specialized international talent; consult current HRSD guidance.

---

## Practical Licensing Timeline

| Stage | Timeline |
|---|---|
| MISA entity establishment | 2–4 weeks |
| SAMA pre-application engagement | 4–8 weeks |
| Sandbox application and approval | 3–6 months |
| Sandbox testing | 12–24 months |
| Full SAMA/CMA license application | 3–6 months after sandbox graduation |
| Estimated total to full license | 18–36 months (sandbox route) |
| Direct licensing (for established entities) | 12–18 months |

---

## Practical Considerations

- SAMA approval timelines for full licensing: **12–18 months** typical.
- Specialized fintech lawyer essential — regulatory complexity is high and evolving.
- Both SAMA and CMA require ongoing compliance reporting post-license.
- Data localization: financial data must remain in Saudi Arabia per SAMA cybersecurity and cloud-computing rules.
- KSA entity required (foreign branch or subsidiary); MISA license pre-condition.

## Caveats & Currency

KSA's fintech regulatory landscape is actively evolving. SAMA and CMA publish updated regulations, circulars, and guidance frequently. Saudization targets, capital requirements, and sandbox cohort details change. The crypto framework is incomplete as of 2025; any crypto-related KSA matter requires up-to-date regulatory check. Verify current SAMA Open Banking phase status and technical specifications.

## Related Skills

- [[kb-fintech-licensing-difc]]
- [[kb-fintech-licensing-adgm]]
- [[kb-shariah-finance-aaoifi]]
- [[kb-employment-law-ksa]]
- [[kb-data-privacy-ksa-pdpl]]
