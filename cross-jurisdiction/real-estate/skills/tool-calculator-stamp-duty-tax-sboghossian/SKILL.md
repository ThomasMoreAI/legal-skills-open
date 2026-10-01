---
name: tool-calculator-stamp-duty-tax-sboghossian
title: Tool — Stamp Duty / Transfer Tax Calculator
description: Use when computing stamp duty, transfer tax, or real-estate transaction tax on property or share transfers across MENA and European jurisdictions. Covers UAE (Dubai DLD 4%, Abu Dhabi 2%), KSA (RETT 5%), Lebanon (5–7% registration + stamp), UK (SDLT with residential surcharges), and France (droits d'enregistrement ~5.8%). Returns computed tax, breakdown by component, applicable exemptions, and jurisdiction-specific structuring notes.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/tool/tool-calculator-stamp-duty-tax
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: real-estate
language: en
---

# Tool — Stamp Duty / Transfer Tax Calculator

## What it does

Computes statutory transfer taxes — stamp duty, transfer fees, registration taxes — applicable to real-estate and share transfers across MENA and selected European jurisdictions. Returns the computed tax with a component breakdown, applicable exemptions, the due date for payment, and notes on structuring considerations.

## Inputs

| Field | Type | Required | Notes |
|---|---|---|---|
| `jurisdiction` | enum | Yes | `UAE-Dubai`, `UAE-AbuDhabi`, `UAE-Sharjah`, `KSA`, `LB`, `UK`, `FR` |
| `propertyValue` | number | Yes | Transaction value in local currency |
| `currency` | string | No | Defaults to jurisdiction currency |
| `propertyType` | enum | Yes | `residential`, `commercial`, `industrial`, `mixed`, `shares` |
| `buyerStatus` | object | Yes | `{ resident: bool, firstTimeBuyer: bool, corporate: bool, nonResident: bool }` |
| `sellerStatus` | object | No | Relevant for split-fee jurisdictions |
| `structuringNotes` | string | No | Any pre-agreed fee-splitting or special structure |

## Jurisdiction rules

### UAE — Dubai (DLD transfer fee)

- **Rate:** 4% of property value
- **Split:** By custom (not law), buyer and seller each pay 2%; confirm split in SPA
- **Payable to:** Dubai Land Department (DLD)
- **Due:** At time of property registration
- **Off-plan:** 4% applies on original transaction value; no re-charge on resale unless registered
- **Mortgaged transfer:** Additional 0.25% mortgage registration fee applies
- **Exemptions:** None for standard transfers; certain government entities exempt

---

### UAE — Abu Dhabi (ADREDA / ADDED)

- **Rate:** 2% of property value
- **Payable to:** Abu Dhabi Department of Municipalities and Transport (DMT)
- **Split:** Typically buyer-paid; confirm in SPA
- **Notes:** Lower than Dubai; relevant for ADGM-adjacent transactions

---

### UAE — Sharjah

- **Rate:** 2% of property value
- **Payable to:** Sharjah Real Estate Registration Department
- **Notes:** Sharjah restricts freehold ownership to UAE nationals; foreigners limited to designated areas

---

### KSA — Real Estate Transaction Tax (RETT)

- **Rate:** 5% of property value
- **Introduced:** October 2020; **replaces** VAT on real-estate transfers (real property is not subject to 15% VAT where RETT applies)
- **Payable by:** Seller (by default), but parties may agree otherwise
- **Exemptions:** First-home transfer (up to SAR 1 million) exempted on first transfer; certain government-related transfers; gifts between first-degree relatives
- **Filing:** RETT declaration required with ZATCA (Zakat, Tax and Customs Authority) before registration
- **Share transfers:** RETT does not apply to share transfers in a company owning real property; however, stamp duty / capital gains considerations may apply

---

### Lebanon — Registration and Stamp

- **Registration tax (rasm tasji3):** 3–5% depending on emirate/type (varies by governorate; Beirut typically ~3%)
- **Stamp duty:** 0.2–2% on top of registration
- **Total typical range:** 5–7% of declared value
- **Currency caveat:** Lebanese property transactions post-2019 involve complex USD/LBP currency issues; declared value and actual payment currency must be verified with the notary
- **Payable to:** Lebanese Land Registry (Cadastre); notarised deed required
- **Notarisation:** Mandatory; transfer deed must be certified by a Lebanese notary

---

### UK — Stamp Duty Land Tax (SDLT)

**Residential:**
- £0 – £250,000: 0%
- £250,001 – £925,000: 5%
- £925,001 – £1,500,000: 10%
- Over £1,500,000: 12%
- **Additional dwelling surcharge (buy-to-let, second home):** +3% on all bands
- **Non-UK resident surcharge:** +2% on all bands (cumulative with additional dwelling surcharge)
- **First-time buyer relief:** £0 on first £425,000; 5% on £425,001–£625,000; standard rates above

**Commercial:**
- £0 – £150,000: 0%
- £150,001 – £250,000: 2%
- Over £250,000: 5%

**Share transfers:** 0.5% Stamp Duty on share transfer forms (SDRT); no SDLT on shares

---

### France — Droits d'enregistrement

- **Standard residential/commercial:** ~5.80% total (4.50% departmental tax + 0.60% municipal tax + 0.70% national levy + notary fees on top)
- **New properties (TVA/VAT applies):** Subject to TVA at 20% instead of droits d'enregistrement; reduced droits at ~0.71%
- **Corporate / SCI share transfers:** 5% on real-estate-holding SCI share transfers (above a threshold)
- **Payable to:** Via notaire at closing; mandatory notarised deed

## Output schema

```json
{
  "jurisdiction": "UAE-Dubai",
  "propertyValue": 5000000,
  "currency": "AED",
  "propertyType": "residential",
  "tax": {
    "transferFee": 200000,
    "mortgageRegistrationFee": 0,
    "total": 200000,
    "breakdown": [
      { "component": "DLD Transfer Fee (4%)", "amount": 200000 }
    ]
  },
  "split": "By custom: buyer AED 100,000 / seller AED 100,000 (confirm in SPA)",
  "exemptions": [],
  "dueDate": "At time of DLD registration",
  "notes": "Confirm off-plan vs secondary market status; mortgage registration fee (0.25%) applies if mortgaged"
}
```

## Structuring notes

- **UAE:** Transfers via offshore corporate holding structures (BVI/Cayman) holding UAE freehold are common for high-value assets. Consult a UAE tax specialist on DLD treatment of corporate-layer transfers; DLD may treat the beneficial owner transfer as a triggering event.
- **KSA:** Share-for-property structuring to avoid RETT is closely watched by ZATCA; anti-avoidance provisions apply.
- **Lebanon:** Notarisation is mandatory and complex in the current financial environment; always involve a Lebanese notary.
- **UK:** SDLT anti-avoidance rules (FA 2003) and the sub-sale rules require specialist advice for complex structures.

## Always pair with

- [[review-title-clean]] — verify clean title before computing tax on a transfer
- [[research-tax-treatment-lookup]] — broader tax treatment (VAT, CGT, WHT)
- [[tool-currency-converter]] — for cross-currency transactions

## Related skills

- [[review-title-clean]]
- [[research-tax-treatment-lookup]]
- [[tool-currency-converter]]
- [[kb-real-estate-law-mena]]
