---
name: revision-contratacion-betobetico
title: Propósito
description: Revisa contratos de trabajo verificando cláusulas obligatorias y adecuación al tipo contractual
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/laboral/skills/revision-contratacion
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: contracts
language: es
---

## Propósito

Esta skill revisa un contrato de trabajo individual, verifica que contiene todas las cláusulas obligatorias según el Código de Trabajo de Panamá y la normativa aplicable, y comprueba que el tipo contractual elegido se ajusta a la situación descrita.

## Instrucciones

### Paso 1 — Identificar tipo de contrato

1. **Por tiempo indefinido**: contrato por defecto bajo el Código de Trabajo (art. 74).
2. **Por tiempo definido**: con plazo determinado (Código de Trabajo, art. 74); no puede exceder de 1 año, o 3 años si requiere preparación técnica.
3. **Por obra determinada**: vinculado a la ejecución de una obra o servicio específico (Código de Trabajo, art. 74).
4. **Contrato de aprendizaje / formación**: regulado principalmente por el Decreto Ley 4 de 1997 y la normativa del INADEH (el Código de Trabajo aplica solo de forma supletoria).

Recordar la regla de continuidad: la celebración sucesiva de contratos por tiempo definido o por obra, o la continuidad tras el vencimiento del plazo, puede convertir la relación en una por tiempo indefinido (Código de Trabajo, art. 77).

### Paso 2 — Verificar cláusulas obligatorias

Comprobar la presencia y corrección de:

| Cláusula | Base legal | Verificación |
|----------|------------|--------------|
| Identidad de las partes (incl. cédula/RUC) | Código de Trabajo | Datos completos |
| Fecha de inicio y duración | Código de Trabajo | Coherente con tipo |
| Domicilio del empleador y lugar de trabajo | Código de Trabajo | Presente |
| Cargo o clase de trabajo | Código de Trabajo | Definido con claridad |
| Salario y forma de pago | Código de Trabajo | ≥ salario mínimo (MITRADEL) |
| Jornada y horario | Código de Trabajo, arts. 30-31 | Dentro de la jornada máxima legal (diurna 8h/48h; nocturna 7h/42h; mixta 7,5h/45h) |
| Vacaciones | Código de Trabajo, art. 54 | 30 días por cada 11 meses de trabajo continuo |
| Período de prueba (si aplica) | Código de Trabajo, art. 78 | Máximo 3 meses, por escrito |
| Décimo tercer mes | Decreto de Gabinete 221 de 1971 | Mención del derecho |
| Inscripción en la CSS | Ley 51 de 2005 (art. 77) | Obligación de afiliación (6 días hábiles) |

### Paso 3 — Revisar cláusulas especiales

- **No competencia postcontractual**: en Panamá el pacto de no competencia es válido durante la relación, pero el pacto **postcontractual no se admite con carácter general** por ser contrario a la libertad de trabajo (art. 40 de la Constitución) y al carácter de orden público del Código de Trabajo (art. 6). A diferencia de otros ordenamientos, no basta con prever una compensación: una cláusula postcontractual es de validez muy dudosa y frecuentemente nula o inejecutable.
- **Confidencialidad**: proporcionalidad y duración razonables.
- **Exclusividad / plena dedicación**: con contraprestación adecuada.
- **Teletrabajo**: acuerdo escrito conforme a la Ley 126 de 2020 sobre teletrabajo.

### Paso 4 — Verificar adecuación del tipo contractual

- El contrato por tiempo definido o por obra tiene causa real y vigente.
- La duración se ajusta a los máximos legales del Código de Trabajo.
- No hay indicios de uso fraudulento de la temporalidad (sucesión de contratos que deba convertirse en indefinido, Código de Trabajo, art. 77).

## Formato de salida

```markdown
## Revisión de contrato de trabajo

**Tipo contractual:** [tipo]
**Trabajador:** [nombre]
**Puesto:** [denominación]
**Convención colectiva aplicable (si existe):** [nombre de la convención]

### Verificación de cláusulas obligatorias

| Cláusula | Presente | Conforme | Observaciones |
|----------|----------|----------|---------------|
| [nombre] | [SÍ/NO] | [SÍ/NO/N/A] | [detalle] |

### Cláusulas especiales

| Cláusula | Presente | Validez | Riesgos |
|----------|----------|---------|---------|
| No competencia | [SÍ/NO] | [válida/dudosa/nula] | [detalle] |

### Adecuación del tipo contractual

[Valoración de si el tipo contractual es correcto para la situación descrita]

### Riesgos detectados

| Riesgo | Severidad | Consecuencia | Recomendación |
|--------|-----------|--------------|---------------|
| [riesgo] | [nivel] | [qué puede pasar] | [qué hacer] |
```

## Referencias normativas

- **Código de Trabajo de Panamá, art. 74** — Forma, duración y modalidades del contrato de trabajo (indefinido, definido y por obra).
- **Código de Trabajo, art. 78** — Período de prueba (máximo 3 meses, por escrito).
- **Código de Trabajo, art. 77** — Conversión a indefinido por sucesión de contratos definidos/por obra o continuidad tras el plazo.
- **Código de Trabajo, arts. 30-31 y 54** — Jornada (diurna 8h/48h; nocturna 7h/42h; mixta 7,5h/45h) y vacaciones (30 días por cada 11 meses).
- **Décimo tercer mes** — Decreto de Gabinete 221 de 1971 (tres partidas: 15 de abril, 15 de agosto y 15 de diciembre).
- **Ley 51 de 2005** — Afiliación e inscripción obligatorias del trabajador en la CSS (art. 77; plazo de 6 días hábiles).
- **Ley 126 de 2020** — Teletrabajo (modifica el art. 151 del Código de Trabajo).
- **Decreto Ley 4 de 1997 e INADEH** — Contrato de aprendizaje.
- **Constitución Política de Panamá, art. 40, y Código de Trabajo, art. 6** — Libertad de trabajo y orden público (relevantes para la no competencia postcontractual).

## Guardrails

- **NO** redacta contratos de trabajo — solo revisa los existentes.
- **NO** determina la convención colectiva aplicable con certeza — sugiere la probable.
- **NO** calcula planillas ni cuotas obrero-patronales de la CSS.
- **ESCALAR** si el contrato por tiempo definido o por obra carece de causa o supera la duración máxima legal.
- **ESCALAR** si el contrato incluye una cláusula de no competencia postcontractual: en Panamá es de validez muy dudosa o inejecutable (libertad de trabajo, art. 40 de la Constitución; orden público, art. 6 del Código de Trabajo), aun previendo compensación.
- **AVISAR** si no se identifica la convención colectiva aplicable (cuando exista) para verificar mejoras sobre el mínimo legal.
