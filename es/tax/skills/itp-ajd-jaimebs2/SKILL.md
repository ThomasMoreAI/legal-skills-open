---
name: itp-ajd-jaimebs2
title: Fiscalidad -- ITP y AJD (Transmisiones Patrimoniales y Actos Juridicos Documentados)
description: 'Use when the user asks about Transfer Tax or Stamp Duty in Spain (Impuesto de Transmisiones Patrimoniales y Actos Juridicos Documentados, ITP-AJD): buying a second-hand property (TPO), mortgage stamp duty (AJD), corporate transactions (OS), tax rates by region, who pays, Modelo 600, Modelo 620 (used vehicles), IVA/TPO incompatibility rule, filing deadlines (30 business days). Triggers on: ''transmisiones patrimoniales'', ''ITP'', ''AJD'', ''actos juridicos documentados'', ''comprar piso segunda mano impuesto'', ''impuesto compraventa vivienda'', ''modelo 600'', ''modelo 620'', ''transferencia coche impuesto'', ''impuesto hipoteca'', ''TPO'', ''operaciones societarias'', ''cuanto se paga por comprar un piso usado'', ''ITP vivienda'', ''tipo ITP comunidad'', ''impuesto escritura'', ''impuesto notario'', ''transmision vehiculo usado''.'
author: jaimebs2
author_url: https://github.com/jaimebs2/OpenSpain/tree/main/openspain/skills/fiscalidad/itp-ajd
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: tax
language: es
---

# Fiscalidad -- ITP y AJD (Transmisiones Patrimoniales y Actos Juridicos Documentados)

Guia completa sobre el Impuesto de Transmisiones Patrimoniales y Actos
Juridicos Documentados: cuando se paga, cuanto, quien paga, y las
diferencias por comunidad autonoma.

> **Competencia autonomica**: cada CCAA fija sus propios tipos
> impositivos dentro de los margenes legales. Esta skill explica el
> marco general y los rangos habituales.

> **No sustituye asesoramiento fiscal profesional.**

---

## 1. Que es el ITP-AJD

El ITP-AJD es un impuesto indirecto que grava tres tipos de operaciones
distintas (son tres impuestos en uno):

| Modalidad | Que grava |
|---|---|
| **TPO** (Transmisiones Patrimoniales Onerosas) | Transmisiones de bienes y derechos entre particulares (no empresarios) |
| **AJD** (Actos Juridicos Documentados) | Documentos notariales, mercantiles y administrativos |
| **OS** (Operaciones Societarias) | Constitucion, ampliacion de capital, disolucion de sociedades |

Se regula en el **Real Decreto Legislativo 1/1993** (Texto Refundido) y
el **Real Decreto 828/1995** (Reglamento).

---

## 2. TPO -- Transmisiones Patrimoniales Onerosas

### Cuando se aplica TPO

- **Compraventa de vivienda de segunda mano** (entre particulares).
- Compraventa de **vehiculos usados** entre particulares.
- Transmision de otros bienes y derechos entre no empresarios.
- **Arrendamientos** (si no estan sujetos a IVA).

### Regla de incompatibilidad IVA/TPO

| Vendedor | Impuesto aplicable |
|---|---|
| **Particular** (no empresario) | **TPO** |
| **Empresario o profesional** | **IVA** (generalmente 21 %; 10 % vivienda nueva) |

Las dos figuras son **incompatibles**: una operacion tributa por IVA o por
TPO, nunca por ambos.

**Excepcion**: entregas de inmuebles exentas de IVA (viviendas de segunda
entrega por empresario) tributan por TPO, salvo renuncia a la exencion.

### Tipos impositivos TPO (vivienda)

Los tipos los fija cada CCAA. Rangos habituales:

| Concepto | Rango tipico |
|---|---|
| Vivienda general | **6-10 %** (segun CCAA) |
| Vivienda habitual jovenes / familias numerosas | **4-6 %** (tipo reducido en muchas CCAA) |
| Vivienda protegida (VPO) | **4 %** (tipo reducido habitual) |
| Vehiculos usados | **4-8 %** (sobre valor de tablas de Hacienda) |
| Bienes muebles en general | **4 %** |

### Ejemplos orientativos por CCAA (tipo general vivienda)

| CCAA | Tipo TPO vivienda |
|---|---|
| Madrid | 6 % |
| Cataluna | 10 % |
| Andalucia | 7 % |
| Comunidad Valenciana | 10 % |
| Pais Vasco | 4-7 % (segun territorio) |
| Galicia | 9 % |
| Castilla y Leon | 8 % |

**Estas cifras son orientativas y pueden cambiar.** Verificar la
normativa vigente de la CCAA.

### Quien paga el TPO

El **comprador** o adquirente.

### Base imponible

El **valor de referencia del Catastro** (desde 2022) o, si no existe,
el mayor entre el valor declarado y el valor de mercado. En vehiculos
usados, se aplican las **tablas de valoracion** publicadas anualmente
por la AEAT.

---

## 3. AJD -- Actos Juridicos Documentados

### Documentos notariales (cuota variable)

Se aplica cuando se otorgan escrituras publicas que tengan por objeto
cantidad o cosa valuable, sean inscribibles en un registro publico y
no esten sujetas a TPO ni a OS.

Ejemplos principales:
- **Escritura de hipoteca** (desde noviembre 2018, paga el **banco**).
- Escritura de obra nueva y division horizontal.
- Escritura de agrupacion o segregacion de fincas.
- Escritura de compraventa sujeta a IVA (al ser incompatible con TPO,
  la compra de vivienda nueva tributa por IVA + AJD).

### Tipos AJD (cuota variable)

| Concepto | Rango tipico |
|---|---|
| AJD documentos notariales | **0,5-1,5 %** (segun CCAA) |
| Hipotecas (desde 11/2018, paga el banco) | 0,5-1,5 % |

### Documentos notariales (cuota fija)

- Papel timbrado: 0,30 EUR por pliego o 0,15 EUR por folio.

### Documentos mercantiles

- Letras de cambio, pagares: escala segun importe.

---

## 4. OS -- Operaciones Societarias

| Operacion | Tipo |
|---|---|
| Constitucion de sociedad | **1 %** (exento desde 2010 para constituciones y ampliaciones) |
| Ampliacion de capital | **1 %** (exento desde 2010) |
| Disolucion de sociedad | **1 %** |
| Aportaciones no dinerarias | **1 %** (exento en muchos casos) |

Desde la reforma de 2010, las constituciones y ampliaciones de capital
estan **exentas** de OS, lo que hace este impuesto poco relevante para
nuevas empresas.

---

## 5. Modelo 600 y Modelo 620

### Modelo 600

Es el modelo de autoliquidacion general del ITP-AJD. Se usa para:
- Compraventa de inmuebles (TPO).
- Escrituras sujetas a AJD.
- Operaciones societarias.

Se presenta ante la **hacienda autonomica** (no la AEAT), en la CCAA
donde radique el inmueble.

### Modelo 620

Modelo especifico para la transmision de **vehiculos usados** entre
particulares. En muchas CCAA se puede presentar directamente en la
DGT al hacer la transferencia.

### Plazo de presentacion

**30 dias habiles** desde el devengo (firma de la escritura, contrato
de compraventa, etc.).

---

## 6. Compraventa de vivienda: resumen fiscal

### Vivienda de segunda mano (entre particulares)

| Concepto | Impuesto |
|---|---|
| Precio de compra | **TPO** (6-10 % segun CCAA) |
| Escritura (si procede) | Incluido en TPO |
| Hipoteca | **AJD** (0,5-1,5 %, paga el banco) |

### Vivienda nueva (de promotor/empresario)

| Concepto | Impuesto |
|---|---|
| Precio de compra | **IVA** (10 % vivienda, 21 % otros inmuebles) |
| Escritura de compraventa | **AJD** (0,5-1,5 %) |
| Hipoteca | **AJD** (0,5-1,5 %, paga el banco) |

---

## 7. Vehiculos usados entre particulares

- Impuesto: **TPO**.
- Modelo: **620** (o 600 segun la CCAA).
- Tipo: **4-8 %** segun la CCAA.
- Base imponible: **valor de tablas** de Hacienda (publicadas anualmente),
  no el precio pactado si este es inferior.
- Plazo: 30 dias habiles.
- Necesario para hacer la **transferencia en la DGT**.

---

## 8. Resumen rapido

```
ITP-AJD — TRES IMPUESTOS EN UNO:

TPO (Transmisiones Patrimoniales Onerosas):
  Compraventa entre particulares
  Vivienda 2.a mano: 6-10 % (segun CCAA)
  Vehiculos usados: 4-8 %
  Paga: el comprador
  Modelo: 600 (inmuebles) / 620 (vehiculos)

AJD (Actos Juridicos Documentados):
  Escrituras publicas (no sujetas a TPO)
  Hipotecas: 0,5-1,5 % (paga el banco desde 2018)
  Compra vivienda nueva: IVA 10 % + AJD 0,5-1,5 %
  Modelo: 600

OS (Operaciones Societarias):
  Constitucion/ampliacion: exento desde 2010
  Disolucion: 1 %

PLAZO: 30 dias habiles desde el devengo
COMPETENCIA: autonomica (se presenta en la hacienda de la CCAA)

REGLA CLAVE: IVA y TPO son incompatibles
  Particular vende → TPO
  Empresario vende → IVA
```

---

## Cuando NO usar esta skill

- Si pregunta por **herencias o donaciones** (ISD) ->
  **fiscalidad-sucesiones-donaciones**.
- Si pregunta por **IVA** (tipos, modelo 303, regimenes) ->
  **fiscalidad-iva**.
- Si pregunta por **plusvalia municipal** al vender un inmueble ->
  **fiscalidad-impuestos-locales**.
- Si pregunta por **IBI** u otros impuestos locales ->
  **fiscalidad-impuestos-locales**.
- Si pregunta por el **proceso de compraventa de vivienda** (no solo
  fiscal) -> **vivienda-compraventa**.
- Si pregunta por **transferencia de vehiculos en la DGT** (tramite
  administrativo) -> **dgt-trafico**.
- Si pregunta por **IRPF** por ganancia patrimonial al vender ->
  **fiscalidad-irpf-asalariados**.
- Si pregunta por obligaciones de **autonomos** -> **fiscalidad-autonomos**.
- Si pregunta por **estadisticas de recaudacion** -> **aeat**.
