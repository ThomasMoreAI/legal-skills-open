# Auditoría de descriptores operativos de las fichas curriculares de ESO

**Fecha:** 2026-08-05
**Alcance:** las 18 fichas `CUR` de ESO en `estado_extraccion: completado` que tienen
descriptores operativos volcados — 101 competencias específicas.
**Fuente de contraste:** `07_corpus_ia/textos-completos/texto-oficial-NOR-005-decreto-30-2023.txt`
(Decreto 30/2023, currículo de ESO y Bachillerato de Canarias).
**Motivo:** aportar datos a `PREG-008`.

## Método

Del texto oficial se extrae cada bloque competencial, que tiene esta forma:

```
Competencia específica
N. <enunciado oficial>
Descriptores operativos de las
competencias clave. Perfil de salida
<códigos>
Criterios de evaluación
```

Cada bloque se anota con el curso al que pertenece, porque el decreto repite los bloques por
curso dentro de cada materia. El emparejamiento con la ficha se hace por el **texto del
enunciado**, que es largo y distintivo, exigiendo una similitud mínima de 0,90. Por debajo de
ese umbral no se compara: se reporta aparte, para no arriesgar una comparación falsa.

Se extrajeron 308 bloques. El texto contiene unas 392 marcas de competencia, así que **el
extractor no alcanza la totalidad**; eso se refleja en los resultados y limita el alcance de
esta auditoría, no la invalida.

## Resultado global

| Situación | Competencias | % |
| --- | ---: | ---: |
| Los descriptores coinciden con los de un curso del decreto | 78 | 77,2 % |
| Divergen: contienen códigos que no están en ninguna versión | 5 | 5,0 % |
| No comparables: el extractor no localizó el bloque | 12 | 11,9 % |
| No comparables: el enunciado de la ficha no es literal | 6 | 5,9 % |
| **Total** | **101** | |

Sobre las 83 competencias efectivamente comparadas, **5 divergen (6,0 %)**.

## 1. Cinco competencias con descriptores que no se sostienen

Contienen códigos que no aparecen en **ninguna** versión de curso del decreto, y en dos casos
omiten códigos presentes en **todas**.

| Ficha | Comp. | Sobran (no están en ningún curso) | Faltan (están en todos) |
| --- | --- | --- | --- |
| `CUR-001` Biología y Geología | C3 | CCL5, CD3, CE1, CP1, CPSAA4, CCEC3, CCEC4 | CCL3, STEM1, STEM3, CPSAA3 |
| `CUR-001` Biología y Geología | C5 | CC2 | CPSAA1 |
| `CUR-009` Ed. Plástica, Visual y Audiovisual | C6 | CCL1, CCL3, CD2, CP3 | — |
| `CUR-009` Ed. Plástica, Visual y Audiovisual | C7 | CCL2, CD2, CE1, CE2, CPSAA3, CPSAA4 | — |
| `CUR-009` Ed. Plástica, Visual y Audiovisual | C8 | CD2, CE3 | — |

El caso más grave es `CUR-001` C3: siete códigos que no existen en la fuente y cuatro ausentes
que sí están en los tres cursos. La lista de la ficha guarda poca relación con el decreto.

`CUR-001` C5 es el más ilustrativo porque los tres cursos coinciden en la fuente, así que no
cabe la explicación de la agregación: la ficha pone `CC2` donde el decreto dice `CPSAA1`.

## 2. Once competencias válidas solo para uno de los cursos

De las 78 que coinciden, **11 pertenecen a materias en las que el decreto asigna descriptores
distintos según el curso**. La ficha declara una única lista, que reproduce fielmente uno de los
cursos y calla que en los demás es otra.

Ejemplo, `CUR-001` competencia 2:

| Curso | Descriptores oficiales |
| --- | --- |
| 1.º ESO | CCL3, CD1, CD2, CD4, CPSAA4 |
| 3.º ESO | CCL3, STEM4, CD1, CD2, CD3, CD4, CD5, CPSAA4 |
| 4.º ESO | CCL3, STEM4, CD1, CD2, CD3, CD4, CD5, CPSAA4 |

No es un error de transcripción: es que el modelo de datos no puede representar la dimensión de
curso. Es el núcleo de `PREG-008`.

## 3. Seis enunciados que no reproducen la fuente

En seis competencias, el `enunciado_oficial` de la ficha no aparece literalmente en el decreto.
Se comprobó buscando sus nueve primeras palabras normalizadas en el texto completo.

| Ficha | Comp. | Similitud con el mejor candidato |
| --- | --- | ---: |
| `CUR-007` Educación en Valores Cívicos y Éticos | C4 | 0,37 |
| `CUR-001` Biología y Geología | C6 | 0,52 |
| `CUR-001` Biología y Geología | C4 | 0,62 |
| `CUR-012` Física y Química | C6 | 0,83 |
| `CUR-009` Ed. Plástica, Visual y Audiovisual | C2 | 0,86 |
| `CUR-010` Expresión Artística | C3 | 0,87 |

Los tres primeros no son variaciones de redacción: son textos distintos. `DEC-0004` exige
recoger la competencia con su enunciado oficial, así que estas seis lo incumplen con
independencia de sus descriptores.

## 4. Doce competencias no verificadas

En doce casos el enunciado **sí** aparece literalmente en el decreto, pero el extractor no
localizó su bloque de descriptores. No se afirma nada sobre ellas: quedan sin verificar.

`CUR-002` C5 · `CUR-003` C3 · `CUR-005` C3 · `CUR-006` C2 · `CUR-009` C1 · `CUR-009` C5 ·
`CUR-010` C1 · `CUR-013` C1 · `CUR-013` C5 · `CUR-014` C5 · `CUR-014` C9 · `CUR-022` C3

## Estado por ficha

| Ficha | Materia | Cursos | Comp. | Coinciden | Divergen | No comparables |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| `CUR-001` | Biología y Geología | 3 | 6 | 2 | 2 | 2 |
| `CUR-002` | Cultura Clásica | 1 | 5 | 4 | 0 | 1 |
| `CUR-003` | Cultura y Ciudadanía Digital | 1 | 6 | 5 | 0 | 1 |
| `CUR-004` | Digitalización | 1 | 4 | 4 | 0 | 0 |
| `CUR-005` | Economía Personal y Social | 1 | 3 | 2 | 0 | 1 |
| `CUR-006` | Economía y Emprendimiento | 1 | 7 | 6 | 0 | 1 |
| `CUR-007` | Ed. en Valores Cívicos y Éticos | 1 | 4 | 3 | 0 | 1 |
| `CUR-008` | Educación Física | 4 | 5 | 5 | 0 | 0 |
| `CUR-009` | Ed. Plástica, Visual y Audiovisual | 3 | 8 | 2 | 3 | 3 |
| `CUR-010` | Expresión Artística | 1 | 4 | 2 | 0 | 2 |
| `CUR-011` | Filosofía | 1 | 3 | 3 | 0 | 0 |
| `CUR-012` | Física y Química | 3 | 6 | 5 | 0 | 1 |
| `CUR-013` | Formación y Orientación Personal y Profesional | 1 | 5 | 3 | 0 | 2 |
| `CUR-014` | Geografía e Historia | 4 | 9 | 7 | 0 | 2 |
| `CUR-017` | Lengua Castellana y Literatura | 4 | 10 | 10 | 0 | 0 |
| `CUR-018` | Lengua Extranjera | 4 | 6 | 6 | 0 | 0 |
| `CUR-020` | Música | 3 | 4 | 4 | 0 | 0 |
| `CUR-022` | Tecnología | 1 | 6 | 5 | 0 | 1 |

Seis fichas salen sin ninguna incidencia: `CUR-004`, `CUR-008`, `CUR-011`, `CUR-017`,
`CUR-018` y `CUR-020`. Dos concentran las incidencias graves: `CUR-001` y `CUR-009`.

## Conclusiones para PREG-008

1. **El grueso del corpus resiste el contraste.** 78 de 101 competencias reproducen la fuente
   para al menos un curso, y seis fichas están impecables. No procede degradar las 18 en bloque.
2. **`CUR-001` y `CUR-009` necesitan re-extracción completa.** Concentran las 5 divergencias y
   buena parte de los enunciados no literales.
3. **La dimensión de curso es un problema de modelo, no de datos.** Afecta al menos a 11
   competencias hoy y afectará a cualquier futura extracción. Decidirlo es previo a desbloquear
   `TAREA-066` a `TAREA-069`.
4. **Hay un problema adicional de literalidad** que `PREG-008` no contemplaba: seis enunciados
   no reproducen la fuente. Conviene extender la comprobación a las 32 fichas parciales, cuyo
   campo `descripcion` nunca se ha contrastado.
5. **El extractor necesita trabajo antes de usarse para volcar datos.** Localiza 308 de unas 392
   competencias. Sirve para auditar, no todavía para extraer.

## Reproducción

El guion de auditoría no se ha incorporado al repositorio: es de un solo uso y depende de una
conversión de PDF. El método queda descrito arriba para poder rehacerlo.

Este informe no sustituye la consulta de la fuente oficial. Cualquier corrección derivada de él
debe verificarse en el BOC antes de aplicarse.
