---
id: TAREA-076
titulo: "Consolidar la extracción curricular ejecutada en paralelo y corregir el auditor de descriptores"
estado: "Hecha"
prioridad: "Alta"
tipo: "curriculo"
responsable: "@.agents/skills/control-calidad-documental"
fecha_creacion: 2026-08-05
fecha_actualizacion: 2026-08-05
fecha_cierre: 2026-08-05
relacionadas: [PREG-009, DEC-0008, TAREA-066, TAREA-067, TAREA-068, TAREA-069, TAREA-070, TAREA-073, TAREA-077]
---

# TAREA-076 — Consolidación de la extracción curricular en paralelo

## Objetivo

Ejecutar en paralelo las tareas curriculares pendientes y consolidar el resultado: verificar lo
producido contra la fuente oficial, sincronizar índices y registrar los hallazgos.

## Qué se ejecutó

Siete ramas independientes, cada una limitada a sus propias fichas `CUR` para que no se pisaran:
Bachillerato en dos lotes, ESO, Primaria y Infantil con análisis previo del decreto, las siete
competencias de `TAREA-073` y la localización de `FTE-051`.

## Verificación: tres fallos eran del auditor, no de la extracción

Los agentes de Bachillerato reportaron que `extraer_descriptores.py --auditar` marcaba su
trabajo como divergente y lo atribuían a limitaciones de la herramienta. Comprobado punto por
punto, **tenían razón en los tres casos**:

1. **Comparación rota tras `DEC-0008`.** El auditor seguía comparando `descriptores` como lista
   plana, así que con el mapa por curso comparaba códigos contra nombres de curso. Toda ficha
   migrada salía divergente.
2. **Subcódigos decimales truncados.** Bachillerato usa `CPSAA1.1`, `CCEC3.2` y similares —197
   apariciones de `CPSAA1.1` solo en el decreto—, que la expresión regular reducía a `CPSAA1`.
3. **Variantes por curso colapsadas.** Cuando no se detectaba la cabecera de curso, todas las
   apariciones caían bajo la clave `?` y `setdefault` conservaba solo la primera, ocultando justo
   las variantes que interesan. Era la causa de que `CUR-009` pareciera divergir: sus
   descriptores «sobrantes» son los de 2.º de ESO.

Corregidos los tres, y añadida la búsqueda en los textos por materia
(`texto-oficial-CUR-0NN-*.txt`) para las cuatro materias propias de Canarias, que no figuran en
el decreto consolidado.

## Resultado de la verificación

**229 de 230 competencias verifican contra la fuente oficial (99,6 %).** La restante,
`CUR-057` C5, se comprobó a mano: también es correcta; el anclaje falla porque un número de
página parte la frase en la conversión del PDF.

El reparto de extracción curricular pasa de 26 completadas y 32 parciales a **38 y 20**.

## Hallazgos que no estaban previstos

- **Infantil no tiene descriptores operativos.** El Perfil de salida es de la enseñanza básica y
  el Decreto 196/2022 describe las competencias clave solo en prosa. `TAREA-069` se cierra por
  no proceder, y el cuarto elemento de `DEC-0004` no aplica a esta etapa.
- **La copia local del decreto de Primaria no sirve.** Sus anexos se publican como PDF o imagen
  y la conversión los sustituyó por un marcador: cero descriptores en todo el fichero.
  `TAREA-067` queda bloqueada y `TAREA-077` recoge la re-exportación.
- **`FTE-051` declara una resolución que no existe** como norma diferenciada. Queda como
  `PREG-009`.

## Coordinación con trabajo paralelo

IDs consumidos: `TAREA-076`, `TAREA-077`, `PREG-009`. Se modificaron 21 fichas `CUR` y el índice
`06_indices/curriculos.yaml`. Ninguna entidad nueva `FTE`, `NOR`, `REL` ni `CHUNK`.
