---
id: TAREA-072
titulo: "Auditar los descriptores operativos de las 18 fichas de ESO marcadas como completadas"
estado: "Hecha"
prioridad: "Alta"
tipo: "calidad-documental"
responsable: "@.agents/skills/control-calidad-documental"
fecha_creacion: 2026-08-05
fecha_actualizacion: 2026-08-05
fecha_cierre: 2026-08-05
relacionadas: [PREG-008, CUR-001, CUR-009, NOR-005, TAREA-071, TAREA-073]
---

# TAREA-072 — Auditoría de descriptores operativos

## Objetivo

Dar a `PREG-008` el dato que le faltaba para poder decidirse: cuántas competencias de las 18
fichas en `estado_extraccion: completado` divergen realmente del texto oficial.

## Trabajo realizado

Contraste de las 101 competencias de esas 18 fichas contra
`07_corpus_ia/textos-completos/texto-oficial-NOR-005-decreto-30-2023.txt`, emparejando por el
texto del enunciado con una similitud mínima de 0,90 y anotando el curso de cada bloque del
decreto.

Informe completo en `11_calidad/informes/2026-08-05-auditoria-descriptores-operativos.md`.

## Resultado

| Situación | Competencias |
| --- | ---: |
| Coinciden con los descriptores de un curso del decreto | 78 |
| Divergen: códigos que no están en ninguna versión de curso | 5 |
| No comparables: el extractor no localizó el bloque | 12 |
| No comparables: el enunciado de la ficha no es literal | 6 |

Sobre las 83 efectivamente comparadas, divergen 5 (6,0 %).

Hallazgos:

- Seis fichas salen sin ninguna incidencia: `CUR-004`, `CUR-008`, `CUR-011`, `CUR-017`,
  `CUR-018` y `CUR-020`.
- Las 5 divergencias se concentran en `CUR-001` y `CUR-009`.
- 11 competencias declaran una lista válida solo para uno de los cursos de su materia.
- Seis enunciados no reproducen literalmente el decreto, lo que incumple `DEC-0004` al margen
  de los descriptores. Es un problema que `PREG-008` no contemplaba.

## Conclusión

No procede degradar las 18 fichas en bloque: la decisión de `PREG-008` puede tomarse por ficha.
La re-extracción completa de `CUR-001` y `CUR-009` queda abierta en `TAREA-073`.

El extractor sirve para auditar pero no todavía para volcar datos: localiza 308 de unas 392
competencias del decreto. No se incorpora al repositorio por ser de un solo uso y depender de
una conversión de PDF; el método queda descrito en el informe.

## Coordinación con trabajo paralelo

IDs consumidos: `TAREA-072` y `TAREA-073`. No se ha modificado ninguna ficha `CUR`: esta tarea
solo audita.
