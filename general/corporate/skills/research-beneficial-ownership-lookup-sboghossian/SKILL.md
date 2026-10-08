---
name: research-beneficial-ownership-lookup-sboghossian
title: Beneficial Ownership (UBO) Lookup
description: Use when a lawyer, compliance officer, or KYC analyst needs to identify the ultimate beneficial owners (UBOs) of a company or structure — piercing through nominee shareholders, holding vehicles, and trust arrangements to identify natural persons with ≥ 25% ownership or equivalent control. Covers MENA (UAE, KSA, Lebanon, Egypt, BVI/Cayman offshore structures common in the region), UK, and EU registries. Integrates sanctions screening and known-nominee cross-checks.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/research/research-beneficial-ownership-lookup
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Beneficial Ownership (UBO) Lookup

Systematic research skill for identifying natural-person ultimate beneficial owners behind corporate structures, nominee arrangements, and multi-tier holding vehicles. Used in KYC onboarding, AML due diligence, transaction clearance, and regulatory filings.

## When to use this

- **KYC / CDD onboarding**: a new client is a legal entity; the firm must identify the natural persons behind it.
- **Transaction due diligence**: buyer, seller, or counterparty is a company whose owners are unclear.
- **Sanctions pre-check**: sanctions lists target natural persons and specific entities; you need to know who ultimately controls the entity being screened.
- **Regulatory filing**: many MENA jurisdictions now require UBO disclosure in licensing applications, real-estate transactions, and banking relationships.
- **Litigation / enforcement**: tracing asset-holding structures for freezing orders, garnishments, or enforcement actions.

## Inputs

| Input | Why it matters | Default |
|-------|---------------|---------|
| Entity name (full legal name) | Starting point for registry searches | Required |
| Jurisdiction of incorporation | Determines which registry and filing regime applies | Required |
| Registry number / commercial number | Speeds up registry search, avoids false matches | Provide if known |
| Free-zone or onshore? (UAE) | Separate registries for DIFC, ADGM, JAFZA, etc. | Infer from jurisdiction context |
| Threshold for reporting | Ownership % that triggers UBO identification | Default: 25% (FATF standard) |
| Depth of search | Stop at direct shareholders, or recurse through all intermediaries? | Recurse to natural person or until path is blocked |

## Research methodology

### Step 1 — Primary registry search

Pull the current register of members / shareholders from the jurisdiction's authoritative registry:

| Jurisdiction | Registry | What it shows | Accessibility |
|---|---|---|---|
| **UK** | Companies House — PSC (Persons with Significant Control) register | Natural persons or entities with > 25% shares, voting rights, or control | Public, free API |
| **UAE (onshore)** | DED (Dubai) or ADDED (Abu Dhabi) commercial register; MOE for federal | Shareholders, capital percentages | Partial public access; full via filing agent |
| **UAE DIFC** | DIFC Companies register (DIFC Authority) | Share register, ultimate controller disclosure | Public registry search |
| **UAE ADGM** | ADGM Companies Authority | Beneficial ownership register (2023 regulations) | Public search |
| **KSA** | Ministry of Commerce (MOC) Qiyas system; CCHI for commercial register | Shareholders, capital | Accessible via MOC portal (Arabic) |
| **Lebanon** | Commercial Register (Registre du Commerce), Beirut / per-court registries | Partners, shares | In-person or certified-agent access; often incomplete |
| **Egypt** | GAFI (General Authority for Investment and Free Zones) + Commercial Registry | Shareholders | Arabic portal |
| **BVI** | Beneficial Ownership Secure Search System (BOSS) | Natural-person UBOs filed with Registered Agent | **Not public** — requires filing agent cooperation or court order |
| **Cayman** | CIMA / CORIS registry | UBO register held by registered agent | **Not public** — requires filing agent or regulatory gateway |
| **EU (public)** | National UBO registers (e.g., French RNE / infogreffe, German Transparenzregister) | 25%+ beneficial owners | Variable public access; EU Directive 2018/843 harmonized but implementation varies |

### Step 2 — Recursive entity resolution

For each shareholder identified:
1. **Is it a natural person?** → Add to UBO list with ownership percentage and path.
2. **Is it a legal entity?** → Identify the jurisdiction of that entity and repeat Step 1 for it.
3. **Is it a trust or foundation?** → Identify settlor, trustee, protector, and named beneficiaries. All may qualify as UBOs under FATF guidance depending on control.
4. **Is it a nominee?** → Flag; apply nominee cross-check (Step 3).
5. **Is it an unknown or dissolved entity?** → Flag as `unresolved node`; escalate to compliance officer.

Recurse until either a natural person is identified at every branch, or the path is blocked and flagged.

### Step 3 — Nominee and leak cross-check

Cross-reference all identified intermediary entities and nominee directors/shareholders against known-nominee exposure databases:
- ICIJ Offshore Leaks database (Panama Papers, Paradise Papers, Pandora Papers, Bahamas Leaks)
- Commercial nominee-director red flags: Mossack Fonseca-affiliated structures, known BVI shelf-company factories
- Common patterns: single registered office managing hundreds of entities in BVI/Cayman; circular shareholding; same individual as director across dozens of unrelated companies.

**Important**: Presence in the ICIJ database does not itself establish wrongdoing — it indicates use of offshore structures. Escalate to human review when a nominee match is found.

### Step 4 — Control pathways beyond direct shareholding

Legal ownership > 25% is the bright-line threshold, but UBO analysis must also consider:
- **Voting agreements**: shareholder agreements that give one party voting control beyond their shareholding percentage
- **Options and warrants**: future ownership rights may trigger notification obligations
- **Convertible instruments**: SAFEs, convertible notes that convert to shares above the threshold
- **De facto control**: board majority, veto rights, right to appoint / remove management
- **Beneficial interest through trust / foundation**: the settlor who retains effective control

FATF Recommendation 10 and most MENA UBO regulations include control-based UBO identification, not just ownership.

## Output schema

```json
{
  "rootEntity": {
    "name": "string",
    "jurisdiction": "string",
    "registryNumber": "string",
    "asOfDate": "ISO date"
  },
  "ubos": [
    {
      "name": "string",
      "nationality": "string (if available)",
      "percentageDirect": number,
      "percentageUltimate": number,
      "pathToRoot": ["Entity A → Entity B → Root Entity"],
      "controlBasis": "shares | voting | control | trust-settlor | option",
      "nomineeFlag": boolean,
      "leaksDatabaseHit": boolean,
      "confidence": "high | medium | low",
      "confidenceBasis": "string"
    }
  ],
  "unresolvedNodes": [
    {
      "entityName": "string",
      "jurisdiction": "string",
      "blockerReason": "no-public-register | dissolved | nominee-uncooperative | BVI-private | other",
      "escalationRequired": true
    }
  ],
  "screeningRecommendation": "run [[research-sanctions-screening]] on all identified UBOs"
}
```

## Jurisdictional notes

### UAE
- Onshore companies must file UBO registers with the relevant licensing authority (Cabinet Decision No. 58 of 2020). Threshold: 25% ownership or control.
- DIFC: Beneficial ownership disclosure under DIFC Companies Law. DFSA-regulated entities have additional FATF-aligned CDD obligations.
- ADGM: Enhanced UBO register introduced 2023 under Companies Regulations.
- Free zones vary: JAFZA, DMCC, DAFZA each have their own UBO forms and filing timelines.

### KSA
- Anti-Money Laundering Law (Royal Decree M/20 of 2003, as amended) and SAMA AML guidelines require CDD including UBO identification.
- MOC commercial register increasingly captures beneficial ownership but gaps remain for complex holding structures.
- Foreign investment structures often use BVI/Cayman holding; cross-border cooperation required.

### Lebanon
- Banking secrecy law (Law 3/1956) is among the most restrictive globally — bank records are protected even from Lebanese courts in most circumstances. UBO tracing through Lebanese banks is highly constrained.
- Commercial Register records are incomplete and may not reflect recent changes.
- Special Investigation Commission (SIC) at the BDL handles AML matters; disclosure to SIC is required for suspicious transaction reports.

### BVI / Cayman (structures common in MENA)
- Beneficial ownership information is not publicly accessible. The BOSS system (BVI) and CIMA register (Cayman) are accessible to financial intelligence units and law enforcement via treaty gateway — not to private parties.
- Client-side: only obtain UBO information via the registered agent acting on instructions from the entity itself, or via court-ordered disclosure.

## Common mistakes

1. **Stopping at the first legal-entity shareholder** without recursing to natural persons.
2. **Treating legal ownership as sole determinant of control** — missing voting agreements and de facto control.
3. **Ignoring trust structures** — trusts do not appear in commercial registries; they require separate document requests.
4. **Accepting a certificate of incumbency from a nominee at face value** without cross-checking against known-nominee databases.
5. **Not re-running UBO searches periodically** — ownership structures change; a quarterly refresh is good practice for ongoing client relationships.

## Limits and escalation

This skill can structure the research process and interpret results, but:
- **Cannot compel disclosure** from secretive jurisdictions (BVI, Cayman, Delaware LLC).
- **Cannot access closed registries** without the cooperation of the entity or a legal order.
- If UBO identification is incomplete and the transaction is high-value or high-risk, a compliance officer or lawyer must decide whether to proceed, seek additional assurances, or decline.
- Always pair this output with [[research-sanctions-screening]] — UBO identification is only the first half of AML/KYC due diligence.

## Related skills

- [[research-sanctions-screening]]
- [[review-compliance-gap-analysis]]
- [[kb-aml-kyc]]
- [[research-regulation-lookup]]
- [[research-regulator-guidance-lookup]]
