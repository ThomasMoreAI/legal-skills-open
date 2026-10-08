---
name: kb-real-estate-uae-sboghossian
title: Knowledge Pack — UAE Real Estate Law
description: Use when a matter involves real estate ownership, leasing, off-plan purchases, RERA regulation, Ejari or Tawtheeq registration, or real estate transactions in UAE (Dubai, Abu Dhabi, and other emirates). Covers freehold vs designated-area foreign ownership, Dubai Land Department (DLD) procedures, RERA rent-cap calculator, Abu Dhabi Tawtheeq, off-plan escrow rules, VAT treatment of real estate, DIFC and ADGM real estate frameworks, and the Golden Visa real estate pathway. Triggers on UAE real estate purchase, Ejari registration, RERA rent increase, off-plan Dubai, DLD transfer, or UAE property questions.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/kb/kb-real-estate-uae
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ae
practice: real-estate
language: en
---

# Knowledge Pack — UAE Real Estate Law

## Federal vs Emirate Framework

Real estate in UAE is primarily regulated at the **emirate level** — there is no single UAE federal real estate law:

- **UAE Federal Civil Code** (Federal Law 5/1985, as amended) provides general contract and property principles.
- Each emirate enacts its own real estate laws, registration systems, and rent regulations.
- **Dubai** and **Abu Dhabi** are the dominant markets; Sharjah, RAK, Ajman, Fujairah, and UAQ have their own systems.

---

## Dubai Real Estate

### Regulatory Architecture

| Body | Role |
|---|---|
| **DLD** (Dubai Land Department) | Title registration; NOC process; off-plan oversight |
| **RERA** (Real Estate Regulatory Authority, part of DLD) | Broker licensing; rental regulation; strata management |
| **RDC** (Rental Disputes Centre) | First-instance tribunal for rental disputes |
| **Ejari** | Mandatory tenancy contract registration system |

### Ownership Categories

| Category | Who May Own |
|---|---|
| Freehold | UAE nationals, GCC nationals — across all of Dubai |
| Freehold (Designated Areas) | Foreign nationals may own freehold in **designated freehold areas** per DLD Decree 3/2006 and subsequent additions |
| Leasehold (up to 99 years) | Foreign nationals in non-designated areas (limited) |
| Off-plan designated areas | Same as freehold; off-plan projects in designated areas available to foreigners |

**Designated freehold areas** include: Dubai Marina, Palm Jumeirah, Downtown Dubai, Business Bay, JBR, DIFC, Dubai Hills, Arabian Ranches, Jumeirah Village, and many others — DLD publishes the current list.

### Sale Transaction Process (Resale)

1. **MOU (Memorandum of Understanding — Form F)**: standard DLD form; signed by buyer, seller, and agent; outlines agreed price, timeline, NOC conditions.
2. **NOC (No Objection Certificate)** from developer: confirms no outstanding service charges or defects.
3. **DLD Transfer**: both parties (or authorized power of attorney) attend DLD; transfer fee paid.
4. **Transfer Fee**: **4% of property value** (DLD transfer fee); typically split equally between buyer and seller (or as agreed in MOU).
5. **Agent Commission**: typically 2% of value.
6. **New Title Deed** issued by DLD.

Timeline from signed MOU to title transfer: typically **2–4 weeks** for cash transactions; longer for mortgage transactions (bank approval + DLD mortgage registration).

### Off-Plan Transactions (Dubai)

Governed by **Dubai Decree 13/2008** and subsequent RERA regulations:

| Requirement | Rule |
|---|---|
| Escrow account | Developer must hold buyer payments in DLD-approved escrow |
| Escrow release | Funds released as construction milestones verified |
| Developer registration | Project and developer must be registered with RERA |
| Buyer protection | Buyer entitled to refund if developer fails to complete (via escrow); additional remedies |
| Completion timeline | Developer must disclose and meet stated timeline |
| DLD oversight | Project completion certificates, inspections |

### Rental Regulation (Dubai)

- **Dubai Tenancy Law** (Decree 26/2013 as amended by Decree 33/2020 and Decree 43/2013).
- **Ejari**: mandatory registration of all residential and commercial tenancy contracts.
- **Rent increase cap**: RERA publishes an online rent calculator; rent increases above the calculator output require RERA approval.
  - If current rent is **within 25%** of market: no increase permitted.
  - If 11–25% below market: max 5% increase.
  - If 26–35% below market: max 10% increase.
  - If 36–45% below market: max 15% increase.
  - If > 45% below market: max 20% increase.
- **Non-renewal notice**: landlord must give **12 months' written notice** (via Notary Public or registered mail) to not renew or to regain the property for personal use.
- **RDC (Rental Disputes Centre)**: resolves Dubai rental disputes; filing fee applies; decisions appealable to Dubai Courts.

---

## Abu Dhabi Real Estate

### Regulatory Architecture

| Body | Role |
|---|---|
| **DMT** (Department of Municipalities and Transport, Abu Dhabi) | Land registration; property regulation |
| **Tawtheeq** | Mandatory tenancy contract registration (residential and commercial) |
| **Abu Dhabi Judicial Department (ADJD)** | Judicial disputes |

### Ownership Categories (Abu Dhabi)

- **UAE/GCC nationals**: freehold across Abu Dhabi.
- **Foreign nationals**: freehold ownership in **Investment Zones** (designated areas: Al Reem Island, Yas Island, Saadiyat Island, Al Raha Beach, Masdar City, etc.).
- **Outside Investment Zones**: foreign nationals may hold **musataha** (long-term right of use + build, up to 50 years renewable) or **usufruct**.

### Tawtheeq Registration

- **Mandatory** for all residential and commercial leases in Abu Dhabi.
- Tawtheeq generates a registered tenancy contract number.
- Required for DEWA/ADDC utility connections and other services.
- Rental disputes: Abu Dhabi Judicial Department (Rent Disputes section).

---

## Sharjah, RAK, Ajman, Fujairah, UAQ

| Emirate | Foreign Ownership | Land Dept | Rent Registration |
|---|---|---|---|
| Sharjah | Restricted; nationals + GCC; limited foreigners in specific areas | SRERD | Ejari (Sharjah) |
| Ras Al Khaimah | Foreign freehold in designated zones (growing RAK Real Estate Dept list) | RAK Real Estate Dept | RAK |
| Ajman | Foreign ownership in designated areas | AREDA | AREDA |
| Fujairah | Limited foreign; nationals + GCC | FDED | FDED |
| UAQ | Very limited | UAQ Lands Dept | UAQ |

---

## DIFC and ADGM Real Estate

### DIFC

- **DIFC Real Estate Law 2009** governs real property within DIFC.
- **Common-law principles** apply (English law-inspired).
- Direct **freehold ownership** of units/floors within DIFC buildings by foreign investors.
- DIFC Courts resolve disputes.
- Wills: DIFC Wills Service Centre allows registration of non-Muslim wills covering DIFC-situated real estate.

### ADGM

- **ADGM Real Property Regulations** govern ADGM real estate.
- Common-law principles.
- Foreign ownership permitted within ADGM designated development areas.
- ADGM Courts resolve disputes.

---

## VAT Treatment of Real Estate

| Type | VAT Treatment |
|---|---|
| Residential property — first supply | **Zero-rated** (0% VAT) |
| Residential property — subsequent supplies | **Exempt** (no VAT; no input credit recovery) |
| Commercial property (offices, retail) | **Standard rated** (5% VAT) |
| Bare land | **Zero-rated** |
| Off-plan residential | **Zero-rated** |
| Off-plan commercial | **5% VAT** on installments |
| Hotel accommodation / serviced apartments | **5% VAT** (treated as service, not accommodation supply) |

VAT registration threshold: AED 375,000 turnover per year — property developers must register if above this.

---

## Golden Visa via Real Estate

Foreign nationals owning UAE real estate valued at **AED 2,000,000+** qualify for a 10-year Golden Visa self-sponsored residency (see [[kb-immigration-residency-uae-golden-visa]]):
- Must be freehold ownership in a designated area.
- Property value: paid-up value (cash or mortgage paid-down) must equal AED 2M.
- Applies in all Emirates with designated freehold areas.

---

## Common Transaction Structures

| Transaction | Procedure Summary |
|---|---|
| Resale (Dubai) | MOU (Form F) → NOC from developer → DLD transfer → 4% fee → new title deed |
| Lease (Dubai) | Private contract → Ejari registration → utility connection |
| Lease (Abu Dhabi) | Private contract → Tawtheeq registration → utility connection |
| Off-plan (Dubai) | Developer SPA → escrow account → RERA oversight → handover + DLD registration |
| Mortgage | Bank loan agreement → DLD mortgage registration → lender holds title charge |
| DIFC property | DIFC Real Estate Law process → DIFC Courts jurisdiction |

---

## Practical Drafting Notes

- **POA for DLD**: if buyer or seller cannot attend in person, a UAE-authenticated POA is required; foreign-notarized POAs must be apostilled and UAE Embassy attested.
- **Service charges**: confirm RERA-registered service charge amounts before purchase; outstanding service charges may block NOC.
- **Strata law**: Dubai Owners' Association Law (Law 27/2007); maintenance fees, strata management, common area rights.
- **Mortgage pre-approval**: obtain bank pre-approval before signing MOU with mortgage condition.

## Caveats & Currency

Dubai's designated freehold area list expands periodically — verify current DLD list. Abu Dhabi Investment Zone list also evolves. RERA rent calculator thresholds and market indices are updated regularly. VAT treatment of complex property transactions requires UAE Federal Tax Authority guidance verification. Off-plan regulations are strengthened regularly — verify current RERA requirements before advising on a specific project.

## Related Skills

- [[kb-real-estate-ksa]]
- [[kb-real-estate-lb]]
- [[kb-employment-law-uae]]
- [[kb-immigration-residency-uae-golden-visa]]
- [[kb-family-law-uae-civil-personal-status]]
