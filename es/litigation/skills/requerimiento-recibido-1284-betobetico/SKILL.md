---
name: requerimiento-recibido-1284-betobetico
title: Propósito
description: Analiza una demanda o requerimiento recibido e identifica plazos, opciones de respuesta y riesgos
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/procesal/skills/requerimiento-recibido
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: litigation
language: es
---

## Propósito

Esta skill analiza una demanda, requerimiento o reclamación recibida. Extrae los plazos de respuesta, identifica las opciones procesales disponibles, evalúa los riesgos y genera un informe de triaje para facilitar la toma de decisiones rápida.

## Instrucciones

### Paso 1 — Clasificar el documento recibido

1. **Demanda judicial**: ordinario, verbal, monitorio, cambiario, ejecución.
2. **Requerimiento extrajudicial**: burofax, carta notarial, email con acuse.
3. **Reclamación administrativa**: expediente sancionador, requerimiento de información.
4. **Reclamación arbitral**: solicitud de arbitraje.
5. **Mediación / conciliación**: papeleta de conciliación laboral (SMAC).

### Paso 2 — Extraer datos clave

- **Reclamante**: identificación, representación, defensa.
- **Pretensiones**: qué pide y cuánto (cuantía).
- **Hechos alegados**: resumen de la posición del reclamante.
- **Fundamentos jurídicos**: normas invocadas.
- **Fecha de notificación**: para computar plazos.
- **Juzgado / órgano**: jurisdicción y competencia.

### Paso 3 — Calcular plazos

| Tipo de procedimiento | Plazo de contestación | Base legal |
|-----------------------|-----------------------|------------|
| Ordinario | 20 días hábiles | LEC art. 404 |
| Verbal | 10 días hábiles | LEC art. 438 |
| Monitorio | 20 días hábiles para oposición | LEC art. 815 |
| Cambiario | 10 días hábiles | LEC art. 824 |
| Ejecución | 10 días hábiles para oposición | LEC art. 556 |
| Laboral (conciliación) | Comparecencia en fecha señalada | LRJS art. 82 |

Reglas de cómputo:
- Días hábiles (no sábados, domingos ni festivos).
- Agosto inhábil en jurisdicción civil (salvo excepciones del art. 183 LOPJ).
- El día de la notificación no cuenta (dies a quo).

### Paso 4 — Evaluar opciones y riesgos

## Formato de salida

```markdown
## Triaje de requerimiento recibido

**Tipo:** [demanda/requerimiento/reclamación]
**Reclamante:** [nombre]
**Fecha de notificación:** [fecha]
**Cuantía:** [importe o indeterminada]

### Plazos

| Acción | Plazo | Fecha límite | Base legal |
|--------|-------|--------------|------------|
| Contestación/oposición | [días] hábiles | [fecha] | [artículo] |
| Reconvención | [días] hábiles | [fecha] | [artículo] |
| Declinatoria | [días] hábiles | [fecha] | LEC art. 63 |

### Resumen de pretensiones

[Síntesis de qué pide el reclamante y por qué]

### Opciones de respuesta

| Opción | Descripción | Riesgo | Coste estimado |
|--------|-------------|--------|----------------|
| Contestar y oponerse | [detalle] | [nivel] | [orientativo] |
| Allanamiento total | Aceptar pretensiones | Condena sin costas (art. 395 LEC) | [cuantía] |
| Allanamiento parcial | Aceptar parte | Reduce litigio | [parcial] |
| Reconvención | Contrarreclamar | [nivel] | [orientativo] |
| Declinatoria | Impugnar competencia | [nivel] | [orientativo] |
| Negociación extrajudicial | Transacción | [nivel] | [orientativo] |

### Análisis de riesgo

- **Riesgo de condena:** [ALTO/MEDIO/BAJO] — [justificación]
- **Riesgo de costas:** [ALTO/MEDIO/BAJO]
- **Riesgo reputacional:** [SÍ/NO] — [detalle]

### Próximos pasos recomendados

1. [Acción inmediata]
2. [Acción a corto plazo]
3. [Acción estratégica]
```

## Referencias normativas

- **LEC art. 404-405**: Contestación a la demanda (ordinario).
- **LEC art. 438**: Contestación en juicio verbal.
- **LEC arts. 63-65**: Declinatoria.
- **LEC art. 395**: Costas en caso de allanamiento.
- **LEC art. 406**: Reconvención.
- **LEC arts. 812-818**: Proceso monitorio.
- **LOPJ arts. 182-185**: Días y horas hábiles.
- **LRJS** (Ley 36/2011): Procedimiento laboral.

## Guardrails

- **NO** decide la estrategia procesal — presenta opciones para que decida el letrado.
- **NO** contesta demandas ni presenta escritos.
- **NO** computa plazos con certeza absoluta — los plazos calculados son orientativos y deben verificarse.
- **NO** valora la prueba del contrario.
- **ESCALAR** si el plazo de respuesta vence en menos de 5 días hábiles.
- **ESCALAR** si las pretensiones superan el umbral de cuantía configurado en el despacho.
- **AVISAR** si la notificación puede no haberse practicado válidamente.
- **AVISAR** si agosto puede afectar al cómputo del plazo.
