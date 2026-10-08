---
id: TAREA-091
titulo: "Auditar y normalizar el corpus: estados de tarea, resúmenes sangrados, chunks fuera de esquema, frontmatters ausentes y puntos ciegos del validador"
estado: "Hecha"
prioridad: "Alta"
tipo: "calidad-documental"
responsable: "@.agents/skills/control-calidad-documental"
fecha_creacion: 2026-08-23
fecha_actualizacion: 2026-08-23
fecha_cierre: 2026-08-23
relacionadas:
- TAREA-010
- TAREA-069
- TAREA-075
- TAREA-089
- TAREA-090
- DEC-0010
siguiente_accion: null
---

# TAREA-091 — Auditoría y normalización del corpus

## Objetivo

Corregir las incidencias detectadas en la auditoría documental del 2026-08-23
(0 errores en el validador oficial, pero incidencias fuera de su cobertura):

## Bloques de trabajo

- **Bloque A** — Datos de tareas: corregir la entrada corrupta de TAREA-069 en
  `status.yaml` (duplica título y relacionadas de TAREA-075); alinear estados
  contradictorios de TAREA-010 (ficha), TAREA-089 y TAREA-090
  (`06_indices/tareas.yaml`); sustituir referencias a NOR-048/NOR-049
  (retirados por DEC-0010) por sus fusiones NOR-044/NOR-046.
- **Bloque B** — Anular `siguiente_accion` residuales de tareas realmente
  completadas.
- **Bloque C** — Normalizar los 4 resúmenes íntegramente sangrados a 4 espacios
  en `07_corpus_ia/resumenes/` (resumen-NOR-001 a NOR-004).
- **Bloque D** — Migrar CHUNK-00006 a CHUNK-00022 al esquema
  `schemas/chunk.schema.yaml`.
- **Bloque E** — Añadir frontmatter a las 27 fichas curriculares `.md` sin él
  (Infantil, Primaria, Bachillerato) y a DEC-0006.
- **Bloque F** — Ampliar el validador: chunks contra esquema, frontmatter en
  CUR `.md`, sangrado en resúmenes.

## Criterios de cierre

- `python3 11_calidad/validar_corpus.py` con 0 errores tras cada bloque.
- Sin referencias vivas a IDs retirados en índices ni status.yaml.
- Todos los chunks conformes a su esquema; validador cubre los tres focos.

## Notas

Los 3 avisos actuales sobre copias locales de NOR-017, NOR-018 y NOR-050 se
mantienen como avisos: su verificación contra fuente oficial corresponde al
ámbito de TAREA-085.

## Coordinación con trabajo paralelo

Sin tareas ajenas `En progreso` en el momento de la reserva (2026-08-23).
