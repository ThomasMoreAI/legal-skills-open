---
id: TAREA-075
titulo: "Migrar los descriptores operativos a mapa por curso e incorporar el extractor al repositorio"
estado: "Hecha"
prioridad: "Alta"
tipo: "curriculo"
responsable: "@.agents/skills/analisis-curricular"
fecha_creacion: 2026-08-05
fecha_actualizacion: 2026-08-05
fecha_cierre: 2026-08-05
relacionadas: [DEC-0008, PREG-008, CUR-001, CUR-009, NOR-005, TAREA-072, TAREA-073]
---

# TAREA-075 — Migración a mapa por curso

## Objetivo

Aplicar `DEC-0008`: pasar `descriptores` de lista plana a mapa por curso en las 18 fichas de ESO
que los tienen volcados, y dejar el extractor como herramienta del repositorio.

## Trabajo realizado

### El extractor, corregido y verificado

`TAREA-072` usó un extractor que localizaba 308 bloques de unos 637 y dejaba 18 competencias sin
comparar. Dos fallos, ambos corregidos:

1. **La marca de descriptores tiene dos formas.** Unas veces es «Descriptores operativos de las
   competencias clave. Perfil de salida» y otras solo «…competencias clave». Exigir el sufijo
   dejaba fuera 327 bloques. Cobertura: de 308 a **616**.
2. **La conversión del PDF entremezcla las celdas de la tabla.** Unas veces el enunciado precede
   a la marca y otras la sigue, así que analizar la estructura del documento era frágil. El
   extractor pasa a **anclar en el texto de la competencia** y recoger los códigos que van entre
   el enunciado y «Criterios de evaluación», que funciona con ambas disposiciones.

Además normaliza tildes y **todos los espacios** antes de buscar, lo que absorbe los saltos de
línea dentro de una frase y variantes como «medio ambiente» frente a «medioambiente», que
rompían el anclaje exacto.

Resultado sobre las 101 competencias: **94 verificadas** (93,1 %), 5 divergentes y 2 con
enunciado no literal, frente a 78/5/18 de la medición anterior. Las 5 divergencias son las
mismas que se habían verificado a mano, lo que respalda el método.

`11_calidad/extraer_descriptores.py` queda en el repositorio con modo `--auditar` y `--cobertura`.

### La migración

Las 94 competencias con vinculación verificada pasan a mapa por curso. Las 7 restantes —las 5
divergentes y las 2 no literales, todas en `CUR-001` y `CUR-009`— **se dejan intactas**: no se
sustituye un dato dudoso por otro sin evidencia. Quedan como lista plana y el validador las
reporta como aviso hasta que `TAREA-073` las resuelva.

Cada fichero se verificó tras la reescritura comprobando que el YAML sigue siendo válido y que
no se pierde ninguna competencia.

### Comprobaciones nuevas

- El esquema admite `descriptores` como mapa de curso a lista, y la lista plana como forma
  transitoria.
- El validador avisa de cada lista plana que quede, con referencia a `DEC-0008` y `TAREA-073`.

## Resultado

0 errores y 7 avisos, que son exactamente las 7 competencias pendientes. **20 de las 99
competencias comparadas tienen descriptores distintos según el curso**: casi el doble de lo
estimado antes de corregir el extractor, lo que confirma que el problema de modelo no era
marginal.

## Pendiente

Los decretos de Primaria (`NOR-043`) e Infantil (`NOR-047`) tienen otra estructura y el extractor
no localiza bloques en ellos. `TAREA-067` y `TAREA-069` necesitan un análisis previo de esos
textos antes de poder aplicar el mismo método.

## Coordinación con trabajo paralelo

IDs consumidos: `TAREA-075` y `DEC-0008`. Se han modificado las 18 fichas `CUR` de ESO con
descriptores volcados; no se ha creado ninguna entidad nueva.
