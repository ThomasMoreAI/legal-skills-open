---
id: TAREA-078
titulo: "Catalogar la Resolución Conjunta n.º 24/2024 de instrucciones para el primer ciclo de Educación Infantil"
estado: "Hecha"
prioridad: "Media"
tipo: "catalogacion"
responsable: "@.agents/skills/catalogacion-fuentes"
fecha_creacion: 2026-08-05
fecha_actualizacion: 2026-08-05
fecha_cierre: 2026-08-05
relacionadas: [PREG-009, FTE-049, FTE-051, NOR-046]
siguiente_accion: "Crear la ficha FTE de la Resolución 24/2024 desde su PDF oficial y decidir si procede ficha NOR."
---

# TAREA-078 — Catalogar la Resolución Conjunta n.º 24/2024

## Contexto

Al resolver `PREG-009` se comprobó que `FTE-051` describía una resolución inexistente. Pero en
esa investigación apareció una norma **real y vigente que el corpus no recoge**: la Resolución
Conjunta n.º 24/2024, de 16 de julio, de instrucciones de organización y funcionamiento para los
centros autorizados a implantar el **primer ciclo de Educación Infantil**.

Es la norma a la que remite expresamente la Resolución 73/2025 (`FTE-049`) en su Anexo II punto
2: los centros autorizados «deberán atender a las instrucciones específicas que se dicten al
efecto».

## Evidencia ya recogida

- PDF oficial verificado:
  `https://www.gobiernodecanarias.org/cmsgob1/export/sites/educacion/web/_galerias/descargas/normativa-internas/Instrucciones_organizacion_funcionamiento_primer_ciclo_infantil.pdf`
- Sello de registro electrónico: «RESOLUCION - Nº: 24 / 2024 - Tomo: 1 - Libro: 2739 - Fecha:
  16/07/2024».
- Órgano: Dirección General de Administración de Centros, Escolarización y Servicios
  Complementarios, y Dirección General de Ordenación de las Enseñanzas, Inclusión e Innovación.
  **No** la Viceconsejería, a diferencia de la 73/2025.
- Comprobado en la página de normativa clasificada de Infantil de la Inspección: es la más
  reciente de la etapa, sin sustituta de 2025 ni de 2026.

## Qué hacer

1. Crear la ficha `FTE-NNN` con el siguiente ID libre, conforme a `AGENTS.md` §7.
2. Decidir si procede además una ficha `NOR`: es una resolución de instrucciones, del mismo tipo
   que `NOR-046` y `NOR-049`, así que probablemente sí.
3. Registrar la relación con `NOR-007` o con la norma que ampare el primer ciclo, y con
   `FTE-049`, que remite a ella.
4. Valorar una copia local del texto conforme a §10 bis y R16.
5. Actualizar `06_indices/fuentes.yaml` y, si procede, `normativa.yaml` y `relaciones.yaml`.

## Coordinación con trabajo paralelo

IDs consumidos: `TAREA-078`. Consumirá además un `FTE` y posiblemente un `NOR` y un `REL` al
ejecutarse; recalcular los libres en ese momento.

## Resultado (2026-08-05)

Catalogada como `FTE-078` y `NOR-071`, con copia local del texto y cabecera R16 completa.

La resolución consta de 23 instrucciones y tres anexos —Plan de Acogida, guion de entrevista
individual y autorización de alimentación—, dirigidos a los centros autorizados a implantar el
primer ciclo con carácter de experiencia piloto.

`fecha_entrada_vigor` queda en `null` (R15): no hay disposición final expresa, aunque varias
instrucciones citan el curso 2024-2025.
