---
id: TAREA-038
titulo: "Extraer módulos profesionales FP — Familia Sanidad (CUR-046, CUR-047)"
estado: "Hecha"
prioridad: "Media"
tipo: "curriculo"
responsable: "@.agents/skills/experto-formacion-profesional"
fecha_creacion: 2026-04-26
fecha_actualizacion: 2026-04-26
relacionadas: [NOR-051, NOR-052, CUR-046, CUR-047, TAREA-037, PREG-005]
---

# TAREA-038 — Extraer módulos profesionales FP — Familia Sanidad

## Objetivo

Extraer la lista de módulos profesionales (con código, nombre y horas) de los dos ciclos formativos de la familia Sanidad catalogados en TAREA-037, actualizando los ficheros CUR placeholder y verificando las referencias BOE de NOR-051 y NOR-052.

## Ciclos procesados

### CUR-046 — Técnico en Cuidados Auxiliares de Enfermería (GM)

| Código | Módulo | Horas |
|--------|--------|-------|
| M01 | Operaciones administrativas y documentación sanitaria | 65 |
| M02 | Técnicas básicas de enfermería | 350 |
| M03 | Higiene del medio hospitalario y limpieza de material | 155 |
| M04 | Promoción de la salud y apoyo psicológico al paciente | 130 |
| M05 | Técnicas de ayuda odontológica/estomatológica | 130 |
| M06 | Relaciones en el equipo de trabajo | 65 |
| M07 | Formación y orientación laboral | 65 |
| FCT | Formación en centros de trabajo | 440 |

- **Total**: 8 módulos / 1.400 horas
- **estado_extraccion**: parcial (módulos con horas; capacidades terminales/CEs pendientes)
- **Nota**: Era LOGSE — usa capacidades terminales, no resultados de aprendizaje LOE.

### CUR-047 — T.S. Imagen para el Diagnóstico y Medicina Nuclear (GS)

| Código | Módulo | Horas | ECTS |
|--------|--------|-------|------|
| 1345 | Atención al paciente | 80 | 9 |
| 1346 | Fundamentos físicos y equipos | 135 | 13 |
| 1347 | Anatomía por la imagen | 135 | 13 |
| 1348 | Protección radiológica | 80 | 9 |
| 1349 | Técnicas de radiología simple | 65 | 8 |
| 1350 | Técnicas de radiología especial | 50 | 6 |
| 1351 | Técnicas de tomografía computarizada y ecografía | 60 | 7 |
| 1352 | Técnicas de imagen por resonancia magnética | 55 | 6 |
| 1353 | Técnicas de imagen en medicina nuclear | 60 | 7 |
| 1354 | Técnicas de radiofarmacia | 50 | 6 |
| 1355 | Proyecto de imagen para el diagnóstico y medicina nuclear | 25 | 5 |
| 1356 | Formación y orientación laboral | 50 | 5 |
| 1357 | Empresa e iniciativa emprendedora | 35 | 4 |
| 1358 | Formación en centros de trabajo | 220 | 22 |

- **Total**: 14 módulos / 2.000 horas / 120 ECTS
- **estado_extraccion**: parcial (módulos con horas y ECTS; RAs y CEs completos pendientes)

## Hallazgos importantes — Discrepancia de RD

Durante la verificación BOE se detectaron discrepancias en los números de RD catalogados en TAREA-037:

- **NOR-051**: el RD 1538/1995 no coincide con el BOE encontrado (BOE-A-1995-13533 = RD 546/1995).
- **NOR-052**: el RD 772/2014 corresponde a Radioterapia y Dosimetría; el título de Imagen para el Diagnóstico es el RD 770/2014 (BOE-A-2014-10067).

Se abrió **PREG-005** para investigar y corregir estas referencias.

## IDs consumidos

- **PREG**: PREG-005

## Pendientes para fase posterior

- Resolver PREG-005: confirmar números de RD correctos y actualizar NOR-051/052.
- Extraer capacidades terminales y criterios de evaluación de CUR-046 (era LOGSE).
- Extraer resultados de aprendizaje y criterios de evaluación completos de CUR-047.

## Coordinación con trabajo paralelo

- Esta TAREA se ejecutó en paralelo con TAREA-039, TAREA-040 y TAREA-041.
- Solo se tocaron archivos de la familia Sanidad (NOR-051, NOR-052, CUR-046, CUR-047).
