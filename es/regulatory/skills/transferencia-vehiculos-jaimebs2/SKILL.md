---
name: transferencia-vehiculos-jaimebs2
title: Compraventa de Vehículos Usados — Transferencia
description: 'Use when the user asks about buying or selling used vehicles in Spain: how to transfer ownership at the DGT, required documents (purchase contract, circulation permit, technical sheet, valid ITV, ID), electronic vs in-person vs gestoria processing, ITP tax on used vehicles (Model 620, Hacienda value tables), prior checks (charges, embargoes, pending fines via DGT report), temporary and permanent vehicle deregistration, importing a vehicle (homologation, taxes). This skill covers the transfer process — for driving licences use carnet-conducir, for ITV use itv, for traffic use dgt-trafico. Triggers on: ''transferencia vehículo'', ''cambio de titular'', ''compraventa coche'', ''vender coche'', ''comprar coche usado'', ''contrato compraventa vehículo'', ''ITP vehículo'', ''modelo 620'', ''informe DGT'', ''cargas vehículo'', ''baja temporal vehículo'', ''baja definitiva'', ''importar coche'', ''matricular coche importado'', ''gestoría transferencia'', ''notificación de venta DGT''.'
author: jaimebs2
author_url: https://github.com/jaimebs2/OpenSpain/tree/main/openspain/skills/vehiculos/transferencia-vehiculos
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: regulatory
language: es
---

# Compraventa de Vehículos Usados — Transferencia

Guía completa sobre cómo comprar o vender un vehículo usado en España:
transferencia en la DGT, documentación, impuestos (ITP), comprobaciones
previas y trámites relacionados.

> Esta skill orienta sobre el proceso general. **La tramitación real
> requiere acceso a la Sede Electrónica de la DGT** (con certificado
> digital, Cl@ve o gestoría).

---

## 1. Proceso general de transferencia (cambio de titular)

Cuando se vende un vehículo entre particulares (o de particular a
profesional), hay que realizar un **cambio de titularidad** ante la DGT.
El proceso tiene dos grandes bloques: el fiscal (ITP) y el
administrativo (DGT).

### Orden recomendado

1. **Comprobaciones previas** (comprador).
2. **Contrato de compraventa** (ambas partes).
3. **Pago del ITP** — Impuesto de Transmisiones Patrimoniales (comprador).
4. **Cambio de titular en la DGT** (comprador, o gestoría).
5. **Notificación de venta** (vendedor, recomendable).

---

## 2. Comprobaciones previas (comprador)

Antes de comprar un vehículo usado conviene verificar:

### Informe de vehículo de la DGT

Se puede solicitar un **informe de vehículo** en la Sede Electrónica de
la DGT o en una Jefatura de Tráfico. Coste: 8,67 € (tasa 4.4).

El informe revela:
- **Titular actual** del vehículo.
- **Cargas, reservas de dominio** (financiaciones activas).
- **Embargos** administrativos o judiciales.
- **Situación del vehículo**: alta, baja temporal, baja definitiva.
- **ITV**: fecha de última inspección y resultado.
- **Multas pendientes**: si hay sanciones sin pagar que puedan generar
  embargos.

URL: `https://sede.dgt.gob.es/es/vehiculos/informe-vehiculo/`

### Otras comprobaciones

- **ITV en vigor**: pedir al vendedor el justificante de la última ITV.
  Un vehículo con ITV caducada o desfavorable será más difícil de
  transferir y puede tener problemas ocultos. Ver skill **itv**.
- **Seguro**: el seguro del vendedor cubre hasta la transferencia. El
  comprador debe contratar su propio seguro antes de conducir.
- **Kilómetros**: cotejar los km del anuncio con los del informe DGT
  y la última ITV.

---

## 3. Contrato de compraventa

El contrato de compraventa es el documento que acredita la operación.
Puede ser privado (no necesita notario).

### Datos mínimos del contrato

1. **Datos del vendedor**: nombre, DNI/NIE, domicilio.
2. **Datos del comprador**: nombre, DNI/NIE, domicilio.
3. **Datos del vehículo**: marca, modelo, matrícula, número de bastidor,
   km.
4. **Precio** de la operación.
5. **Fecha y firma** de ambas partes.
6. **Declaración del vendedor**: que es el legítimo propietario, que
   el vehículo está libre de cargas (o las que tenga), que la ITV está
   al día.
7. **Declaración del comprador**: que acepta el vehículo en su estado
   actual.

Conviene hacer dos copias firmadas (una para cada parte). Un modelo
de contrato se puede descargar de múltiples fuentes, incluida la
propia DGT.

---

## 4. Impuesto de Transmisiones Patrimoniales (ITP)

La compraventa de un vehículo usado entre particulares tributa por el
**Impuesto de Transmisiones Patrimoniales (ITP)**. Es un impuesto
cedido a las comunidades autónomas.

### Base imponible

Hacienda establece unas **tablas de valoración** de vehículos usados
que fijan el valor mínimo fiscal según marca, modelo y antigüedad.
Se tributa sobre el **mayor** de estos dos importes:

- El precio real de la compraventa.
- El valor de las tablas de Hacienda.

Esto significa que aunque compres un coche por 1.000 €, si las tablas
dicen que vale 3.000 €, pagarás ITP sobre 3.000 €.

Las tablas se publican cada año en una Orden Ministerial (BOE).

### Tipo impositivo

El tipo general es del **4 %** en la mayoría de comunidades autónomas,
pero algunas aplican tipos diferentes (hasta un 8 % en ciertos casos).
Consultar la normativa de cada comunidad.

### Modelo 620

El pago se realiza con el **Modelo 620** ante la Hacienda autonómica
correspondiente al domicilio fiscal del comprador. Se puede presentar:

- **Online**: en la sede electrónica de la comunidad autónoma.
- **Presencialmente**: en oficinas de la agencia tributaria autonómica.

**Plazo**: 30 días hábiles desde la fecha del contrato de compraventa.

**Ejemplo orientativo**: coche valorado en 8.000 € × 4 % = **320 € de ITP**.

Para más detalle sobre el ITP → **fiscalidad-itp-ajd**.

---

## 5. Cambio de titular en la DGT

Una vez pagado el ITP, se realiza el cambio de titularidad en la DGT.

### Documentación necesaria

1. **Solicitud de transferencia** (impreso DGT o formulario online).
2. **Contrato de compraventa** firmado por ambas partes.
3. **Justificante de pago del ITP** (Modelo 620 sellado o justificante
   electrónico).
4. **Permiso de circulación** original del vehículo.
5. **Ficha técnica** (tarjeta ITV).
6. **ITV en vigor** (para vehículos obligados).
7. **DNI/NIE** de comprador y vendedor (fotocopia).
8. **Tasa DGT** de transferencia: **55,70 €** (tasa 4.1).

### Vías de tramitación

| Vía | Cómo | Plazo |
|---|---|---|
| **Electrónica** | Sede Electrónica DGT (requiere certificado digital o Cl@ve de ambas partes, o que una apodere a la otra) | Inmediato o 24-48 h |
| **Presencial** | Jefatura Provincial de Tráfico con cita previa | Según disponibilidad |
| **Gestoría** | Un gestor administrativo tramita todo (se les da poder de representación) | 1-3 días hábiles |

URL tramitación electrónica:
`https://sede.dgt.gob.es/es/vehiculos/cambio-de-titularidad/`

### Notificación de venta (vendedor)

El vendedor puede (y es muy recomendable) comunicar a la DGT que ha
vendido el vehículo mediante la **notificación de venta**. Esto le
protege de:

- Multas que lleguen a su nombre después de la venta.
- Responsabilidad por accidentes del nuevo propietario.

Se puede hacer en la Sede Electrónica de la DGT (con Cl@ve o certificado)
o presencialmente con cita previa.

URL: `https://sede.dgt.gob.es/es/vehiculos/notificacion-de-venta/`

---

## 6. Compraventa a/de profesional (concesionario)

Cuando interviene un profesional (concesionario, compraventa de coches):

- La operación tributa por **IVA** (21 %) en lugar de ITP si el vendedor
  es profesional.
- El concesionario suele gestionar la transferencia.
- Si el concesionario opera con **régimen de bienes usados** (REBU),
  el IVA se aplica solo sobre el margen de beneficio.
- El comprador particular no paga ITP en este caso.

---

## 7. Baja temporal y baja definitiva

### Baja temporal

Se puede dar de baja temporal un vehículo cuando no se va a usar
durante un periodo prolongado. Efectos:

- No puede circular por vías públicas.
- No es necesario mantener el seguro obligatorio (pero sí es
  recomendable si el vehículo está en la vía pública).
- No paga el Impuesto de Vehículos de Tracción Mecánica (IVTM) durante
  la baja, si se comunica al ayuntamiento. Consultar
  **fiscalidad-impuestos-locales**.

Tasa DGT: **8,67 €** (tasa 4.4).

Para reactivar: alta con ITV en vigor y seguro.

### Baja definitiva

Cuando el vehículo se desguaza o se exporta definitivamente. Hay que
entregarlo en un Centro Autorizado de Tratamiento (CAT) que emite el
certificado de destrucción. Con ese certificado se tramita la baja
definitiva en la DGT.

---

## 8. Importación de vehículos

Traer un vehículo del extranjero para matricularlo en España implica
varios trámites:

### Desde la UE

1. **Impuesto de Matriculación** (Impuesto Especial sobre Determinados
   Medios de Transporte): varía según emisiones de CO₂ (0 % para
   emisiones bajas, hasta 14,75 % para altas emisiones). Muchos
   vehículos quedan exentos.
2. **IVA**: si el vendedor es profesional, lo incluye en la factura.
   Si es particular y el vehículo tiene más de 6 meses y más de
   6.000 km, no lleva IVA en destino.
3. **Homologación**: con COC (Certificate of Conformity) europeo, el
   proceso es sencillo. Sin COC, se necesita homologación individual.
4. **ITV previa a matriculación**: inspección obligatoria.
5. **Matriculación en DGT**: con toda la documentación.

### Desde fuera de la UE

Además de lo anterior:
- **Despacho aduanero** (arancel + IVA de importación).
- **Homologación individual** (más compleja y costosa).

---

## 9. Resumen rápido: pasos para transferir un vehículo usado

```
COMPRADOR:
  1. Pedir informe DGT del vehículo (8,67 €)
  2. Verificar: ITV, cargas, embargos, km
  3. Firmar contrato de compraventa
  4. Pagar ITP (Modelo 620, ~4 % del valor)
  5. Contratar seguro
  6. Tramitar cambio de titular en DGT (55,70 €)

VENDEDOR:
  1. Tener ITV al día
  2. Firmar contrato de compraventa
  3. Entregar permiso de circulación y ficha técnica
  4. Hacer notificación de venta en la DGT (recomendable)

DOCUMENTACIÓN DGT:
  ├── Contrato de compraventa
  ├── Modelo 620 pagado (ITP)
  ├── Permiso de circulación
  ├── Ficha técnica
  ├── ITV en vigor
  ├── DNI/NIE ambas partes
  └── Tasa DGT (55,70 €)
```

---

## Cuándo NO usar esta skill

- Si pregunta por la **ITV** en detalle (periodicidad, resultados,
  documentación) → **itv**.
- Si pregunta por el **carnet de conducir** (tipos, obtención,
  renovación, puntos) → **carnet-conducir**.
- Si pregunta por el **ITP** en profundidad (más allá de vehículos) →
  **fiscalidad-itp-ajd**.
- Si pregunta por el **Impuesto de Circulación** (IVTM) →
  **fiscalidad-impuestos-locales**.
- Si pregunta por el **estado del tráfico** en tiempo real →
  **dgt-trafico**.
- Si pregunta por **Permiso Internacional de Conducción** →
  **permiso-internacional**.
- Si pregunta por **zonas de bajas emisiones** → **dgt-zbe**.
- Si pregunta por el **texto de una ley** o normativa → **boe**.
