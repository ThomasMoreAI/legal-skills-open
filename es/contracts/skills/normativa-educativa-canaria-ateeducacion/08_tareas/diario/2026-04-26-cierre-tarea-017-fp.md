# Diario — 2026-04-26: Cierre TAREA-017 (FP) y TAREA-020

## TAREA-017 — Hecha

Se cierra la tarea de inventariado de normativa de Formación Profesional en Canarias con los siguientes resultados:

### Marco estatal vigente
- `FTE-016`: BOE consolidado de la Ley Orgánica 3/2022 (BOE-A-2022-5139).
- `NOR-007` (LOFP): ficha estatal con datos verificados (BOE n.º 78, 1-04-2022; entrada en vigor 21-04-2022; deroga LO 5/2002).
- `REL-008`: NOR-007 relaciona NOR-002 (LOMLOE) como base del marco actual de FP.

### Marco autonómico catalogado
Tomando como recurso `FTE-015` (rama de FP de Inspección Educativa de Canarias):
- `NOR-008`: Decreto 156/1996 (Ordenación general de FP Específica) — `Pendiente de verificación` (`DEC-0003`) por ser pre-LOMLOE/LOFP.
- `NOR-014`: Orden de 22 de febrero de 2008 (acceso a FP del sistema educativo y enseñanzas deportivas).
- `NOR-015`: Orden de 20 de octubre de 2000 (evaluación de FP Específica).
- `NOR-016`: Orden de 3 de diciembre de 2003 (modifica la Orden de 20 de octubre de 2000).
- `REL-012`: NOR-016 modifica NOR-015.

Las tres órdenes se incorporan con `estado_vigencia: Pendiente de verificación` por estar redactadas bajo el marco anterior a LOMLOE/LOFP.

### Coordinación con trabajo paralelo

- En paralelo, otra IA cerró `TAREA-014` (Centros) y catalogó `NOR-009`..`NOR-013` con sus `REL-009`..`REL-011` y `FTE-017`..`FTE-021`. Para preservar R10 (IDs estables, no reutilizar), las órdenes de FP se han numerado a continuación como `NOR-014..016` y la nueva relación como `REL-012`.

### Pendientes registradas para futuras iteraciones (no bloqueantes)

- Verificar la vigencia real del Decreto 156/1996 (`NOR-008`) y de las tres órdenes contra publicación en BOC.
- Catalogar los principales reales decretos estatales de títulos de FP relevantes para la oferta canaria.
- Catalogar las resoluciones administrativas de organización de FP listadas en `FTE-015` (2014-2026), si llega a requerirse para la consulta operativa.

## TAREA-020 — Hecha

Cubre la catalogación de las tres órdenes (`NOR-014`/`NOR-015`/`NOR-016`) y la relación `REL-012` que documentan el marco autonómico de FP previo a la LOFP. Se cierra junto con `TAREA-017`.
