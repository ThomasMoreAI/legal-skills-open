---
id: TAREA-096
titulo: "Ampliar la cobertura Akoma Ntoso a nuevas normas del corpus"
estado: "Hecha"
fecha_cierre: 2026-08-23
prioridad: "Media"
tipo: "corpus-ia"
responsable: "@.agents/skills/preparacion-corpus-ia"
fecha_creacion: 2026-08-23
fecha_actualizacion: 2026-08-23
relacionadas:
- TAREA-090
- TAREA-091
siguiente_accion: null
---

# TAREA-096 — Cobertura Akoma Ntoso ampliada

## Objetivo

Ampliar `11_calidad/akoma_ntoso_pilotos.yaml` con porciones Akoma Ntoso
validadas contra el XSD oficial (TAREA-089) para normas incorporadas o no
cubiertas hasta ahora.

## Criterios de cierre

Nuevas porciones generadas por el pipeline estándar y conformes al XSD;
`generar_interoperabilidad.py --check` en verde.

## Resultado

Añadido el piloto de `NOR-001` (LOE), la norma más citada del corpus: artículo 1
«Principios» completo con sus 21 párrafos (letras a a r, incluida a bis),
contrastado contra el texto consolidado del BOE. Total: **61 XML conformes al
XSD Akoma Ntoso 3.0**; `generar_interoperabilidad.py --check` en verde.
