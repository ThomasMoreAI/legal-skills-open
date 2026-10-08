# Diario — 2026-04-26: Cierre TAREA-006, apertura TAREA-007 y resolución de PREG-002 / PREG-003

## Sincronización de estado

- Sincronizado `status.yaml` y `06_indices/tareas.yaml` con la ficha real de **TAREA-006**, que ya estaba en `Hecha` desde el 2026-04-26 (commit `21945a1`). Limpiada `siguiente_accion` y actualizada `fecha_actualizacion`.
- Limpiada también la `siguiente_accion` de **TAREA-004**, ahora cubierta por `DEC-0004` y por `TAREA-007`.

## Apertura de tarea

- Creada **TAREA-007 — Redactar ficha normativa NOR-005 (Decreto 30/2023, Canarias)** vinculada a `FTE-009`. Origen: cierre parcial de `PREG-001` y necesidad de cubrir el currículo autonómico de ESO/Bachillerato.

## Decisiones editoriales nuevas

- **DEC-0004 — Alcance editorial de extracción curricular** (resuelve `PREG-002`): obligatorio extraer en YAML competencias específicas, criterios de evaluación, saberes básicos y vinculación con descriptores operativos. Markdown narrativo opcional, sin material no oficial.
- **DEC-0005 — Tratamiento documental de orientaciones y recursos no normativos** (resuelve `PREG-003`): excluidos del corpus normativo y curricular; se catalogan en `01_fuentes/` con `tipo_fuente: orientacion-no-normativa` y pueden citarse en análisis con marca `[INTERPRETACIÓN]`.

## Estado de preguntas abiertas

- `PREG-002` → Resuelta (referencia DEC-0004).
- `PREG-003` → Resuelta (referencia DEC-0005).
- No quedan preguntas abiertas tras esta jornada.

## Próximos pasos sugeridos

- Ejecutar `TAREA-007` para crear la ficha `NOR-005`.
- Planificar las primeras extracciones curriculares según `DEC-0004`, comenzando por una materia piloto (`CUR-001`) para validar el formato.
