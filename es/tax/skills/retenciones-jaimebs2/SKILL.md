---
name: retenciones-jaimebs2
title: Fiscalidad -- Retenciones e Ingresos a Cuenta
description: 'Use when the user asks about withholding taxes and payments on account in Spain (retenciones e ingresos a cuenta): who is obliged to withhold (employer, payer), Modelo 111 (withholdings on employment income and professional fees, quarterly), Modelo 115 (withholdings on property rental, quarterly), Modelo 190 (annual summary of withholdings), Modelo 180 (annual summary of rental withholdings), IRPF withholding tables for payroll, professional withholding rate (15%, 7% for new professionals), rental withholding (19%), prize withholding (19%). Triggers on: ''retencion IRPF'', ''modelo 111'', ''modelo 115'', ''modelo 190'', ''modelo 180'', ''retencion nomina'', ''tipo retencion profesional'', ''retencion alquiler'', ''tabla retenciones'', ''ingreso a cuenta'', ''obligado a retener'', ''retencion 15 %'', ''retencion 7 %'', ''declaracion retenciones'', ''resumen anual retenciones'', ''retenciones empleados'', ''cuanto me retienen''.'
author: jaimebs2
author_url: https://github.com/jaimebs2/OpenSpain/tree/main/openspain/skills/fiscalidad/retenciones
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: tax
language: es
---

# Fiscalidad -- Retenciones e Ingresos a Cuenta

Guia completa sobre las retenciones e ingresos a cuenta en Espana:
quien esta obligado a retener, tipos de retencion, modelos a presentar,
y las tablas de retencion del IRPF sobre nominas.

> Esta skill cubre las retenciones desde la perspectiva del **pagador**
> (quien retiene e ingresa). Si eres autonomo y soportas retenciones en
> tus facturas, consulta **fiscalidad-irpf-autonomos**.

> **No sustituye asesoramiento fiscal profesional.**

---

## 1. Que son las retenciones

Las retenciones son **anticipos del IRPF o del IS** que el pagador de
una renta descuenta al perceptor y ingresa directamente en Hacienda.

```
Ejemplo: un profesional factura 1.000 EUR + IVA con 15 % de retencion

  Base: 1.000 EUR
  IVA (21 %): +210 EUR
  Retencion IRPF (15 %): -150 EUR
  Total a cobrar: 1.060 EUR

  El pagador ingresa los 150 EUR a Hacienda (Modelo 111)
  El profesional se los deduce en su Renta (Modelo 100/130)
```

### Quien esta obligado a retener

- **Empresas y profesionales** que pagan rentas sujetas a retencion.
- **Personas fisicas empresarios o profesionales** que pagan
  rendimientos del trabajo, actividades profesionales o alquileres.
- **Entidades** (asociaciones, fundaciones, comunidades de propietarios
  que tienen empleados o alquilan locales).

**Los particulares no retenedores** (empleadores del hogar, por ejemplo)
no tienen obligacion de retener.

---

## 2. Tipos de retencion principales

### Rendimientos del trabajo (nominas)

La retencion sobre nominas depende de:
- Salario bruto anual.
- Situacion personal y familiar (estado civil, hijos, discapacidad).
- Tipo de contrato (fijo, temporal).
- Comunidad autonoma (la escala autonomica influye).

La AEAT publica anualmente las **tablas de retencion** y un algoritmo
de calculo. Tambien ofrece un simulador online:

`https://sede.agenciatributaria.gob.es/Sede/irpf/retenciones-ingresos-cuenta-pagos-fraccionados.html`

### Tipos fijos de retencion

| Concepto | Tipo de retencion |
|---|---|
| **Profesionales** (actividades profesionales) | **15 %** |
| **Profesionales nuevos** (ano de alta y los 2 siguientes) | **7 %** |
| **Alquiler de inmuebles** (urbanos) | **19 %** |
| **Rendimientos del capital mobiliario** (intereses, dividendos) | **19 %** |
| **Premios** (sorteos, concursos) | **19 %** |
| **Administradores de sociedades** | **35 %** (entidades con CN < 100.000 EUR: 19 %) |
| **Cursos, conferencias, seminarios** | **15 %** |
| **Cesion derechos de imagen** | **24 %** |
| **Rendimientos del trabajo en especie** (ingreso a cuenta) | Segun tablas |

### Cuando NO se retiene

- Facturas entre empresarios/profesionales sujetas **solo a IVA**
  (sin componente de actividad profesional). Ejemplo: un autonomo
  empresarial (epigrafe de la seccion 1.a del IAE) no soporta
  retencion en sus facturas.
- Actividades en estimacion objetiva (modulos) que determinen su
  rendimiento neto por ese metodo.
- Arrendamientos de vivienda (solo se retiene en alquiler de
  locales/oficinas, no de vivienda habitual).
- Alquileres <= 900 EUR/ano al mismo arrendador.

---

## 3. Modelo 111 -- Retenciones sobre trabajo y actividades profesionales

### Datos clave

| Concepto | Detalle |
|---|---|
| **Que declara** | Retenciones e ingresos a cuenta sobre rendimientos del trabajo, actividades economicas (profesionales), premios y otras rentas |
| **Periodicidad** | **Trimestral** (mensual si gran empresa, CN > 6.016.000 EUR) |
| **Plazos trimestrales** | 1T: 1-20 abril / 2T: 1-20 julio / 3T: 1-20 octubre / 4T: 1-30 enero |
| **Presentacion** | Telematica (obligatoria para sociedades; personas fisicas pueden usar papel si no son grandes empresas) |

### Quien lo presenta

Toda persona o entidad que haya **practicado retenciones** sobre:
- Nominas de empleados.
- Facturas de profesionales con retencion.
- Premios.

Si en un trimestre no has pagado ninguna renta sujeta a retencion,
**no es obligatorio presentar el 111** (salvo que la AEAT te lo haya
exigido especificamente). Pero es recomendable presentarlo con resultado
cero para evitar requerimientos.

---

## 4. Modelo 115 -- Retenciones sobre alquileres de inmuebles

### Datos clave

| Concepto | Detalle |
|---|---|
| **Que declara** | Retenciones sobre rendimientos de alquiler de inmuebles urbanos |
| **Tipo de retencion** | **19 %** |
| **Periodicidad** | **Trimestral** (mensual si gran empresa) |
| **Plazos trimestrales** | 1T: 1-20 abril / 2T: 1-20 julio / 3T: 1-20 octubre / 4T: 1-30 enero |

### Cuando se presenta

Si alquilas un local, oficina o nave para tu actividad economica y
el arrendador es una persona fisica o entidad sujeta a IRPF/IS, debes
retener el 19 % del alquiler e ingresarlo con el Modelo 115.

### Excepciones (no se retiene)

- Arrendamiento de **vivienda** por empresa para sus empleados.
- Si el arrendador tributa por algun epigrafe del IAE por la actividad
  de alquiler y alguna de sus rentas esta sujeta a retencion del 1 %.
- Alquileres <= 900 EUR anuales al mismo arrendador.

---

## 5. Modelo 190 -- Resumen anual de retenciones (trabajo y profesionales)

### Datos clave

| Concepto | Detalle |
|---|---|
| **Que declara** | Resumen anual de todas las retenciones declaradas en los Modelos 111 del ano |
| **Plazo** | **1-31 de enero** del ano siguiente |
| **Presentacion** | Obligatoriamente telematica |
| **Detalle** | Incluye **datos individualizados** de cada perceptor: NIF, nombre, tipo de renta, importe, retencion |

El Modelo 190 es la base de los **datos fiscales** que la AEAT pone a
disposicion de los contribuyentes para hacer la Renta. Si un pagador no
presenta o presenta mal el 190, los datos fiscales del perceptor estaran
incompletos.

---

## 6. Modelo 180 -- Resumen anual de retenciones (alquileres)

### Datos clave

| Concepto | Detalle |
|---|---|
| **Que declara** | Resumen anual de todas las retenciones declaradas en los Modelos 115 del ano |
| **Plazo** | **1-31 de enero** del ano siguiente |
| **Presentacion** | Telematica |
| **Detalle** | Datos individualizados de cada arrendador: NIF, nombre, inmueble, importe, retencion |

---

## 7. Tablas de retencion del IRPF sobre nominas

La retencion sobre la nomina se calcula aplicando un algoritmo que tiene
en cuenta:

### Variables del calculo

1. **Retribucion bruta anual** (incluyendo pagas extra).
2. **Situacion familiar**:
   - Soltero/a, casado/a, separado/a.
   - Numero de hijos y sus edades.
   - Hijos con discapacidad.
   - Ascendientes a cargo.
3. **Tipo de contrato**: indefinido, temporal (< 1 ano: retencion
   minima del 2 %), relacion laboral especial.
4. **Reducciones**: por rendimientos del trabajo (hasta 7.302 EUR
   para salarios bajos), por obtener rendimientos del trabajo.
5. **Minimo personal y familiar**.
6. **Deducciones**: cuota de reduccion por tributacion conjunta, etc.

### Ejemplo orientativo de retenciones sobre nomina

| Salario bruto anual (EUR) | Retencion aproximada (soltero, sin hijos) |
|---|---|
| 15.000 | ~2-5 % |
| 20.000 | ~8-11 % |
| 25.000 | ~12-15 % |
| 30.000 | ~14-17 % |
| 40.000 | ~18-22 % |
| 50.000 | ~22-25 % |
| 60.000 | ~25-28 % |
| 80.000 | ~28-32 % |
| 100.000 | ~32-35 % |

Estas cifras son **muy aproximadas** y varian segun la situacion personal.
Usar el simulador de la AEAT para calculos precisos.

### Regularizacion

El tipo de retencion se puede **regularizar** a lo largo del ano si
cambian las circunstancias personales o salariales. El trabajador debe
comunicar los cambios al pagador (modelo interno 145).

### Minimo de retencion

- Contratos **temporales** < 1 ano: minimo **2 %**.
- Contratos **indefinidos**: no hay minimo legal, pero el resultado
  del algoritmo suele dar al menos un 2 %.

---

## 8. Calendario de presentacion

| Modelo | Periodicidad | Plazos |
|---|---|---|
| **111** | Trimestral | 1T: 1-20 abr / 2T: 1-20 jul / 3T: 1-20 oct / 4T: 1-30 ene |
| **115** | Trimestral | 1T: 1-20 abr / 2T: 1-20 jul / 3T: 1-20 oct / 4T: 1-30 ene |
| **190** | Anual | 1-31 enero |
| **180** | Anual | 1-31 enero |

Grandes empresas (CN > 6.016.000 EUR): presentacion **mensual** (los
20 primeros dias del mes siguiente, excepto diciembre: 1-30 enero).

URL del simulador de retenciones:
`https://sede.agenciatributaria.gob.es/Sede/irpf/retenciones-ingresos-cuenta-pagos-fraccionados.html`

---

## 9. Resumen rapido

```
RETENCIONES E INGRESOS A CUENTA:

TIPOS FIJOS:
  Profesionales: 15 % (7 % nuevos, primeros 3 anos)
  Alquiler inmuebles: 19 %
  Capital mobiliario: 19 %
  Premios: 19 %
  Administradores: 35 % (19 % si CN < 100.000 EUR)
  Nominas: segun tablas AEAT (variable)

MODELOS TRIMESTRALES:
  111 → retenciones trabajo + profesionales
  115 → retenciones alquileres
  Plazos: abril, julio, octubre, enero

RESUMENES ANUALES (enero):
  190 → resumen anual del 111
  180 → resumen anual del 115

QUIEN RETIENE:
  Empresas y profesionales que pagan rentas sujetas
  Particulares no retenedores: NO retienen
```

---

## Cuando NO usar esta skill

- Si el usuario es **autonomo que soporta retenciones** en sus facturas
  (perspectiva del perceptor) -> **fiscalidad-irpf-autonomos**.
- Si pregunta por obligaciones generales del **autonomo** ->
  **fiscalidad-autonomos**.
- Si pregunta por la **Declaracion de la Renta** de un asalariado
  (como le afectan las retenciones en su declaracion) ->
  **fiscalidad-irpf-asalariados**.
- Si pregunta por **IVA** -> **fiscalidad-iva**.
- Si pregunta por el **Impuesto de Sociedades** ->
  **fiscalidad-sociedades**.
- Si pregunta por **nominas y aspectos laborales** (no fiscales) ->
  **laboral-nominas**.
- Si pregunta por retenciones a **no residentes** ->
  **fiscalidad-no-residentes**.
- Si pregunta por **estadisticas de recaudacion** -> **aeat**.
