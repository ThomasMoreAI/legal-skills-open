# Glosario

Glosario operativo de términos usados en el corpus.

## IDs

- `FTE-NNN`: fuente oficial, portal institucional, boletín o documento usado como evidencia.
- `NOR-NNN`: ficha normativa.
- `CUR-NNN`: ficha curricular.
- `REL-NNN`: relación explícita entre entidades.
- `AN-NNN`: análisis editorial o nota transversal.
- `CHUNK-NNNNN`: unidad breve para uso IA/RAG.
- `PREG-NNN`: pregunta abierta o duda documental.
- `TAREA-NNN`: unidad de trabajo del backlog.
- `DEC-NNNN`: decisión editorial o ADR.

Los IDs son estables, correlativos y no se reutilizan. Si hay huecos por coordinación de trabajo paralelo, se conservan.

## Estados Frecuentes

- `Vigente`: la norma se considera vigente según la fuente revisada.
- `Vigente con modificaciones`: la norma sigue vigente, pero debe consultarse el texto consolidado.
- `Pendiente de verificación`: falta confirmación suficiente de vigencia o datos clave.
- `Derogada`: la norma ya no está vigente por derogación expresa o acreditada.
- `Histórica`: se conserva por trazabilidad, sin aplicarla como norma vigente.
- `Superada`: se conserva aunque haya sido sustituida por un marco posterior.
- `completado`: extracción curricular cerrada según el alcance definido.
- `pendiente`: extracción no iniciada o placeholder registrado.
- `parcial`: extracción iniciada con límites documentados.
- `Hecha`: tarea cerrada con criterios mínimos cumplidos.
- `En progreso`: tarea activa; no editar sus archivos asociados sin coordinación.

## Marcadores Editoriales

- `[PENDIENTE]`: dato pendiente de verificar.
- `[HIPÓTESIS]`: afirmación razonable, pero no confirmada.
- `[INTERPRETACIÓN]`: lectura editorial propia sobre una fuente.
- `[OBSOLETO]`: contenido conservado solo por trazabilidad.

## Tipos De Contenido

- Fuente: evidencia primaria o portal oficial de consulta.
- Norma: disposición con valor jurídico o administrativo.
- Currículo: extracción estructurada de competencias, criterios, saberes, módulos o elementos curriculares.
- Relación: vínculo trazable entre dos entidades, por ejemplo `desarrolla`, `modifica`, `deroga` o `relaciona`.
- Chunk: resumen IA-friendly de una ficha, nunca sustituto de la fuente oficial.
- ADR: decisión editorial que explica una regla estable del corpus.

## Principio De Cita

Para responder a usuarios, la cita principal debe ser la denominación jurídica oficial de la norma y su localización concreta. Los IDs internos sirven como trazabilidad secundaria.
