---
id: TAREA-012
titulo: "Normalizar el frontmatter YAML de FTE-001 a FTE-008"
estado: "Hecha"
prioridad: "Media"
tipo: "calidad-documental"
responsable: "@.agents/skills/control-calidad-documental"
fecha_creacion: 2026-04-26
fecha_actualizacion: 2026-04-26
relacionadas: [FTE-001, FTE-002, FTE-003, FTE-004, FTE-005, FTE-006, FTE-007, FTE-008, TAREA-008]
---

# TAREA-012 — Normalizar el frontmatter YAML de FTE-001 a FTE-008

## Objetivo

Aplicar a las fichas de fuente `FTE-001` a `FTE-008` la misma normalización ejecutada en `TAREA-008` para `NOR-001..NOR-004`: eliminar la sangría espuria de 4 espacios en frontmatter y cuerpo y dejar el frontmatter parseable por `yaml.safe_load`.

## Criterios de cierre

- Frontmatter de las ocho fichas parsea correctamente con `yaml.safe_load`.
- Cuerpo Markdown sin sangría inicial superflua.
- Sin pérdida de información respecto al estado anterior.
- Reflejada en `AGENTS.md` la regla de formato (sección 5.1).

## Notas

- Fecha de creación: 2026-04-26
- Fecha de cierre: 2026-04-26
- Resultado: las ocho fichas se han normalizado mediante el mismo script empleado en `TAREA-008` (FTEs no tienen bloque `relaciones:` anidado, solo un `relacionadas: [...]` plano, así que basta con dedentar). `FTE-009`, `FTE-010` y `FTE-011` ya estaban en el formato correcto y no requirieron cambios.
- Cambio asociado: codificada en `AGENTS.md` (sección 5.1) la regla de formato para frontmatter YAML.
