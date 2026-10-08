---
name: kb-tax-ksa-sboghossian
title: Knowledge Pack — KSA Tax Law
description: Use when a user asks about Saudi Arabian tax law, zakat obligations, VAT, withholding tax, real estate transactions tax, or ZATCA compliance for any entity structure operating in or paying into the Kingdom. Covers corporate income tax, excise, transfer pricing, permanent establishment, tax treaties, and Vision 2030 incentive zones. Triggers on any KSA-jurisdiction tax or zakat question.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/kb/kb-tax-ksa
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: sa
practice: tax
language: en
---

# Knowledge Pack — KSA Tax Law

## Scope

This pack covers the Saudi Arabian tax framework as administered by the Zakat, Tax and Customs Authority (ZATCA). It is a practitioner-facing reference for lawyers, in-house counsel, and finance professionals advising entities with Saudi nexus. Verify currency before relying on specific rates or thresholds — KSA tax law has moved quickly since 2016 and continues to evolve under Vision 2030.

---

## Governing Authority

**ZATCA** (Zakat, Tax and Customs Authority) consolidated the General Authority of Zakat and Tax (GAZT) and the General Customs Authority effective 2021. ZATCA issues implementing regulations, rulings, and binding assessments for all taxes below.

---

## Zakat

| Attribute | Detail |
|-----------|--------|
| Rate | 2.5% of the zakat base |
| Taxpayers | Saudi nationals and legal entities that are Saudi or GCC-owned (their share of the entity) |
| Base | Broadly net assets adjusted per ZATCA zakat bylaws; not net income |
| Filing | Annual; due within 120 days of fiscal year-end |
| Nature | Religious levy with civic-obligation status; not a "tax" in the conventional commercial sense |
| Dual obligation | A mixed Saudi/foreign-owned entity pays both zakat (on Saudi/GCC share) and corporate income tax (on foreign share) |

**Key trap:** Foreign shareholders sometimes incorrectly assume zakat is included in the 20% CIT. It is not. Saudi and GCC-owned portions of a JV remain subject to zakat even where the overall entity also pays CIT on the foreign portion.

---

## Corporate Income Tax (CIT)

| Parameter | Detail |
|-----------|--------|
| Rate | 20% on the net adjusted profit attributable to non-Saudi/non-GCC shareholders |
| Scope | Foreign investor's share of Saudi-resident entities (LLCs, JSCs, partnerships) |
| Oil & hydrocarbons | Special ring-fenced regime: 50%–85% (rate varies by field/royalty structure); negotiated with Ministry of Energy for upstream activities |
| Filing | Annual return; due 120 days after fiscal year-end |
| Advance payments | Required for entities with prior-year liability > SAR 500,000 |
| Consolidated filing | Not currently available in KSA (each legal entity files separately) |

**Practical note:** "Net adjusted profit" follows KSA-specific adjustments — depreciation schedules, deductibility of zakat, interest deductibility limitations (thin-cap rules). OECD BEPS alignment is partial; verify current ZATCA Bylaws for disallowances.

---

## Value Added Tax (VAT)

| Parameter | Detail |
|-----------|--------|
| Standard rate | 15% (increased from 5% in July 2020 by Royal Decree) |
| Legal basis | KSA VAT Law (2017 Royal Decree) and Executive Regulations |
| Registration threshold | Mandatory: SAR 375,000 annual taxable supplies; Voluntary: SAR 187,500 |
| Filing | Monthly or quarterly based on turnover; electronic via ZATCA portal |
| Zero-rated | Exports of goods/services, international transport, gold/silver bullion, certain financial services (when qualifying), first residential sale by developer |
| Exempt | Residential rentals (ongoing), certain health/education services, certain local financial transactions |

**GCC Unified VAT Framework:** KSA VAT implements the GCC VAT Framework Agreement. Cross-border transactions within the GCC may have special treatment; verify each GCC member's domestic position.

---

## Real Estate Transactions Tax (RETT)

| Parameter | Detail |
|-----------|--------|
| Rate | 5% of the total transaction value |
| Legal basis | Royal Decree M/84 (2020); replaces VAT on real estate transfers |
| Taxpayer | Seller is primarily liable; buyer jointly liable |
| Scope | All disposals of real property and in-kind contributions of real estate |
| Key exemptions | First-time Saudi homebuyer (residential, primary residence); inheritance transfers; certain reorganizations |
| Registration | RETT is filed and paid through ZATCA within 30 days of transaction |

**Planning trap:** RETT and VAT are mutually exclusive on residential property. However, commercial real estate that is not a "first supply" falls under RETT at 5% rather than VAT at 15%. Confirm classification before structuring.

---

## Withholding Tax (WHT)

WHT applies to payments made by Saudi-resident entities to non-residents. Rates below are domestic; treaty rates may reduce them.

| Payment type | Domestic WHT rate |
|--------------|------------------|
| Services (technical, managerial, consulting) | 5% |
| Royalties (IP, patents, licenses) | 15% |
| Rent (movable assets and certain real property) | 5% |
| Dividends to foreign shareholders | 5% |
| Branch remittance profit tax | 5% |
| Insurance / reinsurance premiums | 5% |
| Air and sea freight (international) | 5% |
| International telecommunications | 5% |

**Filing:** WHT returns filed and paid within 10 days following the month of payment. Late payment attracts a 1% monthly penalty.

---

## Personal Income Tax

- **None.** Saudi Arabia imposes no personal income tax on individuals.
- No capital gains tax on personal investments (securities, real estate held personally).
- Expatriate employees are not subject to KSA personal income tax; their income from Saudi sources is not taxed at source (other than social insurance / GOSI contributions).

---

## Excise Tax

| Product | Rate |
|---------|------|
| Tobacco products (cigarettes, cigars, hookah) | 100% |
| Energy drinks | 100% |
| Sweetened beverages (added sugar) | 50% |
| Electronic smoking devices / e-cigarettes | 100% |

Excise is levied on the first supply in KSA (import or local manufacture). Registration required if handling excisable goods.

---

## Transfer Pricing

- **Legal basis:** ZATCA Transfer Pricing Bylaws (effective January 2019), OECD-aligned.
- **Arm's length standard** applies to all controlled transactions between related parties.
- **Documentation thresholds:**
  - Master File: required for groups with consolidated KSA turnover > SAR 6 million
  - Local File: same threshold; must be prepared annually
  - CbCR (Country-by-Country Reporting): for MNE groups with consolidated revenue ≥ SAR 3.2 billion (approx. €750 million), filed by the KSA ultimate parent or surrogate entity
- **Penalty for non-disclosure:** Up to 4% of the controlled transaction value for failure to prepare TP documentation

---

## Permanent Establishment (PE)

- Determined under domestic law and applicable Double Tax Treaty (DTT).
- **Service PE** is a common trap: providing services in KSA for more than **183 days** (cumulative over 12 months) can trigger PE, subjecting the foreign entity to CIT on KSA-sourced income.
- **Construction PE:** Typically 6–12 months threshold under DTTs.
- **Agency PE:** A dependent agent habitually concluding contracts in KSA creates PE.

---

## Investment Incentives & Special Economic Zones

Under Vision 2030, KSA has created several investment zones with favourable tax treatment:

| Scheme | Key benefit |
|--------|-------------|
| Special Economic Zones (SEZs) | Up to 30-year CIT holiday; customs suspension; expedited licensing |
| Regional Headquarters (RHQ) incentive | 0% CIT for 30 years for qualifying MNE regional HQ relocated to KSA |
| NEOM | Bespoke regulatory and tax framework (in development) |
| Export and logistics zones | Customs and VAT deferral mechanisms |

**Sharia-compliant financing:** Profit payments under murabaha, ijara, and sukuk structures are generally deductible as the equivalent of interest; specific rules apply — confirm with ZATCA ruling for novel structures.

---

## Double Tax Treaties (DTTs)

KSA has over 50 DTTs in force, including treaties with the UK, France, India, China, and most GCC member states. Key effects:

- Reduced WHT rates on dividends, interest, royalties, and services
- PE thresholds and carve-outs
- Competent authority procedures for dispute resolution

**Verify treaty status** before structuring cross-border payments; some treaties have MFN clauses or are under renegotiation. The MLI (Multilateral Instrument) has been ratified by KSA — check which treaties are covered.

---

## How to Use This Pack

Load this pack when the user's query involves:
- Any KSA tax compliance or structuring question
- ZATCA filings, assessments, or penalties
- Cross-border payments into or out of KSA
- M&A or JV structuring with Saudi nexus
- Investment zone eligibility for Vision 2030 projects

Pair with [[kb-corporate-ksa]] for entity structure context and [[kb-tax-uae]] for comparative GCC analysis.

---

## Caveats & Currency

KSA tax law is actively evolving. The RETT, excise expansion, CIT rate for hydrocarbons, and SEZ frameworks have all changed since 2016. ZATCA publishes circulars and FAQs that supplement statutory rules. Always verify:
1. Current ZATCA Bylaws and Executive Regulations
2. Applicable DTT in force (check ZATCA treaty portal)
3. Any VAT rulings specific to the sector or transaction type

This pack does not constitute tax advice. Engage a KSA-licensed tax adviser for specific compliance positions.

---

## Related skills

- [[kb-tax-uae]]
- [[kb-tax-lb]]
- [[kb-corporate-ksa]]
- [[review-employment-contract-ksa]]
- [[draft-service-agreement-ksa]]
