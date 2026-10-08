# Checklist Formularios y captación

## FORMS-001 — Información junto al formulario (art. 13 RGPD)

**Qué buscar**: información básica en la propia página del formulario (no solo enlazada). Mínimo: responsable, finalidad, base legal, derechos, enlace a política completa.

**Severidad**: ALTA si ausente.

## FORMS-002 — Checkbox de consentimiento explícito

**Qué buscar**: casilla **NO premarcada** junto al submit con texto "He leído y acepto la [Política de Privacidad]" (enlace a la política).

**Severidad**: CRÍTICA si falta.

## FORMS-003 — Consentimientos granulares por finalidad

**Qué buscar**: si hay múltiples finalidades (alta + newsletter + cesión a socios + WhatsApp marketing), deben ser checkboxes separados.

**Ejemplo correcto**:
- [ ] Acepto la política de privacidad (obligatorio)
- [ ] Quiero recibir newsletter (opcional)
- [ ] Autorizo comunicaciones comerciales por WhatsApp (opcional)

**Severidad**: GRAVE si "todo en uno".

## FORMS-004 — Minimización de campos (art. 5.1.c RGPD)

**Qué buscar**: solo los datos estrictamente necesarios para la finalidad declarada. "Descarga un ebook" no justifica pedir DNI, empresa y facturación.

**Severidad**: MEDIA.

## FORMS-005 — Doble opt-in para email marketing

**Qué buscar**: tras envío del formulario, email de confirmación con enlace de verificación. Sin click, el email no entra en la lista.

**Cómo verificarlo**: si la skill puede enviar el formulario de prueba, comprueba si llega el email de confirmación. Si no, marca como "Requiere verificación humana — solicitar al responsable confirmación del flujo de doble opt-in".

**Severidad**: MEDIA a GRAVE (depende también de AEPD criterio).

## FORMS-006 — Consentimiento específico para WhatsApp / SMS

**Qué buscar**: si el formulario pide teléfono y se usará para marketing directo en ese canal, checkbox separado: "Autorizo a [responsable] a contactarme por WhatsApp / SMS con comunicaciones comerciales".

**Norma**: Art. 21 LSSI + art. 6/7 RGPD.

**Severidad**: GRAVE.

## FORMS-007 — Captcha / anti-bot

**Qué buscar**: reCAPTCHA, hCaptcha, Turnstile u otro mecanismo. Si existe, nota que reCAPTCHA de Google transfiere datos a EE.UU. y debe mencionarse en política de privacidad.

**Severidad**: INFORMATIVO / MEDIA si no se menciona.

## FORMS-008 — Campos UTM/tracking ocultos

**Qué buscar**: inputs tipo `<input type="hidden" name="utm_source">`. Legal en sí mismo, pero son datos personales si se cruzan con el lead. Deben aparecer en la política como "datos de trazabilidad recogidos".

**Severidad**: INFORMATIVO.

## FORMS-009 — Dark patterns en CTAs

**Qué buscar**:
- Botón "No quiero ahorrar dinero" para rechazar (confirmshaming)
- Opción de rechazar escondida tras toggles
- Envío condicionado a dar más datos de los necesarios

**Norma**: Art. 5 RGPD + Directrices EDPB 3/2022 sobre dark patterns.

**Severidad**: ALTA.

## FORMS-010 — Thank-you page y qué se dispara tras submit

**Qué buscar**: tras enviar, observa qué llamadas de red se disparan. Típico: evento de conversión a Meta Pixel, Google Ads, TikTok Events API. Deben estar sometidos al mismo régimen de consentimiento.

**Severidad**: CRÍTICA si dispara eventos de tracking antes del consentimiento.
