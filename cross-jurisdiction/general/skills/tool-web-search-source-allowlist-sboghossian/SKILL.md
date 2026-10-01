---
name: tool-web-search-source-allowlist-sboghossian
title: Web Search Source Allowlist
description: Use when configuring or consulting the per-tenant list of trusted web sources that the web search orchestrator is permitted to query or cite. Defines which domains are considered authoritative for which jurisdiction and source type. Reduces hallucination and citation of unreliable sources by restricting web search results to pre-approved government, regulator, court, and publisher domains. Configurable at tenant level to add firm-specific trusted sources.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/tool/tool-web-search-source-allowlist
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: general
language: en
---

# Web Search Source Allowlist

## What it does

This tool manages the per-tenant configuration of trusted source domains for web searches. By restricting which websites the [[tool-web-search-orchestrator]] can query and cite, it reduces the risk of sourcing from unreliable, outdated, or legally irrelevant websites — a primary mechanism for preventing hallucination and citation errors in legal research.

The allowlist is not a wall — it is a priority and filter system. Sources on the list are queried preferentially; sources not on the list are queried only as a last resort and are returned with a lower confidence flag.

## Why this matters

Legal research requires source quality standards that general-purpose web search does not enforce. A legal AI that cites a Reddit thread, a Wikipedia article, or a law student blog as authority is dangerous. The allowlist operationalizes professional source standards.

Common failures this prevents:
- Citing an unofficial "explainer" blog for statute text (the statute may have been amended since the blog was written)
- Using a news article as the source for a regulatory requirement (the article may have mischaracterized the regulation)
- Citing a forum post as support for a legal proposition
- Using a law firm client alert as a primary source when the underlying regulation should be cited directly

## Default allowlist structure

The default allowlist is organized by source tier and jurisdiction. Tenants can add, remove, or reprioritize entries.

### Tier 1 — Official government and courts (always trusted)

| Domain | Jurisdiction | Content |
|--------|-------------|---------|
| uqn.gov.sa | KSA | Umm Al-Qura official gazette |
| mc.gov.sa | KSA | Ministry of Commerce |
| sama.gov.sa | KSA | Saudi Central Bank |
| cma.org.sa | KSA | Capital Markets Authority |
| moj.gov.ae | UAE | Ministry of Justice / Federal Gazette |
| centralbank.ae | UAE | CBUAE |
| difccourts.ae | DIFC | DIFC Courts |
| adgmcourts.com | ADGM | ADGM Courts |
| difc.ae | DIFC | DIFC Authority |
| adgm.com | ADGM | ADGM Authority |
| economy.gov.lb | LB | Lebanon Ministry of Economy |
| bdl.gov.lb | LB | Banque du Liban |
| legifrance.gouv.fr | FR | French official legal text |
| legislation.gov.uk | UK | UK legislation |
| bailii.org | UK | British and Irish case law |
| eur-lex.europa.eu | EU | EU legislation and case law |
| sec.gov | US | SEC EDGAR |
| courtlistener.com | US | US federal case law |
| supremecourt.gov | US | US Supreme Court |
| wipo.int | Int'l | WIPO — international IP |

### Tier 2 — Established legal publishers (trusted secondary sources)

| Domain | Content | Notes |
|--------|---------|-------|
| practicallaw.thomsonreuters.com | Practical Law (TR) | Premium; subscription required |
| lexisnexis.com | LexisNexis | Premium; subscription required |
| westlaw.com | Westlaw | Premium; subscription required |
| kluwerlawonline.com | Kluwer — int'l commercial law | Academic / practitioner |
| iflr.com | IFLR | Finance and banking law |
| out-law.com | Pinsent Masons | Reliable practitioner commentary |
| globallegalgroup.com | Getting the Deal Done | Country guides |
| iclg.com | ICLG | Comparative law guides |

### Tier 3 — Bar associations and professional bodies

| Domain | Content |
|--------|---------|
| lawsociety.org.uk | Law Society (England and Wales) |
| americanbar.org | American Bar Association |
| barreau.fr | French Bar (Barreau de Paris) |
| saudibar.org.sa | Saudi Bar Association |

### Tenant-configurable additions

A tenant can add firm-specific trusted sources:
- Their own website (for published legal guides)
- Specific law firm sites they consider authoritative (e.g., Al Tamimi for UAE, Hadef for DIFC, Audi for Lebanon)
- Subscription services the firm has licensed
- Academic institutions specific to their practice areas

## Configuration schema

```json
{
  "tenantId": "tenant-xyz",
  "allowlist": {
    "tier1": [
      { "domain": "sama.gov.sa", "jurisdiction": "KSA", "contentTypes": ["regulation", "circular", "press_release"] },
      { "domain": "centralbank.ae", "jurisdiction": "UAE", "contentTypes": ["regulation", "circular"] }
    ],
    "tier2": [
      { "domain": "out-law.com", "jurisdiction": "__multi__", "contentTypes": ["commentary"] }
    ],
    "tenantAdditions": [
      { "domain": "altamimi.com", "jurisdiction": "UAE", "contentTypes": ["client_alert"], "tier": 2 }
    ],
    "blocklist": [
      "reddit.com", "quora.com", "wikipedia.org", "*.blogspot.com"
    ]
  },
  "lastUpdated": "2026-05-01",
  "updatedBy": "admin@firm.com"
}
```

## Blocklist

The following source types are always blocked regardless of tenant configuration:
- Wikipedia (unreliable for legal authority)
- Reddit and other forums
- Anonymous legal Q&A sites (Avvo, JustAnswer, LegalZoom Q&A)
- Law student blogs
- News aggregator snippets (Google News, Yahoo News, Flipboard)
- LinkedIn posts and articles
- Facebook / social media
- Any domain that is not indexed as a legal or government source

## Usage by the web search orchestrator

When [[tool-web-search-orchestrator]] executes a query:

1. **Primary pass**: restrict query to Tier 1 domains (using `site:` operator) for the relevant jurisdiction
2. **Secondary pass**: if Tier 1 returns < 3 results, expand to Tier 2 (publishers and bar associations)
3. **General pass**: if still insufficient, run without site restriction but filter results against the allowlist — only return results from allowed domains
4. **Labeling**: every returned result is labeled with its tier (`sourceType`, `sourceTier`)
5. **Blocked domains**: any result from the blocklist is silently dropped

## Quality signals appended to results

The allowlist system appends quality metadata to every search result:

| Field | Value | Meaning |
|---|---|---|
| `sourceTier` | 1–4 | Allowlist tier of the source |
| `verifiedPrimary` | true/false | Whether the domain is in Tier 1 |
| `jurisdictionMatch` | true/false | Whether the source jurisdiction matches the query |
| `freshness` | high/medium/low | Based on publication date |
| `contentTypeMatch` | true/false | Whether the content type matches what was searched |

## Related skills

- [[tool-web-search-orchestrator]] — the search tool that reads and enforces this allowlist
- [[tool-legal-data-hunter]] — orchestrator that invokes the web search orchestrator
