# Checklist LSSI-CE (Ley 34/2002 de Servicios de la Sociedad de la Información y Comercio Electrónico)

## LSSI-001 — Información general del prestador (art. 10)

**Qué buscar**: en cualquier sitio web que preste servicios SSI (incluye landings comerciales, tiendas, blogs monetizados), deben figurar de forma permanente y fácil:
- Nombre o denominación social
- Domicilio o dirección de una de sus establecimientos
- Dirección de correo electrónico + otro medio de contacto directo y efectivo
- Datos de inscripción en el registro mercantil (si aplica) u otro registro público
- NIF
- Si ejerce actividad sujeta a autorización administrativa: datos de la autoridad de supervisión
- Si pertenece a profesión regulada: Colegio profesional + título académico + normas profesionales aplicables
- Códigos de conducta a los que esté adherido (si aplica)

**Cómo verificarlo**: normalmente en el footer o en el Aviso Legal. Si el Aviso Legal existe pero esta sección está vacía o incompleta, es infracción.

**Severidad**: LEVE → pero fácilmente escalable a GRAVE si la omisión es total.

**Remediación**: `assets/templates/aviso-legal.md`.

## LSSI-002 — Identificación de comunicaciones comerciales (art. 20)

**Qué buscar**: las comunicaciones comerciales (ads, email marketing, push, notificaciones) deben:
- Ser claramente identificables como tales ("Publicidad", "Anuncio", "Patrocinado")
- Identificar a la persona física o jurídica en cuyo nombre se realizan
- Si son ofertas promocionales, concursos o juegos: identificarlos como tales y condiciones accesibles

**Cómo verificarlo**: revisa emails transaccionales (si los hay), anuncios en la propia web, popups.

**Severidad**: LEVE a GRAVE.

## LSSI-003 — Comunicaciones comerciales no solicitadas (art. 21)

**Qué buscar**: prohibido enviar comunicaciones comerciales por email, SMS, WhatsApp u otro medio de comunicación electrónica equivalente **sin consentimiento previo expreso**.

Excepción: si hay relación contractual previa y los datos se obtuvieron lícitamente, puede enviarse comunicación sobre **productos o servicios similares**, siempre con opción de baja en cada envío.

**Cómo verificarlo**:
1. Si el formulario pide teléfono y la finalidad incluye marketing, debe haber consentimiento específico para ese canal.
2. Si hay subscripción a newsletter, debe ser activa (no premarcada) y con doble opt-in.

**Severidad**: GRAVE si se envían masivamente sin consentimiento. La AEPD también sanciona esto bajo LSSI.

## LSSI-004 — Cookies e identificadores (art. 22.2)

**Qué buscar**: "Los prestadores de servicios podrán utilizar dispositivos de almacenamiento y recuperación de datos en equipos terminales de los destinatarios, a condición de que los mismos hayan dado su consentimiento después de que se les haya facilitado información clara y completa sobre su utilización."

Cubre: cookies, localStorage, sessionStorage, IndexedDB, fingerprinting, píxeles, SDK de terceros.

Excepción (cookies exentas de consentimiento):
- Estrictamente necesarias para el servicio solicitado por el usuario
- De autenticación, sesión, preferencias de idioma, carrito de compra, balanceo de carga

**NO están exentas**: analítica (salvo casos muy específicos), publicidad, personalización avanzada, remarketing.

**Cómo verificarlo**: combina detección de trackers en red + ausencia de banner. Si se dispara TikTok Pixel sin banner, es infracción directa.

**Severidad**: GRAVE (art. 38.4.g LSSI → 30.001€-150.000€). Muy grave si reiterada o afecta a gran número de usuarios.

**Remediación**: `assets/templates/cookie-banner-snippet.html`.

## LSSI-005 — Información previa a la contratación (art. 27)

**Qué buscar**: si la web contrata electrónicamente (pedidos, compras, suscripciones), antes del procedimiento de contratación debe informar:
- Trámites a seguir para celebrar el contrato
- Si archiva el contrato y accesibilidad
- Medios técnicos para corregir errores
- Lengua(s) en que puede formalizarse
- Condiciones generales aplicables (accesibles con posibilidad de imprimir/archivar)

**Severidad**: LEVE a GRAVE según la actividad.

## LSSI-006 — Confirmación de la recepción (art. 28)

**Qué buscar**: tras aceptar una oferta, el oferente debe confirmar la recepción:
- Enviando acuse de recibo por email u otro medio equivalente en plazo de 24 horas desde la recepción, **o**
- Confirmando por medio equivalente al utilizado en el procedimiento inmediatamente después

**Severidad**: LEVE.

## LSSI-007 — Registro de dominios y privacidad en Whois

**Qué buscar**: si el dominio está a nombre de persona física con datos ocultos, debe tenerse cuidado al cruzar con art. 10 LSSI (hay que identificar al prestador aunque no en whois).

**Severidad**: no evaluable externamente, informativo.
