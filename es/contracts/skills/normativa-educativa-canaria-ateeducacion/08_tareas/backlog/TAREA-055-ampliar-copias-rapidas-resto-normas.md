---
id: TAREA-055
titulo: "Ampliar copias rápidas de texto oficial al resto de normas"
estado: "Hecha"
prioridad: "Alta"
tipo: "corpus-ia"
responsable: "@.agents/skills/preparacion-corpus-ia"
fecha_creacion: 2026-04-27
fecha_actualizacion: 2026-04-27
relacionadas: [TAREA-053, NOR-002, NOR-039, NOR-040, NOR-041, NOR-042, NOR-045, NOR-046, NOR-059, NOR-060]
---

# TAREA-055 — Ampliar copias rápidas de texto oficial al resto de normas

## Objetivo

Completar la cobertura de `07_corpus_ia/textos-completos/` para las normas del corpus que aún no tenían `texto_plano_local`, manteniendo trazabilidad con la fuente oficial y actualizando el resolutor `06_indices/textos-oficiales.yaml`.

## Criterios de cierre

- Publicar las 57 copias locales rápidas pendientes para las normas `NOR-002` y `NOR-004` a `NOR-060`, salvo las ya cubiertas en `TAREA-053`.
- Actualizar `06_indices/textos-oficiales.yaml` para que cada `NOR` disponga de `estado_acceso: con-copia-local`, `ruta_local`, `sha256`, `url_origen` y `fecha_exportacion`.
- Corregir los accesos oficiales que habían quedado obsoletos o indirectos cuando la descarga pública actual exigía PDF o índice de número del BOC.
- Reflejar el nuevo alcance en los resúmenes globales del repositorio.

## Resultado

- Publicadas 57 copias locales rápidas adicionales en `07_corpus_ia/textos-completos/`.
- Cobertura completada para las 60 fichas normativas registradas (`NOR-001` a `NOR-060`).
- Actualizados `06_indices/textos-oficiales.yaml`, `README.md`, `llms.txt` y `llms-full.txt`.

## IDs consumidos

- `TAREA-055`.

## Coordinación con trabajo paralelo

- Se ha renumerado la tarea a `TAREA-055` al integrar `origin/main`, porque `TAREA-054` ya había sido consumida por otra edición paralela del corpus.
- La tarea se ha limitado a materiales IA, al resolutor de textos oficiales y a los resúmenes globales del repositorio.
