---
name: facturacion-jaimebs2
title: Fiscalidad — Facturación
description: 'Use when the user asks about invoicing as a Spanish autónomo or company: difference between factura and recibo (invoice vs receipt), what document is needed to deduct an expense, required data on a full factura, when a simplified factura (antes ''ticket'') can be issued, rectifying invoices and credit notes (facturas rectificativas), mandatory electronic invoicing (Ley Crea y Crece, VeriFactu / SIF, Facturae), invoices received from EU SaaS providers without VAT (reverse charge), invoices from outside the EU (imports/exports, DUA), numbering series, conservation periods, and what invoicing software must comply with from 2026. Triggers on: ''factura'', ''recibo'', ''diferencia factura recibo'', ''invoice vs receipt'', ''factura simplificada'', ''ticket factura'', ''datos factura obligatorios'', ''factura rectificativa'', ''factura electrónica'', ''VeriFactu'', ''Ley Crea y Crece'', ''Facturae'', ''numeración facturas'', ''conservar facturas'', ''factura Anthropic sin IVA'',
  ''factura proveedor UE'', ''factura extranjera'', ''factura sin IVA desgravar'', ''factura software VeriFactu''.'
author: jaimebs2
author_url: https://github.com/jaimebs2/OpenSpain/tree/main/openspain/skills/fiscalidad/facturacion
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: tax
language: es
---

# Fiscalidad — Facturación

Skill que cubre **los documentos que emites y recibes** como autónomo o
empresa en España: qué es cada tipo (factura, simplificada, recibo,
albarán, presupuesto), qué datos deben llevar, cómo se corrigen, la
obligación progresiva de factura electrónica (Ley Crea y Crece y
VeriFactu) y los casos especiales (facturas UE sin IVA, facturas de
fuera de la UE).

> Esta skill orienta sobre requisitos y formatos. **No sustituye
> asesoramiento fiscal profesional ni genera facturas.**

---

## 1. Qué es cada tipo de documento

| Documento | Qué es | Validez fiscal |
|---|---|---|
| **Factura** (completa) | Documento legal que detalla una operación entre dos partes (vendedor y comprador identificados) con todos los datos fiscales | Sí — permite deducir IVA y gasto |
| **Factura simplificada** (antes *ticket*) | Versión reducida sin datos completos del destinatario, para importes pequeños o actividades específicas | Sí, con límites |
| **Recibo** | Comprobante de **pago** de una factura u otra deuda | **No** — solo justifica el pago, no la operación |
| **Albarán** | Documento de **entrega** de mercancía, sin carácter fiscal | No |
| **Presupuesto / Proforma** | Oferta previa a la operación, sin obligación de pago | No |

---

## 2. Factura vs Recibo — el malentendido más común

Muchas plataformas SaaS (Anthropic, Stripe, servicios web) entregan dos
documentos distintos por la misma operación:

- **Invoice**: factura — contiene NIF/VAT, base, IVA, total, condiciones.
- **Receipt**: recibo — confirma que esa factura ya se ha cobrado
  (suele incluir "Payment history").

### Cuál necesita Hacienda

**Para deducir un gasto en España, siempre la factura**. El recibo por sí
solo no vale porque no contiene todos los datos fiscales exigidos por el
Reglamento de Facturación (RD 1619/2012).

> **Consejo práctico**: muchas plataformas entregan un PDF único con
> ambos documentos. Si tienes que elegir o enviar uno al gestor, envía
> siempre el **invoice** (factura).

---

## 3. Datos obligatorios de una factura completa

Según el art. 6 del Reglamento de Facturación (RD 1619/2012):

1. **Número y, en su caso, serie**. La numeración debe ser correlativa y
   sin saltos dentro de cada serie.
2. **Fecha de emisión**.
3. **Fecha de operación** si es distinta de la emisión.
4. **Datos del emisor**:
   - Nombre o razón social completo.
   - NIF.
   - Domicilio fiscal.
5. **Datos del destinatario**:
   - Nombre o razón social.
   - NIF.
   - Domicilio.
6. **Descripción** clara de la operación (bien entregado o servicio
   prestado).
7. **Base imponible**.
8. **Tipo impositivo de IVA** aplicado (0 %, 4 %, 10 %, 21 %) y **cuota**
   resultante.
9. **Retención de IRPF** (si aplica), porcentaje y cuota.
10. **Importe total** = base + IVA − retención.
11. Menciones especiales según el caso:
    - "Operación exenta de IVA (art. 20 LIVA)" — si aplica.
    - "Inversión del sujeto pasivo (art. 84.1.2º LIVA)" — operaciones
      internas con reverse charge.
    - "Inversión del sujeto pasivo. Art. 44 de la Directiva 2006/112/CE"
      — operaciones intracomunitarias B2B.
    - "Régimen especial de recargo de equivalencia" — si el receptor es
      minorista en REQ.
    - "Régimen especial del criterio de caja" — si el emisor tributa por
      criterio de caja.

---

## 4. Factura simplificada

Sustituye al antiguo "ticket". Puede emitirse **en vez** de la factura
completa en los siguientes casos:

| Supuesto | Límite (IVA incluido) |
|---|---|
| Regla general | ≤ 400 € |
| Servicios específicos (hostelería, taxis, peluquerías, parkings, discotecas, aparcamientos, autopistas, tintorerías, alquiler de vídeo, venta al por menor, revelado fotográfico) | ≤ 3.000 € |
| Cualquier operación si lo autoriza expresamente la AEAT | Sin límite |

### Datos obligatorios

1. Número y serie.
2. Fecha de emisión.
3. NIF del emisor.
4. Tipo de operación (descripción).
5. Tipo impositivo y/o menciones "IVA incluido".
6. Contraprestación total.

> **No incluye los datos del destinatario**. Por eso, si el cliente es
> empresario/profesional y quiere deducir el gasto, debe **exigir
> factura completa** (art. 2.3 RD 1619/2012). Un autónomo no puede
> deducir una factura simplificada sin sus datos fiscales identificados.

---

## 5. Factura rectificativa y abonos

### Cuándo hay que rectificar

- Error en los datos fiscales (NIF, nombre, domicilio).
- Error en base, tipo o cuota del IVA.
- Devolución total o parcial de mercancía.
- Descuento o bonificación posterior a la emisión.
- Impago (operaciones a las que aplica la modificación de la base
  imponible por morosidad, arts. 80.3 y 80.4 LIVA).

### Requisitos

- Serie **específica** para rectificativas (p. ej. `R-2026-001`).
- Fecha de emisión de la rectificativa.
- Referencia a la factura rectificada (número y fecha) y motivo.
- Datos del emisor y destinatario (como factura completa).
- Cuantificación clara: indicar los importes corregidos, bien como
  "diferencias" (solo lo que cambia) o como "sustitutiva" (indicando
  todos los importes nuevos y mencionando que sustituye a la anterior).

### Plazo

- Hasta **4 años** desde el devengo del IVA de la operación rectificada.
- Para impagos: plazos específicos (6 meses desde el vencimiento en PYMES,
  1 año en empresas con facturación > 6.010.121 €).

---

## 6. Factura electrónica — obligación progresiva

### 6.1 Ley Crea y Crece (Ley 18/2022)

Obliga a la **facturación electrónica B2B** (entre empresarios y
profesionales) en todas las operaciones.

- Empresas con facturación **> 8 millones €/año**: entra en vigor al año
  del desarrollo reglamentario definitivo.
- Resto de empresas y autónomos: 2 años después.

> El reglamento técnico concreto aún está pendiente de publicación
> definitiva, por lo que las fechas exactas de entrada en vigor pueden
> variar. Consultar la información más reciente de la AEAT antes de
> tomar decisiones de software.

### 6.2 VeriFactu / SIF (RD 1007/2023)

Requisitos técnicos que deben cumplir los **sistemas informáticos de
facturación** (SIF) usados por autónomos y empresas. Incluye:

- **Registro de facturación** íntegro e inmodificable.
- **Huella digital** (hash) de cada factura encadenada con la anterior.
- **Código QR** obligatorio en la factura con los datos básicos.
- Modalidad **VeriFactu**: envío en tiempo real de los registros a la
  AEAT (voluntario). Quien no se acoja a VeriFactu tiene que conservar
  los registros y ponerlos a disposición de la AEAT si se le requieren.

**Entrada en vigor**:
- Empresas: 1 de enero de 2026.
- Autónomos: 1 de julio de 2026.

Implicación práctica: el software de facturación (propio, Excel o
servicio online) debe estar adaptado antes de la fecha. La mayoría de
plataformas comerciales (Holded, Quipu, Contasimple, FacturaDirecta,
Sage, SAP…) están emitiendo actualizaciones para cumplir.

### 6.3 Facturae (AAPP)

Formato XML obligatorio para facturar a las **Administraciones Públicas**
(AAPP) por importe superior a 5.000 €. Se presenta a través de la
plataforma **FACe** (`https://face.gob.es`).

No aplica a operaciones B2B (que irán por Crea y Crece) ni a B2C.

---

## 7. Facturas UE sin IVA (reverse charge)

Cuando recibes una factura de un proveedor establecido en **otro país
UE** (Anthropic Ireland, AWS Ireland, Stripe Ireland, Google Cloud, etc.)
y has dado tu NIF-IVA español:

- La factura llega **sin IVA** con mención *"Reverse charge applies —
  Art. 196 Directive 2006/112/EC"* o similar.
- Tú tienes que **autoimputarte el IVA** en tu declaración trimestral.

El detalle de cómo declarar (Modelo 303 casillas 10–11 y 12–13, Modelo
349, qué hacer si no estás en ROI) está en la skill
**fiscalidad-operaciones-intracomunitarias**.

> **Para poder deducir**: necesitas la **factura** del proveedor UE, no
> solo el recibo de pago. Guarda siempre el PDF del invoice.

---

## 8. Facturas de fuera de la UE

### Exportaciones (tú vendes a un cliente fuera UE)

- Factura **sin IVA** (operación exenta plena).
- Mención: "Exportación exenta conforme al art. 21 LIVA".
- Declara en casilla informativa del Modelo 303 (60, 61).
- Conserva el DUA de exportación si hay envío físico.

### Importaciones (compras a proveedor fuera UE)

- La factura del proveedor viene **sin IVA**.
- El **IVA a la importación** se paga en aduana cuando entra la
  mercancía, documentado en el **DUA** (Documento Único Administrativo).
- El DUA es el documento que permite deducir ese IVA.

### Servicios de fuera UE (Zoom USA, OpenAI USA antes de la entidad EU…)

- Si el proveedor no está en UE y actúa como empresa, la operación se
  localiza en España (regla del destino, art. 69.1.1º LIVA).
- Autoimputación del IVA similar al reverse charge intracomunitario,
  pero **no va al Modelo 349** (solo operaciones UE) y no requiere ROI.
- Se declara en casillas 10–11 o 12–13 del 303 según el caso.

---

## 9. Numeración, series y conservación

### Numeración

- Correlativa y sin saltos dentro de cada serie.
- Puede haber múltiples series (ej. `A-` para ventas normales, `R-` para
  rectificativas, `E-` para exportaciones) siempre que dentro de cada una
  la secuencia sea íntegra.
- Se reinicia cada ejercicio (recomendado, no obligatorio).

### Plazo de emisión

- **Al momento de la operación** si el destinatario es consumidor final.
- Antes del **día 16 del mes siguiente** si el destinatario es empresario
  o profesional.

### Conservación

- **4 años** fiscales (plazo de prescripción fiscal, art. 66 LGT).
- **6 años** mercantiles (art. 30 Código de Comercio) si hay obligación
  de llevar contabilidad mercantil.
- **10 años** si hay bases imponibles negativas o deducciones pendientes
  de aplicar en el Impuesto de Sociedades (art. 120 LGT).

Formato: papel, electrónico o ambos. Se puede digitalizar y destruir el
original siempre que el proceso esté homologado por la AEAT (software de
digitalización certificada).

---

## 10. Herramientas y software

Cualquier software que uses debe cumplir **VeriFactu / SIF** antes de
julio de 2026 (autónomos) o enero de 2026 (empresas). Requisitos clave:

- Firma o hash encadenado de cada factura.
- Código QR con datos de la factura.
- Modo VeriFactu (envío a AEAT) o modo no-VeriFactu con registro íntegro
  a disposición de la AEAT.
- Imposibilidad de borrar o alterar registros emitidos.

Alternativas comunes en España: **Holded**, **Quipu**, **Contasimple**,
**FacturaDirecta**, **Sage**, **A3** (Wolters Kluwer), **SAP Business
One**, plataformas propias con módulos adaptados.

Excel y Word **ya no sirven** como único sistema de facturación desde
2026; pueden usarse como apoyo, pero el registro oficial tiene que pasar
por un SIF homologado.

---

## 11. Enlaces oficiales

| Recurso | URL |
|---|---|
| Reglamento de Facturación (RD 1619/2012) | `https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696` |
| Sistemas Informáticos de Facturación y VeriFactu (AEAT) | `https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu.html` |
| Ley Crea y Crece (Ley 18/2022) | `https://www.boe.es/buscar/act.php?id=BOE-A-2022-15818` |
| FACe (factura electrónica AAPP) | `https://face.gob.es` |
| Portal IVA AEAT | `https://sede.agenciatributaria.gob.es/Sede/iva.html` |

---

## Cuándo NO usar esta skill

- Si la pregunta es sobre **cálculo del IVA trimestral** (Modelo 303,
  regímenes, tipos impositivos generales) → **fiscalidad-iva**.
- Si la pregunta es sobre **gastos deducibles** (qué puedo meter como
  gasto, retenciones en factura recibida) → **fiscalidad-irpf-autonomos**.
- Si la pregunta es sobre la **parte fiscal de facturas UE sin IVA**
  (autoimputación, Modelo 349, ROI) → **fiscalidad-operaciones-intracomunitarias**.
- Si la pregunta es sobre **obligaciones generales de autónomo** (plazos,
  calendario, qué modelos presento) → **fiscalidad-autonomos**.
- Si la pregunta es sobre el **texto de una ley** (RD 1619/2012, Ley
  Crea y Crece) completo → **boe**.
- Si la pregunta es sobre **cómo darse de alta censal** (Modelo 036) →
  **fiscalidad-modelo-036**.
