# Diario — 2026-08-22: JSON-LD, ELI y Akoma Ntoso en todo el corpus (TAREA-087)

## Hecho

La capa interoperable del PR de estándares se extendió al resto del corpus sin cambiar el
formato editorial Markdown/YAML.

- 27 fichas `NOR` con permalink ELI en el BOE reciben `uri_eli`. La URI se copió del
  permalink oficial; no se construyó a partir del título. Las 81 normas cuya fuente es el
  portal canario o el BOC quedan sin ELI (`PREG-013`).
- El generador publica tres grafos JSON-LD: legislación (108), currículos (58) y fuentes
  (117), más el catálogo `Dataset`.
- Akoma Ntoso deja de estar hardcodeado. El catálogo revisado
  `11_calidad/akoma_ntoso_pilotos.yaml` cubre el artículo 1 de `NOR-003`, `NOR-004`,
  `NOR-005`, `NOR-006`, `NOR-007` y `NOR-079`. El XML de `NOR-004` se conserva idéntico.

## IDs consumidos

- `TAREA-087`
- `PREG-013`
