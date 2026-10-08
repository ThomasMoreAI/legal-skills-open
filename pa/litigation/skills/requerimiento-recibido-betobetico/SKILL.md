---
name: requerimiento-recibido-betobetico
title: Propósito
description: Analiza una demanda o requerimiento recibido e identifica plazos, opciones de respuesta y riesgos
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/procesal/skills/requerimiento-recibido
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: litigation
language: es
---

## Propósito

Esta skill analiza una demanda, requerimiento o reclamación recibida. Extrae los plazos de respuesta, identifica las opciones procesales disponibles, evalúa los riesgos y genera un informe de triaje para facilitar la toma de decisiones rápida.

## Instrucciones

### Paso 1 — Clasificar el documento recibido

1. **Demanda judicial**: proceso ordinario, sumario, oral, ejecutivo. [verificar]
2. **Requerimiento extrajudicial**: carta notarial, correo certificado con acuse, email con acuse.
3. **Reclamación administrativa**: procedimiento sancionador, requerimiento de información (Ley 38 de 2000).
4. **Reclamación arbitral**: solicitud de arbitraje.
5. **Conciliación**: la conciliación administrativa individual ante el MITRADEL es voluntaria (no requisito previo obligatorio general); la conciliación obligatoria es la fase dentro de la audiencia ante la Junta de Conciliación y Decisión o el Juzgado de Trabajo.

### Paso 2 — Extraer datos clave

- **Reclamante**: identificación, representación, defensa.
- **Pretensiones**: qué pide y cuánto (cuantía).
- **Hechos alegados**: resumen de la posición del reclamante.
- **Fundamentos jurídicos**: normas invocadas.
- **Fecha de notificación**: para computar plazos.
- **Tribunal / órgano**: jurisdicción y competencia.

### Paso 3 — Calcular términos

| Tipo de proceso | Término de contestación | Base legal |
|-----------------|-------------------------|------------|
| Ordinario | 10 días hábiles | Código Judicial (coincide con el Código Procesal Civil) |
| Sumario | 5 días hábiles (confirmar en el Código Procesal Civil) | Código Judicial de Panamá |
| Ejecutivo | 8 días hábiles para oposición/excepciones; traslado al ejecutante 5 días (confirmar en el Código Procesal Civil) | Código Judicial de Panamá |
| Laboral | Según traslado del juez de trabajo | Código de Trabajo de Panamá |
| Conciliación laboral | Comparecencia en fecha señalada (la conciliación administrativa individual ante el MITRADEL es voluntaria) | MITRADEL |

Reglas de cómputo:
- Días hábiles (no sábados, domingos ni días feriados/de duelo nacional) — arts. 509 y 512 del Código Judicial.
- No existe un mes de vacancia judicial general equivalente al agosto inhábil español; verificar el calendario del Órgano Judicial.
- Los términos de días corren desde el día siguiente a la notificación; el día de la notificación no cuenta (dies a quo) — art. 511 del Código Judicial.
- El vencimiento se produce a las 5:00 p.m. del último día (art. 511 del Código Judicial).

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
| Contestación/oposición | [días] hábiles | [fecha] | [artículo del Código Judicial — verificar] |
| Reconvención | [días] hábiles | [fecha] | [artículo del Código Judicial — verificar] |
| Excepción de incompetencia | dentro del traslado de la demanda (10 días en el ordinario) | [fecha] | Código Judicial (en el Código Procesal Civil se ventila en el saneamiento/audiencia preliminar) |

### Resumen de pretensiones

[Síntesis de qué pide el reclamante y por qué]

### Opciones de respuesta

| Opción | Descripción | Riesgo | Coste estimado |
|--------|-------------|--------|----------------|
| Contestar y oponerse | [detalle] | [nivel] | [orientativo] |
| Allanamiento total | Aceptar pretensiones | Efecto sobre costas según el Código Judicial | [cuantía] |
| Allanamiento parcial | Aceptar parte | Reduce litigio | [parcial] |
| Reconvención | Contrarreclamar | [nivel] | [orientativo] |
| Excepción de incompetencia | Impugnar competencia | [nivel] | [orientativo] |
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

- **Código Judicial de Panamá**: contestación a la demanda en proceso ordinario (10 días; confirmar en el Código Procesal Civil para procesos nuevos).
- **Código Judicial de Panamá**: traslado y contestación en proceso sumario (5 días; confirmar en el Código Procesal Civil).
- **Código Judicial de Panamá**: excepciones, incluida la de incompetencia (en el Código Procesal Civil se ventilan en el saneamiento/audiencia preliminar).
- **Código Judicial de Panamá**: efectos del allanamiento sobre las costas [verificar].
- **Código Judicial de Panamá**: reconvención [verificar].
- **Código Judicial de Panamá**: proceso ejecutivo (oposición/excepciones 8 días; confirmar en el Código Procesal Civil).
- **Código Judicial de Panamá, arts. 509, 511 y 512**: días hábiles y cómputo de términos.
- **Código de Trabajo de Panamá**: proceso laboral [verificar].

## Guardrails

- **NO** decide la estrategia procesal — presenta opciones para que decida el abogado.
- **NO** contesta demandas ni presenta escritos.
- **NO** computa términos con certeza absoluta — los términos calculados son orientativos y deben verificarse.
- **NO** valora la prueba del contrario.
- **ESCALAR** si el término de respuesta vence en menos de 5 días hábiles.
- **ESCALAR** si las pretensiones superan el umbral de cuantía configurado en el despacho.
- **AVISAR** si la notificación puede no haberse practicado válidamente.
- **AVISAR** si días feriados o de duelo nacional pueden afectar al cómputo del término.
