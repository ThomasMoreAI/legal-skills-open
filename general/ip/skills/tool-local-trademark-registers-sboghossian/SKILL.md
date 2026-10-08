---
name: tool-local-trademark-registers-sboghossian
title: MENA Local Trademark Registers
description: Use when performing trademark clearance, conflict checks, or portfolio monitoring in MENA jurisdictions where WIPO's Global Brand Database does not capture purely national filings. Queries the local trademark registers of KSA (SAIP), UAE (Ministry of Economy), Egypt (EPO), Lebanon (MoE), and other GCC national offices. Always pair with WIPO search for Madrid System and international registrations. Triggers on IP clearance, brand registration, or trademark watching requests for MENA markets.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/tool/tool-local-trademark-registers
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
---

# MENA Local Trademark Registers

## What it does

This tool queries the national trademark registers of MENA jurisdictions for marks that are registered only domestically and therefore not captured by WIPO's Global Brand Database. In the MENA region, a significant portion of trademark filings — especially by local companies and SMEs — are made through national IP offices without filing an international application under the Madrid System.

**When a WIPO search is insufficient**: A WIPO search covers international registrations designating a jurisdiction. It does not show marks filed and registered purely at the national level through the domestic procedure. For a complete clearance opinion in any MENA jurisdiction, both searches are mandatory.

## Register overview by jurisdiction

### KSA — Saudi Authority for Intellectual Property (SAIP)
- **URL**: https://saip.gov.sa
- **Search interface**: Arabic-primary; English transliteration search available for word marks
- **Coverage**: All marks registered or applied for in Saudi Arabia (both national filings and Madrid System designations)
- **Nice classes**: All 45 classes
- **Opposition window**: 30 days from gazette publication in Umm Al-Qura
- **Term**: 10 years, renewable
- **Language of register**: Arabic; English names are shown where provided
- **API**: Limited programmatic access; primarily web scraping

### UAE — Ministry of Economy (Trademark Section)
- **URL**: https://www.moec.gov.ae (Trademark Registration portal)
- **Search interface**: English + Arabic; web-based; no open API
- **Coverage**: Mainland UAE filings; does **not** cover free zone–specific registrations
- **Nice classes**: All 45 classes
- **Opposition window**: 30 days from Federal Gazette publication
- **Term**: 10 years, renewable
- **Free zone note**: DIFC and JAFZA do not maintain separate trademark registers; mainland UAE registration suffices for free zone use

### Egypt — Egyptian Patent Office (EPO) / Trademark Division
- **URL**: https://www.egipat.sci.eg (Egyptian Patent Office)
- **Search interface**: Limited web search; Arabic-only for many records
- **Coverage**: All Egyptian national trademark filings
- **Nice classes**: All 45 classes
- **Opposition window**: 60 days from publication in the Official Gazette
- **Term**: 10 years, renewable
- **Key feature**: Egypt has a trademark watching service via private agents; direct API access is limited

### Lebanon — Ministry of Economy and Trade (MoE)
- **URL**: https://www.economy.gov.lb
- **Search interface**: Basic; Arabic + French; often requires in-person or agent search for definitive results
- **Coverage**: Marks filed at the MoE IP department
- **Nice classes**: All 45 classes
- **Opposition window**: 30 days from Official Gazette (al-Jarida al-Rasmiyya)
- **Term**: 15 years (Lebanon), renewable
- **Data freshness**: Backend system is inconsistently updated; physical file inspection at the MoE is recommended for critical matters

### Bahrain — BCIP (Bahrain Center for Intellectual Property)
- **URL**: https://www.bcip.gov.bh
- **Search**: English + Arabic; web portal search available
- **Term**: 10 years, renewable; 6-month opposition window from gazette

### Kuwait — Ministry of Commerce and Industry (Patents & Trademarks Department)
- **URL**: https://www.moci.gov.kw
- **Search**: Arabic-primary; limited English search
- **Term**: 10 years, renewable

### Oman — Ministry of Commerce, Industry and Investment Promotion (Trademark Division)
- **URL**: https://www.mociip.gov.om
- **Search**: Arabic + English; web portal search
- **Term**: 10 years, renewable

### Qatar — Trademark Department, Ministry of Commerce and Industry
- **URL**: https://www.moci.gov.qa
- **Search**: Arabic + English
- **Term**: 10 years, renewable

## Setup / auth

Most MENA national IP offices do not expose public APIs. The tool operates through:
1. **Programmatic web scraping** where terms of service permit
2. **Agent network integration** — for tenants with relationships with in-country IP agents, the tool can dispatch a search request and ingest the returned report
3. **Manual upload** — where the user's agent provides a search certificate, the tool parses and indexes it

| Parameter | Description | Required |
|-----------|-------------|----------|
| `markText` | Word mark or transliteration to search | Yes for word marks |
| `niceClasses` | Comma-separated class numbers (e.g., "9,35,42") | Recommended |
| `jurisdiction` | One or more MENA jurisdiction codes | Yes |
| `deviceMark` | Image file for device mark search | Conditional |
| `proprietorName` | Owner name for portfolio lookup | Conditional |

## Capabilities

### Clearance search
```
Input:  {
  markText: "NOVA",
  niceClasses: [9, 35, 42],
  jurisdictions: ["KSA", "UAE", "EG"]
}
Output: {
  KSA: { hits: [...], pending: [...], gaps: [...] },
  UAE: { hits: [...], pending: [...], gaps: [...] },
  EG:  { hits: [...], pending: [...], gaps: [...] }
}
```

Each hit includes: mark text/image, owner, Nice classes, status, filing date, registration date, expiry date, and register URL.

### Portfolio watch
Monitor registered marks for similar new filings:
```
Input:  { markText: "NOVA", niceClasses: [9], watchJurisdictions: ["KSA", "UAE"] }
Output: New applications in gazette since last watch date
```

### Opposition deadline tracker
For marks currently in the opposition window — calculate opposition filing deadlines per jurisdiction.

## Arabic script search considerations

Word marks in Arabic require special handling:
- **Transliteration variants**: "محمد" can be transliterated as Muhammad, Mohammed, Mohammad — search all variants
- **Root/stem matching**: Arabic morphology means "عمل" (work) and "أعمال" (business) share a root; semantic similarity must be checked
- **Bilingual marks**: A mark filed in both Arabic and Latin script needs both searched
- **Diacritics (tashkeel)**: Marks are usually filed without diacritics; search with and without

## Nice Class quick-reference for MENA filings

The following Nice classes are most frequently relevant in MENA transactions:

| Class | Coverage | Common MENA context |
|-------|----------|---------------------|
| 9 | Software, apps, electronics | Tech / fintech startups |
| 35 | Business services, advertising | Management consulting |
| 36 | Financial, insurance | Banks, financial services |
| 41 | Education | EdTech |
| 42 | Technology services, SaaS | Cloud / IT |
| 43 | Hospitality, food | F&B, hotels |
| 45 | Legal services, security | Law firms |

## Clearance opinion workflow

A complete MENA trademark clearance typically involves:
1. **WIPO search** via [[tool-wipo-trademark-search]] — captures Madrid registrations
2. **National register searches** via this tool — captures domestic-only filings
3. **Common law / unregistered mark check** — web search for prior business use
4. **Distinctiveness analysis** — assess inherent registrability
5. **Risk matrix** — color-coded by class and jurisdiction
6. **Clearance opinion** — draft the legal opinion or memo

## Permissions & safety

- Search results are advisory; always confirm with an in-country trademark agent for filing or opposition decisions.
- Do not represent a clearance search as exhaustive unless both WIPO and all relevant national registers have been queried.
- Device (image) mark searches are approximate — similarity analysis for device marks requires visual assessment and should be escalated to an IP attorney.

## Failure modes

| Failure | Symptom | Resolution |
|---------|---------|------------|
| No API / scraping blocked | Empty result | Route to agent network; flag to user |
| Arabic encoding error | Garbled Arabic text | Use UTF-8 encoding; try transliteration search |
| Register maintenance | Offline | Retry; note timestamp gap in report |
| Outdated data | Results lag by days/weeks | Confirm with in-country agent for pending applications |

## Related skills

- [[tool-wipo-trademark-search]] — Madrid System and international registration search; always pair with this tool
- [[research-precedent-finder]] — trademark opposition decisions and MENA IP case law
- [[draft-trademark-assignment]] — draft the assignment agreement once clearance is confirmed
