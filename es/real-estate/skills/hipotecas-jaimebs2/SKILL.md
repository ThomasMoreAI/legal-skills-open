---
name: hipotecas-jaimebs2
title: Vivienda --- Hipotecas
description: 'Use when the user asks about mortgages in Spain: fixed vs. variable vs. mixed rates, TAE vs. TIN, Euribor, mortgage costs, FEIN/FiAE pre-contractual documents, early repayment, subrogation, novation, bank good practices code, or mortgage simulators. Triggers on: ''hipoteca'', ''hipoteca fija'', ''hipoteca variable'', ''hipoteca mixta'', ''TAE hipoteca'', ''TIN hipoteca'', ''Euribor'', ''cuota hipoteca'', ''gastos hipoteca'', ''FEIN'', ''FiAE'', ''amortización anticipada hipoteca'', ''subrogación hipoteca'', ''novación hipoteca'', ''vinculaciones hipoteca'', ''simulador hipoteca'', ''Ley 5/2019'', ''cláusula suelo'', ''Código Buenas Prácticas'', ''comparar hipotecas'', ''qué hipoteca me conviene''.'
author: jaimebs2
author_url: https://github.com/jaimebs2/OpenSpain/tree/main/openspain/skills/vivienda/hipotecas
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: real-estate
language: es
---

# Vivienda --- Hipotecas

Guía completa sobre hipotecas en España: tipos, costes, documentos
precontractuales, amortización, subrogación y normativa aplicable.

> Esta skill orienta sobre conceptos y normativa hipotecaria general.
> **No sustituye asesoramiento financiero profesional.**

---

## 1. Tipos de hipoteca

### Hipoteca a tipo fijo

- La cuota **no varía** durante toda la vida del préstamo.
- Mayor seguridad para el prestatario: sabe exactamente cuánto paga
  cada mes.
- Generalmente el tipo de interés inicial es **más alto** que el
  variable.
- Ideal cuando el Euribor está en niveles bajos y se espera que suba.

### Hipoteca a tipo variable

- La cuota se **revisa periódicamente** (normalmente cada 6 o 12
  meses) según un índice de referencia + un diferencial.
- El índice más habitual en España es el **Euribor** a 12 meses.
- Ejemplo: Euribor + 0,99 %. Si el Euribor está al 2,5 %, el tipo
  aplicado es 3,49 %.
- Mayor incertidumbre, pero el tipo inicial suele ser más bajo.

### Hipoteca mixta

- Combina un **periodo inicial a tipo fijo** (normalmente 3-10 años)
  y luego pasa a **tipo variable** el resto del plazo.
- Compromiso intermedio entre seguridad y ahorro.

---

## 2. TAE vs. TIN

| Concepto | Qué incluye | Para qué sirve |
|---|---|---|
| **TIN** (Tipo de Interés Nominal) | Solo el interés puro aplicado al capital | Calcular la cuota mensual |
| **TAE** (Tasa Anual Equivalente) | TIN + comisiones + gastos vinculados (seguros obligatorios, etc.) | **Comparar** ofertas entre bancos |

La TAE es el indicador correcto para comparar hipotecas, porque refleja
el **coste total** del préstamo para el cliente.

**Importante**: en hipotecas variables, la TAE es orientativa porque
depende de la evolución futura del Euribor.

---

## 3. Euribor

El **Euribor** (Euro Interbank Offered Rate) es el tipo de interés al
que los bancos europeos se prestan dinero entre sí. Se publica
diariamente y existe a varios plazos (1 semana, 1 mes, 3 meses, 6
meses, 12 meses).

### Euribor a 12 meses

Es el índice de referencia más utilizado en las hipotecas españolas a
tipo variable:

- **Publicación**: el Banco de España publica la media mensual en el
  BOE el primer día hábil del mes siguiente.
- **Consulta**: `https://www.bde.es/webbe/es/estadisticas/compartida/datos/pdf/ti_1_3.pdf`
- Para datos históricos y series temporales del Euribor, consulta la
  skill **bde**.

### Cómo afecta a tu cuota

Cuando toca revisión (cada 6 o 12 meses según contrato):

1. Se toma el Euribor medio del mes anterior (o dos meses antes, según
   contrato).
2. Se suma el diferencial pactado.
3. Se recalcula la cuota para el siguiente periodo.

**Ejemplo**: hipoteca de 150.000 EUR a 25 años, Euribor + 1 %.
- Si Euribor = 2 %: tipo aplicado 3 %, cuota ~711 EUR/mes.
- Si Euribor = 4 %: tipo aplicado 5 %, cuota ~877 EUR/mes.

---

## 4. Gastos de constitución de hipoteca

Desde la **Ley 5/2019** (LCCI), reguladora de los contratos de crédito
inmobiliario, los gastos se reparten así:

| Gasto | Quién paga |
|---|---|
| **Tasación** | Cliente |
| **Notaría** (escritura de hipoteca) | Banco |
| **Registro de la Propiedad** (inscripción de hipoteca) | Banco |
| **Gestoría** | Banco |
| **AJD** (Actos Jurídicos Documentados) de la hipoteca | Banco |
| **Copia de la escritura** para el cliente | Cliente |

**Nota**: los gastos de la **escritura de compraventa** (notaría,
registro, ITP/IVA) los paga el **comprador** --- no se incluyen aquí.
Ver skill **vivienda-compraventa**.

### Tasación

- Obligatoria si se solicita hipoteca.
- La realiza una sociedad de tasación homologada por el Banco de
  España.
- Coste habitual: 250-500 EUR según tipo y ubicación del inmueble.
- El banco debe aceptar cualquier tasación de una sociedad homologada
  (no puede imponer una concreta).

---

## 5. Vinculaciones y bonificaciones

Los bancos ofrecen **bonificaciones** (reducción del diferencial o del
tipo fijo) a cambio de contratar productos adicionales:

| Producto vinculado | Bonificación típica |
|---|---|
| Domiciliar nómina | -0,10 % a -0,30 % |
| Seguro de hogar | -0,05 % a -0,15 % |
| Seguro de vida | -0,05 % a -0,20 % |
| Plan de pensiones | -0,05 % a -0,15 % |
| Uso de tarjetas | -0,05 % a -0,10 % |

**Ley 5/2019**: el banco debe ofrecer siempre una oferta **sin
vinculaciones** (oferta vinculada) y otra con bonificaciones (oferta
combinada). El cliente elige.

**Consejo**: calcular si el coste anual de los productos vinculados
compensa la bonificación obtenida.

---

## 6. FEIN y FiAE --- Documentos precontractuales obligatorios

La Ley 5/2019 obliga al banco a entregar al cliente, **al menos 10
días naturales antes de la firma**, los siguientes documentos:

### FEIN (Ficha Europea de Información Normalizada)

- Documento estandarizado a nivel europeo.
- Tiene carácter de **oferta vinculante** para el banco.
- Contiene: importe, plazo, tipo de interés (fijo/variable), TAE,
  cuota mensual, tabla de amortización, gastos, comisiones, seguros
  obligatorios.
- Es el documento clave para comparar ofertas.

### FiAE (Ficha de Advertencias Estandarizadas)

- Alerta sobre los principales riesgos del préstamo:
  - Si es variable: que la cuota puede subir.
  - Índice de referencia utilizado.
  - Existencia de comisiones (apertura, amortización anticipada).
  - Cláusula de vencimiento anticipado.

### Otros documentos obligatorios

- Copia del contrato.
- Documento con los gastos detallados.
- Condiciones de los seguros (si los hay).
- Información sobre el acta notarial previa (gratuita).

### Acta notarial previa

Antes de la firma de la hipoteca, el prestatario debe acudir al
notario (elegido por él) para firmar un **acta de transparencia**:

- El notario verifica que el cliente ha recibido toda la documentación.
- Resuelve dudas.
- El acta es **gratuita** (la paga el banco).
- Debe firmarse **al menos 1 día antes** de la escritura de hipoteca.

---

## 7. Amortización anticipada

### Amortización parcial

Permite reducir el capital pendiente antes de lo previsto. Dos
opciones:

1. **Reducir cuota**: se mantiene el plazo, baja la mensualidad.
2. **Reducir plazo**: se mantiene la cuota, se acorta la duración
   (ahorra más intereses a largo plazo).

### Amortización total (cancelación)

Se devuelve todo el capital pendiente de una vez. El banco cancela la
hipoteca.

### Comisiones por amortización anticipada (Ley 5/2019)

| Tipo de hipoteca | Periodo | Comisión máxima |
|---|---|---|
| **Variable** | Primeros 3 años | 0,25 % del capital amortizado |
| **Variable** | Primeros 5 años (alternativa) | 0,15 % del capital amortizado |
| **Variable** | A partir de 3/5 años | 0 % |
| **Fija** | Primeros 10 años | 2 % del capital amortizado |
| **Fija** | A partir de 10 años | 1,5 % del capital amortizado |

**Nota**: estos límites aplican a hipotecas firmadas a partir del
16/06/2019 (entrada en vigor de la Ley 5/2019). Hipotecas anteriores
se rigen por sus propias condiciones contractuales.

---

## 8. Subrogación y novación

### Subrogación (cambio de banco)

- Llevar la hipoteca a **otro banco** que ofrezca mejores condiciones.
- El nuevo banco cancela la deuda con el antiguo y constituye una
  nueva hipoteca.
- No genera nuevo AJD (exención).
- Comisión máxima del banco saliente: según Ley 5/2019 (mismos
  límites que amortización anticipada).

### Novación (renegociar con tu banco)

- Cambiar las condiciones de la hipoteca **sin cambiar de banco**:
  tipo de interés, plazo, sistema de amortización.
- Requiere escritura pública (con coste de notaría y registro).
- AJD reducido o exento en algunos supuestos.
- No hay comisión regulada por ley, pero el banco suele cobrar
  comisión de novación (negociable).

### ¿Qué conviene más?

- Si tu banco no mejora condiciones --> **subrogación**.
- Si tu banco iguala la oferta del mercado --> **novación** (más
  sencillo y rápido).

---

## 9. Código de Buenas Prácticas Bancarias

Mecanismo voluntario (RDL 6/2012, actualizado) para proteger a
**deudores hipotecarios en situación de vulnerabilidad**:

### Medidas del Código

1. **Reestructuración**: carencia, ampliación de plazo, reducción de
   tipo.
2. **Quita**: reducción del capital pendiente si la reestructuración
   no es viable.
3. **Dación en pago**: entregar la vivienda al banco y quedar libre
   de deuda. Solo como último recurso.

### Requisitos del deudor

- Vivienda habitual.
- Ingresos familiares inferiores a ciertos umbrales (varían según
  composición familiar y circunstancias).
- Cuota hipotecaria superior al 50 % de los ingresos netos.

Consulta las condiciones actualizadas en:
`https://www.bde.es/bde/es/secciones/informes/Folletos/`

---

## 10. Simuladores y comparadores

### Simulador del Banco de España

El BdE ofrece un simulador gratuito de préstamos hipotecarios:
`https://app.bde.es/asb_www/es/cuota.html`

Permite calcular:
- Cuota mensual según capital, plazo y tipo de interés.
- Tabla de amortización completa.
- Efecto de amortizaciones anticipadas.

Para datos del Euribor y tipos de interés oficiales, consulta la
skill **bde**.

### Qué comparar entre ofertas

```
PARA CADA OFERTA DE HIPOTECA, COMPARAR:
  ├── TAE (coste total real, incluyendo vinculaciones)
  ├── TIN (tipo nominal puro)
  ├── Cuota mensual resultante
  ├── Comisión de apertura (limitada o eliminada por Ley 5/2019)
  ├── Comisión de amortización anticipada
  ├── Vinculaciones exigidas y su coste anual
  ├── Coste total del préstamo (intereses + comisiones + seguros)
  └── Flexibilidad (carencias, amortizaciones parciales)
```

---

## 11. Resumen rápido

```
ANTES DE PEDIR HIPOTECA:
  ├── Calcular capacidad de endeudamiento (cuota < 30-35 % ingresos)
  ├── Ahorrar ~20-30 % del precio (entrada + gastos compraventa)
  └── Comparar ofertas de varios bancos (mínimo 3)

DOCUMENTOS CLAVE:
  ├── FEIN → oferta vinculante del banco (recibir 10 días antes)
  ├── FiAE → advertencias de riesgo
  └── Acta notarial previa → firma al menos 1 día antes

DURANTE LA HIPOTECA:
  ├── Revisión del Euribor (si variable): cada 6 o 12 meses
  ├── Amortización anticipada: valorar reducir plazo vs. cuota
  └── Si dificultades: Código de Buenas Prácticas Bancarias

CAMBIAR CONDICIONES:
  ├── Novación → renegociar con tu banco
  └── Subrogación → cambiar a otro banco
```

---

## Cuándo NO usar esta skill

- Si necesita el **proceso de compraventa** (arras, escritura, gastos
  comprador/vendedor) --> **vivienda-compraventa**.
- Si necesita información sobre el **Registro de la Propiedad** -->
  **vivienda-registro-propiedad**.
- Si pregunta por **comunidad de propietarios** -->
  **vivienda-comunidad-propietarios**.
- Si pregunta por **alquiler de vivienda** --> **vivienda-alquiler**.
- Si pregunta por el **Euribor actual, series históricas o tipos
  de interés oficiales** --> **bde**.
- Si pregunta por **ITP o AJD** de la compraventa -->
  **fiscalidad-itp-ajd**.
- Si pregunta por **datos catastrales** de la vivienda -->
  **catastro**.
- Si pregunta por **herencias de vivienda** (impuesto de sucesiones)
  --> **fiscalidad-sucesiones-donaciones**.
