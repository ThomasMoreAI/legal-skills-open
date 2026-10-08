# Diario — 2026-04-26: Regla de frontmatter y apertura de TAREA-011

## Cambios en AGENTS.md

- Añadida la sección **5.1 Frontmatter YAML — formato obligatorio** documentando la regla a seguir: claves en columna 0, indentación de 2 espacios para bloques anidados, validación con `yaml.safe_load` y obligación de partir de las plantillas de `10_plantillas/`.

## TAREA-012 — Normalización FTE-001 a FTE-008 (Hecha)

- Aplicada la misma normalización que en `TAREA-008` a las ocho fichas de fuente `FTE-001` a `FTE-008`. `FTE-009`, `FTE-010` y `FTE-011` ya estaban en el formato correcto.
- Los frontmatter resultantes parsean limpios con `yaml.safe_load`.

## TAREA-011 — Cotejo BOC anexo Biología y Geología (Pendiente)

- Abierta para sustituir los enunciados resumidos de las competencias específicas (C1-C6) y los `[PENDIENTE]` de `CUR-001` por el contenido literal del anexo del Decreto 30/2023 publicado en BOC.
- Riesgo registrado: el documento utilizado en la extracción inicial era un borrador previo al BOC y puede haber divergencias con el texto definitivo.
- Siguiente paso: identificar la URL del PDF/HTML oficial del anexo en BOC.

## Próximos pasos sugeridos

- Ejecutar `TAREA-011` cuando se localice el anexo oficial.
- Replicar el patrón de extracción de `CUR-001` en otra materia piloto (por ejemplo, una de Bachillerato vinculada al Decreto 30/2023).
