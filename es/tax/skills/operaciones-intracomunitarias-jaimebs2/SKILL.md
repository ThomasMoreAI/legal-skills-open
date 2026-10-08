---
name: operaciones-intracomunitarias-jaimebs2
title: Fiscalidad — Operaciones Intracomunitarias
description: 'Use when the user asks about VAT treatment of cross-border B2B transactions within the EU from a Spanish autónomo or company''s perspective: reverse charge (inversión del sujeto pasivo), how to verify or obtain a ROI/NIF-IVA (VIES registry), quarterly self-assessment in Modelo 303 (casillas 10–11 for intracommunity acquisitions and 12–13 for reverse charge), Modelo 349 informative declaration, practical cases with SaaS providers (Anthropic Ireland, AWS Ireland, Google Cloud, Stripe) that invoice without VAT, selling services to EU businesses, or what to do when you receive an EU invoice without VAT and you are NOT registered in ROI. For the actual ROI registration procedure (Modelo 036 casillas) see fiscalidad-modelo-036. Triggers on: ''ROI'', ''VIES'', ''NIF-IVA'', ''VAT number España'', ''reverse charge'', ''inversión sujeto pasivo'', ''modelo 349'', ''operaciones intracomunitarias'', ''factura sin IVA UE'', ''Anthropic factura autónomo'', ''AWS Ireland IVA'', ''autoimputación
  IVA'', ''casilla 10 303'', ''casilla 12 303'', ''comprar SaaS UE autónomo'', ''vender servicios UE'', ''art 196 directiva 2006 112''.'
author: jaimebs2
author_url: https://github.com/jaimebs2/OpenSpain/tree/main/openspain/skills/fiscalidad/operaciones-intracomunitarias
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: tax
language: es
---

# Fiscalidad — Operaciones Intracomunitarias

Skill que cubre la operativa fiscal de compras y ventas entre un autónomo
o empresa españoles y contrapartes establecidas en **otros Estados
miembros de la UE**. Incluye ROI/VIES, inversión del sujeto pasivo
(reverse charge) y los modelos trimestrales asociados (303 autoimputación
y 349 informativa).

Para el trámite concreto del alta en ROI mediante el Modelo 036 (casillas
130, 582, 584 y paso a paso por Sede AEAT) → **fiscalidad-modelo-036**.

> Esta skill orienta sobre la operativa. **No sustituye asesoramiento
> fiscal profesional ni presenta declaraciones.**

---

## 1. Qué es una operación intracomunitaria

Transacción (de bienes o servicios) entre una empresa o autónomo
establecido en España y una contraparte establecida en otro país de la
UE, donde **ambas partes actúan como empresarios/profesionales**.

**Importante**: el régimen especial solo aplica a operaciones **B2B**
(empresa a empresa). Si vendes a un consumidor final europeo (B2C) la
regla general es otra (OSS / régimen especial de ventas a distancia).

### Dos tipos principales

| Tipo | Qué es | Tu rol típico |
|---|---|---|
| **Adquisición intracomunitaria de bienes** | Compras mercancía que cruza la frontera UE | Comprador: declaras tú el IVA (reverse) |
| **Prestación intracomunitaria de servicios** | Recibes o prestas servicios a/desde otro Estado miembro UE | Quien recibe el servicio declara el IVA |

---

## 2. ROI y VIES: qué son y por qué importan

### ROI (Registro de Operadores Intracomunitarios)

Registro censal **nacional** de la AEAT. Tienes que estar inscrito para
operar como empresario intracomunitario. El alta se solicita con el
Modelo 036.

### VIES (VAT Information Exchange System)

Base de datos **europea** que permite a cualquier empresa comprobar en
tiempo real si un NIF-IVA de otro Estado miembro es válido. Si estás en
el ROI, tu NIF aparece en VIES con el prefijo **ES** (ej. `ES12345678A`).

Si no estás en el ROI → tu NIF-IVA español **no figura** en VIES y los
proveedores UE no pueden aplicarte reverse charge.

### Verificar si estás en VIES

1. Abre `https://ec.europa.eu/taxation_customs/vies/`
2. Selecciona **"Member State: ES-España"**
3. Introduce tu **NIF sin guiones ni espacios**
4. Pulsa verificar
   - **"Sí, número de IVA válido"** → estás en ROI, todo correcto
   - **"Invalid VAT number"** → no estás en ROI, hay que solicitar el alta

### Cómo darse de alta en ROI

Se solicita con el **Modelo 036** marcando:
- Página 1 → casilla **130** (Solicitud de alta/baja en ROI). Si ya
  estás dado de alta en el censo general, también casilla **120**
  (modificación).
- Página 5, bloque D) Registros → casilla **582** (Alta) y casilla
  **584** (Fecha solicitada).

Detalle completo del trámite en **fiscalidad-modelo-036** (navegación
paso a paso por Sede AEAT, validación y firma).

**Qué esperar**: el alta **no es automática**. Hacienda tiene hasta
**3 meses** para resolver y puede pedir justificación documental
(facturas, correos con proveedores, presupuestos). Silencio positivo a
los 3 meses.

---

## 3. Inversión del sujeto pasivo (reverse charge)

### El concepto

En una operación B2B intracomunitaria, el **vendedor no cobra IVA** al
comprador. En lugar de eso, la responsabilidad de declarar (y deducir)
ese IVA recae en el **comprador**, que lo autoliquida en su propio país.

Esto se hace al amparo del **artículo 196 de la Directiva 2006/112/CE**
(servicios) o del régimen de adquisiciones intracomunitarias de bienes.
La factura del proveedor UE incluirá una mención del tipo:

> *"Reverse charge applies — Customer to account for tax under Article
> 196 of Directive 2006/112/EC"*

y aplicará un tipo impositivo del **0 %**.

### Condiciones para que aplique reverse charge

- Proveedor establecido en **otro Estado miembro UE**.
- Cliente (tú) establecido en **España** y actuando como
  **empresario/profesional**.
- Cliente con **NIF-IVA válido en VIES** (= alta en ROI).
- Operación **B2B** (no consumidor final).

### Consecuencia económica

El impacto en tu caja es **cero** (te autoimputas y deduces la misma
cuota a la vez), pero el registro formal es obligatorio.

---

## 4. Cómo declarar la operación (autónomo / PYME)

Toda operación intracomunitaria con reverse charge genera **dos
obligaciones trimestrales**:

### 4.1 Modelo 303 — Autoimputación del IVA

Aunque la factura del proveedor UE viene al 0 %, tú tienes que calcular
el IVA español que correspondería (21 % general, 10 % reducido, 4 %
superreducido, según el bien/servicio) y declararlo simultáneamente:

**Servicios intracomunitarios** (ej. SaaS):
- Casilla **12** (base imponible, bloque "Otras operaciones con
  inversión del sujeto pasivo").
- Casilla **13** (cuota IVA, misma base × tipo aplicable).
- Casilla **28–29** (base y cuota como IVA deducible por cuotas
  soportadas en operaciones interiores corrientes).

**Adquisiciones intracomunitarias de bienes**:
- Casilla **10** (base imponible de adquisiciones intracomunitarias).
- Casilla **11** (cuota IVA).
- Casilla **28–29** (deducible).

> Conceptualmente son dos grupos de casillas: bienes (10–11) vs
> servicios y otros reverse charge (12–13). En ambos casos la cuota
> vuelve a aparecer como deducible (28–29), dejando saldo neto cero
> para la operación.

**Ejemplo práctico** — factura SaaS de 180 € de Anthropic Ireland:

| Concepto | Casillas | Importe |
|---|---|---|
| Servicio recibido (base) | 12 | 180,00 € |
| IVA español equivalente (21 %) | 13 | 37,80 € |
| IVA deducible | 28 | 180,00 € |
| Cuota deducible | 29 | 37,80 € |
| **Efecto neto** | | **0,00 €** |

### 4.2 Modelo 349 — Declaración informativa

Modelo **informativo** (sin pago) donde relacionas todas las operaciones
intracomunitarias del trimestre con el NIF-IVA de cada contraparte.

- **Periodicidad**: trimestral por defecto; **mensual** si el importe
  trimestral de entregas intracomunitarias de bienes supera los
  **50.000 €**.
- **Plazos**: 1–20 del mes siguiente al fin del periodo (abril, julio,
  octubre, enero). Mensualmente, 1–20 del mes siguiente.
- **Contenido por cada operación**: NIF-IVA del proveedor/cliente UE,
  nombre, país, importe e indicador del tipo de operación:
  - **A**: adquisición intracomunitaria de bienes
  - **E**: entrega intracomunitaria de bienes
  - **I**: adquisición intracomunitaria de servicios
  - **S**: prestación intracomunitaria de servicios
  - **T**: operaciones triangulares
  - **M/H**: otros supuestos específicos
- **Hacienda cruza datos**: envía la información a la administración
  fiscal del otro país, que comprueba que el proveedor/cliente también
  ha declarado la operación. Incongruencias → requerimiento.

### 4.3 Modelo 390 (resumen anual)

Todas las operaciones intracomunitarias del año aparecerán consolidadas
en el Modelo 390 (resumen anual del IVA). Si estás exonerado del 390
(SII, o régimen simplificado + arrendamientos), se incluyen en la última
autoliquidación anual del 303.

---

## 5. Supuestos prácticos

### 5.1 Compras SaaS a proveedor UE (Anthropic, AWS Ireland, Google Cloud, Stripe, GitHub Ireland, Notion)

- Les das tu NIF al contratar.
- Te emiten factura sin IVA con mención al reverse charge.
- Cada trimestre: Modelo 303 (casillas 12, 13, 28, 29) + Modelo 349
  (clave **I**).

Si en el momento de la compra **no estabas en ROI**, la factura sigue
llegando sin IVA (el sistema del proveedor no siempre revalida en VIES),
pero **tú debes**:

1. Solicitar el alta en ROI cuanto antes (Modelo 036).
2. Declarar igualmente la operación en Modelo 303 y 349 del trimestre
   correspondiente.
3. Si Hacienda cuestiona la deducción, la jurisprudencia europea (TJUE,
   asuntos *Ecotrade* C-95/07, *Idexx* C-590/13) establece que el derecho
   a deducir no puede denegarse por un incumplimiento formal si el
   contribuyente es empresario real y el gasto está afecto.

### 5.2 Venta de servicios a autónomo/empresa de otro país UE

- Pides al cliente su NIF-IVA y lo verificas en VIES antes de facturar.
- Emites factura **sin IVA** con la mención: *"Inversión del sujeto
  pasivo. Art. 44 de la Directiva 2006/112/CE"*.
- En tu Modelo 303: casillas informativas (no generan cuota).
- En tu Modelo 349: relacionas la operación con clave **S**.

### 5.3 Compra de bienes a proveedor UE

- Proveedor emite factura sin IVA al amparo del régimen intracomunitario.
- Tu Modelo 303: casillas **10** (base) y **11** (cuota autoimputada),
  + 28/29 deducible.
- Modelo 349: clave **A**.

### 5.4 Venta B2C (a consumidor final UE)

**No** aplica reverse charge. Dependiendo del tipo de producto/servicio
y del volumen anual, puede tocar:
- Cobrar IVA español (régimen general).
- Cobrar IVA del país del comprador mediante el régimen **OSS**
  (One-Stop Shop) si superas el umbral de 10.000 € anuales en ventas
  intracomunitarias B2C.

OSS tiene sus propios modelos (Modelo 369). Fuera del alcance de esta
skill — consulta con asesoría si vendes mucho a consumidores UE.

---

## 6. Qué hacer si recibo una factura UE sin IVA y no estoy en ROI

Orden recomendado:

1. **Presentar Modelo 036** ya (casillas 120, 130, 582, 584) — ver
   **fiscalidad-modelo-036**. Se puede presentar en cualquier momento.
2. **Declarar la factura** en el Modelo 303 del trimestre en que se
   recibió, aunque el alta aún no haya sido resuelta formalmente.
3. **Incluir la operación** en el Modelo 349 del trimestre.
4. Si Hacienda requiere explicación del alta tardía: aportar la propia
   factura recibida como justificación de la necesidad del ROI.

No es recomendable indicar una fecha de alta retroactiva en la casilla
584 del 036: VIES guarda los cambios en tiempo real y Hacienda lo detecta.

---

## 7. Enlaces oficiales

| Recurso | URL |
|---|---|
| Portal IVA AEAT | `https://sede.agenciatributaria.gob.es/Sede/iva.html` |
| Modelo 349 — ficha | `https://sede.agenciatributaria.gob.es/Sede/procedimientoini/G417.shtml` |
| Modelo 303 — ficha | `https://sede.agenciatributaria.gob.es/Sede/procedimientoini/G414.shtml` |
| Modelo 036/037 — ficha | `https://sede.agenciatributaria.gob.es/Sede/procedimientoini/G322.shtml` |
| VIES (verificación NIF-IVA) | `https://ec.europa.eu/taxation_customs/vies/` |
| Directiva 2006/112/CE (IVA) | `https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:02006L0112-20240101` |

---

## 8. Resumen rápido

```
FLUJO COMPLETO (compra a proveedor UE — servicio SaaS)
──────────────────────────────────────────────────────

ANTES:
  □ Dado de alta en ROI (verificar en VIES)
  □ Proporcionar NIF-IVA ES al proveedor

AL RECIBIR FACTURA:
  □ Comprobar: sin IVA + mención reverse charge + país UE

CADA TRIMESTRE (abril, julio, octubre, enero):
  □ Modelo 303: casillas 12, 13, 28, 29 (servicios)
                 o 10, 11, 28, 29 (bienes)
  □ Modelo 349: una línea por contraparte, clave I (servicios),
                 A (bienes), S (ventas servicios), E (ventas bienes)
  □ Cuadrar: cuota devengada = cuota deducible → efecto 0

AL CIERRE:
  □ Modelo 390 (o casillas finales del 303-4T si estás exento)
```

---

## Cuándo NO usar esta skill

- Si la pregunta es solo sobre **cómo rellenar el Modelo 036** (casillas,
  páginas, navegación Sede) → **fiscalidad-modelo-036**.
- Si la pregunta es sobre el **Modelo 303** en general (tipos de IVA,
  regímenes, cálculo devengado − deducible) → **fiscalidad-iva**.
- Si la pregunta es sobre **ventas B2C al consumidor final UE** (OSS,
  Modelo 369, umbrales) → esta skill no lo cubre; derivar a asesoría o
  a una skill futura de OSS.
- Si la pregunta es sobre **importaciones/exportaciones fuera de la UE**
  (DUA, aduanas) → esta skill no lo cubre.
- Si la pregunta es sobre **emisión de la factura en sí** (datos
  obligatorios, formato, factura electrónica) → **fiscalidad-facturacion**.
- Si la pregunta es sobre **pagos fraccionados del IRPF** → **fiscalidad-irpf-autonomos**.
