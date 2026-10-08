---
name: connector-legal-data-hunter-sboghossian
title: Connector — Legal Data Hunter
description: Use when a legal research query requires primary legal sources from MENA jurisdictions — Lebanon, UAE (onshore and free zones), KSA, Egypt, Jordan, and related Gulf states — that are not available in Westlaw, EUR-Lex, or other mainstream legal databases. The Legal Data Hunter is HAQQ's in-house scraping and structuring service for MENA legal materials. Triggers on requests for Lebanese law, UAE ministerial decrees, KSA SAMA regulations, Egyptian Official Gazette entries, or MENA court judgments not available in commercial databases.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/connector/connector-legal-data-hunter
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Connector — Legal Data Hunter

## What it does

Legal Data Hunter is HAQQ's proprietary internal service for acquiring, structuring, and surfacing legal data from MENA jurisdictions. It addresses the core gap in MENA legal research: the region's primary legal sources — statutes, decrees, regulations, ministerial decisions, court judgments — are often scattered across government portals, published only in Arabic or French, behind opaque websites with no structured API, or in scanned PDFs without machine-readable text.

The service combines:
- **Automated scraping** of government legal portals and official gazettes.
- **OCR and text extraction** for scanned Arabic and French legal documents.
- **Structured indexing** with consistent metadata (jurisdiction, source, date, category).
- **A queryable internal API** that the legal-AI platform calls when a request requires MENA-specific primary sources.

## Setup / auth

This is an **internal HAQQ API**:
- API endpoint: internal service mesh (not publicly accessible).
- Auth: per-tenant service token, issued by the platform operator.
- Rate limit: 200 requests/minute per tenant; enforced to protect the scraping infrastructure.
- No external API key management required by the end user.

## Source coverage

### UAE

| Source | Content | Notes |
|---|---|---|
| UAE Official Gazette (Al Jarida Al Rasmiya) | Federal laws, decrees, ministerial decisions | Arabic; PDF; OCR required for older issues |
| DIFC Laws & Regulations | DIFC primary legislation | English; well-structured HTML |
| ADGM legislation | ADGM primary legislation | English; well-structured |
| QFC Regulatory Authority | QFC framework | English |
| UAE MOJ Legal Database | Federal laws compilation | Arabic + English (some) |
| UAE CBUAE circulars | Central bank circulars | Arabic + English |
| MOHRE decisions | Labor + employment ministerial decisions | Arabic |

### KSA

| Source | Content | Notes |
|---|---|---|
| Umm al-Qura (Official Gazette) | Royal decrees, ministerial decisions | Arabic; weekly |
| SAMA circulars | Banking and finance regulations | Arabic + English |
| Saudi Arbitration Center (SCCA) rules | Arbitration procedural rules | Arabic + English |
| ZATCA publications | Tax and customs regulations | Arabic + English |
| MOJ Saudi Arabia | Judicial circulars, form judgments | Arabic |

### Lebanon

| Source | Content | Notes |
|---|---|---|
| Lebanese Official Journal (Al Jarida Al Rasmiya) | Laws, decrees, decisions | Arabic + French; often PDF |
| Banque du Liban circulars | BDL central bank circulars | Arabic + English + French |
| Bar Association of Beirut | Professional guidance; not primary law | Arabic + French |
| Cassation Court (selective) | Published cassation judgments | Arabic; limited digital availability |

### Egypt

| Source | Content | Notes |
|---|---|---|
| Egyptian Official Gazette | Laws, presidential decrees, ministerial decisions | Arabic |
| EFSA regulations | Financial services regulatory text | Arabic + English |
| Cairo Regional Centre for International Commercial Arbitration (CRCICA) | Arbitration rules | Arabic + English |

### GCC (regional)

| Source | Content | Notes |
|---|---|---|
| GCC Secretariat | GCC unified laws (commercial, customs) | Arabic |
| FATF/MENAFATF | AML/CFT guidance applicable to the region | English + Arabic |

## Capabilities

| Capability | Description |
|---|---|
| Statute full-text retrieval | Retrieve full text of a law by name, number, or year |
| Ministerial decision lookup | Search by issuing ministry, subject, and date range |
| Official gazette search | Full-text search across indexed gazette issues |
| Judgment retrieval (where available) | Published court judgments by court and date |
| Arabic → English extraction | Returns Arabic text with an auto-translated English gloss (for orientation, not authoritative translation) |
| Amendment tracking | Where tracked, surface amendments to a base law |
| Regulatory timeline | Chronological list of enactments in a specific area of law |

## Usage patterns

### Pattern 1 — Lebanese commercial law provision

```
User: "What does Lebanese law say about the form requirements for a pledge of shares?"
→ Legal Data Hunter searches Lebanese Code of Commerce
→ Returns relevant provisions (in Arabic) with English gloss
→ Note: cite the official Arabic text; the English gloss is for orientation only
```

### Pattern 2 — UAE labor law update

```
User: "Has the MOHRE issued any new decisions on remote work since 2022?"
→ Searches MOHRE decisions index for date:after:2022 + keyword "remote"
→ Returns list of matching decisions with date and short description
→ Flags if OCR confidence on any document is below threshold
```

### Pattern 3 — KSA recent ZATCA change

```
User: "What are the current VAT rules for cross-border services into KSA?"
→ Searches ZATCA publications for VAT + cross-border services
→ Returns current regulatory text (KSA VAT rate: 15%)
→ Note effective date of the most recent amendment
```

### Pattern 4 — Egyptian investment law

```
User: "What incentives does Egypt's Investment Law offer to foreign investors?"
→ Searches Egyptian Official Gazette for Investment Law text
→ Returns full text with auto-translated English summary
```

## Accuracy and verification requirements

MENA primary legal sources retrieved by the Legal Data Hunter must be treated as **research starting points**, not final authoritative texts, because:

1. **Arabic legal Arabic is specialized.** OCR and machine translation of legal Arabic is imperfect. Always have a qualified Arabic-reading lawyer verify the operative provisions.
2. **Gazette issues are not always indexed in full.** Coverage gaps exist — particularly for older issues and for scanned-only documents.
3. **Amendment tracking is incomplete.** A law may have been amended by a subsequent decree that is not yet in the index. Always verify whether a retrieved text is the current in-force version.
4. **Free-zone law is partly internal.** DIFC and ADGM legislative drafts and amendments are covered; confidential DFSA/FSRA guidance and supervisory letters are not.

For any MENA legal matter where the outcome depends on a specific statutory provision, the practitioner must verify the text against the original Official Gazette issue.

## Permissions & safety

- **Internal API only.** The Legal Data Hunter is not a public connector; its endpoint and credentials must not be shared with end users or external parties.
- **Rate limiting.** Respect the 200 req/min limit. Long research queries should be queued, not burst.
- **Translation disclaimers.** All English translations returned by the service are machine-generated for orientation purposes. They must not be cited in legal documents or proceedings as authoritative translations — a certified sworn translator (مترجم محلف) is required for that.
- **No fabricated provisions.** If the service cannot find a provision, return "Not found in current index" — never synthesize or interpolate statutory text.

## Failure modes

| Failure | Cause | Resolution |
|---|---|---|
| "Not in index" | Source not yet scraped or OCR failed | Try [[connector-firecrawl]] directly on the source URL; flag for index expansion |
| Low OCR confidence | Scanned document with poor quality | Flag to user; provide raw image link for manual review |
| Arabic rendering issue | Text pipeline encoding error | Return raw UTF-8 Arabic string; let the UI handle rendering |
| Stale data | New decree not yet picked up by scraper | Note retrieval date; advise user to check source directly for recent weeks |

## Related skills

- [[connector-eur-lex]]
- [[connector-legifrance]]
- [[connector-firecrawl]]
- [[connector-ofac-sanctions]]
- [[connector-companies-house-uk]]
