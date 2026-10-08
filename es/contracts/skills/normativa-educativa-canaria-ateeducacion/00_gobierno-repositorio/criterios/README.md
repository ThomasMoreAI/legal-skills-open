# Criterios

Criterios de cierre, validación y control documental del corpus.

## Criterios De Cierre De Una Tarea

Una `TAREA-NNN` solo puede pasar a `Hecha` si cumple, cuando aplique, todos estos puntos:

1. La fuente oficial está identificada y registrada como `FTE-NNN`.
2. La fecha de consulta consta en la ficha y en el índice afectado.
3. Los IDs nuevos son correlativos, estables y no reutilizan huecos ya consumidos.
4. Los índices YAML afectados están actualizados.
5. Las fichas Markdown/YAML parsean correctamente y respetan la plantilla correspondiente.
6. Toda norma tiene estado de vigencia.
7. Toda ficha curricular mantiene `estado_extraccion` coherente.
8. Toda relación normativa necesaria está registrada como `REL-NNN`.
9. Las dudas abiertas están registradas como `PREG-NNN`.
10. Las interpretaciones, hipótesis y datos pendientes usan los marcadores obligatorios.
11. El diario de trabajo refleja los IDs consumidos y los límites de la tarea.
12. Los exports IA (`llms.txt`, `llms-full.txt` y chunks) solo declaran contenido ya indexado.
13. Las copias locales de texto completo indican origen oficial, fecha y advertencia de subordinación a la fuente oficial.

## Validaciones Mínimas

Antes de cerrar una edición, ejecutar al menos:

```bash
python3 -c "import yaml,pathlib; [yaml.safe_load(pathlib.Path(p).read_text()) for p in ['status.yaml','06_indices/tareas.yaml','06_indices/normativa.yaml','06_indices/fuentes.yaml','06_indices/relaciones.yaml','06_indices/curriculos.yaml','06_indices/chunks.yaml','06_indices/preguntas.yaml','06_indices/textos-oficiales.yaml']]; print('OK')"
git diff --check
```

Si se han tocado schemas, exports, páginas públicas o scripts, añadir la validación específica de esa zona.

## Criterios Por Tipo De Ficha

### Fuentes `FTE`

- Deben indicar autoridad, URL oficial, tipo de fuente, fecha de consulta y ruta.
- Solo se consideran fuente normativa si proceden de BOE, BOC, Juriscan, portal institucional competente u otra fuente oficial documentada.

### Normativa `NOR`

- Debe incluir fuente principal, ámbito, tipo de norma, fechas disponibles, estado de vigencia y ruta.
- Si la vigencia no se puede confirmar, usar `Pendiente de verificación` y abrir o enlazar una duda/tarea.
- No se eliminan normas derogadas o históricas: se conservan marcadas.

### Currículos `CUR`

- Deben indicar etapa, materia o ciclo, norma base, fuente, rutas y estado de extracción.
- `completado` exige que el contenido previsto por la tarea esté extraído o que los límites estén documentados.
- `pendiente` o `parcial` debe señalar claramente qué falta.

### Relaciones `REL`

- Deben indicar origen, destino, tipo de relación, evidencia, fecha de registro y nivel de evidencia.
- No sustituyen la cita jurídica oficial; sirven para navegación y trazabilidad interna.

### Chunks IA

- Deben ser breves, autocontenidos y fieles a la ficha origen.
- Deben incluir fuente, localización y advertencia de que no sustituyen la fuente oficial.
- No deben mezclar orientación no normativa con normativa.

### Textos oficiales rápidos

- Deben mantener URL oficial, fecha de consulta, fecha de exportación y ruta local.
- Su función es facilitar lectura rápida o extracción; nunca sustituyen la publicación oficial.
- Deben estar indexados en `06_indices/textos-oficiales.yaml`.

## Señales De Bloqueo

- Falta fuente oficial.
- Falta fecha de consulta.
- El ID ya existe o no está registrado en índice.
- El YAML no parsea.
- La ficha afirma vigencia sin evidencia.
- Se mezcla norma con orientación o recurso no normativo.
- Hay cambios locales ajenos en archivos de otra tarea en progreso.
