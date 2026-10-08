---
name: folio-identify-forum-venue-alea-institute
title: Identify a Forum or Venue with FOLIO
description: Identify the appropriate forum, venue, or governmental body for a legal dispute or regulatory matter using the FOLIO ontology's forum_venues and governmental_bodies taxonomy branches. Use when the user needs to determine where a case should be filed, which court has jurisdiction, which regulatory body oversees a matter, or what type of dispute resolution forum applies — courts, arbitration panels, administrative agencies, regulatory bodies, or other tribunals.
author: alea-institute
author_url: https://github.com/alea-institute/folio-mcp/tree/main/skills/folio-identify-forum-venue
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Identify a Forum or Venue with FOLIO

Identify the appropriate forum, venue, or governmental body using the FOLIO ontology's `forum_venues` and `governmental_bodies` taxonomy branches.

## Workflow

Given a description of a legal dispute or regulatory matter, follow these steps:

1. **Search for matches**: Use `folio:search_concepts` with terms describing the forum, court, or regulatory body to find candidates in FOLIO.

2. **Browse forums and venues**: Use `folio:get_taxonomy_branch("forum_venues")` to see dispute forums (courts, tribunals), stock exchanges, and dispute venues.

3. **Browse governmental bodies**: Use `folio:get_taxonomy_branch("governmental_bodies")` to see federal, state, local, county, tribal, multinational, and regulatory bodies.

4. **Drill into the best matches**: Use `folio:get_children(iri)` on the most relevant categories to find specific forums or bodies.

5. **Get full details**: Use `folio:get_concept(iri)` on each match for the complete definition, translations, identifiers, and cross-references.

## Output Format

Return each applicable forum or body as:

- **FOLIO Label**: The official FOLIO concept name
- **FOLIO IRI**: The concept's unique identifier (e.g., `https://folio.openlegalstandard.org/...`)
- **Definition**: The FOLIO definition of this forum or body type
- **Branch**: `forum_venues` (courts, tribunals, exchanges) or `governmental_bodies` (agencies, regulators)
- **Relevance**: primary (most likely forum) or secondary (alternative or related)
- **Reasoning**: Brief explanation of why this forum or body applies

If multiple forums could apply (e.g., federal vs. state court, or court vs. arbitration), list all with their relevance.
