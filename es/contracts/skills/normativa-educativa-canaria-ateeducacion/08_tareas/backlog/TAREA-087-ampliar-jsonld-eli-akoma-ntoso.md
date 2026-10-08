---
id: TAREA-087
titulo: "Ampliar JSON-LD, ELI y Akoma Ntoso al resto del corpus"
estado: "Hecha"
prioridad: "Alta"
tipo: "corpus-ia"
responsable: "@.agents/skills/preparacion-corpus-ia"
fecha_creacion: 2026-08-22
fecha_actualizacion: 2026-08-22
fecha_cierre: 2026-08-22
relacionadas: [TAREA-063, NOR-001, NOR-003, NOR-004, NOR-005, NOR-006, NOR-007, NOR-079, PREG-013]
siguiente_accion: null
---

# TAREA-087 — Ampliar JSON-LD, ELI y Akoma Ntoso al resto del corpus

## Objetivo

Extender al corpus completo la capa interoperable introducida para `NOR-004`: URI ELI
confirmada por el publicador, grafos JSON-LD generados y pilotos Akoma Ntoso revisados.

## Criterios de cierre

- Las fichas `NOR` con permalink ELI en la fuente oficial del BOE tienen `uri_eli`.
- El generador publica `legislacion.jsonld`, `curriculos.jsonld`, `fuentes.jsonld` y el catálogo.
- Los XML Akoma Ntoso salen de `11_calidad/akoma_ntoso_pilotos.yaml` y no se editan a mano.
- `python3 11_calidad/validar_corpus.py` y `python3 11_calidad/generar_interoperabilidad.py --check` pasan.
- La duda sobre ELI en el BOC queda registrada como `PREG-013`.

## Notas

Consulta de permalinks ELI del BOE: 2026-08-22. No se infiere ninguna URI a partir del título
o de la apariencia de la URL. El BOC no publica permalink ELI en las páginas revisadas.
