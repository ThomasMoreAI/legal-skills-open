---
id: TAREA-011
titulo: "Cotejar el anexo de Biología y Geología del Decreto 30/2023 contra la extracción inicial de CUR-001"
estado: "Hecha"
prioridad: "Alta"
tipo: "curriculo"
responsable: "@.agents/skills/analisis-curricular"
fecha_creacion: 2026-04-26
fecha_actualizacion: 2026-04-26
fecha_cierre: 2026-04-26
relacionadas: [CUR-001, NOR-005, FTE-009, TAREA-010, DEC-0004]
---

# TAREA-011 — Cotejar el anexo de Biología y Geología del Decreto 30/2023 contra la extracción inicial de CUR-001

## Objetivo

Sustituir los enunciados resumidos de las competencias específicas y los `[PENDIENTE]` actuales de `CUR-001` por el contenido literal del anexo del Decreto 30/2023 publicado en BOC (`FTE-009`), completando los cuatro elementos obligatorios de `DEC-0004` para llevar la ficha a `estado_extraccion: completado`.

## Criterios de cierre

- [x] Localizada la URL o PDF oficial del anexo de Biología y Geología del Decreto 30/2023 publicado en BOC.
- [x] Sustituidos los `enunciado_oficial: null` de cada competencia específica (C1-C6) por el enunciado literal del decreto.
- [x] Volcados los criterios de evaluación literales por curso (1.º, 3.º y 4.º).
- [x] Volcados los descriptores operativos del Perfil de salida vinculados a cada competencia y criterio.
- [x] Detalle de saberes básicos por bloque y curso completado.
- [x] `estado_extraccion` actualizado a `completado` en `CUR-001` (YAML, MD e índice `06_indices/curriculos.yaml`).
- [x] Eliminadas o resueltas las marcas `[INTERPRETACIÓN]` y `[PENDIENTE]` que dependían del cotejo.

## Notas

- Fecha de creación: 2026-04-26
- Origen: cierre parcial de `TAREA-010`, que dejó la extracción en estado parcial a partir del documento `borrador_curriculo_2022/Biologia_geologia_ESO.pdf`.
- Riesgo conocido: el documento usado para la extracción inicial es un borrador previo a la publicación del Decreto 30/2023. La cotejación puede requerir ajustes en C1-C6 o en la organización de bloques.
- Dependencia: identificar la URL pública del anexo (sede electrónica BOC o PDF descargable). Si no es accesible vía WebFetch, registrar la limitación y mantener `[PENDIENTE]`.
