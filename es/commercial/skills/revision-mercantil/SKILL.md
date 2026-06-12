---
name: revision-mercantil
title: Propósito
description: Revisa contratos mercantiles contra el playbook del despacho e identifica desviaciones
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/mercantil/skills/revision
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: es
practice: commercial
language: es
---

## Propósito

Esta skill revisa un contrato mercantil comparándolo con las posiciones estándar definidas en el playbook del despacho. Identifica desviaciones cláusula por cláusula y genera una tabla de revisión con semáforo de riesgo.

## Instrucciones

### Paso 1 — Cargar fuentes

1. Leer el contrato proporcionado por el usuario.
2. Cargar el playbook desde `~/.claude/plugins/config/claude-para-abogados/mercantil/CLAUDE.md`.
3. Si no existe playbook, informar al usuario y ofrecer revisión genérica basada en estándares de mercado.

### Paso 2 — Identificar cláusulas clave

Extraer y clasificar las siguientes cláusulas (como mínimo):

- Objeto y alcance
- Precio y condiciones de pago
- Duración y renovación
- Limitación de responsabilidad
- Indemnización
- Propiedad intelectual
- Confidencialidad
- Protección de datos
- Resolución y terminación
- Ley aplicable y jurisdicción
- Fuerza mayor

### Paso 3 — Comparar contra playbook

Para cada cláusula:

1. Identificar la posición del playbook (ideal, aceptable, inaceptable).
2. Extraer la posición actual del contrato.
3. Determinar el nivel de desviación.
4. Formular recomendación concreta.

### Paso 4 — Asignar semáforo

- **VERDE**: La cláusula se ajusta a la posición del playbook o es más favorable.
- **AMARILLO**: Desviación aceptable con condiciones — negociable pero no bloqueante.
- **ROJO**: Desviación significativa — requiere escalado o renegociación antes de firmar.

### Paso 5 — Generar informe

Producir la tabla de revisión y un resumen ejecutivo.

## Formato de salida

```markdown
## Revisión de contrato mercantil

**Contrato:** [nombre del documento]
**Fecha de revisión:** [fecha]
**Contraparte:** [nombre]

### Resumen ejecutivo

[2-3 frases con hallazgos principales y recomendación general]

### Tabla de revisión

| Cláusula | Posición playbook | Posición contrato | Semáforo | Recomendación |
|----------|-------------------|-------------------|----------|---------------|
| [nombre] | [resumen]         | [resumen]         | [color]  | [acción]      |

### Cláusulas ROJO — Requieren escalado

[Detalle de cada cláusula roja con justificación]

### Cláusulas ausentes

[Cláusulas que el playbook exige y no aparecen en el contrato]
```

## Referencias normativas

- **Código Civil:** arts. 1254-1314 (obligaciones y contratos)
- **Código de Comercio:** arts. 50-63 (contratos mercantiles)
- **LSSI-CE** (Ley 34/2002): condiciones generales de contratación electrónica
- **LCGC** (Ley 7/1998): condiciones generales de la contratación
- **RGPD** y **LOPDGDD** (LO 3/2018): cuando el contrato implique tratamiento de datos

## Guardrails

- **NO** redacta cláusulas alternativas — solo identifica desviaciones y recomienda.
- **NO** sustituye la revisión de un abogado colegiado.
- **NO** valora la adecuación comercial del contrato (solo la jurídica).
- **ESCALAR** cuando una cláusula ROJO afecte a limitación de responsabilidad ilimitada, indemnización cruzada sin cap, o renuncia a jurisdicción española.
- **ESCALAR** si el contrato está en idioma distinto del español y no se proporciona traducción jurada.
