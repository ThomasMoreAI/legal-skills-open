# Diario — 2026-08-05: auditoría de descriptores operativos (TAREA-072)

## Hecho

Contrastadas las 101 competencias de las 18 fichas de ESO en `estado_extraccion: completado`
contra el texto oficial del Decreto 30/2023, para dar a `PREG-008` el dato que le faltaba.

El emparejamiento se hace por el texto del enunciado, exigiendo similitud mínima de 0,90, y
anotando el curso de cada bloque del decreto. Por debajo de ese umbral no se compara: se reporta
aparte, para no arriesgar una comparación falsa.

## Resultado

| Situación | Competencias |
| --- | ---: |
| Coinciden con los descriptores de un curso del decreto | 78 |
| Divergen: códigos que no están en ninguna versión de curso | 5 |
| No comparables: el extractor no localizó el bloque | 12 |
| No comparables: el enunciado de la ficha no es literal | 6 |

Sobre las 83 efectivamente comparadas, divergen 5 — un 6,0 %.

## Lo que cambia el diagnóstico

**El corpus resiste mejor de lo temido.** Seis fichas salen impecables: `CUR-004`, `CUR-008`,
`CUR-011`, `CUR-017`, `CUR-018` y `CUR-020`. No procede degradar las 18 en bloque, y la decisión
de `PREG-008` puede tomarse ficha a ficha.

**Las incidencias graves están concentradas.** Las cinco divergencias son de `CUR-001` y
`CUR-009`. La peor es `CUR-001` C3: siete códigos que no existen en la fuente y cuatro ausentes
que sí están en los tres cursos. Abierta `TAREA-073` para re-extraerlas.

**Aparece un problema que `PREG-008` no contemplaba: la literalidad.** Seis enunciados no
reproducen el texto del decreto, tres de ellos con similitudes de 0,37, 0,52 y 0,62 —textos
distintos, no variantes de redacción—. `DEC-0004` exige el enunciado oficial, así que lo
incumplen al margen de sus descriptores. Conviene extender la comprobación al campo
`descripcion` de las 32 fichas parciales, que nunca se ha contrastado.

**El problema de modelo queda cuantificado.** 11 competencias declaran una lista válida solo
para uno de los cursos de su materia, mientras la ficha se presenta como válida para todos.

## Sobre el método

El extractor localiza 308 de las ~392 competencias del decreto, así que 12 competencias quedan
sin verificar: sirve para auditar, no todavía para volcar datos. No se incorpora al repositorio
por ser de un solo uso y depender de una conversión de PDF; el método queda descrito en el
informe para poder rehacerlo.

Esta sesión se trabajó sobre un clon del repositorio: macOS revocó a mitad de sesión el acceso
de lectura a `~/Downloads`, donde vive la copia local. No afecta al contenido.

## IDs consumidos

`TAREA-072`, `TAREA-073`.

## Pendiente

- `PREG-008`: decidir el modelo para la dimensión de curso y qué hacer con cada ficha.
- `TAREA-073`: re-extraer `CUR-001` y `CUR-009`.
- Extender la comprobación de literalidad a las 32 fichas parciales.
