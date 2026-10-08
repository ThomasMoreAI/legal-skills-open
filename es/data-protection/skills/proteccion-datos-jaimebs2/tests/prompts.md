# Tests manuales — proteccion-datos

Preguntas para validar que el agente usa la skill correctamente.

---

## Test 1 — Derechos del ciudadano

**Prompt**: "Una empresa tiene mis datos y quiero que los borren. ¿Qué puedo hacer?"

**Criterios de aceptación**:
- Explica el derecho de supresión (derecho al olvido).
- Indica que debe dirigirse primero a la empresa (responsable del tratamiento).
- Menciona el plazo de 1 mes para que la empresa responda.
- Si la empresa no responde o deniega, indica que puede reclamar ante la AEPD (gratuito).
- Menciona que hay excepciones (obligación legal, libertad de expresión, interés público).

---

## Test 2 — Reclamación ante la AEPD

**Prompt**: "He pedido a una tienda online que me diga qué datos míos tiene y no me contestan. ¿Qué hago?"

**Criterios de aceptación**:
- Identifica que se ha ejercido el derecho de acceso.
- Indica que si no responden en 1 mes, puede reclamar ante la AEPD.
- Explica cómo reclamar (sede electrónica, con certificado digital o Cl@ve).
- Menciona que es gratuito.
- Indica que debe adjuntar prueba de la solicitud y la falta de respuesta.

---

## Test 3 — Obligaciones de una empresa

**Prompt**: "Tengo una tienda online y recojo datos de clientes. ¿Qué tengo que cumplir de protección de datos?"

**Criterios de aceptación**:
- Menciona la necesidad de base jurídica (consentimiento para marketing, contrato para venta).
- Indica la política de privacidad y el deber de información.
- Menciona el registro de actividades de tratamiento.
- Sugiere la herramienta Facilita RGPD de la AEPD.
- Menciona la notificación de brechas en 72 horas.

---

## Test 4 — Routing a otra skill

**Prompt**: "¿Qué dice exactamente el artículo 17 del RGPD?"

**Criterios de aceptación**:
- Indica que para consultar el texto exacto de una norma debería usarse otra fuente.
- Redirige a la skill **boe** para textos legales.
