---
name: revision-mercantil-betobetico
title: Propósito
description: Revisa contratos mercantiles contra el playbook del despacho e identifica desviaciones
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/mercantil/skills/revision
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: contracts
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

- **Código Civil de Panamá:** Libro IV (obligaciones y contratos) [verificar]
- **Código de Comercio de Panamá** (Ley 2 de 1916): contratos mercantiles
- **Ley 51 de 2008**: documentos y firmas electrónicas y contratación electrónica
- **Ley 45 de 2007**: protección al consumidor y defensa de la competencia (cláusulas abusivas)
- **Ley 81 de 2019** y **Decreto Ejecutivo 285 de 2021**: cuando el contrato implique tratamiento de datos personales

## Guardrails

- **NO** redacta cláusulas alternativas — solo identifica desviaciones y recomienda.
- **NO** sustituye la revisión de un abogado idóneo.
- **NO** valora la adecuación comercial del contrato (solo la jurídica).
- **ESCALAR** cuando una cláusula ROJO afecte a limitación de responsabilidad ilimitada, indemnización cruzada sin cap, o renuncia a la jurisdicción de los tribunales panameños.
- **ESCALAR** si el contrato está en idioma distinto del español y no se proporciona traducción de traductor público autorizado.
