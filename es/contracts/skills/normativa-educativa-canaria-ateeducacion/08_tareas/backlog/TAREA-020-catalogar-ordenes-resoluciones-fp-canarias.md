---
id: TAREA-020
titulo: "Catalogar las órdenes y resoluciones canarias de Formación Profesional listadas en FTE-015"
estado: "Hecha"
prioridad: "Media"
tipo: "analisis"
responsable: "@.agents/skills/experto-formacion-profesional"
fecha_creacion: 2026-04-26
fecha_actualizacion: 2026-04-26
fecha_cierre: 2026-04-26
relacionadas: [FTE-015, NOR-007, NOR-008, NOR-014, NOR-015, NOR-016, REL-012, TAREA-017]
---

# TAREA-020 — Catalogar las órdenes y resoluciones canarias de Formación Profesional listadas en FTE-015

## Objetivo

Continuar `TAREA-017` abriendo fichas `NOR-NNN` para las órdenes y resoluciones autonómicas de FP catalogadas en `FTE-015` que sigan vigentes, y resolver la verificación pendiente del `NOR-008` (Decreto 156/1996).

## Criterios de cierre

- Verificada y registrada la vigencia o derogación de `NOR-008`.
- Catalogadas como `NOR-NNN` las normas vigentes identificadas en `FTE-015`, con cita oficial completa, BOC, fechas y relaciones.
- Diferenciado claramente el alcance temporal (LOGSE / LOE / LOMLOE / LOFP) de cada norma.
- Catálogo de Reales Decretos de títulos de FP del Estado más relevantes para la oferta canaria identificado al menos como lista de cita oficial.
- Índices `06_indices/normativa.yaml` y `06_indices/relaciones.yaml` actualizados.

## Notas

- Fecha de creación: 2026-04-26
- Recurso principal: `FTE-015`. La página lista actualmente:
  - Ley 6/2014 (ya catalogada como `NOR-004`).
  - Decreto 156/1996 (catalogado como `NOR-008`, pendiente de verificación).
  - Orden de 22 de febrero de 2008 (acceso a FP del sistema educativo y enseñanzas deportivas).
  - Orden de 3 de diciembre de 2003 (modifica la Orden de 20 de octubre de 2000).
  - Orden de 20 de octubre de 2000 (evaluación de FP Específica).
  - Resoluciones varias (organización, funcionamiento, convalidaciones, optatividad, especialización) entre 2014 y 2026.
- Diferenciación con `DEC-0005`: las orientaciones y guías no normativas se catalogan como fuente, no como `NOR`.

## Cierre — 2026-04-26

- Catalogadas como `NOR-NNN` las tres órdenes vigentes listadas en `FTE-015`:
  - `NOR-014` — Orden de 22 de febrero de 2008 (acceso a FP del sistema educativo y enseñanzas deportivas).
  - `NOR-015` — Orden de 20 de octubre de 2000 (evaluación de FP Específica).
  - `NOR-016` — Orden de 3 de diciembre de 2003 (modifica la Orden de 20 de octubre de 2000).
- Registrada `REL-012` (NOR-016 modifica NOR-015).
- Coordinación con TAREA-014 (Centros): `NOR-009`..`NOR-013` y `REL-009`..`REL-011` se asignaron en paralelo a esa tarea, por lo que las órdenes de FP se han numerado a continuación (`NOR-014..016`, `REL-012`) preservando R10.
- Las tres fichas mantienen `estado_vigencia: Pendiente de verificación` conforme a `DEC-0003`, dado el cambio de marco posterior (LOE/LOMLOE y LOFP de 2022).
- Las resoluciones administrativas de organización (2014-2026) listadas en `FTE-015` quedan fuera del alcance de esta tarea por ser principalmente convocatorias/instrucciones organizativas. Podrán abordarse de forma específica en una tarea futura si la consulta operativa lo requiere.
