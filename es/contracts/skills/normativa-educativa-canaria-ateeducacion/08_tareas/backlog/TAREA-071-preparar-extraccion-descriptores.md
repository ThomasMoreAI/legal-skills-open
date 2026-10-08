---
id: TAREA-071
titulo: "Preparar la extracción de descriptores operativos y verificar el conjunto de control"
estado: "Hecha"
prioridad: "Alta"
tipo: "curriculo"
responsable: "@.agents/skills/analisis-curricular"
fecha_creacion: 2026-08-05
fecha_actualizacion: 2026-08-05
fecha_cierre: 2026-08-05
relacionadas: [PREG-008, CUR-001, NOR-005, TAREA-066, TAREA-067, TAREA-068, TAREA-069]
---

# TAREA-071 — Preparación de la extracción de descriptores operativos

## Objetivo

Ejecutar `TAREA-066` a `TAREA-069`: volcar los descriptores operativos del perfil de salida en
las 32 fichas curriculares en `estado_extraccion: parcial`.

## Trabajo realizado

Se identificó el patrón del bloque competencial en el texto oficial del Decreto 30/2023, que
está disponible en local (`07_corpus_ia/textos-completos/`):

```
Competencia específica
N. <enunciado oficial>
Descriptores operativos de las
competencias clave. Perfil de salida
<códigos>
Criterios de evaluación
```

Se escribió un extractor y se validó contra las 18 fichas de ESO que ya tenían descriptores
volcados, tomándolas como conjunto de control. El resultado fue de 75 coincidencias exactas
sobre 101 competencias, insuficiente para aplicarlo.

Al investigar las discrepancias apareció la causa, que no era del extractor.

## Hallazgo

**Los descriptores operativos varían según el curso** en el que se imparte la materia. La misma
competencia específica tiene listas distintas en 1.º y en 3.º de ESO. El modelo actual guarda
una lista plana por competencia y no puede representarlo.

Además, comparando `CUR-001` con el texto oficial, solo la primera de sus seis competencias
coincide exactamente; en la competencia 5 la ficha declara `CC2`, que no aparece en la fuente, y
omite `CPSAA1`, que sí aparece en los tres cursos.

De las 18 fichas dadas por completas, 8 declaran varios cursos, y ninguna de las 32 parciales
declara `cursos`.

El detalle y la evidencia quedan en `PREG-008`.

## Decisión

No se aplica la extracción. Hacerlo consolidaría el mismo defecto en 32 fichas más y añadiría
datos normativos que no reproducen la fuente, contra R1.

`TAREA-066` a `TAREA-069` pasan a `Bloqueada` y recogen el trabajo de preparación —patrón de
extracción identificado y textos disponibles en local— para quien las retome tras resolver
`PREG-008`.

## Coordinación con trabajo paralelo

IDs consumidos: `TAREA-071` y `PREG-008`. No se ha modificado ninguna ficha `CUR`.
