---
id: TAREA-056
titulo: "Catalogar portales oficiales de programas y marcos operativos canarios (FTE-057 a FTE-067)"
estado: "Hecha"
prioridad: "Media"
tipo: "catalogacion"
responsable: "@.agents/skills/catalogacion-fuentes"
fecha_creacion: 2026-05-01
fecha_actualizacion: 2026-05-01
relacionadas: [FTE-057, FTE-058, FTE-059, FTE-060, FTE-061, FTE-062, FTE-063, FTE-064, FTE-065, FTE-066, FTE-067]
---

# TAREA-056 — Catalogar portales oficiales de programas y marcos operativos canarios

## Objetivo

Incorporar al corpus las fuentes oficiales correspondientes a los principales programas y marcos operativos del sistema educativo canario que un usuario habitual menciona en consultas (PROA+, InnovAS, Viera, ProIDEAC, AICLE, EnSeñas, Newton, EVAGD, OPEEC, protección de datos, prevención de riesgos), de modo que el asistente reconozca estas siglas y pueda remitir al portal oficial correspondiente sin inventar articulado.

## Trabajo realizado

- Creadas 11 nuevas fichas FTE-057 a FTE-067 en `01_fuentes/portales-oficiales/`.
- Registradas las 11 entradas en `06_indices/fuentes.yaml`.
- Añadida sección «Programas y marcos operativos canarios habituales» a `skills/experto-normativa-educativa-canaria/SKILL.md` y al bloque copiable de `docs/skill.html` (manteniendo ambos sincronizados).

## Criterios de cierre

- Las 11 fichas tienen frontmatter válido y pasan `yaml.safe_load`.
- Cada ficha indica la diferencia entre programa/marco y norma con articulado.
- El skill canónico reconoce las siglas comunes y remite al portal oficial sin inventar artículos.

## Notas

- Fecha de catalogación: 2026-05-01.
- Tipo de fuente unificado: `portal-oficial`.
- Las URL son institucionales del Gobierno de Canarias; no se incorpora normativa derivada todavía (las convocatorias y resoluciones específicas se catalogarán cuando proceda).
