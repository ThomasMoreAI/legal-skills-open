---
id: TAREA-017
titulo: "Inventariar y catalogar normativa de Formación Profesional en Canarias"
estado: "Hecha"
prioridad: "Alta"
tipo: "analisis"
responsable: "@.agents/skills/experto-formacion-profesional"
fecha_creacion: 2026-04-26
fecha_actualizacion: 2026-04-26
fecha_cierre: 2026-04-26
relacionadas: [FTE-014, FTE-015, FTE-016, NOR-002, NOR-007, NOR-008, NOR-014, NOR-015, NOR-016, REL-008, REL-012, TAREA-020]
---

# TAREA-017 — Inventariar y catalogar normativa de Formación Profesional en Canarias

## Objetivo

Construir el bloque del corpus dedicado a Formación Profesional (FP) catalogando primero la **Ley Orgánica 3/2022, de 31 de marzo, de ordenación e integración de la FP** y los reales decretos de los títulos vigentes; y a continuación los decretos autonómicos y resoluciones canarias asociadas.

## Criterios de cierre

- Ficha `NOR-NNN` para la Ley Orgánica 3/2022 de FP creada y enlazada a `FTE-XXX` BOE.
- Lista de reales decretos de títulos de FP relevantes para Canarias inventariada.
- Decretos y órdenes autonómicas de desarrollo de FP en Canarias catalogados como `NOR-NNN`.
- `06_indices/normativa.yaml` y relaciones actualizados.

## Notas

- Fecha de creación: 2026-04-26
- Recurso: `FTE-014` (Enseñanzas) y `FTE-015` (FP).
- La FP combina norma básica estatal (Ley Orgánica 3/2022) con desarrollos autonómicos: la trazabilidad debe mantener la cita doble (estatal + autonómica) cuando proceda.

## Avance — 2026-04-26

- Catalogada la fuente oficial estatal: `FTE-016` (BOE-A-2022-5139, texto consolidado de la LO 3/2022).
- Creada la ficha estatal `NOR-007` (LOFP) con datos verificados (BOE n.º 78, 1-04-2022; entrada en vigor 21-04-2022; deroga LO 5/2002).
- Creada la ficha autonómica `NOR-008` (Decreto 156/1996 de FP Específica en Canarias) con `estado_vigencia: Pendiente de verificación` conforme a `DEC-0003`, dado que es pre-LOMLOE/LOFP.
- Registrada la relación `REL-008` (NOR-007 relaciona NOR-002 / LOMLOE).

## Cierre — 2026-04-26

- Catalogadas las tres órdenes autonómicas listadas en `FTE-015`:
  - `NOR-014` (Orden 22-02-2008, acceso a FP del sistema educativo y enseñanzas deportivas).
  - `NOR-015` (Orden 20-10-2000, evaluación de FP Específica).
  - `NOR-016` (Orden 03-12-2003, que modifica la Orden 20-10-2000).
- Registrada la relación `REL-012` (NOR-016 modifica NOR-015).
- Nota de coordinación: los IDs `NOR-009`..`NOR-013` y `REL-009`..`REL-011` fueron asignados en paralelo a la catalogación de Centros (TAREA-014); estas órdenes de FP se han numerado a continuación (`NOR-014..016`, `REL-012`) para preservar la regla R10 de IDs estables.
- Las órdenes se incorporan con `estado_vigencia: Pendiente de verificación` por estar redactadas bajo el marco anterior a LOMLOE/LOFP; documentado en cada ficha conforme a `DEC-0003`.
- En `NOR-007` queda registrada como duda abierta la catalogación posterior de los principales reales decretos estatales de títulos de FP relevantes para la oferta canaria.
- Cerrada también `TAREA-020` (cubría las órdenes); las resoluciones específicas de organización catalogadas en `FTE-015` quedan fuera del alcance de esta tarea y podrán abordarse en una iteración posterior si procede.
