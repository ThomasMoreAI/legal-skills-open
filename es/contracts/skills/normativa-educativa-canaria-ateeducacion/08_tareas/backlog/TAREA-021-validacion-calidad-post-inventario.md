---
id: TAREA-021
titulo: "Validar calidad documental tras el inventario normativo inicial"
estado: "Hecha"
prioridad: "Media"
tipo: "calidad-documental"
responsable: "@.agents/skills/control-calidad-documental"
fecha_creacion: 2026-04-26
fecha_actualizacion: 2026-04-26
relacionadas: [TAREA-014, TAREA-015, TAREA-016, TAREA-017, TAREA-018, TAREA-019]
---

# TAREA-021 — Validar calidad documental tras el inventario normativo inicial

## Objetivo

Comprobar la consistencia documental del repositorio tras el cierre del inventario normativo inicial, sin intervenir en `TAREA-019`, que permanece en progreso.

## Criterios de cierre

- Validación de YAML de índices principales.
- Comprobación de rutas indexadas existentes.
- Validación de frontmatter Markdown parseable.
- Registro de incidencias y límites en `11_calidad/`.
- Actualización de `status.yaml` y `06_indices/tareas.yaml`.

## Notas

- Se dejan fuera del alcance los archivos sin seguimiento ajenos a esta tarea.
- La validación no sustituye la revisión jurídica o normativa de fuentes oficiales.

## Resultado

- Informe creado: `11_calidad/informes/2026-04-26-validacion-post-inventario.md`.
- Validaciones ejecutadas con resultado correcto.
- `TAREA-019` queda sin modificar.
