---
name: tool-legal-data-hunter-sboghossian
title: Legal Data Hunter
description: Use when a task requires systematically hunting for authoritative legal data across multiple heterogeneous sources — statutes, regulations, court judgments, official gazettes, regulator bulletins — and consolidating the results into a coherent, cited dataset. Acts as an orchestrating agent that selects and sequences the right data-source tools for a given legal research query, prioritizing primary sources and flagging data gaps.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/tool/tool-legal-data-hunter
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Legal Data Hunter

## What it does

The Legal Data Hunter is a meta-tool that orchestrates multiple legal data sources to answer a single complex legal research query. Rather than querying one database in isolation, it:

1. Decomposes the query into sub-questions (statute text, case law, regulatory guidance, commentary).
2. Routes each sub-question to the most appropriate source tool.
3. Consolidates results, deduplicates citations, and flags gaps.
4. Returns a structured legal data package with provenance attached to every piece of information.

It is the right tool when the research question spans more than one source category — for example, "What are the UAE requirements for data localization in the financial sector?" requires statute text (UAE PDPL), regulatory guidance (CBUAE circulars), and possibly case law or enforcement decisions.

## Setup / auth

The Legal Data Hunter inherits credentials from whichever sub-tools are configured for the tenant:
- Premium databases (Westlaw, LexisNexis) — require tenant API keys
- Public sources (official gazettes, regulator websites) — no auth required
- RAG corpora — require the embedding store to be indexed

The tool gracefully degrades: if premium databases are unavailable, it falls back to public sources and clearly labels the limitation.

## Source hierarchy

The tool applies the following source priority order, consistent with the web-search allowlist:

| Priority | Source category | Examples |
|----------|-----------------|---------|
| 1 | Official legislation / gazettes | Umm Al-Qura (KSA), UAE Federal Gazette, Legifrance (FR), legislation.gov.uk, EUR-Lex |
| 2 | Regulator publications | SAMA, CBUAE, BDL, CMA, SDAIA, DFSA, FSRA, FCA |
| 3 | Court databases | DIFC Courts, ADGM Court, UK BAILII, CJEU, SCOTUS |
| 4 | Premium legal research | Westlaw, LexisNexis, Practical Law |
| 5 | Public legal corpora (RAG) | Internal indexed corpus |
| 6 | Secondary / commentary | Practical Law, academic journals, Out-Law, Kluwer |
| 7 | Web search (allowlisted) | Bar associations, established legal blogs |

## Logic / decision rules

```
Given query Q and jurisdiction J:

1. Extract entities: statutes, regulations, topics, parties, dates
2. For each statute/regulation named: → use statute-lookup first (training data or Legifrance/EDGAR/official gazette)
3. For case law: → route to Westlaw/LexisNexis if credentialed; else Google Scholar + RAG corpus
4. For recent developments (< 12 months): → web search (regulator site first, then top publishers)
5. For MENA-specific: → Lexis Middle East if credentialed; else official gazette + web search
6. Consolidate: deduplicate identical citations, merge complementary snippets
7. Flag: any sub-question with no authoritative source → mark as GAP
```

## Capabilities

### Multi-source research bundle
```
Input:  {
  query: "UAE PDPL data localization requirements for banks",
  jurisdiction: "UAE",
  urgency: "standard"
}
Output: {
  statutes: [{ title, source, text, effectiveDate }],
  regulations: [{ title, issuer, date, text }],
  caseLaw: [{ case, court, date, snippet, url }],
  regulatoryGuidance: [{ issuer, title, date, url }],
  secondarySources: [{ title, author, publication, url }],
  gaps: ["No enforcement decisions found as of fetch date"],
  confidence: "high" | "medium" | "low"
}
```

### Jurisdiction-specific gazette scrape
For MENA jurisdictions where databases lag, the hunter can directly scrape official gazette feeds for recent legislation:
- KSA: Umm Al-Qura (أم القرى)
- UAE: UAE Official Gazette (الجريدة الرسمية)
- Lebanon: al-Jarida al-Rasmiyya (الجريدة الرسمية اللبنانية)
- Egypt: al-Jaridah al-Rasmiyya
- France: Journal Officiel de la République Française (via Legifrance)

### Gap analysis
After the research run, the hunter explicitly reports what it could not find — this is as important as what it did find, because absence of authority has legal significance (e.g., no reported case law on a novel issue).

## Usage patterns

**Pattern 1 — Statute + regulation bundle**
```
User: "Pull everything on Lebanon data protection law."
→ Identify: Law 81/2018 on Electronic Transactions, draft Personal Data Protection Bill
→ Fetch official gazette texts
→ Fetch BDL circulars on data handling for banks
→ Fetch any recent parliamentary committee reports
→ Return consolidated package with dates and source URLs
```

**Pattern 2 — Recent regulatory change scan**
```
User: "Any new CBUAE regulations on crypto in the last 6 months?"
→ Web search: site:cbuae.gov.ae + date filter
→ RAG corpus check for CBUAE circulars
→ Return new circulars with effective dates + summary
```

**Pattern 3 — Multi-jurisdiction comparison**
```
User: "Compare DIFC vs ADGM vs onshore UAE company formation requirements."
→ Route each to respective official source (DIFC Companies Law, ADGM Companies Regulations, UAE Commercial Companies Law)
→ Consolidate in a comparison table
```

## Permissions & safety

- Apply the source allowlist from [[tool-web-search-source-allowlist]] — never cite Wikipedia or forums as primary sources.
- Label every result with its source, date, and source tier.
- Flag materials older than 2 years as potentially outdated, especially for fast-moving regulatory areas (crypto, AI, fintech).
- Do not fabricate statute article numbers or case citations. If a source is unavailable, say so explicitly.

## Failure modes

| Failure | Symptom | Resolution |
|---------|---------|------------|
| No primary source found | Gaps in all tiers | Report gap; recommend human researcher |
| Contradictory sources | Conflicting authority | Surface the conflict; do not silently resolve it |
| Stale data | Sources > 18 months old | Flag with timestamp; recommend fresh verification |
| Rate limits | 429 on premium DB | Fall back to public tier; inform user |
| Non-indexed language | Arabic-only source not parsed | Flag; route to [[tool-ocr-arabic]] if document available |

## Related skills

- [[tool-web-search-orchestrator]] — the web-search sub-tool this hunter invokes
- [[tool-rag-public-legal-corpus]] — RAG layer over curated public legal corpus
- [[tool-lexisnexis]] — premium legal research for case law and commentary
- [[tool-thomson-reuters-westlaw]] — premium legal research (US/UK/AU primary)
- [[tool-legifrance-fr]] — French official legal text
- [[tool-web-search-source-allowlist]] — per-tenant source trust configuration
