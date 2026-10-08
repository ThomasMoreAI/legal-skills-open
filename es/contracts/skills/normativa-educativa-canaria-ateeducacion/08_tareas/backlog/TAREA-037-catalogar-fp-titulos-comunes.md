---
id: TAREA-037
titulo: "Catalogar RD de títulos FP más comunes en Canarias (fase acotada)"
estado: "Hecha"
prioridad: "Media"
tipo: "curriculo"
responsable: "@.agents/skills/experto-formacion-profesional"
fecha_creacion: 2026-04-26
fecha_actualizacion: 2026-04-26
relacionadas: [NOR-007, FTE-015, FTE-016, FTE-054, NOR-051, NOR-052, NOR-053, NOR-054, NOR-055, NOR-056, NOR-057, NOR-058, CUR-046, CUR-047, CUR-048, CUR-049, CUR-050, CUR-051, CUR-052, CUR-053]
---

# TAREA-037 — Catalogar RD de títulos FP más comunes en Canarias (fase acotada)

## Objetivo

Catalogar los Reales Decretos de título de los ciclos formativos con mayor matrícula en Canarias, agrupados en cuatro familias profesionales prioritarias. No se extraen todavía los resultados de aprendizaje ni los criterios de evaluación completos (eso corresponde a una fase posterior). Esta tarea se limitó a:

1. Crear la estructura de carpetas `03_curriculos/fp/` (subcarpeta por familia).
2. Registrar FTE-054 para el catálogo de títulos en BOE.
3. Crear fichas NOR para los Reales Decretos de cada título seleccionado.
4. Crear fichas CUR placeholder (`estado_extraccion: "pendiente"`) para cada ciclo.
5. Actualizar los índices afectados.

## Familias y ciclos catalogados

### Sanidad
| Grado | Título | RD | BOE-A | CUR | NOR |
|-------|--------|-----|-------|-----|-----|
| GM | Cuidados Auxiliares de Enfermería | RD 1538/1995 | [PENDIENTE] | CUR-046 | NOR-051 |
| GS | Imagen para el Diagnóstico y Medicina Nuclear | RD 772/2014 | [PENDIENTE] | CUR-047 | NOR-052 |

### Administración y Gestión
| Grado | Título | RD | BOE-A | CUR | NOR |
|-------|--------|-----|-------|-----|-----|
| GM | Gestión Administrativa | RD 1631/2009 | BOE-A-2009-19148 | CUR-048 | NOR-053 |
| GS | Administración y Finanzas | RD 1584/2011 | BOE-A-2011-19533 | CUR-049 | NOR-054 |

### Informática y Comunicaciones
| Grado | Título | RD | BOE-A | CUR | NOR |
|-------|--------|-----|-------|-----|-----|
| GS | Desarrollo de Aplicaciones Multiplataforma (DAM) | RD 450/2010 | BOE-A-2010-8067 | CUR-050 | NOR-055 |
| GS | Desarrollo de Aplicaciones Web (DAW) | RD 686/2010 | BOE-A-2010-9269 | CUR-051 | NOR-056 |

### Servicios Socioculturales y a la Comunidad
| Grado | Título | RD | BOE-A | CUR | NOR |
|-------|--------|-----|-------|-----|-----|
| GS | Educación Infantil | RD 1394/2007 | BOE-A-2007-20201 | CUR-052 | NOR-057 |
| GS | Integración Social | RD 289/2023 | BOE-A-2023-7234 | CUR-053 | NOR-058 |

## IDs consumidos

- **FTE**: FTE-054
- **NOR**: NOR-051 a NOR-058
- **CUR**: CUR-046 a CUR-053

## Pendientes para fase posterior

- Verificar fechas exactas de publicación BOE para NOR-051, NOR-052, NOR-057, NOR-058.
- Verificar BOE-A de NOR-051 (RD 1538/1995) y NOR-052 (RD 772/2014, posible discrepancia con BOE-A-2014-10067).
- Extraer módulos profesionales, resultados de aprendizaje y criterios de evaluación (nueva TAREA).

## Coordinación con trabajo paralelo

- IDs utilizados: TAREA-037, FTE-054, NOR-051–NOR-058, CUR-046–CUR-053.
- Archivos tocados: `03_curriculos/fp/` (nuevo), fichas NOR y CUR (nuevas), índices.
- No se han tocado CUR-001 a CUR-045 ni TAREA-001 a TAREA-036.
