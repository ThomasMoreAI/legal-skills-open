# Workflow operativo detallado

Carga este archivo al arrancar una auditoría. Te guía paso a paso con los comandos concretos a ejecutar.

## Herramientas disponibles por orden de preferencia

| Herramienta | Cuándo | Ventaja |
|---|---|---|
| `mcp__Claude_in_Chrome__*` | Por defecto, si el usuario tiene Chrome MCP | Navegador real, intercepta red real, ejecuta JS, permite clicks |
| `mcp__firecrawl__firecrawl_scrape` | Si no hay Chrome MCP | Ignora JS protections, stealth mode, bueno para scrape masivo |
| `WebFetch` | Fallback | Sin JS; solo HTML estático |
| `curl` (vía Bash) | Para headers HTTP | Rápido, no abre navegador |

## Fase 2 — Descubrimiento y scrape

### 2.1 Abrir URL en navegador real

```
mcp__Claude_in_Chrome__tabs_context_mcp(createIfEmpty=true)
mcp__Claude_in_Chrome__navigate(url="<URL>", tabId=<tab>)
```

### 2.2 Capturar estado de red INMEDIATAMENTE (antes de cualquier interacción)

Esto es clave. Los trackers publicitarios se disparan en la primera carga sin consentimiento. Si esperas o interactúas, contaminas la evidencia.

```
mcp__Claude_in_Chrome__read_network_requests(tabId=<tab>, limit=300)
```

Guarda el resultado tal cual en `network-trace.json`. Esa es tu evidencia.

### 2.3 Extraer texto completo y enlaces del footer

```
mcp__Claude_in_Chrome__get_page_text(tabId=<tab>)
mcp__Claude_in_Chrome__find(query="footer links to privacy policy, legal notice, terms, cookies", tabId=<tab>)
```

Para cada enlace legal encontrado, anota el `href` y luego navega a esa URL (en otra pestaña o la misma) para auditar el contenido.

### 2.4 Detectar formularios y sus campos

```
mcp__Claude_in_Chrome__find(query="all form inputs, checkboxes, consent text, submit buttons", tabId=<tab>)
```

Apunta: `type`, `name`, `placeholder`, label asociado, y si hay checkbox de consentimiento.

### 2.5 Screenshot de la carga inicial

```
mcp__Claude_in_Chrome__preview_screenshot (si disponible)
# o
mcp__firecrawl__firecrawl_scrape(formats=["screenshot"], screenshotOptions={fullPage:true})
```

Guarda en `screenshots/homepage.png`. Si detectas algún hallazgo visual (ej. ausencia de banner de cookies), esta captura es la evidencia.

### 2.6 Detectar stack tecnológico

Pistas en el HTML:
- `wp-content/` → WordPress
- `elementor` en clases → Elementor
- `leadconnectorhq` en assets → GoHighLevel / LeadConnector
- `stcdn.leadconnectorhq` / `filesafe.space` → HighLevel funnels
- `__NEXT_DATA__` → Next.js
- `window.wixEmbedsAPI` → Wix
- `cdn.shopify.com` → Shopify
- `GTM-XXXXXXX` iframe → Google Tag Manager
- `elementorFrontendConfig` → Elementor Pro

El stack condiciona qué trackers y comportamiento esperar. Un GoHighLevel por defecto no instala banner de cookies; un WordPress suele tener plugins que sí.

## Fase 3 — Trackers

Ver `trackers-database.md`.

## Fase 4 — Cargar checklists uno por uno

No cargues los 7 checklists a la vez. Carga el que toca, ejecuta los checks, apunta resultados, pasa al siguiente.

Orden sugerido (de mayor a menor gravedad):

1. `checklist-cookies.md` — si hay trackers sin banner, es lo más urgente
2. `checklist-rgpd.md` — deber de información
3. `checklist-lssi.md` — identificación prestador
4. `checklist-forms.md` — consentimientos y doble opt-in
5. `checklist-advertising.md` — claims publicitarios
6. `checklist-security.md` — headers HTTP
7. `checklist-accessibility.md` — WCAG/EAA (es el más laborioso, déjalo para el final)

## Fase 5 — Construir el JSON de hallazgos

Formato estándar, usado por `generate-docx.mjs`:

```json
{
  "metadata": {
    "auditDate": "YYYY-MM-DD",
    "urls": ["https://..."],
    "stack": "WordPress + Elementor Pro",
    "jurisdiction": "España / UE",
    "auditor": "Automated legal audit"
  },
  "findings": [
    {
      "id": "COOKIES-001",
      "category": "cookies",
      "severity": "critical",
      "title": "Banner de cookies ausente",
      "evidence": "0 elementos con clase 'cookie-banner' o similar. 0 ocurrencias de 'cookie' en el DOM.",
      "norm": "Art. 22.2 LSSI-CE",
      "url": "https://...",
      "recommendation": "Implementar banner con opciones aceptar/rechazar/configurar...",
      "recommendationRef": "assets/templates/cookie-banner-snippet.html"
    }
  ],
  "trackers": [
    {
      "name": "TikTok Pixel",
      "url": "https://analytics.tiktok.com/api/v2/pixel/act",
      "triggered": "on page load, before any consent",
      "country": "EEUU / Irlanda / RPC (TikTok Ltd)",
      "norm": "Art. 22.2 LSSI + art. 44-49 RGPD"
    }
  ],
  "revenue": {
    "reported": 1600000,
    "source": "aportado por el auditado",
    "relevance": "criterio agravante art. 83.2.k RGPD"
  },
  "exposureScenarios": {
    "conservative": { "min": 50000, "max": 120000 },
    "medium": { "min": 150000, "max": 400000 },
    "aggravated": { "description": "...", "max": 650000 }
  }
}
```

## Fase 6 — Generar entregables

### 6.1 Generar informe docx

```bash
node <skill-path>/scripts/generate-docx.mjs \
  --findings <output-dir>/evidence.json \
  --output <output-dir>/Auditoria-Legal-<dominio>_<YYYY-MM-DD>.docx
```

### 6.2 Generar plan de remediación

Crea `remediation.md` con:

1. Resumen de acciones priorizadas (crítica/alta/media/baja)
2. Por cada hallazgo, una sección con:
   - Qué hay que cambiar
   - Texto modelo (de `assets/templates/`) si aplica
   - Snippet de código si aplica
3. Checklist final marcable

### 6.3 Abrir y ofrecer enviar

```bash
open <output-dir>/Auditoria-Legal-*.docx
```

Entrega la ruta del `.docx` al usuario. Si tiene instalada alguna skill de envío (WhatsApp, email), ofrécele usarla; no asumas que existe.

## Errores comunes y cómo evitarlos

- **Scraping antes de interceptar red**: primero `read_network_requests`, después el resto. La red se limpia entre navegaciones.
- **Confundir subdominios**: `edibschool.com` ≠ `mkthackers.edibschool.com`. Audita cada subdominio por separado si tienen stacks distintos.
- **Política de cookies dice X pero la realidad es Y**: muy común. Siempre contrasta lo que declara la política con lo que observas en la red. La discrepancia es por sí misma una infracción del art. 5.1.a RGPD (principio de lealtad).
- **Enlaces legales rotos**: prueba variantes típicas `/politica-privacidad` vs `/politica-de-privacidad`. Un 404 aquí es hallazgo.
- **Claims publicitarios sin soporte**: no los verifiques, pero cítalos y marca "Requiere verificación humana — solicitar al responsable prueba documental de: [claim]".
