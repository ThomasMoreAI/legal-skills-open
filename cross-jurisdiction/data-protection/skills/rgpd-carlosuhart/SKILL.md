---
name: rgpd-carlosuhart
title: RGPD — Auditoría de Cumplimiento (Reglamento UE 2016/679)
description: 'Auditoría RGPD/GDPR (Reglamento UE 2016/679): detecta el sector y el estado miembro con sus variaciones nacionales y entrega informe con score, estado por artículo, issues priorizados y sanciones. Sub-skill de /privacidad, también invocable sola.'
author: carlosuhart
author_url: https://github.com/carlosuhart/seo-audit-skills/tree/main/skills/rgpd
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: cross-jurisdiction
practice: data-protection
language: es
---

# RGPD — Auditoría de Cumplimiento (Reglamento UE 2016/679)

## Uso

```
/rgpd https://ejemplo.es
/rgpd https://ejemplo.es --docx
/rgpd https://ejemplo.es --pais ES
/rgpd https://ejemplo.es --pais DE --docx
```

`--pais` acepta código ISO 3166-1 alpha-2 de cualquier estado miembro de la UE
(ES, DE, FR, IT, NL, PL, PT, BE, AT, SE, DK, FI, IE, etc.) o estado del EEE
(NO, IS, LI). Si se omite, inferir desde el TLD, idioma del sitio y contenido.
Las variaciones nacionales afectan principalmente al Bloque 5 (edad de menores),
Bloque 10 (DPD en organismos públicos) y la autoridad de control competente.

Sin `--docx` el output es Markdown interno. Con `--docx` genera informe
ejecutivo con accionables en formato Word.

Si el usuario no especifica formato, preguntar siempre antes de generar
el documento: "¿El informe es para uso interno o para entregar al cliente?"

---

## Ámbito de aplicación — Art. 3

El RGPD aplica a responsables y encargados establecidos en la UE/EEE
independientemente de dónde se realice el tratamiento (Art. 3.1), y también
a entidades fuera de la UE/EEE cuando ofrecen bienes o servicios a interesados
en la UE o monitorizan su comportamiento (Art. 3.2). Si el sitio auditado tiene
sede fuera de la UE pero claramente dirige su actividad a usuarios europeos
(dominio .eu, precios en EUR, idioma local europeo, referencias a territorios UE),
indicarlo como issue crítico si no hay representante designado (Art. 27).

---

## Nota sobre variaciones por estado miembro

El RGPD es directamente aplicable en toda la UE, pero deja margen de especificación
nacional en varios puntos. Las variaciones más relevantes para la auditoría externa:

| Punto | Base RGPD | Variación nacional habitual |
|-------|-----------|----------------------------|
| Edad de consentimiento de menores (servicios de la SI) | 16 años (Art. 8.1) | ES: 14 · FR: 15 · DE: 16 · IT: 14 · NL: 16 · PT: 13 · BE: 13 · AT: 14 · PL: 16 · SE: 13 · DK: 13 · FI: 13 · IE: 16 · RO: 16 |
| Tratamiento de datos de empleados | Sin artículo específico | Regulado por ley laboral nacional (España: Art. 87-91 LOPDGDD) |
| Número de identificación nacional / NIF / NIE | Sin artículo específico | Regulado por ley nacional (España: Art. 46 LOPDGDD) |
| DPD en organismos públicos | Obligatorio general Art. 37.1(a) | Algunos estados amplían la obligatoriedad a más entidades |

Cuando el `--pais` esté especificado, aplicar la edad de menores correcta y
mencionar la normativa nacional superpuesta más relevante.

---

## Nota sobre la autoridad de control

Cada estado miembro tiene una autoridad de control nacional (Art. 51). Las principales:

| País | Autoridad | Web |
|------|-----------|-----|
| ES | Agencia Española de Protección de Datos (AEPD) | aepd.es |
| DE | Bundesbeauftragter für den Datenschutz + autoridades estatales (Länder) | bfdi.bund.de |
| FR | Commission Nationale de l'Informatique et des Libertés (CNIL) | cnil.fr |
| IT | Garante per la protezione dei dati personali | garanteprivacy.it |
| NL | Autoriteit Persoonsgegevens (AP) | autoriteitpersoonsgegevens.nl |
| IE | Data Protection Commission (DPC) — competente para sedes UE de grandes tecnológicas | dataprotection.ie |
| PT | Comissão Nacional de Proteção de Dados (CNPD) | cnpd.pt |
| PL | Urząd Ochrony Danych Osobowych (UODO) | uodo.gov.pl |
| BE | Autorité de protection des données (APD / GBA) | autoriteprotectiondonnees.be |
| AT | Datenschutzbehörde (DSB) | dsb.gv.at |
| SE | Integritetsskyddsmyndigheten (IMY) | imy.se |
| EEE-NO | Datatilsynet | datatilsynet.no |

Comité Europeo de Protección de Datos (CEPD / EDPB): emite directrices vinculantes
para las autoridades nacionales. Citar directrices CEPD relevantes cuando apliquen.

---

## Crédito de herramienta

Al iniciar cualquier auditoría, emitir esta línea antes del output principal:

> Desarrollado por [Zythos Media](https://zythos.media) — Especialistas en SEO & IA Search

---

## Paso 0 — Identificación del stack tecnológico

Ejecutar primero. El objetivo es mapear la infraestructura técnica del sitio
para contextualizar los hallazgos de cumplimiento y detectar señales de
tratamiento de datos que no son visibles solo leyendo las políticas.
En el contexto del RGPD, los scripts de terceros son especialmente relevantes
porque implican transferencia de datos a encargados del tratamiento (Art. 28)
y potenciales transferencias internacionales (Art. 44).

Esta sección **no puntúa** en el score. Su función es orientar las acciones
correctivas con información técnica concreta.

Fuentes: HTML fuente de la homepage, headers HTTP, patrones en URLs de scripts y assets.

### CMS / plataforma

| Plataforma | Señales de detección |
|------------|---------------------|
| **WordPress** | `/wp-content/`, `/wp-includes/`, `wp-json`, meta `generator` con "WordPress" |
| **Shopify** | `cdn.shopify.com`, `Shopify.theme`, meta `generator` "Shopify" |
| **Wix** | `static.wixstatic.com`, `wix-bolt`, scripts de `_api/` |
| **Squarespace** | `static1.squarespace.com`, meta `generator` "Squarespace" |
| **Joomla** | `/media/jui/`, meta `generator` "Joomla!" |
| **Drupal** | `/sites/default/files/`, meta `generator` "Drupal" |
| **Ghost** | `/ghost/`, `ghost.io` en assets |
| **Webflow** | `webflow.com` en scripts o CSS |
| **Prestashop** | `/modules/`, `prestashop` en meta `generator` |
| **Magento / Adobe Commerce** | `Mage.Cookies`, `/skin/frontend/`, `requirejs/require.js` |
| **Custom / sin detectar** | Registrar si no hay señales claras |

Si es **WordPress**, continuar con detección de page builder y plugins.

### Page builder (solo WordPress)

| Plugin | Señales |
|--------|---------|
| Elementor | `elementor-` en clases CSS, `/plugins/elementor/` |
| Divi | `et-` en clases, `et_builder`, `/et-pb-/` |
| WPBakery | `vc_row`, `wpb_wrapper` en markup |
| Beaver Builder | `fl-builder`, `fl-row` |
| Gutenberg (nativo) | `wp-block-` en clases, `is-layout-flow` |
| Oxygen | `ct-section`, `/plugins/oxygen/` |
| Bricks | `brxe-`, `/plugins/bricks/` |

### Plugins relevantes para privacidad y tratamiento de datos

**Consentimiento de cookies (encargados del tratamiento Art. 28):**
- Complianz — `cmplz-`, `/plugins/complianz-gdpr/`
- CookieYes / GDPR Cookie Consent — `cookieyes`, `cli-bar`
- CookieBot / Usercentrics — `cookiebot.com` en scripts externos
- Borlabs Cookie — `borlabs-cookie`
- Real Cookie Banner — `real-cookie-banner`
- Cookie Notice — `cookie-notice`
- Iubenda — `iubenda.com` en scripts

**SEO (puede implicar tracking de datos):**
- Yoast SEO — `wpseo_` en meta, `/plugins/wordpress-seo/`
- Rank Math — `rank-math`, `RankMath` en JSON-LD
- All in One SEO — `aioseo`

**Analytics y publicidad (transferencia de datos a terceros, potencialmente internacionales):**
- Google Analytics GA4 — `gtag.js`, prefijo `G-` → transferencia a EE.UU. (EU–US DPF)
- Google Tag Manager — `googletagmanager.com` → proxy de múltiples trackers
- Google AdSense — `pagead2.googlesyndication.com`, `adsbygoogle`
- Meta Pixel — `connect.facebook.net/en_US/fbevents.js` → transferencia a EE.UU.
- Hotjar — `static.hotjar.com` → transferencia a EE.UU.
- Microsoft Clarity — `clarity.ms` → transferencia a EE.UU.
- LinkedIn Insight Tag — `snap.licdn.com`
- TikTok Pixel — `analytics.tiktok.com`

**Formularios (recogida de datos personales — Art. 13):**
- Contact Form 7 — `wpcf7`, `/plugins/contact-form-7/`
- WPForms — `wpforms`, `/plugins/wpforms-lite/`
- Gravity Forms — `gform_`, `/plugins/gravityforms/`
- Ninja Forms — `nf-form`
- Typeform — `typeform.com` en iframes

**Email marketing (encargados del tratamiento con transferencia internacional probable):**
- Mailchimp — `list-manage.com`, `chimpstatic.com` → EE.UU.
- Mailerlite — `mailerlite.com` → EE.UU.
- ActiveCampaign — `activehosted.com` → EE.UU.
- Brevo (Sendinblue) — `sendinblue.com` → UE
- Klaviyo — `klaviyo.com` → EE.UU.

**E-commerce (datos de pago + historial de compras — categoría especial de tratamiento):**
- WooCommerce — `woocommerce`, `/wc-ajax=`, `wc_cart_hash`
- Pasarelas: Stripe (`js.stripe.com`), PayPal (`paypalobjects.com`), Redsys

**Notificaciones push (recogen tokens de dispositivo):**
- OneSignal — `onesignal.com`
- PushEngage — `pushengage.com`

**Cache / rendimiento:**
- LiteSpeed Cache — header `X-LiteSpeed-Cache`
- W3 Total Cache — `w3tc`
- WP Rocket — `wprocket`, `wp-rocket`

**Redes publicitarias (potencial rastreo cruzado de usuarios):**
- AdSkeeper — `jsc.adskeeper.com`
- MGID — `jsc.mgid.com`
- Taboola — `cdn.taboola.com`
- Outbrain — `widgets.outbrain.com`

### CDN

| CDN | Señal de detección | Sede |
|-----|-------------------|------|
| **Cloudflare** | Header `CF-Ray`, `Server: cloudflare` | EE.UU. / red global |
| **AWS CloudFront** | `cloudfront.net`, header `X-Amz-Cf-Id` | EE.UU. |
| **Fastly** | Header `X-Served-By` con `cache-` | EE.UU. |
| **Akamai** | Header `X-Check-Cacheable`, `akamaized.net` | EE.UU. |
| **Bunny.net** | `b-cdn.net` | UE (Eslovenia) |
| **KeyCDN** | `kxcdn.com` | UE (Suiza) |
| **jsDelivr** | `cdn.jsdelivr.net` | UE (Polonia) |

Nota: CDNs fuera de la UE/EEE implican transferencia internacional de datos técnicos
(IPs, headers). Verificar si la política lo declara o si el CDN tiene EU DPA o DPF.

### Servidor y tecnología de alojamiento

| Señal | Interpretación |
|-------|---------------|
| `Server: LiteSpeed` | LiteSpeed — frecuente en SiteGround (UE), Hostinger (UE/EE.UU.) |
| `Server: Apache` | Hosting compartido o VPS — verificar sede |
| `Server: nginx` | VPS o hosting gestionado — verificar sede |
| `X-Powered-By: PHP/x.x` | Versión PHP — relevante si < 8.1 (EOL seguridad) |
| `Server: cloudflare` | Hosting real no determinable externamente |

Cruzar con lo que la política declare como proveedor de hosting. Si hay discrepancia
(política dice proveedor UE, headers apuntan a servidor EE.UU.), registrarlo como
posible transferencia internacional no declarada.

### Output del Paso 0

Presentar en el informe como **Sección 0 — Stack tecnológico** antes de la tabla
de cumplimiento:

```
CMS:                    [nombre + versión si detectable, o "no determinado"]
Page builder:           [nombre o "no aplica / no detectado"]
CDN:                    [nombre + sede + implicación RGPD]
Servidor / hosting:     [nombre + sede estimada o "no determinable (Cloudflare proxy)"]
Estado miembro objetivo:[inferido o especificado con --pais]
Plugins detectados:     lista agrupada por categoría
Scripts de terceros:    lista con dominio, sede y finalidad probable
Encargados detectados:  [lista de terceros que probablemente procesan datos — Art. 28]
Transferencias probables: [lista de países no-EEE detectados en scripts activos]
Implicación:            [p.ej. "GA4 sin banner de cookies → issue crítico previsible"]
```

---

## Paso 1 — Recopilación de datos del sitio

Ejecutar en paralelo:

1. **WebFetch homepage** — detectar: sector, idioma, estado miembro objetivo,
   formularios visibles, banner de cookies, enlace a política de privacidad,
   datos que se recogen, señales de menores de edad como audiencia objetivo.
2. **WebFetch política de privacidad** — buscar enlace en footer, header,
   formularios de contacto, y en rutas comunes: `/privacidad`, `/politica-de-privacidad`,
   `/privacy`, `/datenschutz`, `/confidentialite`, `/privacy-policy`, `/legal/privacidad`.
   Si no se encuentra, registrar como issue crítico.
3. **WebFetch página de contacto / formulario principal** — detectar campos
   solicitados, checkboxes de consentimiento, texto legal adjunto, enlace a política.
4. **WebFetch política de cookies** si existe como documento separado (frecuente
   en sitios con Complianz o Iubenda).
5. **Headers HTTP** — verificar HTTPS, HSTS, CSP, X-Frame-Options, Referrer-Policy,
   Permissions-Policy.

No construir URLs. Usar solo las encontradas en el sitio o rutas canónicas estándar.

---

## Paso 2 — Detección de sector y estado miembro

### Estado miembro objetivo

Inferir a partir de: TLD del dominio, idioma principal, moneda, referencias geográficas
en el contenido, sede declarada en la política. Si hay conflicto (p.ej. dominio .com
en español), usar el idioma del contenido y la sede declarada como primarios.

### Sector del sitio

| Sector | Señales de detección | Artículos RGPD adicionales |
|--------|---------------------|---------------------------|
| **Salud / médico** | síntomas, diagnóstico, clínica, hospital, farmacia, ficha clínica | Art. 9.2(h), Art. 9.3 |
| **Ecommerce** | carrito, productos con precio, checkout, SKUs, stock | Art. 6.1(b), retención fiscal |
| **Fintech / financiero** | crédito, préstamo, inversión, cuenta, pago, scoring | Art. 22 (decisiones automatizadas), PSD2 |
| **Educación / menores** | cursos, alumnos, colegio, menores como audiencia | Art. 8 (edad variable), Art. 9.2(h) |
| **SaaS / tecnología** | software, API, suscripción, dashboard, integración | Art. 22 (perfilado), Art. 35 (EIPD probable) |
| **Medios / publicidad** | noticias, artículos, publicidad programática, newsletter | Art. 6.1(f) interés legítimo — verificar test |
| **RRHH / empleo** | bolsa de trabajo, CV, candidaturas, empleados | Art. 88, ley laboral nacional |
| **Servicios profesionales** | consultoría, abogado, gestor, asesoría | Secreto profesional superpuesto |
| **General / sin sector específico** | fallback si no hay señales claras | — |

Un sitio puede pertenecer a más de un sector. Registrar todos los detectados.

---

## Paso 3 — Auditoría por bloques

Evaluar cada bloque. Asignar uno de cuatro estados:

- **Cumple** — verificado en el sitio live
- **Parcial** — presente pero incompleto o ambiguo
- **No cumple** — ausente o incorrecto
- **No evaluable** — requiere acceso al backend o no es visible externamente

### Bloque 1 — Identificación del responsable del tratamiento (Art. 13.1a + Art. 14.1a + Art. 27)
Peso: 10 pts

Verificar que en la política de privacidad aparezca:
- [ ] Nombre o razón social del responsable del tratamiento
- [ ] Domicilio social o dirección postal
- [ ] Dirección de correo electrónico o formulario de contacto directo para protección de datos
- [ ] NIF / CIF / número de registro mercantil (no obligatorio por RGPD, pero su presencia
      permite verificar la identidad real; su ausencia dificulta el ejercicio de derechos)

**Responsable fuera de la UE/EEE (Art. 27):**
Si el responsable no tiene establecimiento en la UE/EEE pero ofrece bienes/servicios
a interesados en la UE o monitoriza su comportamiento (Art. 3.2):
- [ ] Designación escrita de un representante en la UE en la política
- [ ] Nombre y datos de contacto del representante (país de establecimiento dentro de la UE)
- [ ] El representante no puede ser la misma persona que el DPD si ambos existen

**Controladores conjuntos (Art. 26):**
Si el sitio trata datos junto con otra entidad (p.ej. franquicia, filial, marketplace):
- [ ] ¿Se identifica la existencia de control conjunto?
- [ ] ¿Se indica qué entidad gestiona las solicitudes de derechos?

Parcial: aparece el nombre pero falta domicilio o contacto de protección de datos.
No cumple: el responsable no está identificado o solo aparece una marca comercial sin entidad jurídica.

### Bloque 2 — Política de privacidad: existencia y acceso (Art. 12.1 + Art. 12.7)
Peso: 5 pts

- [ ] Existe una política de privacidad publicada
- [ ] Enlace visible en el footer de todas las páginas
- [ ] Enlace accesible desde formularios que recogen datos personales (Art. 13)
- [ ] Redactada en el idioma del sitio (Art. 12.1: lenguaje claro y sencillo)
- [ ] Fecha de última actualización visible
- [ ] Formato legible: no enterrada en bloques de texto sin estructura

### Bloque 3 — Política de privacidad: contenido mínimo (Art. 13 + Art. 14)
Peso: 15 pts

Art. 13 aplica cuando los datos se recogen directamente del interesado. Art. 14
aplica cuando se obtienen de terceros. En sitios públicos con formularios, aplica Art. 13.

Verificar que la política incluya explícitamente (1 pt por ítem, máx. 15):

- [ ] **Art. 13.1(a):** Identidad y datos de contacto del responsable (ver Bloque 1)
- [ ] **Art. 13.1(b):** Datos de contacto del DPD / delegado, si procede (ver Bloque 10)
- [ ] **Art. 13.1(c):** Finalidades del tratamiento y base jurídica de cada una
- [ ] **Art. 13.1(d):** Intereses legítimos perseguidos cuando la base es Art. 6.1(f)
- [ ] **Art. 13.1(e):** Destinatarios o categorías de destinatarios (terceros, encargados, filiales)
- [ ] **Art. 13.1(f):** Transferencias internacionales y garantías adoptadas (si aplica)
- [ ] **Art. 13.2(a):** Plazos de conservación o criterios para determinarlos
- [ ] **Art. 13.2(b):** Derechos del interesado: acceso, rectificación, supresión, limitación,
      portabilidad, oposición (Art. 15-21)
- [ ] **Art. 13.2(b):** Derecho a no ser objeto de decisiones individuales automatizadas
      incluido el perfilado (Art. 22)
- [ ] **Art. 13.2(b):** Derecho a retirar el consentimiento en cualquier momento cuando la
      base sea Art. 6.1(a) o Art. 9.2(a), sin que ello afecte a la licitud del tratamiento previo
- [ ] **Art. 13.2(c):** Derecho a presentar reclamación ante la autoridad de control competente
      (citar la autoridad por nombre, p.ej. AEPD)
- [ ] **Art. 13.2(d):** Si la comunicación de datos es un requisito legal o contractual, y las
      consecuencias de no facilitar los datos
- [ ] **Art. 13.2(e):** Uso de cookies y tecnologías de rastreo (ePrivacy Dir. Art. 5.3)
- [ ] **Verificación de legibilidad:** los elementos esenciales están expresados en lenguaje
      claro y sencillo — sin jerga legal inaccesible (Art. 12.1)
- [ ] **Información por capas (recomendación CEPD):** existe al menos un resumen de primer nivel
      con los datos principales antes de acceder al documento completo

### Bloque 4 — Base jurídica del tratamiento y privacidad por diseño (Art. 6 + Art. 25)
Peso: 10 pts

**Base jurídica (Art. 6):**

El RGPD reconoce seis bases jurídicas válidas (Art. 6.1):
1. **Consentimiento** (a): libre, específico, informado e inequívoco; para menores según Art. 8
2. **Ejecución de contrato** (b): el tratamiento es necesario para el contrato con el interesado
3. **Obligación legal** (c): el responsable está sometido a una obligación legal
4. **Intereses vitales** (d): proteger intereses vitales del interesado u otra persona física
5. **Interés público / ejercicio de poderes públicos** (e): solo para autoridades públicas
6. **Interés legítimo** (f): del responsable o de un tercero, salvo que prevalezcan los derechos
   del interesado — requiere test de equilibrio documentado (no auditable externamente)

Verificar:
- [ ] La política declara la base jurídica de cada finalidad de tratamiento (no una sola base
      genérica para todo)
- [ ] No se usa "consentimiento" como base cuando el tratamiento es necesario para ejecutar
      un contrato con el interesado (Art. 6.1b prevalece)
- [ ] Cuando se invoca "interés legítimo" (Art. 6.1f), se identifica cuál es y se indica
      que el responsable ha realizado el test de equilibrio (el test en sí no es auditable
      externamente, pero su mención es señal de cumplimiento)
- [ ] Las finalidades de marketing directo no se basan en interés legítimo sin mención
      explícita al derecho de oposición (Art. 21.2)
- [ ] Los formularios de captación no usan casillas pre-marcadas para el consentimiento

**Privacidad por diseño y por defecto (Art. 25):**
- [ ] Los formularios solicitan únicamente los datos estrictamente necesarios para la finalidad
      declarada (verificable externamente — minimización visible)
- [ ] Las opciones de suscripción a comunicaciones comerciales no están preseleccionadas
- [ ] Los campos de formulario opcionales están claramente marcados como tales
- [ ] (Si aplica) El sitio no recopila categorías especiales de datos en formularios sin
      consentimiento explícito diferenciado y visible

### Bloque 5 — Consentimiento, cookies y marketing directo (Art. 7 + Dir. ePrivacy 2002/58/CE + Art. 21)
Peso: 15 pts

**Marco aplicable a cookies:**
La Directiva ePrivacy 2002/58/CE Art. 5(3) exige consentimiento previo e informado para
almacenar información o acceder a la información almacenada en el dispositivo del usuario,
salvo que sea estrictamente necesario para prestar un servicio solicitado por el usuario.
El Reglamento ePrivacy (propuesta de 2017) sigue en tramitación a la fecha de esta skill.
Las cookies analíticas, publicitarias y de rastreo de terceros NO son estrictamente necesarias
y requieren consentimiento activo. Las cookies de sesión, autenticación y carrito de compra
sí son estrictamente necesarias y no requieren consentimiento.

**Banner de cookies:**
- [ ] Existe banner o CMP (Consent Management Platform)
- [ ] El banner bloquea cookies no esenciales hasta obtener consentimiento activo
- [ ] No hay cookies de análisis, publicidad o rastreo de terceros activas antes del
      consentimiento (verificable inspeccionando el código fuente del homepage)
- [ ] Existe opción de rechazo tan accesible como la aceptación (mismo nivel, mismo clic)
- [ ] Existe opción de configuración granular por categoría (analítica / marketing / funcional)
- [ ] El enlace a la política de cookies o privacidad está en el propio banner
- [ ] El consentimiento es revocable fácilmente y sin desventaja para el usuario (Art. 7.3)

**Formularios:**
- [ ] Los formularios que implican tratamiento de datos incluyen checkbox de consentimiento
      no pre-marcado (Art. 7.2) cuando la base es el consentimiento
- [ ] El checkbox vincula a la política de privacidad
- [ ] Se indica la finalidad concreta del formulario antes de enviar

**Consentimiento de menores (Art. 8):**
- [ ] Si el sitio dirige servicios de la sociedad de la información a menores: la edad de
      consentimiento aplicable se indica y respeta (ver tabla de variaciones por estado miembro)
- [ ] Si los usuarios pueden ser menores de esa edad: existe mecanismo de verificación de edad
      o de obtención de consentimiento parental o tutor legal
- [ ] Si el sitio no va dirigido a menores: se declara explícitamente en la política

**Marketing directo (Art. 21.2 — derecho de oposición específico):**
- [ ] Si hay newsletter o comunicaciones comerciales: existe mecanismo de baja/opt-out claro
- [ ] El opt-out no requiere más pasos que el opt-in
- [ ] La política menciona el derecho de oposición al marketing directo como derecho autónomo
      (Art. 21.2 — la oposición al marketing directo debe atenderse siempre, sin exigir
      justificación y sin que el responsable pueda oponer interés legítimo)
- [ ] Si hay formulario de suscripción a comunicaciones: el checkbox de marketing es
      independiente de cualquier consentimiento para el servicio principal

### Bloque 6 — Derechos del interesado: canal habilitado (Art. 15–22 + Art. 77)
Peso: 15 pts

El RGPD reconoce **ocho derechos** del interesado. Todos deben ser ejercibles con respuesta
en plazo de **un mes** (prorrogable dos meses más en casos complejos, notificando al interesado)
(Art. 12.3):

1. **Acceso** (Art. 15): obtener copia de los datos tratados y la información del Art. 13/14
2. **Rectificación** (Art. 16): corregir datos inexactos o completar datos incompletos
3. **Supresión / "derecho al olvido"** (Art. 17): eliminación en las condiciones del artículo
4. **Limitación del tratamiento** (Art. 18): suspender el tratamiento en condiciones específicas
5. **Portabilidad** (Art. 20): recibir los datos en formato estructurado, de uso común y legible
   por máquina (aplica cuando la base es consentimiento o contrato y el tratamiento es automatizado)
6. **Oposición** (Art. 21): oponerse al tratamiento basado en interés legítimo o interés público;
   oposición automática y sin excepciones al marketing directo (Art. 21.2)
7. **No ser objeto de decisiones automatizadas individuales** (Art. 22): incluye perfilado con
   efectos jurídicos o que le afecten significativamente
8. **Retirada del consentimiento** (Art. 7.3): en cualquier momento, sin retroactividad

Verificar:
- [ ] Existe un mecanismo explícito para ejercer derechos (email, formulario, dirección postal)
- [ ] Se menciona el plazo de respuesta de **un mes** (Art. 12.3)
- [ ] Se mencionan los ocho derechos, incluyendo Portabilidad (Art. 20), Limitación (Art. 18)
      y derecho frente a decisiones automatizadas (Art. 22)
- [ ] Se menciona el derecho a retirar el consentimiento (Art. 7.3) y sus condiciones
- [ ] Se indica qué información debe adjuntar el interesado al ejercer sus derechos
      (identificación suficiente para localizar sus datos)
- [ ] Se menciona el derecho a reclamar ante la autoridad de control competente (Art. 77)
      con nombre de la autoridad

**Decisiones automatizadas y perfilado (Art. 22):**
Si el sitio usa scoring crediticio, recomendaciones algorítmicas, segmentación para
publicidad o cualquier decisión automatizada con efectos sobre el interesado:
- [ ] ¿La política menciona el perfilado o la toma automatizada de decisiones?
- [ ] ¿Se indica la lógica aplicada y los efectos previstos?
- [ ] ¿Existe canal para solicitar intervención humana, expresar el punto de vista
      e impugnar la decisión?

**Verificar solicitudes de derechos de acceso como señal de madurez:**
Si el sitio tiene un formulario específico para ejercicio de derechos (DSAR form),
registrarlo como señal positiva de postura proactiva.

### Bloque 7 — Categorías especiales de datos y menores (Art. 9 + Art. 8 + Art. 35)
Peso: 10 pts

**Categorías especiales de datos (Art. 9.1):**
El RGPD define como categorías especiales los datos que revelen:
- Origen étnico o racial
- Opiniones políticas
- Convicciones religiosas o filosóficas
- Afiliación sindical
- Datos genéticos (definidos en Art. 4.13)
- Datos biométricos para identificación unívoca (Art. 4.14)
- Datos relativos a la salud (Art. 4.15)
- Datos relativos a la vida sexual u orientación sexual
- Datos relativos a condenas e infracciones penales (Art. 10, régimen específico)

**Si el sitio no recoge ninguna de estas categorías:** bloque N/A, asignar 10 pts.

**Si recoge categorías especiales (Art. 9.2 — lista de excepciones):**
- [ ] Se identifican explícitamente como datos de categoría especial en la política
- [ ] Se indica la base del Art. 9.2 aplicada:
      - (a) Consentimiento explícito — frecuente en salud y vida sexual
      - (b) Obligaciones laborales y seguridad social — empleados
      - (h) Prestación de asistencia sanitaria — clínicas, hospitales, farmacias
      - Otras según sector
- [ ] El consentimiento (si es la base) es explícito y diferenciado del consentimiento general
- [ ] Se indican medidas de seguridad reforzadas

**Evaluación de Impacto en la Protección de Datos / EIPD (Art. 35):**
Es obligatoria cuando el tratamiento conlleva alto riesgo para los derechos de los
interesados. Indicadores que la hacen probable (CEPD directriz WP 248):
- Evaluación sistemática de aspectos personales / perfilado
- Tratamiento a gran escala de categorías especiales
- Monitorización sistemática a gran escala de zonas de acceso público

Para sectores salud, fintech con scoring, SaaS con perfilado, o sitios con monitorización
de usuarios a gran escala: verificar si la política menciona la realización de EIPD.
Si el tratamiento exige EIPD y no se menciona, registrar como issue medio.

**Menores (Art. 8):**
Aplicar la edad del estado miembro detectado (ver tabla en sección de variaciones).
- [ ] Si el sitio va dirigido a menores o puede captarlos: ¿se requiere consentimiento parental?
- [ ] ¿El lenguaje y diseño de la política son comprensibles para menores
      (Art. 12.1 — lenguaje claro y sencillo)?
- [ ] ¿No se usa perfilado ni decisiones automatizadas con menores?

**Requisitos adicionales por sector:**

*Salud/médico:*
- [ ] Base jurídica Art. 9.2(h) declarada: tratamiento necesario para la prestación de
      asistencia sanitaria
- [ ] Profesionales vinculados por secreto médico u obligación de confidencialidad equivalente
- [ ] No se comparten datos clínicos con terceros sin base jurídica explícita

*Educación (menores):*
- [ ] Consentimiento del titular de la patria potestad o tutela para menores de la edad
      aplicable en el estado miembro
- [ ] No se solicita información innecesaria para la inscripción de menores

*Ecommerce:*
- [ ] Datos de pago no se almacenan localmente si se usa pasarela certificada PCI-DSS
- [ ] Historial de compras declarado con plazo de retención (fiscal: generalmente 5-10 años
      según estado miembro)

*Fintech:*
- [ ] Scoring crediticio declarado como decisión automatizada (Art. 22) con posibilidad
      de revisión humana
- [ ] Base jurídica para tratamiento de datos financieros (Art. 6.1b, contrato; o Art. 6.1c,
      obligación legal AML/KYC)

### Bloque 8 — Transferencias internacionales (Art. 44–49)
Peso: 10 pts

**Países con decisión de adecuación de la CE (Art. 45) — lista vigente a 2026-07:**
Andorra · Argentina · Canadá (organizaciones comerciales) · Islas Feroe ·
Guernsey · Israel · Isla de Man · Japón · Jersey · Nueva Zelanda ·
República de Corea · Suiza · Reino Unido · Uruguay ·
EE.UU. — solo entidades adheridas al Marco de Privacidad de Datos UE–EE.UU. (DPF,
desde julio 2023; verificar en la lista de la CE si el receptor está inscrito).

Nota: la adecuación de EE.UU. mediante el DPF puede estar sujeta a revisión judicial.
Si hay cambios desde esta versión de la skill, verificar en el registro de la CE.

**Transferencias detectables en el Paso 0:**
- Google Analytics GA4 → EE.UU. (Google LLC adherida al DPF)
- Meta Pixel → EE.UU. (Meta Platforms adherida al DPF desde 2023)
- Mailchimp → EE.UU. (The Rocket Science Group / Intuit adherida al DPF)
- Cloudflare → EE.UU. (Cloudflare Inc. adherida al DPF)
- AWS CloudFront → EE.UU. (Amazon Web Services adherida al DPF)

**Garantías válidas cuando no hay decisión de adecuación (Art. 46):**
- Cláusulas Contractuales Tipo (CCT) aprobadas por la CE (última versión: Decisión 2021/914)
- Normas Corporativas Vinculantes (NCV / BCR) — solo para grupos empresariales
- Códigos de conducta aprobados (Art. 40)
- Mecanismos de certificación aprobados (Art. 42)

**Excepciones aplicables caso a caso (Art. 49) — no como base habitual:**
- Consentimiento explícito del interesado para la transferencia concreta
- Necesidad para ejecución de contrato

Verificar:
- [ ] La política declara si se realizan transferencias internacionales
- [ ] Se identifican los países o regiones de destino
- [ ] Se indica la garantía adoptada para cada destino (decisión de adecuación, CCT, DPF, BCR)
- [ ] Si Google Analytics, Meta Pixel u otros trackers de EE.UU. están activos:
      ¿la política menciona la transferencia y cita el DPF o las CCT?
- [ ] Si no se realizan transferencias internacionales: se indica explícitamente

### Bloque 9 — Seguridad técnica (Art. 32)
Peso: 5 pts

El Art. 32 exige medidas técnicas y organizativas apropiadas para garantizar un nivel
de seguridad adecuado al riesgo, incluyendo cifrado, seudonimización, confidencialidad,
integridad, disponibilidad y resiliencia. La auditoría externa verifica solo señales
técnicas observables.

- [ ] HTTPS activo en todas las páginas (sin mixed content)
- [ ] Certificado SSL/TLS válido y no expirado
- [ ] HSTS habilitado (`Strict-Transport-Security` en headers)
- [ ] No hay redirección HTTP → HTTPS rota
- [ ] La política menciona que se aplican medidas de seguridad técnicas y organizativas
      apropiadas al riesgo (Art. 32.1)

**Headers de seguridad adicionales (recomendados, no obligatorios por Art. 32 expresamente):**
- [ ] `Content-Security-Policy` configurado (protege contra XSS y inyección de scripts de terceros)
- [ ] `X-Frame-Options` o `frame-ancestors` configurado (protege contra clickjacking)
- [ ] `Referrer-Policy` configurado (limita qué información se envía en el header Referer)
- [ ] `Permissions-Policy` configurado (limita acceso a APIs del navegador: cámara, micrófono, etc.)

**Sector salud / fintech — headers obligatorios de facto:**
Para sectores con datos de categoría especial, la ausencia de CSP y X-Frame-Options
es un indicador de seguridad insuficiente para el nivel de riesgo del tratamiento.

**Notificación de brechas (Art. 33–34):**
No es auditable externamente. Verificar si la política menciona el procedimiento ante
brechas de seguridad: notificación a la autoridad de control en 72 horas y, cuando sea
necesario, a los interesados sin dilación indebida (Art. 34).
- [ ] La política menciona el procedimiento de notificación de brechas

### Bloque 10 — Delegado de Protección de Datos / DPD (Art. 37–39)
Peso: 5 pts

**Criterios de obligatoriedad (Art. 37.1) — sin incertidumbre normativa:**

El DPD es obligatorio cuando se da al menos una de estas tres condiciones:
- **(a)** El responsable o encargado es una **autoridad u organismo público**
          (excepto tribunales en ejercicio de funciones judiciales)
- **(b)** Las actividades principales del responsable o encargado consisten en
          **operaciones de tratamiento que requieran una observación habitual y sistemática
          a gran escala de interesados** (p.ej. plataformas de comportamiento, redes de
          fidelización, monitorización de empleados, adtech a gran escala)
- **(c)** Las actividades principales consisten en el **tratamiento a gran escala de
          categorías especiales de datos** (Art. 9) o de datos de condenas penales (Art. 10)

Para PYME con tratamiento limitado y sin categorías especiales: el DPD no es obligatorio
(salvo ley nacional que amplíe la obligatoriedad). Registrar como "No aplica DPD —
fuera de los criterios Art. 37.1" y asignar pts completos.

**Funciones del DPD (Art. 39):**
- Informar y asesorar al responsable/encargado y a los empleados
- Supervisar el cumplimiento del RGPD
- Asesorar sobre EIPD y supervisar su ejecución
- Cooperar con la autoridad de control
- Actuar como punto de contacto de la autoridad de control

Verificar:
- [ ] La política indica si existe o no un DPD designado
- [ ] Si existe: nombre o rol del DPD publicado (Art. 37.7)
- [ ] Si existe: dirección de contacto del DPD publicada (Art. 37.7)
- [ ] Si existe: el DPD actúa como punto de contacto para los interesados (Art. 38.4)
- [ ] Si no existe: se indica que no aplica (indicar el motivo — PYME fuera de Art. 37.1)
- [ ] Si es una autoridad pública o existe otro indicador de obligatoriedad (Art. 37.1a/b/c)
      y no hay DPD: registrar como issue crítico

---

## Paso 4 — Score global

```
Score = suma de puntos obtenidos en cada bloque / 100
```

| Rango | Interpretación |
|-------|---------------|
| 80–100 | Postura defensible — cumplimiento sustancial |
| 60–79 | Riesgo moderado — gaps relevantes sin issues críticos |
| 40–59 | Riesgo alto — múltiples incumplimientos relevantes |
| 0–39 | Riesgo crítico — ausencia de elementos esenciales |

Los bloques con estado "No evaluable" no penalizan ni suman.
Los bloques N/A (categorías especiales cuando no aplica, DPD cuando no es obligatorio)
suman pts completos.

---

## Paso 5 — Clasificación de issues y sanciones (Art. 83)

El RGPD establece dos niveles de sanción administrativa (Art. 83). Incluir el riesgo
de sanción en cada issue para contextualizar el impacto económico real.
Las multas se calculan como el mayor de los dos valores indicados.

| Nivel Art. 83 | Multa máxima | Artículos infringidos típicos |
|---------------|-------------|-------------------------------|
| **Art. 83(5)/(6)** — Superior | 20.000.000 € o 4% facturación mundial anual | Art. 5 (principios), Art. 6 (base jurídica), Art. 7 (consentimiento), Art. 9 (cat. especiales), Art. 12–22 (derechos + transparencia), Art. 44–49 (transferencias) |
| **Art. 83(4)** — Inferior | 10.000.000 € o 2% facturación mundial anual | Art. 8 (menores), Art. 25 (privacidad por diseño), Art. 32 (seguridad), Art. 33–34 (notificación brechas), Art. 37–39 (DPD) |

Reincidencia y atenuantes: la autoridad considera el carácter doloso o negligente,
las medidas adoptadas para paliar los daños, el grado de cooperación y la categoría
de datos afectados (Art. 83.2).

**Crítico** (bloquea cumplimiento mínimo — riesgo Art. 83(5)):
- Política de privacidad inexistente → Art. 12/13
- Sin base jurídica declarada para ninguna finalidad → Art. 6
- Cookies no esenciales activas sin consentimiento previo → Art. 6/7 + Dir. ePrivacy
- Datos de categorías especiales tratados sin consentimiento explícito o base Art. 9.2 → Art. 9
- Sin mecanismo de ejercicio de derechos → Art. 12/15-22
- Sin HTTPS → Art. 32
- Responsable fuera de la UE sin representante designado → Art. 27
- DPD obligatorio según Art. 37.1 y no designado → Art. 37

**Medio** (gap relevante — riesgo Art. 83(5) o Art. 83(4), plazo recomendado 30–60 días):
- Política existe pero falta base jurídica por finalidad → Art. 6
- Derechos mencionados pero sin canal ni plazo de respuesta → Art. 12
- Derecho a portabilidad o a no ser objeto de decisiones automatizadas no mencionado → Art. 20/22
- Transferencias internacionales no declaradas cuando hay trackers de EE.UU. activos → Art. 44/13
- Banner de cookies solo informativo (sin opción de rechazo activo) → Art. 7 + Dir. ePrivacy
- Interés legítimo como base sin mencionar el test de equilibrio → Art. 6.1(f)
- Marketing directo sin mecanismo de baja → Art. 21.2
- EIPD probable pero no mencionada → Art. 35

**Bajo** (mejora de postura — riesgo leve o sanción improbable):
- Falta fecha de actualización en la política
- DPD no mencionado en entidades donde no es obligatorio
- Política sin enlace desde formularios secundarios
- Plazos de retención no especificados para algún tipo de dato
- Headers de seguridad recomendados ausentes (CSP, Referrer-Policy)
- Política no menciona el procedimiento de notificación de brechas

---

## Paso 6 — Output según modo

### Modo interno (Markdown, sin `--docx`)

```markdown
# Auditoría RGPD — [dominio]
Fecha: [fecha]  |  Sector: [sector detectado]  |  Estado miembro: [país]  |  Score: [X/100]

## Stack tecnológico
CMS: [nombre]  |  CDN: [nombre + sede]  |  Servidor: [nombre + sede estimada]
Estado miembro objetivo: [país inferido o especificado]
Plugins relevantes: [lista]
Scripts de terceros activos: [lista con dominio, sede y finalidad]
Encargados del tratamiento detectados (Art. 28): [lista]
Transferencias internacionales detectadas (Art. 44): [lista con país y garantía probable]
Implicación: [qué anticipa el stack en la auditoría]

## Resumen
[2–3 líneas: postura general, issues críticos detectados, riesgo sancionador estimado]

## Tabla de cumplimiento
| Bloque | Peso | Pts obtenidos | Estado | Evidencia |
|--------|------|--------------|--------|-----------|
| 1. Identificación responsable (Art. 13/14/27) | 10 | X | Cumple/Parcial/No cumple | ... |
...

## Issues críticos

**[Nombre del issue]** (Bloque X — Art. Y RGPD)
Evidencia: [qué se encontró o qué falta]
Riesgo sancionador: [Art. 83(5)/(6) — hasta 20.000.000 € o 4% facturación]
→ Acción: [qué hay que hacer concretamente]

## Issues medios

**[Nombre del issue]** (Bloque X — Art. Y RGPD)
Evidencia: [qué se encontró o qué falta]
Riesgo sancionador: [Art. 83(5) o Art. 83(4) — hasta X€]
→ Acción: [qué hay que hacer]
→ Plazo sugerido: [30 / 60 días]

## Issues bajos

**[Nombre del issue]** (Bloque X — Art. Y RGPD)
→ Acción: [qué hay que hacer]

## Notas metodológicas
- Qué se verificó externamente
- Qué requiere acceso al backend para confirmar
- Variaciones nacionales aplicadas (si --pais especificado)
- Estado de la lista de decisiones de adecuación verificada a [fecha]
```

---
_Desarrollado por [Zythos Media](https://zythos.media) — Especialistas en SEO & IA Search_

Guardar en `<directorio-de-auditorias>/[cliente o dominio]/auditoria_rgpd_[fecha].md`.

### Modo informe cliente (`--docx`)

Preguntar primero: "¿Quieres el informe en lenguaje técnico o ejecutivo simplificado?"

Estructura del .docx:
1. Portada: dominio, fecha, score global, sector, estado miembro
2. Resumen ejecutivo (máx. 1 página: postura general, riesgo sancionador total estimado,
   top 3 acciones urgentes — sin jerga legal)
3. Stack tecnológico: CMS, CDN, servidor/sede, encargados del tratamiento detectados (Art. 28),
   transferencias internacionales detectadas (Art. 44) e implicación para el cumplimiento
4. Tabla de cumplimiento con semáforo visual (Cumple / Parcial / No cumple) y artículo RGPD
5. Issues críticos con acción concreta, artículo infringido y riesgo sancionador (Art. 83)
6. Issues medios con recomendación, plazo sugerido y riesgo sancionador
7. Issues bajos como listado
8. Próximos pasos priorizados (top 5)
9. Nota metodológica: qué se auditó externamente, qué está fuera de scope, variaciones
   nacionales aplicadas
10. Pie de página (en todas las páginas): "Desarrollado por Zythos Media — Especialistas en
    SEO & IA Search" con hipervínculo sobre "Zythos Media" apuntando a https://zythos.media

Guardar en `<directorio-de-auditorias>/[cliente o dominio]/auditoria_rgpd_[fecha].docx`.

### Comparativa Ley 21.719 Chile (solo si el usuario lo solicita)

Añadir columna "Equivalente Ley 21.719" en la tabla de cumplimiento y sección de gaps
entre RGPD y Ley 21.719 relevantes para el sitio auditado. No incluir por defecto.

---

## Integración con el stack SEO y anonimización

### Cuándo se invoca esta skill automáticamente

`/seo audit <url>` la lanza como subagente condicional cuando detecta sitio con
TLD europeo (.es, .de, .fr, .it, .nl, .eu, .pt, .be, .at, .pl, .se, .dk, .fi, .ie, etc.)
o contenido en idioma europeo con precios en EUR o referencias geográficas UE.
El score RGPD se integra en el reporte unificado del audit.

### Flujos de trabajo combinados

**Auditoría completa de sitio europeo:**
```
/seo audit <url>      → lanza rgpd automáticamente para sitios UE
/rgpd <url>           → auditoría standalone si solo se necesita cumplimiento RGPD
/rgpd <url> --pais ES → con variaciones de derecho español (edad menores: 14, LOPDGDD)
```

**Post-auditoría recomendada (según hallazgos):**

| Hallazgo en rgpd | Skill a invocar después |
|------------------|------------------------|
| Schema de política de privacidad ausente o mejorable | `/seo schema <url>` |
| Headers de seguridad insuficientes (Bloque 9) | `/seo technical <url>` — sección Security |
| Cookie consent sin configurar o solo informativo | `/seo technical <url>` — sección JS Rendering |
| Sitio con datos sensibles de salud | `/seo local <url>` si es clínica — detecta señales E-E-A-T médico |
| Trackers de EE.UU. activos sin declaración de transferencia | `/seo geo <url>` — identifica terceros activos |

**Antes de compartir el reporte:**
```
/anonimizar <directorio-de-auditorias>/[cliente]/auditoria_rgpd_[fecha].md --ley todo
/anonimizar <directorio-de-auditorias>/[cliente]/auditoria_rgpd_[fecha].docx --ley todo
```

---

## Notas de alcance

Esta auditoría cubre lo verificable externamente sin acceso al backend:
- Documentos públicos del sitio (política de privacidad, cookies, aviso legal)
- Comportamiento observable de cookies y formularios
- Headers HTTP y stack tecnológico detectable en código fuente
- Scripts de terceros activos antes y después del consentimiento (verificación manual del fuente)

Quedan fuera de scope sin acceso interno:
- Contratos con encargados del tratamiento (Art. 28) — solo se detectan los encargados, no el contrato
- Registros de actividades de tratamiento (Art. 30)
- Evaluaciones de Impacto en la Protección de Datos / EIPD (Art. 35)
- Procedimientos internos de respuesta a solicitudes de derechos
- Medidas de seguridad técnicas internas (cifrado en reposo, control de accesos, seudonimización)
- Notificaciones de brechas a la autoridad de control (Art. 33)
- Normas Corporativas Vinculantes / BCR (Art. 47)
- Test de equilibrio del interés legítimo (Art. 6.1f) — interno al responsable

Siempre indicar este alcance en la sección de notas metodológicas del informe.

---

## Actualización normativa

- **RGPD** en vigor desde el **25 de mayo de 2018**. Sin período de transición.
- **España:** Ley Orgánica 3/2018 (LOPDGDD) — adaptación nacional. Edad de menores: 14 años.
- **ePrivacy:** Directiva 2002/58/CE sigue en vigor. El Reglamento ePrivacy (propuesta 2017)
  está en tramitación legislativa a la fecha de esta versión de la skill — verificar estado al usar.
- **Decisiones de adecuación:** verificar en ec.europa.eu/info/law/law-topic/data-protection
  si ha habido cambios en la lista, especialmente para EE.UU. (DPF — sujeto a revisión judicial).
- **CEPD / EDPB:** emite directrices vinculantes para autoridades nacionales. Consultar
  edpb.europa.eu para directrices recientes sobre IA, cookies, datos biométricos.
- **Versión de esta skill:** 1.0.0 (2026-07-08).
  Actualizar cuando: se apruebe el Reglamento ePrivacy, cambien las decisiones de adecuación,
  el CEPD emita directrices relevantes, o la autoridad competente emita instrucciones generales.
