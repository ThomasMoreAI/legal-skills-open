# Checklist Seguridad HTTP

La seguridad técnica no es estrictamente "cumplimiento legal", pero medidas técnicas inadecuadas (art. 32 RGPD) contribuyen al riesgo sancionador en caso de brecha.

## Cómo verificar rápido

```bash
curl -sI https://<dominio> | tr -d '\r'
# o
curl -s "https://securityheaders.com/?q=<dominio>&followRedirects=on&hide=on"
```

También: https://hstspreload.org, https://www.ssllabs.com/ssltest/

## SEC-001 — HTTPS obligatorio

**Qué buscar**: `https://` con certificado válido. Probar también `http://` → debe redirigir 301/302 a https.

**Severidad**: CRÍTICA si pide datos por HTTP.

## SEC-002 — HSTS (Strict-Transport-Security)

**Header**: `Strict-Transport-Security: max-age=31536000; includeSubDomains; preload`

Obliga al navegador a usar solo HTTPS aunque el usuario escriba http://.

**Severidad**: MEDIA si ausente.

## SEC-003 — Content-Security-Policy

**Header**: `Content-Security-Policy: default-src 'self'; script-src 'self' https://...`

Protege contra XSS. Debería al menos tener directivas básicas. Una CSP ausente en 2026 es una bandera roja.

**Severidad**: MEDIA.

## SEC-004 — X-Frame-Options / frame-ancestors

**Header**: `X-Frame-Options: DENY` o `SAMEORIGIN`, o en CSP `frame-ancestors 'none'`.

Protege contra clickjacking.

**Severidad**: MEDIA.

## SEC-005 — X-Content-Type-Options

**Header**: `X-Content-Type-Options: nosniff`

Evita MIME sniffing.

**Severidad**: BAJA.

## SEC-006 — Referrer-Policy

**Header**: `Referrer-Policy: strict-origin-when-cross-origin`

Evita filtrar URLs con datos sensibles en el Referer.

**Severidad**: BAJA.

## SEC-007 — Permissions-Policy

**Header**: `Permissions-Policy: geolocation=(), microphone=(), camera=()`

Desactiva APIs no usadas.

**Severidad**: BAJA.

## SEC-008 — Cookies seguras

Cookies de sesión / autenticación deben tener: `Secure; HttpOnly; SameSite=Lax` (o `Strict`).

Cookies de análisis/marketing con datos personales: similares requisitos salvo que HttpOnly no aplica si las lee JS.

**Severidad**: MEDIA a ALTA.

## SEC-009 — Tecnologías obsoletas

Comprobar si el servidor expone versión (Server: Apache/2.2.x) y versiones vulnerables (jQuery <3, WordPress <6.4, etc.).

**Severidad**: depende del CVE.

## SEC-010 — Subresource Integrity

Scripts externos cargados deberían tener `integrity="sha384-..."` para verificar no han sido modificados.

**Severidad**: BAJA.
