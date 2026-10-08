---
id: TAREA-097
titulo: "Revisión periódica de vigencia: auditoría de copias locales y contraste con el BOC"
estado: "Hecha"
fecha_cierre: 2026-08-23
prioridad: "Alta"
tipo: "control-vigencia"
responsable: "@.agents/skills/control-vigencia"
fecha_creacion: 2026-08-23
fecha_actualizacion: 2026-08-23
relacionadas:
- TAREA-094
- DEC-0011
siguiente_accion: null
---

# TAREA-097 — Revisión periódica de vigencia (2026-08-23)

## Objetivo

Ejecutar la revisión periódica que exige `DEC-0011`: auditoría de correspondencia
de las copias locales (`reexportar_texto_oficial.py --auditar`) y contraste con
los sumarios oficiales.

## Primer hallazgo

La auditoría del 2026-08-23 detectó que los títulos de `NOR-114` y `NOR-115`
no coinciden literalmente con los títulos oficiales del BOC (coincidencia 44 %
y 52 %): fueron registrados parafraseados. R7 exige el título oficial; se
corrigen en esta tarea.

## Criterios de cierre

Auditoría sin fichas «a revisar» o con cada desviación corregida/documentada;
informe de la revisión en `11_calidad/informes/`.

## Resultado

Auditoría inicial: 68 fichas contrastadas, 2 a revisar (títulos no literales en
NOR-114/115). Corregidos con la redacción literal del BOC en ficha e índice.
Re-ejecución: **0 a revisar**. Informe: `11_calidad/informes/2026-08-23-revision-vigencia.md`.

