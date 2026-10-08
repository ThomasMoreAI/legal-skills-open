---
name: compraventa-jaimebs2
title: Vivienda --- Compraventa de vivienda
description: 'Use when the user asks about buying or selling a property in Spain: the full purchase process, earnest money (arras), public deed (escritura), buyer and seller costs, nota simple, cadastral reference, energy certificate, new-build vs. second-hand tax differences, or off-plan purchases. Triggers on: ''comprar vivienda'', ''comprar piso'', ''vender casa'', ''gastos comprador'', ''gastos vendedor'', ''arras'', ''contrato de arras'', ''señal piso'', ''escritura compraventa'', ''notario compraventa'', ''registro propiedad compraventa'', ''nota simple'', ''cargas vivienda'', ''ITP vivienda'', ''IVA obra nueva'', ''plusvalía venta'', ''ganancia patrimonial vivienda'', ''referencia catastral'', ''certificado energético'', ''compra sobre plano'', ''proceso compra piso España''.'
author: jaimebs2
author_url: https://github.com/jaimebs2/OpenSpain/tree/main/openspain/skills/vivienda/compraventa
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: real-estate
language: es
---

# Vivienda --- Compraventa de vivienda

Guía completa del proceso de compraventa de una vivienda en España:
desde la oferta hasta la inscripción en el Registro de la Propiedad.

> Esta skill orienta sobre el proceso general. **No sustituye
> asesoramiento jurídico ni fiscal profesional.**

---

## 1. El proceso de compraventa paso a paso

### Fase 1 --- Búsqueda y verificación

1. **Buscar la vivienda** (portales, agencias, particulares).
2. **Pedir la nota simple** del Registro de la Propiedad para verificar:
   - Quién es el titular real.
   - Si tiene cargas (hipoteca, embargos, servidumbres).
   - Descripción y superficie registral.
3. **Comprobar la referencia catastral** en el Catastro (ver skill
   **catastro**) para verificar superficie y uso.
4. **Solicitar el certificado de eficiencia energética** (obligatorio
   para vender o alquilar desde 2013).

### Fase 2 --- Contrato de arras o señal

Antes de la escritura, comprador y vendedor suelen firmar un
**contrato de arras** (o contrato privado de compraventa con señal).

#### Tipos de arras

| Tipo | Efecto si se incumple | Base legal |
|---|---|---|
| **Penitenciales** (las más habituales) | Comprador pierde la señal; vendedor devuelve el doble | Art. 1454 Código Civil |
| **Confirmatorias** | La parte perjudicada puede exigir cumplimiento o indemnización | Art. 1124 Código Civil |
| **Penales** | Se pierde la señal como penalización, pero se puede exigir además el cumplimiento | Art. 1152-1153 Código Civil |

La cantidad habitual de arras oscila entre el **5 % y el 10 %** del
precio de compraventa.

**Plazo**: se pacta un plazo (normalmente 30-90 días) para firmar la
escritura pública ante notario.

### Fase 3 --- Escritura pública ante notario

La compraventa se formaliza mediante **escritura pública** ante notario:

1. El notario verifica la identidad de las partes, la titularidad y las
   cargas.
2. Se lee el contenido de la escritura.
3. Las partes firman.
4. Se paga el precio (normalmente cheque bancario o transferencia).
5. El notario remite copia electrónica al Registro de la Propiedad y a
   Hacienda.

**Elección de notario**: el comprador tiene derecho a elegir notario
(art. 126 del Reglamento Notarial).

URL: `https://www.notariado.org`

### Fase 4 --- Inscripción en el Registro de la Propiedad

Tras la escritura, el notario (o el gestor) presenta la copia
autorizada en el Registro de la Propiedad correspondiente. La
inscripción:

- Da publicidad y seguridad jurídica (terceros de buena fe).
- Protege frente a dobles ventas y cargas ocultas.
- No es obligatoria legalmente, pero es **imprescindible en la
  práctica** (los bancos la exigen para hipotecas).

Plazo de inscripción: normalmente 15-30 días hábiles.

URL: `https://www.registradores.org`

---

## 2. Gastos del comprador

| Concepto | Detalle | Cuantía orientativa |
|---|---|---|
| **Impuestos** | IVA 10 % (obra nueva) o ITP (segunda mano, varía por CCAA: 4-10 %) | 4-10 % del precio |
| **AJD** | Actos Jurídicos Documentados. En obra nueva, 0,5-1,5 % según CCAA | 0,5-1,5 % |
| **Notaría** | Según arancel regulado por RD 1426/1989 | 600-1.200 EUR aprox. |
| **Registro de la Propiedad** | Arancel regulado por RD 1427/1989 | 300-700 EUR aprox. |
| **Gestoría** | Tramitación (opcional pero habitual) | 300-500 EUR |
| **Tasación** | Si se pide hipoteca; la paga el comprador | 250-500 EUR |

### Vivienda nueva (del promotor) vs. segunda mano

| | Vivienda nueva | Segunda mano |
|---|---|---|
| **Impuesto principal** | IVA 10 % + AJD | ITP (varía por CCAA) |
| **IVA/ITP** | IVA: 10 % (4 % VPO en algunas CCAA) | ITP: 4-10 % según CCAA |
| **AJD** | Sí (0,5-1,5 % según CCAA) | No (ya incluido en el ITP) |
| **Certificado energético** | Lo aporta el promotor | Lo debe obtener el vendedor |

Para detalle sobre ITP y AJD, consulta la skill **fiscalidad-itp-ajd**.

---

## 3. Gastos del vendedor

| Concepto | Detalle |
|---|---|
| **Plusvalía municipal** (IIVTNU) | Impuesto sobre el incremento de valor de los terrenos de naturaleza urbana. Lo liquida el ayuntamiento. Dos métodos de cálculo: real y objetivo. Consulta **fiscalidad-impuestos-locales** |
| **Ganancia patrimonial en IRPF** | Diferencia entre precio de venta y precio de adquisición (con gastos). Tipos: 19 %, 21 %, 23 %, 27 % según tramo. Exención por reinversión en vivienda habitual y para mayores de 65 años |
| **Cancelación de hipoteca** | Si la vivienda tiene hipoteca: cancelación registral (notario + registro) y posible comisión bancaria por amortización anticipada |
| **Certificado energético** | Obligatorio. Si no lo tiene, debe obtenerlo antes de la venta (coste: 50-300 EUR) |
| **IBI del año** | Se paga por quien sea propietario a 1 de enero, pero es habitual pactar prorrateo en la escritura |

---

## 4. La nota simple: qué es y para qué sirve

La **nota simple informativa** es un extracto del Registro de la
Propiedad que contiene:

- **Titular/es** de la finca y su porcentaje de propiedad.
- **Descripción** de la finca (superficie, linderos, ubicación).
- **Cargas**: hipotecas, embargos, servidumbres, afecciones fiscales,
  condiciones resolutorias.

### Cómo solicitar una nota simple

1. **Online**: a través de `https://sede.registradores.org` (coste:
   ~9,02 EUR + IVA). Se recibe en minutos.
2. **Presencialmente**: en el Registro de la Propiedad correspondiente a
   la ubicación de la finca.
3. **A través del notario**: si se está tramitando una escritura, el
   notario la solicita de oficio.

**Recomendación**: pedir siempre una nota simple **actualizada** (menos
de 15 días) antes de firmar arras o escritura.

Para más información sobre el Registro de la Propiedad, consulta
**vivienda-registro-propiedad**.

---

## 5. Referencia catastral y certificado energético

### Referencia catastral

Es el identificador oficial de cada inmueble en el Catastro (20
caracteres alfanuméricos). Obligatoria en la escritura de compraventa
(art. 3 TRLCI).

Se puede consultar gratuitamente en la Sede Electrónica del Catastro.
Para detalle sobre cómo consultar datos catastrales, ver skill
**catastro**.

### Certificado de eficiencia energética

Obligatorio desde el RD 235/2013 para vender o alquilar:

- Lo obtiene el vendedor (o arrendador) antes de la comercialización.
- Lo elabora un técnico competente (arquitecto, ingeniero).
- Tiene una **validez de 10 años**.
- Clasifica la vivienda de A (más eficiente) a G (menos eficiente).
- Debe registrarse en el organismo autonómico correspondiente.
- Debe incluirse en los anuncios de venta/alquiler.

---

## 6. Compra sobre plano (obra nueva en construcción)

Cuando se compra una vivienda sobre plano (antes de que esté
construida):

1. **Contrato de reserva o compraventa privada**: se firma con el
   promotor y se van haciendo pagos parciales.
2. **Garantía de cantidades anticipadas** (obligatoria): el promotor
   debe contar con un **seguro** o **aval bancario** que cubra la
   devolución de las cantidades entregadas a cuenta si no se entrega la
   vivienda (Ley 20/2015 y disposición adicional primera de la LOE).
3. **Licencia de primera ocupación**: al terminar la obra, el
   ayuntamiento la expide. Sin ella no se pueden contratar suministros.
4. **Escritura**: una vez terminada la vivienda, se firma escritura
   pública.

**Importante**: antes de firmar el contrato privado, verificar que el
promotor tiene:
- Licencia de obra concedida.
- Seguro de cantidades anticipadas (pedir copia del aval o póliza).
- Fecha estimada de entrega y penalizaciones por retraso.

---

## 7. Checklist del comprador

```
ANTES DE LAS ARRAS:
  ├── Nota simple actualizada (< 15 días)
  ├── Referencia catastral y datos del Catastro
  ├── Certificado de eficiencia energética
  ├── Último recibo de IBI pagado
  ├── Certificado de la comunidad de estar al corriente de pagos
  ├── Cédula de habitabilidad / licencia de primera ocupación
  └── Si hay hipoteca del vendedor: verificar saldo pendiente

ANTES DE LA ESCRITURA:
  ├── Preaprobación de hipoteca (si procede)
  ├── FEIN y FiAE firmados (si hipoteca)
  ├── Cheque bancario o transferencia preparada
  ├── DNI/NIE en vigor
  └── NIE (obligatorio para extranjeros)

DESPUÉS DE LA ESCRITURA:
  ├── Inscripción en el Registro de la Propiedad
  ├── Liquidación de impuestos (ITP/AJD o IVA+AJD)
  ├── Cambio de titularidad de suministros (luz, agua, gas)
  ├── Cambio de domicilio en el padrón municipal
  └── Comunicar al administrador de la comunidad
```

---

## 8. Plazos y prescripción

| Trámite | Plazo |
|---|---|
| **Liquidar ITP/AJD** | 30 días hábiles desde la escritura |
| **Liquidar IVA (autoliquidación)** | Simultáneo a la escritura (obra nueva) |
| **Plusvalía municipal** | 30 días hábiles desde la escritura (comprador o vendedor según municipio) |
| **Inscripción en el Registro** | No hay plazo legal, pero se recomienda hacerlo de inmediato |
| **Prescripción ITP** | 4 años |

---

## 9. Fiscalidad de la compraventa --- resumen

| Quién | Impuesto | Skill con detalle |
|---|---|---|
| Comprador (obra nueva) | IVA 10 % + AJD | **fiscalidad-itp-ajd** |
| Comprador (segunda mano) | ITP (4-10 % según CCAA) | **fiscalidad-itp-ajd** |
| Vendedor | Plusvalía municipal (IIVTNU) | **fiscalidad-impuestos-locales** |
| Vendedor | Ganancia patrimonial IRPF (19-27 %) | — |
| Propietario (anual) | IBI | **fiscalidad-impuestos-locales** |

---

## 10. Resumen rápido del proceso

```
1. BÚSQUEDA
   └── Visitar, comparar, negociar precio

2. VERIFICACIÓN
   ├── Nota simple (Registro de la Propiedad)
   ├── Datos catastrales (Catastro)
   ├── Certificado energético
   └── Cargas, deudas de comunidad, IBI

3. CONTRATO DE ARRAS
   ├── Tipo de arras (penitenciales lo más habitual)
   ├── Señal: 5-10 % del precio
   └── Plazo para escriturar: 30-90 días

4. FINANCIACIÓN
   ├── Solicitar hipoteca (si procede)
   ├── Tasación oficial
   └── FEIN y FiAE → skill vivienda-hipotecas

5. ESCRITURA PÚBLICA (notario)
   ├── Pago del precio (cheque bancario)
   └── Entrega de llaves

6. POST-ESCRITURA
   ├── Inscripción en Registro de la Propiedad
   ├── Liquidación de impuestos
   └── Cambio de titularidad de suministros
```

---

## Cuándo NO usar esta skill

- Si necesita **detalle sobre hipotecas** (tipos, TAE, Euribor, FEIN)
  --> **vivienda-hipotecas**.
- Si necesita información sobre el **Registro de la Propiedad** (nota
  simple en detalle, inscripción, principios registrales) -->
  **vivienda-registro-propiedad**.
- Si pregunta por **comunidad de propietarios** (juntas, cuotas, obras,
  morosos) --> **vivienda-comunidad-propietarios**.
- Si pregunta por **alquiler de vivienda** (LAU, fianza, renta) -->
  **vivienda-alquiler**.
- Si pregunta por **ITP o AJD** en detalle (tipos por CCAA, exenciones,
  liquidación) --> **fiscalidad-itp-ajd**.
- Si pregunta por **plusvalía municipal o IBI** -->
  **fiscalidad-impuestos-locales**.
- Si pregunta por **herencias de vivienda** (impuesto de sucesiones) -->
  **fiscalidad-sucesiones-donaciones**.
- Si pregunta por **datos catastrales** (referencia catastral, valor
  catastral, consulta de inmuebles) --> **catastro**.
- Si pregunta por **Euribor o tipos de interés** --> **bde**.
