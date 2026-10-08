---
name: irpf-autonomos-jaimebs2
title: Fiscalidad — IRPF Pagos Fraccionados para Autónomos
description: 'Use when the user asks about Spanish quarterly income tax payments for self-employed workers (autónomos/personas físicas): Modelo 130 (estimación directa), Modelo 131 (estimación objetiva/módulos), deductible expenses for autónomos, withholding rates on invoices (retenciones 15 %/7 %), or IRPF obligations specific to autónomos. Does NOT cover Impuesto de Sociedades for companies or the annual income tax return (Renta, Modelo 100). Triggers on: ''modelo 130'', ''modelo 131'', ''pago fraccionado IRPF'', ''IRPF autónomo'', ''estimación directa'', ''estimación objetiva'', ''módulos autónomo'', ''gastos deducibles autónomo'', ''retención factura'', ''retención 15%'', ''retención 7%'', ''IRPF trimestral autónomo'', ''pagos fraccionados''.'
author: jaimebs2
author_url: https://github.com/jaimebs2/OpenSpain/tree/main/openspain/skills/fiscalidad/irpf-autonomos
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: tax
language: es
---

# Fiscalidad — IRPF Pagos Fraccionados para Autónomos

Skill de orientación sobre los **pagos fraccionados trimestrales del IRPF**
que deben realizar los trabajadores autónomos (personas físicas con
actividades económicas) en España.

**Solo para autónomos.** Las sociedades (SL, SA, cooperativas…) no tributan
por IRPF sino por el **Impuesto de Sociedades** (Modelo 200/202).

> Esta skill orienta sobre plazos, cálculo y gastos deducibles. **No
> sustituye asesoramiento fiscal profesional ni presenta declaraciones.**

---

## Modelo 130 — Estimación directa

### Quién lo presenta

Autónomos que determinen el rendimiento de su actividad económica en
**estimación directa** (normal o simplificada). Es el régimen más común
para profesionales y freelances.

### Excepción: cuándo NO hay que presentarlo

No están obligados los profesionales cuyo **70 % o más** de los ingresos de
actividades económicas del año anterior fueron objeto de retención o ingreso
a cuenta. En ese caso, las retenciones ya aplicadas por los clientes sustituyen
al pago fraccionado.

### Cálculo

El pago fraccionado es **acumulativo** a lo largo del año:

```
Pago = 20 % × (Ingresos acumulados − Gastos acumulados)
       − Pagos fraccionados anteriores del mismo ejercicio
       − Retenciones soportadas acumuladas
```

Paso a paso para cada trimestre:

1. Sumar todos los **ingresos** de la actividad desde el 1 de enero hasta
   el último día del trimestre.
2. Restar todos los **gastos deducibles** del mismo periodo.
3. Aplicar el **20 %** sobre el rendimiento neto resultante.
4. Restar los pagos fraccionados ya ingresados en trimestres anteriores
   del mismo año.
5. Restar las retenciones e ingresos a cuenta soportados en el periodo.
6. El resultado es el importe a ingresar (o a compensar si es negativo).

### Minoración por rendimientos bajos

Si el rendimiento neto del ejercicio anterior fue ≤ 12.000 €, se aplica
una minoración trimestral de entre 25 € y 100 € según la siguiente escala:

| Rendimiento neto año anterior | Minoración trimestral |
|---|---|
| ≤ 9.000 € | 100 € |
| 9.000,01 – 10.000 € | 75 € |
| 10.000,01 – 11.000 € | 50 € |
| 11.000,01 – 12.000 € | 25 € |

---

## Modelo 131 — Estimación objetiva (módulos)

### Quién lo presenta

Autónomos que tributen en el régimen de **estimación objetiva** del IRPF
(módulos). Solo es posible para actividades incluidas en la Orden de Módulos
vigente y si no se superan los límites de ingresos (250.000 €/año hasta
2026) ni de compras (250.000 €/año).

### Cálculo

El porcentaje se aplica sobre cantidades fijas derivadas de los módulos,
no sobre ingresos y gastos reales:

| Tipo de actividad | Porcentaje |
|---|---|
| Actividades empresariales con más de 1 empleado | 4 % |
| Actividades empresariales con 1 empleado | 3 % |
| Actividades empresariales sin empleados | 2 % |
| Actividades agrícolas, ganaderas y forestales | 2 % del volumen de ingresos del trimestre (excluidas subvenciones de capital) |

---

## Plazos de presentación

Idénticos para el Modelo 130 y el 131:

| Periodo | Plazo |
|---|---|
| 1T (enero–marzo) | 1–20 abril |
| 2T (abril–junio) | 1–20 julio |
| 3T (julio–septiembre) | 1–20 octubre |
| 4T (octubre–diciembre) | 1–30 enero del año siguiente |

Si el último día cae en sábado o festivo, el plazo se extiende al
siguiente día hábil.

La presentación es telemática a través de la Sede Electrónica de la AEAT
(certificado digital, DNI-e o Cl@ve).

---

## Retenciones en factura

Los autónomos que realizan **actividades profesionales** (sección segunda
del IAE) deben aplicar retención de IRPF en las facturas emitidas a otros
empresarios o profesionales:

| Situación | Tipo de retención |
|---|---|
| General (profesionales) | 15 % |
| Nuevos autónomos (año de alta + 2 siguientes) | 7 % |
| Actividades agrícolas y ganaderas | 2 % |
| Actividades forestales | 2 % |
| Actividades de engorde de porcino y avicultura | 1 % |

### Cuándo aplicar retención

- **Sí**: facturas a empresas o a otros autónomos por actividades
  profesionales (abogado, diseñador, consultor, programador, arquitecto,
  médico, etc.).
- **No**: facturas a consumidores finales (particulares).
- **No**: actividades empresariales (sección primera del IAE: comercio,
  hostelería, industria…) salvo excepciones.

Para aplicar el tipo reducido del 7 %, comunicarlo al cliente y cumplir
que no se haya ejercido actividad profesional en el año anterior.

---

## Gastos deducibles (estimación directa)

Para deducir un gasto debe cumplir **tres requisitos**:
1. Estar **vinculado** a la actividad económica.
2. Estar **justificado** con factura completa (o documento equivalente).
   Un recibo, ticket o factura simplificada sin datos fiscales del
   autónomo **no permite deducir** — ver **fiscalidad-facturacion**.
3. Estar **registrado** en los libros de ingresos y gastos obligatorios.

### Principales gastos deducibles

| Concepto | Deducción | Notas |
|---|---|---|
| **Cuota de autónomos** (Seguridad Social) | 100 % | Incluye todas las contingencias |
| **Alquiler de local/oficina** | 100 % | Si es de uso exclusivo profesional |
| **Suministros de local afecto** | 100 % | Luz, agua, internet, gas del local profesional |
| **Suministros del hogar** (si se trabaja desde casa) | 30 % de la parte proporcional | Proporción = m² afectos / m² totales × 30 % |
| **Material de oficina** | 100 % | Consumibles, papelería, tóner… |
| **Teléfono e internet** | Proporción afecta | 50 % si uso mixto (sin justificación detallada) |
| **Servicios profesionales** | 100 % | Gestoría, abogado, asesor fiscal, notaría |
| **Formación** | 100 % | Cursos, libros y congresos vinculados a la actividad |
| **Seguros** | 100 % | RC profesional, salud (hasta 500 €/persona/año, 1.500 € con discapacidad) |
| **Amortización de inmovilizado** | Según tablas | Equipos informáticos: 25 %/año (máx. 4 años). Mobiliario: 10 %/año |
| **Dietas (sin pernocta)** | Hasta 26,67 €/día en España | 48,08 €/día en el extranjero |
| **Dietas (con pernocta)** | Hasta 53,34 €/día en España | 91,35 €/día en el extranjero. Requiere pago electrónico en establecimiento de hostelería |
| **Vehículo** | Difícil: 100 % solo si exclusivo | Exclusividad difícil de probar excepto taxis, transportistas, repartidores, comerciales |
| **Gastos de representación** | Con límites | Comidas de negocios, regalos a clientes (justificar vinculación) |

### Gastos en estimación directa simplificada

Además de los gastos reales documentados, se aplica una **reducción del 7 %**
sobre el rendimiento neto en concepto de gastos de difícil justificación
(con un máximo de 2.000 €/año). Esta reducción sustituye a la contabilización
de pequeños gastos sin factura.

---

## Modelos relacionados

Según la situación del autónomo, puede ser necesario presentar otros modelos
trimestrales adicionales:

| Modelo | Cuándo | Qué declara |
|---|---|---|
| **111** | Si contrata empleados o paga a profesionales con retención | Retenciones sobre nóminas y facturas de profesionales |
| **115** | Si alquila local de negocio | Retenciones sobre alquileres |
| **303** | Si la actividad está sujeta a IVA | Autoliquidación trimestral del IVA → ver **fiscalidad-iva** |
| **349** | Si opera con la UE | Declaración recapitulativa de operaciones intracomunitarias → ver **fiscalidad-operaciones-intracomunitarias** |
| **100** | Anual (abril–junio del año siguiente) | Declaración de la Renta (IRPF anual) |

---

## Enlaces oficiales

| Recurso | URL |
|---|---|
| Modelo 130 — ficha | `https://sede.agenciatributaria.gob.es/Sede/procedimientoini/G601.shtml` |
| Instrucciones Modelo 130 | `https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-130-irpf______esionales-estimacion-directa-fraccionado_/instrucciones.html` |
| Modelo 131 — ficha | `https://sede.agenciatributaria.gob.es/Sede/procedimientoini/G602.shtml` |
| Pagos fraccionados — plazos | `https://sede.agenciatributaria.gob.es/Sede/irpf/retenciones-ingresos-cuenta-pagos-fraccionados/pagos-fraccionados/plazos-declaracion-ingreso.html` |
| Folleto actividades económicas | `https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/folleto-actividades-economicas.html` |
| Calendario fiscal 2026 | `https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026.html` |

---

## Cuándo NO usar esta skill

- Si el usuario pregunta por **estadísticas fiscales** (recaudación, IRPF
  por municipio, datos agregados) → **aeat**.
- Si pregunta por el **IVA** (Modelo 303, tipos, regímenes) →
  **fiscalidad-iva**.
- Si pregunta por **operaciones intracomunitarias** (ROI/VIES, reverse
  charge, Modelo 349) → **fiscalidad-operaciones-intracomunitarias**.
- Si pregunta por **cómo emitir una factura** (datos obligatorios,
  rectificativas, VeriFactu, factura electrónica) → **fiscalidad-facturacion**.
- Si pregunta por el **Modelo 036** (alta/modificación censal, casillas,
  cambio de régimen) → **fiscalidad-modelo-036**.
- Si pregunta por **cuotas de la Seguridad Social** de autónomos →
  **seguridad-social**.
- Si pregunta por obligaciones fiscales de **sociedades** (Impuesto de
  Sociedades, Modelo 200/202) → esta skill no lo cubre; redirigir a
  `https://sede.agenciatributaria.gob.es/Sede/impuesto-sobre-sociedades.html`.
- Si quiere **presentar la declaración** → redirigir a
  `https://sede.agenciatributaria.gob.es`.
- Si pregunta por el **texto de una ley** fiscal → **boe**.
