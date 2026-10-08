---
id: TAREA-042
titulo: "Resolver PREG-005 — Verificar y corregir RDs de ciclos de Sanidad (NOR-051, NOR-052)"
estado: "Hecha"
tipo: "calidad-documental"
fecha_creacion: 2026-04-26
fecha_actualizacion: 2026-04-26
relacionadas: [NOR-051, NOR-052, CUR-046, CUR-047, PREG-005]
---

# TAREA-042 — Resolver PREG-005: verificar y corregir RDs de ciclos de Sanidad

## Objetivo

Verificar directamente en BOE.es los números correctos de Real Decreto para los dos ciclos de FP de Sanidad catalogados en NOR-051 y NOR-052, y corregir todos los campos afectados.

## RDs verificados (fuente: BOE.es, 2026-04-26)

| Ficha | Título del ciclo | RD incorrecto (catalogación inicial) | RD correcto | BOE-A confirmado | Fecha publicación |
|-------|-----------------|--------------------------------------|-------------|-----------------|-------------------|
| NOR-051 | Técnico en Cuidados Auxiliares de Enfermería (GM) | 1538/1995 | **546/1995** | BOE-A-1995-13533 | 1995-06-05 (BOE núm. 133) |
| NOR-052 | T.S. Imagen para el Diagnóstico y Medicina Nuclear (GS) | 772/2014 | **770/2014** | BOE-A-2014-10067 | 2014-10-04 (BOE núm. 241) |

### Notas adicionales

- **NOR-051**: El RD 558/1995 (BOE-A-1995-13592, BOE núm. 134, 6 jun 1995) establece el currículo detallado del ciclo. El número 1538/1995 no se ha localizado en BOE.es para este título.
- **NOR-052**: El RD 772/2014 (BOE-A-2014-10069) corresponde al título de Radioterapia y Dosimetría (ciclo diferente). El número 772/2014 era un error de catalogación.

## Archivos modificados

- `02_normativa/estatal/reales-decretos/NOR-051-rd-1538-1995-cuidados-auxiliares-enfermeria.md` — frontmatter y notas corregidos.
- `02_normativa/estatal/reales-decretos/NOR-052-rd-772-2014-imagen-diagnostico-medicina-nuclear.md` — frontmatter y notas corregidos.
- `03_curriculos/fp/sanidad/CUR-046-cuidados-auxiliares-de-enfermeria.yaml` — url_oficial y observaciones actualizadas.
- `03_curriculos/fp/sanidad/CUR-047-imagen-para-el-diagnostico-y-medicina-nuclear.yaml` — url_oficial y observaciones actualizadas.
- `08_tareas/preguntas/PREG-005-discrepancia-rd-sanidad-nor-051-nor-052.md` — estado → Resuelta; sección Respuesta añadida.
- `06_indices/preguntas.yaml` — PREG-005 estado → Resuelta, fecha_resolucion añadida.
- `06_indices/tareas.yaml` — TAREA-042 estado → Hecha.
- `status.yaml` — TAREA-042 estado → Hecha, siguiente_accion → null.

## Decisión editorial

Los nombres de archivo NOR-051 y NOR-052 NO se han renombrado para preservar la estabilidad de ID (regla R10). El renombrado queda pendiente para una tarea futura dedicada.

## Fuentes consultadas

- https://www.boe.es/buscar/doc.php?id=BOE-A-1995-13533 (RD 546/1995 — título CAE)
- https://www.boe.es/buscar/doc.php?id=BOE-A-1995-13592 (RD 558/1995 — currículo CAE)
- https://www.boe.es/buscar/doc.php?id=BOE-A-2014-10067 (RD 770/2014 — título Imagen Diagnóstico)
- https://www.boe.es/buscar/doc.php?id=BOE-A-2014-10069 (RD 772/2014 — Radioterapia, ciclo diferente)
