# Finding Object Schema

Every finding emitted by the compliance-auditor MUST conform to this shape:

```json
{
  "id": "F-001",
  "check": "C3",
  "severity": "critical | high | medium | low | info",
  "entity_id": "<workspace entity id>",
  "entity_type": "<one of the 33 ontology entity types>",
  "evidence": "<verbatim text or paraphrase pointing at the gap>",
  "remediation": "<concrete next action — name the missing entity type or relationship>",
  "source_chunks": ["chunk-xxxxxxxx", "..."]
}
```

## Field semantics

- **`id`** — Sequential `F-001`, `F-002`, ... in emission order. Stable for a given run.
- **`check`** — Check ID (`C1`–`C8`) from SKILL.md.
- **`severity`** — From `references/severity_rubric.md`. Critical = will be rated Unacceptable; do not inflate.
- **`entity_id`** — The exact `entity_id` of the failing entity, as returned by `kg_entities` or `kg_query`. NEVER a free-form name.
- **`entity_type`** — Lowercase snake_case ontology type (e.g. `requirement`, `clause`, `evaluation_factor`).
- **`evidence`** — One sentence describing the gap. May quote chunk text in `"..."` or summarize. Must point at WHY the entity fails the check.
- **`remediation`** — One-line concrete action. Name the missing entity type or relationship (e.g. "Add a `SATISFIED_BY` edge to a `deliverable` entity").
- **`source_chunks`** — At least one `chunk_id` from `kg_chunks` or `kg_query` that justifies the finding. **Required for every finding.** No citation = no finding.

## Anti-patterns

- ❌ Aggregated findings ("12 requirements missing deliverables" as one row). Emit one finding per entity.
- ❌ Free-form `entity_id` like "the cybersecurity requirement". Use the actual entity ID.
- ❌ Empty `source_chunks`. If you cannot cite, you cannot raise.
- ❌ "Section L is missing" as evidence on a non-UCF solicitation. Map to entities, not headings.
