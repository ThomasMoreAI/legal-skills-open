# Cómo contribuir

¡Gracias por contribuir a `compliance-uy`! El objetivo es que cualquier empresa uruguaya pueda
dar un primer paso fundado hacia el cumplimiento de la Ley 18.331.

## Regla de oro: trazabilidad normativa

1. **Toda afirmación normativa cita fuente, artículo y archivo en `/sources`:**
   `(Ley 18.331, art. 9 — sources/ley-18331.md)`.
2. **Solo fuentes oficiales uruguayas** (IMPO, Parlamento, gub.uy/URCDP, normas y resoluciones).
   No copiar texto legal de Chile, España, la UE u otras jurisdicciones.
3. **Lo no verificable se marca** con `[verificar contra fuente oficial]`.
4. Si agregás o cambiás una cita, actualizá el archivo correspondiente en `/sources` (citación
   canónica + URL oficial + fecha de consulta).

## Tipos de contribución

- **Controles** (`references/controls.md`): nuevos controles o mejoras de heurísticas.
- **Pack** (`packs/ley-18331/`): precisión normativa, plazos, definiciones.
- **Plantillas** (`templates/`): documentos más claros o completos.
- **Detección** (en `SKILL.md`): nuevas categorías de datos o proveedores.
- **Fuentes** (`/sources`): mantener enlaces y números de artículo verificados.

## Flujo

1. Hacé un fork y una rama (`feat/...`, `fix/...`, `docs/...`).
2. Mantené el disclaimer en todos los documentos generados/plantillas.
3. Abrí un PR describiendo el cambio y citando las fuentes.
4. Para discrepancias de numeración de artículos, documentá la fuente de cada número.

## Estilo

- Español rioplatense, claro y conciso.
- Markdown simple. Tablas para catálogos.
- No introducir dependencias innecesarias.
