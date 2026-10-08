---
name: demanda-1992-betobetico
title: Propósito
description: Redacta secciones de una demanda civil en formato del despacho siguiendo la estructura de la LEC
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/procesal/skills/demanda
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: contracts
language: es
---

## Propósito

Esta skill redacta secciones individuales de una demanda civil siguiendo la estructura exigida por la LEC y el formato del despacho. Genera borradores que requieren revisión obligatoria por el abogado firmante. No redacta demandas completas de una vez — trabaja sección por sección.

## Instrucciones

### Paso 1 — Identificar sección a redactar

1. **Encabezamiento**: juzgado, partes, representación y defensa.
2. **Hechos**: narración ordenada y numerada de los hechos relevantes.
3. **Fundamentos de derecho**: normas aplicables con subsunción.
4. **Petitum (suplico)**: pretensiones concretas y cuantificadas.
5. **Otrosíes**: medidas cautelares, prueba anticipada, cuantía, turno de oficio.

### Paso 2 — Recopilar información necesaria

**Para hechos:**
- Cronología de hechos (usar skill cronología si está disponible).
- Documentos de soporte para cada hecho.
- Relación causal entre hechos.

**Para fundamentos de derecho:**
- Norma sustantiva aplicable.
- Jurisdicción y competencia (arts. 44-62 LEC).
- Legitimación activa y pasiva.
- Tipo de procedimiento (ordinario art. 249 / verbal art. 250).
- Jurisprudencia de apoyo (si disponible).

**Para petitum:**
- Pretensiones principales y subsidiarias.
- Cuantificación de daños si aplica.
- Intereses y costas.

### Paso 3 — Redactar sección

Seguir el formato del despacho (si existe en config) o el formato estándar.

**Hechos:**
- Numerados correlativamente.
- Un hecho relevante por párrafo.
- Con referencia al documento probatorio ("doc. nº X").
- Lenguaje fáctico — sin valoraciones jurídicas.

**Fundamentos de derecho:**
- Numerados correlativamente.
- Estructura: norma → interpretación → aplicación al caso.
- Cita literal del precepto cuando sea relevante.
- Jurisprudencia con referencia completa (tribunal, fecha, ROJ/ECLI).

**Petitum:**
- Pretensiones numeradas, claras y concretas.
- Alternativas o subsidiarias claramente separadas.
- Pronunciamiento sobre costas e intereses.

## Formato de salida

```markdown
## BORRADOR — Sección de demanda

**Estado:** BORRADOR — Requiere revisión del letrado firmante
**Asunto:** [nombre]
**Sección:** [hechos / fundamentos / petitum / encabezamiento / otrosí]

---

[Contenido de la sección redactada según el formato correspondiente]

---

### Notas internas (no incluir en el escrito final)

- **Documentos referenciados:** [lista de docs citados]
- **Puntos que requieren confirmación del letrado:** [lista]
- **Jurisprudencia citada:** [verificar vigencia]
- **Cuantía del procedimiento:** [cálculo orientativo]
```

## Referencias normativas

- **LEC art. 399**: Requisitos de la demanda.
- **LEC art. 400**: Preclusión de la alegación de hechos y fundamentos jurídicos.
- **LEC arts. 249-250**: Determinación del procedimiento (ordinario/verbal).
- **LEC arts. 44-62**: Jurisdicción y competencia.
- **LEC arts. 5-10**: Comparecencia, representación y defensa.
- **LEC art. 219**: Sentencias con reserva de liquidación (condenas de futuro).
- **LEC art. 394**: Imposición de costas.

## Guardrails

- **NO** genera demandas completas listas para presentar — solo secciones borrador.
- **NO** firma ni presenta escritos — todo es borrador para revisión.
- **NO** garantiza la viabilidad de la pretensión ni la estrategia procesal.
- **NO** sustituye al procurador en la representación procesal.
- **ESCALAR** si la pretensión puede estar prescrita o caducada.
- **ESCALAR** si hay dudas sobre la jurisdicción o competencia (arbitraje, fuero imperativo).
- **AVISAR** que la jurisprudencia citada debe verificarse en bases de datos actualizadas (CENDOJ).
- **AVISAR** siempre al inicio: "Este documento es un BORRADOR y no constituye un escrito procesal válido hasta su revisión y firma por letrado colegiado."
