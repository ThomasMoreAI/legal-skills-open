---
id: TAREA-067
titulo: "Extraer los descriptores operativos de las fichas curriculares de primaria (CUR-024 a CUR-033)"
estado: "Hecha"
prioridad: "Alta"
tipo: "curriculo"
responsable: "@.agents/skills/analisis-curricular"
fecha_creacion: 2026-08-05
fecha_actualizacion: 2026-08-05
fecha_cierre: 2026-08-05
relacionadas: [PREG-008, FTE-046, NOR-043, TAREA-065, PREG-007]
siguiente_accion: "Volcar los descriptores operativos del perfil de salida desde FTE-046 a las 10 fichas y pasarlas a estado_extraccion completado."
---

# TAREA-067 — Descriptores operativos de primaria

## Objetivo

Completar el cuarto elemento obligatorio de `DEC-0004` en las 10 fichas curriculares de
primaria (CUR-024 a CUR-033), que hoy están en `estado_extraccion: parcial` por carecer de la
vinculación con los descriptores operativos del perfil de salida.

## Contexto

`DEC-0007` unificó el contenedor `elementos` de todas las fichas curriculares y marcó como
`parcial` las que no reúnen los cuatro elementos de `DEC-0004`. Las fichas de esta etapa
tienen competencias específicas, criterios de evaluación y saberes básicos, pero no
descriptores operativos.

Las fichas de ESO `CUR-001` a `CUR-014` sirven de referencia: están en `completado` y
muestran el formato esperado dentro de `elementos.descriptores_operativos`.

## Qué hacer

1. Abrir la fuente oficial `FTE-046` y localizar el perfil de salida y sus descriptores operativos.
2. Para cada una de las 10 fichas, volcar la vinculación entre cada competencia específica y
   sus descriptores, con la numeración oficial y sin reformular el texto (R1, R7).
3. Pasar la ficha a `estado_extraccion: "completado"` y realinear `06_indices/curriculos.yaml`.
4. Retirar de `observaciones` la nota `[PENDIENTE]` sobre descriptores operativos.
5. Ejecutar `python3 11_calidad/validar_corpus.py` y comprobar 0 errores.

## Coordinación con trabajo paralelo

IDs consumidos: `TAREA-067`. No se crean entidades nuevas: solo se completan fichas `CUR`
existentes. No tocar fichas fuera del rango CUR-024 a CUR-033.

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

## Bloqueo (2026-08-05): la copia local no sirve

El análisis previo encontró que **el texto local de `NOR-043` no contiene ni los enunciados de
las competencias específicas ni los descriptores operativos**. Cero códigos de descriptor
(`CCL1`, `STEM4`…) en todo el fichero.

No es un fallo de la extracción del corpus: los bloques competenciales se publican en el BOC
como **anexo en PDF o imagen**, y la conversión a texto los sustituyó por un marcador.

Antes de poder ejecutar esta tarea hay que conseguir una copia utilizable del Anexo del Decreto
211/2022 —del PDF oficial, no del HTML— y registrarla en `06_indices/textos-oficiales.yaml`
conforme a R16. Eso queda como `TAREA-077`.

## Resultado (2026-08-05)

Nueve de las diez fichas pasan a `estado_extraccion: completado`: `CUR-024` a `CUR-032`.

Los descriptores se mapean **por ciclo** —«Primer ciclo», «Segundo ciclo», «Tercer ciclo»—, que
es como los organiza el Decreto 211/2022, y varían realmente entre ciclos en varias competencias
de Educación Artística, Educación Física, Matemáticas y Educación Emocional. Se añadió además el
campo `cursos`, que faltaba en las diez.

La extracción se validó contrastando, área por área, el número de competencias y de criterios
resultante contra lo que el propio decreto declara en su introducción: coincide en las nueve
áreas. Verificación independiente posterior: 56 de las 62 competencias localizadas literalmente
en el texto oficial; las 6 restantes son las de `CUR-033`, que no se tocó.

Se corrigieron dos erratas heredadas detectadas al contrastar con la fuente: los títulos de los
bloques III a V de saberes de `CUR-030` no correspondían al decreto, y a `CUR-032` le faltaba el
cuarto bloque, «Dimensiones Interpersonal e Intrapersonal».

`CUR-033` (Religión) **queda en `parcial`**: el Decreto 211/2022 no contiene su currículo. Su
disposición adicional primera delega esa competencia en la jerarquía eclesiástica, y el currículo
se publica en el BOE. Seguimiento en `TAREA-082`.
