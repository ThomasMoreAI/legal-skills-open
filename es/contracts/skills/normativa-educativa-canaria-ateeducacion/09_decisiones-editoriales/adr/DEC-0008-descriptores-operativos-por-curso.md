---
id: DEC-0008
titulo: "Representación por curso de los descriptores operativos y literalidad del enunciado"
estado: "Aceptada"
fecha: 2026-08-05
relacionadas: [PREG-008, DEC-0004, DEC-0007, CUR-001, CUR-009, TAREA-072, TAREA-073, TAREA-075]
---

# DEC-0008 — Descriptores operativos por curso y literalidad del enunciado

## Contexto

`DEC-0004` fijó que la ficha curricular debe recoger la vinculación de cada competencia
específica con los descriptores operativos del perfil de salida, y `DEC-0007` unificó el
contenedor `elementos`. Ninguna de las dos previó que **los descriptores no son los mismos en
todos los cursos** en que se imparte una materia.

La auditoría de `TAREA-072`, rehecha con un extractor que cubre 616 bloques competenciales del
Decreto 30/2023, midió el alcance sobre las 18 fichas de ESO en `estado_extraccion: completado`
—101 competencias—:

| Situación | Competencias |
| --- | ---: |
| Los descriptores coinciden con los de un curso del decreto | 94 |
| Divergen de todas las versiones de curso | 5 |
| No comparables: el enunciado de la ficha no es literal | 2 |

**20 de las 99 competencias comparadas tienen descriptores distintos según el curso.** El modelo
guardaba una lista plana, así que en esos casos la ficha reproducía fielmente uno de los cursos
y callaba que en los demás era otra.

## Decisión

**1. `descriptores` pasa a ser un mapa por curso.** Siempre, también cuando la materia se imparte
en un solo curso: una única forma evita que cada consumidor tenga que distinguir dos tipos.

```yaml
competencias_especificas:
  - codigo: C2
    enunciado_oficial: "Identificar, localizar y reconocer..."
    descriptores:
      "1.º ESO": [CCL3, CD1, CD2, CD4, CPSAA4]
      "3.º ESO": [CCL3, STEM4, CD1, CD2, CD3, CD4, CD5, CPSAA4]
      "4.º ESO": [CCL3, STEM4, CD1, CD2, CD3, CD4, CD5, CPSAA4]
```

Las claves del mapa son los cursos tal como los nombra el decreto. `elementos.descriptores_operativos`
se mantiene como catálogo plano de los códigos usados en la ficha, para consulta rápida.

**2. El enunciado de la competencia es siempre literal.** El campo se llama `enunciado_oficial` en
todas las fichas y contiene la redacción del decreto sin resumir ni reformular. En las fichas
parciales, el campo `descripcion` —que hoy contiene un resumen— se sustituye por
`enunciado_oficial` con el texto literal durante la re-extracción.

Un resumen es legítimo como material derivado, pero no puede ocupar el lugar del texto normativo:
un sistema que cite la ficha estaría citando una paráfrasis como si fuera la norma, contra R7.

**3. Alcance de la corrección de las fichas ya completadas.** No se degradan las 18 en bloque: 94
de 101 competencias reproducen la fuente. Se corrigen las que la auditoría señala —las 5
divergencias y los 2 enunciados no literales, todas en `CUR-001` y `CUR-009`— y se mantiene el
resto. `TAREA-073` recoge ese trabajo.

## Consecuencias

- El esquema admite `descriptores` como mapa de curso a lista de códigos.
- `11_calidad/extraer_descriptores.py` se incorpora al repositorio. Ancla en el texto de la
  competencia en lugar de en la estructura del documento, porque la conversión del PDF
  entremezcla las celdas de la tabla, y normaliza tildes y espacios para absorber variantes como
  «medio ambiente» frente a «medioambiente».
- `TAREA-066` a `TAREA-069` se desbloquean con el modelo ya definido, y su alcance incluye
  sustituir `descripcion` por `enunciado_oficial`.
- Los decretos de Primaria (`NOR-043`) e Infantil (`NOR-047`) tienen otra estructura: el
  extractor no localiza bloques en ellos. `TAREA-067` y `TAREA-069` requieren un análisis previo
  de esos textos.

## Alternativas descartadas

- **Una ficha por materia y curso**: máxima precisión de consulta, pero multiplica los `CUR-NNN`,
  rompe la correlación de IDs ya establecida y obliga a duplicar los saberes básicos, que sí son
  comunes.
- **Lista plana declarando a qué curso corresponde**: cambio mínimo, pero pierde la información
  de los demás cursos, que es justo lo que la auditoría demostró que falta.

## Relación con IA

Un chunk generado a partir de una competencia debe indicar el curso al que corresponden los
descriptores que cita. Sin esa marca, la cita es ambigua en las 20 competencias afectadas.
