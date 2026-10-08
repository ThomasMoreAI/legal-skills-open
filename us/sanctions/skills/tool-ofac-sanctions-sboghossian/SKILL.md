---
name: tool-ofac-sanctions-sboghossian
title: OFAC Sanctions Screening
description: Use when screening a counterparty, individual, vessel, or aircraft against the US Treasury OFAC Specially Designated Nationals (SDN) list as part of KYC, AML, or transaction compliance checks. Applies fuzzy name matching with transliteration support (Latin/Arabic/Cyrillic), the OFAC 50% Rule for beneficial-owner taint, and Sectoral Sanctions Identifications (SSI). Always pair with UN and EU sanctions lists for a complete compliance screen. Critical for any transaction with a US-dollar leg or US-person nexus.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/tool/tool-ofac-sanctions
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: sanctions
language: en
---

# OFAC Sanctions Screening

## What it does

This tool screens counterparties, individuals, vessels, aircraft, and associated addresses against the US Office of Foreign Assets Control (OFAC) Specially Designated Nationals and Blocked Persons (SDN) list and related sanctions programs. OFAC's jurisdiction extends beyond US persons: any transaction that touches the US financial system — including any USD-denominated payment — creates US nexus and OFAC exposure for non-US parties.

For MENA-region transactions, OFAC screening is mandatory wherever:
- USD is used as the contract or payment currency
- A US bank is in the correspondent chain
- Any US person (individual or entity) is involved
- The counterparty may have connections to sanctioned programs (Iran, Syria, Yemen Houthi forces, designated terrorist organizations, Russian sectoral sanctions)

## Sanctions programs and lists

OFAC administers over 35 sanctions programs. The key ones for MENA-region practice:

| Program | Key designation basis | MENA relevance |
|---------|-----------------------|----------------|
| SDN List (Global) | Terrorism, WMD proliferation, narcotics, human rights | All transactions |
| Iran | Nuclear program, terrorism, human rights | Iran-nexus transactions |
| Syria | Civil war atrocities, terrorism | Syria-nexus transactions |
| Yemen (Ansar Allah / Houthi) | SDGT designation (2024) | Red Sea, GCC transactions |
| Hamas / PIJ / Hezbollah | Foreign terrorist organizations | Lebanon, Palestine, Israel-nexus |
| Russia (CAATSA / Executive Orders) | Invasion of Ukraine; defence sector | GCC-Russia investment |
| DPRK | Nuclear/missile program | Cross-border banking |
| Venezuela | PDVSA, Maduro government | Oil / energy |
| Sectoral Sanctions (SSI) | Russia energy, finance, defence sectors | Finance / energy deals |

## Setup / auth

| Parameter | Description | Required |
|-----------|-------------|----------|
| `ofacApiKey` | OFAC API key (free registration at sanctionssearch.ofac.treas.gov) | Recommended |
| `minScore` | Minimum fuzzy match score to flag (0–100); default 75 | No |
| `checkBeneficialOwners` | Apply OFAC 50% Rule to ownership chain | Default: `true` |
| `includeSSI` | Include Sectoral Sanctions Identifications | Default: `true` |

OFAC's list data is also publicly downloadable in XML, CSV, and SDN XML formats from https://sanctionssearch.ofac.treas.gov. The tool caches a local copy and refreshes daily.

## Capabilities

### SDN name screening
```
Input:  {
  name: "محمد عبدالله",
  nameTranslit: "Mohammed Abdullah",
  dob: "1975-03-15",
  nationality: "SY",
  entityType: "individual"
}
Output: {
  hits: [
    {
      sdnName, programs, score,
      alternateSpellings, dateOfBirth, nationality,
      idDocuments, addresses,
      lastUpdated, ofacId
    }
  ],
  cleared: false,
  checkDate: "2026-05-14"
}
```

### OFAC 50% Rule — beneficial owner taint
The OFAC 50% Rule provides that any entity **owned 50% or more** (individually or in aggregate) by one or more SDN persons is itself treated as blocked, even if not named on the SDN list.

```
Input:  { entityName: "Acme Trading LLC", owners: [...] }
Process:
  1. Screen each owner against SDN list
  2. Sum SDN-tainted ownership percentages
  3. If tainted total ≥ 50% → entity is effectively blocked
Output: { blocked: true | false, taintedOwnership: 0.60, taintedOwners: [...] }
```

**MENA application**: this rule is particularly important in the GCC where complex nominee-ownership structures are common and UBO disclosure is inconsistent. If the beneficial ownership chain cannot be verified, flag the transaction as unable-to-clear.

### Vessel and aircraft screening
```
Input:  { imoNumber: "9XXXXXXX", vesselName: "MV EXAMPLE" }
Output: { hits: [...], flagState, operator }
```
IMO numbers are matched exactly. Vessel names are fuzzy-matched with flag-state as a tiebreaker.

### Address screening
Flag transactions with addresses matching OFAC-listed locations (certain Iranian provinces, Crimea, designated territories).

### Sectoral Sanctions (SSI) check
For Russia-related transactions, the SSI list identifies entities in the Russian energy, financial services, and defence sectors subject to restrictions short of full blocking — e.g., restrictions on new debt with tenors over 30 days. These are distinct from SDN designations and require separate analysis.

## Match rules and fuzzy logic

| Match factor | Weight | Implementation |
|---|---|---|
| Name similarity | 40% | Jaro-Winkler distance + phonetic matching |
| Arabic transliteration | 30% | ISO 233 + common variant dictionary (Muhammad/Mohammed/Mohamad) |
| DOB | 20% | Exact match ±2 years tolerance (per OFAC guidance) |
| Address/nationality | 10% | Country code match |

A score ≥ 75 triggers a **potential hit** requiring manual review. A score ≥ 90 is a **strong match** requiring escalation before transaction proceeds. A score < 75 is a **clear** for OFAC purposes (though UN and EU checks must still be run).

## Output schema

```json
{
  "screeningId": "ofac-2026-05-14-001",
  "subject": {
    "name": "Mohammed Abdullah",
    "dob": "1975-03-15",
    "nationality": "SY"
  },
  "hits": [
    {
      "ofacId": "12345",
      "sdnName": "ABDALLAH, Muhammad",
      "programs": ["SDGT", "SYRIA"],
      "score": 82,
      "alternateSpellings": ["Muhammad Abdallah", "محمد عبد الله"],
      "dateOfBirth": "1975",
      "lastUpdated": "2025-11-01",
      "classification": "Individual"
    }
  ],
  "cleared": false,
  "fiftyPercentRuleApplied": true,
  "checkDate": "2026-05-14",
  "checkVersion": "OFAC SDN 2026-05-10",
  "recommendation": "ESCALATE — potential SDN match; do not proceed pending compliance review"
}
```

## Compliance workflow

OFAC screening is not a one-time check at onboarding. Best practice requires:

1. **Pre-transaction screen** — before signing a contract or initiating a payment
2. **Periodic re-screen** — for ongoing business relationships (annually or on regulatory trigger)
3. **Real-time payment screening** — for banks and payment processors, all wire instructions screened at execution
4. **Triggered re-screen** — on any material change (ownership restructuring, new sanction designation)

For high-risk transactions (Iran/Syria/Russia nexus, cash-intensive industries), OFAC recommends enhanced due diligence including transaction monitoring.

## MENA-specific notes

- **Lebanon**: OFAC has active designations related to Hezbollah including many Lebanese individuals and entities in banking, construction, and trade. Lebanese entities require careful screening.
- **UAE**: the UAE has been on the FATF grey list (removed in 2024) and is under pressure to strengthen AML/CFT. UAE onshore entities with Iranian or Russian UBOs require enhanced screening.
- **KSA**: generally lower OFAC exposure, but watch for Yemen/Houthi-adjacent trade and construction contracts.
- **Yemen**: OFAC designated Ansar Allah (Houthis) as a Specially Designated Global Terrorist (SDGT) in 2024; any transaction with Yemen-based entities requires comprehensive screening.
- **Iran nexus**: any entity with Iranian ownership or management, or dealing in Iranian-origin goods, is potentially subject to OFAC's comprehensive Iran sanctions regardless of where it is incorporated.

## Failure modes

| Failure | Symptom | Resolution |
|---------|---------|------------|
| API unavailable | 503 from OFAC API | Fall back to locally cached SDN XML (daily refresh) |
| Name ambiguity | High-score hit on common name | Require additional identifiers (DOB, ID number, address) |
| Transliteration gap | Arabic name missed | Expand to full variant dictionary; flag for manual review |
| Ownership chain incomplete | Cannot apply 50% Rule | Flag as unable-to-clear; request UBO documentation |
| Stale cache | List not refreshed | Force refresh before any screening; OFAC updates daily |

## Related skills

- [[tool-un-sanctions]] — UN Security Council consolidated list; the first layer of any complete sanctions screen
- [[tool-ksa-moc]] — Saudi commercial registry for UBO chain verification
- [[tool-lb-commercial-register]] — Lebanon registry for UBO verification
- [[tool-uae-ded]] — UAE DED registry
- [[research-beneficial-ownership-lookup]] — UBO tracing to apply the 50% Rule
