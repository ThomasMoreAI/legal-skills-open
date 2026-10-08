---
name: heuristic-shariah-compliance-check-when-relevant-sboghossian
title: Sharia Compliance Check When Relevant
description: Use when a matter involves Saudi onshore parties, Islamic finance structures, personal status of Muslim parties in MENA, KSA real estate, or any instrument that may be subject to Sharia-compliance review in a GCC jurisdiction. Identifies the key Sharia-law concerns (riba, gharar, maisir, penalty clauses, inheritance fixed shares, takaful) and surfaces them proactively before drafting or advising. Also covers the UAE Federal Law 41/2022 civil option for non-Muslims and Lebanon's confession-based personal-status system.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/heuristic/heuristic-shariah-compliance-check-when-relevant
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: finance
language: en
---

# Sharia Compliance Check When Relevant

## When this applies

This heuristic fires when the matter has any of the following characteristics:

- The governing law is KSA law (Sharia is a source of KSA law).
- The parties include Saudi onshore entities or individuals.
- The transaction is structured as Islamic finance (murabaha, ijara, mudaraba, sukuk, musharaka).
- The matter involves personal status (marriage, divorce, inheritance, guardianship) of a Muslim individual in a MENA jurisdiction.
- The contract is for KSA real estate or Saudi-registered assets.
- The matter involves enforcement against Saudi-resident parties or assets (where Saudi public-policy review applies to the judgment or award).

## Key Sharia-law concerns to surface

### 1. Riba (interest / usury)

Riba — the payment or receipt of interest — is prohibited under Sharia and applies to virtually all KSA financing transactions governed by KSA law. In UAE onshore banking, conventional interest is permitted for commercial banking (under UAE federal banking law) but is subject to Islamic banking supervisory frameworks for Islamic banks and Islamic windows.

**When relevant**: any loan, credit facility, or financing instrument involving KSA parties or KSA governing law.

**Restructuring options**:
- **Murabaha**: cost-plus-profit sale; used as a substitute for conventional loans.
- **Ijara**: lease financing; the funder buys the asset and leases it to the customer at a profit rental.
- **Mudaraba**: profit-sharing; funder provides capital, customer provides labor/expertise.
- **Musharaka**: equity partnership; parties share profits and losses.

**Advisory note**: AAOIFI (Accounting and Auditing Organization for Islamic Financial Institutions) standards govern Islamic finance products in many GCC markets. See [[kb-shariah-finance-aaoifi]].

### 2. Gharar and maisir (speculation and gambling)

*Gharar* (excessive uncertainty) and *maisir* (gambling) render contracts unenforceable under Sharia. This affects:
- Derivatives and contingent instruments: forward contracts, options, and swaps are challenged under Sharia unless structured through accepted Islamic equivalents (wa'd, arbun).
- Insurance: conventional insurance involves elements of gharar. *Takaful* (mutual insurance) is the Sharia-compliant alternative.
- Speculative joint ventures: ventures where the outcome is entirely uncertain may be challenged.

### 3. Penalty clauses

Saudi courts apply judicial discretion on penalty clauses (liquidated damages) — they may reduce or void a penalty if it is disproportionate to actual damage, as Sharia disfavors penalties without demonstrated loss. This is a significant difference from DIFC/ADGM/English law, where liquidated damages clauses that represent a genuine pre-estimate of loss are fully enforced.

**When drafting for KSA**: use a penalty clause but also document the rationale for the amount (genuine pre-estimate of loss). Alternatively, use a performance bond structure, which is more reliably enforced in KSA courts.

### 4. Inheritance fixed shares

Under Sharia inheritance rules, the shares of heirs are fixed by religious law and cannot be freely altered by will:
- Daughters receive half the share of sons (*asabat* rules).
- Non-Muslim relatives do not inherit.
- A bequest (*wasiyyah*) is limited to one-third of the estate for non-heirs.

**When relevant**: wills, estate planning, and succession planning for Muslim individuals in KSA, UAE (where Islamic inheritance applies to Muslim nationals and residents unless they opt into the civil-law registry), and other GCC jurisdictions.

**Advisory note**: for UAE, Federal Decree-Law No. 41 of 2022 provides a civil-law personal status option for non-Muslims in the UAE. See below.

### 5. Insurance — takaful preference

Conventional insurance products (term life, P&C) may be challenged under Sharia on gharar grounds. In KSA, SAMA-regulated takaful companies provide the compliant alternative. In UAE, both conventional and takaful products are available.

When advising KSA clients on insurance requirements (e.g., employer liability, professional indemnity, construction all-risk): flag the takaful preference and confirm the insurer is SAMA-supervised.

### 6. Cross-border enforcement and KSA public-policy review

Even where a transaction is governed by a non-Sharia law (e.g., English law) and adjudicated in a non-KSA forum (e.g., ICC Paris), enforcement of the resulting award or judgment against Saudi-resident parties or Saudi-located assets may trigger KSA public-policy review. A KSA enforcement court may refuse enforcement of an award that contains interest, penalty provisions, or other provisions that conflict with Sharia.

**Advisory**: when advising on enforcement strategy involving KSA assets or parties, consider whether the award structure is enforceable in KSA courts. This is a deal-structuring issue, not just a dispute-resolution issue.

## Non-Muslim parties in MENA

### UAE — Federal Decree-Law No. 41 of 2022

UAE Federal Decree-Law No. 41 of 2022 provides a civil-law personal status framework for non-Muslims residing in the UAE. Non-Muslim expatriates may opt into this regime for marriage, divorce, and inheritance, which applies civil-law principles rather than the default UAE Personal Status Law (which is based on Sharia for Muslims and applies by default to non-Muslims in the absence of an opt-in).

**When relevant**: wills and estate planning for non-Muslim expatriates in UAE. Louis's [[draft-will]] skill should surface this option.

### Lebanon

Lebanon's personal-status system is confession-based — each recognized religious community (Maronite, Greek Orthodox, Sunni, Shia, Druze, etc.) has its own personal-status courts and rules. There is no civil marriage in Lebanon (civil marriages contracted abroad are recognized). For Muslim individuals, inheritance follows Sharia; for Christian individuals, applicable rules depend on the confession.

**When relevant**: Lebanese succession planning, marriage, divorce, and custody matters require identification of the applicable confession and its specific court and rules.

### Other GCC

Qatar, Bahrain, Kuwait, and Oman apply Sharia to personal-status matters for Muslim parties and have specific provisions for non-Muslim expatriates. The details vary; verify with local counsel.

## Drafting note

When Sharia compliance is relevant, flag it explicitly in the advice or document preamble:

> *"Note: this transaction involves KSA-governed obligations. The following provisions have been reviewed for Sharia compliance / have been structured to address Sharia requirements. You should obtain a Sharia-compliance opinion from a recognized Sharia board if required by your institution or counterparty."*

Do not assert Sharia compliance without a qualified Sharia board opinion — Louis can flag the issues and structure the analysis, but formal Sharia-compliance certification requires a qualified scholar.

## Related skills

- [[kb-shariah-finance-aaoifi]]
- [[draft-will]]
- [[heuristic-always-state-jurisdiction-first]]
- [[heuristic-governing-law-must-match-forum]]
- [[heuristic-no-us-style-boilerplate-in-civil-law-jx]]
