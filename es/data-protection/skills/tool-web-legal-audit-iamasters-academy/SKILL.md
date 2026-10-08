---
name: tool-web-legal-audit-iamasters-academy
title: Web Legal Audit
description: Audita cualquier URL web para detectar incumplimientos legales — RGPD, LSSI-CE, cookies (Guía AEPD), accesibilidad WCAG 2.2 / EAA, seguridad HTTP, publicidad engañosa — y genera un informe docx para abogados con sanciones estimadas basadas en precedentes reales de la AEPD y un plan de remediación con textos modelo y snippets de código. Úsala SIEMPRE que el usuario pase una URL y pida "auditar", "revisar legalmente", "ver si cumple GDPR/RGPD", "auditar cookies", "comprobar accesibilidad", "detectar trackers", "revisar política de privacidad", "ver si es legal", "landing auditoría" o conceptos equivalentes. Úsala también de forma proactiva cuando el usuario comparta una landing/web propia o de terceros y mencione dudas de cumplimiento, riesgo de sanción, AEPD, cookies, banner, pixel, Meta/TikTok/Google Analytics, checkbox de consentimiento, aviso legal, política de privacidad o garantías publicitarias. Si el usuario solo pega una URL sin contexto claro pero la conversación va
  de legal/marketing/web, pregunta brevemente antes de triggerar.
author: iamasters-academy
author_url: https://github.com/iamasters-academy/iamasters-os/tree/main/skills-library/tools/tool-web-legal-audit
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: data-protection
language: es
sources:
- title: Aepd Precedents
  path: references/aepd-precedents.md
- title: Checklist Accessibility
  path: references/checklist-accessibility.md
- title: Checklist Advertising
  path: references/checklist-advertising.md
- title: Checklist Cookies
  path: references/checklist-cookies.md
- title: Checklist Forms
  path: references/checklist-forms.md
- title: Checklist Lssi
  path: references/checklist-lssi.md
- title: Checklist Rgpd
  path: references/checklist-rgpd.md
- title: Checklist Security
  path: references/checklist-security.md
- title: Report Structure
  path: references/report-structure.md
- title: Trackers Database
  path: references/trackers-database.md
- title: Workflow
  path: references/workflow.md
---

# Web Legal Audit

Auditoría integral black-box de una URL para detectar incumplimientos legales y generar dos entregables: un informe .docx para abogados (con sanciones estimadas y precedentes reales) y un plan de remediación con textos + código listos para aplicar.

## Cuándo usar esta skill

Arranca cuando el usuario pida auditar una URL desde cualquier ángulo de cumplimiento legal. La skill cubre:

- **RGPD** (UE) 2016/679 — derechos del interesado, base legal, transferencias internacionales
- **LOPDGDD** (España) L.O. 3/2018 — régimen sancionador nacional
- **LSSI-CE** (España) Ley 34/2002 — identificación prestador, cookies (art. 22.2), comunicaciones comerciales
- **Guía AEPD sobre uso de cookies** (vigente)
- **Directiva ePrivacy** 2002/58/CE
- **WCAG 2.2 AA** + European Accessibility Act (EN 301 549) — obligatorio en UE desde 28-jun-2025
- **Seguridad HTTP** — headers, HTTPS, cookies
- **Ley General de Publicidad** 34/1988 y **LGDCU** R.D.L. 1/2007 — claims publicitarios y información precontractual

Si el usuario da solo el dominio raíz, pregunta si quiere auditar también subpáginas clave (landings de captación, checkout, thank-you, páginas legales).

## Filosofía de la auditoría

La credibilidad del informe depende de **evidencias verificables**, no de opiniones. Cada hallazgo debe:

1. Citar el check concreto (qué se buscaba)
2. Reportar qué se encontró o qué faltaba (evidencia literal: trozo de HTML, URL de red interceptada, cita de texto)
3. Vincularlo a la norma y artículo preciso
4. Asociar una horquilla sancionadora apoyada en precedentes reales

Sin evidencias directas, un informe legal no sirve: los abogados necesitan citar hechos.

## Workflow maestro

Ejecuta estas 6 fases en orden. Cada fase tiene un archivo de referencia con el detalle operativo — cárgalo cuando toque esa fase.

### Fase 1 — Plan y confirmación
Antes de navegar, define con el usuario:

- **URL(s) objetivo**: ¿solo la que dio o también subpáginas? (recomienda incluir siempre home, landings de captación y páginas legales enlazadas)
- **Jurisdicción principal**: España/UE por defecto; si el responsable es extranjero, adapta
- **Contexto comercial sensible**: ¿la URL ha generado ingresos cuantificables? Esto es criterio agravante (art. 83.2.k RGPD)
- **Formato de salida**: docx para abogados por defecto; pregunta si quiere también HTML dashboard

Confirma el directorio de salida. Default: `projects/web-legal-audit/<YYYY-MM-DD>/<dominio>/`

### Fase 2 — Descubrimiento y scrape
Carga `references/workflow.md` sección "Fase 2" para los comandos concretos. En resumen:

- Abre la URL en navegador real (Claude in Chrome preferido, Firecrawl como fallback)
- Extrae DOM completo, encabezados HTTP, `<html lang>`, meta, scripts
- Detecta stack (WordPress+Elementor, GoHighLevel/LeadConnector, Next.js, Webflow, Wix, etc.) — condiciona qué trackers/cookies esperar
- Encuentra y lista todos los enlaces legales en el footer (aviso, privacidad, cookies, términos)
- Identifica formularios y sus campos (tipo, name, label)

### Fase 3 — Interceptación de red y detección de trackers
Carga `references/trackers-database.md` para la tabla de patrones. La clave: **las llamadas disparadas en la primera carga, sin interacción del usuario, sin banner**, son infracciones del art. 22.2 LSSI-CE. Registra:

- Todas las peticiones XHR/Fetch/Document
- Matcheo por patrón (TikTok Pixel, Meta Pixel, Google Ads, GA4, GTM, Hotjar, Clarity, LinkedIn Insight, Pinterest, etc.)
- País de destino del tracker → implicaciones art. 44-49 RGPD

### Fase 4 — Checks de cumplimiento
Ejecuta los 7 checklists especializados. Carga cada archivo **solo cuando toque** para no saturar el contexto:

- `references/checklist-rgpd.md` — información al interesado, base legal, derechos, RAT, encargados
- `references/checklist-lssi.md` — identificación prestador, comunicaciones comerciales, términos
- `references/checklist-cookies.md` — banner, inventario, Consent Mode v2, doble capa
- `references/checklist-forms.md` — consentimiento granular, doble opt-in, captcha, dark patterns
- `references/checklist-accessibility.md` — WCAG 2.2 AA + EAA (cómo usar Lighthouse/axe-core)
- `references/checklist-security.md` — headers HTTP, HTTPS, cookies seguras
- `references/checklist-advertising.md` — claims cuantificados, testimonios, garantías

Para cada check: marca **Cumple / No cumple / No aplica / Requiere verificación humana** con evidencia.

### Fase 5 — Valoración de riesgo sancionador
Carga `references/aepd-precedents.md` y cruza los hallazgos con la jurisprudencia reciente. Construye tres escenarios (conservador / medio / agravado) considerando:

- Gravedad de cada infracción (art. 83.4 o 83.5 RGPD; art. 72-74 LOPDGDD; art. 39 LSSI)
- Agravantes: intencionalidad, duración, número de afectados, categorías de datos, **beneficio económico directo** (art. 83.2.k)
- Acumulación de infracciones

Si el usuario aportó cifras de facturación vinculadas a la URL, úsalas como base del cálculo del 4% (art. 83.5 RGPD).

### Fase 6 — Entregables
Carga `references/report-structure.md` para la estructura del docx. Genera:

1. **Informe .docx** ejecutando `scripts/generate-docx.mjs` con el JSON de hallazgos
2. **Plan de remediación** en `remediation.md` con:
   - Lista priorizada de acciones (crítica → baja)
   - Textos modelo para aviso legal, política de privacidad y política de cookies (ver `assets/templates/`)
   - Snippets de código (banner cookies conforme AEPD, checkbox formulario, headers HTTP, Consent Mode v2)
3. **JSON de evidencias** `evidence.json` con los hallazgos crudos para trazabilidad

Archiva todo en la carpeta definida en Fase 1. Abre el docx al terminar o indica la ruta exacta para revisarlo.

## Principios inquebrantables

**No inventes sanciones.** Si el usuario pregunta cuánto podrían multarle, responde solo con horquillas legales reales (del art. 83 RGPD o art. 39 LSSI) y precedentes documentados en `references/aepd-precedents.md`. Si no hay precedente claro, dilo.

**No prometas resultados procesales.** El informe estima exposición, no garantiza que la AEPD vaya a sancionar ni la cuantía final. Este es un documento técnico-jurídico, no un dictamen.

**Cita textualmente.** Cuando detectes texto problemático (un claim, una política contradictoria), transcríbelo entre comillas en el informe. Los abogados necesitan la cita literal para construir el expediente.

**Separa hecho de calificación.** "Se disparó una petición a analytics.tiktok.com/api/v2/pixel/act" es un hecho. "Esto infringe el art. 22.2 LSSI-CE" es una calificación. Ambos van al informe, pero no los mezcles.

**Marca lo que requiere verificación humana.** Algunos checks (por ejemplo, si un testimonio es real o está inventado) no se pueden verificar automáticamente. Márcalo como "Requiere verificación humana" y documenta qué debería revisar un jurista.

## Acumulación de conocimiento

Cuando termines una auditoría, si descubres:

- Un tracker nuevo no listado en `trackers-database.md`
- Un precedente AEPD reciente con cifra (desde resoluciones de aepd.es)
- Un patrón recurrente en cierto stack (ej. GoHighLevel siempre sin banner)

Añádelo al archivo de referencia correspondiente con la fecha y la fuente. La skill mejora con cada uso.

## Uso de otras skills

- `anthropic-skills:docx` o `scripts/generate-docx.mjs` → informe para abogados
- `whatsapp` → enviar el informe al usuario cuando termine
- `tool-web-security-audit` → **NO usar en lugar de esta skill**; complementaria si el usuario pide análisis técnico de vulnerabilidades (OWASP, CVE)

## Estructura de archivos generados

```
projects/web-legal-audit/<YYYY-MM-DD>/<dominio>/
├── Auditoria-Legal-<dominio>_<YYYY-MM-DD>.docx    # Informe principal
├── remediation.md                                  # Plan de acción
├── evidence.json                                   # Hallazgos crudos
├── screenshots/                                    # Capturas de hallazgos
│   ├── homepage.png
│   ├── form-without-consent.png
│   └── ...
└── network-trace.json                              # Peticiones interceptadas
```

Skill original de Angel Aparicio (IA Masters Academy), adaptada para iamasters-os.
