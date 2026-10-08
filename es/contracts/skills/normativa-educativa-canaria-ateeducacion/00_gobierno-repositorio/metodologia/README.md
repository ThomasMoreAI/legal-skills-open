# Metodología

Metodología editorial, disciplina de evidencia y criterios de trabajo del repositorio.

## Flujo Editorial

1. Sincronizar el repositorio y comprobar si hay tareas en progreso.
2. Leer `README.md`, `index.md`, `status.yaml`, `AGENTS.md` y las plantillas aplicables.
3. Identificar la fuente oficial y registrar fecha de consulta.
4. Revisar los índices YAML afectados para evitar duplicados.
5. Reservar IDs temprano en el índice correspondiente cuando se creen entidades nuevas.
6. Crear o actualizar fichas desde plantillas.
7. Registrar relaciones, dudas y chunks cuando proceda.
8. Validar YAML, formato Markdown y coherencia de índices.
9. Actualizar exports (`llms.txt`, `llms-full.txt`) solo con contenido ya indexado.
10. Documentar en el diario los IDs consumidos y límites de la tarea.

## Disciplina De Evidencia

No se afirma nada sobre una norma o currículo sin fuente oficial, localización relevante y fecha de consulta.

Prioridad de evidencia:

1. BOE o BOC, preferentemente texto consolidado cuando exista.
2. Juriscan u otro repositorio jurídico oficial competente.
3. Portal institucional competente.
4. Ficha interna del corpus, siempre subordinada a la fuente oficial.

Si la evidencia no basta:

- usar `[PENDIENTE]` para datos no confirmados;
- usar `[HIPÓTESIS]` para inferencias razonables pendientes de contraste;
- usar `[INTERPRETACIÓN]` para lectura editorial;
- abrir o enlazar `PREG-NNN` si la duda afecta a uso normativo.

## Separación De Entidades

- Una fuente (`FTE`) no es una norma: documenta dónde se verifica la información.
- Una norma (`NOR`) resume y estructura una disposición oficial.
- Un currículo (`CUR`) extrae elementos curriculares de una norma base.
- Una relación (`REL`) enlaza entidades con evidencia.
- Un chunk (`CHUNK`) es un resumen breve para IA, no una fuente.
- Una decisión (`DEC`) explica reglas editoriales del corpus.

## Trabajo En Paralelo

- No editar archivos asociados a tareas en `En progreso` de otra persona o agente.
- Antes de crear IDs, revisar índices y calcular el siguiente libre.
- Si aparece una colisión, renumerar el trabajo propio; no reutilizar IDs.
- Al añadir cambios a git, incluir solo archivos tocados por la tarea propia.
- Si el árbol contiene cambios ajenos, trabajar alrededor de ellos y no revertirlos.

## Exports IA

`llms.txt` y `llms-full.txt` deben ser mapas de navegación, no sustitutos del corpus.

Reglas:

- declarar solo entidades ya presentes en `06_indices/`;
- reflejar conteos y últimos IDs actuales;
- advertir sobre tareas en progreso y extracciones pendientes;
- remitir a índices y fichas para evidencia completa;
- mantener la regla de cita jurídica oficial.
- remitir a `06_indices/textos-oficiales.yaml` y a `07_corpus_ia/textos-completos/` cuando exista una copia local rápida del texto oficial.

## Textos Oficiales Rápidos

Cuando una norma o currículo requiera lectura íntegra rápida, puede publicarse una copia local en texto plano, siempre subordinada a la fuente oficial.

Reglas:

- no sustituye el BOE, BOC ni el portal institucional competente;
- debe indicar URL oficial, fecha de consulta, fecha de exportación y advertencia expresa;
- debe registrarse en `06_indices/textos-oficiales.yaml`;
- debe conservar trazabilidad con `FTE-NNN`, `NOR-NNN` o `CUR-NNN`;
- debe regenerarse o marcarse desactualizada si cambia la fuente oficial.

## Cierre

Una edición documental se considera cerrada solo cuando los índices parsean, los enlaces principales son coherentes, los estados reflejan la realidad y los pendientes quedan marcados sin ambigüedad.
