# Catálogo de controles — `compliance-uy`

Este catálogo define los controles que la skill evalúa. **No es asesoramiento legal**
(ver disclaimer en `SKILL.md`). Cada control cita su base normativa como
`(Norma, art. — sources/archivo.md)`. Lo no verificable se marca `[verificar contra fuente oficial]`.

## Modelo de cada control

- **id**: identificador estable (se usa en `state.json`).
- **nombre**: control evaluado.
- **base_legal**: norma, artículo y archivo en `/sources`.
- **objetivo**: qué busca asegurar.
- **señales_en_codigo**: patrones que la skill busca con Grep/Glob (indicios, no prueba).
- **estados**: `cumple` | `parcial` | `no_cumple` | `no_aplica` | `requiere_revision`.
- **evidencia**: cómo se documenta (`archivo:línea` + descripción).
- **riesgo**: `alto` | `medio` | `bajo` (impacto + probabilidad, criterio del operador).
- **remediacion**: pasos sugeridos (borrador técnico, no dictamen).

> Las "señales en código" son **heurísticas**. Detectar un patrón no prueba cumplimiento ni
> incumplimiento: orienta dónde mirar. Toda conclusión queda en estado `requiere_revision`
> hasta validación humana.

---

## C-01 · Responsable / Encargado del tratamiento

- **base_legal:** Ley 18.331, art. 4 (definiciones) y art. 29 (servicios por cuenta de terceros) — `sources/ley-18331.md`; Decreto 414/009 (encargado vs. cesión) — `sources/decreto-414-009.md`. `[verificar numeración art. 29/30]`
- **objetivo:** Determinar quién es responsable de la base/tratamiento y qué terceros actúan como encargados.
- **señales_en_codigo:** SDKs de terceros, variables de entorno de proveedores, archivos de configuración de servicios externos, contratos/links en `legal/`, `docs/`.
- **evidencia:** lista de proveedores detectados con `archivo:línea`.
- **riesgo por defecto:** medio.
- **remediacion:** definir rol (responsable/encargado) por cada tratamiento; documentar en `inventario-datos.md` y `matriz-proveedores-transferencias.md`.

## C-02 · Base de legitimación / Consentimiento

- **base_legal:** Ley 18.331, art. 9 (previo consentimiento informado y excepciones); art. 18 (datos sensibles: consentimiento expreso y escrito) — `sources/ley-18331.md`.
- **objetivo:** Verificar que cada tratamiento tenga base legítima (consentimiento u otra excepción del art. 9).
- **señales_en_codigo:** checkboxes de consentimiento en formularios, flags `consent`/`tos_accepted`, banners de cookies, campos `accepted_at`, tablas `consents`.
- **estados:** `no_cumple` si se recolectan datos personales sin rastro de base legítima.
- **riesgo por defecto:** alto (datos sensibles) / medio (datos comunes).
- **remediacion:** registrar la base legal por tratamiento en `matriz-tratamientos.md`; para datos sensibles, asegurar consentimiento expreso y escrito (art. 18).

## C-03 · Deber de información / Transparencia

- **base_legal:** Ley 18.331, art. 13 (qué informar al recabar datos) — `sources/ley-18331.md`. `[verificar numeración: algunas ediciones art. 12]`
- **objetivo:** Confirmar que existe y es completa la información al titular (finalidad, responsable, derechos, transferencias internacionales, etc.).
- **señales_en_codigo:** archivos `privacy`, `politica-privacidad`, `terms`, rutas `/privacy`, textos legales en el front.
- **riesgo por defecto:** medio.
- **remediacion:** completar `politica-privacidad.md` con los extremos del art. 13.

## C-04 · Finalidad

- **base_legal:** Ley 18.331, art. 5 (principios) y art. 8 (finalidad) — `sources/ley-18331.md`. `[verificar numeración art. 8]`
- **objetivo:** Que los datos se usen solo para fines determinados y compatibles con el declarado.
- **señales_en_codigo:** usos cruzados de datos (p. ej. emails de registro usados para marketing sin base), pipelines de analítica, exportaciones a CRM.
- **riesgo por defecto:** medio.
- **remediacion:** declarar finalidad por tratamiento en `matriz-tratamientos.md`; separar finalidades incompatibles.

## C-05 · Minimización / Proporcionalidad

- **base_legal:** Ley 18.331, art. 7 (datos adecuados y no excesivos) — `sources/ley-18331.md`; Decreto 64/020, arts. 7-9 (privacidad por defecto) — `sources/decreto-64-020.md`.
- **objetivo:** Recolectar solo los datos necesarios para el fin.
- **señales_en_codigo:** esquemas de base de datos/modelos con campos sensibles o de más (p. ej. `cedula`, `fecha_nacimiento`, `direccion` no usados); logs que guardan payloads completos.
- **riesgo por defecto:** medio.
- **remediacion:** revisar esquema; eliminar campos no usados; aplicar privacidad por defecto.

## C-06 · Seguridad de los datos

- **base_legal:** Ley 18.331, art. 12 (redacción dada por art. 39 de la Ley 19.670) — `sources/ley-18331.md`, `sources/ley-19670-arts-37-40.md`; Decreto 64/020, arts. 5, 7 (medidas y estándares; Marco de Ciberseguridad de AGESIC) — `sources/decreto-64-020.md`.
- **objetivo:** Medidas técnicas y organizativas para integridad, confidencialidad y disponibilidad.
- **señales_en_codigo:** secretos hardcodeados, ausencia de cifrado en tránsito/reposo, dependencias desactualizadas, falta de control de acceso, `http://` en endpoints, contraseñas sin hash.
- **riesgo por defecto:** alto.
- **remediacion:** corregir hallazgos; documentar medidas (responsabilidad proactiva, Decreto 64/020 art. 5).

## C-07 · Derechos de los titulares

- **base_legal:** Ley 18.331, arts. 14 (acceso), 15 (rectificación/actualización/inclusión/supresión), 16 (comunicación) — `sources/ley-18331.md`. `[verificar numeración del bloque de derechos]`
- **objetivo:** Que existan vías efectivas para ejercer acceso, rectificación, supresión, etc., en los plazos legales (5 días hábiles).
- **señales_en_codigo:** endpoints `/account/delete`, `export-data`, formularios de contacto de privacidad, flujos "descargar mis datos".
- **riesgo por defecto:** medio.
- **remediacion:** implementar/documentar el procedimiento en `procedimiento-derechos-titulares.md`.

## C-08 · Retención / Conservación

- **base_legal:** Ley 18.331, art. 7 (no conservar más allá de lo necesario) — `sources/ley-18331.md`; Decreto 64/020, art. 7 (plazo de conservación por defecto) — `sources/decreto-64-020.md`.
- **objetivo:** Definir y aplicar plazos de retención y borrado.
- **señales_en_codigo:** jobs de borrado/TTL, columnas `deleted_at`, políticas de logs, retención en data warehouse.
- **riesgo por defecto:** medio.
- **remediacion:** definir plazos por categoría en `matriz-tratamientos.md`; automatizar borrado.

## C-09 · Contratos con encargados

- **base_legal:** Ley 18.331, art. 29 (servicios por cuenta de terceros) — `sources/ley-18331.md`; obligación de documentar por contrato el tratamiento por terceros (reforma Ley 19.670) — `sources/ley-19670-arts-37-40.md`. `[verificar numeración art. 29/30]`
- **objetivo:** Que cada proveedor que trata datos por cuenta de la empresa tenga contrato de encargo.
- **señales_en_codigo:** proveedores detectados (C-01) sin DPA/contrato en `legal/`.
- **riesgo por defecto:** medio.
- **remediacion:** firmar contrato de encargado (`contrato-encargado.md`) con cada proveedor.

## C-10 · Transferencias internacionales

- **base_legal:** Ley 18.331, art. 23 — `sources/ley-18331.md`; Decreto 414/009 (procedimiento de autorización) — `sources/decreto-414-009.md`; Resoluciones URCDP 63/2023 y 70/2023 — `sources/urcdp-guias.md`. `[verificar resoluciones]`
- **objetivo:** Identificar transferencias fuera de Uruguay y su base legal (nivel adecuado, excepción del art. 23, o autorización URCDP).
- **señales_en_codigo:** regiones de proveedores cloud (`us-east-1`, `europe-west`), dominios `.com` de SaaS extranjeros, CDNs, sub-encargados.
- **riesgo por defecto:** alto.
- **remediacion:** mapear cada transferencia en `matriz-proveedores-transferencias.md`; determinar base legal; informar al titular (Res. URCDP).

## C-11 · Incidentes / Vulneraciones de seguridad

- **base_legal:** Ley 19.670, art. 38 — `sources/ley-19670-arts-37-40.md`; Decreto 64/020, arts. 3-4 (24h minimizar, 72h notificar URCDP, comunicar a titulares, informe final) — `sources/decreto-64-020.md`; Guía URCDP de vulneraciones — `sources/urcdp-guias.md`.
- **objetivo:** Que exista plan de respuesta y registro de incidentes con los plazos legales.
- **señales_en_codigo:** runbooks de incidentes, alertas/monitoring (Sentry, Datadog), `SECURITY.md`, canal de reporte.
- **riesgo por defecto:** alto.
- **remediacion:** completar `plan-respuesta-incidentes.md` y `registro-incidentes.md`.

## C-12 · Datos sensibles

- **base_legal:** Ley 18.331, art. 4 (definición), art. 18 (régimen) y art. 19 (salud) — `sources/ley-18331.md`; Decreto 64/020, art. 6 (EIPD obligatoria) — `sources/decreto-64-020.md`.
- **objetivo:** Detectar tratamiento de datos sensibles (salud, vida sexual, origen racial/étnico, opiniones políticas, convicciones religiosas/morales, afiliación sindical), datos biométricos y de menores, y exigir consentimiento expreso y escrito + EIPD.
- **señales_en_codigo:** campos `salud`, `diagnostico`, `religion`, `etnia`, `sindicato`, `orientacion`, `biometric`, `huella`, `face`, datos de `menor`/`edad`.
- **riesgo por defecto:** alto.
- **remediacion:** consentimiento expreso y escrito (art. 18); EIPD (Decreto 64/020 art. 6); evaluar designación de DPO (Ley 19.670 art. 40).

## C-13 · Delegado de Protección de Datos (DPO) · *condicional*

- **base_legal:** Ley 19.670, art. 40 — `sources/ley-19670-arts-37-40.md`; Decreto 64/020, arts. 10-15 (comunicación a URCDP en 90 días) — `sources/decreto-64-020.md`.
- **objetivo:** Determinar si la empresa está obligada a designar DPO (datos sensibles como negocio principal o grandes volúmenes) y si lo hizo.
- **señales_en_codigo:** menciones a "DPO"/"delegado de protección de datos", volumen de titulares (estimado por esquema), tratamiento sensible como core.
- **riesgo por defecto:** medio.
- **remediacion:** si aplica, designar DPO y comunicar a la URCDP en 90 días.

## C-14 · Registro de bases ante la URCDP · *condicional*

- **base_legal:** Ley 18.331, art. 6 (principio de legalidad / inscripción) — `sources/ley-18331.md`; Decreto 414/009 (inscripción) — `sources/decreto-414-009.md`.
- **objetivo:** Recordar la obligación de inscribir las bases de datos en el Registro de la URCDP.
- **estado:** normalmente `requiere_revision` (es un trámite administrativo externo al código).
- **remediacion:** inscribir las bases en el Registro de Bases de Datos Personales de la URCDP.

---

## Mapa control → documento generado

| Control | Documento(s) en `.compliance/docs/` |
|---|---|
| C-01, C-12 | `inventario-datos.md` |
| C-02, C-04, C-05, C-08 | `matriz-tratamientos.md` |
| C-03 | `politica-privacidad.md` |
| C-09 | `contrato-encargado.md` |
| C-10 | `matriz-proveedores-transferencias.md` |
| C-07 | `procedimiento-derechos-titulares.md` |
| C-11 | `plan-respuesta-incidentes.md`, `registro-incidentes.md` |
| C-12, C-06 | `evaluacion-riesgo-privacidad.md` |
| Todos | `resumen-cumplimiento.md`, `state.json` |
