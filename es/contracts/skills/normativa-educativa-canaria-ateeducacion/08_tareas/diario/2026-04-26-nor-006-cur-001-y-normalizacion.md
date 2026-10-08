# Diario — 2026-04-26: TAREA-008/009 cerradas, TAREA-010 en progreso

## TAREA-008 — Normalización de frontmatter (Hecha)

- Normalizadas las fichas `NOR-001`, `NOR-002`, `NOR-003` y `NOR-004` para eliminar la sangría espuria de 4 espacios y reindentar correctamente el bloque `relaciones:`. Frontmatter parseado por `yaml.safe_load` sin errores.
- Pendiente futuro: aplicar la misma normalización a las fichas `FTE-005` a `FTE-010` que comparten el mismo defecto.

## TAREA-009 — Alta de NOR-006 (Hecha)

- Catalogada `FTE-011`: texto consolidado del BOE del Real Decreto 243/2022 (BOE-A-2022-5521).
- Creada `NOR-006 — Real Decreto 243/2022, de 5 de abril, por el que se establecen la ordenación y las enseñanzas mínimas del Bachillerato`. Datos verificados contra `FTE-011` (BOE n.º 82, 6-04-2022): publicación, entrada en vigor (7-04-2022), estructura (34 artículos, 5 disposiciones adicionales, 2 transitorias, 1 derogatoria, 5 finales, 5 anexos) y modalidades reguladas (Artes; Ciencias y Tecnología; General; Humanidades y Ciencias Sociales).
- Registradas dos relaciones nuevas:
  - `REL-006`: NOR-006 desarrolla NOR-002 (LOMLOE) en el ámbito del Bachillerato.
  - `REL-007`: NOR-005 (Decreto 30/2023) desarrolla NOR-006 en el ámbito autonómico canario.
- Actualizado `desarrolla_a` de NOR-005 para incluir `NOR-006`.
- Índices actualizados: `06_indices/fuentes.yaml`, `06_indices/normativa.yaml`, `06_indices/relaciones.yaml`.

## TAREA-010 — Inicio de extracción CUR-001 (En progreso)

- `CUR-001` (Biología y Geología, ESO Canarias) actualizada con `norma_base: NOR-005`, `fuente: FTE-009`, fecha de consulta y análisis 2026-04-26.
- Cursos afectados: 1.º, 3.º y 4.º de la ESO.
- Volcadas las seis competencias específicas (C1-C6) como resumen no literal y la estructura por bloques de saberes básicos por curso.
- Marcados como `[PENDIENTE]` los criterios de evaluación literales, los descriptores operativos y los enunciados oficiales literales de cada competencia.
- Fuente consultada para la extracción: `borrador_curriculo_2022/Biologia_geologia_ESO.pdf` enlazado desde el portal `FTE-002`. Pendiente verificación contra el anexo definitivo del Decreto 30/2023 en BOC (`FTE-009`); cautela documentada en la ficha y en `06_indices/curriculos.yaml`.
- `estado_extraccion` se mantiene `Pendiente` por aplicación de `DEC-0004` hasta volcar los cuatro elementos obligatorios.
- Actualizada `06_indices/curriculos.yaml` reflejando el avance.

## Próximos pasos sugeridos

- Localizar y volcar el anexo definitivo de Biología y Geología publicado en BOC para sustituir los enunciados resumidos por los oficiales literales.
- Completar criterios de evaluación y descriptores operativos del Perfil de salida.
- Considerar la normalización de `FTE-005`..`FTE-010` para arreglar el frontmatter heredado.
