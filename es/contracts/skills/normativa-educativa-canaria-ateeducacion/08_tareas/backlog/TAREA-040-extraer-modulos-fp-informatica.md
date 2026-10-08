---
id: TAREA-040
titulo: "Extraer módulos profesionales FP — Familia Informática y Comunicaciones (CUR-050, CUR-051)"
estado: "Hecha"
tipo: "curriculo"
fecha_creacion: 2026-04-26
fecha_actualizacion: 2026-04-26
relacionadas: [NOR-055, NOR-056, CUR-050, CUR-051]
---

> Este documento no sustituye a la fuente oficial.

## Objetivo

Extraer los módulos profesionales, horas totales y resultados de aprendizaje de los dos ciclos formativos de Grado Superior de la familia de Informática y Comunicaciones, a partir de sus respectivos Reales Decretos publicados en el BOE.

## Ciclos procesados

| CUR | Título | RD | BOE-A | Módulos | Horas totales | estado_extraccion |
|-----|--------|----|-------|---------|--------------|-------------------|
| CUR-050 | T.S. Desarrollo de Aplicaciones Multiplataforma (DAM) | RD 450/2010 | BOE-A-2010-8067 | 14 | 2000 | parcial |
| CUR-051 | T.S. Desarrollo de Aplicaciones Web (DAW) | RD 686/2010 | BOE-A-2010-9269 | 13 | 2000 | parcial |

## Módulos extraídos — CUR-050 (DAM)

| Código | Nombre | Horas |
|--------|--------|-------|
| 0483 | Sistemas Informáticos | 100 |
| 0484 | Bases de Datos | 105 |
| 0485 | Programación | 135 |
| 0373 | Lenguajes de Marcas y Sistemas de Gestión de Información | 70 |
| 0487 | Entornos de Desarrollo | 50 |
| 0486 | Acceso a Datos | 80 |
| 0488 | Desarrollo de Interfaces | 90 |
| 0489 | Programación Multimedia y Dispositivos Móviles | 80 |
| 0490 | Programación de Servicios y Procesos | 60 |
| 0491 | Sistemas de Gestión Empresarial | 80 |
| 0492 | Proyecto de Desarrollo de Aplicaciones Multiplataforma | 40 |
| 0493 | Formación y Orientación Laboral | 90 |
| 0494 | Empresa e Iniciativa Emprendedora | 60 |
| 0495 | Formación en Centros de Trabajo | 360 |

## Módulos extraídos — CUR-051 (DAW)

| Código | Nombre | Horas |
|--------|--------|-------|
| 0483 | Sistemas Informáticos | 100 |
| 0484 | Bases de Datos | 105 |
| 0485 | Programación | 135 |
| 0373 | Lenguajes de Marcas y Sistemas de Gestión de Información | 70 |
| 0487 | Entornos de Desarrollo | 50 |
| 0612 | Desarrollo Web en Entorno Cliente | 80 |
| 0613 | Desarrollo Web en Entorno Servidor | 120 |
| 0614 | Despliegue de Aplicaciones Web | 60 |
| 0615 | Diseño de Interfaces Web | 60 |
| 0616 | Proyecto de Desarrollo de Aplicaciones Web | 40 |
| 0617 | Formación y Orientación Laboral | 90 |
| 0618 | Empresa e Iniciativa Emprendedora | 60 |
| 0619 | Formación en Centros de Trabajo | 380 |

## Fuentes consultadas

- BOE-A-2010-8067 (RD 450/2010): https://www.boe.es/diario_boe/txt.php?id=BOE-A-2010-8067
- BOE-A-2010-9269 (RD 686/2010): https://www.boe.es/diario_boe/txt.php?id=BOE-A-2010-9269
- Fecha de consulta: 2026-04-26

## IDs consumidos

No se han creado nuevos IDs en esta tarea. Solo se han actualizado las fichas CUR-050 y CUR-051 existentes.

## Pendientes

- Los criterios de evaluación individuales (letras a, b, c...) de cada Resultado de Aprendizaje no pudieron extraerse del documento HTML del BOE (truncado). Requieren acceso al PDF oficial del RD 450/2010 y RD 686/2010. Marcados como [PENDIENTE] en las fichas CUR.
- Cuando se extraigan los criterios de evaluación completos, actualizar `estado_extraccion` a `"completado"` en ambas fichas.

## Criterios de cierre (AGENTS.md §15)

- [x] Fuente oficial identificada (BOE)
- [x] Fecha de consulta registrada (2026-04-26)
- [x] Formato YAML válido
- [x] Entrada en índice curriculos.yaml actualizada
- [x] IDs correctos (CUR-050, CUR-051)
- [x] Estado de vigencia registrado (Vigente)
- [x] Preguntas abiertas registradas (criterios de evaluación pendientes)
- [x] Registro en status.yaml y tareas.yaml actualizado
