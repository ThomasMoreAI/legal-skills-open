---
name: tool-lexisnexis-sboghossian
title: LexisNexis
description: Use when a user needs premium case law research, statute annotation, or citator verification across US, UK, French, or MENA jurisdictions. LexisNexis is the preferred database for MENA legal research via Lexis Middle East, covering KSA, UAE, Bahrain, Kuwait, Oman, and Qatar in both Arabic and English. Triggers on requests for case law, citator checks (Shepard's), regulatory updates, or practice guidance in jurisdictions where LexisNexis has superior coverage over Westlaw.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/tool/tool-lexisnexis
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# LexisNexis

## What it does

LexisNexis is one of two premier legal research databases (alongside Westlaw). This tool connects to the LexisNexis API to retrieve case law, statutes, regulations, secondary sources, and citator (Shepard's) signals. Its standout advantage for this platform is **Lexis Middle East** — a specialized MENA database covering GCC jurisdictions in both Arabic and English.

## Setup / auth

| Parameter | Description | Required |
|-----------|-------------|----------|
| `lexisClientId` | LexisNexis API client ID (OAuth2) | Yes |
| `lexisClientSecret` | LexisNexis API client secret | Yes |
| `subscription` | `lexis-plus` / `lexis-middle-east` / `jurisclasseur` | Yes — determines available corpora |
| `languagePreference` | `en` / `ar` / `fr` | No — defaults to `en` |

A Lexis Middle East subscription is separate from the standard LexisNexis US/UK subscription. Confirm which product the tenant is licensed for before routing queries.

## Coverage comparison: LexisNexis vs Westlaw

| Coverage area | LexisNexis | Westlaw |
|---------------|-----------|---------|
| US federal + state case law | Comprehensive | Comprehensive |
| UK case law | Strong (Butterworths) | Strong |
| France (civil law) | JurisClasseur — leading | Dalloz — strong |
| Germany | Strong | Strong |
| MENA (via Lexis Middle East) | **Primary strength** | Limited |
| KSA regulatory (CMA, SAMA, ZATCA) | Strong via Lexis ME | Weak |
| UAE federal + local decrees | Strong via Lexis ME | Limited |
| DIFC/ADGM court judgments (full text) | Yes | Partial |
| Australia / Canada | Good | Strong |
| Citator | Shepard's Citations | KeyCite |

## Capabilities

### Case law search
```
Input:  {
  query: "force majeure COVID-19 commercial lease",
  jurisdiction: ["UAE", "DIFC"],
  dateFrom: "2020-01-01"
}
Output: {
  cases: [
    {
      caseName, citation, court, date,
      headnotes: [...],
      fullTextUrl,
      shepards: { status: "Good Law" | "Caution" | "Overruled", citingReferences: [...] }
    }
  ]
}
```

### Lexis Middle East — MENA-specific search
```
Input:  {
  query: "تصفية شركة ذات مسؤولية محدودة",
  jurisdiction: "KSA",
  language: "ar",
  corpus: "lexis-middle-east"
}
Output: { statutes: [...], regulations: [...], caseLaw: [...] }
```

Lexis Middle East covers:
- KSA: Royal Decrees, Council of Ministers resolutions, CMA regulations, SAMA circulars, ZATCA rulings, Board of Grievances decisions
- UAE: Federal laws, DIFC laws/regulations, ADGM regulations, individual emirate free-zone rules, Dubai Courts + Abu Dhabi Courts decisions
- Bahrain, Kuwait, Oman, Qatar: Primary legislation + selected case law
- Arabic-English bilingual interface with parallel text where available

### Shepard's citator
```
Input:  { citation: "2019 DIFC AT 001" }
Output: {
  status: "Good Law",
  history: [{ type: "Affirmed", court: "...", date: "..." }],
  negativelyTreatments: [],
  citingCases: [{ name, citation, treatment }]
}
```

Shepard's is LexisNexis's exclusive citator. It distinguishes:
- **Red stop sign** — overruled or reversed on the key point
- **Orange Q** — validity questioned
- **Yellow triangle** — some negative treatment but still good law
- **Green diamond** — cited positively

Always run Shepard's before relying on any case as precedent.

### Statutes and regulations (annotated)
Returns the statutory text plus LexisNexis editorial annotations: relevant cases, cross-references, and practice notes. Particularly valuable for:
- UAE Commercial Companies Law annotations
- DIFC Contract Law with case cross-references
- KSA Company Law with regulatory guidance

### JurisClasseur (French law)
LexisNexis's flagship French law secondary source — encyclopedic practitioner commentaries organized by Code article. Authoritative for French law analysis in MENA contracts governed by French law.

### Practice guidance and forms
LexisNexis Practical Guidance provides jurisdiction-specific checklists, negotiating guides, and forms across the US, UK, and selected common-law jurisdictions.

## Usage patterns

**Pattern 1 — DIFC contract dispute research**
```
User: "Find DIFC Court cases on liquidated damages clauses."
→ Lexis Middle East: jurisdiction=DIFC, query="liquidated damages"
→ Run Shepard's on top results
→ Return with headnotes + treatment status
```

**Pattern 2 — KSA regulatory update scan**
```
User: "Latest SAMA banking circulars on AML."
→ Lexis Middle East: jurisdiction=KSA, corpus=regulations, issuer=SAMA, dateFrom=2024-01-01
→ Return chronological list with summaries
```

**Pattern 3 — French Code civil annotation**
```
User: "What do French courts say about Article 1218 force majeure post-2016?"
→ JurisClasseur: Article 1218 commentary + Cassation cases citing it
→ Supplement with Legifrance for the statutory text ([[tool-legifrance-fr]])
```

**Pattern 4 — Multi-jurisdiction triangulation**
```
User: "Research choice-of-law clauses in international M&A — US, UK, and UAE."
→ Westlaw for US (hand-off to [[tool-thomson-reuters-westlaw]])
→ LexisNexis Butterworths for UK
→ Lexis Middle East for UAE
→ Consolidate
```

## Permissions & safety

- Credentials are tenant-scoped; never share across tenants.
- Shepard's status is authoritative only at the time of query — always note the fetch date in any deliverable.
- LexisNexis content is subject to copyright; reproduce only fair-use extracts in deliverables. Summarize and cite rather than block-quote entire cases.
- Arabic-language results should be reviewed by a native Arabic speaker for critical matters — transliteration normalization in the search engine is imperfect.

## Failure modes

| Failure | Symptom | Resolution |
|---------|---------|------------|
| Auth error | 401 | Refresh OAuth2 token; check client credentials |
| Subscription gap | No results for Lexis Middle East | Confirm Middle East subscription is active |
| No results | Empty set | Broaden query; try Arabic transliterations |
| Shepard's unavailable | Citator returns null | Run manually via LexisNexis web UI |
| Arabic OCR mismatch | Arabic search missing obvious hits | Try English transliteration variants |

## Related skills

- [[tool-thomson-reuters-westlaw]] — pair for US/AU/CA where Westlaw's depth is superior
- [[tool-google-scholar-legal]] — free fallback for US/Commonwealth case law
- [[tool-rag-public-legal-corpus]] — internal corpus for DIFC/ADGM judgments already indexed
- [[tool-legifrance-fr]] — official French statute text to complement JurisClasseur annotations
- [[research-precedent-finder]] — higher-level skill that orchestrates database queries into a precedent brief
