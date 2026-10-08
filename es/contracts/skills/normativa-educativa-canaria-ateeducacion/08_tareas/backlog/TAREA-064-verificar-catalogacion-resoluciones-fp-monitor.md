---
id: TAREA-064
titulo: "Verificar la catalogación de las tres resoluciones de FP detectadas por el monitor en TAREA-061"
estado: "Hecha"
prioridad: "Media"
tipo: "catalogacion"
responsable: "@.agents/skills/catalogacion-fuentes"
fecha_creacion: 2026-08-05
fecha_actualizacion: 2026-08-05
fecha_cierre: 2026-08-05
relacionadas: [TAREA-061, TAREA-063, FTE-080, FTE-081, FTE-082, NOR-073, NOR-074, NOR-075]
siguiente_accion: null
---

# TAREA-064 — Verificar la catalogación de las tres resoluciones de FP del monitor

## Objetivo

`TAREA-061` dejó anotado como pendiente «completar la catalogación individual de las tres
resoluciones de FP detectadas originalmente por el monitor». Al cerrarla el 2026-08-05 no fue
posible confirmar si ese trabajo se completó por otra vía, así que se traslada aquí en lugar de
darlo por hecho.

## Contexto

- `TAREA-061` catalogó el Decreto 120/2026 (`FTE-075`, `NOR-068`, `REL-058`) y cerró el PR 29
  como duplicado del PR 28. Ese alcance sí está completo e indexado.
- `TAREA-062` catalogó la modificación de la FP semipresencial y virtual (`FTE-076`, `FTE-077`,
  `NOR-069`, `NOR-070`, `REL-059`, `REL-060`), que podría cubrir parte o la totalidad de esas
  tres resoluciones.
- El corpus tiene catalogadas resoluciones de FP de 2025 y 2026 en `NOR-061` a `NOR-070`.
- `11_calidad/monitor/portal-normativa-canaria.seen.json` solo guarda las URL ya vistas, sin
  distinguir cuáles se llegaron a catalogar, así que no sirve por sí solo para resolver la duda.

## Qué hacer

1. Localizar en el historial del PR 28 y en el diario `08_tareas/diario/2026-07-20-tarea-061-decreto-120-2026.md`
   qué tres resoluciones concretas detectó el monitor.
2. Comprobar para cada una si ya existe ficha `NOR` y entrada en `06_indices/normativa.yaml`.
3. Catalogar las que falten con la skill `catalogacion-fuentes` y `analisis-normativo`.
4. Si estaban todas catalogadas, cerrar esta tarea dejando constancia de la comprobación.

## Coordinación con trabajo paralelo

IDs consumidos: `TAREA-064`. No se reservan `FTE` ni `NOR` hasta saber cuántas fichas faltan
realmente.

## Cierre (2026-08-05)

### Cómo se identificaron las tres

El diario de `TAREA-061` no las nombraba y el snapshot del monitor sólo guarda URL con la fecha
en que se vieron, sin decir cuáles se catalogaron. Se resolvió cruzando ambas cosas: **de las 76
URL del snapshot, exactamente tres se registraron el 2026-07-20 —el día de `TAREA-061`— y no
dejan rastro en el corpus**. No hacía falta reconstruir el historial del PR.

Las tres son, verificadas una a una contra el sumario oficial del BOC:

| Ficha | Disposición | Publicación |
| --- | --- | --- |
| `NOR-073` | Resolución de 25-06-2026, cursos de acceso directo CAD2 y CAD3 | BOC 139, 13-07-2026, anuncio 2475 (41 páginas) |
| `NOR-074` | Resolución de 25-06-2026, horarios de Cocina y Restauración y de Prevención de Riesgos | BOC 141, 15-07-2026, anuncio 2507 (5 páginas) |
| `NOR-075` | Resolución de 02-07-2026, cuadros horarios de cinco dobles titulaciones de Grado D | BOC 141, 15-07-2026, anuncio 2508 (8 páginas) |

Ninguna estaba catalogada: `TAREA-062` cubrió otra resolución distinta, la de FP semipresencial
y virtual del BOC 144.

### Trabajo realizado

Catalogadas las tres con fuente (`FTE-080`, `FTE-081`, `FTE-082`), ficha normativa (`NOR-073`,
`NOR-074`, `NOR-075`) y copia local extraída del PDF firmado con `pdftotext -layout`. Todo
registrado en `06_indices/fuentes.yaml`, `06_indices/normativa.yaml` y
`06_indices/textos-oficiales.yaml`.

La más sustancial es `NOR-073`: regula por completo la vía de acceso a los ciclos formativos para
quien no cumple los requisitos académicos —CAD2 de 400 horas para grado medio, CAD3 de 600 para
grado superior—, con doce apéndices de documentación. El corpus no tenía nada de ese itinerario.

### Un falso hallazgo que conviene dejar anotado

Uno de los agentes informó de que el servidor del BOC le había servido, bajo el nombre de fichero
correcto, un PDF que correspondía a otra resolución. Comprobado descargando la misma URL tres
veces: el servidor devuelve siempre el documento correcto, con el mismo hash. Lo que ocurrió es
que los tres agentes trabajaban en paralelo y el encargo les sugería a todos la misma ruta
temporal, así que se pisaron el fichero entre ellos. **No hay un problema de integridad en el
BOC**, y no debe registrarse como tal.

### Deuda que queda a la vista

`NOR-074` y `NOR-075` modifican anexos de cuatro resoluciones que **no están catalogadas**: las
de 30 de octubre de 2024, 21 de febrero de 2025, 25 de abril de 2025, 26 de noviembre de 2025 y
27 de enero de 2026. Sin ellas el corpus no puede ofrecer el cuadro horario resultante ni trazar
la cadena de modificaciones, y por eso estas dos fichas no registran ninguna `REL`.

Además, el cruce del snapshot del monitor contra el corpus deja ver que **61 de sus 76 URL no
tienen rastro en el corpus**. La mayoría son páginas de índice del portal, pero hay entre ellas
PDF de resoluciones concretas. Conviene una revisión sistemática, que excede esta tarea.

## Coordinación con trabajo paralelo

IDs consumidos: `FTE-080`, `FTE-081`, `FTE-082`, `NOR-073`, `NOR-074`, `NOR-075`.
