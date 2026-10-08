---
id: TAREA-083
titulo: "Fusionar las fichas normativas desdobladas por etapa y detectar el patrón en el validador"
estado: "Hecha"
prioridad: "Alta"
tipo: "calidad-documental"
responsable: "@.agents/skills/control-calidad-documental"
fecha_creacion: 2026-08-05
fecha_actualizacion: 2026-08-05
fecha_cierre: 2026-08-05
relacionadas: [DEC-0010, PREG-009, NOR-044, NOR-046, NOR-047, FTE-047, FTE-051]
---

# TAREA-083 — Fusión de fichas desdobladas por etapa

## Objetivo

Resolver lo que `PREG-009` dejó anotado: si el desdoblamiento de una norma en varias fichas por
etapa es deliberado o duplicación, y aplicar el criterio en todo el corpus.

## Alcance real

Se buscó el patrón sistemáticamente por dos señales —fichas que comparten `fecha_disposicion` y
`fuente_principal`, y copias locales con contenido idéntico— y aparecieron **exactamente dos
casos**, ambos confirmados por ambas señales:

| Norma | Fichas | |
| --- | --- | --- |
| Resolución conjunta 73/2025 | `NOR-046` + `NOR-049` | ya fusionadas |
| Orden de 31 de mayo de 2023, evaluación y promoción | `NOR-044` + `NOR-048` | fusionadas aquí |

## Trabajo realizado

`DEC-0010` fija el criterio: una norma, una ficha. La etapa se expresa en `etapas_afectadas` y en
apartados del cuerpo, no duplicando entidades.

`NOR-048` se fusiona en `NOR-044`. Como en el caso anterior, no eran idénticas: `NOR-048` traía
su análisis de evaluación en Infantil —observación directa, promoción automática, informe de
etapa—, que se conserva como apartado 3 de `NOR-044`. Su propio título delataba que no era una
norma distinta: «Evaluación en Educación Infantil (**según** Orden de 31 de mayo de 2023)».

Además declaraba mal sus metadatos: `tipo_norma: resolucion-administrativa` y autoridad
«Dirección General de Ordenación», cuando la norma es una orden autonómica de la Consejería. Es
la misma clase de deriva que en `NOR-049`, que llegó a apuntar a una fuente inexistente.

- `NOR-044` recibe el apartado de Infantil, amplía `relacionada_con` y `desarrolla_a` con
  `NOR-047`, y su fichero y copia local pierden el «primaria» del nombre:
  `NOR-044-orden-evaluacion-31-mayo-2023`.
- `NOR-048` se retira con su copia local duplicada. Su identificador no se reutiliza (R10).
- `FTE-047` y `NOR-047`, que la citaban, se reapuntan a `NOR-044`.

## Prevención

El validador incorpora el tipo `DESDOBLAMIENTOS`, que avisa cuando dos fichas comparten fecha de
disposición y fuente, o cuando dos copias locales tienen contenido idéntico. Comprobado
recreando artificialmente un desdoblamiento: lo detecta por ambas vías.

Es aviso y no error: puede haber casos legítimos —una norma y su corrección de errores publicadas
el mismo día desde la misma fuente— que exigen mirar antes de fusionar.

## Coordinación con trabajo paralelo

IDs consumidos: `TAREA-083` y `DEC-0010`. `NOR-048` retirado y no reutilizable.
