---
name: revision-despido-betobetico
title: Propósito
description: Analiza un despido propuesto contra los requisitos del Estatuto de los Trabajadores e identifica riesgos
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/laboral/skills/revision-despido
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: employment
language: es
---

## Propósito

Esta skill analiza un despido propuesto o ejecutado verificando el cumplimiento de los requisitos formales y sustantivos del Estatuto de los Trabajadores. Identifica riesgos de improcedencia o nulidad y recomienda acciones correctivas.

## Instrucciones

### Paso 1 — Identificar tipo de despido

1. **Despido objetivo** (art. 52 ET): causas económicas, técnicas, organizativas o de producción; ineptitud sobrevenida; falta de adaptación.
2. **Despido disciplinario** (art. 54 ET): incumplimiento grave y culpable del trabajador.
3. **Despido colectivo** (art. 51 ET): afecta a umbrales numéricos en período de 90 días.
4. **Extinción por causas objetivas durante período de prueba** (art. 14 ET).

### Paso 2 — Verificar requisitos formales

**Despido objetivo (art. 53 ET):**
- Comunicación escrita expresando la causa.
- Puesta a disposición simultánea de indemnización (20 días/año, máx. 12 mensualidades).
- Preaviso de 15 días (o indemnización sustitutoria).
- Licencia de 6 horas semanales para búsqueda de empleo durante el preaviso.

**Despido disciplinario (art. 55 ET):**
- Carta de despido con hechos y fecha de efectos.
- Si hay representantes: audiencia previa a delegados sindicales (si afiliado y conocido).
- Si hay convenio: tramitar expediente contradictorio si lo exige.

**Despido colectivo (art. 51 ET):**
- Comunicación a representantes y autoridad laboral.
- Período de consultas (30 días, 15 en empresas < 50 trabajadores).
- Documentación económica, memoria explicativa.
- Plan de recolocación si > 50 trabajadores.

### Paso 3 — Analizar causa

- Verificar que la causa alegada se ajusta al tipo invocado.
- Evaluar la proporcionalidad en el disciplinario.
- Comprobar la concurrencia de la causa objetiva con documentación de soporte.
- Identificar indicios de nulidad: discriminación, vulneración de derechos fundamentales, garantía de indemnidad, embarazo, reducción de jornada.

### Paso 4 — Evaluar riesgos

## Formato de salida

```markdown
## Revisión de despido

**Tipo:** [objetivo/disciplinario/colectivo]
**Trabajador:** [nombre] — Antigüedad: [fecha inicio]
**Fecha prevista de efectos:** [fecha]

### Verificación formal

| Requisito | Cumple | Base legal | Observaciones |
|-----------|--------|------------|---------------|
| Carta de despido | [SÍ/NO] | Art. [X] ET | [detalle] |
| Indemnización simultánea | [SÍ/NO/N/A] | Art. 53.1.b ET | [detalle] |
| Preaviso 15 días | [SÍ/NO/N/A] | Art. 53.1.c ET | [detalle] |

### Análisis de causa

[Valoración de la causa alegada con referencia a jurisprudencia relevante]

### Indicios de nulidad

| Indicador | Detectado | Detalle |
|-----------|-----------|---------|
| Discriminación | [SÍ/NO] | [detalle] |
| Embarazo/maternidad | [SÍ/NO] | [detalle] |
| Garantía de indemnidad | [SÍ/NO] | [detalle] |
| Representante de trabajadores | [SÍ/NO] | [detalle] |

### Valoración de riesgo

- **Riesgo de improcedencia:** [ALTO/MEDIO/BAJO] — [justificación]
- **Riesgo de nulidad:** [ALTO/MEDIO/BAJO] — [justificación]
- **Coste de improcedencia:** [cálculo orientativo — 33 días/año, máx. 24 mensualidades]
- **Salarios de tramitación:** [si aplica]

### Recomendaciones

[Acciones correctivas concretas antes de ejecutar el despido]
```

## Referencias normativas

- **ET arts. 49-57**: Extinción del contrato de trabajo.
- **ET art. 51**: Despido colectivo.
- **ET art. 52**: Extinción por causas objetivas.
- **ET art. 53**: Forma y efectos del despido objetivo.
- **ET art. 54**: Despido disciplinario — causas.
- **ET art. 55**: Forma y efectos del despido disciplinario.
- **ET art. 56**: Despido improcedente.
- **LRJS** (Ley 36/2011): Procedimiento de impugnación.
- **CE art. 14**: Igualdad y no discriminación.

## Guardrails

- **NO** decide si el despido es procedente, improcedente o nulo — eso corresponde al juzgado.
- **NO** redacta la carta de despido — solo revisa la propuesta.
- **NO** sustituye el asesoramiento de un abogado laboralista.
- **ESCALAR** si se detectan indicios de nulidad (discriminación, embarazo, derechos fundamentales).
- **ESCALAR** si el despido puede ser colectivo por superar los umbrales del art. 51 ET.
- **AVISAR** si faltan datos para completar la verificación formal.
