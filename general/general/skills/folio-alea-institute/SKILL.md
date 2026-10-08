---
name: folio-alea-institute
title: FOLIO Legal Ontology Skill
description: 'Search and browse FOLIO, the open legal ontology with 18,000+ concepts covering areas of law, document types, legal entities, and more. Use when classifying legal concepts, finding document types, identifying areas of law, or mapping legal entity structures. Classification workflows available as slash commands: /folio:classify-document, /folio:identify-area-of-law, /folio:classify-entity.'
author: alea-institute
author_url: https://github.com/alea-institute/folio-mcp/tree/main/skills/folio
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# FOLIO Legal Ontology Skill

## When to Use

Use the FOLIO MCP tools when you need to:

- **Classify legal concepts**: Find the correct ontology term for a legal concept
- **Identify document types**: Look up legal document classifications (contracts, filings, opinions)
- **Find areas of law**: Determine which legal practice area applies
- **Map entity types**: Identify types of legal entities (corporations, trusts, partnerships)
- **Explore relationships**: Find how legal concepts relate to each other
- **Export definitions**: Get formal definitions in markdown, JSON-LD, or OWL XML

## How to Search

Follow this workflow:

1. **Search by name**: Start with `folio:search_concepts(query)` to find concepts by label
2. **Refine by definition**: If name search is too broad, use `folio:search_definitions(query)`
3. **Advanced query**: Use `folio:query_concepts(label, definition, branch, parent)` for composable filters
4. **Query properties**: Use `folio:query_properties(label, definition, domain, range)` to find relationships
5. **Browse branches**: Use `folio:list_branches()` then `folio:get_taxonomy_branch(branch_name)` to explore a category
6. **Navigate hierarchy**: Use `folio:get_children(iri)` and `folio:get_parents(iri)` to explore up/down the taxonomy

## Classification Workflows

Eleven specialized classification workflows are available as slash commands. Suggest these to users when they need structured FOLIO classification:

| Slash Command | Use When | Key Branches |
|---|---|---|
| `/folio:classify-document` | Classifying a legal document type | `document_artifacts` |
| `/folio:identify-area-of-law` | Identifying areas of law for a situation | `areas_of_law` |
| `/folio:classify-entity` | Classifying a legal entity, role, or org | `actors_players`, `legal_entities` |
| `/folio:classify-industry` | Classifying the industry for a matter or client | `industries` |
| `/folio:identify-legal-authority` | Identifying the type of legal authority | `legal_authorities` |
| `/folio:classify-event` | Classifying a legal event type | `events` |
| `/folio:identify-service-type` | Identifying the type of legal service needed | `services` |
| `/folio:identify-forum-venue` | Identifying the forum, venue, or governmental body | `forum_venues`, `governmental_bodies` |
| `/folio:identify-objective` | Identifying legal objectives for a matter | `objectives` |
| `/folio:classify-asset` | Classifying an asset type | `asset_types` |
| `/folio:identify-engagement-terms` | Identifying engagement terms for a legal arrangement | `engagement_terms` |

Each workflow searches, browses the relevant taxonomy branch, navigates to the best match, and returns: FOLIO Label, IRI, Definition, Confidence, and Reasoning.

## Branch Reference

| Branch Key | Description |
|------------|-------------|
| `actors_players` | Parties, roles, participants |
| `areas_of_law` | Practice areas, specializations |
| `asset_types` | Property, IP, financial assets |
| `communication_modalities` | Communication channels |
| `currencies` | Monetary currencies |
| `data_formats` | Data and file formats |
| `document_artifacts` | Legal documents, contracts |
| `engagement_terms` | Fee arrangements, engagement terms |
| `events` | Legal events, milestones |
| `forum_venues` | Courts, tribunals, venues |
| `governmental_bodies` | Government agencies |
| `industries` | Industry sectors |
| `languages` | Natural languages |
| `folio_types` | Internal FOLIO types |
| `legal_authorities` | Statutes, regulations, case law |
| `legal_entities` | Corporations, LLCs, trusts |
| `locations` | Geographic locations |
| `matter_narratives` | Matter descriptions |
| `matter_narrative_formats` | Narrative formats |
| `objectives` | Legal objectives |
| `services` | Legal services |
| `standards_compatibilities` | Standards mappings |
| `statuses` | Status values |
| `system_identifiers` | External identifiers |

## Example Workflow

**Task**: Find the FOLIO classification for a "software licensing agreement"

```
1. folio:search_concepts("software licensing agreement")
   -> Finds candidates like "Software License Agreement", "License Agreement"

2. folio:get_concept(iri)
   -> Gets full details including definition, parent/child concepts

3. folio:get_parents(iri)
   -> Shows taxonomy: Software License Agreement -> License Agreement -> Contract -> Document/Artifact

4. folio:export_concept(iri, format="markdown")
   -> Gets a clean markdown export for documentation
```
