---
id: TAREA-068
titulo: "Extraer los descriptores operativos de las fichas curriculares de eso (CUR-015 a CUR-023)"
estado: "Hecha"
prioridad: "Media"
tipo: "curriculo"
responsable: "@.agents/skills/analisis-curricular"
fecha_creacion: 2026-08-05
fecha_actualizacion: 2026-08-05
fecha_cierre: 2026-08-05
relacionadas: [PREG-008, FTE-009, NOR-005, TAREA-065, PREG-007]
siguiente_accion: "Volcar los descriptores operativos del perfil de salida desde FTE-009 a las 5 fichas y pasarlas a estado_extraccion completado."
---

# TAREA-068 — Descriptores operativos de eso

## Objetivo

Completar el cuarto elemento obligatorio de `DEC-0004` en las 5 fichas curriculares de
eso (CUR-015 a CUR-023), que hoy están en `estado_extraccion: parcial` por carecer de la
vinculación con los descriptores operativos del perfil de salida.

## Contexto

`DEC-0007` unificó el contenedor `elementos` de todas las fichas curriculares y marcó como
`parcial` las que no reúnen los cuatro elementos de `DEC-0004`. Las fichas de esta etapa
tienen competencias específicas, criterios de evaluación y saberes básicos, pero no
descriptores operativos.

Las fichas de ESO `CUR-001` a `CUR-014` sirven de referencia: están en `completado` y
muestran el formato esperado dentro de `elementos.descriptores_operativos`.

## Qué hacer

1. Abrir la fuente oficial `FTE-009` y localizar el perfil de salida y sus descriptores operativos.
2. Para cada una de las 5 fichas, volcar la vinculación entre cada competencia específica y
   sus descriptores, con la numeración oficial y sin reformular el texto (R1, R7).
3. Pasar la ficha a `estado_extraccion: "completado"` y realinear `06_indices/curriculos.yaml`.
4. Retirar de `observaciones` la nota `[PENDIENTE]` sobre descriptores operativos.
5. Ejecutar `python3 11_calidad/validar_corpus.py` y comprobar 0 errores.

## Coordinación con trabajo paralelo

IDs consumidos: `TAREA-068`. No se crean entidades nuevas: solo se completan fichas `CUR`
existentes. No tocar fichas fuera del rango CUR-015 a CUR-023.

## Desbloqueada (2026-08-05)

`PREG-008` quedó resuelta en `DEC-0008`, así que esta tarea se desbloquea. Al preparar la extracción se comprobó contra el texto oficial que
**los descriptores operativos varían según el curso** en el que se imparte la materia, y el modelo ya admite el mapa por curso que fija `DEC-0008`.

Trabajo de preparación ya hecho, aprovechable cuando se desbloquee:

- El texto oficial completo está en local: `07_corpus_ia/textos-completos/`.
- El patrón de extracción está identificado. Cada bloque competencial tiene la forma:

  ```
  Competencia específica
  N. <enunciado oficial>
  Descriptores operativos de las
  competencias clave. Perfil de salida
  <códigos, repartidos en varias líneas>
  Criterios de evaluación
  ```

- Los bloques se repiten por curso dentro de cada materia, que es justo el origen del problema.
- Antes de extraer hay que rellenar `cursos` en estas fichas: hoy ninguna lo declara, y sin ese
  dato la extracción no es interpretable.

## Alcance ampliado (2026-08-05)

`PREG-008` recoge un hallazgo posterior: el campo `descripcion` de estas fichas **es un resumen,
no el enunciado oficial** del decreto. Cuando esta tarea se desbloquee no bastará con añadir los
descriptores operativos: hay que sustituir también `descripcion` por el texto literal y
renombrar el campo a `enunciado_oficial`, como en las fichas completas.

## Resultado (2026-08-05)

Las 5 fichas —`CUR-015`, `CUR-016`, `CUR-019`, `CUR-021`, `CUR-023`— pasan a
`estado_extraccion: completado`. Enunciados literales y descriptores por curso extraídos del
Decreto 30/2023 y verificados contra la fuente.

`criterios_evaluacion` y `saberes_basicos` ya estaban presentes como selección representativa y
no se han tocado.
