---
name: tool-legifrance-fr-sboghossian
title: Legifrance — French Official Legal Text
description: Use when a task requires authoritative French legislative text, case law, or regulatory instruments — including consolidated Code civil articles, Code de commerce provisions, labor conventions, and Cour de Cassation judgments. Critical for any MENA contract with French governing law (common in Lebanese, Moroccan, and Tunisian drafting traditions) or for OHADA instruments that follow French civil law structure. Primary source; preferred over secondary summaries for statute text.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/tool/tool-legifrance-fr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: general
language: en
---

# Legifrance — French Official Legal Text

## What it does

Legifrance (legifrance.gouv.fr) is the French government's official legal text repository. It is the authoritative primary source for all French legislation, regulation, jurisprudence, and collective labor agreements. This tool provides programmatic access to Legifrance so that Louis can retrieve exact, consolidated statutory text, track legislative history, and cite case law accurately for tasks governed by French law.

**Jurisdiction relevance for MENA practice**: French law is directly relevant in several MENA contexts:
- Lebanese commercial and civil law is heavily modeled on the Code civil and Code de commerce (though Lebanese law has diverged in some areas since 1948)
- Francophone MENA jurisdictions (Morocco, Tunisia, Algeria) follow French civil law tradition
- OHADA (Organisation pour l'Harmonisation en Afrique des Affaires) — covering 17 West and Central African states — uses a unified commercial law framework derived from French law
- Sophisticated MENA contracts (especially those involving French banks, French corporates, or multi-jurisdictional M&A) frequently choose French law as the governing law

## Setup / auth

Legifrance provides a public API (PISTE — Plateforme Industrielle et Scientifique de Transformation de l'État). Access requires:

| Parameter | Description | Required |
|-----------|-------------|----------|
| `pisteClientId` | PISTE OAuth2 client ID | Yes for API access |
| `pisteClientSecret` | PISTE client secret | Yes for API access |

Alternatively, the tool can scrape Legifrance's public HTML interface for cases where API credentials are unavailable, subject to rate limits.

## Capabilities

### Article lookup by reference
```
Input:  { articleRef: "Article 1134 du Code civil" }
Output: {
  articleRef, codeTitle, text, consolidatedVersion,
  effectiveDate, historicalVersions: [...],
  amendedBy: [...], relatedArticles: [...]
}
```

The tool automatically retrieves the **consolidated** (i.e., current) version of the article and flags whether the user's reference matches a historical version.

### Full-text keyword search
```
Input:  { query: "clause pénale réduction judiciaire", corpus: "codes" }
Output: [ { articleRef, codeTitle, snippet, url } ]
```

Searches across all French legal codes simultaneously.

### ECLI case lookup
```
Input:  { ecli: "ECLI:FR:CCASS:2021:CO01234" }
Output: { caseName, court, chamber, date, decision, legalIssues, text, url }
```

ECLI (European Case Law Identifier) is the standard for French jurisprudence. The tool also supports legacy arrêt numbers.

### Code index
Returns the full article index of a named Code, useful for navigating to the relevant section:
```
Input:  { code: "Code de commerce", book: "Livre IV" }
Output: [ { articleRef, heading, url } ]
```

### Convention collective lookup
```
Input:  { idcc: "1486", date: "2026-01-01" }
Output: { conventionTitle, idcc, sectors, articles: [...] }
```

Collective labor agreements (conventions collectives) are indexed by IDCC code.

## Key corpora on Legifrance

| Corpus | Description | MENA relevance |
|--------|-------------|----------------|
| Code civil | General contract, tort, property, family law | High — LB civil law closely follows this |
| Code de commerce | Commercial companies, contracts, insolvency | High — LB commercial law origin |
| Code du travail | Employment | Moderate — for French-law employment contracts |
| Code de procédure civile | Civil procedure | Relevant if French courts have jurisdiction |
| Code monétaire et financier | Banking and finance regulation | Relevant for French-law finance docs |
| Jurisprudence — Cassation | Supreme Court civil + commercial cases | Essential for governing-law analysis |
| Jurisprudence — Conseil d'État | Administrative law cases | Public law contexts |
| Journal Officiel | All new laws, decrees, and ministerial orders | Currency — latest instruments |
| OHADA texts | Not directly on Legifrance, but related via French civil law structure | Cross-reference for West Africa |

## Important consolidation notes

Legifrance consolidates legislation as of a given date. Key points:

1. **Always specify the effective date** for historical contract analysis — the version of an article that applied at contract execution may differ from the current version.
2. **The 2016 reform of French contract law** (Ordonnance 2016-131) significantly rewrote the Code civil's general contract law provisions (Articles 1100–1386). Articles prior to that reform had different numbering (e.g., the old Article 1134 "force of law" provision is now Article 1103). When citing, verify the reform period.
3. **The 2021 reform on security interests** (Ordonnance 2021-1192) rewrote guarantee and pledge provisions — relevant for finance and secured lending.

## Usage for MENA governing-law review

When a MENA contract selects French law as governing law:

1. Fetch the relevant Code civil provisions on the disputed point (e.g., force majeure — Article 1218 post-2016 reform).
2. Check for mandatory rules (lois de police) that override party choice.
3. Note French courts' approach to the specific clause type (e.g., French courts can reduce a penalty clause under Article 1231-5 — unlike English courts which generally cannot).
4. Pair with [[tool-lexisnexis]] (JurisClasseur section) for practitioner commentary on the provision.

See [[review-governing-law-conflict]] for the full governing-law conflict analysis workflow.

## Output schema

```json
{
  "articleRef": "Article 1218 du Code civil",
  "text": "Il y a force majeure en matière contractuelle lorsqu'un événement...",
  "consolidatedVersion": "2016-10-01",
  "effectiveDate": "2016-10-01",
  "codeTitle": "Code civil",
  "url": "https://www.legifrance.gouv.fr/codes/article_lc/...",
  "historicalVersions": [...],
  "source": "Legifrance — Service public de la diffusion du droit"
}
```

## Failure modes

| Failure | Symptom | Resolution |
|---------|---------|------------|
| PISTE auth failure | 401 | Re-check credentials; PISTE tokens expire |
| Article not found | 404 | Verify article number and code name |
| Historical version unavailable | Null history | Use Journal Officiel archives directly |
| Rate limit | 429 | Implement backoff; Legifrance API is rate-limited per minute |
| HTML scrape blocked | Bot detection | Switch to API mode; use PISTE |

## Related skills

- [[tool-lexisnexis]] — JurisClasseur practitioner commentary on French law provisions
- [[tool-thomson-reuters-westlaw]] — Westlaw France for case law annotations
- [[tool-web-search-orchestrator]] — for recent Journal Officiel publications not yet in Legifrance API
- [[tool-rag-public-legal-corpus]] — internal corpus index for OHADA and Francophone African law
