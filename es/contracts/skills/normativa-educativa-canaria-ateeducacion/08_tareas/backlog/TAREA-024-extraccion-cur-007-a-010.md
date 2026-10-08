---
id: TAREA-024
titulo: "Extracción curricular ESO: CUR-007 a CUR-010"
estado: "Hecha"
prioridad: "Alta"
tipo: "curriculo"
responsable: "@.agents/skills/analisis-curricular"
fecha_creacion: 2026-04-26
fecha_actualizacion: 2026-04-26
relacionadas: [CUR-007, CUR-008, CUR-009, CUR-010, NOR-005, NOR-003, FTE-009]
---

# TAREA-024 — Extracción curricular ESO: CUR-007 a CUR-010

## Objetivo

Completar la extracción curricular de cuatro materias de ESO Canarias siguiendo el patrón aplicado a CUR-001 y CUR-002:

- `CUR-007` — Educación en Valores Cívicos y Éticos.
- `CUR-008` — Educación Física.
- `CUR-009` — Educación Plástica, Visual y Audiovisual.
- `CUR-010` — Expresión Artística.

Vincular las fichas al marco autonómico (`NOR-005`, Decreto 30/2023) y al estatal (`NOR-003`, RD 217/2022), con la fuente principal `FTE-009`.

## Criterios de cierre

- `norma_base` y `fuente` apuntan a `NOR-005` y `FTE-009` en las cuatro fichas YAML y MD.
- Cursos de impartición confirmados: CUR-007 (1.º), CUR-008 (1.º a 4.º), CUR-009 (1.º a 3.º), CUR-010 (4.º, optativa).
- Volcados los enunciados literales de las competencias específicas con sus descriptores operativos del Perfil de Salida:
  - CUR-007: 4 competencias.
  - CUR-008: 5 competencias (acrónimo «sONrisas»).
  - CUR-009: 8 competencias.
  - CUR-010: 4 competencias.
- Detalle de criterios de evaluación, saberes básicos por bloques y descriptores operativos.
- `estado_extraccion` actualizado a `completado` en las cuatro fichas y en `06_indices/curriculos.yaml`.

## Notas

- Fecha de creación: 2026-04-26.
- Estado actual: Hecha.
- Resultado: las cuatro fichas (yaml + md) quedan cotejadas contra los anexos oficiales del Decreto 30/2023 publicados por la Consejería de Educación, Universidades, Cultura y Deportes del Gobierno de Canarias.
- Fuentes consultadas (fecha 2026-04-26):
  - https://www.gobiernodecanarias.org/boc/2023/058/001.html (BOC nº 58, Decreto 30/2023).
  - PDFs oficiales por materia bajo `https://www.gobiernodecanarias.org/cmsgob1/export/sites/educacion/web/_galerias/descargas/Secundaria/Ordenacion_curriculo/borrador_curriculo_2022/`.
- La materia Expresión Artística es **optativa de 4.º ESO** y profundiza los aprendizajes de `CUR-009` (Educación Plástica, Visual y Audiovisual). Se ha confirmado que está dentro del Decreto 30/2023 (no es una orden o decreto distinto).

## Coordinación con trabajo paralelo

- No se han creado nuevos IDs (todos los CUR-007 a CUR-010 ya estaban reservados).
- Se han tocado únicamente: las cuatro fichas yaml/md de CUR-007 a CUR-010, sus entradas en `06_indices/curriculos.yaml`, el bloque correspondiente de TAREA-024 en `status.yaml` y `06_indices/tareas.yaml`, y este propio fichero de tarea en backlog.
- No se han modificado las fichas ni índices de las TAREA-023, TAREA-026 ni TAREA-027 (otros agentes paralelos).
