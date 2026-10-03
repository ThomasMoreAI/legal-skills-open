# NIS2 Sector Classification Reference

## Table of Contents
1. Annex I — Sectors of High Criticality
2. Annex II — Other Critical Sectors
3. Size Thresholds
4. Regardless-of-Size Entities
5. German-Specific Sector Mapping (BSIG-neu)
6. Exclusions & Special Rules

---

## 1. Annex I — Sectors of High Criticality

Entities in these sectors can be classified as **essential** (if large) or **important** (if medium).

| # | Sector | Sub-sectors | Examples |
|---|--------|------------|---------|
| 1 | **Energy** | Electricity (supply, distribution, transmission, generation), District heating/cooling, Oil (production, refining, storage, transmission, supply), Gas (distribution, transmission, storage, supply, LNG), Hydrogen | Grid operators, generators >50MW, oil refineries, gas TSOs, hydrogen producers |
| 2 | **Transport** | Air (carriers, airport operators, traffic management), Rail (infrastructure managers, undertakings, service facilities), Water (inland/sea/coastal passenger & freight, port operators, VTS), Road (road authorities, ITS operators) | Airlines, rail operators (DB, etc.), port authorities, motorway operators |
| 3 | **Banking** | Credit institutions as defined by CRR | Banks, savings institutions (Sparkassen), cooperative banks |
| 4 | **Financial market infrastructure** | Trading venues, CCPs | Stock exchanges, central counterparties |
| 5 | **Health** | Healthcare providers, EU reference labs, R&D/manufacturing of pharmaceuticals (NACE C.21), medical devices (critical in public health emergency) | Hospitals, pharma manufacturers, medical device makers |
| 6 | **Drinking water** | Supply and distribution of water for human consumption | Municipal water utilities, water treatment plants |
| 7 | **Waste water** | Collection, disposal, treatment of urban/domestic/industrial waste water | Sewage treatment plants, waste water utilities |
| 8 | **Digital infrastructure** | IXPs, DNS providers, TLD registries, cloud computing, data centres, CDNs, trust service providers, public electronic communications networks/services | Cloud providers, data centres, telecom operators, DNS operators |
| 9 | **ICT service management (B2B)** | Managed service providers (MSPs), managed security service providers (MSSPs) | IT outsourcing providers, SOC-as-a-service |
| 10 | **Public administration** | Central government entities (excl. judiciary, parliament, central banks) | Federal ministries, federal agencies (Germany: Bundesbehörden) |
| 11 | **Space** | Operators of ground-based infrastructure supporting space-based services | Satellite ground station operators, space situational awareness providers |

## 2. Annex II — Other Critical Sectors

Entities in these sectors are classified as **important** (medium or large).

| # | Sector | Sub-sectors | Examples |
|---|--------|------------|---------|
| 1 | **Postal and courier** | Postal service providers (as per Postal Services Directive) | DHL, Hermes, DPD, national postal operators |
| 2 | **Waste management** | Waste collection, treatment, recovery, disposal (excl. waste water) | Recycling plants, municipal waste services, hazardous waste handlers |
| 3 | **Chemicals** | Manufacture, production, distribution of chemicals (NACE C.20) | Chemical plants, specialty chemical producers, distributors |
| 4 | **Food** | Production, processing, distribution (NACE C.10/C.11) including wholesale | Food manufacturers, wholesale distributors, large-scale processors |
| 5 | **Manufacturing** | Medical devices & IVDs, computers/electronics/optical (C.26), electrical equipment (C.27), machinery (C.28), motor vehicles (C.29), other transport equipment (C.30) | Automotive OEMs, electronics manufacturers, machine builders |
| 6 | **Digital providers** | Online marketplaces, online search engines, social networking platforms | E-commerce platforms, search engines, social media |
| 7 | **Research** | Research organizations (where results are exploited for commercial purposes) | Applied research institutes, R&D divisions with commercial output |

## 3. Size Thresholds

NIS2 applies to **medium and large enterprises** as defined by Commission Recommendation 2003/361/EC:

| Category | Employees | Turnover | Balance sheet |
|----------|-----------|----------|---------------|
| **Medium** | ≥ 50 | > €10M | > €10M |
| **Large** | ≥ 250 | > €50M | > €43M |

**Important:** The thresholds use OR/AND logic:
- An entity is medium-sized if it has **≥ 50 employees** OR (**turnover > €10M** AND **balance sheet > €10M**)
- An entity is large if it has **≥ 250 employees** OR (**turnover > €50M** AND **balance sheet > €43M**)

A company with 30 employees but €15M turnover and €12M balance sheet IS in scope (medium-sized).

### Group Structure Rules

- Where the entity is part of a group, apply the linked/partner enterprise rules from Recommendation 2003/361/EC
- Consolidated figures may apply where there is operational integration
- Where entities within a group operate independently in different sectors, assess each entity separately
- In Germany: § 28(3) BSIG-neu provides specific guidance on group-level assessment

## 4. Regardless-of-Size Entities

These entities fall under NIS2 **regardless of their size**, even if below medium thresholds:

| Entity type | Classification | Basis |
|-------------|---------------|-------|
| Qualified trust service providers | Essential | Art. 2(2)(a) |
| TLD name registries | Essential | Art. 2(2)(b) |
| DNS service providers | Essential | Art. 2(2)(c) |
| Public electronic communications networks/services | Essential* | Art. 2(2)(d) |
| Public administration — central level | Essential | Art. 2(2)(f) |
| Sole provider of critical service in Member State | Essential | Art. 2(2)(e) |
| Entity whose disruption could have significant systemic impact | Case-by-case | Art. 2(2)(e) |
| Entities identified under prior CER Directive (2008/114/EC) | In scope | Art. 2(2)(g) |
| Entities providing domain name registration services | Important | Art. 2(2)(b) |

*In Germany, the TK-Schwellenwert was removed during parliamentary proceedings — all telecom providers are now in scope regardless of customer count.

## 5. German-Specific Sector Mapping (BSIG-neu)

The German transposition in the BSIG-neu uses the categories:
- **Besonders wichtige Einrichtungen** (§ 28(1) BSIG) ≈ essential entities
- **Wichtige Einrichtungen** (§ 28(2) BSIG) ≈ important entities
- **KRITIS-Betreiber** — automatically classified as "besonders wichtige Einrichtungen" with additional obligations

Key German additions/differences:
- KRITIS operators have additional threshold-based rules (BSI-KritisV) beyond the general NIS2 size test
- Public administration scope is limited to Bundesverwaltung (federal level); Länder and municipal levels may be covered by state legislation
- § 28(5) BSIG: Energy sector entities where the NIS2-relevant activity is only a Nebentätigkeit (ancillary activity) may be exempt — but this is interpreted narrowly

## 6. Exclusions & Special Rules

**Excluded from NIS2:**
- Entities in national security, public security, defence, law enforcement
- Judiciary, parliaments, central banks
- Entities already covered by sector-specific EU legislation providing equivalent cybersecurity requirements (Art. 4 — e.g., DORA for financial sector entities)

**DORA interaction (Regulation (EU) 2022/2554):**
- Financial entities covered by DORA are excluded from NIS2 cybersecurity measures (Art. 21) and incident reporting (Art. 23)
- However, NIS2 cooperation and information-sharing provisions still apply
- ICT third-party service providers to financial entities remain under NIS2 unless themselves financial entities

**Micro/small enterprise safe harbour:**
- Entities below medium-size thresholds are generally out of scope
- Exception: regardless-of-size entities listed above
- Member States may designate additional small entities if they meet criticality criteria
