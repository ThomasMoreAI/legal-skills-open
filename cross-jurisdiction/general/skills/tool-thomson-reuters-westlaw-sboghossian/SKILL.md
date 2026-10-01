---
name: tool-thomson-reuters-westlaw-sboghossian
title: Thomson Reuters Westlaw
description: Use when a user needs premium legal research across US, UK, Australian, or Canadian jurisdictions — including case law with KeyCite citator verification, annotated statutes, Practical Law forms and checklists, and secondary sources. Also the preferred tool for DIFC/ADGM common-law research and BVI/Cayman holding-structure analysis. Requires client Westlaw credentials. Pair with LexisNexis for MENA-specific and French law research.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/tool/tool-thomson-reuters-westlaw
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: general
language: en
---

# Thomson Reuters Westlaw

## What it does

Westlaw is one of two premier legal research databases (alongside LexisNexis). This tool provides access to Westlaw's research content via the Thomson Reuters API when the tenant has a Westlaw subscription configured. It excels at US federal and state case law, UK case law, and offers the Practical Law practice guides — the most comprehensive drafting and transaction support resource for common-law practitioners.

For MENA legal practice, Westlaw is most useful for:
- English common-law analysis applicable to DIFC and ADGM
- BVI, Cayman Islands, and Channel Islands company law (offshore holding structures)
- English and Welsh case law (when English law is the governing law of a MENA contract)
- US securities law research for US-listed MENA subsidiaries

## Setup / auth

| Parameter | Description | Required |
|-----------|-------------|----------|
| `westlawClientId` | Thomson Reuters API client ID | Yes |
| `westlawClientSecret` | TR API client secret | Yes |
| `subscription` | `westlaw-us` / `westlaw-uk` / `westlaw-au` / `practical-law` / `cocounsel` | Yes — determines available corpora |
| `jurisdiction` | Default jurisdiction for session | No — can specify per query |

Westlaw credentials are licensed per user or per firm — do not share across tenants.

## Coverage

### Case law
| Jurisdiction | Depth | Notes |
|---|---|---|
| US Federal | Comprehensive — all circuits back to founding | Headnotes, key numbers, full text |
| US State | All 50 states + DC | Depth varies by state |
| UK | All High Court + appellate decisions | Includes EWCA, EWHC, UKSC, Privy Council |
| Australia | Federal + all state supreme courts | Via Westlaw AU |
| Canada | Federal + provincial courts | Via Westlaw Canada |
| EU | CJEU and EU General Court | Full text |
| DIFC / ADGM | Selected decisions | Less comprehensive than LexisNexis Middle East |

### Statutes and regulations
- US: Federal Code + all 50 state codes, annotated
- UK: legislation.gov.uk integrated with annotations
- AU/CA: annotated codes

### Practical Law
Practical Law (a Thomson Reuters product) is a practitioner-focused database of:
- Drafting guides and model clauses (by jurisdiction and contract type)
- Transaction toolkits (M&A, finance, real estate, employment)
- Legal updates and briefings
- Jurisdiction-specific compliance checklists
- Know-how notes

For MENA practice, Practical Law covers UAE, KSA, and Egypt through a partnership with local contributors — particularly useful for employment law, corporate, and commercial real estate.

### Secondary sources
- American Jurisprudence (AmJur)
- American Law Reports (ALR)
- Law Reviews and Journals
- Treatises (Nimmer on Copyright, Corbin on Contracts, etc.)

### KeyCite (citator)
KeyCite is Westlaw's exclusive citator:

| Symbol | Meaning |
|--------|---------|
| Red flag | Warning — case directly overruled or unconstitutional |
| Yellow flag | Caution — negative treatment but not necessarily overruled |
| Blue-striped flag | Appeal pending |
| Green C | Cited positively |

Always run KeyCite on any case before citing it in a brief, memo, or opinion.

## Capabilities

### Natural language / Boolean search
```
Input:  {
  query: "force majeure COVID commercial lease non-performance",
  jurisdiction: "UKHL+EWCA+EWHC",
  dateFrom: "2020-01-01",
  database: "case-law"
}
Output: {
  cases: [
    {
      caseName, citation, court, date,
      headnotes, keyNumbers,
      keyctie: { status, flagType, citingCases: [...] },
      fullTextUrl
    }
  ]
}
```

### Practical Law research
```
Input:  {
  query: "SPA representations and warranties UAE",
  database: "practical-law",
  jurisdiction: "UAE"
}
Output: {
  resources: [
    {
      title, type: "practice_note" | "standard_document" | "checklist",
      url, summary, relatedTopics
    }
  ]
}
```

### Statute / code lookup
```
Input:  {
  statute: "Companies Act 2006",
  section: "s 177",
  jurisdiction: "UK"
}
Output: { text, annotations, relatedCases, keyctie }
```

### Secondary source retrieval
Treatise sections, ALR annotations, and law review articles on point.

## Usage patterns

**Pattern 1 — DIFC common-law research**
```
User: "DIFC courts approach to implied terms under English law"
→ Westlaw UK: case law search on implied terms
→ Practical Law UAE/DIFC: know-how note on DIFC contract law
→ KeyCite all cited cases
```

**Pattern 2 — BVI holding company analysis**
```
User: "BVI company pledging shares — formalities?"
→ Westlaw UK: search BVI Business Companies Act cases + Privy Council
→ Practical Law: BVI security over shares toolkit
```

**Pattern 3 — English governing law counterparty research**
```
User: "Contract says English law applies. What is English law on penalty clauses?"
→ Westlaw UK: Cavendish Square v Makdessi [2015] UKSC 67 + subsequent cases
→ KeyCite Cavendish Square
→ Practical Law: drafting note on liquidated damages under English law
```

**Pattern 4 — Triangulate with LexisNexis**
For any significant research question:
→ Run primary search on Westlaw
→ Cross-check with LexisNexis ([[tool-lexisnexis]])
→ Use KeyCite (Westlaw) + Shepard's (LexisNexis) for citator cross-reference
→ Report any discrepancy

## CoCounsel integration

Thomson Reuters CoCounsel is TR's AI layer on top of Westlaw. If the tenant has CoCounsel access, this tool can optionally route queries to CoCounsel for AI-synthesized research summaries, with Westlaw citations as the basis. CoCounsel outputs should always be verified against the underlying Westlaw citations.

## Permissions & safety

- Credentials are tenant-scoped; never share across tenants.
- KeyCite status is authoritative only at the time of query — note the fetch date.
- Practical Law content is copyrighted by Thomson Reuters; summarize and cite rather than reproducing full practice notes.
- AI summaries from CoCounsel must be verified against primary source citations before use in client deliverables.

## Failure modes

| Failure | Symptom | Resolution |
|---------|---------|------------|
| Auth failure | 401 from TR API | Re-check client credentials; refresh OAuth token |
| Subscription gap | No results for requested database | Confirm which Westlaw products are in the subscription |
| KeyCite unavailable | Citator returns null | Run manually via Westlaw web UI |
| Rate limit | 429 | Implement backoff; TR API rate limits vary by subscription tier |
| Practical Law gap | No UAE/KSA content | Check if jurisdiction-specific Practical Law subscription is active |

## Related skills

- [[tool-lexisnexis]] — complementary premium database; superior for MENA (Lexis Middle East) and France (JurisClasseur)
- [[tool-google-scholar-legal]] — free fallback for US/Commonwealth case law
- [[tool-rag-public-legal-corpus]] — internal corpus for DIFC/ADGM judgments
- [[research-precedent-finder]] — orchestrates database queries into a precedent brief
