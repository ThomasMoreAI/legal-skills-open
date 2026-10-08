# Checklist RGPD (UE 2016/679) + LOPDGDD (L.O. 3/2018)

Cada check tiene: **id**, **qué buscar**, **cómo verificarlo**, **norma**, **severidad**, **remediación sugerida**.

## RGPD-001 — Información al interesado en el momento de la recogida (art. 13 RGPD)

**Qué buscar**: cuando la web recoge datos (formulario, chat, registro), debe informar en ese mismo punto de:
- Identidad y contacto del responsable
- DPO/DPD (si procede)
- Fines del tratamiento y base legal
- Destinatarios / cesionarios
- Transferencias internacionales y garantías
- Plazo de conservación
- Derechos (acceso, rectificación, supresión, limitación, portabilidad, oposición, decisiones automatizadas)
- Derecho a reclamar ante la autoridad de control (AEPD)
- Si el dato es requisito legal o contractual

**Cómo verificarlo**:
1. Localiza todos los formularios en la(s) página(s).
2. Junto a cada formulario busca: (a) checkbox con enlace a política de privacidad, (b) texto informativo resumen, o (c) al menos un enlace claro.
3. Abre la política de privacidad enlazada y comprueba presencia de los 10 puntos.

**Norma**: Art. 13 RGPD. LOPDGDD art. 11. Guía AEPD "Directrices para elaborar cláusulas informativas" (2018).

**Severidad**: CRÍTICA si el formulario no tiene ninguna información. ALTA si falta política de privacidad. MEDIA si la política existe pero está incompleta.

**Remediación**: ver `assets/templates/politica-privacidad.md`.

## RGPD-002 — Base legal del tratamiento (art. 6 y 9 RGPD)

**Qué buscar**: la política debe declarar la base legal por cada finalidad. No basta con "su consentimiento". Debe especificar:
- Consentimiento (art. 6.1.a) — cuándo y cómo se obtiene
- Ejecución contractual (art. 6.1.b)
- Obligación legal (art. 6.1.c)
- Interés vital (art. 6.1.d)
- Interés público (art. 6.1.e)
- Interés legítimo (art. 6.1.f) — exige test de ponderación documentado

**Cómo verificarlo**: busca en la política el bloque "Base legal" o "Legitimación". Debe mapear finalidades ↔ bases.

**Norma**: Art. 6 RGPD. Para categorías especiales (salud, ideología, orientación sexual…): art. 9 RGPD requiere base adicional.

**Severidad**: ALTA si ausente. CRÍTICA si la web trata categorías especiales sin declarar base del art. 9.

## RGPD-003 — Consentimiento válido (art. 7 RGPD)

**Qué buscar**: si la base legal declarada es "consentimiento", éste debe ser:
- **Libre** — no condicionado a ejecutar un servicio no vinculado
- **Específico** — granular por finalidad (no un único checkbox para todo)
- **Informado** — con información previa completa
- **Inequívoco** — acción positiva (no casillas premarcadas, no "seguir navegando")
- **Demostrable** — el responsable debe poder probar que lo obtuvo
- **Revocable** — tan fácil como darlo

**Cómo verificarlo**:
1. Rellena un formulario (sin enviar si es testing black-box) y observa: ¿hay checkbox? ¿está premarcado (red flag)? ¿el texto del checkbox es inequívoco?
2. Si hay varias finalidades (recibir producto vs newsletter vs marketing de terceros), ¿hay checkboxes separados?
3. Busca mecanismo de revocación (link "darme de baja", ajustes de cuenta).

**Norma**: Art. 4.11 y art. 7 RGPD. Considerando 32.

**Severidad**: CRÍTICA si hay un solo checkbox "todo en uno" para finalidades múltiples, o si está premarcado.

## RGPD-004 — Derechos ARCO-POL

**Qué buscar**: la política debe listar los derechos y cómo ejercerlos:
- Acceso, Rectificación, Supresión ("olvido"), Oposición
- Portabilidad
- Limitación del tratamiento
- Revocar consentimiento
- No ser objeto de decisiones automatizadas (art. 22)
- Dirección de ejercicio (email + postal) + identificación requerida
- Plazo de respuesta: 1 mes (prorrogable 2 más si complejo, informando)
- Derecho a reclamar ante AEPD (www.aepd.es)

**Norma**: Arts. 15-22 RGPD. LOPDGDD arts. 12-18.

**Severidad**: ALTA si falta todo. MEDIA si faltan algunos.

## RGPD-005 — Transferencias internacionales (arts. 44-49 RGPD)

**Qué buscar**: si se detectan trackers o servicios que transfieren datos fuera del EEE (TikTok, Google, Meta, Zapier, Mailchimp, Stripe, etc.), la política debe:
- Identificar destinatarios
- Indicar país
- Mencionar la garantía aplicable: decisión de adecuación (ej. UK, Japón, Corea), Cláusulas Contractuales Tipo (CCT) de la Comisión 2021/914, EU-US Data Privacy Framework (para EE.UU.)

**Cómo verificarlo**: cruza la lista de trackers detectados en red con lo declarado en la política. Cada tracker que no aparezca = gap.

**Norma**: Arts. 44-49 RGPD.

**Severidad**: CRÍTICA si la web dispara trackers a terceros países sin declarar nada. MEDIA si los declara genéricamente sin identificar garantía.

## RGPD-006 — Registro de Actividades del Tratamiento (art. 30 RGPD)

**Qué buscar**: aunque no siempre es público, si la web es compleja el responsable debe disponer de RAT interno. En auditorías externas no se puede verificar; marca como "Requiere verificación humana".

**Norma**: Art. 30 RGPD. Obligatorio para >250 empleados, o cualquier tratamiento no ocasional, o si incluye datos de categorías especiales.

**Severidad**: No evaluable externamente.

## RGPD-007 — Encargados del tratamiento (art. 28 RGPD)

**Qué buscar**: proveedores que tratan datos en nombre del responsable (hosting, CRM, email marketing, analítica, pasarelas de pago) deben tener contrato de encargo del tratamiento con cláusulas del art. 28.

**Cómo verificarlo**: no es visible externamente. Marca como "Requiere verificación humana — solicitar al responsable los contratos de encargo con: [lista de proveedores detectados]".

**Severidad**: No evaluable externamente, pero se menciona en el informe como obligación pendiente de verificar.

## RGPD-008 — DPO / Delegado de Protección de Datos (art. 37 RGPD)

**Qué buscar**: si la empresa está obligada (autoridades públicas, tratamientos a gran escala, categorías especiales, etc.), debe tener DPO y publicar sus datos de contacto.

**Cómo verificarlo**: busca en la política "DPO", "DPD", "Delegado de Protección de Datos". Si aparece, verifica que hay email de contacto específico.

**Norma**: Arts. 37-39 RGPD.

**Severidad**: MEDIA si la empresa debería tenerlo y no lo publica.

## RGPD-009 — Principio de lealtad y transparencia (art. 5.1.a)

**Qué buscar**: coherencia entre lo que la política declara y la realidad técnica observada. Ejemplos de incumplimiento:
- La política dice "al entrar recibirá un aviso de cookies" y no existe banner.
- La política dice que no se cede a terceros pero la web dispara TikTok Pixel.
- La política está en inglés pero la web es solo en español.

**Norma**: Art. 5.1.a RGPD (principio general).

**Severidad**: ALTA a CRÍTICA según la magnitud de la discrepancia.

## RGPD-010 — Protección de datos por diseño y por defecto (art. 25 RGPD)

**Qué buscar**: el formulario debe pedir **solo los datos necesarios** para la finalidad (minimización). Si la finalidad es "descargar un ebook", pedir teléfono + CIF + dirección postal es desproporcionado.

**Cómo verificarlo**: inventaria campos del formulario vs propósito declarado.

**Norma**: Arts. 5.1.c y 25 RGPD.

**Severidad**: MEDIA si hay campos claramente innecesarios.

## RGPD-011 — Edad mínima / menores (art. 8 RGPD + LOPDGDD art. 7)

**Qué buscar**: en España, edad mínima para consentir tratamiento de datos en servicios digitales = **14 años** (LOPDGDD art. 7). La política debe indicarlo o pedir autorización parental.

**Cómo verificarlo**: busca texto "edad mínima", "menores", "14 años" en la política.

**Severidad**: MEDIA, ALTA si el servicio está claramente orientado a menores.
