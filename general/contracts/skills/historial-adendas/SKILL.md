---
name: historial-adendas
title: Propósito
description: Traza la evolución de cláusulas clave a través del contrato base y sus adendas
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/mercantil/skills/historial-adendas
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: es
---

## Propósito

Esta skill reconstruye la historia de un contrato mercantil leyendo el acuerdo base y todas sus adendas o modificaciones. Genera una tabla de evolución temporal por cláusula, permitiendo ver cómo han cambiado las posiciones a lo largo del tiempo.

## Instrucciones

### Paso 1 — Cargar documentos

1. Leer el contrato base proporcionado.
2. Leer cada adenda o modificación en orden cronológico.
3. Identificar la fecha de cada documento y ordenarlos.
4. Si falta alguna adenda intermedia, avisar al usuario.

### Paso 2 — Identificar cláusulas rastreables

Extraer las cláusulas que han sido objeto de modificación:

- Comparar cada adenda con la versión anterior.
- Registrar qué cláusulas se añaden, modifican o eliminan.
- Anotar la referencia exacta en cada documento (número de cláusula, página).

### Paso 3 — Construir línea temporal

Para cada cláusula modificada, registrar:

1. **Versión original** del contrato base.
2. **Cada modificación** con fecha, documento fuente y texto relevante.
3. **Versión vigente** actual.
4. **Dirección del cambio**: si favorece a una parte u otra.

### Paso 4 — Detectar inconsistencias

- Cláusulas modificadas que contradicen otras no modificadas.
- Adendas que referencian numeración de cláusulas incorrecta.
- Definiciones que cambian sin actualizar las referencias cruzadas.
- Conflictos entre versiones (adenda posterior contradice anterior sin derogarla expresamente).

### Paso 5 — Generar informe

## Formato de salida

```markdown
## Historial de adendas

**Contrato base:** [nombre] — Fecha: [fecha]
**Adendas analizadas:** [número]
**Última modificación:** [fecha]

### Resumen de cambios

[2-3 frases indicando volumen y dirección general de las modificaciones]

### Evolución por cláusula

| Cláusula | Contrato base | Adenda 1 (fecha) | Adenda 2 (fecha) | Versión vigente | Dirección |
|----------|---------------|-------------------|-------------------|-----------------|-----------|
| [nombre] | [resumen]     | [cambio o "—"]    | [cambio o "—"]    | [texto actual]  | [nota]    |

### Inconsistencias detectadas

| Tipo | Documentos afectados | Descripción | Severidad |
|------|----------------------|-------------|-----------|
| [tipo] | [docs]            | [detalle]   | Alta/Media/Baja |

### Cláusulas sin modificar desde el contrato base

[Lista de cláusulas que permanecen inalteradas]
```

## Referencias normativas

- **CC art. 1091**: Las obligaciones que nacen de los contratos tienen fuerza de ley entre las partes.
- **CC arts. 1281-1289**: Reglas de interpretación de los contratos.
- **CC art. 1283**: No se entenderán comprendidos en el contrato cosas distintas de aquellas sobre las que se propusieron contratar.
- **CC art. 1286**: Interpretación sistemática — las cláusulas se interpretan unas por otras.
- **Código de Comercio art. 57**: Contratos mercantiles se ejecutarán de buena fe.

## Guardrails

- **NO** determina cuál versión prevalece en caso de conflicto — eso requiere análisis jurídico caso por caso.
- **NO** redacta adendas de consolidación ni textos refundidos.
- **NO** valora si las modificaciones son válidas formalmente (ej. si la adenda fue firmada por parte legitimada).
- **ESCALAR** si se detectan inconsistencias de severidad alta.
- **ESCALAR** si faltan adendas intermedias que impidan reconstruir la cadena completa.
- **AVISAR** si alguna adenda carece de fecha o las fechas no son consistentes.
