---
name: connector-ofac-sanctions-sboghossian
title: Connector — OFAC Sanctions
description: Use when a legal or compliance workflow requires screening an individual, entity, vessel, or aircraft against the OFAC Specially Designated Nationals (SDN) list and OFAC consolidated sanctions programs. The list is public, updates daily, and can be queried without authentication. Triggers on any KYC/AML screening request, counterparty due diligence involving a US-nexus transaction, sanctions compliance check, or any request to verify whether a named party appears on US sanctions lists. Relevant globally — not only for US-law matters.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/connector/connector-ofac-sanctions
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: sanctions
language: en
---

# Connector — OFAC Sanctions

## What it does

The OFAC Sanctions connector queries the US Treasury Department's Office of Foreign Assets Control (OFAC) Specially Designated Nationals (SDN) list and OFAC's other sanctions programs in real time. It allows the legal-AI platform to perform automated sanctions screening as part of KYC/AML workflows, counterparty due diligence, and cross-border transaction compliance checks.

OFAC administers US economic and trade sanctions against targeted foreign countries, entities, and individuals. Transactions that benefit an SDN are prohibited regardless of where the transaction occurs — US dollar transactions and USD correspondent banking create a global reach.

## Setup / auth

**No authentication required.** The OFAC SDN list is publicly available data. The connector uses OFAC's Data Services API (`sanctionslist.ofac.treas.gov/api`):

- No API key needed.
- Rate limit: respect Treasury guidance (no more than 1 request/second in practice).
- The connector maintains a **local cached copy** of the SDN list, refreshed every hour (cache TTL: 1h). Real-time API queries are used for final verification only.
- The SDN XML data file is approximately 15MB; the SCSN (non-SDN Consolidated Sanctions) file adds further volume.

## OFAC list structure

OFAC administers multiple lists:

| List | Coverage |
|---|---|
| SDN (Specially Designated Nationals) | Individuals and entities blocked under all sanctions programs |
| Consolidated Sanctions (non-SDN) | Non-SDN parties subject to program-specific restrictions (e.g., foreign sanctions evaders, debt/equity restrictions) |
| Sectoral Sanctions (SSI) | Russian entities subject to capital market / debt restrictions (not necessarily full blocking) |
| Foreign Sanctions Evaders (FSE) | Non-US persons who have evaded US sanctions |
| Palestinian Legislative Council (PLC) | |

For most KYC/AML workflows, the SDN list is the primary check. For sophisticated cross-border transactions with Russia, Iran, or Venezuela nexus, check the SSI list as well.

## Capabilities

| Capability | Description |
|---|---|
| SDN name search | Match a name against the SDN list (fuzzy matching supported) |
| Entity search by country | Filter SDN entries by country of origin |
| Program filter | Filter by sanctions program (IRAN, SYRIA, SDN, UKRAINE, etc.) |
| ID match | Match by passport number, registration number, IMO vessel number |
| Vessel and aircraft search | OFAC includes named vessels and aircraft |
| Address matching | Partial address search for entity verification |
| Alias search | Checks all known aliases (AKA/FKA) for a name |
| Date of last update | Returns when the SDN entry was last modified |

## Usage patterns

### Pattern 1 — Counterparty screening before contract execution

```
User: "Screen Al-Rashid Trading LLC before we sign the distribution agreement"
→ Search SDN list for "Al-Rashid Trading"
→ Also check: known directors from corporate registry against SDN
→ Return: MATCH / PARTIAL MATCH / NO MATCH + program name if matched
→ If PARTIAL MATCH: flag for human review; do not clear automatically
```

### Pattern 2 — KYC intake for a new client

When onboarding a new client (individual or entity):
1. Screen the client name and aliases against the SDN list.
2. Screen the UBO (ultimate beneficial owner) if identified from corporate registry.
3. Screen any nominees or proxies if disclosed.
4. Log the screening result with timestamp to the client's KYC file.

### Pattern 3 — Transaction monitoring trigger

For a cross-border payment instruction:
- Screen the beneficiary name and account details.
- Screen the beneficiary's bank (correspondent banking sanctions risk).
- If the payment is denominated in USD, OFAC applies regardless of the parties' jurisdictions.

### Pattern 4 — Vessel and cargo screening

For trade finance or shipping-related legal work:
- Screen vessel name and IMO number against OFAC.
- OFAC's maritime sanctions (North Korea, Iran, Venezuela, Russia) target specific vessels and their operators.

## MENA context — why OFAC matters beyond US law

OFAC's extraterritorial reach is critical for MENA practitioners:

1. **USD transactions.** Any transaction settled in USD passes through a US correspondent bank, giving OFAC jurisdiction. This applies to virtually all international commercial transactions in the region.

2. **Iran sanctions.** Lebanon, UAE, and other MENA jurisdictions are geographically proximate to Iran. OFAC's Iran sanctions program (CISADA, IFCA, IEEPA) impose secondary sanctions risk on non-US entities that transact with Iran.

3. **Lebanese political and financial figures.** Following the 2019 Lebanese financial crisis and subsequent US executive orders, several Lebanese political and financial figures have been designated. OFAC screening is now standard practice for any Lebanon-related transaction.

4. **UAE as a transshipment hub.** OFAC has flagged the UAE (particularly Dubai) as a potential transshipment point for Iran-linked goods. Due diligence for UAE-based counterparties should include verification that the ultimate beneficiary is not Iran-linked.

5. **KSA and the Yemen conflict.** Houthi-related designations are active OFAC sanctions programs. KSA-nexus transactions with Yemeni counterparties require screening.

## EU sanctions note

OFAC covers US sanctions only. EU sanctions (including EU Russia sanctions, Syria sanctions, Iran sanctions, and the UN consolidated list as adopted by the EU) are **separate** and published in the Official Journal via [[connector-eur-lex]]. Always check both OFAC and EU sanctions for MENA cross-border transactions with European parties.

Similarly, UN Security Council sanctions lists (UNSC consolidated list) are adopted into DIFC/ADGM regulations and UAE federal law — these require a separate check.

## Permissions & safety

- **No autonomous clearance.** A "no match" result from the SDN list does not mean a party is sanctions-free — it means they are not on OFAC's SDN list. Always include a disclaimer.
- **Partial matches require human review.** A fuzzy match (e.g., name similarity >70%) must be escalated to a compliance officer. Never auto-clear a partial match.
- **Audit trail mandatory.** Every sanctions screen must be logged with: screened party name, list version date, result, and actor. This log is a legal compliance record.
- **Not a substitute for full KYC.** OFAC screening is one layer of a full KYC/AML process. Additional layers (PEP screening, adverse media, source of funds) are outside the scope of this connector.
- **Cache freshness.** Always note the cache timestamp when returning a result. If the last cache refresh was >4 hours ago, trigger a fresh API call before returning a clean result for a high-risk transaction.

## Failure modes

| Failure | Cause | Resolution |
|---|---|---|
| OFAC API unavailable | Treasury infrastructure maintenance | Fall back to cached list; flag that result is based on cache dated [timestamp] |
| Name transliteration issue | Arabic name transliterated inconsistently | Run multiple transliteration variants; flag for manual review |
| Overly broad match | Common name (e.g., "Mohamed Al-Hassan") returns many results | Require additional identifiers (nationality, DOB, company reg. number) before concluding match |
| SDN entry removed | Party previously designated, now delisted | Confirm against current list; note delisting date in compliance file |

## Related skills

- [[connector-companies-house-uk]]
- [[connector-legal-data-hunter]]
- [[connector-eur-lex]]
- [[connector-wipo-trademark]]
