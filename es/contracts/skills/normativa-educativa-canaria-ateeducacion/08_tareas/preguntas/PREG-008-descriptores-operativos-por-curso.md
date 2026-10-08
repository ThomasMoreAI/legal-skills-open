---
id: PREG-008
titulo: "Los descriptores operativos varían por curso y el modelo de ficha curricular no lo representa"
estado: "Resuelta"
fecha_registro: 2026-08-05
fecha_resolucion: 2026-08-05
relacionadas: [CUR-001, CUR-009, DEC-0004, DEC-0007, TAREA-066, TAREA-067, TAREA-068, TAREA-069, TAREA-071, TAREA-072, TAREA-074, TAREA-075, DEC-0008]
---

# PREG-008 — Los descriptores operativos varían por curso

## Contexto

Al preparar la extracción de descriptores operativos (`TAREA-066` a `TAREA-069`) se comprobó
contra el texto oficial del Decreto 30/2023 (`NOR-005`) que **los descriptores operativos del
perfil de salida asociados a una competencia específica no son los mismos en todos los cursos**
en los que se imparte la materia.

Ejemplo verificado en Biología y Geología (`CUR-001`), competencia específica 2:

| Curso | Descriptores según el texto oficial |
| --- | --- |
| 1.º ESO | CCL3, CD1, CD2, CD4, CPSAA4 |
| 3.º ESO | CCL3, STEM4, CD1, CD2, CD3, CD4, CD5, CPSAA4 |
| 4.º ESO | CCL3, STEM4, CD1, CD2, CD3, CD4, CD5, CPSAA4 |

La competencia 6 de la misma materia varía en los tres cursos.

El modelo actual guarda una **lista plana por competencia**
(`elementos.competencias_especificas[].descriptores`), sin dimensión de curso. No puede
representar esta realidad.

## Consecuencia detectada en el corpus

De las 18 fichas en `estado_extraccion: completado` con descriptores volcados, **8 declaran
varios cursos**, así que su lista plana no puede ser correcta para todos ellos.

Y hay al menos un error que no es de agregación. En `CUR-001`, competencia 5, los tres cursos
coinciden en el texto oficial:

- Texto oficial (1.º, 3.º y 4.º ESO): `STEM2, STEM5, CD4, CPSAA1, CPSAA2, CC3, CC4, CE1`
- Ficha `CUR-001`: `STEM2, STEM5, CD4, CPSAA2, CC2, CC3, CC4, CE1`

La ficha pone `CC2`, que no aparece en la fuente, y omite `CPSAA1`, que sí. Comparando las seis
competencias de `CUR-001` con el texto oficial, solo la primera coincide exactamente.

Además, las 32 fichas en `parcial` **no declaran `cursos`**, así que ni siquiera se sabe a qué
curso habría que referir cada extracción.

## Qué falta decidir

1. ¿Los descriptores pasan a guardarse por curso —por ejemplo
   `descriptores: {1.º ESO: [...], 3.º ESO: [...]}`— o se separan las fichas por curso?
2. ¿Qué se hace con las 18 fichas ya marcadas `completado` cuyos descriptores no reproducen la
   fuente? ¿Se revisan todas o se degradan a `parcial` hasta revisarlas?
3. ¿Se rellena `cursos` en las 32 fichas parciales antes de extraer, dado que sin ese dato la
   extracción no es interpretable?
4. ¿Bachillerato tiene el mismo problema? Sus materias suelen impartirse en un solo curso, pero
   hay que confirmarlo antes de aplicar un criterio distinto por etapa.

## Fuente o evidencia necesaria

La evidencia está en el corpus: `07_corpus_ia/textos-completos/texto-oficial-NOR-005-decreto-30-2023.txt`
contiene los bloques competenciales por curso. No hace falta consultar fuente externa para
decidir el modelo; sí para corregir cada ficha.

## Bloqueo

`TAREA-066` a `TAREA-069` quedan bloqueadas hasta resolver esta pregunta: extraer ahora
consolidaría el mismo defecto en 32 fichas más.

Al resolverse debería registrarse como `DEC-NNNN`, previsiblemente como revisión de `DEC-0004`
y `DEC-0007`.

## Datos de la auditoría (2026-08-05, TAREA-072)

Se han contrastado las 18 fichas `completado` de ESO —101 competencias— contra el texto oficial
del Decreto 30/2023. Informe completo en
`11_calidad/informes/2026-08-05-auditoria-descriptores-operativos.md`.

| Situación | Competencias |
| --- | ---: |
| Los descriptores coinciden con los de un curso del decreto | 78 |
| Divergen: códigos que no están en ninguna versión de curso | 5 |
| No comparables: el extractor no localizó el bloque | 12 |
| No comparables: el enunciado de la ficha no es literal | 6 |

Sobre las 83 efectivamente comparadas, **divergen 5 (6,0 %)**.

Lo que esto cambia respecto al planteamiento inicial de esta pregunta:

1. **No procede degradar las 18 en bloque.** El grueso del corpus resiste el contraste y seis
   fichas salen sin ninguna incidencia: `CUR-004`, `CUR-008`, `CUR-011`, `CUR-017`, `CUR-018`
   y `CUR-020`.
2. **Las incidencias graves se concentran en dos fichas**, `CUR-001` y `CUR-009`, que reúnen
   las 5 divergencias. `CUR-001` C3 tiene siete códigos inexistentes en la fuente y omite
   cuatro presentes en los tres cursos.
3. **11 competencias declaran una lista válida solo para uno de los cursos** de su materia. Es
   el problema de modelo que motiva esta pregunta, ahora cuantificado.
4. **Aparece un problema que esta pregunta no contemplaba: la literalidad.** Seis enunciados no
   reproducen el texto del decreto, tres de ellos con similitudes de 0,37, 0,52 y 0,62 —textos
   distintos, no variantes de redacción—. `DEC-0004` exige el enunciado oficial, así que estas
   seis lo incumplen al margen de sus descriptores. Conviene extender la comprobación al campo
   `descripcion` de las 32 fichas parciales, que nunca se ha contrastado.

Con esto, la decisión sobre el punto 2 de esta pregunta —qué hacer con las fichas ya marcadas
`completado`— puede tomarse por ficha en lugar de en bloque.

## Un quinto problema: la `descripcion` de las fichas parciales no es el enunciado oficial

Al extender la comprobación a las 32 fichas en `estado_extraccion: parcial` —201 competencias—
se ve que su campo `descripcion` **no reproduce el texto del decreto**. Caso verificado,
`CUR-037` competencia 1:

- Ficha: «Adoptar un estilo de vida activo y saludable, incorporando actividades físicas y
  deportivas en las rutinas diarias para mejorar la calidad de vida.»
- Decreto: «Adoptar un estilo de vida activo y saludable, seleccionando e incorporando
  intencionalmente…»

Arranca con la redacción oficial y a partir de ahí resume. Reparto aproximado:

| | Competencias |
| --- | ---: |
| Literales (coinciden 12 palabras o más) | 9 |
| Empiezan literales y luego resumen | 29 |
| Solo coincide el arranque | 52 |
| Sin coincidencia localizada | 111 |

La cifra exacta depende del método y es menos fiable en Primaria e Infantil, cuyos decretos
tienen otra estructura y donde no se ha localizado el bloque competencial. Pero el hecho
cualitativo está verificado: **`descripcion` es un resumen, no el enunciado oficial**.

Esto no es un defecto nuevo, sino la otra cara de que estas fichas sean parciales. Importa
porque un sistema RAG que cite una de ellas estaría citando una paráfrasis como si fuera el
texto de la norma. `DEC-0004` exige la redacción oficial.

Consecuencia para `TAREA-066` a `TAREA-069`: cuando se desbloqueen, no basta con añadir los
descriptores operativos. Hay que **sustituir también `descripcion` por el enunciado literal**,
y previsiblemente renombrar el campo a `enunciado_oficial` para alinearlo con las fichas
completas.

## Respuesta (2026-08-05)

Resuelta en `DEC-0008`, que decide las tres cosas que esta pregunta dejaba abiertas.

**1. Modelo.** `descriptores` pasa a ser un mapa de curso a lista de códigos, siempre, también
cuando la materia se imparte en un solo curso. Una única forma evita que cada consumidor
distinga dos tipos.

**2. Alcance de la corrección.** No se degradan las 18 fichas. Rehecha la auditoría con un
extractor que cubre 616 bloques —frente a los 308 iniciales— y que ancla en el texto de la
competencia en lugar de en la estructura del documento, el resultado mejora sustancialmente:

| Situación | Competencias |
| --- | ---: |
| Coinciden con los descriptores de un curso del decreto | 94 |
| Divergen de todas las versiones de curso | 5 |
| No comparables: el enunciado no es literal | 2 |

**94 de 101, un 93,1 %.** Las 5 divergencias y los 2 enunciados no literales están todos en
`CUR-001` y `CUR-009`, y se corrigen en `TAREA-073`.

**20 de las 99 competencias comparadas tienen descriptores distintos según el curso**, casi el
doble de lo estimado con la medición anterior. Confirma que el problema de modelo era real y no
marginal.

**3. Literalidad.** El enunciado es siempre literal y el campo se llama `enunciado_oficial` en
todas las fichas. En las parciales, `descripcion` se sustituye durante la re-extracción.

## Estado de aplicación

`TAREA-075` ya ha migrado las 18 fichas al mapa por curso: 94 competencias migradas con su
vinculación verificada contra la fuente, y las 7 problemáticas intactas, marcadas como aviso por
el validador hasta que `TAREA-073` las resuelva. No se sustituye un dato dudoso por otro sin
evidencia.

