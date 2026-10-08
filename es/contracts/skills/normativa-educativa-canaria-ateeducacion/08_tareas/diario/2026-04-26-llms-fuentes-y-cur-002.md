# Diario — 2026-04-26: Rigor jurídico en LLMS, nuevas fuentes y extracción CUR-002

## LLMS.txt — Rigor jurídico

- Reescrita la sección de estilo de respuesta para exigir cita exacta de norma + localización (artículo, apartado, disposición o anexo) en cada afirmación.
- Añadido un apartado de **vigencia y jerarquía** que aclara expresamente:
  - La LOE (LO 2/2006) sigue **vigente**, modificada (no derogada) por la LOMLOE (LO 3/2020), conforme al texto consolidado del BOE actualizado a 2024-06-08.
  - El currículo de ESO y Bachillerato vigente en Canarias es el **Decreto 30/2023, de 16 de marzo** (BOC n.º 58, 23-03-2023), que sustituyó a los Decretos 315/2015 y 83/2016.
  - Marco básico estatal vigente: **RD 217/2022 (ESO)** y **RD 243/2022 (Bachillerato)**.

## Fuentes nuevas (TAREA-013 — Hecha)

- `FTE-012`: Centro de Desarrollo Curricular (CDC) del Gobierno de Canarias (`portal-curricular`).
- `FTE-013`: Normativa clasificada por temas — Inspección Educativa de Canarias, con apartados marco general / administración / alumnado / atención a la diversidad / centros / enseñanzas / organización y funcionamiento / personal docente / personal no docente / orientaciones-programas-protocolos / servicios complementarios.
- `FTE-014`: Normativa clasificada — Enseñanzas.
- `FTE-015`: Normativa clasificada — Formación Profesional.
- `06_indices/fuentes.yaml` actualizado.

## FTE-009 — Documento canónico identificado

- Localizada y registrada la URL del PDF oficial completo del Decreto 30/2023 (1953 págs., todos los anexos): `https://sede.gobiernodecanarias.org/boc/boc-a-2023-058-848.pdf`. Sirve de base para `TAREA-011` (cotejo BOC del anexo de Biología y Geología).

## CUR-002 — Extracción inicial parcial (TAREA-019 — En progreso)

- `CUR-002` (Cultura Clásica, ESO Canarias) actualizada: `norma_base=NOR-005`, `fuente=FTE-009`, fecha de consulta y análisis 2026-04-26.
- Volcadas las cuatro primeras competencias específicas (C1-C4) como resumen no literal a partir del documento `borrador_curriculo_2022/Cultura_clasica_ESO.pdf`. C5, criterios de evaluación (12) y saberes básicos quedan `[PENDIENTE]`.
- `06_indices/curriculos.yaml` actualizado.

## Tareas abiertas para inventario sistemático (Pendiente)

- `TAREA-014`: Centros y Organización y funcionamiento.
- `TAREA-015`: Personal docente.
- `TAREA-016`: Atención a la diversidad y Alumnado.
- `TAREA-017`: Formación Profesional (Ley Orgánica 3/2022 y desarrollos autonómicos canarios).
- `TAREA-018`: Marco general, Administración y Servicios complementarios.

## Próximos pasos

- Empezar por `TAREA-017` (FP) o por `TAREA-014` (Centros) según prioridad.
- Continuar `TAREA-011` aprovechando el PDF canónico de BOC ya identificado.
- Replicar el patrón CUR-001/CUR-002 en otras materias (CUR-014 Geografía e Historia, CUR-019 Matemáticas, etc.).
