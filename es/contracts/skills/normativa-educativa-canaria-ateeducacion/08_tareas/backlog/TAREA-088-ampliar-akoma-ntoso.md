---
id: TAREA-088
titulo: "Ampliar los pilotos Akoma Ntoso del núcleo curricular"
estado: "Hecha"
prioridad: "Alta"
tipo: "corpus-ia"
responsable: "@.agents/skills/preparacion-corpus-ia"
fecha_creacion: 2026-08-22
fecha_actualizacion: 2026-08-22
fecha_cierre: 2026-08-22
relacionadas: [TAREA-087, NOR-003, NOR-004, NOR-005, NOR-006, NOR-007, NOR-043, NOR-047, NOR-079, NOR-080]
siguiente_accion: null
---

# TAREA-088 — Ampliar los pilotos Akoma Ntoso

## Objetivo

Extender la capa Akoma Ntoso más allá del artículo 1 de seis normas, sin inferir
estructura desde el texto plano.

## Criterios de cierre

- El catálogo `11_calidad/akoma_ntoso_pilotos.yaml` cubre artículos 1 y 2 del núcleo
  curricular (ESO, Bachillerato, Primaria e Infantil, estatal y canario) y de la
  ordenación de FP (`NOR-080`).
- Cada bloque se ha contrastado con BOE, BOC o la copia local trazable.
- Los XML se regeneran con `generar_interoperabilidad.py` y no se editan a mano.
- `python3 11_calidad/generar_interoperabilidad.py --check` y
  `python3 11_calidad/validar_corpus.py --sin-avisos` pasan.

## Notas

Consulta de las páginas oficiales del BOC (Decretos 211/2022 y 196/2022) y del BOE
(RD 659/2023 consolidado) el 2026-08-22. El artículo 2 de la LOFP (`NOR-007`) no se
incluye: son veinticuatro definiciones y exige una segmentación propia.
