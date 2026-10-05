---
name: textos-legales-arrobabeto
title: Textos legales
description: Crea o actualiza los textos legales del sitio (aviso de privacidad integral y simplificado, términos y condiciones, política de cookies y aviso legal) a partir de una entrevista con el cliente y de lo que el sitio realmente usa (formularios, Google Analytics, GTM, píxeles de Meta, Google Ads o TikTok, embeds). Trae cargados los requisitos de México y, si el sitio es de otro país, los investiga en fuentes oficiales. También configura el banner de cookies (modo y cada cuánto vuelve a preguntar). Úsala cuando pidan "haz el aviso de privacidad", "necesito la política de cookies", "los textos legales", "agregamos el píxel de Meta" o "el sitio es de España, ajusta lo legal".
author: arrobabeto
author_url: https://github.com/arrobabeto/Bin-Astro-Template/tree/main/skills/textos-legales
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: mx
practice: data-protection
language: es
sources:
- title: Documentos
  path: references/documentos.md
- title: Mexico
  path: references/mexico.md
- title: Otros Paises
  path: references/otros-paises.md
---

# Textos legales

Documentos legales coherentes con lo que el sitio hace de verdad, y un banner de cookies
configurado según el país. Los documentos se publican tal cual al pasar la verificación final:
no quedan como borrador ni esperan aprobación externa.

Referencias: [México](references/mexico.md) · [otros países](references/otros-paises.md) ·
[estructura de cada documento](references/documentos.md) · guía para personas:
[textos-legales.md](../../docs/guias/textos-legales.md).

## Input

- **Obligatorio:** país de residencia del responsable del sitio y los datos del responsable
  (se obtienen en la entrevista).
- **Opcional:** textos legales que el cliente ya tenga (se adaptan en lugar de partir de cero).

## Preflight

1. `git status -sb`: no mezcles el trabajo con cambios ajenos. Rama `contenido/*` o `feature/*`.
2. Inventario automático de lo que el sitio usa:

   ```bash
   node skills/textos-legales/scripts/inventario-datos.mjs
   ```

   Reporta idiomas, alojamiento, formularios (proveedor, campos, páginas), newsletter, medición y
   píxeles configurados en `.env`, contenido de terceros detectado (YouTube, Maps, reCAPTCHA,
   Hotjar, Clarity, WhatsApp…), la configuración de consentimiento y el estado de cada
   documento legal. Las variables de Vercel no se ven desde aquí: confírmalas en la entrevista.

3. Lee `src/content/legal/<idioma>/*.md`, `src/content/site/<idioma>.yaml` y
   `src/config/consent.ts`.

## Entrevista

Pregunta solo lo que el inventario no responde, en bloques cortos (usa la herramienta de
preguntas si existe). **Si algo no se sabe, queda pendiente: no lo supongas.**

1. **Jurisdicción:** país (y estado o provincia) de residencia del responsable; países a los que
   se dirige el sitio (si incluye la UE, aplica el RGPD). Idiomas de los textos.
2. **Responsable:** nombre o razón social, domicilio completo, correo (y, si hay, teléfono) para
   temas de privacidad, persona o departamento que atiende solicitudes.
3. **Datos que se recaban:** confirma los campos de cada formulario del inventario y pregunta por
   otros canales (WhatsApp, chat, citas, registro de usuarios, CV para vacantes).
   - ¿Algún dato **sensible** (salud, religión, origen étnico, preferencia sexual, afiliación
     sindical, biométricos)? En México requieren consentimiento expreso y por escrito: avisa que
     un formulario simple no basta.
   - ¿Datos **financieros** o de pago? ¿Datos de **menores de edad**?
4. **Finalidades:** primarias (responder, cotizar, dar el servicio) y secundarias (newsletter,
   promociones, encuestas). Cómo puede negarse la persona a las secundarias.
5. **Medición:** ¿Google Analytics 4, Google Tag Manager, Microsoft Clarity, Hotjar, otra?
6. **Publicidad:** ¿Meta (Facebook/Instagram), Google Ads, TikTok, LinkedIn, otra? ¿Remarketing o
   audiencias personalizadas?
7. **Otros terceros:** proveedor de correo (SendGrid, MailerLite…), CRM, chat, mapas, videos,
   reservas, pasarela de pago.
8. **Comercio electrónico:** ¿se vende en línea? Formas de pago, envíos, cancelaciones,
   devoluciones y garantías.
9. **Transferencias:** ¿se comparten datos con terceros para fines propios de ellos? (Los
   proveedores como Vercel, EE. UU., son encargados; menciónalos igual con su país.)
10. **Conservación:** cuánto tiempo se guardan los datos de cada finalidad.
11. **Banner de cookies** (solo si hay medición, píxeles o terceros que dejan cookies):
    - **Cada cuánto se vuelve a preguntar:** en cada sesión (cada visita nueva con el navegador
      cerrado), cada día, cada X días, cada año. Recomendado: **180 días**. Si la autoridad del
      país recomienda un máximo (por ejemplo, guías de cookies europeas), no lo excedas y cita la
      fuente.
    - **Cuánto se recuerda un rechazo:** igual que la aceptación (recomendado) o menos.
    - **Modo:** se deduce de la ley (`opt-in` si se requiere consentimiento previo; `opt-out` si
      basta informar y permitir rechazar). Confírmalo con la persona solo si la ley deja margen.
12. **Términos:** ley aplicable y tribunales que elige el cliente; si hay cuentas de usuario o
    contenido generado por usuarios.

## Pasos

1. **Requisitos del país:**
   - México: sigue [references/mexico.md](references/mexico.md) y confirma en el texto vigente
     que los artículos no cambiaron.
   - Otro país: sigue [references/otros-paises.md](references/otros-paises.md). Investiga solo en
     fuentes oficiales y arma el checklist con enlaces antes de redactar.
2. **Decide los documentos** con la tabla de [documentos.md](references/documentos.md):
   privacidad integral (siempre), simplificado (si hay formularios), términos (siempre), cookies
   (si hay rastreo o terceros con cookies), aviso legal (si el país lo exige).
3. **Redacta** en `src/content/legal/<idioma>/` con la estructura de `documentos.md`:
   - Frontmatter `title`, `description`, `updatedAt` (hoy) y `translationKey` si hay varios
     idiomas.
   - Quita el bloque "Plantilla de referencia" del texto demo.
   - Solo datos confirmados en la entrevista. Herramientas y proveedores, solo los que el sitio
     usa.
4. **Textos de interfaz** en `src/content/site/<idioma>.yaml`:

   ```yaml
   legal:
     formNotice: "[Responsable] usará tus datos para responder tu mensaje. Consulta el aviso de privacidad."
     cookieBanner: "Usamos Google Analytics para medir visitas y el píxel de Meta para publicidad. Puedes aceptar, rechazar o elegir."
     cookiesHref: /cookies
   ```

   - `formNotice`: aviso simplificado bajo cada formulario (el enlace al aviso integral se agrega
     solo). En México debe cubrir las fracciones I a IV del artículo 15 de la LFPDPPP.
   - `cookieBanner`: texto del banner que nombra lo que el sitio usa de verdad.
   - `cookiesHref`: solo si existe `cookies.md`; si no, el banner enlaza al aviso de privacidad.
   - Agrega o quita los enlaces en `footer.links` (Aviso de privacidad, Términos, Cookies, Aviso
     legal).

5. **Consentimiento** en `src/config/consent.ts`:
   - `mode`: `"opt-in"`, `"opt-out"` u `"off"` (solo si la ley no exige banner y el cliente lo
     decide).
   - `renewal`: `"session"` o `{ days: N }` (1 = cada día, 365 = cada año).
   - `rejectionDays`: días que se recuerda un rechazo.
   - `version`: súbela si cambian las herramientas o la política de cookies.
6. **Variables de entorno** si el cliente agrega píxeles: `PUBLIC_META_PIXEL_ID`,
   `PUBLIC_GOOGLE_ADS_ID`, `PUBLIC_TIKTOK_PIXEL_ID`, además de `PUBLIC_GA4_ID` o `PUBLIC_GTM_ID`
   (guía [analytics.md](../../docs/guias/analytics.md)). Con GTM, Google Ads y GA4 se configuran
   dentro de GTM. Herramientas sin variable (Clarity, Hotjar, LinkedIn) requieren código y una
   ampliación del banner: avísalo, no las agregues por tu cuenta.
7. `pnpm bsi:sync` si cambiaste `legal.*` en `site/<idioma>.yaml`, o si agregaste o quitaste
   documentos o enlaces.

## Reglas

- **No inventes datos:** razón social, domicilio, correos, plazos de conservación, proveedores,
  países o artículos de ley. Lo que falte se pregunta; un documento con huecos no se entrega.
- Cada requisito legal citado lleva su fuente oficial; si no pudiste verificarlo, dilo.
- No escribas que el sitio usa una herramienta que no usa, ni omitas una que sí.
- Los documentos se entregan listos para publicar: sin marcadores de borrador ni avisos de
  "pendiente de revisión". Si falta un dato obligatorio, no publiques: pregúntalo.
- No edites componentes para cambiar textos: todo vive en `src/content/` y `src/config/`.

## Verificación final

Es la última puerta antes de publicar. Si algo no cumple, corrígelo o pregunta; no publiques
con huecos.

1. **Contra el checklist del país:** cada requisito obligatorio aparece en el documento que
   corresponde, con su fuente.
2. **Contra el inventario:** cada formulario, herramienta y proveedor que el sitio usa está
   descrito, y no se menciona ninguno que no use.
3. **Contra la entrevista:** responsable, domicilio, correos, finalidades, plazos y banner
   coinciden con lo confirmado; no queda texto de plantilla ni datos supuestos.
4. **Coherencia:** `legal.formNotice`, `legal.cookieBanner`, `consent.ts`, la política de
   cookies y los enlaces del pie dicen lo mismo.
5. **Técnica:**

   ```bash
   pnpm check:placeholders
   pnpm verify
   ```

Con todo en verde, los documentos quedan publicados en el siguiente despliegue.

## Entrega

- Documentos creados o cambiados, con la ley y los artículos que cubre cada uno.
- Configuración del banner (modo, renovación, rechazo) y por qué.
- Checklist del país con fuentes (y lo que no se pudo verificar).
- Resultado de la verificación final.
- Pendientes que no bloquean la publicación: herramientas que requieren código y variables por
  configurar en Vercel.
