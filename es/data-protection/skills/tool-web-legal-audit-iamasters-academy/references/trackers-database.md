# Base de datos de trackers — patrones de detección

Matchea las URLs interceptadas en red contra estos patrones. Orden: los más habituales primero.

## Publicidad / Marketing (todos requieren consentimiento)

| Tracker | Patrón URL | País | Notas |
|---|---|---|---|
| Meta Pixel | `connect.facebook.net/*/fbevents.js`, `www.facebook.com/tr` | EE.UU. (Meta Platforms) | Infracción AEPD reiterada |
| TikTok Pixel | `analytics.tiktok.com/i18n/pixel/*`, `analytics.tiktok.com/api/v2/pixel/*` | Irlanda/RPC (TikTok Ltd/ByteDance) | Transferencia internacional crítica |
| Google Ads Conversion | `www.google.com/pagead/*`, `googleadservices.com/pagead/*`, `www.google.es/pagead/*` | EE.UU. (Google LLC) | Enhanced Conversions → datos identificables |
| LinkedIn Insight Tag | `snap.licdn.com/li.lms-analytics`, `px.ads.linkedin.com` | EE.UU. (LinkedIn Corp) | — |
| Pinterest Tag | `ct.pinterest.com/v3/*`, `s.pinimg.com/ct/*` | EE.UU. (Pinterest Inc) | — |
| Twitter/X Pixel | `analytics.twitter.com`, `t.co/i/adsct` | EE.UU. (X Corp) | — |
| Snapchat Pixel | `tr.snapchat.com/cm/*`, `sc-static.net` | EE.UU. (Snap Inc) | — |
| Reddit Pixel | `www.redditstatic.com/ads/*` | EE.UU. | — |
| Microsoft UET Tag | `bat.bing.com/bat.js`, `clarity.ms/*` | EE.UU. (Microsoft) | Clarity es específico (ver abajo) |
| Google Ads Remarketing | `www.googleadservices.com/pagead/viewthroughconversion/*` | EE.UU. | — |

## Analítica (requieren consentimiento salvo muy limitadas excepciones)

| Tracker | Patrón URL | País | Notas |
|---|---|---|---|
| Google Analytics 4 | `www.googletagmanager.com/gtag/js`, `region1.google-analytics.com/g/collect`, `www.google-analytics.com/g/collect` | EE.UU. | Requiere consentimiento; usa Consent Mode v2 |
| Google Tag Manager | `www.googletagmanager.com/gtm.js`, `<noscript> iframe GTM-XXXXXX` | EE.UU. | El contenedor en sí no instala cookies; depende de qué etiquetas contenga |
| Hotjar | `static.hotjar.com`, `script.hotjar.com`, `*.hotjar.com/api/*` | Malta (Hotjar Ltd — Contentsquare) | Grabaciones de sesión → datos personales |
| Microsoft Clarity | `www.clarity.ms/tag/*`, `*.clarity.ms` | EE.UU. | Similar a Hotjar |
| Matomo (self-hosted) | `*/matomo.js`, `*/matomo.php` | UE si self-hosted | Con configuración conforme puede quedar exento |
| Plausible | `plausible.io/js/*` | UE (Estonia) | Sin cookies, sin PII — consulta criterios AEPD |
| Fathom Analytics | `cdn.usefathom.com` | EE.UU. / Canadá | Sin cookies |
| Mixpanel | `cdn.mxpnl.com`, `api.mixpanel.com` | EE.UU. | — |
| Amplitude | `cdn.amplitude.com`, `api.amplitude.com` | EE.UU. | — |
| Segment | `cdn.segment.com`, `api.segment.io` | EE.UU. (Twilio) | — |
| Heap | `heapanalytics.com`, `cdn.heapanalytics.com` | EE.UU. | — |

## Funnel builders / CRM embebidos

| Tracker | Patrón URL | Notas |
|---|---|---|
| LeadConnector / GoHighLevel | `assets.cdn.filesafe.space`, `*.leadconnectorhq.com`, `stcdn.leadconnectorhq.com`, `backend.leadconnectorhq.com/attribution_service/*` | Funnel builder SaaS; por defecto no trae banner cookies |
| Kajabi | `kajabi.com`, `*.kajabi-cdn.com` | Cursos/membership |
| ClickFunnels | `*.clickfunnels.com` | — |
| Systeme.io | `systeme.io`, `*.systeme-assets.com` | — |
| ConvertKit / Kit | `convertkit.com`, `api.convertkit.com`, `embed.ck.page` | Formularios de email |
| Mailchimp | `*.list-manage.com`, `chimpstatic.com` | — |
| ActiveCampaign | `trackcmp.net`, `*.activehosted.com` | Tracking explícito |
| HubSpot | `js.hs-scripts.com`, `hsforms.net`, `track.hubspot.com` | Pixel + formularios |
| Intercom | `widget.intercom.io`, `js.intercomcdn.com` | Chat + tracking |
| Drift | `js.driftt.com` | — |

## Chat y widgets

| Tracker | Patrón URL | Notas |
|---|---|---|
| Tawk.to | `embed.tawk.to` | — |
| Crisp | `client.crisp.chat` | — |
| Zendesk Chat | `static.zdassets.com`, `ekr.zdassets.com` | — |
| Tidio | `code.tidio.co` | — |

## Otros de alto impacto

| Tracker | Patrón URL | Notas |
|---|---|---|
| Adobe Analytics / Target | `*.omtrdc.net`, `assets.adobedtm.com` | — |
| Criteo | `static.criteo.net`, `dis.criteo.com` | Retargeting |
| Taboola/Outbrain | `trc.taboola.com`, `widgets.outbrain.com` | Contenido recomendado |
| DoubleClick | `*.doubleclick.net`, `stats.g.doubleclick.net` | Google Ads — remarketing |
| YouTube embeds | `www.youtube.com/embed/*` | En modo `youtube-nocookie.com` → menor tracking |
| reCAPTCHA | `www.google.com/recaptcha`, `www.gstatic.com/recaptcha` | Google — mencionar en política |
| hCaptcha | `hcaptcha.com` | Alternativa más privacy-friendly |
| Stripe | `js.stripe.com`, `api.stripe.com` | Pagos — cookies antifraude |
| Cloudflare Analytics | `static.cloudflareinsights.com` | Puede quedar exento si no usa cookies |

## Cómo reportarlos

Para cada tracker detectado incluye en `evidence.json`:
```json
{
  "name": "TikTok Pixel",
  "urls": ["analytics.tiktok.com/api/v2/pixel/act"],
  "triggered": "page load, no user interaction, no consent",
  "country": "Irlanda (establecimiento UE) y transferencias a RPC",
  "purposes": ["publicidad comportamental", "medición de conversiones"],
  "normCited": ["Art. 22.2 LSSI-CE", "Art. 6 RGPD", "Art. 44 RGPD"],
  "evidenceSource": "network-trace.json línea 123"
}
```

## Manutención

Cuando detectes un tracker no listado, añade su patrón aquí con la fecha de descubrimiento. Patrón: `<!-- added YYYY-MM-DD -->`. Esto mejora la skill en cada uso.
