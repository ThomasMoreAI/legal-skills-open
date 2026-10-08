# Data Models — Esquemas y ontología

Top-level entities (canonical model):
- LegalNorm
- LegalCase
- LegalConcept
- LegalActor
- LegalEvent
- Obligation

Modelo JSON de ejemplo (LegalNorm)

See: examples/schemas/legal_norm.schema.json

Relaciones (graph layer)

Usar triples RDF-like o property graph:
- (actor:trabajador_y) —[PART_OF]→ (concept:relacion_laboral)
- (event:despido) —[AFFECTS]→ (actor:trabajador_y)
- (norm:mx:lft:art47) —[REGULATES]→ (event:despido)
- (case:scjn:2024:xyz) —[INTERPRETS]→ (norm:mx:lft:art47)

Ontología

Ejemplo: Labor law
- Concept: Relación Laboral
  - Element: Subordinación
  - Element: Salario
  - Element: Prestación personal

Encoding

Soporte OWL-like en JSON para condiciones y efectos legales.
