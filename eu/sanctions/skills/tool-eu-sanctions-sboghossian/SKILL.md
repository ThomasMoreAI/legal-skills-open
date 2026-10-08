---
name: tool-eu-sanctions-sboghossian
title: Tool — EU Sanctions Screening (CFSP Consolidated List)
description: Use when screening individuals, entities, or vessels against the EU Consolidated Financial Sanctions List (CFSP) for AML/KYC, transaction clearance, or regulatory compliance. Covers EU-specific designations layered on top of UN sanctions — Russia/Ukraine (Reg 833/2014), Belarus, Syria, Iran nuclear — with the wider EU "available indirectly" rule and export-control dual-use goods overlap. Always cross-check with UN, OFAC, and UK HMT lists for Gulf transactions.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/tool/tool-eu-sanctions
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: sanctions
language: en
---

# Tool — EU Sanctions Screening (CFSP Consolidated List)

## What it does

Screens names, entities, and vessels against the EU's Consolidated List of Financial Sanctions — maintained under the EU's Common Foreign and Security Policy (CFSP). Returns match results with the applicable regulation, listing date, stated grounds, and asset-freeze status. Also flags applicable export-control restrictions under EU Dual-Use Regulation.

## Setup / auth

- **EU Sanctions Database:** Publicly available at https://eeas.europa.eu/topics/sanctions-policy/8442/consolidated-list-of-sanctions_en
- **API:** EU CFSP offers a bulk XML download and an interactive search; for programmatic access, parse the official XML or use a commercial sanctions-data provider (e.g., Acuris/LSEG World-Check, Refinitiv, Dow Jones).
- **Update frequency:** EU sanctions are updated as new Council Regulations are adopted (can be daily during active sanctions packages, e.g., Russia). Refresh daily.

## Jurisdiction background

### EU sanctions framework

EU sanctions operate through **Council Regulations** under the CFSP framework (Treaty on the Functioning of the EU, TFEU). Two layers:

1. **UN-derived sanctions:** EU implements all UN Security Council sanctions (e.g., ISIL/Al-Qaida, DPRK, Iran nuclear) with Council Regulations.

2. **EU-autonomous sanctions:** EU adds its own designations not derived from UN action. Key regimes:
   - **Russia/Ukraine restrictive measures:** Regulation (EU) No. 833/2014 (sectoral) and Council Regulation (EU) No. 269/2014 (individual designations) — extensively expanded since February 2022; multiple amending packages
   - **Belarus:** Council Regulation (EU) No. 765/2006
   - **Syria:** Council Regulation (EU) No. 36/2012
   - **Iran nuclear:** Council Regulation (EU) No. 267/2012
   - **Myanmar, Sudan, Venezuela, and others:** Separate regimes

### Key legal differences from OFAC

| Feature | EU CFSP | US OFAC |
|---|---|---|
| **Scope** | Applies to all EU persons (natural + legal) and any person using EU infrastructure | Applies to US persons (broader reach via SDN secondary sanctions) |
| **"Available indirectly" rule** | EU's asset-freeze extends to making funds available "directly or **indirectly**" to designated persons — **wider than OFAC's 50% Rule** | OFAC's 50% Rule consolidates ownership at 50%+ threshold |
| **Export controls** | Dual-use goods: Regulation (EU) 2021/821 overlaps with sanctions | EAR (Bureau of Industry and Security) is separate from OFAC |
| **Breach penalties** | Varies by member state; criminal and civil in most | Civil up to $1M per violation; criminal in serious cases |
| **Derogations** | EU permits specific derogation requests to competent national authorities | OFAC OTAC / specific license equivalent |

## Output schema

```json
{
  "query": "Ivanov, Dmitry Alexandrovich",
  "queryDate": "2026-05-14",
  "cleared": false,
  "hits": [
    {
      "id": "EU-RU-0456",
      "name": "IVANOV Dmitry Alexandrovich",
      "entityType": "individual",
      "regulation": "Council Regulation (EU) No 269/2014 (as amended, 14th package)",
      "listingDate": "2023-12-13",
      "grounds": "Support for actions undermining the territorial integrity of Ukraine",
      "assetFreezeStatus": "active",
      "travelBan": true,
      "matchConfidence": "high"
    }
  ],
  "exportControlFlags": [
    "Subject of EU sectoral restrictions; check Annex VII of Reg 833/2014 for goods/services restrictions"
  ]
}
```

## Screening methodology

### Name matching

- Apply fuzzy matching for transliterated names (Cyrillic, Arabic, Persian, Chinese → Latin script may vary)
- Screen aliases, former names, and AKA entries from the consolidated list
- For Arabic-script names: screen both Arabic original and all Latin transliterations in the record
- Flag close matches (confidence 70–95%) for human review; do not automatically clear

### Entity screening

- Screen both the legal entity name and all UBO/PSC chains to 25%+ ownership level (EU "available indirectly" rule)
- For GCC-owned entities: screen the GCC beneficial owners against the list (relevant for Russian-connected capital routed through Gulf structures)
- Check for EU-listed vessels in shipping/commodities transactions (separate vessel list)

## Always cross-check with

For comprehensive sanctions clearance in Gulf and MENA transactions, always run parallel checks:

| List | Tool | Why |
|---|---|---|
| UN Consolidated Sanctions | [[tool-un-sanctions]] | UN lists are binding on all UN members including MENA states |
| OFAC SDN + Sectoral | [[tool-ofac-sanctions]] | US secondary sanctions reach Gulf transactions involving USD or US persons |
| HM Treasury (UK) | — | Post-Brexit UK maintains its own OFSP list; applies to London counterparties |
| UAE Executive Office | — | UAE's own sanctions list (mandatory for UAE-nexus transactions) |

## Limits & escalation

- A "cleared" result is not a guarantee of no sanctions nexus — it means no match on the screened lists as of the search date.
- Sanctions change rapidly (especially Russia/Ukraine). Do not rely on a screening more than 24 hours old for active transactions.
- Complex ownership structures or transactions with a high Russia/Belarus/Iran nexus should be escalated to a specialist sanctions lawyer.
- This tool is an AI-assisted screening aid; it does not constitute legal advice on sanctions compliance.

## Related skills

- [[tool-un-sanctions]]
- [[tool-ofac-sanctions]]
- [[research-kyc-ubo]]
- [[kb-sanctions-law-mena]]
