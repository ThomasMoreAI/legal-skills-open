---
name: antai-betobetico
title: /antai
description: 'Gestiona la relación con la Autoridad Nacional de Transparencia y Acceso a la Información (ANTAI): reclamaciones recibidas, actuaciones previas de investigación, procedimientos sancionadores y recursos. Incluye plazos de respuesta, opciones estratégicas y preparación de alegaciones. Usar cuando el usuario dice "reclamación ANTAI", "expediente ANTAI", "procedimiento sancionador", "nos ha llegado un requerimiento de la ANTAI", o necesita gestionar cualquier actuación de la ANTAI.'
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/proteccion-datos/skills/antai
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: data-protection
language: es
---

# /antai

1. Leer `~/.claude/plugins/config/claude-para-abogados/proteccion-datos/CLAUDE.md` — perfil de práctica.
2. Identificar el tipo de actuación de la ANTAI.
3. Evaluar la situación y opciones.
4. Generar estrategia y borrador de respuesta.

---

## Propósito

Orientar la respuesta ante actuaciones de la ANTAI, desde la reclamación inicial hasta el procedimiento sancionador, incluyendo plazos, opciones estratégicas y preparación de escritos. Es un apoyo — la estrategia final requiere decisión letrada.

## Tipos de actuaciones de la ANTAI

### 1. Reclamación de un titular

- **Qué es:** un ciudadano presenta reclamación ante la ANTAI por presunta vulneración de sus derechos como titular de datos personales.
- **Plazo de traslado:** la ANTAI traslada la reclamación al responsable y le otorga un plazo para responder [verificar].
- **Opciones:** resolver la reclamación (satisfacer al reclamante), contestar con alegaciones, o no contestar (peor opción).

### 2. Actuaciones previas de investigación

- **Qué es:** la ANTAI investiga de oficio o a instancia de parte antes de decidir si inicia procedimiento sancionador [verificar].
- **Requerimientos de información:** la ANTAI puede requerir información, documentación o acceso a instalaciones.
- **Plazo de respuesta:** el que fije el requerimiento [verificar].
- **Obligación de colaborar:** la falta de colaboración puede constituir infracción [verificar].

### 3. Procedimiento sancionador

#### Acuerdo de inicio

- **Notificación:** la ANTAI notifica el acuerdo de inicio con los hechos, la calificación provisional y la sanción propuesta [verificar].
- **Plazo de alegaciones:** el plazo legal desde la notificación [verificar].
- **Opciones:**
  - Presentar alegaciones (rebatir hechos, calificación o sanción).
  - Subsanar y acreditar el cumplimiento, si procede [verificar].

#### Propuesta de resolución

- **Plazo de alegaciones:** el plazo legal si difiere del acuerdo de inicio [verificar].
- **Opciones:** alegar, aceptar, o recurrir tras la resolución.

#### Resolución

- **Recurso de reconsideración** ante la Dirección que dictó el acto.
- **Recurso de apelación ante el director general de la ANTAI** (segunda instancia administrativa).
- Agotada la vía gubernativa, **demanda contencioso-administrativa ante la Sala Tercera de lo Contencioso-Administrativo de la Corte Suprema de Justicia**.

## Régimen sancionador (Ley 81 de 2019 y Decreto Ejecutivo 285 de 2021)

### Clasificación de infracciones

Multas de **B/.1.000,00 a B/.10.000,00** (balboa = USD 1:1), según gravedad y reincidencia; además, amonestación, cierre del registro de la base de datos y suspensión/inhabilitación de las actividades de tratamiento.

| Tipo | Prescripción de la infracción | Sanción (rango B/.1.000-10.000) | Ejemplos |
|---|---|---|---|
| Leve | 1 año (verificar el desglose en el Decreto 285) | Tramo inferior del rango B/.1.000-10.000 | Incumplimientos formales menores |
| Grave | 3 años (verificar el desglose en el Decreto 285) | Tramo intermedio del rango B/.1.000-10.000 | No notificar brechas, obstaculizar derechos del titular |
| Muy grave | 5 años (verificar el desglose en el Decreto 285) | Tramo superior del rango B/.1.000-10.000 | Tratamiento sin base de legitimación, transferencias internacionales sin garantías, obstaculización a la ANTAI |

*Prescripción de las sanciones (confianza media; verificar el desglose en el Decreto 285): leves 3 años, graves 5 años, muy graves imprescriptibles.*

### Criterios de graduación

- Naturaleza, gravedad y duración de la infracción.
- Intencionalidad o negligencia.
- Medidas adoptadas para mitigar.
- Categorías de datos afectados.
- Infractores reincidentes.
- Grado de cooperación con la ANTAI.
- Adhesión a códigos de conducta o certificaciones.

## Estrategia de respuesta

### Ante reclamación

| Escenario | Estrategia recomendada |
|---|---|
| Infracción clara y subsanable | Resolver la reclamación antes de que la ANTAI actúe — reduce enormemente el riesgo de sanción |
| Infracción discutible | Contestar con alegaciones fundamentadas + evidencia de cumplimiento |
| Sin infracción | Contestar demostrando cumplimiento con documentación |

### Ante procedimiento sancionador

| Escenario | Estrategia recomendada |
|---|---|
| Infracción clara, sanción proporcionada | Valorar subsanación y reconocimiento, si la ley lo permite con atenuación [verificar] |
| Infracción clara, sanción desproporcionada | Alegar sobre la graduación de la sanción |
| Infracción discutible | Alegar sobre los hechos y la calificación jurídica |
| Sin infracción | Alegar con toda la prueba disponible |

## Formato de salida

```markdown
BORRADOR — RESPUESTA A ACTUACIÓN ANTAI — REVISIÓN LETRADA OBLIGATORIA

> **Nota para el revisor**
> - **Tipo de actuación:** [reclamación / actuaciones previas / procedimiento sancionador]
> - **Expediente ANTAI:** [n.o de expediente]
> - **Plazo de respuesta:** [fecha límite]
> - **Antes de actuar:** verificar plazo exacto; revisar toda la documentación del expediente; validar estrategia con letrado.

## Análisis del expediente ANTAI: [N.o expediente]

### Resumen

| Campo | Valor |
|---|---|
| Tipo de actuación | [tipo] |
| Fecha de notificación | [fecha] |
| Plazo de respuesta | [fecha — VERIFICAR] |
| Infracción imputada | [artículos de la Ley 81 de 2019 / Decreto Ejecutivo 285 de 2021] |
| Sanción propuesta (si aplica) | [importe en USD/B/.] |

### Análisis de los hechos

[Análisis de los hechos imputados vs. la realidad documentada]

### Opciones estratégicas

| Opción | Ventajas | Riesgos | Coste estimado |
|---|---|---|---|
| [opción 1] | [ventajas] | [riesgos] | [coste] |
| [opción 2] | [ventajas] | [riesgos] | [coste] |

### Borrador de escrito de alegaciones / respuesta

[Borrador estructurado con hechos, fundamentos de derecho y petición]

---

**Qué hacer a continuación:**
1. **Completar alegaciones** — relleno con la documentación que aportes.
2. **Preparar prueba** — listo la documentación acreditativa del cumplimiento.
3. **Valorar atenuantes** — si procede subsanación o reconocimiento con atenuación [verificar].
4. **Recurso** — si hay resolución, preparo recurso de reconsideración, apelación ante el director general de la ANTAI y, agotada la vía gubernativa, demanda contencioso-administrativa ante la Sala Tercera de la CSJ.
5. **Otra cosa** — dime qué necesitas.
```

## Referencias legislativas

- **Ley 81 de 2019** — derechos de los titulares; la ANTAI como autoridad de control (arts. 31-33); régimen de infracciones (leves, graves y muy graves); entrada en vigor el 29 de marzo de 2021 (art. 44).
- **Decreto Ejecutivo 285 de 2021** — reglamento; procedimiento sancionador, graduación de sanciones y multas de B/.1.000,00 a B/.10.000,00.
- **Ley 38 de 2000** — procedimiento administrativo general, supletoriamente aplicable.
- **Código Judicial de Panamá** — demanda contencioso-administrativa ante la Sala Tercera de la CSJ, agotada la vía gubernativa (reconsideración y apelación ante el director general de la ANTAI).

## Guardarraíles

- **Los plazos son preclusivos.** Pasado el plazo de alegaciones, se pierde la oportunidad. Marcar siempre `[VERIFICAR PLAZO]`.
- **No ignorar requerimientos de la ANTAI.** La falta de colaboración puede agravar cualquier sanción [verificar].
- **No inventar prueba de cumplimiento.** Si no hay RAT, EIPD, cláusulas informativas o contratos de custodio/encargado, no fingir que sí los hay — la ANTAI lo descubrirá y agravará la sanción.
- **Ante sanciones elevadas, derivar siempre a letrado especializado.** Este skill orienta, pero un procedimiento sancionador de la ANTAI con sanción significativa requiere defensa letrada especializada.
- **No aconsejar "no pasa nada".** Las sanciones de la ANTAI son reales y ejecutivas. Tomárselas en serio.
