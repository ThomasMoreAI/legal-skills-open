---
name: clausulas-betobetico
title: Propósito
description: Revisa cláusulas de propiedad intelectual e industrial en contratos verificando cesión, alcance y conformidad legal
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/propiedad-intelectual/skills/clausulas
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: contracts
language: es
---

## Propósito

Esta skill revisa las cláusulas de propiedad intelectual e industrial contenidas en un contrato. Verifica la estructura de cesión/licencia, exclusividad, territorio, duración y conformidad con la legislación española de PI, prestando especial atención a la obra por encargo y la PI generada en relación laboral.

## Instrucciones

### Paso 1 — Identificar cláusulas de PI

Localizar en el contrato:

1. Cláusula de titularidad / propiedad de los resultados.
2. Cesión de derechos de explotación.
3. Licencia de uso (si no hay cesión).
4. Obra por encargo / work made for hire.
5. PI preexistente (background IP).
6. PI desarrollada conjuntamente.
7. Derecho moral del autor.
8. Garantías de no infracción.
9. Invenciones y patentes (en contratos laborales o de I+D).

### Paso 2 — Analizar cada cláusula

Para cada cláusula de PI verificar:

| Aspecto | Verificación |
|---------|-------------|
| **Cesión vs. licencia** | ¿Se cede la titularidad o se licencia el uso? |
| **Exclusividad** | ¿Es exclusiva o no exclusiva? |
| **Territorio** | ¿Limitación geográfica? (España, UE, mundial) |
| **Duración** | ¿Temporal o por toda la vigencia de los derechos? |
| **Modalidades** | ¿Qué derechos se ceden? (reproducción, distribución, comunicación pública, transformación) |
| **Sublicencia** | ¿Se permite sublicenciar? |
| **Contraprestación** | ¿Se establece precio o se incluye en el precio del contrato? |
| **Reversión** | ¿Qué ocurre con la PI al terminar el contrato? |

### Paso 3 — Verificar conformidad legal

**Software (art. 97 LPI):**
- Si es empleado: el empresario es titular de los derechos de explotación (art. 97.4 LPI) salvo pacto en contrario.
- Si es autónomo/encargo: se rige por el contrato — no hay presunción de cesión.

**Obras no software:**
- Art. 51 LPI: la transmisión entre vivos se limita a las modalidades expresamente cedidas.
- Art. 14 LPI: los derechos morales son irrenunciables e inalienables.

**Invenciones laborales (Ley de Patentes 24/2015):**
- Art. 15: invenciones del trabajador — pertenecen al empresario si son resultado de su actividad investigadora.
- Art. 16: invenciones libres del trabajador — le pertenecen.
- Art. 17: compensación económica al trabajador inventor.

### Paso 4 — Generar informe

## Formato de salida

```markdown
## Revisión de cláusulas de PI

**Contrato:** [nombre]
**Tipo de contrato:** [prestación de servicios / laboral / licencia / colaboración / I+D]
**Fecha de revisión:** [fecha]

### Tabla de análisis

| Cláusula | Tipo | Exclusividad | Territorio | Duración | Modalidades | Conforme | Observaciones |
|----------|------|-------------|------------|----------|-------------|----------|---------------|
| [ref] | Cesión/Licencia | Sí/No | [territorio] | [duración] | [lista] | [SÍ/NO] | [detalle] |

### Problemas detectados

| # | Cláusula | Problema | Base legal | Severidad | Recomendación |
|---|----------|----------|------------|-----------|---------------|
| 1 | [ref] | [descripción] | [art. X LPI] | [nivel] | [acción] |

### PI preexistente

[Análisis de si se delimita correctamente la PI preexistente y la generada]

### Derechos morales

[Verificar que no se incluyen renuncias a derechos morales — nulas por ley]

### Recomendaciones

[Acciones concretas para corregir o mejorar las cláusulas]
```

## Referencias normativas

- **LPI** (RDL 1/1996): Ley de Propiedad Intelectual.
- **LPI art. 14**: Derechos morales irrenunciables.
- **LPI art. 43**: Transmisión inter vivos — formalidades y limitaciones.
- **LPI art. 51**: Transmisión de derechos — presunción de cesión limitada.
- **LPI arts. 95-104**: Programas de ordenador.
- **LPI art. 97.4**: Titularidad del software creado en relación laboral.
- **Ley de Patentes 24/2015**: arts. 15-17 (invenciones laborales).
- **CC arts. 1254 y ss.**: Teoría general de contratos.

## Guardrails

- **NO** redacta cláusulas de PI alternativas — solo identifica problemas y recomienda.
- **NO** determina la titularidad de derechos de PI en caso de disputa.
- **NO** valora la adecuación comercial de la cesión/licencia.
- **ESCALAR** si el contrato contiene renuncia a derechos morales (nula por ley).
- **ESCALAR** si la cesión de PI en un contrato laboral no respeta los arts. 15-17 Ley de Patentes.
- **AVISAR** si el contrato no distingue entre PI preexistente y PI generada.
- **AVISAR** si no se establece qué ocurre con la PI a la terminación del contrato.
