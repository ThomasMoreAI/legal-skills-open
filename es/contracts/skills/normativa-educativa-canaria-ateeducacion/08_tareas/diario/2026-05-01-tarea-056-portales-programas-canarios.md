# Diario — 2026-05-01: cierre TAREA-056 portales de programas y marcos operativos canarios

## Trabajo realizado

- Creadas 11 nuevas fichas de fuente oficial en `01_fuentes/portales-oficiales/` para programas y marcos operativos del sistema educativo canario:
  - `FTE-057` — Programa PROA+ (Cooperación Territorial 2024-2028).
  - `FTE-058` — Red Canaria-InnovAS y PIDAS.
  - `FTE-059` — Proyecto Viera (fomento de la lectura y comunicación lingüística).
  - `FTE-060` — ProIDEAC (marco pedagógico de programación y evaluación competencial).
  - `FTE-061` — Programa AICLE (Aprendizaje Integrado de Contenidos y Lenguas Extranjeras).
  - `FTE-062` — Programa EnSeñas (patrimonio canario, eje de InnovAS).
  - `FTE-063` — Matemáticas Newton Canarias.
  - `FTE-064` — EVAGD y Aula Digital Canaria.
  - `FTE-065` — OPEEC, Erasmus+ y eTwinning.
  - `FTE-066` — Protección de Datos en Educación (sub-portal Inspección Educativa).
  - `FTE-067` — Prevención de Riesgos Laborales y Emergencias en Centros Públicos.
- Registradas las 11 entradas en `06_indices/fuentes.yaml`.
- Añadida nueva sección «Programas y marcos operativos canarios habituales» a `skills/experto-normativa-educativa-canaria/SKILL.md` y al bloque copiable equivalente en `docs/skill.html`. La sección lista los programas como **no-normas**, recuerda al asistente que no debe inventar articulado y le indica que remita al portal oficial correspondiente.

## Fuente oficial

Las URL incorporadas son páginas institucionales del Gobierno de Canarias (Consejería de Educación, Formación Profesional, Actividad Física y Deportes; Inspección General de Educación; OPEEC). Se ha unificado el tipo de fuente como `portal-oficial`. Fecha de consulta: 2026-05-01.

## Justificación

El asistente especializado se beneficia de reconocer explícitamente las siglas y marcos operativos que un usuario real (docente, equipo directivo, asesoría CEP, inspección) menciona en sus consultas. Sin esa referencia, el modelo tiende a confundir programas con normas y a inventar articulado inexistente. La sección añadida acota el comportamiento del asistente para estos casos.

## Incidencias y límites

- No se han creado fichas NOR para los programas: no son normas con articulado propio.
- No se han catalogado todavía las convocatorias y resoluciones derivadas; quedan pendientes para tareas posteriores.
- Algunas relaciones cruzadas se han marcado como `[PENDIENTE]` cuando dependen de catalogaciones futuras.

## IDs consumidos

- `FTE-057`, `FTE-058`, `FTE-059`, `FTE-060`, `FTE-061`, `FTE-062`, `FTE-063`, `FTE-064`, `FTE-065`, `FTE-066`, `FTE-067`.
- `TAREA-056`.

## Coordinación con trabajo paralelo

- `git fetch origin main` antes de iniciar para confirmar IDs libres.
- Solo se ha tocado `06_indices/fuentes.yaml` (sección final), `skills/experto-normativa-educativa-canaria/SKILL.md`, `docs/skill.html` (bloque copiable, manteniendo el resto del fichero intacto), y se han creado los archivos nuevos listados arriba. No se han modificado fichas ajenas.
