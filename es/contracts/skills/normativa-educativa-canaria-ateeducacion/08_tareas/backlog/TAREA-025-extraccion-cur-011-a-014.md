---
id: TAREA-025
titulo: "Extracción curricular ESO: CUR-011 a CUR-014"
estado: "Hecha"
prioridad: "Alta"
tipo: "curriculo"
responsable: "@.agents/skills/analisis-curricular"
fecha_creacion: 2026-04-26
fecha_actualizacion: 2026-04-26
relacionadas: [CUR-011, CUR-012, CUR-013, CUR-014, NOR-005, FTE-009]
---

# TAREA-025 — Extracción curricular ESO: CUR-011 a CUR-014

## Objetivo

Iniciar la extracción curricular de cuatro materias de la ESO según el Decreto 30/2023 (`NOR-005`) y vincular las fichas a la fuente oficial (`FTE-009`):

- `CUR-011` — Filosofía
- `CUR-012` — Física y Química
- `CUR-013` — Formación y Orientación Personal y Profesional
- `CUR-014` — Geografía e Historia

## Criterios de cierre

- `norma_base: NOR-005` y `fuente: FTE-009` confirmados en cada ficha.
- Curso(s) de impartición identificados en el articulado del Decreto 30/2023 (arts. 23, 24 y 25).
- `estado_extraccion: "iniciado"` mientras esté pendiente el cotejo del anexo curricular de cada materia.
- Detalle de competencias específicas, criterios de evaluación y saberes básicos marcado como `[PENDIENTE]` hasta cotejo del anexo correspondiente del decreto.
- Entradas correspondientes actualizadas en `06_indices/curriculos.yaml`.

## Notas

- Fecha de creación: 2026-04-26.
- Fuente consultada para el encuadre: índice del BOC n.º 58, de 23 de marzo de 2023 (`https://www.gobiernodecanarias.org/boc/2023/058/001.html`).
- El detalle textual de los anexos del Decreto 30/2023 quedó pendiente de cotejo dado que el PDF oficial completo (1953 páginas) no admitió extracción literal automática durante la sesión; las fichas quedan, por tanto, en `iniciado` y no en `completado`.
- Materias y encuadre normativo identificados:
  - **Filosofía**: optativa de 4.º ESO (art. 25.5 del Decreto 30/2023).
  - **Física y Química**: común de 2.º y 3.º ESO (art. 23.1.d) y disponible en 4.º ESO (art. 24).
  - **Formación y Orientación Personal y Profesional**: 4.º ESO (art. 25), alineada con el carácter orientador del último curso.
  - **Geografía e Historia**: común de 1.º, 2.º y 3.º ESO (art. 23.1.e) y obligatoria en 4.º ESO (art. 24).

## Coordinación con trabajo paralelo

- No se han creado nuevos IDs distintos de `TAREA-025`.
- Se han tocado únicamente las cuatro fichas `CUR-011` a `CUR-014`, sus entradas en `06_indices/curriculos.yaml`, el registro de `TAREA-025` en `status.yaml` y `06_indices/tareas.yaml` y el diario de cierre correspondiente.
- No se han modificado las entradas de tareas ajenas en curso (TAREA-023, TAREA-027).

## Próximos pasos sugeridos

- Cotejo literal del anexo de cada materia en el Decreto 30/2023, con incorporación de competencias específicas, criterios de evaluación, descriptores operativos y bloques de saberes básicos. Cuando se complete el cotejo, actualizar `estado_extraccion` a `completado`.
