---
id: TAREA-026
titulo: "Extracción curricular ESO: CUR-015 a CUR-018"
estado: "Hecha"
prioridad: "Alta"
tipo: "curriculo"
responsable: "@.agents/skills/analisis-curricular"
fecha_creacion: 2026-04-26
fecha_actualizacion: 2026-04-26
relacionadas: [CUR-015, CUR-016, CUR-017, CUR-018, NOR-005, FTE-009]
---

# TAREA-026 — Extracción curricular ESO: CUR-015 a CUR-018

## Objetivo

Iniciar la extracción curricular de cuatro materias de ESO en el ámbito autonómico canario:

- `CUR-015` — Historia y Geografía de Canarias (3.º ESO)
- `CUR-016` — Latín (4.º ESO)
- `CUR-017` — Lengua Castellana y Literatura (1.º a 4.º ESO)
- `CUR-018` — Lengua Extranjera (1.º a 4.º ESO)

Vincular las cuatro fichas al marco autonómico (`NOR-005`, Decreto 30/2023) y, donde corresponda, al marco estatal (`NOR-003`, RD 217/2022).

## Criterios de cierre

- `norma_base` y `fuente` apuntan a `NOR-005` y `FTE-009` para las cuatro fichas.
- Para cada CUR, los cursos confirmados se documentan a partir del articulado del Decreto 30/2023.
- Los enunciados literales de competencias específicas, criterios de evaluación, saberes básicos y descriptores operativos del anexo del decreto quedan marcados como `[PENDIENTE]` cuando no han podido cotejarse en esta extracción inicial.
- `estado_extraccion` actualizado a `parcial` con observaciones detalladas.
- Entradas de `06_indices/curriculos.yaml` actualizadas para los cuatro IDs.

## Notas

- Fecha de creación: 2026-04-26.
- Estado actual: hecha.
- Resultado:
    - `CUR-015` queda registrada como materia propia canaria de 3.º ESO conforme al artículo 23.5 del Decreto 30/2023; sin equivalente directo en el RD 217/2022.
    - `CUR-016` queda registrada como materia optativa de 4.º ESO conforme al artículo 25.2.g del Decreto 30/2023 (opción D).
    - `CUR-017` queda registrada como materia troncal de 1.º a 4.º ESO conforme a los artículos 23.1.f y 25.1.c del Decreto 30/2023.
    - `CUR-018` queda registrada como materia troncal de 1.º a 4.º ESO conforme a los artículos 23.1.i y 25.1.d del Decreto 30/2023.
- Fuente consultada: articulado del Decreto 30/2023 publicado en el BOC n.º 58 de 23 de marzo de 2023, vía `https://www.gobiernodecanarias.org/boc/2023/058/001.html`. El cotejo del anexo (competencias específicas, criterios de evaluación literales, saberes básicos) queda como tarea de seguimiento.
- Esta tarea sigue el mismo patrón que `TAREA-010` para CUR-001 y `TAREA-019` para CUR-002.

## Coordinación con trabajo paralelo

- No se han creado nuevos IDs distintos de TAREA-026.
- Se han tocado únicamente: `CUR-015`, `CUR-016`, `CUR-017`, `CUR-018` (sus YAML y MD), las entradas correspondientes en `06_indices/curriculos.yaml`, los registros de TAREA-026 en `status.yaml` y `06_indices/tareas.yaml`, y este propio fichero de TAREA-026.
- No se han modificado bloques de tareas paralelas (TAREA-023, TAREA-027) ni fichas de otras CUR.
