---
id: TAREA-027
titulo: "Extracción curricular ESO: CUR-019 a CUR-023"
estado: "Hecha"
prioridad: "Alta"
tipo: "curriculo"
responsable: "@.agents/skills/analisis-curricular"
fecha_creacion: 2026-04-26
fecha_actualizacion: 2026-04-26
relacionadas: [CUR-019, CUR-020, CUR-021, CUR-022, CUR-023, NOR-005, FTE-009]
---

# TAREA-027 — Extracción curricular ESO: CUR-019 a CUR-023

## Objetivo

Iniciar la extracción curricular de cinco materias de la ESO Canarias bajo el marco del Decreto 30/2023 (`NOR-005`):

- `CUR-019` Matemáticas
- `CUR-020` Música
- `CUR-021` Segunda Lengua Extranjera
- `CUR-022` Tecnología
- `CUR-023` Tecnología y Digitalización

## Criterios de cierre

- `norma_base: NOR-005` y `fuente: FTE-009` en cada ficha.
- Cursos correctos según el articulado del Decreto 30/2023 (Capítulo II).
- `estado_extraccion: parcial` cuando metadata y cursos están confirmados pero el detalle del anexo II queda pendiente, o `completado` cuando los cuatro elementos obligatorios de `DEC-0004` estén cubiertos.
- Entradas correspondientes actualizadas en `06_indices/curriculos.yaml`.
- Registro de la tarea en `status.yaml`, `06_indices/tareas.yaml` y diario de cierre.

## Notas

- Fecha de creación: 2026-04-26.
- Estado actual: hecha (extracción parcial).
- Resultado: las cinco fichas reflejan ya `NOR-005` como norma base y `FTE-009` como fuente principal. Los cursos quedan confirmados contra el articulado del decreto:
  - Matemáticas: 1.º, 2.º y 3.º ESO; en 4.º como Matemáticas A o Matemáticas B (artículos 23.1.g y 25.1.e).
  - Música: 1.º y 2.º obligatoria; 3.º optativa (artículo 23.1.h); 4.º dentro de la opción E (artículo 25.3).
  - Segunda Lengua Extranjera: 1.º-3.º optativa (artículo 23.1.j); 4.º en la opción D (artículo 25.3).
  - Tecnología: 4.º ESO como materia ofertable (artículo 25.2.j).
  - Tecnología y Digitalización: 1.º y 2.º obligatoria; 3.º optativa (artículo 23.1.k).
- Las competencias específicas, los criterios de evaluación y los saberes básicos por curso quedan pendientes de cotejo con el anexo II del Decreto 30/2023 (PDF oficial del BOC, 1953 páginas) y se marcan como `[PENDIENTE]` siguiendo R15.
- Fuente consultada: índice HTML del BOC `https://www.gobiernodecanarias.org/boc/2023/058/001.html` y referencia al PDF oficial `https://sede.gobiernodecanarias.org/boc/boc-a-2023-058-848.pdf`. Fecha de consulta: 2026-04-26.

## Coordinación con trabajo paralelo

- No se han creado nuevos IDs `CUR-`, `NOR-`, `FTE-` ni `REL-`.
- Se ha consumido el ID `TAREA-027` y se ha registrado en `06_indices/tareas.yaml` y `status.yaml`.
- Se han modificado únicamente las cinco fichas asignadas (`CUR-019` a `CUR-023`), su entrada en `06_indices/curriculos.yaml`, los registros de `TAREA-027` y el diario de cierre.
