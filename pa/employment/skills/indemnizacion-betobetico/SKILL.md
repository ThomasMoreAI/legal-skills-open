---
name: indemnizacion-betobetico
title: Propósito
description: Calcula la indemnización por despido y la prima de antigüedad según tipo de terminación, antigüedad y salario con desglose legal
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/laboral/skills/indemnizacion
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: employment
language: es
---

## Propósito

Esta skill calcula las prestaciones por terminación del contrato de trabajo en Panamá —indemnización por despido injustificado y prima de antigüedad— según el tipo de terminación, aplicando las reglas del Código de Trabajo de Panamá. Genera un desglose detallado con base legal. Todos los importes se expresan en USD / balboas (B/.).

## Instrucciones

### Paso 1 — Recopilar datos

Solicitar al usuario:

1. **Fecha de inicio** de la relación de trabajo.
2. **Fecha de terminación** (efectos).
3. **Salario** del trabajador (mensual o diario); identificar si incluye conceptos promediables (comisiones, sobretiempo habitual) [verificar].
4. **Tipo de terminación**:
   - Despido injustificado.
   - Despido justificado (causa disciplinaria o económica).
   - Renuncia / mutuo acuerdo.
   - Vencimiento de contrato por tiempo definido o por obra.

### Paso 2 — Determinar régimen aplicable

**Prima de antigüedad (Código de Trabajo, art. 224):**
- En contratos por tiempo indefinido, el trabajador tiene derecho a una prima de antigüedad equivalente a una semana de salario por cada año de servicio, desde el inicio de la relación. Procede cualquiera que sea la causa de terminación. La base de cálculo es el promedio de la remuneración de los últimos 5 años; se provisiona vía Fondo de Cesantía (Ley 44 de 1995).

**Indemnización por despido injustificado (Código de Trabajo, art. 225):**
- Para relaciones iniciadas bajo la Ley 44 de 1995, la escala es: 3,4 semanas de salario por cada año en los primeros 10 años de servicio, más 1 semana adicional por cada año a partir del año 11. Es adicional a la prima de antigüedad del art. 224.

**Despido justificado:**
- No genera indemnización por despido injustificado, pero sí la prima de antigüedad (art. 224) y las prestaciones proporcionales (vacaciones y décimo tercer mes).

**Renuncia / mutuo acuerdo:**
- Prima de antigüedad (art. 224) y prestaciones proporcionales según el caso.

**Vencimiento de contrato por tiempo definido o por obra:**
- Prestaciones proporcionales; verificar si procede indemnización por terminación anticipada injustificada [verificar].

### Paso 3 — Calcular

1. Computar antigüedad total en años y fracción.
2. Determinar el salario base de cálculo: para la prima de antigüedad, promedio de la remuneración de los últimos 5 años (art. 224); para vacaciones y décimo tercer mes, promedio del período correspondiente.
3. Calcular la prima de antigüedad (una semana de salario por año de servicio, art. 224).
4. Calcular la indemnización por despido injustificado aplicando la escala del art. 225 (3,4 semanas por año en los primeros 10 años, más 1 semana adicional por cada año a partir del año 11).
5. Sumar prestaciones proporcionales pendientes (vacaciones, décimo tercer mes) si procede.

### Paso 4 — Generar desglose

## Formato de salida

```markdown
## Cálculo de prestaciones por terminación

### Datos de partida

| Concepto | Valor |
|----------|-------|
| Fecha de inicio | [fecha] |
| Fecha de terminación | [fecha] |
| Antigüedad total | [X años, Y meses, Z días] |
| Salario base de cálculo | [importe] B/. |
| Tipo de terminación | [tipo] |

### Cálculo

#### Prima de antigüedad

- Antigüedad computable: [X años]
- Fórmula: una semana de salario × [años de servicio] (Código de Trabajo, art. 224)
- Resultado: [importe] B/.

#### Indemnización por despido injustificado (si aplica)

- Antigüedad computable: [X años]
- Escala aplicada (Código de Trabajo, art. 225): 3,4 semanas de salario por año en los primeros 10 años + 1 semana adicional por año a partir del año 11 — [detalle de tramos]
- Resultado: [importe] B/.

#### Prestaciones proporcionales pendientes

- Vacaciones proporcionales (Código de Trabajo, art. 54): [importe] B/.
- Décimo tercer mes proporcional (Decreto de Gabinete 221 de 1971): [importe] B/.

#### Total

- **Total de prestaciones: [importe] B/.**

### Base legal

[Artículos aplicados: prima de antigüedad (Código de Trabajo, art. 224), indemnización por despido injustificado (art. 225), vacaciones (art. 54) y décimo tercer mes (Decreto de Gabinete 221 de 1971)]

### Advertencias

[Factores que pueden alterar el cálculo: conceptos salariales variables, descuentos, saldos pendientes, etc.]
```

## Referencias normativas

- **Código de Trabajo de Panamá, art. 224** — Prima de antigüedad (una semana de salario por año de servicio; base: promedio de los últimos 5 años; Fondo de Cesantía, Ley 44 de 1995).
- **Código de Trabajo de Panamá, art. 225** — Indemnización por despido injustificado: 3,4 semanas de salario por año en los primeros 10 años + 1 semana adicional por año a partir del año 11 (relaciones bajo la Ley 44 de 1995).
- **Código de Trabajo de Panamá, art. 54** — Vacaciones: 30 días por cada 11 meses de trabajo continuo (un día por cada 11 días trabajados).
- **Décimo tercer mes** — Decreto de Gabinete 221 de 1971: un mes de salario al año en tres partidas (15 de abril, 15 de agosto y 15 de diciembre).

## Guardrails

- **NO** determina si el despido es justificado o injustificado — calcula según el escenario indicado.
- **NO** calcula retenciones de ISR (Impuesto sobre la Renta) sobre las prestaciones — señalar que ciertas prestaciones pueden tener tratamiento fiscal especial [verificar].
- **NO** calcula cuotas obrero-patronales de la CSS sobre las prestaciones.
- **NO** sustituye la liquidación final completa — se centra en indemnización y prima de antigüedad.
- **AVISAR** si el salario proporcionado no contempla conceptos variables promediables.
- **AVISAR** si la escala de indemnización o la fórmula de la prima de antigüedad deben confirmarse contra el texto vigente del Código de Trabajo.
- **ESCALAR** si el caso involucra trabajadores con fuero (maternidad, sindical) o reintegro con salarios caídos.
