---
name: indemnizacion-7102-betobetico
title: Propósito
description: Calcula la indemnización por despido según tipo, antigüedad y salario con desglose legal
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/laboral/skills/indemnizacion
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: employment
language: es
---

## Propósito

Esta skill calcula la indemnización por extinción del contrato de trabajo según el tipo de despido, aplicando las reglas del Estatuto de los Trabajadores incluida la transición del régimen pre-2012 cuando proceda. Genera un desglose detallado con base legal.

## Instrucciones

### Paso 1 — Recopilar datos

Solicitar al usuario:

1. **Fecha de inicio** de la relación laboral.
2. **Fecha de despido** (efectos).
3. **Salario bruto diario** regulador (incluye prorrateo de pagas extras).
4. **Tipo de despido/extinción**:
   - Despido improcedente.
   - Despido objetivo procedente.
   - Despido colectivo.
   - Extinción por voluntad del trabajador (art. 50 ET).
   - Fin de contrato temporal.

### Paso 2 — Determinar régimen aplicable

**Despido improcedente:**
- Contratos anteriores al 12/02/2012: 45 días/año (máx. 42 mensualidades) hasta esa fecha + 33 días/año (máx. 24 mensualidades) desde esa fecha. El tope de 24 mensualidades se aplica al total combinado salvo que el tramo pre-2012 ya supere esa cifra.
- Contratos desde el 12/02/2012: 33 días/año (máx. 24 mensualidades).

**Despido objetivo procedente / despido colectivo:**
- 20 días/año (máx. 12 mensualidades), para cualquier fecha de inicio.

**Extinción por voluntad del trabajador (art. 50 ET):**
- Misma indemnización que despido improcedente.

**Fin de contrato temporal:**
- 12 días/año trabajado (contratos desde 01/01/2015).

### Paso 3 — Calcular

1. Computar antigüedad total en años y fracción (los períodos inferiores al año se prorratean por meses y días).
2. Calcular cada tramo por separado si hay transición pre/post-2012.
3. Aplicar topes de mensualidades.
4. El salario diario regulador = (salario bruto anual incluyendo todos los conceptos salariales) / 365.

### Paso 4 — Generar desglose

## Formato de salida

```markdown
## Cálculo de indemnización por despido

### Datos de partida

| Concepto | Valor |
|----------|-------|
| Fecha de inicio | [fecha] |
| Fecha de despido | [fecha] |
| Antigüedad total | [X años, Y meses, Z días] |
| Salario bruto diario | [importe] EUR |
| Tipo de despido | [tipo] |

### Cálculo

#### Tramo 1 (si aplica): [fecha inicio] — 11/02/2012

- Antigüedad en este tramo: [X años, Y meses, Z días]
- Fórmula: [salario diario] x 45 x [antigüedad en años decimales]
- Resultado: [importe] EUR
- Tope: 42 mensualidades = [importe] EUR

#### Tramo 2: 12/02/2012 — [fecha despido]

- Antigüedad en este tramo: [X años, Y meses, Z días]
- Fórmula: [salario diario] x 33 x [antigüedad en años decimales]
- Resultado: [importe] EUR

#### Total

- Suma de tramos: [importe] EUR
- Tope aplicable: 24 mensualidades = [importe] EUR
- **Indemnización resultante: [importe] EUR**

### Base legal

[Artículos aplicados y régimen transitorio si procede — Disposición transitoria 5ª RDL 3/2012]

### Advertencias

[Factores que pueden alterar el cálculo: salarios de tramitación, FOGASA, etc.]
```

## Referencias normativas

- **ET art. 49.1.c**: Indemnización por fin de contrato temporal.
- **ET art. 50**: Extinción por voluntad del trabajador.
- **ET art. 53.1.b**: Indemnización por despido objetivo (20 días/año).
- **ET art. 56.1**: Indemnización por despido improcedente (33 días/año).
- **Disposición transitoria 5ª RDL 3/2012**: Régimen transitorio del cálculo indemnizatorio.
- **Disposición transitoria 11ª ET**: Indemnización de contratos de fomento.

## Guardrails

- **NO** determina si el despido es procedente o improcedente — calcula según el escenario indicado.
- **NO** incluye salarios de tramitación en el cálculo salvo que se solicite expresamente.
- **NO** calcula retenciones de IRPF sobre la indemnización (exención del art. 7.e LIRPF hasta ciertos límites).
- **NO** calcula liquidación (finiquito) — solo indemnización.
- **AVISAR** si el salario proporcionado parece no incluir el prorrateo de pagas extras.
- **AVISAR** si la antigüedad es anterior a 1995 (posibles regímenes transitorios adicionales).
- **ESCALAR** si el caso involucra representantes de trabajadores (indemnización mínima de 45 días por readmisión obligatoria).
