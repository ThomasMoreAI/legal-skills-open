---
id: TAREA-092
titulo: "Resolver los avisos del validador sobre copias locales contaminadas y alinear textos-oficiales.yaml"
estado: "Hecha"
fecha_cierre: 2026-08-23
prioridad: "Alta"
tipo: "calidad-documental"
responsable: "@.agents/skills/control-calidad-documental"
fecha_creacion: 2026-08-23
fecha_actualizacion: 2026-08-23
relacionadas:
- TAREA-084
- TAREA-085
- TAREA-091
- DEC-0011
- PREG-010
- PREG-011
- PREG-012
siguiente_accion: null
---

# TAREA-092 — Resolución de los avisos sobre copias locales

## Objetivo

Eliminar los 3 avisos que `validar_corpus.py` lleva emitiendo desde TAREA-085
sobre las copias locales de NOR-017, NOR-018 y NOR-050, y corregir las
desalineaciones detectadas después en `06_indices/textos-oficiales.yaml`.

## Diagnóstico

Las tres copias contienen solo la caché de navegación de la página del BOC
(menús, «Mapa web», párrafos `<p>`), sin una sola línea normativa. Las normas
que declaraban fueron retiradas como catalogación errónea (`DEC-0011`,
`PREG-010`, `PREG-011`, `PREG-012`) y las normas reales que NOR-018 confundía
(NOR-076, NOR-077) ya tienen ficha y copia local propia.

## Qué hacer

1. Eliminar los 3 `.txt` y sus bloques `texto_plano_local` del índice
   (`estado_acceso` pasa a `enlace-oficial`).
2. Alinear `estado_vigencia` de NOR-017/018/050 (retiradas) y NOR-025
   (rectificada por PREG-012) con sus fichas normativas.
3. Nueva comprobación en el validador: cada `ruta_local` del índice debe
   resolver y cada `estado_vigencia` debe coincidir con la ficha normativa.

## Criterios de cierre

- `python3 11_calidad/validar_corpus.py` con **0 errores · 0 avisos**. Cumplido.
- Sin entradas de índice apuntando a ficheros inexistentes. Cumplido.

## Coordinación con trabajo paralelo

Rama `feat/tarea-092-resolucion-avisos`. Sin tareas ajenas `En progreso`
en el momento de la reserva (2026-08-23).
