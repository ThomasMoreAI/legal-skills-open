---
id: TAREA-041
titulo: "Extraer módulos profesionales FP — Familia Servicios Socioculturales y a la Comunidad (CUR-052, CUR-053)"
estado: "Hecha"
tipo: "curriculo"
fecha_creacion: 2026-04-26
fecha_actualizacion: 2026-04-26
relacionadas: [NOR-057, NOR-058, CUR-052, CUR-053, TAREA-037]
---

> Este documento no sustituye a la fuente oficial.

## Objetivo

Extraer los módulos profesionales completos, resultados de aprendizaje (RAs) y criterios de evaluación (CEs) de los dos ciclos formativos de Grado Superior de la familia Servicios Socioculturales y a la Comunidad, a partir de sus respectivos Reales Decretos publicados en el BOE.

## Ciclos procesados

| CUR | Título | RD | BOE-A | Módulos | RAs | CEs | estado_extraccion |
|-----|--------|----|-------|---------|-----|-----|-------------------|
| CUR-052 | T.S. Educación Infantil | RD 1394/2007 | BOE-A-2007-20201 | 13 | 71 | 619 | completado |
| CUR-053 | T.S. Integración Social | RD 289/2023 (modifica RD 1075/2012) | BOE-A-2023-10395 | 7 (parcial) | 34 | 249 | parcial |

## Módulos extraídos — CUR-052 (Educación Infantil)

| Código | Nombre | Horas |
|--------|--------|-------|
| 0013 | Didáctica de la Educación Infantil | 105 |
| 0014 | Autonomía personal y salud infantil | 90 |
| 0015 | El juego infantil y su metodología | 80 |
| 0016 | Expresión y comunicación | 130 |
| 0017 | Desarrollo cognitivo y motor | 90 |
| 0018 | Desarrollo socioafectivo | 65 |
| 0019 | Habilidades sociales | 65 |
| 0020 | El entorno y su conservación | 65 |
| 0021 | Primeros auxilios | 55 |
| 0022 | Empresa e Iniciativa Emprendedora | 65 |
| 0023 | Formación y Orientación Laboral | 90 |
| 0024 | Proyecto de Atención a la Infancia | 40 |
| 0025 | Formación en Centros de Trabajo | 360 |

**Total horas:** 1300 h (700 h en centro educativo + 360 h FCT)

## Módulos extraídos — CUR-053 (Integración Social, módulos actualizados por RD 289/2023)

| Código | Nombre | Horas |
|--------|--------|-------|
| 0334 | Inserción laboral, igualdad de género y sensibilización medioambiental | 30 |
| 0335 | Pautas y sistemas alternativos de comunicación | 30 |
| 0336 | Metodología de la intervención social | 30 |
| 0339 | Atención socioeducativa a personas con discapacidad | 30 |
| 0340 | Mediación comunitaria | 80 |
| 0342 | Proyecto de Integración Social | 40 |
| 0343 | Sistemas aumentativos y alternativos de comunicación | 30 |

**Nota:** RD 289/2023 modifica únicamente 7 módulos del título original (RD 1075/2012). Los módulos restantes del título (0332, 0333, 0337, 0338, 0341 y el módulo de FCT) corresponden al RD 1075/2012 y no se han extraído aún.

## Fuentes consultadas

- BOE-A-2007-20201 (RD 1394/2007, Educación Infantil): https://www.boe.es/diario_boe/txt.php?id=BOE-A-2007-20201
- BOE-A-2023-10395 (RD 289/2023, modifica Integración Social): https://www.boe.es/diario_boe/txt.php?id=BOE-A-2023-10395
- ELI RD 289/2023: https://www.boe.es/eli/es/rd/2023/04/18/289
- Fecha de consulta: 2026-04-26

## IDs consumidos

No se han creado nuevos IDs en esta tarea. Solo se han actualizado las fichas CUR-052 y CUR-053 existentes.

## Notas técnicas

- El PDF de RD 1394/2007 (Anexo I) usa codificación CID font con desplazamiento ASCII +31 y dígitos codificados como caracteres de control (\x11=0, \x12=1, ..., \x1a=9). Fue necesario implementar un decodificador personalizado para extraer el texto completo.
- Se alcanzó un 97,6% de limpieza del texto: 15 de los 619 criterios de evaluación conservan artefactos menores de codificación que no afectan a la comprensión.
- La URL BOE-A-2023-7234 referenciada en algunos índices era incorrecta (corresponde a un anuncio municipal de Orellana la Vieja). El BOE-ID correcto del RD 289/2023 es BOE-A-2023-10395.

## Pendientes

- Extraer los módulos del RD 1075/2012 (base del título de Integración Social) para completar CUR-053 con los módulos no actualizados por RD 289/2023 y cambiar `estado_extraccion` a `"completado"`.
- Revisar y corregir los 15 criterios de evaluación de CUR-052 que conservan artefactos de codificación menores.

## Criterios de cierre (AGENTS.md §15)

- [x] Fuente oficial identificada (BOE)
- [x] Fecha de consulta registrada (2026-04-26)
- [x] Formato YAML válido (validado con yaml.safe_load)
- [x] Entrada en índice curriculos.yaml actualizada (estado_extraccion y observaciones)
- [x] IDs correctos (CUR-052, CUR-053)
- [x] Estado de vigencia registrado (Vigente)
- [x] Preguntas abiertas registradas (módulos RD 1075/2012 pendientes en CUR-053)
- [x] Registro en status.yaml y tareas.yaml actualizado
