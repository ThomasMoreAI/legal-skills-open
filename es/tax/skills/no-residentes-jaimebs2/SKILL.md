---
name: no-residentes-jaimebs2
title: Fiscalidad -- No Residentes (IRNR)
description: 'Use when the user asks about taxation for non-residents in Spain (IRNR, Impuesto sobre la Renta de No Residentes): who is considered a non-resident (183-day rule), IRNR with and without permanent establishment, Modelo 210, Modelo 720 (foreign assets declaration), double taxation treaties, imputed income for non-residents with Spanish property, withholding taxes on dividends/interest/royalties, fiscal representative, Beckham Law (special impatriate regime, art. 93 LIRPF), digital nomad visa taxation. Triggers on: ''no residente fiscal'', ''IRNR'', ''modelo 210'', ''modelo 720'', ''Ley Beckham'', ''regimen impatriados'', ''doble imposicion'', ''extranjero con piso en Espana'', ''impuesto no residente'', ''residencia fiscal 183 dias'', ''nomada digital impuestos'', ''representante fiscal'', ''tributar como no residente'', ''bienes en el extranjero'', ''retencion no residente'', ''alquiler no residente'', ''vender piso no residente''.'
author: jaimebs2
author_url: https://github.com/jaimebs2/OpenSpain/tree/main/openspain/skills/fiscalidad/no-residentes
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: tax
language: es
---

# Fiscalidad -- No Residentes (IRNR)

Guia completa sobre la fiscalidad para no residentes en Espana: quien es
no residente fiscal, que impuestos paga, modelos a presentar, convenios
de doble imposicion, y regimenes especiales como la Ley Beckham.

> Materia tecnica. **Se recomienda siempre consultar a un asesor
> especializado en fiscalidad internacional.**

> **No sustituye asesoramiento fiscal profesional.**

---

## 1. Quien es no residente fiscal en Espana

Una persona fisica es **residente fiscal** en Espana si cumple
**cualquiera** de estos criterios:

- Permanece **mas de 183 dias** en territorio espanol durante el ano
  natural (no es necesario que sean consecutivos).
- Tiene en Espana el **nucleo principal o base de sus actividades o
  intereses economicos**, directa o indirectamente.
- Presuncion (salvo prueba en contrario): su conyuge no separado
  legalmente e hijos menores residen habitualmente en Espana.

Si **no cumple** ninguno de estos criterios, es **no residente fiscal**
y tributa por el IRNR en lugar del IRPF.

### Residencia fiscal de personas juridicas

Una entidad es residente en Espana si:
- Se constituyo conforme a las leyes espanolas.
- Tiene su domicilio social en Espana.
- Tiene su sede de direccion efectiva en Espana.

---

## 2. El IRNR (Impuesto sobre la Renta de No Residentes)

### Sin establecimiento permanente

La mayoria de no residentes con rentas en Espana tributan **sin
establecimiento permanente**. Se grava cada renta de forma **separada**
(no se pueden compensar unas con otras):

| Tipo de renta | Tipo impositivo |
|---|---|
| **Rendimientos del trabajo** | 24 % (19 % si residente en otro pais UE/EEE) |
| **Pensiones** | Escala especifica (8-40 %) |
| **Intereses, dividendos, canones** | 19 % |
| **Ganancias patrimoniales** (venta inmueble, acciones) | 19 % |
| **Imputacion de rentas inmobiliarias** (inmueble no alquilado) | 19 % (UE/EEE) o 24 % sobre el 1,1-2 % del valor catastral |
| **Alquileres** | 24 % (19 % UE/EEE) sobre ingreso bruto (sin deducciones, salvo UE/EEE con gastos deducibles) |

### Con establecimiento permanente

Si el no residente opera a traves de un **establecimiento permanente**
(oficina, sucursal, fabrica, obra > 6 meses), tributa como una sociedad
espanola al **25 %** sobre el beneficio neto del establecimiento.

---

## 3. Modelo 210 -- Autoliquidacion del IRNR

El **Modelo 210** es la declaracion del IRNR para no residentes sin
establecimiento permanente.

### Datos clave

| Concepto | Detalle |
|---|---|
| **Que declara** | Cada tipo de renta por separado |
| **Periodicidad** | Varia segun el tipo de renta (ver tabla abajo) |
| **Presentacion** | Telematica (certificado digital o Cl@ve) o en papel |
| **Representante** | Puede necesitar un representante fiscal en Espana |

### Plazos de presentacion

| Renta | Plazo |
|---|---|
| **Imputacion de rentas inmobiliarias** | Ano natural siguiente (1 ene - 31 dic) |
| **Ganancias patrimoniales** (sin retencion) | 3 meses desde la transmision |
| **Rentas con retencion** | Del 1 al 20 del mes siguiente al trimestre |
| **Rentas sin retencion** (salvo las anteriores) | Del 1 al 20 del mes siguiente al trimestre |

URL: `https://sede.agenciatributaria.gob.es/Sede/no-residentes.html`

---

## 4. Modelo 720 -- Declaracion de bienes en el extranjero

El Modelo 720 es una **declaracion informativa** (sin pago) obligatoria
para **residentes fiscales** en Espana que tengan bienes y derechos en
el extranjero que superen determinados umbrales.

**Atencion**: este modelo afecta a los **residentes**, no a los no
residentes. Se incluye aqui porque es relevante para expatriados que
se convierten en residentes fiscales al mudarse a Espana.

### Que se declara

Tres bloques, cada uno con umbral independiente de **50.000 EUR**:

| Bloque | Que incluye |
|---|---|
| **Cuentas bancarias** | Cuentas en entidades financieras en el extranjero |
| **Valores y derechos** | Acciones, fondos, seguros, rentas vitalicias en el extranjero |
| **Inmuebles y derechos** | Bienes inmuebles y derechos sobre ellos en el extranjero |

Solo se declara el bloque cuyo saldo/valor supere 50.000 EUR. En anos
sucesivos, solo si el valor ha aumentado mas de 20.000 EUR respecto a
la ultima declaracion.

### Plazo

Del **1 de enero al 31 de marzo** del ano siguiente.

### Sanciones

Tras la sentencia del TJUE (2022), el regimen sancionador
desproporcionado fue anulado. Las sanciones actuales son las generales
de la LGT (no las especificas que antes establecio la norma).

---

## 5. Convenios de doble imposicion (CDI)

Espana tiene firmados convenios de doble imposicion con mas de **90
paises**. Estos convenios:

- **Evitan la doble imposicion**: determinan que pais tiene derecho
  a gravar cada tipo de renta.
- **Reducen retenciones**: los tipos de retencion sobre dividendos,
  intereses y canones suelen ser menores en el CDI que en la norma
  interna.
- **Establecen la residencia fiscal** en caso de conflicto (tie-
  breaker rules).

### Ejemplos de tipos reducidos habituales en CDI

| Renta | Tipo interno | Tipo CDI tipico |
|---|---|---|
| Dividendos | 19 % | 10-15 % |
| Intereses | 19 % | 0-10 % |
| Canones (royalties) | 19 % | 0-10 % |

Para aplicar el CDI, el no residente debe **acreditar su residencia
fiscal** en el otro pais (certificado de residencia fiscal emitido por
la autoridad tributaria del pais de residencia).

### Lista de convenios

`https://sede.agenciatributaria.gob.es/Sede/no-residentes/convenios-doble-imposicion.html`

---

## 6. Ley Beckham (Regimen Especial de Impatriados)

### Que es

El regimen especial del art. 93 LIRPF (conocido como "Ley Beckham")
permite a determinados trabajadores que se trasladan a Espana tributar
como **no residentes** durante el ano del traslado y los **5 siguientes**
(total: hasta 6 anos), aunque sean residentes fiscales.

### Ventajas

- Tipo fijo del **24 %** sobre rendimientos del trabajo hasta
  600.000 EUR (47 % sobre el exceso).
- Solo tributan en Espana por las rentas **de fuente espanola**
  (no por la renta mundial).
- No estan obligados a presentar el Modelo 720.

### Requisitos principales

1. No haber sido residente fiscal en Espana en los **5 ejercicios
   anteriores** al desplazamiento.
2. El desplazamiento debe producirse como consecuencia de:
   - Un **contrato de trabajo** (excepto deportistas profesionales,
     desde 2015).
   - La condicion de **administrador** de una entidad (con limites).
   - Actividad **emprendedora** (desde la Ley de Startups 2022).
   - Profesional **altamente cualificado** que preste servicios a
     empresas emergentes.
3. Obtener rentas que no se consideren obtenidas a traves de un
   establecimiento permanente en Espana.

### Como solicitarlo

Modelo 149 (comunicacion de opcion) ante la AEAT, en el plazo de **6
meses** desde el alta en la Seguridad Social o desde el inicio de la
actividad.

---

## 7. No residente con inmueble en Espana

Caso muy frecuente: un no residente que posee una vivienda en Espana
(tipicamente en zona costera).

### Si NO lo alquila

Debe presentar **Modelo 210** anual por **imputacion de rentas
inmobiliarias**:
- Base: 1,1 % o 2 % del valor catastral.
- Tipo: 19 % (UE/EEE) o 24 % (resto).
- Ejemplo: valor catastral 200.000 EUR, tipo 1,1 %: base = 2.200 EUR,
  cuota = 418 EUR (al 19 %).

### Si lo alquila

Debe presentar **Modelo 210** trimestral por los ingresos de alquiler:
- Residente UE/EEE: puede deducir gastos (intereses hipoteca,
  comunidad, IBI, reparaciones...) y tributa al 19 % sobre el
  rendimiento neto.
- No UE/EEE: tributa al 24 % sobre el ingreso **bruto** (sin
  deduccion de gastos).

### Si lo vende

- **IRNR**: 19 % sobre la ganancia patrimonial (valor venta - valor
  adquisicion actualizado).
- **Retencion del 3 %**: el comprador esta obligado a retener e
  ingresar el **3 % del precio de venta** como pago a cuenta del
  IRNR del vendedor no residente (Modelo 211). El vendedor puede
  solicitar la devolucion del exceso presentando el Modelo 210.
- **Plusvalia municipal**: tambien se devenga (ver
  **fiscalidad-impuestos-locales**).

---

## 8. Representante fiscal

Los no residentes que obtengan rentas en Espana pueden necesitar un
**representante fiscal** ante la AEAT:

- **Obligatorio** si operan a traves de establecimiento permanente.
- **Obligatorio** si asi lo requiere la AEAT (requerimiento expreso).
- **Recomendable** en todo caso para gestionar las obligaciones
  tributarias.

El representante actua ante la AEAT en nombre del no residente y es
responsable solidario de las obligaciones tributarias.

---

## 9. Resumen rapido

```
FISCALIDAD NO RESIDENTES:

RESIDENCIA FISCAL:
  183 dias en Espana → residente
  Centro de intereses economicos → residente
  Si no → no residente → tributa por IRNR

IRNR (sin establecimiento permanente):
  Tipos: 24 % (general) / 19 % (UE/EEE, ganancias, dividendos)
  Modelo: 210 (cada renta por separado)

MODELO 720 (bienes en el extranjero):
  Solo para RESIDENTES con bienes fuera > 50.000 EUR por bloque
  Plazo: enero-marzo

CONVENIOS DE DOBLE IMPOSICION:
  90+ paises → reducen retenciones y evitan doble gravamen

LEY BECKHAM (regimen impatriados):
  24 % fijo (hasta 600.000 EUR) durante 6 anos
  Solo rentas de fuente espanola
  Solicitar en 6 meses desde alta en SS (Modelo 149)

NO RESIDENTE CON PISO EN ESPANA:
  No alquilado: imputacion rentas (1,1-2 % valor catastral)
  Alquilado: modelo 210 trimestral
  Venta: 19 % ganancia + retencion 3 % por comprador
```

---

## Cuando NO usar esta skill

- Si el usuario es **residente fiscal** y pregunta por la Declaracion
  de la Renta -> **fiscalidad-irpf-asalariados**.
- Si es **autonomo residente** -> **fiscalidad-autonomos** o
  **fiscalidad-irpf-autonomos**.
- Si pregunta por el **permiso de residencia** (aspecto migratorio,
  no fiscal) -> **extranjeria-residencia**.
- Si pregunta por **IVA** -> **fiscalidad-iva**.
- Si pregunta por **Impuesto de Sociedades** -> **fiscalidad-sociedades**.
- Si pregunta por **herencias de no residentes** -> primero
  **fiscalidad-sucesiones-donaciones** (el ISD tambien afecta a no
  residentes).
- Si pregunta por **plusvalia municipal** al vender ->
  **fiscalidad-impuestos-locales**.
- Si pregunta por **estadisticas de recaudacion** -> **aeat**.
