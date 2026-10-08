---
name: revision-despido-4025-betobetico
title: Propósito
description: Analiza un despido propuesto contra los requisitos del Código de Trabajo de Panamá e identifica riesgos
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/laboral/skills/revision-despido
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: employment
language: es
---

## Propósito

Esta skill analiza un despido propuesto o ejecutado verificando el cumplimiento de los requisitos formales y sustantivos del Código de Trabajo de Panamá. Identifica riesgos de despido injustificado o nulo y recomienda acciones correctivas.

## Instrucciones

### Paso 1 — Identificar tipo de despido

El art. 213 del Código de Trabajo agrupa las causas justificadas en tres acápites: **A) causas de naturaleza disciplinaria; B) causas no imputables al trabajador** (p. ej., incapacidad física o mental, pena de prisión); **C) causas de naturaleza económica o de mercado** (quiebra, cierre, reducción comprobada de operaciones).

1. **Despido por causa justificada de naturaleza disciplinaria** (Código de Trabajo, art. 213, acápite A): incumplimiento grave del trabajador.
2. **Despido por causa no imputable al trabajador** (Código de Trabajo, art. 213, acápite B): incapacidad física o mental, pena de prisión y supuestos análogos.
3. **Despido por causa justificada de naturaleza económica o de mercado** (Código de Trabajo, art. 213, acápite C): quiebra, cierre o reducción comprobada de operaciones de la empresa.
4. **Despido de trabajador con fuero** (maternidad, sindical, dirigente) — requiere autorización judicial previa (Código de Trabajo, arts. 106 para maternidad y 383 para fuero sindical).
5. **Terminación durante el período de prueba** (Código de Trabajo, art. 78): máximo 3 meses, debe constar por escrito.

### Paso 2 — Verificar requisitos formales

**Despido por causa justificada (Código de Trabajo, art. 213 y ss.):**
- Aviso de despido por escrito expresando la causa concreta y la fecha de efectos.
- Invocación de causal específica del Código de Trabajo; no pueden alegarse después otras causas.
- Plazo de caducidad para invocar la causa disciplinaria: 2 meses desde los hechos, o desde su conocimiento si constituyen delito (Código de Trabajo, art. 220).
- Pago de las prestaciones que correspondan según el caso (prima de antigüedad, vacaciones proporcionales, décimo tercer mes proporcional).

**Despido de trabajador con fuero:**
- Autorización judicial previa ante el Juzgado de Trabajo (la autorización de despido de aforados se tramita ante el juzgado de trabajo; competencia laboral repartida entre Juzgados de Trabajo y Juntas de Conciliación y Decisión, Ley 7 de 1975).
- Sin autorización previa, el despido es ineficaz y procede el reintegro con salarios caídos. En contrato indefinido, el trabajador despedido injustificadamente puede pedir reintegro con salarios caídos o la indemnización del art. 225 (Código de Trabajo, art. 218); estabilidad reforzada a partir de 2 años de antigüedad.

**Despido por causas económicas o de operación (art. 213, acápite C):**
- Cumplimiento del procedimiento ante MITRADEL cuando aplique (autorización o notificación) [verificar].
- Sustento documental de la causa económica o de mercado invocada.

### Paso 3 — Analizar causa

- Verificar que la causa alegada se ajusta a una causal del Código de Trabajo.
- Evaluar la proporcionalidad y gravedad en el despido disciplinario.
- Comprobar el sustento documental de la causa económica o de operación.
- Identificar indicios de nulidad o ineficacia: discriminación, represalia, fuero de maternidad, fuero sindical, fuero por enfermedad o riesgo profesional.

### Paso 4 — Evaluar riesgos

## Formato de salida

```markdown
## Revisión de despido

**Tipo:** [disciplinario/económico-operación/fuero]
**Trabajador:** [nombre] — Antigüedad: [fecha inicio]
**Fecha prevista de efectos:** [fecha]

### Verificación formal

| Requisito | Cumple | Base legal | Observaciones |
|-----------|--------|------------|---------------|
| Aviso de despido por escrito | [SÍ/NO] | Código de Trabajo, art. 213 | [detalle] |
| Causal específica invocada | [SÍ/NO/N/A] | Código de Trabajo, art. 213 (acápites A/B/C) | [detalle] |
| Autorización judicial previa (fuero) | [SÍ/NO/N/A] | Código de Trabajo, arts. 106 (maternidad) y 383 (sindical) | [detalle] |
| Pago de prestaciones que correspondan | [SÍ/NO/N/A] | Código de Trabajo, arts. 224 y 225 | [detalle] |

### Análisis de causa

[Valoración de la causa alegada con referencia a jurisprudencia relevante de la Corte Suprema de Justicia (Sala Tercera/Sala de lo Laboral) [verificar]]

### Indicios de nulidad o ineficacia

| Indicador | Detectado | Detalle |
|-----------|-----------|---------|
| Discriminación | [SÍ/NO] | [detalle] |
| Fuero de maternidad | [SÍ/NO] | [detalle] |
| Represalia / persecución | [SÍ/NO] | [detalle] |
| Fuero sindical / dirigente | [SÍ/NO] | [detalle] |

### Valoración de riesgo

- **Riesgo de despido injustificado:** [ALTO/MEDIO/BAJO] — [justificación]
- **Riesgo de ineficacia / reintegro:** [ALTO/MEDIO/BAJO] — [justificación]
- **Coste de despido injustificado:** [cálculo orientativo — indemnización (art. 225) y prima de antigüedad (art. 224) del Código de Trabajo]
- **Salarios caídos:** [si aplica, en caso de reintegro — Código de Trabajo, art. 218]

### Recomendaciones

[Acciones correctivas concretas antes de ejecutar el despido]
```

## Referencias normativas

- **Código de Trabajo de Panamá** — Terminación de la relación de trabajo (Decreto de Gabinete 252 de 1971).
- **Código de Trabajo, art. 213** — Causas justificadas de despido (acápite A disciplinario; acápite B no imputable al trabajador; acápite C económico o de mercado). Caducidad de la causa disciplinaria: art. 220 (2 meses).
- **Código de Trabajo, arts. 106 y 383** — Régimen de fueros: maternidad (art. 106; licencia en el art. 107) y fuero sindical (art. 383; amparados en el art. 381), con autorización judicial previa.
- **Código de Trabajo, arts. 218, 224 y 225** — Reintegro con salarios caídos o indemnización (art. 218), prima de antigüedad (art. 224) e indemnización por despido injustificado (art. 225).
- **MITRADEL** — Procedimientos administrativos en despidos por causa económica [verificar].
- **Constitución Política de Panamá** — Garantías laborales y no discriminación [verificar].

## Guardrails

- **NO** decide si el despido es justificado, injustificado o nulo — eso corresponde al juez o a la Junta de Conciliación y Decisión.
- **NO** redacta el aviso de despido — solo revisa la propuesta.
- **NO** sustituye el asesoramiento de un abogado laboralista idóneo.
- **ESCALAR** si se detectan indicios de nulidad o ineficacia (discriminación, fuero de maternidad, fuero sindical).
- **ESCALAR** si el trabajador goza de fuero y no hay autorización judicial previa.
- **AVISAR** si faltan datos para completar la verificación formal.
