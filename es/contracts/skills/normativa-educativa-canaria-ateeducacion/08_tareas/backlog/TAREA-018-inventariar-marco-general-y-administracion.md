---
id: TAREA-018
titulo: "Inventariar y catalogar normativa de Marco general, Administración y Servicios complementarios"
estado: "Hecha"
prioridad: "Media"
tipo: "analisis"
responsable: "@.agents/skills/experto-normativa-canaria"
fecha_creacion: 2026-04-26
fecha_actualizacion: 2026-04-26
relacionadas: [FTE-013, FTE-034, FTE-035, FTE-036, FTE-037, FTE-038, FTE-039, NOR-004, NOR-010, NOR-027, NOR-031, NOR-032, NOR-033, NOR-034, NOR-035, NOR-036, REL-028, REL-029, REL-030, REL-031, REL-032, REL-033, DEC-0005]
---

# TAREA-018 — Inventariar y catalogar normativa de Marco general, Administración y Servicios complementarios

## Objetivo

Cerrar el inventario inicial del corpus revisando los apartados restantes del portal de Inspección Educativa (`FTE-013`): marco general, administración educativa, orientaciones-programas-protocolos y servicios complementarios (transporte, comedor, residencias, etc.).

## Criterios de cierre

- Inventario y fichas `NOR-NNN` para las normas vigentes en cada uno de los apartados que aún no estén cubiertos por TAREA-014, TAREA-015, TAREA-016 o TAREA-017.
- Diferenciación clara entre normativa y orientaciones/protocolos no normativos según `DEC-0005`.
- `06_indices/normativa.yaml` y relaciones actualizados.

## Notas

- Fecha de creación: 2026-04-26
- Recurso: `FTE-013` apartados `/marco_general/`, `/administracion/`, `/orientaciones_programas_protocolos/`, `/servicios_complementarios/`.
- Las orientaciones, guías y protocolos no normativos se incorporarán solo como `tipo_fuente: orientacion-no-normativa` conforme a `DEC-0005`, no como `NOR-NNN`.

## Resultado

- Catalogadas fuentes `FTE-034` a `FTE-039`.
- Creadas fichas normativas `NOR-031` a `NOR-036`.
- Registradas relaciones `REL-028` a `REL-033`.
- Aplicado `DEC-0005`: no se han creado fichas `NOR` para orientaciones, guías, protocolos o instrucciones anuales de curso.

## Coordinación con trabajo paralelo

- IDs consumidos en esta tarea: `FTE-034` a `FTE-039`, `NOR-031` a `NOR-036`, `REL-028` a `REL-033`.
- No se han tocado archivos de `TAREA-019`, que permanece en progreso.
