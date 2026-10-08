---
id: TAREA-053
titulo: "Indexar textos oficiales y crear copias rápidas iniciales"
estado: "Hecha"
prioridad: "Alta"
tipo: "corpus-ia"
responsable: "@.agents/skills/preparacion-corpus-ia"
fecha_creacion: 2026-04-26
fecha_actualizacion: 2026-04-26
relacionadas: [FTE-005, FTE-007, FTE-009, NOR-001, NOR-003, NOR-005]
---

# TAREA-053 — Indexar textos oficiales y crear copias rápidas iniciales

## Objetivo

Añadir una vía rápida y trazable para acceder al texto oficial completo, diferenciando enlaces oficiales estructurados y copias locales rápidas cuando aporten valor para lectura íntegra, RAG o extracción.

## Criterios de cierre

- Crear `06_indices/textos-oficiales.yaml` con accesos estructurados para `FTE`, `NOR` y `CUR`.
- Publicar un lote inicial de copias locales rápidas del texto completo para `NOR-001`, `NOR-003` y `NOR-005`.
- Actualizar plantillas, reglas editoriales y mapas de navegación para reflejar el nuevo flujo.
- Validar YAML, artefacto Pages y existencia de las rutas locales declaradas.

## Resultado

- Índice nuevo creado: `06_indices/textos-oficiales.yaml`.
- Copias locales rápidas creadas en `07_corpus_ia/textos-completos/` para `NOR-001`, `NOR-003` y `NOR-005`.
- Actualizados `README.md`, `index.md`, `llms.txt`, `llms-full.txt`, plantillas y documentación metodológica.

## IDs consumidos

- `TAREA-053`.

## Coordinación con trabajo paralelo

- No se han reservado nuevos IDs de `FTE`, `NOR`, `CUR`, `REL`, `CHUNK`, `PREG` o `DEC`.
- Se han tocado solo archivos documentales transversales, índices y materiales IA propios de esta tarea.
