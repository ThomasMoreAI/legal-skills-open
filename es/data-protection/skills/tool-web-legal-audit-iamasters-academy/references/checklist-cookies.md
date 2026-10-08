# Checklist Cookies y tecnologías similares (Guía AEPD actualizada)

La Guía AEPD sobre uso de cookies, vigente en su versión revisada, desarrolla el art. 22.2 LSSI. Desde 11-enero-2024 la AEPD sanciona de forma reiterada y sistemática los incumplimientos cubiertos aquí.

## COOKIES-001 — Banner visible en la primera capa

**Qué buscar**: al acceder a cualquier página, aparece un aviso informando del uso de cookies con:
- Información básica sobre finalidades
- Opción **Aceptar todas**
- Opción **Rechazar todas** (con mismo peso visual que Aceptar — tamaño, color, visibilidad)
- Opción **Configurar / Preferencias** que abra una segunda capa granular

Prohibido: botón "Rechazar" escondido tras menú, color tenue, tamaño menor, o que requiera scroll.

**Cómo verificarlo**: carga la página en modo incógnito y observa. Usa `find` con query "cookie banner". Haz screenshot.

**Severidad**: GRAVE si el banner falta o no tiene "Rechazar" en primera capa con paridad visual.

## COOKIES-002 — Bloqueo previo de cookies no necesarias

**Qué buscar**: hasta que el usuario consienta, **no debe dispararse ninguna cookie** ni llamada a terceros no estrictamente necesaria (analítica, publicidad, redes sociales). El script del banner debe cargar **antes** que cualquier otro tracker.

**Cómo verificarlo**: intercepta la red en la primera carga. Si aparecen peticiones a facebook.com/tr, analytics.tiktok.com, google-analytics.com, hotjar.com, clarity.ms, etc. SIN que el usuario haya interactuado con el banner, es infracción directa.

**Severidad**: CRÍTICA. Es uno de los incumplimientos más sancionados por la AEPD en 2024-2025.

## COOKIES-003 — Granularidad en la segunda capa (panel de preferencias)

**Qué buscar**: el panel de preferencias debe permitir aceptar/rechazar por **categoría** al menos:
- Técnicas / estrictamente necesarias (no desactivables)
- De preferencias / personalización
- De análisis / medición
- De publicidad comportamental
- De terceros identificados por nombre

Permitir decisión granular es requisito. Un banner binario "Aceptar todo / Rechazar todo" sin granularidad para categorías de publicidad/análisis se considera insuficiente.

**Severidad**: GRAVE.

## COOKIES-004 — Inventario público en la Política de Cookies

**Qué buscar**: la Política de Cookies debe listar cada cookie utilizada con:
- Nombre
- Titular (propia o de tercero; identificar proveedor)
- Finalidad
- Duración
- Tipo (técnica, preferencias, análisis, publicidad)

Una política que dice "usamos cookies de análisis y publicidad" sin más detalle es insuficiente.

**Severidad**: MEDIA a GRAVE.

## COOKIES-005 — Consent Mode v2 (si usa Google Ads/GA4)

**Qué buscar**: desde 6-marzo-2024 Google exige Consent Mode v2 para anunciantes EEE. La web debe enviar a Google los 4 parámetros:
- `ad_user_data`
- `ad_personalization`
- `ad_storage`
- `analytics_storage`

Con Consent Mode v2 correctamente configurado, si el usuario rechaza, Google recibe pings agregados sin PII.

**Cómo verificarlo**: intercepta red tras rechazar cookies y busca llamadas a Google con `gcs=G100` (denegado) o `gcs=G111` (otorgado).

**Severidad**: MEDIA (Google puede suspender cuenta publicitaria además).

## COOKIES-006 — Persistencia del rechazo

**Qué buscar**: si el usuario rechaza cookies, al recargar la página **no debe volver a aparecer el banner inmediatamente** (persistencia mínima aceptable: 6 meses según Guía AEPD). Tampoco debe volver a dispararse los trackers.

**Cómo verificarlo**: rechaza → recarga → observa red.

**Severidad**: MEDIA.

## COOKIES-007 — Fácilmente revocable

**Qué buscar**: el usuario debe poder cambiar su preferencia en cualquier momento. Enlace o widget accesible desde footer ("Configurar cookies", "Preferencias de cookies"). No basta con decir "puedes hacerlo desde tu navegador".

**Severidad**: MEDIA.

## COOKIES-008 — No dark patterns

**Qué buscar**:
- Pre-marcado de casillas: prohibido
- "Seguir navegando equivale a aceptar": inválido desde 2020
- Muros de cookies puros (cookie walls) que fuerzan el consentimiento: la AEPD y el Comité Europeo han declarado que no configuran consentimiento libre
- Diseños oscuros (botón Rechazar en gris claro sobre fondo blanco)
- Botón Rechazar que requiere más clicks que Aceptar

**Severidad**: GRAVE — la AEPD actualizó su Guía específicamente para perseguirlos.

## COOKIES-009 — Cookie walls y "aceptar o pagar"

**Qué buscar**: si la web ofrece elección "aceptar tracking gratis" vs "pagar X€/mes sin tracking", aplica el criterio EDPB de 17-abril-2024: debe ser una alternativa **real y proporcional**. Un precio prohibitivo (>5-10€/mes típicamente) hace que el consentimiento no sea libre.

**Severidad**: GRAVE. Discutible jurídicamente, requiere análisis del caso concreto.

## COOKIES-010 — Transparencia sobre perfilado

**Qué buscar**: si se perfila al usuario para publicidad comportamental, la política debe indicar:
- Lógica básica del perfilado
- Si los perfiles se cruzan con terceros (data brokers)
- Derecho a oponerse

**Norma**: Arts. 13.2.f, 21.2, 22 RGPD.

**Severidad**: MEDIA.
