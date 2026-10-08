---
name: research-tax-treatment-lookup-sboghossian
title: Tax Treatment Lookup
description: 'Use when a lawyer, tax adviser, or CFO needs a structured overview of how a specific transaction or entity is treated for tax purposes across relevant jurisdictions — covering corporate income tax rates, VAT/GST, withholding taxes on cross-border payments, treaty relief, transfer pricing, and special regimes. MENA-first: covers KSA (ZATCA), UAE (FTA — 9% CIT since June 2023, free-zone QFZP rules, 5% VAT), Egypt, Lebanon, and GCC generally, with secondary UK, France, and US coverage. Always disclaims: not tax advice — confirm with licensed tax adviser.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/research/research-tax-treatment-lookup
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: tax
language: en
---

# Tax Treatment Lookup

Structured tax analysis for a specific transaction or entity type across one or more jurisdictions. Covers the headline tax exposures (CIT, VAT, withholding, stamp duty) plus treaty relief, transfer pricing, and watch-out items for MENA-specific structures. Not a tax return or filing service; outputs are a starting framework for a licensed tax adviser to build on.

## When to use this

- Structuring a cross-border transaction and needing to understand the tax stack in each jurisdiction
- Advising on repatriation of profits (dividends, interest, royalties) from a MENA entity to a foreign parent
- Evaluating UAE free-zone vs onshore entity tax treatment under the new CIT regime
- Checking whether a transaction triggers VAT registration or reverse-charge obligations
- Understanding GCC-wide VAT coordination rules for intra-GCC transactions
- Preliminary assessment before engaging a tax adviser for a formal opinion

## Inputs

| Input | Why it matters | Default |
|-------|---------------|---------|
| Transaction type or entity | CIT and VAT treatment differ by transaction type (service, goods, financial instrument, IP license, dividend) | Required |
| Jurisdiction(s) | Tax rules are jurisdiction-specific; cross-border transactions implicate multiple | Required |
| Entity type | Free-zone vs onshore; resident vs non-resident; financial institution vs corporate | Required for accurate analysis |
| Counterparty jurisdiction | For withholding tax and treaty relief analysis | Provide if cross-border |
| Industry / sector | Some sectors have specific regimes (insurance, banking, oil & gas, real estate) | Provide if specialized |

## MENA tax framework overview

### UAE — Federal Tax

The UAE introduced a corporate income tax (CIT) regime effective for financial years starting on or after 1 June 2023, administered by the Federal Tax Authority (FTA) under Federal Decree-Law No. 47 of 2022.

| Tax type | Rate | Threshold / scope |
|---|---|---|
| **Corporate Income Tax (CIT)** | 9% | Taxable income exceeding AED 375,000; 0% below this threshold |
| **Free Zone Qualifying Income** (QFZP) | 0% | Income qualifying under the Qualifying Free Zone Person rules (must meet substance, nexus, and non-disqualifying income tests) |
| **Value Added Tax (VAT)** | 5% standard; 0% for designated zero-rated supplies | Mandatory registration threshold: AED 375,000 taxable supplies/year |
| **Withholding Tax** | 0% (currently) | UAE imposes no withholding tax on dividends, interest, or royalties — a key structuring feature |
| **Excise Tax** | 50–100% | Selective goods (tobacco, carbonated beverages, energy drinks, etc.) |
| **Transfer Pricing** | OECD arm's-length standard applies under CIT Law | TP documentation required for groups above thresholds |

**UAE free-zone QFZP watch-outs**:
- A free-zone entity loses QFZP status if it earns "Excluded Income" — broadly, income from transactions with UAE mainland customers above a de minimis threshold
- The substance requirements (adequate employees, assets, management in UAE) are enforced
- Pillar Two Global Minimum Tax: large multinational groups (€750M+ revenue) will be subject to 15% top-up under the UAE's adoption of the OECD framework

### KSA — Zakat, Tax & Customs Authority (ZATCA)

| Tax type | Rate | Threshold / scope |
|---|---|---|
| **Corporate Income Tax** | 20% (foreign companies / non-Saudi shareholders' portion) | Applicable to the share of profits attributable to non-Saudi shareholders |
| **Zakat** | 2.5% of Zakat base | Applicable to Saudi and GCC shareholders' portion; replaces CIT for them |
| **VAT** | 15% (increased from 5% in July 2020) | Mandatory registration threshold: SAR 375,000 taxable supplies |
| **Withholding Tax** | 5–20% on various outbound payments | Dividends: 5%; interest and royalties: 15%; technical services: 5–20%; management fees: 20% |
| **Transfer Pricing** | BEPS-aligned TP rules (Ministerial Resolution No. 4322 of 2019) | CbC, master file, local file for qualifying groups |

**KSA Zakat vs CIT split**: in a mixed-ownership entity, the Zakat base and CIT base are computed separately and allocated proportionally to Saudi/GCC vs non-Saudi ownership. This creates complexity in JV structures.

### GCC VAT coordination

The GCC Unified VAT Agreement (2017) established a harmonized VAT framework. All GCC member states have implemented VAT, but rates and scope vary:

| Country | VAT rate | Notes |
|---|---|---|
| UAE | 5% | FTA |
| KSA | 15% | ZATCA |
| Bahrain | 10% | NBR |
| Oman | 5% | OTA |
| Qatar | Not yet implemented | |
| Kuwait | Not yet implemented | |

**Place-of-supply rules for intra-GCC B2B services**: the destination-country rule applies for registered businesses (reverse charge); the origin-country rule for non-registered recipients. Practical complexity arises for digital services.

### UAE (DIFC / ADGM specific)

DIFC and ADGM entities are subject to UAE federal CIT. However, free-zone entities within DIFC/ADGM may qualify as QFZPs.

DIFC additionally has no UAE real estate registration fees on DIFC-internal transfers; strata title transfers have separate DIFC-specific charges.

### Egypt

| Tax type | Rate | Notes |
|---|---|---|
| **Corporate Income Tax** | 22.5% (general); 25% for oil & gas and certain sectors | |
| **VAT** | 14% standard rate | Introduced 2016 replacing Sales Tax |
| **Withholding Tax** | 5–20% | Dividends to non-residents: 10% (reduced by treaty); royalties: 20%; interest: 20% |
| **Capital Gains Tax** | 10% on listed securities (suspended/varied); 22.5% for unlisted | Regime has been amended frequently |
| **Stamp Duty** | Varies by instrument | 0.4% on loan agreements; share transfers: 0.3% |

### Lebanon

| Tax type | Rate | Notes |
|---|---|---|
| **Corporate Income Tax (Real profits)** | 17% | Applicable to SAL companies on worldwide income; SARL similar |
| **Built property tax** | Varies by municipality | On rental income / notional rental value |
| **VAT** | 11% | Registration threshold: LBP equivalent (monitor; LBP devaluation makes USD-equivalent threshold effectively very low) |
| **Withholding Tax on dividends** | 10% | Applies to profit distributions |
| **Withholding Tax on interest** | 7% | On interest earned at Lebanese banks (suspended for foreign currency interest under BDL circular regime) |
| **Capital Gains** | Generally exempt on share sales; tax on real property gains | |

**Lebanon banking secrecy (Law 3/1956)**: secrecy provisions historically prevented effective tax enforcement; the economic crisis and IMF reform requirements are driving gradual erosion of this framework. Tax certainty for Lebanon-domiciled structures is currently low.

### UK

| Tax type | Rate | Notes |
|---|---|---|
| **Corporation Tax** | 25% (main rate, from April 2023); 19% small profits rate | Main rate applies to profits > £250,000 |
| **VAT** | 20% standard; 5% reduced; 0% zero-rated | Registration threshold: £90,000 (2024) |
| **Withholding Tax on dividends** | 0% under domestic law | UK imposes no WHT on dividends |
| **Withholding Tax on interest** | 20% (reduced/eliminated by treaty in most cases) | |
| **Withholding Tax on royalties** | 20% (reduced by treaty) | |
| **Capital Gains** | 25% (companies, from April 2023) | Part of corporation tax |
| **Stamp Duty Land Tax (SDLT)** | 0–12% on property value | |
| **OECD Pillar Two** | 15% minimum | UK adopted via Multinational Top-up Tax |

### France

| Tax type | Rate | Notes |
|---|---|---|
| **Impôt sur les Sociétés (IS)** | 25% (standard); 15% for SMEs on first €42,500 | |
| **VAT (TVA)** | 20% standard; 10% / 5.5% / 2.1% reduced rates | |
| **Withholding Tax on dividends** | 12.8% (may be reduced by treaty) | |
| **Withholding Tax on royalties/interest** | 0% EU recipients (Parent-Subsidiary Directive); 0–33% third countries | |
| **CVAE / CFE** | Local business tax (being phased out 2024–2027) | |

### US

| Tax type | Rate | Notes |
|---|---|---|
| **Federal Corporate Income Tax** | 21% (TCJA flat rate since 2018) | |
| **State corporate income tax** | 0–12% (varies by state) | Delaware: 8.7% |
| **Sales tax (VAT equivalent)** | 0–10.25% | State + local; no federal VAT in US |
| **Withholding Tax on dividends to foreign persons** | 30% (treaty may reduce to 5–15%) | |
| **Withholding Tax on interest** | 30% (treaty may reduce or eliminate) | |
| **GILTI / FDII** | Anti-abuse measures for offshore structures | Relevant for MENA holding structures |

## Withholding tax and double tax treaty (DTT) analysis

Cross-border payments trigger withholding tax in the source jurisdiction unless reduced by a DTT. Key MENA DTT coverage:

| From → To | KSA treaty? | UAE treaty? |
|---|---|---|
| MENA → UK | KSA-UK DTT: dividends 5%/15%; interest 0% | UAE-UK DTT: dividends 0%; interest 0% |
| MENA → France | KSA-FR DTT; UAE-FR DTT | Check treaty for current rates |
| MENA → US | No KSA-US DTT (! — 30% WHT applies) | No UAE-US DTT (! — 30% WHT applies) |
| MENA → MENA (GCC) | GCC treaty for avoidance of double tax | Mutual exemptions under GCC DTT |

**Critical trap**: Neither UAE nor KSA has a double tax treaty with the US. Payments from US entities to UAE/KSA entities (royalties, interest, dividends) are subject to US withholding at the full 30% treaty rate unless a third-country intermediary holding company in a treaty jurisdiction is used — a legitimate structuring consideration.

## Transfer pricing

BEPS (Base Erosion and Profit Shifting) compliance requirements apply in UAE (since CIT law 2023), KSA (since 2019 TP rules), Egypt, and broadly GCC:

| Obligation | Threshold | Description |
|---|---|---|
| Country-by-Country Report (CbCR) | Revenue ≥ AED 3.15B / SAR 3.2B | Annual filing with tax authority |
| Master File | Revenue above threshold (varies) | Group-level TP documentation |
| Local File | Revenue above threshold (varies) | Entity-level TP documentation |
| Arm's length standard | All related-party transactions | OECD-aligned |

## Special regimes and watch-outs

- **UAE free-zone QFZP**: 0% on qualifying income; strict substance and nexus tests; loss of QFZP status if disqualifying income exceeds threshold
- **KSA Zakat/CIT split**: complex for JV/mixed-ownership; requires separate computation
- **Lebanon bank secrecy erosion**: tax environment increasingly uncertain under IMF reform pressure
- **OECD Pillar Two top-up**: UAE multinational groups with €750M+ revenue face 15% minimum effective tax rate regardless of free-zone regime
- **VAT on digital services (B2C)**: all GCC VAT regimes now require non-resident digital service providers to register if B2C sales exceed registration threshold

## Output schema

```json
{
  "headline": "2–3 sentence summary of the tax position",
  "breakdown": {
    "CIT": { "rate": "string", "base": "string", "notes": "string" },
    "VAT": { "rate": "string", "scope": "string", "notes": "string" },
    "withholdingTax": [
      { "paymentType": "dividends | interest | royalties | services", "rate": "string", "treatyRelief": "string" }
    ],
    "transferPricing": { "applicable": boolean, "obligations": ["list"] },
    "stampDutyOrOther": { "description": "string" }
  },
  "treatyReliefAvailable": "string — which DTTs are relevant and what relief they provide",
  "optimizationOptions": ["legitimate structuring considerations to discuss with tax adviser"],
  "watchOuts": ["jurisdiction-specific traps, recent changes, Pillar Two exposure"],
  "disclaimer": "Not tax advice — confirm with a licensed tax adviser in the relevant jurisdiction(s) before taking any position."
}
```

## Disclaimer

This skill produces a preliminary tax framework for informational purposes only. It does not constitute tax advice. Tax positions must be confirmed by a licensed tax adviser qualified in the relevant jurisdiction(s). Tax laws change frequently; verify the currency of all rates and rules before reliance, particularly in UAE (post-CIT 2023 regulations continue to develop) and KSA (ZATCA enforcement posture is evolving).

## Related skills

- [[research-regulation-lookup]]
- [[research-regulator-guidance-lookup]]
- [[research-jurisdiction-comparison]]
- [[research-recent-amendments-tracker]]
- [[review-compliance-gap-analysis]]
