---
name: impuestos-locales-jaimebs2
title: Fiscalidad -- Impuestos Locales (IBI, IAE, Plusvalia, IVTM)
description: 'Use when the user asks about local taxes in Spain (impuestos locales, impuestos municipales): IBI (Impuesto sobre Bienes Inmuebles, property tax), IAE (Impuesto sobre Actividades Economicas, business tax), plusvalia municipal (IIVTNU, tax on increase in urban land value), IVTM (vehicle tax, sello del coche), how they are calculated, who pays, municipal competence, common local fees (basura, vado, terrazas). Triggers on: ''IBI'', ''impuesto bienes inmuebles'', ''valor catastral'', ''plusvalia municipal'', ''IIVTNU'', ''vender piso plusvalia'', ''IAE'', ''impuesto actividades economicas'', ''IVTM'', ''impuesto circulacion'', ''sello del coche'', ''impuesto vehiculo'', ''impuestos municipales'', ''impuestos locales'', ''tasa basura'', ''recibo IBI'', ''exencion IAE'', ''bonificacion vehiculo electrico''.'
author: jaimebs2
author_url: https://github.com/jaimebs2/OpenSpain/tree/main/openspain/skills/fiscalidad/impuestos-locales
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: tax
language: es
---

# Fiscalidad -- Impuestos Locales (IBI, IAE, Plusvalia, IVTM)

Guia completa sobre los cuatro impuestos locales principales en Espana:
IBI, IAE, plusvalia municipal e IVTM. Estos impuestos los gestionan los
ayuntamientos y sus tipos varian de un municipio a otro.

> **Competencia municipal**: cada ayuntamiento fija sus tipos impositivos
> dentro de las horquillas legales. Esta skill explica el marco general
> establecido en la Ley de Haciendas Locales.

> **No sustituye asesoramiento fiscal profesional.**

---

## 1. IBI -- Impuesto sobre Bienes Inmuebles

El IBI es el principal impuesto local. Grava la titularidad de bienes
inmuebles (pisos, casas, locales, garajes, terrenos).

### Quien paga

El **propietario** (o titular de un derecho real de usufructo, superficie
o concesion) a 1 de enero de cada ano. Si vendes un inmueble en marzo,
el IBI de ese ano lo paga el vendedor.

### Como se calcula

```
Cuota IBI = Valor catastral x Tipo impositivo municipal
```

### Valor catastral

- Lo fija el **Catastro** (Direccion General del Catastro).
- No debe superar el valor de mercado.
- Se revisa periodicamente (ponencias de valores).
- Se puede consultar en `https://www.sedecatastro.gob.es`

### Tipos impositivos (horquillas legales)

| Tipo de inmueble | Tipo minimo | Tipo maximo |
|---|---|---|
| **Urbano** | 0,4 % | 1,10 % |
| **Rustico** | 0,3 % | 0,90 % |
| **Especiales** (autopistas, puertos, centrales) | 0,4 % | 1,30 % |

### Ejemplo

Piso con valor catastral de 100.000 EUR en un municipio con tipo del
0,65 %: IBI = 650 EUR/ano.

### Bonificaciones habituales

- **Familia numerosa**: reduccion del 50-90 % (segun ordenanza municipal).
- **Vivienda de proteccion oficial (VPO)**: 50 % durante 3 anos.
- **Instalaciones de energia solar**: hasta 50 % (cada vez mas municipios).
- **Obras de rehabilitacion**: hasta 90 % durante las obras (max. 3 anos).

### Pago

- Periodo voluntario: segun calendario del ayuntamiento (varia por
  municipio; habitual entre septiembre y noviembre).
- Muchos ayuntamientos permiten **domiciliacion** y **fraccionamiento**.
- En via ejecutiva: recargo del 5-20 % + intereses de demora.

---

## 2. IAE -- Impuesto sobre Actividades Economicas

El IAE grava el ejercicio de actividades empresariales, profesionales o
artisticas.

### Quien paga

Solo las personas juridicas (empresas) con **cifra de negocios neta
>= 1.000.000 EUR** en el penultimo ano anterior.

### Quien NO paga (exentos)

- **Personas fisicas** (autonomos): siempre exentos de IAE.
- **Empresas con cifra de negocios < 1 M EUR**: exentas.
- Entidades de nueva creacion: exentas los **2 primeros ejercicios**.
- Administraciones publicas, organismos autonomos, entidades sin fines
  lucrativos (Ley 49/2002).

### Calculo

Se basa en las **tarifas del IAE** (cuotas fijas por actividad, segun
epigrafe) ajustadas con:
- **Coeficiente de ponderacion**: segun cifra de negocios (1,29 a 1,35).
- **Coeficiente de situacion**: segun la calle o zona del municipio.

### Matricula

Aunque esten exentos, los obligados a declarar por el IS o IRPF deben
darse de **alta en la matricula** del IAE (elegir epigrafe en el modelo
036/037). Esto no implica pago.

---

## 3. Plusvalia Municipal (IIVTNU)

El **Impuesto sobre el Incremento de Valor de los Terrenos de Naturaleza
Urbana** (IIVTNU), conocido como "plusvalia municipal", grava el
incremento de valor del suelo urbano cuando se transmite.

### Cuando se paga

- **Venta** de un inmueble urbano.
- **Herencia** (paga el heredero; plazo 6 meses desde el fallecimiento).
- **Donacion** (paga el donatario; plazo 30 dias habiles).

### Quien paga

| Transmision | Sujeto pasivo |
|---|---|
| Venta (onerosa) | **Vendedor** (transmitente) |
| Herencia / donacion (lucrativa) | **Adquirente** (heredero / donatario) |

### Metodos de calculo (desde noviembre 2021)

Tras las sentencias del Tribunal Constitucional, existen **dos metodos**
y el contribuyente puede elegir el mas favorable:

#### Metodo objetivo (por coeficientes)

```
Base imponible = Valor catastral del suelo x Coeficiente (segun anos de tenencia)
```

| Anos de tenencia | Coeficiente maximo |
|---|---|
| 1 | 0,14 |
| 2 | 0,13 |
| 3 | 0,15 |
| 4 | 0,17 |
| 5 | 0,17 |
| 6 | 0,16 |
| 7 | 0,12 |
| 8 | 0,10 |
| 9 | 0,09 |
| 10 | 0,08 |
| 11 | 0,08 |
| 12 | 0,08 |
| 13 | 0,08 |
| 14 | 0,10 |
| 15 | 0,12 |
| 16 | 0,16 |
| 17 | 0,20 |
| 18 | 0,26 |
| 19 | 0,36 |
| >= 20 | 0,45 |

Los ayuntamientos pueden reducir estos coeficientes.

#### Metodo real (por plusvalia efectiva)

```
Base imponible = (Valor transmision - Valor adquisicion) x (% valor catastral del suelo / valor catastral total)
```

Se toma la plusvalia real y se prorratea por la parte de suelo.

### Importante: si no hay incremento, no se paga

Desde la sentencia del TC de 2021, si la transmision genera una
**minusvalia** (se vende por menos de lo que se compro), **no se paga**
plusvalia municipal. El contribuyente puede acreditar la inexistencia
de incremento con las escrituras de compra y venta.

### Tipo impositivo

Maximo legal: **30 %** sobre la base imponible. Cada ayuntamiento fija
su tipo (habitualmente entre el 20 % y el 30 %).

---

## 4. IVTM -- Impuesto sobre Vehiculos de Traccion Mecanica

Conocido popularmente como el "sello del coche" o "impuesto de
circulacion".

### Quien paga

El **titular del vehiculo** a 1 de enero de cada ano. Si compras un
coche en marzo, ese ano paga el vendedor.

### Cuotas minimas (Ley de Haciendas Locales)

Los ayuntamientos pueden aplicar un coeficiente de hasta **2** sobre
estas cuotas minimas:

| Tipo de vehiculo | Cuota minima (EUR) |
|---|---|
| Turismo < 8 CV fiscales | 12,62 |
| Turismo 8-11,99 CV | 34,08 |
| Turismo 12-15,99 CV | 71,94 |
| Turismo 16-19,99 CV | 89,61 |
| Turismo >= 20 CV | 112,00 |
| Motocicleta < 125 cc | 4,42 |
| Motocicleta 125-250 cc | 7,57 |
| Motocicleta 250-500 cc | 15,15 |
| Motocicleta 500-1000 cc | 30,29 |
| Motocicleta > 1000 cc | 60,58 |

### Bonificaciones habituales

- **Vehiculos electricos**: hasta **75 %** de bonificacion en muchos
  municipios.
- **Vehiculos hibridos**: hasta 50-75 % (segun municipio).
- **Vehiculos GLP/GNC**: hasta 50 % en algunos municipios.
- **Vehiculos historicos** (mas de 25 anos): hasta 100 % en algunos
  municipios.
- **Discapacidad**: exencion para vehiculos de personas con
  discapacidad >= 33 % (adaptados o para su uso exclusivo).

### Baja del vehiculo

Si das de baja un vehiculo (baja definitiva en la DGT), puedes
solicitar la **devolucion proporcional** del IVTM del ano en curso
(prorrata trimestral, segun normativa de cada ayuntamiento).

---

## 5. Tasas municipales habituales

Ademas de los cuatro impuestos, los ayuntamientos cobran **tasas** por
servicios publicos:

| Tasa | Que cubre |
|---|---|
| **Basura** (recogida de residuos) | Servicio de recogida y tratamiento |
| **Vado** (paso de vehiculos) | Reserva de espacio en la via publica |
| **Terrazas** | Ocupacion de via publica por hosteleria |
| **Licencia de obras** | Autorizacion municipal para reformas |
| **ICIO** (Impuesto sobre Construcciones, Instalaciones y Obras) | Obras que requieran licencia (hasta 4 % del coste) |

---

## 6. Marco legal

Los impuestos locales se regulan en el **Real Decreto Legislativo 2/2004**
(Texto Refundido de la Ley Reguladora de las Haciendas Locales):

`https://www.boe.es/buscar/act.php?id=BOE-A-2004-4214`

Cada ayuntamiento aprueba sus **ordenanzas fiscales** (normalmente
disponibles en el BOP o la web del ayuntamiento) donde fija los tipos,
bonificaciones y plazos dentro de los limites legales.

---

## 7. Resumen rapido

```
IMPUESTOS LOCALES — COMPETENCIA MUNICIPAL:

IBI (Impuesto sobre Bienes Inmuebles):
  Paga: propietario a 1 de enero
  Calculo: valor catastral x tipo (0,4-1,10 % urbano)
  Bonificaciones: familia numerosa, energia solar, VPO

IAE (Impuesto sobre Actividades Economicas):
  Solo empresas con facturacion >= 1 M EUR
  Autonomos: siempre exentos
  Nuevas empresas: exentas 2 primeros ejercicios

PLUSVALIA MUNICIPAL (IIVTNU):
  Paga: vendedor (venta) o adquirente (herencia/donacion)
  Dos metodos: objetivo (coeficientes) o real (plusvalia efectiva)
  Si no hay incremento real → no se paga
  Tipo: hasta 30 %

IVTM ("sello del coche"):
  Paga: titular a 1 de enero
  Bonificaciones: electrico 75 %, hibrido 50-75 %, discapacidad exento
```

---

## Cuando NO usar esta skill

- Si pregunta por **IBI y quiere consultar el valor catastral** en
  detalle -> **catastro**.
- Si pregunta por **ITP** (compraventa de vivienda entre particulares)
  -> **fiscalidad-itp-ajd**.
- Si pregunta por **herencias/donaciones** (ISD) ->
  **fiscalidad-sucesiones-donaciones**.
- Si pregunta por el **epigrafe IAE** al darse de alta como autonomo
  -> **fiscalidad-autonomos** (ahi se explica el alta censal).
- Si pregunta por **transferencia de vehiculos** (tramite en la DGT)
  -> **dgt-trafico**.
- Si pregunta por **IRPF, IVA, Impuesto de Sociedades** -> usar la
  skill de fiscalidad correspondiente.
- Si pregunta por **estadisticas de recaudacion** -> **aeat**.
