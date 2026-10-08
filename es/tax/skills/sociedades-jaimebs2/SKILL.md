---
name: sociedades-jaimebs2
title: Fiscalidad -- Impuesto de Sociedades
description: 'Use when the user asks about corporate tax in Spain (Impuesto de Sociedades): who must pay it (SL, SA, cooperatives, foundations), tax rates (general 25%, reduced rates), annual filing (Modelo 200), advance payments (Modelo 202), taxable base calculation, deductions (R&D, job creation, Canary Islands incentives), loss carryforwards, accounting obligations, or filing deadlines. Triggers on: ''impuesto de sociedades'', ''impuesto sociedades'', ''modelo 200'', ''modelo 202'', ''IS empresa'', ''tipo impositivo sociedades'', ''declaración sociedad'', ''pago fraccionado sociedad'', ''base imponible sociedad'', ''deducciones I+D+i'', ''compensar pérdidas empresa'', ''sociedad limitada impuestos'', ''SL impuestos'', ''SA impuestos'', ''contabilidad sociedad'', ''resultado contable'', ''ajustes fiscales''.'
author: jaimebs2
author_url: https://github.com/jaimebs2/OpenSpain/tree/main/openspain/skills/fiscalidad/sociedades
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: tax
language: es
---

# Fiscalidad -- Impuesto de Sociedades

Guia completa sobre el Impuesto de Sociedades (IS) en Espana: quien
tributa, a que tipo, como se calcula la base imponible, que modelos se
presentan y las principales deducciones y bonificaciones.

> Esta skill orienta sobre el marco general del IS. **No sustituye
> asesoramiento fiscal profesional.** La contabilidad de sociedades
> requiere un asesor o gestor especializado.

---

## 1. Que es el Impuesto de Sociedades

El Impuesto de Sociedades (IS) es un tributo directo y personal que grava
la renta de las **personas juridicas** (sociedades, asociaciones con
actividad economica, fundaciones, etc.). Es el equivalente al IRPF pero
para entidades con personalidad juridica propia.

Se regula en la **Ley 27/2014, de 27 de noviembre, del Impuesto sobre
Sociedades** (LIS).

### Quien esta obligado a declarar

- Sociedades limitadas (SL / SRL).
- Sociedades anonimas (SA).
- Sociedades laborales.
- Cooperativas.
- Asociaciones y fundaciones con actividad economica.
- Sociedades civiles con objeto mercantil (desde 2016).
- Agrupaciones de interes economico (AIE).
- Uniones temporales de empresas (UTE).
- Entidades no residentes con establecimiento permanente en Espana.

**No** tributan por IS: las personas fisicas (tributan por IRPF),
las comunidades de bienes ni las herencias yacentes.

---

## 2. Tipos impositivos

| Tipo de entidad | Tipo IS |
|---|---|
| **General** (SL, SA, la mayoria) | **25 %** |
| Entidades de nueva creacion (primer periodo con BI positiva y el siguiente) | **15 %** |
| Cooperativas fiscalmente protegidas (resultados cooperativos) | **20 %** |
| Entidades sin fines lucrativos (Ley 49/2002) | **10 %** |
| SOCIMI | **0 %** (con condiciones; 19 % sobre dividendos no distribuidos) |
| Fondos de pensiones | **0 %** |
| Micropymes (cifra de negocios < 1 M EUR, tributacion reducida) | **23 %** |
| Entidades con cifra de negocios < 1 M EUR | **23 %** |

El tipo general del **25 %** es uno de los mas bajos de la UE y se aplica
desde el ejercicio 2015.

### Tipo reducido para nuevas empresas

Las entidades de nueva creacion tributan al **15 %** en el primer periodo
impositivo en que la base imponible sea positiva y en el siguiente. No se
aplica si la actividad ya se realizaba por otra entidad vinculada.

---

## 3. Base imponible: como se calcula

La base imponible del IS parte del **resultado contable** (beneficio o
perdida segun la contabilidad) y se le practican **ajustes fiscales**
(diferencias entre el criterio contable y el fiscal).

```
Base imponible = Resultado contable
                 +/- Ajustes extracontables
                 - Compensacion de bases imponibles negativas
```

### Principales ajustes fiscales

**Ajustes positivos** (aumentan la base imponible):
- Gastos no deducibles fiscalmente: multas y sanciones, donativos y
  liberalidades (salvo los previstos en la ley), gastos de actuaciones
  contrarias al ordenamiento juridico.
- Amortizaciones contables superiores a las fiscalmente admitidas.
- Deterioros de valor no admitidos fiscalmente.
- Retribuciones de fondos propios.

**Ajustes negativos** (reducen la base imponible):
- Exencion por doble imposicion de dividendos (art. 21 LIS).
- Libertad de amortizacion (ERD y otros supuestos).
- Reserva de capitalizacion (art. 25 LIS): reduccion del 10 % del
  incremento de fondos propios, sin limite, si se mantiene 5 anos.
- Reserva de nivelacion (solo micropymes, art. 105 LIS): reduccion
  de hasta el 10 % de la BI con limite de 1 M EUR, a devolver en 5
  anos si no hay perdidas.

---

## 4. Compensacion de bases imponibles negativas (perdidas)

Si una sociedad tiene perdidas en un ejercicio, genera una **base
imponible negativa** (BIN) que puede compensar con beneficios futuros.

- **Sin limite temporal**: las BIN se pueden compensar en ejercicios
  futuros indefinidamente.
- **Limite cuantitativo**: se puede compensar hasta el **70 %** de la
  base imponible previa a la compensacion en cada ejercicio (para
  entidades con cifra de negocios >= 20 M EUR). En todo caso, se
  puede compensar hasta 1 M EUR sin limite porcentual.
- Para entidades con cifra de negocios < 20 M EUR: compensacion
  sin limite porcentual.

---

## 5. Modelo 200 -- Declaracion anual del IS

El **Modelo 200** es la declaracion anual del Impuesto de Sociedades.

### Datos clave

| Concepto | Detalle |
|---|---|
| **Que declara** | Resultado del ejercicio, ajustes fiscales, base imponible, cuota, deducciones |
| **Periodo** | Ejercicio economico (normalmente coincide con el ano natural: 1 ene - 31 dic) |
| **Plazo** | **25 dias naturales siguientes a los 6 meses posteriores al cierre del ejercicio**. Para ejercicio = ano natural: **1-25 de julio** del ano siguiente |
| **Presentacion** | Obligatoriamente electronica (certificado digital) |
| **Quien presenta** | Todas las entidades sujetas al IS, incluso sin actividad (mientras no se disuelvan) |

URL: `https://sede.agenciatributaria.gob.es/Sede/procedimientoini/GE04.shtml`

### Documentacion necesaria

Para cumplimentar el Modelo 200 se necesitan:
- Cuentas anuales aprobadas (balance, cuenta de perdidas y ganancias,
  memoria).
- Libro diario y libro de inventarios.
- Conciliacion del resultado contable con la base imponible.
- Detalle de deducciones y bonificaciones aplicadas.

---

## 6. Modelo 202 -- Pagos fraccionados

Los **pagos fraccionados** son anticipos a cuenta del IS que se ingresan
tres veces al ano.

### Plazos

| Periodo | Plazo de presentacion |
|---|---|
| 1P | 1-20 **abril** |
| 2P | 1-20 **octubre** |
| 3P | 1-20 **diciembre** |

### Quien esta obligado

Todas las entidades cuyo ultimo Modelo 200 presentado tuviera
**cuota integra positiva** (casilla correspondiente > 0). Si el ultimo IS
dio resultado cero o negativo, no hay obligacion de presentar el 202
(pero conviene verificarlo cada ejercicio).

### Calculo (modalidad general, art. 40.2 LIS)

```
Pago fraccionado = 18 % x Cuota integra del ultimo IS presentado
                   - Retenciones e ingresos a cuenta
                   - Pagos fraccionados anteriores del ejercicio
```

### Calculo (modalidad alternativa, art. 40.3 LIS)

Obligatoria para grandes empresas (cifra de negocios > 6 M EUR en los
12 meses anteriores al inicio del periodo impositivo):

```
Pago fraccionado = Porcentaje x Base imponible de los 3, 9 u 11 meses
                   transcurridos del ejercicio en curso
```

El porcentaje es 5/7 del tipo de gravamen (para el 25 %: 17,86 %).

---

## 7. Principales deducciones y bonificaciones

### Deducciones por actividades

| Deduccion | Porcentaje |
|---|---|
| **I+D** (investigacion y desarrollo) | 25 % (42 % si supera la media de los 2 anos anteriores) |
| **Innovacion tecnologica** (IT) | 12 % |
| **Producciones cinematograficas** (produccion espanola) | 30 % (primer millon) / 25 % (resto) |
| **Creacion de empleo** (contratacion indefinida de trabajadores con discapacidad) | 9.000-12.000 EUR/persona |
| **Donativos** (Ley 49/2002) | 40 % (fidelizacion: 50 %) |

### Incentivos para empresas de reducida dimension (ERD)

Aplicable a entidades con cifra de negocios < 10 M EUR:
- Libertad de amortizacion para inversiones generadoras de empleo.
- Amortizacion acelerada (doble del coeficiente lineal maximo).
- Perdidas por deterioro de deudores: deduccion global del 1 % de
  deudores al cierre.
- Reserva de nivelacion (reduccion hasta 1 M EUR, solo micropymes
  con CN < 1 M EUR).

### Regimenes especiales Canarias (ZEC, REF)

- **ZEC** (Zona Especial Canaria): tipo reducido del 4 % para
  entidades que cumplan requisitos de creacion de empleo e inversion.
- **REF** (Regimen Economico y Fiscal de Canarias): reserva para
  inversiones en Canarias (RIC), bonificacion por produccion de
  bienes corporales.

---

## 8. Contabilidad obligatoria

Las sociedades estan obligadas a llevar contabilidad ajustada al
**Plan General de Contabilidad** (PGC) y al Codigo de Comercio:

### Libros obligatorios

- **Libro diario**: registra todas las operaciones dia a dia.
- **Libro de inventarios y cuentas anuales**: incluye el balance
  inicial, balances trimestrales de comprobacion y las cuentas anuales.
- **Libro de actas**: acuerdos de la junta general y del organo de
  administracion.
- **Libro registro de socios** (SL) o **libro registro de acciones
  nominativas** (SA).

Los libros deben legalizarse en el **Registro Mercantil** (plazo: 4
meses desde el cierre del ejercicio).

Las cuentas anuales deben aprobarse en junta general (plazo: 6 meses
desde el cierre) y depositarse en el Registro Mercantil (plazo: 1 mes
desde la aprobacion).

### Plan General de Contabilidad

- **PGC completo**: para sociedades que no cumplan los requisitos
  para el abreviado.
- **PGC PYMES**: para entidades que durante 2 ejercicios consecutivos
  no superen 2 de estos 3 limites: activo 4 M EUR, cifra de negocios
  8 M EUR, 50 empleados.

---

## 9. Plazos y calendario

| Obligacion | Plazo | Modelo |
|---|---|---|
| Pago fraccionado 1P | 1-20 abril | 202 |
| Pago fraccionado 2P | 1-20 octubre | 202 |
| Pago fraccionado 3P | 1-20 diciembre | 202 |
| Declaracion anual (ejercicio = ano natural) | 1-25 julio | 200 |
| Deposito de cuentas anuales en Registro Mercantil | 1 mes tras aprobacion (habitual: julio-agosto) | -- |

Calendario fiscal de la AEAT:
`https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026.html`

---

## 10. Resumen rapido

```
IMPUESTO DE SOCIEDADES (IS):
  Tipo general: 25 %
  Tipo nuevas empresas: 15 %

DECLARACION ANUAL:
  Modelo 200 → julio (ejercicio = ano natural)
  Base imponible = resultado contable +/- ajustes

PAGOS FRACCIONADOS:
  Modelo 202 → abril, octubre, diciembre
  18 % de la cuota del IS anterior (modalidad general)

DEDUCCIONES PRINCIPALES:
  I+D+i: 25-42 % / IT: 12 %
  Reserva de capitalizacion: 10 % incremento fondos propios
  ERD: amortizacion acelerada, deterioro global, reserva nivelacion

CONTABILIDAD:
  PGC (o PGC PYMES) + legalizacion libros en Registro Mercantil
  Cuentas anuales: aprobar en 6 meses, depositar en RM en 1 mes mas
```

---

## Cuando NO usar esta skill

- Si pregunta por obligaciones de **autonomos persona fisica** (IRPF,
  IVA trimestral, alta censal) -> **fiscalidad-autonomos**.
- Si pregunta por **IVA** (tipos, modelos 303/390, regimenes) ->
  **fiscalidad-iva**.
- Si pregunta por **IRPF pagos fraccionados de autonomos** (modelos
  130/131, gastos deducibles del autonomo) -> **fiscalidad-irpf-autonomos**.
- Si pregunta por la **Declaracion de la Renta** de un asalariado
  (tramos, borrador, deducciones personales) -> **fiscalidad-irpf-asalariados**.
- Si pregunta por **retenciones** que la sociedad practica a empleados o
  profesionales (modelos 111, 115) -> **fiscalidad-retenciones**.
- Si pregunta por **estadisticas de recaudacion** o datos agregados
  de la AEAT -> **aeat**.
- Si pregunta sobre **como crear una empresa** (tramites de
  constitucion) -> **emprendimiento-crear-empresa**.
