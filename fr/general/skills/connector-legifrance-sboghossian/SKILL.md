---
name: connector-legifrance-sboghossian
title: Connector — Légifrance
description: Use when a lawyer or compliance professional needs to retrieve official French legal texts — statutes, codes, decrees, ordonnances, circulars, and Conseil d'État or Cour de cassation decisions — from Légifrance, the French government's official legal publication portal. No authentication required. Triggers on requests involving French law research, Code civil provisions, French regulatory compliance, or Franco-Lebanese legal analysis where the Lebanese code derives from French law.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/connector/connector-legifrance
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: general
language: en
---

# Connector — Légifrance

## What it does

Légifrance (`legifrance.gouv.fr`) is the French government's official portal for the publication of French law. It is the authoritative source for all French primary legislation: codes, statutes, decrees, ordonnances, ministerial decisions, administrative circulars, and the published jurisprudence of the Conseil d'État (administrative courts) and the Cour de cassation (civil/criminal courts).

The Légifrance connector retrieves full legal text from the Légifrance API and web interface for use in French-law research and analysis workflows.

## Setup / auth

Légifrance offers a **public REST API** (`api.piste.gouv.fr/dila/legifrance`) that is free but requires API key registration:

1. Register at `piste.gouv.fr` (PISTE is the French government API gateway).
2. Subscribe to the Légifrance product in the API catalog.
3. Receive a client ID and client secret for OAuth 2.0 client credentials flow.
4. Store credentials in the platform's secrets manager.

For lower-volume use, the Légifrance website can be scraped directly (no key needed), but the API is more reliable and structured.

## Content coverage

| Content type | Available |
|---|---|
| Codes (Code civil, Code de commerce, Code du travail, etc.) | Yes — consolidated current versions |
| Lois et ordonnances | Yes |
| Décrets et arrêtés | Yes |
| Jurisprudence judiciaire (Cour de cassation, Cours d'appel) | Yes (selected published judgments) |
| Jurisprudence administrative (Conseil d'État, Cours administratives) | Yes |
| Constitutionnel (Conseil constitutionnel) | Yes |
| Circulaires et instructions | Yes |
| Conventions collectives (labour) | Yes |
| Journal officiel (JORF) full archive | Yes |
| Historical versions (consolidated at a given date) | Yes — point-in-time retrieval |

## Key French codes with MENA relevance

| Code | Relevance to MENA practice |
|---|---|
| Code civil | Foundation for Lebanese Code des obligations et des contrats; French law often chosen as governing law by sophisticated MENA parties |
| Code de commerce | Corporate law applicable to French-incorporated MENA holding companies |
| Code monétaire et financier | Applicable to MENA fintech companies operating in France or with French investors |
| Code du travail | Employment law for French subsidiaries of MENA groups |
| Code de procédure civile | Procedural rules relevant when French courts have jurisdiction over a MENA–France dispute |
| Code de la consommation | Consumer protection — relevant for MENA e-commerce companies selling to French consumers |

## Usage patterns

### Pattern 1 — Retrieve a specific Code civil article

```
User: "What does the Code civil say about force majeure?"
→ Légifrance API: GET /consult/code?textId=LEGITEXT000006070721 + navigate to Art. 1218
→ Return Article 1218 Code civil (consolidated current text)
→ Note: Article 1218 was inserted by the 2016 ordonnance réformant le droit des contrats
```

### Pattern 2 — Franco-Lebanese legal comparison

Lebanon's Code des obligations et des contrats (COC) was modelled directly on the French Code civil and Code de commerce of the early 20th century. When advising on Lebanese law, comparing the Lebanese provision with its French source can illuminate the legislative intent:

- Retrieve the current French provision from Légifrance.
- Note any divergences from the Lebanese version.
- Identify French jurisprudence interpreting the original provision — this is persuasive (but not binding) in Lebanese courts.

### Pattern 3 — French corporate law for MENA holding company

For a MENA family group with a French SAS (Société par actions simplifiée) as its European holding vehicle:
- Retrieve the corporate governance provisions of the Code de commerce applicable to SAS.
- Check recent ordonnances affecting corporate disclosure requirements.
- Cross-reference with EU corporate-law directives via [[connector-eur-lex]].

### Pattern 4 — Jurisprudence on a contractual dispute

```
User: "Find Cour de cassation decisions on the limitation of liability clauses in B2B contracts"
→ Full-text search in Légifrance jurisprudence: "clause limitative de responsabilité" + chambre commerciale
→ Returns list of published decisions with date, chamber, and summary
→ Filter to post-2016 (post-reform) if the contract was signed after the 2016 contract law reform
```

### Pattern 5 — Point-in-time retrieval

When a contract was signed in 2015 (before the 2016 French contract law reform), retrieve the version of the Code civil in force as at the contract date:
- Légifrance supports historical consolidated versions.
- Specify `dateVersion=2015-01-01` in the API call.
- Return the pre-reform text for interpretation purposes.

## French law and the 2016 contract law reform

A critical trap for MENA practitioners using French law: the **2016 ordonnance n°2016-131** substantially reformed French contract law (Articles 1100–1386-1 Code civil), introducing codified provisions on:
- Formation, validity, and interpretation of contracts.
- Unforeseen circumstances (imprévision) — now codified in Art. 1195.
- Force majeure — codified in Art. 1218.
- Rescission for lesion and hardship.

Contracts signed before 1 October 2016 are governed by pre-reform provisions. Contracts signed after that date are governed by the new text. Always check the contract date before retrieving and applying French contract law provisions.

## Permissions & safety

- **Cite the JORF or Légifrance reference** when returning statutory text. Include the version date (date of consolidation).
- **No fabricated article numbers.** If an article is not found in the current consolidated version, do not guess or interpolate.
- **Translation note.** Légifrance content is in French. If returning French legal text to an English-speaking user, provide a working translation with a clear note that the French original is authoritative.

## Failure modes

| Failure | Cause | Resolution |
|---|---|---|
| PISTE API token expired | OAuth 2.0 client credentials token has 1h TTL | Implement token refresh before each API call |
| Article not found | Incorrect code identifier or article number | Search by title or keyword; provide Légifrance permalink |
| Historical version unavailable | Requested date predates digitized records | Flag; advise consultation of print Journal officiel or a specialized library |
| Jurisprudence not published | Many French court decisions are unpublished | Note that only published decisions are available; for unpublished decisions, a legal database subscription (Dalloz, LexisNexis FR) is needed |

## Related skills

- [[connector-eur-lex]]
- [[connector-legal-data-hunter]]
- [[connector-cocounsel-thomson-reuters]]
