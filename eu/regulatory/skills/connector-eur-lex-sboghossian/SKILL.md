---
name: connector-eur-lex-sboghossian
title: Connector — EUR-Lex
description: Use when a lawyer or compliance professional needs to retrieve, read, or cite official EU legal texts — regulations, directives, decisions, case law of the Court of Justice, and consolidated legislation — from EUR-Lex, the EU's official legal database. No authentication required. Triggers on any request involving EU law research, GDPR text, EU directive transposition, CELEX number lookups, or EU case law retrieval. Relevant globally for MENA companies doing business with EU counterparties or processing EU personal data.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/connector/connector-eur-lex
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: en
---

# Connector — EUR-Lex

## What it does

EUR-Lex is the European Union's official legal database, operated by the Publications Office of the EU. It contains the complete and authoritative text of all EU law: treaties, regulations, directives, decisions, recommendations, and the case law of the Court of Justice of the EU (CJEU) and the General Court. All content is freely accessible.

The EUR-Lex connector enables the legal-AI platform to:
- Retrieve the full text of EU legal instruments by CELEX number or text search.
- Return the consolidated (current, in-force) version of a regulation or directive.
- Retrieve the legislative history of an instrument (original text + all amending acts).
- Return CJEU and General Court judgments by case number.
- Link EU directives to their transposition status across member states.

## Setup / auth

EUR-Lex is a **public API with no authentication requirement**. The SPARQL endpoint and the REST API are freely accessible.

Two access methods:

| Method | Best for |
|---|---|
| EUR-Lex REST API (`publications.europa.eu/webapi/rdf/sparql`) | Structured CELEX lookups, legislative metadata |
| EUR-Lex web scraping via the HTML endpoint | Full document text where the API returns only metadata |

For production use, implement caching with a 24-hour TTL (EU legislation changes infrequently; high-frequency scraping is both unnecessary and impolite).

## Understanding CELEX numbers

CELEX numbers are EUR-Lex's document identifiers. The structure is: `[sector][year][document type][number]`.

Common sectors:
- `1` — Treaties (e.g., TFEU)
- `3` — Secondary legislation (regulations, directives, decisions)
- `6` — CJEU / General Court case law
- `7` — National implementation measures (transposition)
- `9` — Parliamentary questions and answers

Examples:
- `32016R0679` — Regulation 2016/679 (GDPR)
- `32018L1808` — Directive 2018/1808 (AVMS Directive)
- `62019CJ0311` — CJEU Case C-311/19

Always use the CELEX number for unambiguous retrieval. Title-based searches can return multiple hits from different years.

## Key EU instruments with MENA relevance

| Instrument | CELEX | Relevance to MENA |
|---|---|---|
| GDPR (General Data Protection Regulation) | 32016R0679 | Applies to any MENA company processing EU residents' data |
| NIS2 Directive (network security) | 32022L2555 | Cybersecurity obligations for operators in / serving the EU |
| AI Act | 32024R1689 | AI system compliance for MENA-built AI products marketed in EU |
| MiCA (Markets in Crypto-Assets) | 32023R1114 | MENA crypto/fintech companies targeting EU market |
| EU Audit Regulation | 32014R0537 | Relevant for MENA subsidiaries of EU-listed parents |
| Brussels I Recast (jurisdiction) | 32012R1215 | Cross-border litigation involving EU parties |
| Rome I (applicable law in contract) | 32008R0593 | Choice-of-law analysis for MENA–EU contracts |
| Rome II (applicable law in tort) | 32007R0864 | Tort/delict claims with EU nexus |

## Capabilities

| Capability | Details |
|---|---|
| CELEX number lookup | Full document text, metadata, HTML and PDF |
| Full-text search | Natural language query across all EUR-Lex documents |
| Consolidated text retrieval | Current in-force version incorporating all amendments |
| Legislative history | Original text + amending acts in chronological order |
| CJEU case retrieval by case number | Full judgment text |
| Directive transposition status | National measures notified by member states |
| Related documents | Documents citing or cited by the retrieved instrument |

## Usage patterns

### Pattern 1 — Retrieve GDPR text for a compliance review

```
User: "Get Article 83 of the GDPR"
→ Connector fetches CELEX 32016R0679, navigates to Article 83
→ Returns full text of Art. 83 (administrative fines)
→ Note: return the consolidated version (post-2018 corrections incorporated)
```

### Pattern 2 — Check AI Act obligations for a MENA legal-AI product

```
User: "Does Louis AI qualify as a high-risk AI system under the EU AI Act?"
→ Connector retrieves the AI Act (32024R1689), Annex III (high-risk AI list)
→ Returns the relevant classification criteria
→ Assistant applies criteria to the product description
→ Note: this is analysis assistance; legal sign-off requires qualified EU counsel
```

### Pattern 3 — Choice of law research for a MENA–EU contract

For a UAE-company selling services to a German buyer under a contract governed by UAE law: retrieve Rome I (32008R0593) to understand how an EU court would assess the choice-of-law clause, and whether mandatory EU consumer protection rules would override the choice.

### Pattern 4 — CJEU case law on a data-transfer question

```
User: "What did the CJEU say about EU-US data transfers in Schrems II?"
→ Case C-311/19 is the Schrems II judgment
→ Connector retrieves CELEX 62019CJ0311 (note: verify the correct CELEX against the actual case)
→ Returns judgment summary with key holdings on Standard Contractual Clauses
```

## Jurisdictional context — EU law in MENA practice

MENA lawyers encounter EU law primarily in four contexts:

1. **Data protection.** The GDPR applies extraterritorially — any MENA company with an EU establishment, or that targets EU data subjects, or that monitors EU persons' behavior, is subject to the GDPR. This is the single most common EU-law compliance question from MENA companies.

2. **Contract choice of law.** MENA–EU contracts frequently choose English law or UAE law as governing law. Where an EU court ends up hearing a dispute, Rome I determines how that choice-of-law clause is analyzed. MENA practitioners need to understand the mandatory provisions that override choice-of-law.

3. **Competition law.** EU competition law (Articles 101–102 TFEU) applies to conduct that has effect in the EU market, regardless of where the company is located. MENA companies with EU distribution agreements should be aware of EU vertical restraints guidelines.

4. **Sanctions.** EU sanctions (distinct from OFAC) are published in the Official Journal and accessible via EUR-Lex. For dual-use export compliance or financial sanctions screening, EUR-Lex is one of the primary sources alongside [[connector-ofac-sanctions]].

## Permissions & safety

- **Public data; no access restrictions.**
- **Always cite the CELEX number** when returning EU legal text to ensure traceability and reproducibility.
- **Version flag.** Always specify whether the text is the original version or the consolidated (current) version. Citing an unamended original where amendments are material is a professional error.
- **No hallucinated CELEX numbers.** If the CELEX number is uncertain, return the search result with the title and date and let the user confirm before citing.

## Failure modes

| Failure | Cause | Resolution |
|---|---|---|
| Document not found | Incorrect CELEX format or instrument not yet published | Verify CELEX structure; search by title + year |
| Only metadata returned | Full text requires HTML scrape | Fall back to the EUR-Lex HTML endpoint |
| Outdated text | Consolidated version not yet updated by EUR-Lex | Flag; note last consolidation date; link to amending acts |
| Server slow | EUR-Lex is government infrastructure; periodically slow | Implement 30s timeout; cache aggressively |

## Related skills

- [[connector-legifrance]]
- [[connector-cocounsel-thomson-reuters]]
- [[connector-companies-house-uk]]
- [[connector-ofac-sanctions]]
