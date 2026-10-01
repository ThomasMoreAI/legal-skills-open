# Fingerprint — CMP e tracker

## Identificazione della CMP (Consent Management Platform)

| CMP | Prefisso cookie / storage | Globale JS | Selettore banner | Come concedere consenso |
|-----|---------------------------|-----------|------------------|--------------------------|
| **Complianz** (WordPress) | `cmplz_*`, `cmplz_user_data` (sessionStorage) | `window.cmplz` | `.cmplz-cookiebanner` | `cmplz_set_consent('allow')` |
| **Cookiebot** (Usercentrics) | `CookieConsent` | `window.Cookiebot` | `#CybotCookiebotDialog` | `Cookiebot.submitCustomConsent(true,true,true)` |
| **OneTrust** | `OptanonConsent`, `OptanonAlertBoxClosed` | `window.OneTrust` | `#onetrust-banner-sdk` | `OneTrust.AllowAll()` |
| **iubenda** | `_iub_cs-*`, `euconsent-v2` | `window._iub` | `#iubenda-cs-banner` | `_iub.cs.api.consent()` |
| **Usercentrics** | `uc_*`, `ucData` | `window.UC_UI` | `[id*="usercentrics"]` | `UC_UI.acceptAllConsents()` |
| **CookieYes** | `cookieyes-*`, `cky-*` | `window.CookieYes` | `.cky-consent-bar` | click `.cky-btn-accept` |
| **Osano** | `osano_*` | `window.Osano` | `.osano-cm-window` | click accept-all |

> Se i cookie di consenso della policy non combaciano con la CMP reale (es. la policy dichiara `OptanonConsent` ma il sito usa Complianz), è un **inventario auto-scansionato generico**: segnalalo come difetto di accuratezza.

## Pattern degli ID tracker (per `inspect_container.sh` o grep manuale)

| Strumento | Pattern ID | Note |
|-----------|-----------|------|
| Google Analytics 4 | `G-[A-Z0-9]{6,12}` | Cookie reali: `_ga` (2 anni) + `_ga_<ID>` (2 anni). |
| Google Tag Manager | `GTM-[A-Z0-9]{5,9}` | Contenitore di tag; di per sé non traccia, ma carica gli altri. |
| Google Ads | `AW-[0-9]{8,12}` | Conversioni/remarketing. Cookie `_gcl_*`. |
| Floodlight (DV360/CM360) | `DC-[0-9]{6,12}` | Advertising Google. |
| Universal Analytics (legacy) | `UA-[0-9]{4,10}-[0-9]+` | Dismesso lug-2023: se presente, la policy è vecchia. Cookie `_gid`, `_gat`. |
| Meta Pixel | `fbq(`, `connect.facebook.net`, `facebook.com/tr` | Cookie `_fbp`, `_fbc`. |
| LinkedIn Insight | `_linkedin_data_partner_ids`, `px.ads.linkedin.com`, `snap.licdn.com` | Cookie `li_*`, `bcookie`, `lidc`, `UserMatchHistory`. |
| Hotjar | `static.hotjar.com`, `hj(` | Cookie `_hj*`. |
| Microsoft Clarity | `clarity.ms`, `window.clarity` | Cookie `_clck`, `_clsk`. |
| HubSpot | `hs-scripts.com`, `_hsq` | Cookie `hubspotutk`, `__hstc`. |
| TikTok | `analytics.tiktok.com`, `ttq` | Cookie `_ttp`. |

## Boilerplate GA4 vs tag reali (evitare falsi positivi)
Un container GA4-only contiene spesso riferimenti a `googleadservices` e `doubleclick.net`: **non** sono tag Ads separati, ma il boilerplate del `gtag` (funzioni Google Signals/remarketing di GA4). Un tag pubblicitario vero si riconosce da un ID `AW-`/`DC-` esplicito. Se `inspect_container.sh` trova solo `G-` (nessun `AW-`/`DC-`), il sito misura ma **non** fa conversion-tracking pubblicitario.

**Google Signals**: se il container mostra `google_signals`/`allow_google_signals` attivi, GA4 abilita tracciamento cross-device e cookie pubblicitari Google → finalità che sconfinano nel **marketing** e trasferimento a Google LLC (USA). Da segnalare (copertura: consenso «marketing» + adeguatezza EU-US Data Privacy Framework, di cui Google LLC è certificata).

**Consent Mode v2**: la presenza abbondante di `consent`, `ad_storage`, `ad_user_data`, `ad_personalization`, `analytics_storage`, `wait_for_update` nel container indica che i tag Google sono correttamente gattati sul consenso (default *denied*). `ads_data_redaction` attivo = quando `ad_storage` è negato i dati pubblicitari sono ridotti. È un buon segnale di conformità.

## Cookie tecnici comuni (di norma esenti da consenso, art. 122)
`PHPSESSID`, `wordpress_*`/`wp-settings-*` (solo aree autenticate), `pll_language` (Polylang), `wp-wpml_current_language` (WPML), `*_csrf*`/`XSRF-TOKEN` (sicurezza), il cookie della CMP stessa (memorizza la scelta), cookie di bilanciamento di carico. **reCAPTCHA** (`rc::a`/`rc::c`, `_GRECAPTCHA` su gstatic/google.com): spesso classificato «necessario» sui form, ma comporta trattamento Google — valutarne la classificazione caso per caso.
