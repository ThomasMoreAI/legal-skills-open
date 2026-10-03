---
name: renovaciones
title: Propósito
description: Escanea el registro de contratos y alerta sobre vencimientos y renovaciones próximas
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/mercantil/skills/renovaciones
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: commercial
language: en
---

## Propósito

Esta skill analiza el registro de contratos mercantiles del despacho o empresa para identificar contratos que se acercan a su fecha de vencimiento, renovación automática o plazo de denuncia. Genera una tabla de próximos vencimientos organizada por urgencia (30, 60 y 90 días).

## Instrucciones

### Paso 1 — Cargar registro de contratos

1. Leer el registro de contratos proporcionado por el usuario (CSV, Excel, JSON o listado de documentos).
2. Si no se proporciona registro, solicitar al usuario la fuente de datos.
3. Extraer de cada contrato:
   - Nombre/identificador del contrato.
   - Contraparte.
   - Fecha de inicio.
   - Fecha de vencimiento.
   - Tipo de renovación (automática / manual / no renovable).
   - Plazo de preaviso para no renovar (días antes del vencimiento).
   - Responsable interno.

### Paso 2 — Calcular fechas críticas

Para cada contrato:

1. **Fecha de vencimiento**: cuándo expira el contrato.
2. **Fecha límite de denuncia**: vencimiento menos plazo de preaviso.
3. **Días restantes**: desde hoy hasta cada fecha crítica.
4. **Estado**:
   - URGENTE: fecha límite de denuncia en los próximos 30 días.
   - ATENCIÓN: fecha límite de denuncia entre 31 y 60 días.
   - PLANIFICAR: fecha límite de denuncia entre 61 y 90 días.
   - VENCIDO: fecha límite de denuncia ya pasada.

### Paso 3 — Detectar riesgos

- Contratos con renovación automática cuyo plazo de denuncia ya venció (se renovarán automáticamente).
- Contratos sin fecha de vencimiento registrada.
- Contratos sin responsable asignado.
- Contratos con condiciones de renovación distintas al período original.

### Paso 4 — Generar informe

## Formato de salida

```markdown
## Tracker de renovaciones

**Fecha del informe:** [fecha]
**Contratos analizados:** [número]
**Alertas activas:** [número]

### Resumen

- Contratos URGENTE (≤30 días): [número]
- Contratos ATENCIÓN (31-60 días): [número]
- Contratos PLANIFICAR (61-90 días): [número]
- Contratos ya auto-renovados: [número]

### Próximos vencimientos

| Estado | Contrato | Contraparte | Vencimiento | Límite denuncia | Días restantes | Renovación | Responsable |
|--------|----------|-------------|-------------|-----------------|----------------|------------|-------------|
| URGENTE | [nombre] | [parte]    | [fecha]     | [fecha]         | [n]            | [tipo]     | [nombre]    |
| ATENCIÓN | [nombre] | [parte]   | [fecha]     | [fecha]         | [n]            | [tipo]     | [nombre]    |

### Alertas de riesgo

| Contrato | Riesgo | Detalle |
|----------|--------|---------|
| [nombre] | Auto-renovación inminente | Plazo de denuncia vence en [n] días |
| [nombre] | Sin fecha registrada | No se puede calcular vencimiento |

### Acciones recomendadas

1. [Acción concreta para cada contrato urgente]
```

## Referencias normativas

- **CC art. 1566**: Tácita reconducción en arrendamientos (aplicable por analogía).
- **CC art. 1128**: Plazos de las obligaciones.
- **Código de Comercio art. 62**: Rescisión de contratos mercantiles.
- **LCGC** (Ley 7/1998): Cláusulas de renovación automática en condiciones generales.

## Guardrails

- **NO** envía notificaciones ni avisos automáticos a contrapartes.
- **NO** ejecuta la denuncia o no renovación del contrato.
- **NO** accede a sistemas externos — trabaja con los datos proporcionados.
- **NO** recomienda si renovar o no — esa es decisión de negocio.
- **AVISAR** cuando un contrato carezca de información suficiente para calcular fechas.
- **AVISAR** cuando la fecha límite de denuncia ya haya pasado y la renovación sea automática.
- **ESCALAR** si se detectan más de 5 contratos en estado URGENTE simultáneamente.
