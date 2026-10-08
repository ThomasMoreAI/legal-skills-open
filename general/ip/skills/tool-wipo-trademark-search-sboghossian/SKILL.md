---
name: tool-wipo-trademark-search-sboghossian
title: WIPO Trademark Search — Global Brand Database
description: Use when searching for trademarks registered under the Madrid System (international registrations) or in the national databases that feed into WIPO's Global Brand Database. Covers word marks, device marks, sound marks across Nice classes 1–45 with designation-territory filtering. Always the first step in trademark clearance; must be paired with national MENA register searches for a complete clearance opinion, as the WIPO database does not capture purely domestic filings.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/tool/tool-wipo-trademark-search
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
---

# WIPO Trademark Search — Global Brand Database

## What it does

This tool queries the WIPO Global Brand Database (branddb.wipo.int) — the world's most comprehensive trademark database, aggregating Madrid System international registrations plus national office contributions from over 60 countries.

It is the mandatory first step in any trademark clearance exercise. For MENA clients launching or expanding a brand, a WIPO search identifies:
- Registered marks that could block registration in target markets
- Active oppositions or refusals on pending applications
- Lapsed or cancelled marks that may be available for registration or licensing
- Existing owners whose consent or assignment might be needed

## Coverage

### Madrid System registrations
The Madrid System (administered by WIPO under the Madrid Agreement and Protocol) allows a single international trademark application to designate protection in up to 130+ member states. All Madrid registrations and their designated territories are searchable in the Global Brand Database.

### Contributing national offices
WIPO feeds from national offices include — with varying completeness:
- US (USPTO), EU (EUIPO), UK (UKIPO)
- France (INPI), Germany (DPMA), Italy (UIBM)
- China (CNIPA), Japan (JPO), South Korea (KIPO)
- **MENA**: UAE (Ministry of Economy — partial feed), KSA (SAIP — partial feed), Egypt (EPO — partial feed), Morocco (OMPIC), Tunisia (INNORPI)
- Australia (IP Australia), Canada (CIPO), India (CGPDTM)
- Brazil (INPI-BR)

**Important caveat**: national office feeds to WIPO are incomplete in MENA. Saudi SAIP, UAE MoE, and Egypt EPO feed only a subset of their registered marks. Always supplement with [[tool-local-trademark-registers]] for complete national clearance.

## Setup / auth

WIPO's Global Brand Database offers a public API:

| Parameter | Description | Required |
|-----------|-------------|----------|
| `wipoApiKey` | WIPO API key (obtainable from WIPO's developer portal) | Recommended |
| `markText` | Word mark text to search | Conditional |
| `deviceMark` | Image file for device/figurative mark search | Conditional |
| `niceClasses` | Nice class numbers (1–45) | Recommended |
| `jurisdictions` | Designation territories to filter by | Optional |
| `owner` | Owner/applicant name for portfolio lookup | Optional |
| `status` | `registered` / `pending` / `lapsed` / `all` | Default: `all` |

Public access is available without an API key at reduced rate limits.

## Capabilities

### Word mark search
```
Input:  {
  markText: "NOVA",
  niceClasses: [9, 35, 42],
  jurisdictions: ["AE", "SA", "EG"],
  status: "registered"
}
Output: {
  totalResults: 47,
  marks: [
    {
      markId: "1234567",
      markText: "NOVA",
      markType: "word",
      owner: "Nova Technologies Inc",
      ownerCountry: "US",
      niceClasses: [9, 42],
      status: "Registered",
      priorityDate: "2018-03-15",
      registrationDate: "2019-11-01",
      designations: ["AE", "SA", "EG", "QA", "KW"],
      imageUrl: null,
      wipoUrl: "https://branddb.wipo.int/..."
    }
  ]
}
```

### Device / figurative mark search
```
Input:  { deviceMark: <image_file>, niceClasses: [43], jurisdictions: ["AE"] }
Output: [ { mark, owner, visualSimilarityScore, ... } ]
```
Visual similarity search uses WIPO's AI-based image comparison. Results are ordered by similarity score; marks with score > 0.7 should be reviewed by an IP attorney.

### Owner / applicant portfolio search
```
Input:  { owner: "Al Rawabi UAE", jurisdictions: ["AE"] }
Output: [ { markText, classes, status, designations, filingDate } ]
```
Returns all registrations held by a specific owner — useful for competitor monitoring and prior art investigation.

### Opposition / refusal status
For pending applications, check whether an opposition has been filed:
```
Input:  { markId: "1234567" }
Output: { oppositions: [{ opposer, filedDate, grounds, status }], refusals: [...] }
```

## Nice Classification reference

| Class range | Category | Common MENA business sectors |
|---|---|---|
| 1–5 | Chemicals, pharmaceuticals | Pharma, agro |
| 6–11 | Hardware, machinery, electronics | Manufacturing |
| 12–14 | Vehicles, jewelry, instruments | Automotive, luxury retail |
| 16 | Paper goods, printed matter | Publishing |
| 25 | Clothing, footwear | Fashion |
| 28 | Games, toys, sports | Entertainment |
| 29–34 | Food, beverages, tobacco | F&B, hospitality |
| 35 | Advertising, business services | Consulting, retail |
| 36 | Financial, insurance | Banks, fintech |
| 38 | Telecommunications | Telco |
| 41 | Education, entertainment | EdTech |
| 42 | Technology services, research | SaaS, cloud |
| 43 | Food and beverage services | Restaurants, hotels |
| 44 | Medical, beauty services | Healthcare, wellness |
| 45 | Legal, security, personal services | Law firms |

Always search all classes in which the mark is used or intended to be used, plus adjacent classes.

## MENA-specific Madrid System notes

All MENA/GCC states are Madrid Protocol members:
- UAE (acceded 1996), KSA (acceded 2007), Jordan (acceded 1999), Egypt (acceded 2009), Morocco (acceded 1917/1999), Algeria (acceded 1972), Tunisia (acceded 1892/1997), Bahrain (acceded 2005), Qatar (acceded 2006), Kuwait (acceded 2014), Oman (acceded 2007), Lebanon (acceded 1999)

**Refusal windows**: each national office has 12 or 18 months after receiving a WIPO notification to issue a provisional refusal. If no refusal is issued within that window, the mark is considered registered in that territory.

**Common MENA refusal grounds**:
- Descriptiveness or lack of distinctiveness (especially in Arabic)
- Similarity to existing national mark (not captured in WIPO)
- Cultural or religious sensitivity under local law (KSA and UAE regulators can refuse marks on moral grounds)
- Prohibited goods/services in the jurisdiction (e.g., alcohol-related classes in KSA)

## Trademark watching

After a mark is registered, ongoing clearance monitoring detects potential infringers:
```
Input:  { markText: "NOVA", watchClasses: [9, 42], watchJurisdictions: ["AE", "SA"] }
Schedule: weekly automated check for new filings similar to "NOVA"
Output: Alert when a new application with similarity score > 0.8 is filed
```

## Clearance workflow

A complete trademark clearance for MENA markets:

1. **WIPO Global Brand Database search** (this tool) — Madrid System + national feeds
2. **National MENA register searches** ([[tool-local-trademark-registers]]) — catches national-only filings
3. **Common law / unregistered mark check** — web search for business names, domain registrations
4. **Distinctiveness analysis** — is the mark inherently registrable in each jurisdiction?
5. **Risk matrix** — likelihood of confusion analysis per conflicting mark
6. **Opposition risk assessment** — are there large brand owners in the space who might oppose?
7. **Clearance opinion** — written opinion or memo for client

## Output schema

```json
{
  "searchId": "wipo-2026-05-14-001",
  "query": { "markText": "NOVA", "classes": [9, 35, 42], "jurisdictions": ["AE", "SA"] },
  "totalResults": 47,
  "marks": [...],
  "searchDate": "2026-05-14T10:00:00Z",
  "coverage": {
    "AE": "partial — UAE MoE feed incomplete; supplement with national search",
    "SA": "partial — SAIP feed incomplete; supplement with national search"
  },
  "warnings": [
    "UAE and KSA feeds to WIPO are incomplete. Always pair with tool-local-trademark-registers."
  ]
}
```

## Failure modes

| Failure | Symptom | Resolution |
|---------|---------|------------|
| API rate limit | 429 from WIPO API | Backoff; WIPO limits to 10 requests/second |
| Image search unavailable | Visual search error | Fall back to word mark search; note limitation |
| Arabic mark not found | Zero results on Arabic search | Try Latin transliteration; supplement national search |
| Partial national data | "partial" coverage flag | Always run [[tool-local-trademark-registers]] for MENA |

## Related skills

- [[tool-local-trademark-registers]] — national MENA registers; mandatory complement to WIPO search
- [[research-precedent-finder]] — trademark opposition decisions and precedent analysis
- [[draft-trademark-assignment]] — drafting trademark assignment agreements post-clearance
