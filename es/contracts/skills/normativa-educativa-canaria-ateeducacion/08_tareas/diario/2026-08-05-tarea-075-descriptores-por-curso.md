# Diario — 2026-08-05: descriptores por curso (DEC-0008, TAREA-075)

## Decisiones tomadas

Resueltas las tres preguntas que bloqueaban `PREG-008`, registradas en `DEC-0008`:

1. **`descriptores` pasa a mapa por curso**, siempre, también en materias de un solo curso. Una
   única forma evita que cada consumidor distinga dos tipos.
2. **Se corrigen solo las fichas señaladas por la auditoría**, no las 18 en bloque, y además se
   verifican las competencias que habían quedado sin comparar.
3. **El enunciado es siempre literal**, en un campo `enunciado_oficial`. En las fichas parciales,
   `descripcion` se sustituye durante la re-extracción.

## El extractor tenía dos fallos, no uno

`TAREA-072` avisó de que el extractor localizaba 308 bloques de unos 637 y dejaba 18
competencias sin comparar. Al ir a arreglarlo aparecieron dos causas:

- **La marca tiene dos formas.** Unas veces «…competencias clave. Perfil de salida» y otras solo
  «…competencias clave». Exigir el sufijo dejaba fuera 327 bloques. Cobertura: 308 → **616**.
- **La conversión del PDF entremezcla las celdas de la tabla.** Unas veces el enunciado precede
  a la marca y otras la sigue, así que analizar la estructura era frágil. El extractor pasa a
  anclar en el texto de la competencia y recoger los códigos entre el enunciado y «Criterios de
  evaluación», que funciona con ambas disposiciones.

Corregir solo lo primero no cambió nada: seguían 18 sin emparejar. Fue el cambio de enfoque el
que lo resolvió. Y aún faltaba un detalle: normalizar tildes y **todos los espacios** antes de
buscar, porque la ficha dice «medioambiente» donde el decreto dice «medio ambiente» y el ancla
exacta fallaba.

## Resultado de la auditoría, rehecha

| Situación | Antes | Ahora |
| --- | ---: | ---: |
| Coinciden con un curso del decreto | 78 | **94** |
| Divergen | 5 | **5** |
| Sin comparar | 18 | **2** |

Las 5 divergencias son las mismas que se habían verificado a mano, lo que respalda el método. Y
un dato que cambia con la mejor cobertura: **20 de las 99 competencias comparadas tienen
descriptores distintos según el curso**, casi el doble de lo estimado. El problema de modelo no
era marginal.

## La migración

Las 94 competencias verificadas pasan a mapa por curso. Las 7 restantes —5 divergentes y 2 con
enunciado no literal, todas en `CUR-001` y `CUR-009`— se dejan intactas: no se sustituye un dato
dudoso por otro sin evidencia. Conservan la lista plana y el validador las reporta como aviso.

`11_calidad/extraer_descriptores.py` queda en el repositorio con modos `--auditar` y
`--cobertura`. El esquema admite el mapa por curso y la lista plana como forma transitoria.

`TAREA-073` queda acotada a esas siete, con una nota sobre el orden correcto: primero corregir el
`enunciado_oficial` y después extraer, porque el extractor se ancla en ese texto.

## Resultado

0 errores y 7 avisos, que son exactamente las 7 competencias pendientes. `TAREA-066` a `069` se
desbloquean con el modelo ya definido.

## IDs consumidos

`TAREA-075`, `DEC-0008`.

## Pendiente

Los decretos de Primaria e Infantil tienen otra estructura y el extractor no localiza bloques en
ellos: `TAREA-067` y `TAREA-069` necesitan un análisis previo de esos textos.
