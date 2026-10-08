---
name: kb-tax-uae-sboghossian
title: Knowledge Pack — UAE Tax Law
description: Use when a user asks about UAE federal corporate tax, VAT, excise, withholding obligations, free zone tax treatment, DIFC or ADGM tax positions, transfer pricing, or Pillar Two compliance for entities with UAE nexus. Covers Federal Decree-Law 47/2022 (Corporate Tax), Decree-Law 8/2017 (VAT), and the Qualifying Free Zone Person regime. Triggers on any UAE tax structuring, compliance, or due-diligence question.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/kb/kb-tax-uae
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ae
practice: tax
language: en
---

# Knowledge Pack — UAE Tax Law

## Scope

This pack covers the UAE federal tax framework as of 2026. The UAE introduced federal corporate income tax in 2023 (a historic shift), operates VAT at 5% since 2018, and in 2025 began applying a Domestic Minimum Top-Up Tax (DMTT) for large multinationals under the OECD Pillar Two framework. Despite these additions, the UAE remains a low-tax jurisdiction. Verify current FTA (Federal Tax Authority) guidance before advising on any specific position.

---

## Governing Authority

**Federal Tax Authority (FTA)** — administers Corporate Tax, VAT, and Excise Tax. Issues decisions, public clarifications, and binding private rulings (advance pricing arrangements available for CT).

---

## Corporate Tax (CT)

| Parameter | Detail |
|-----------|--------|
| Legal basis | Federal Decree-Law 47/2022 (CT Law), effective for tax periods starting on or after 1 June 2023 |
| Standard rate | 9% on taxable income above AED 375,000 |
| Small business relief | 0% effective rate for businesses with revenue ≤ AED 3 million (Small Business Relief; election available until 31 December 2026 per Ministerial Decision 73/2023) |
| Zero bracket | First AED 375,000 of taxable income: 0% |
| Multinational top-up (DMTT) | 15% for UAE-resident entities of MNE groups with consolidated global revenue ≥ €750 million; effective for periods starting on or after 1 January 2025 |

### Taxable persons

- UAE-resident juridical persons (mainland and free zone companies, branches of foreign companies)
- Non-resident juridical persons with UAE permanent establishment or UAE-source income
- Natural persons carrying on business in the UAE (if annual business income > AED 1 million)

### Exempt persons

- UAE federal and emirate governments and their wholly owned entities
- Qualifying Public Benefit Entities
- Qualifying Investment Funds (QIF) — subject to conditions
- Pension and social security funds

---

## Qualifying Free Zone Persons (QFZP)

Free zones retain 0% tax on qualifying income subject to strict conditions:

| Condition | Requirement |
|-----------|-------------|
| Qualifying income | Must derive from activities listed in Ministerial Decision 265/2023 (financial services, shipping, logistics, holding, manufacturing, etc.) |
| Adequate substance | Must have sufficient substance in the free zone (employees, assets, operations) |
| Related-party transactions | Domestic-mainland related-party income may be non-qualifying |
| Transfer pricing | All related-party transactions subject to arm's-length rules |
| Excluded income | Certain income (e.g., from mainland UAE real estate) is automatically non-qualifying |

**Key trap:** Free zone companies transacting with mainland-UAE related parties risk tainting their QFZP status. Even a small volume of non-qualifying income can subject the entire entity to 9% on all income in some interpretations — seek specific FTA guidance.

---

## Value Added Tax (VAT)

| Parameter | Detail |
|-----------|--------|
| Legal basis | Federal Decree-Law 8/2017 and Executive Regulation (as amended) |
| Standard rate | 5% |
| Mandatory registration | Annual taxable supplies or imports ≥ AED 375,000 |
| Voluntary registration | ≥ AED 187,500 |
| Filing | Quarterly (default); monthly for large taxpayers |
| Zero-rated supplies | Exports of goods and services, international passenger/freight transport, certain healthcare, certain education, first supply of residential real estate, precious metals for investment |
| Exempt supplies | Bare land, subsequent supplies of residential real estate, local passenger transport, certain financial services |

**Designated zones (free zones for VAT):** Goods moving between designated zones are outside UAE for VAT purposes (not an import/export). A common planning tool for goods businesses but requires compliance with FTA designated-zone rules.

---

## Excise Tax

| Product | Rate |
|---------|------|
| Tobacco products (cigarettes, cigars) | 100% |
| Electronic smoking devices and tools | 100% |
| Energy drinks | 100% |
| Sweetened beverages (carbonated) | 50% |
| Carbonated water / drinks | 50% |

Excise is levied on the first supply in the UAE (import or local production). Registration and monthly filing required for excisable goods.

---

## Personal Income Tax

- **None.** The UAE imposes no individual income tax.
- No capital gains tax on personal investments in securities, real estate, or business interests held personally.
- Real estate gains inside a company (CT-registered) may constitute taxable corporate income.

---

## Withholding Tax

The UAE imposes no withholding tax on outbound payments under the CT Law as enacted. This favourable position applies to:
- Dividends to foreign shareholders
- Interest payments to foreign lenders
- Royalties to foreign IP owners
- Service fees to non-resident service providers

**DTT interaction:** Even without domestic WHT, the UAE's extensive treaty network (80+ treaties) may benefit recipients in treaty-partner jurisdictions in terms of the other state's domestic tax treatment of UAE-source income.

---

## Transfer Pricing

- Arm's-length principle applies to all transactions between "Related Parties" (defined broadly under the CT Law to include 50%+ common ownership and other control tests)
- Documentation aligned with OECD Transfer Pricing Guidelines:
  - **Master File** and **Local File** for taxpayers above AED 200 million in revenue (or as specified by Ministerial Decision)
  - **Disclosure Form** for related-party transactions — filed with CT return for all taxpayers with related-party transactions
  - **Country-by-Country Report (CbCR):** for UAE Ultimate Parent entities of groups with consolidated revenue ≥ AED 3.15 billion; filed within 12 months of fiscal year-end
- Connected-person transactions (individuals and their related entities) also subject to arm's-length requirement

---

## DIFC and ADGM

Both the Dubai International Financial Centre (DIFC) and Abu Dhabi Global Market (ADGM) are now subject to UAE federal corporate tax. Previously they operated under a 50-year tax-holiday guarantee from their founding legislation. The CT Law supersedes those guarantees for income tax purposes.

**Residual DIFC/ADGM advantages:**
- Common law courts and English-language legislation (not a tax advantage, but critical for deal structuring)
- Specific fund, investment manager, and family office exemptions may still reduce effective CT rate
- ADGM and DIFC retain their own company law, which does not affect federal CT applicability

---

## Family Offices and Investment Funds

- **Qualifying Investment Fund (QIF):** Exempt from CT if it meets ownership diversification, regulatory registration, and arm's-length management requirements. Fund investors taxed on their share of fund income when distributed, not at fund level.
- **Family Foundations:** Ministerial guidance allows certain family foundations to elect transparent treatment (income taxed in hands of founders/beneficiaries rather than foundation itself).
- **Single Family Offices:** Specific guidance available; structure-dependent.

---

## Anti-Avoidance

| Mechanism | Description |
|-----------|-------------|
| General Anti-Abuse Rule (GAAR) | FTA may disregard or recharacterise arrangements whose primary purpose is obtaining a CT advantage not intended by the CT Law |
| Specific anti-avoidance rules | Target dividend-stripping, hybrid mismatch arrangements, and certain related-party payment structures |
| Interest limitation rule | Net interest expenditure deduction capped at 30% of EBITDA (with a de minimis threshold of AED 12 million) |
| CFC rules | Controlled Foreign Company provisions apply to UAE-resident persons holding interests in foreign entities |

---

## Permanent Establishment (PE)

- The CT Law adopts a PE concept for non-resident persons deriving UAE-source income.
- Fixed-place PE: a fixed place of business in the UAE (office, factory, warehouse).
- Deemed PE: an agent habitually concluding contracts on behalf of the non-resident, or activities in the UAE exceeding time thresholds specified in applicable DTTs.
- **Key planning point:** Non-residents relying on UAE agents (sales agents, distributors) must assess PE risk carefully; the CT Law's deemed PE provision is broader than the pre-2023 position.

---

## How to Use This Pack

Load when the user's query involves:
- UAE CT registration, filing, or rate application
- Free zone QFZP status eligibility or taint risk
- VAT registration, return preparation, or input tax recovery
- Transfer pricing documentation requirements
- Pillar Two / DMTT applicability for large MNE groups
- DIFC/ADGM entity tax treatment
- Investment fund or family office structuring in the UAE

Pair with [[kb-corporate-uae]] for entity-type selection, [[kb-difc-company-law]] for DIFC-specific entity law, and [[kb-tax-ksa]] for comparative GCC analysis.

---

## Caveats & Currency

UAE tax law post-2023 is evolving rapidly. The FTA issues Cabinet Decisions, Ministerial Decisions, and Public Clarifications that supplement and sometimes amend the Decree-Law on short notice. Key areas of current flux:
- QFZP qualifying activities list (Ministerial Decision 265/2023 — subject to revision)
- DMTT implementing regulations (2025)
- Interest limitation safe harbours
- Specific guidance on family foundations and QIFs

Always verify the current FTA website and seek a private ruling for novel or high-value positions. This pack does not constitute tax advice.

---

## Related skills

- [[kb-tax-ksa]]
- [[kb-tax-lb]]
- [[kb-corporate-uae]]
- [[kb-difc-company-law]]
- [[review-contract-uae]]
