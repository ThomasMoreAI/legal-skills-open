---
id: TAREA-073
titulo: "Re-extraer CUR-001 y CUR-009, que concentran las divergencias con el texto oficial"
estado: "Hecha"
prioridad: "Alta"
tipo: "curriculo"
responsable: "@.agents/skills/analisis-curricular"
fecha_creacion: 2026-08-05
fecha_actualizacion: 2026-08-05
fecha_cierre: 2026-08-05
relacionadas: [PREG-008, DEC-0008, CUR-001, CUR-009, NOR-005, FTE-009, TAREA-072, TAREA-075]
siguiente_accion: "Re-extraer las competencias de CUR-001 desde el Decreto 30/2023, empezando por C3 y C5."
---

# TAREA-073 — Re-extracción de CUR-001 y CUR-009

## Objetivo

`TAREA-072` encontró que las cinco divergencias de descriptores del corpus de ESO se concentran
en estas dos fichas, junto con buena parte de los enunciados que no reproducen la fuente.

## Qué corregir

### `CUR-001` — Biología y Geología

- **C3**: la ficha declara siete códigos que no aparecen en ninguna versión de curso del decreto
  (CCL5, CD3, CE1, CP1, CPSAA4, CCEC3, CCEC4) y omite cuatro que están en los tres
  (CCL3, STEM1, STEM3, CPSAA3). La lista guarda poca relación con la fuente.
- **C5**: declara `CC2`, que no aparece, y omite `CPSAA1`, presente en los tres cursos.
- **C4** y **C6**: el enunciado no reproduce el decreto (similitudes 0,62 y 0,52).

### `CUR-009` — Educación Plástica, Visual y Audiovisual

- **C6**, **C7** y **C8**: contienen códigos ausentes de la fuente.
- **C2**: el enunciado no es literal.

## Cómo hacerlo

1. Abrir `FTE-009` o la copia local del Decreto 30/2023 en `07_corpus_ia/textos-completos/`.
2. Localizar el bloque competencial de cada materia y curso.
3. Volcar el enunciado **literal** y los descriptores que el decreto asigna a cada competencia.
4. Si `PREG-008` ya está resuelta, aplicar el modelo que fije para la dimensión de curso; si no,
   dejar constancia en `observaciones` de a qué curso corresponde cada lista.
5. Validar con `python3 11_calidad/validar_corpus.py`.

## Advertencia

Ambas fichas están hoy en `estado_extraccion: completado`. Hasta corregirlas, ese estado no se
sostiene contra la fuente. Si esta tarea se demora, conviene degradarlas a `parcial` para no
dar por buenos unos datos que la auditoría ya ha desmentido.

## Coordinación con trabajo paralelo

IDs consumidos: `TAREA-073`. Solo se modifican `CUR-001` y `CUR-009`.

## Alcance acotado tras TAREA-075 (2026-08-05)

El extractor corregido reduce el trabajo a **siete competencias**, las únicas que no se pudieron
verificar contra la fuente. El resto de ambas fichas ya está migrado a mapa por curso con su
vinculación comprobada.

| Ficha | Comp. | Problema |
| --- | --- | --- |
| `CUR-001` | C3 | Diverge: 7 códigos ausentes de la fuente, faltan 4 presentes en los tres cursos |
| `CUR-001` | C4 | Enunciado no literal: no se puede anclar en el decreto |
| `CUR-001` | C5 | Diverge: declara `CC2`, que no aparece; omite `CPSAA1`, que sí |
| `CUR-001` | C6 | Enunciado no literal |
| `CUR-009` | C6 | Diverge: sobran `CCL1`, `CCL3`, `CD2`, `CP3` |
| `CUR-009` | C7 | Diverge: sobran `CCL2`, `CD2`, `CE1`, `CE2`, `CPSAA3`, `CPSAA4` |
| `CUR-009` | C8 | Diverge: sobran `CD2`, `CE3` |

Las siete conservan la lista plana y el validador las reporta como aviso, así que están
localizadas sin necesidad de volver a auditar.

Para las dos con enunciado no literal, el orden correcto es **primero corregir el
`enunciado_oficial`** con el texto del decreto y después extraer, porque el extractor se ancla
en ese texto: con el enunciado literal, `11_calidad/extraer_descriptores.py --auditar` resolverá
la vinculación sin trabajo manual.

## Resultado (2026-08-05)

Las siete competencias corregidas y verificadas contra el Decreto 30/2023, localizando los
bloques por sección de materia y cabecera de curso.

En `CUR-001` se corrigieron primero los enunciados no literales de C4 y C6 y, de paso, dos
desviaciones menores de literalidad que la auditoría no había detectado: «cooperando, cuando sea
necesario» por «cooperando cuando sea necesario» en C3, y «medioambiente» por «medio ambiente»
en C5 —esta última era justamente la que rompía el anclaje del extractor—. Después se migraron
C3, C4, C5 y C6 a mapa por curso.

En `CUR-009` los enunciados de C6, C7 y C8 ya eran literales; lo que faltaba era el desglose por
curso. Sus descriptores «sobrantes» resultaron ser los de **2.º de ESO**: la lista plana
original recogía esa variante y por eso parecía divergir.
