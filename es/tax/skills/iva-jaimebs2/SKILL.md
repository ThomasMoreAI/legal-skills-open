---
name: iva-jaimebs2
title: Fiscalidad — IVA (Impuesto sobre el Valor Añadido)
description: 'Use when the user asks about Spanish VAT (IVA) obligations, Modelo 303 quarterly filing, IVA rates (general 21%, reduced 10%, super-reduced 4%), IVA regimes, exempt activities, Modelo 390 annual summary, or IVA calculation (devengado minus deducible). Applies to both autónomos and sociedades. This is a guidance skill — it does NOT file taxes or access AEAT systems. Triggers on: ''IVA'', ''modelo 303'', ''modelo 390'', ''declaración IVA'', ''IVA trimestral'', ''tipos de IVA'', ''IVA reducido'', ''IVA superreducido'', ''IVA devengado'', ''IVA deducible'', ''régimen simplificado IVA'', ''recargo equivalencia'', ''criterio de caja'', ''actividades exentas IVA'', ''liquidación IVA''.'
author: jaimebs2
author_url: https://github.com/jaimebs2/OpenSpain/tree/main/openspain/skills/fiscalidad/iva
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: tax
language: es
---

# Fiscalidad — IVA (Impuesto sobre el Valor Añadido)

Skill de orientación sobre las obligaciones del IVA en España. Aplica tanto
a **autónomos** (personas físicas) como a **sociedades** (SL, SA, etc.) — el
Modelo 303 es idéntico para ambos.

> Esta skill orienta sobre plazos, cálculo y tipos. **No sustituye
> asesoramiento fiscal profesional ni presenta declaraciones.**

---

## Modelo 303 — Autoliquidación del IVA

### Quién lo presenta

Todo empresario o profesional que realice actividades sujetas y no exentas
de IVA, ya sea autónomo o sociedad. Excepciones: quienes tributen
exclusivamente en régimen de recargo de equivalencia o en el régimen especial
de agricultura, ganadería y pesca (REAGYP).

### Periodicidad

- **Trimestral** (mayoría de autónomos y pymes): periodos 1T, 2T, 3T, 4T.
- **Mensual**: grandes empresas (facturación > 6.010.121,04 €/año), inscritos
  en el Registro de Devolución Mensual (REDEME) y sujetos al SII.

### Plazos de presentación

| Periodo | Plazo |
|---|---|
| 1T (enero–marzo) | 1–20 abril |
| 2T (abril–junio) | 1–20 julio |
| 3T (julio–septiembre) | 1–20 octubre |
| 4T (octubre–diciembre) | 1–30 enero del año siguiente |
| Mensual | 1–30 del mes siguiente (febrero: hasta último día) |

Si el último día cae en sábado o festivo, el plazo se extiende al siguiente
día hábil.

### Cálculo básico (régimen general)

```
Resultado = IVA devengado − IVA deducible
```

- **IVA devengado**: suma de las cuotas de IVA repercutidas a los clientes
  en las facturas emitidas durante el periodo.
- **IVA deducible**: suma de las cuotas de IVA soportadas en las facturas
  recibidas de proveedores, siempre que estén vinculadas a la actividad.

Si el resultado es **positivo** → se ingresa a Hacienda.
Si el resultado es **negativo** → se compensa en trimestres siguientes (o se
solicita devolución en el 4T / mes 12).

### Casillas principales del Modelo 303

| Tipo IVA | Base (casilla) | Tipo (casilla) | Cuota (casilla) |
|---|---|---|---|
| 4% superreducido | 01 | 02 | 03 |
| 10% reducido | 04 | 05 | 06 |
| 21% general | 07 | 08 | 09 |

Casillas adicionales relevantes:
- **10–11**: adquisiciones intracomunitarias de bienes y servicios.
- **12–13**: inversión del sujeto pasivo (el receptor declara el IVA).
- **28–29**: cuotas soportadas en operaciones interiores corrientes (IVA deducible).
- **64**: resultado régimen general + simplificado.
- **71**: resultado final de la autoliquidación.

Para **ejemplo práctico de autoimputación** (factura SaaS UE sin IVA,
casillas 12/13/28/29, impacto neto cero) y cumplimentación del Modelo
349 → skill **fiscalidad-operaciones-intracomunitarias**.

---

## Tipos de IVA vigentes

### 21 % — General

Aplica a la mayoría de bienes y servicios no incluidos en tipos reducidos:
electrónica, ropa, servicios profesionales, telecomunicaciones, etc.

### 10 % — Reducido

- Hostelería y restauración (comidas y bebidas en establecimientos).
- Transporte de viajeros (avión, tren, autobús, taxi).
- Espectáculos en vivo (teatro, conciertos, cine).
- Obras de renovación y reparación de viviendas (con condiciones).
- Productos alimenticios en general (excepto los de tipo superreducido).
- Servicios de limpieza de vías públicas y recogida de residuos.
- Agua para riego y consumo animal.
- Hostelería y alojamiento turístico.

### 4 % — Superreducido

- Pan, harinas panificables, leche, quesos, huevos, frutas, verduras,
  hortalizas, legumbres, tubérculos y cereales naturales.
- Libros, periódicos y revistas (no publicidad).
- Medicamentos de uso humano.
- Prótesis, órtesis e implantes para personas con discapacidad.
- Viviendas de protección oficial (primera entrega).
- Servicios de teleasistencia, ayuda a domicilio, centros de día y noche,
  y atención residencial para dependientes.

### 0 % — Operaciones específicas

Desde 2024, determinadas entregas de bienes y prestaciones de servicios
pueden tributar al 0 % según normativa temporal o sectorial. Consultar
la normativa vigente en cada momento.

---

## Regímenes especiales del IVA

### Régimen general

El descrito arriba. Obligación de repercutir IVA en facturas, deducir IVA
soportado y presentar Modelo 303. Es el régimen por defecto.

### Régimen simplificado (módulos)

- Para autónomos en estimación objetiva del IRPF (módulos).
- Incompatible con el régimen general (salvo actividades diferenciadas).
- La cuota se calcula mediante **índices o módulos** (personal, superficie,
  consumo eléctrico…), no por facturas reales.
- Límite de ingresos: 250.000 €/año (hasta 2026).
- Presenta Modelo 303 pero con las casillas del régimen simplificado.

### Recargo de equivalencia

- Obligatorio para **comerciantes minoristas** personas físicas que venden
  al consumidor final sin transformar el producto.
- El proveedor aplica un recargo adicional al IVA en la factura.
- El minorista **no presenta Modelo 303** ni lleva libros de IVA.
- Recargos: 5,2 % (sobre base al 21 %), 1,4 % (sobre base al 10 %),
  0,5 % (sobre base al 4 %), 1,75 % (sobre base al 0 %).

### Régimen especial de agricultura, ganadería y pesca (REAGYP)

- Para explotaciones agrícolas, ganaderas, forestales o pesqueras.
- No se repercute IVA; se percibe una **compensación** del comprador:
  12 % (productos agrícolas/forestales) o 10,5 % (ganadería/pesca).
- No se presenta Modelo 303.

### Criterio de caja

- Opcional para autónomos y pymes (facturación < 2.000.000 €/año).
- El IVA se devenga **cuando se cobra** la factura (no cuando se emite).
- El IVA soportado se deduce **cuando se paga** al proveedor.
- Límite temporal: 31 de diciembre del año siguiente a la operación.
- Renuncia voluntaria con efectos mínimos de 3 años.

---

## Actividades exentas de IVA

Según el artículo 20 de la Ley 37/1992, estas actividades están **exentas**
(no se repercute IVA, pero tampoco se deduce el soportado):

- **Sanidad**: asistencia médica y sanitaria a personas físicas por
  profesionales médicos (médicos, enfermeros, psicólogos clínicos,
  odontólogos, etc.).
- **Educación**: enseñanza en centros públicos o privados autorizados,
  clases particulares por personas físicas, guarderías y centros de día
  educativos.
- **Servicios artísticos y literarios**: derechos de autor de escritores,
  artistas plásticos y colaboradores literarios o gráficos.
- **Seguros y reaseguros**: operaciones de seguro y capitalización.
- **Servicios financieros**: intermediación financiera, operaciones
  bancarias.
- **Arrendamiento de vivienda**: alquiler de inmuebles destinados
  exclusivamente a vivienda (no locales comerciales).
- **Correos**: entregas de sellos postales y efectos timbrados de curso
  legal.

Exento ≠ no sujeto. Las actividades exentas **sí** están sujetas al IVA
pero exentas de tributación. El profesional exento puede optar por no
presentar Modelo 303 si solo realiza operaciones exentas sin derecho a
deducción (casilla 501 del modelo censal 036/037).

---

## Modelo 390 — Declaración resumen anual

Declaración **informativa** (no de pago) que resume todas las operaciones
del año. Plazo: **1–30 de enero** del año siguiente.

### Exonerados de presentar el 390

- Contribuyentes trimestrales que tributen solo en territorio común y
  realicen actividades exclusivamente en régimen simplificado y/o
  arrendamiento de inmuebles urbanos.
- Sujetos pasivos incluidos en el SII (Suministro Inmediato de
  Información).

Estos contribuyentes completan la información equivalente en la última
autoliquidación del 303 del año (casillas de datos estadísticos y
volumen de operaciones).

---

## Modelo 349 — Operaciones intracomunitarias

Declaración **informativa** obligatoria para quienes realicen entregas
o adquisiciones intracomunitarias de bienes o prestaciones de servicios
a empresarios de otros países de la UE. Periodicidad trimestral (o
mensual si el importe supera 50.000 € en el trimestre).

Detalle completo (ROI/VIES, reverse charge, claves A/E/I/S, casillas
del 303 asociadas) → skill **fiscalidad-operaciones-intracomunitarias**.

---

## Enlaces oficiales

| Recurso | URL |
|---|---|
| Portal IVA AEAT | `https://sede.agenciatributaria.gob.es/Sede/iva.html` |
| Modelo 303 | `https://sede.agenciatributaria.gob.es/Sede/procedimientoini/G414.shtml` |
| Instrucciones 303 (2026) | `https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-303-iva-autoliquidacion_/instrucciones-2026.html` |
| Modelo 390 | `https://sede.agenciatributaria.gob.es/Sede/procedimientoini/G412.shtml` |
| Regímenes IVA | `https://sede.agenciatributaria.gob.es/Sede/iva/regimenes-tributacion-iva.html` |
| Actividades exentas | `https://sede.agenciatributaria.gob.es/Sede/iva/calculo-iva-repercutido-clientes/que-casos-no-tengo-que-iva/operaciones-exentas.html` |
| Calendario fiscal 2026 | `https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026.html` |

---

## Cuándo NO usar esta skill

- Si pregunta por **operaciones intracomunitarias** en detalle (ROI/VIES,
  reverse charge, Modelo 349, autoimputación en 303 con ejemplos) →
  **fiscalidad-operaciones-intracomunitarias**.
- Si pregunta por **facturación** (datos obligatorios, factura
  electrónica, VeriFactu, factura vs recibo) → **fiscalidad-facturacion**.
- Si pregunta por el **Modelo 036** (alta/modificación/baja censal,
  casillas, cambio de régimen IVA) → **fiscalidad-modelo-036**.
- Si el usuario pregunta por **estadísticas fiscales** (recaudación,
  IRPF por municipio, datos agregados del IVA) → **aeat**.
- Si pregunta por el **texto de una ley** (Ley del IVA, Reglamento) →
  **boe**.
- Si quiere **presentar la declaración** o acceder a su expediente →
  redirigir a `https://sede.agenciatributaria.gob.es`.
- Si pregunta por **pagos fraccionados del IRPF** (Modelo 130/131) →
  **fiscalidad-irpf-autonomos**.
- Si pregunta por **indicadores macroeconómicos** (PIB, IPC) → **ine**.
