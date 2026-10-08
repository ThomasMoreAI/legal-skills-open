---
id: TAREA-070
titulo: "Localizar la ubicación actual de las fuentes cuya URL oficial devuelve 404"
estado: "Hecha"
prioridad: "Media"
tipo: "catalogacion"
responsable: "@.agents/skills/catalogacion-fuentes"
fecha_creacion: 2026-08-05
fecha_actualizacion: 2026-08-05
fecha_cierre: 2026-08-05
relacionadas: [FTE-045, FTE-048, FTE-049, FTE-051, TAREA-065]
siguiente_accion: "Localizar la Resolución de 20 de junio de 2025 de IOF de Escuelas Infantiles que declara FTE-051."
---

# TAREA-070 — Fuentes con URL oficial rota

## Objetivo

`TAREA-065` comprobó las URL de las fuentes sin `nivel_evidencia` y encontró cuatro que
devolvían 404. Localizar su ubicación actual en el portal oficial y restaurar la trazabilidad.

## Resueltas

**`FTE-045` — Resolución de 24 de febrero de 2026, permisos y licencias del personal docente.**
El BOC dejó de usar la numeración por boletín (`001.html`) y pasó a numeración anual. Localizada
en el índice del BOC 2026/046 y verificada por contenido:
`https://www.gobiernodecanarias.org/boc/2026/046/751.html`

**`FTE-048` — Resolución de 15 de mayo de 2025, rúbricas de los criterios de evaluación de
Primaria.** Mismo cambio de numeración. Verificada por contenido:
`https://www.gobiernodecanarias.org/boc/2025/107/2005.html`

**`FTE-049` — Resolución conjunta 73/2025, instrucciones de organización y funcionamiento
2025-2026.** La ruta del portal desapareció. El documento sigue publicado como PDF y su primera
página confirma el título:
`https://www.gobiernodecanarias.org/cmsgob1/export/sites/educacion/web/_galerias/descargas/normativa-internas/r_73-2025-instrucciones_or_func_2025-2026.pdf`

Las tres pasan a `estado_fuente: Activa` y `nivel_evidencia: confirmado-fuente-primaria`, con
fecha de consulta 2026-08-05.

## Pendiente

**`FTE-051` — «Resolución de 20 de junio de 2025, IOF Escuelas Infantiles».** No localizada. La
página de normativa clasificada de la Inspección ofrece hoy la Resolución Conjunta n.º 24/2024,
de 16 de julio, sobre el Primer Ciclo de Educación Infantil, que es **un documento distinto**;
no se dan por equivalentes.

`url_oficial` apunta provisionalmente a esa página, que sí resuelve y lista los documentos de
organización y funcionamiento, y la fuente queda en `Pendiente de verificación`.

Qué comprobar:

1. Si la resolución de 20 de junio de 2025 para Escuelas Infantiles existe y con qué numeración.
2. Si fue sustituida por la 24/2024 o por una posterior, en cuyo caso corresponde marcar la
   fuente como `Superada` y catalogar la vigente.
3. Si el título de `FTE-051` era impreciso desde el origen, corregirlo con la evidencia hallada.

## Coordinación con trabajo paralelo

IDs consumidos: `TAREA-070`. Solo se modifican fichas `FTE` existentes.

## Resultado (2026-08-05)

`FTE-051` no se ha podido localizar porque **el documento que declara no existe como norma
diferenciada**. La única resolución de 20 de junio de 2025 es la Resolución conjunta n.º 73/2025,
ya catalogada como `FTE-049`, verificada por su sello de registro electrónico.

La ficha no se ha modificado: cualquiera de las salidas posibles cambia la identidad de la
fuente y afecta a `FTE-049`, `NOR-046` y `NOR-049`. Queda como `PREG-009` para decisión
editorial.

Las otras tres fuentes de esta tarea quedaron resueltas y verificadas el mismo día.
