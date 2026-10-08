---
id: TAREA-008
titulo: "Normalizar el frontmatter YAML de NOR-001 a NOR-004"
estado: "Hecha"
prioridad: "Media"
tipo: "calidad-documental"
responsable: "@.agents/skills/control-calidad-documental"
fecha_creacion: 2026-04-26
fecha_actualizacion: 2026-04-26
relacionadas: [NOR-001, NOR-002, NOR-003, NOR-004]
---

# TAREA-008 — Normalizar el frontmatter YAML de NOR-001 a NOR-004

## Objetivo

Eliminar la sangría espuria de 4 espacios y reindentar correctamente el bloque `relaciones:` en las fichas `NOR-001`, `NOR-002`, `NOR-003` y `NOR-004` para que el frontmatter sea YAML válido y coherente con `plantilla-norma.md`.

## Criterios de cierre

- Frontmatter de las cuatro fichas parsea correctamente con `yaml.safe_load`.
- Bloque `relaciones:` mantiene sus seis claves (`desarrolla_a`, `modificada_por`, `modifica_a`, `deroga_a`, `derogada_por`, `relacionada_con`).
- Cuerpo Markdown sin sangría inicial superflua.
- Sin pérdida de información respecto al estado anterior.

## Notas

- Fecha de creación: 2026-04-26
- Fecha de cierre: 2026-04-26
- Resultado: las cuatro fichas se han normalizado mediante un script Python que elimina la sangría inicial y reindenta el bloque `relaciones:` con dos espacios. Verificación con `yaml.safe_load` confirma que el frontmatter es válido y que los seis tipos de relación se preservan en cada ficha.
- Pendiente como mejora futura: aplicar la misma normalización a las fichas `FTE-005` a `FTE-010`, que comparten el mismo defecto de sangría inicial.
