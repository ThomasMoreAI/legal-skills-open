---
name: research-sanctions-screening-sboghossian
title: Sanctions Screening
description: 'Use when a compliance officer, lawyer, or KYC analyst needs to check whether a person, entity, vessel, or aircraft appears on any active sanctions list before entering a transaction, onboarding a client, or executing a payment. Runs multi-list screening in parallel: OFAC (US), UN Consolidated, EU Consolidated, UK HMT OFSI, KSA NCASGS, UAE EOCN, and Lebanon BDL-SIC. Uses fuzzy name matching with transliteration awareness, DOB, POB, and ID-number matching. Always pairs with UBO lookup — screen beneficial owners, not just direct counterparties.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/research/research-sanctions-screening
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: sanctions
language: en
---

# Sanctions Screening

Multi-list, multi-signal sanctions screening of natural persons, legal entities, vessels, and aircraft. Runs all relevant lists in parallel and returns a consolidated hit report with match confidence scores and escalation flags. Essential pre-transaction and KYC step for any party operating in or connected to a sanctioned-risk jurisdiction.

## When to use this

- **KYC onboarding**: before accepting a new client — person or entity
- **Pre-transaction**: before executing a payment, signing a contract, or completing a deal
- **Periodic re-screening**: existing clients and counterparties, as sanctions lists are updated daily
- **Counterparty due diligence**: in M&A, trade finance, correspondent banking, and letter-of-credit transactions
- **Vessel / aircraft diligence**: shipping, aviation, and logistics involving high-risk routes
- **UBO screening**: sanctions targets often hold assets through intermediaries; screen UBOs identified via [[research-beneficial-ownership-lookup]], not just the direct entity

## Why multi-list screening matters

No single sanctions list captures all designations. A party may be on the UN list but not OFAC; on the EU list but not UK HMT; on the UAE EOCN list but not on any international list. A party connected to a MENA transaction must be screened against all lists that could give rise to legal liability or reputational risk.

| Jurisdiction of exposure | Required lists at minimum |
|---|---|
| UAE | OFAC + UN + EU + UK + UAE EOCN + OFSI |
| KSA | OFAC + UN + EU + UK + KSA NCASGS |
| Lebanon | OFAC + UN + EU + UK + BDL-SIC |
| Any USD-clearing transaction | OFAC (mandatory — US secondary sanctions risk) |
| Any EUR-clearing transaction | OFAC + EU |
| UK-nexus transaction | OFAC + EU + UK HMT OFSI |

## Sanctions lists

### OFAC (US Office of Foreign Assets Control)
- **SDN List** (Specially Designated Nationals and Blocked Persons): the most comprehensive US list; entities and individuals subject to full asset block
- **Sectoral Sanctions Identifications (SSI) List**: entities in specific Russian sectors subject to limited prohibitions (not full block)
- **Consolidated Sanctions List**: combines SDN + SSI + other OFAC lists
- **Key programs relevant to MENA**: Iran, Syria, Yemen, Sudan, Iraq, Lebanon (EO 13441), Global Terrorism (EO 13224), Non-Proliferation
- Access: [[tool-ofac-sanctions]] or ofac.treas.gov API

### UN Consolidated Sanctions List
- Maintained by the UN Security Council Sanctions Committee
- Covers ISIL (Da'esh), Al-Qaida, Taliban, Iran, North Korea, Sudan, Yemen, Libya, South Sudan programs
- Accessible via un.org/securitycouncil/sanctions/consolidated

### EU Consolidated Financial Sanctions List
- Published by the EU and updated continuously on the European External Action Service portal
- Covers all EU Council Regulation designations including Russia, Iran, Belarus, Syria, Sudan, and global terrorism
- Access: eeas.europa.eu/topics/sanctions-policy or [[tool-eu-sanctions]]

### UK HMT OFSI (Office of Financial Sanctions Implementation)
- UK autonomous sanctions regime post-Brexit; partially mirrors EU list but with UK-specific additions
- Access: gov.uk/government/publications/financial-sanctions-consolidated-list-of-targets

### KSA NCASGS (National Committee for Combating Money Laundering and Terrorism Financing)
- Saudi national terrorism and money-laundering designated-entities list
- Relevant for any transaction with a Saudi nexus; accessible via Saudi Ministry of Interior

### UAE EOCN (Executive Office of AML/CFT)
- UAE national list; Cabinet Decision No. 74 of 2020 requires UAE-licensed entities to screen against this list
- Populated by the UAE's domestic AML/CFT framework aligned with FATF
- Access: amlcft.gov.ae

### Lebanon BDL-SIC (Special Investigation Commission)
- Administers Lebanese AML/sanctions framework
- BDL Circular No. 83 and related circulars require banks to screen against international lists; SIC publishes domestic designations
- Lebanese banks are required by law to freeze assets of designated parties

## Match methodology

Effective sanctions screening requires more than an exact string match. The following matching signals should be applied in combination:

| Signal | Matching approach |
|--------|------------------|
| **Name** | Fuzzy matching + transliteration variants (Arabic ↔ English; Persian/Farsi variants; patronymic vs surname variations in Arabic names); AKA/alias matching from the list entries |
| **Date of birth** | Exact + ±2-year tolerance to account for document errors and deliberate obfuscation |
| **Place of birth** | Exact + regional/country-level match |
| **ID / passport number** | Exact match; normalize format (remove spaces, hyphens) before matching |
| **Address** | Match to registered or last known address; useful for confirming or excluding a candidate match |
| **Vessel IMO number** | Exact match; IMO number is the permanent vessel identifier |
| **Aircraft tail number** | Exact match |
| **Entity registration number** | Exact match; normalize jurisdiction format |

### Transliteration note — MENA names
Arabic names are frequently transliterated inconsistently across documents. "Mohamed" / "Muhammad" / "Mohammed" / "Mohamad" are all valid transliterations of the same Arabic name. The screening engine must use phonetic matching and all known variants in the sanctions list entry (most list entries include AKAs). Flag any near-match as a potential hit for human review — do not auto-clear on transliteration variation alone.

## Output schema

```json
{
  "subject": {
    "name": "string",
    "type": "natural-person | legal-entity | vessel | aircraft",
    "identifiers": {}
  },
  "hits": [
    {
      "name": "matched entry on list",
      "lists": [
        {
          "list": "OFAC-SDN | UN | EU | UK-OFSI | KSA-NCASGS | UAE-EOCN | BDL-SIC",
          "matchScore": number (0–100),
          "matchBasis": "name | dob | id | address | alias",
          "programs": ["program names, e.g., 'SDGT', 'Iran', 'Syria'"],
          "designationDate": "ISO date",
          "listReference": "URL or identifier"
        }
      ],
      "requiresEscalation": true,
      "escalationReason": "string"
    }
  ],
  "cleared": boolean,
  "screenedLists": ["list of all lists checked"],
  "screenedAt": "ISO timestamp",
  "screenedBy": "system | analyst-name",
  "expiresAt": "ISO timestamp (72 hours — re-screen before transaction executes)",
  "notes": "any match rationale or exclusion reasoning"
}
```

## Escalation rules

Any hit with `matchScore` ≥ 70 on any list requires immediate escalation to:
1. The compliance officer for the transaction / relationship
2. Legal counsel if the match involves the SDN list, UN list, or any full-asset-block program

**Do not proceed with the transaction** until the compliance officer or legal counsel has made a disposition decision. Document the decision with rationale.

For hits with `matchScore` 40–69: human review required before clearance. The screener must document the basis for clearing a near-match (e.g., "matched name but DOB and nationality do not match listed entity; two different individuals").

For hits with `matchScore` < 40: note in the screening record; clear with brief rationale.

## Periodic re-screening

Sanctions lists are updated daily. A cleared screen is not perpetually valid:
- For high-value or high-risk counterparties: re-screen monthly
- For ongoing client relationships in elevated-risk jurisdictions: re-screen quarterly at minimum
- **Always re-screen immediately before execution of any material transaction** — a party may have been designated between initial due diligence and closing

## Pairing with UBO screening

The most common sanctions-evasion technique is to hold assets through intermediary entities whose direct shareholders are not themselves sanctioned. The sanctioned party holds indirect ownership or control. **This skill must be paired with [[research-beneficial-ownership-lookup]]**: identify the UBOs first, then screen every UBO as well as the direct counterparty.

## Limits and escalation

- This skill screens against **published** lists. Sanctions evasion via complex structures, front companies, or undisclosed beneficial ownership may not be detected by list screening alone — UBO analysis and adverse media screening are complementary.
- Name matching is probabilistic. False positives are common for common Arabic names (e.g., "Ali Hassan," "Ahmed Abdullah"). The skill flags matches for human review; a human must make the final disposition decision.
- OFAC's secondary sanctions programs (Iran, Russia, etc.) can impose liability on non-US parties for transactions that do not touch the US directly but involve USD clearing or US persons. Legal counsel should advise on secondary sanctions exposure in MENA transactions involving Iran-connected parties.
- This skill does not constitute legal advice on sanctions compliance. For complex transactions, engage specialist sanctions counsel.

## Related skills

- [[research-beneficial-ownership-lookup]]
- [[review-compliance-gap-analysis]]
- [[kb-aml-kyc]]
- [[research-regulation-lookup]]
- [[research-regulator-guidance-lookup]]
