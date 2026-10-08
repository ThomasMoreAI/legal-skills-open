---
name: aepd-betobetico
title: /aepd
description: 'Gestiona la relación con la Agencia Española de Protección de Datos: reclamaciones recibidas, información previa al procedimiento sancionador, procedimientos sancionadores y recursos. Incluye plazos de respuesta, opciones estratégicas y preparación de alegaciones. Usar cuando el usuario dice "reclamación AEPD", "expediente AEPD", "procedimiento sancionador", "nos ha llegado un requerimiento de la AEPD", o necesita gestionar cualquier actuación de la AEPD.'
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/proteccion-datos/skills/aepd
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: data-protection
language: es
---

# /aepd

1. Leer `~/.claude/plugins/config/claude-para-abogados/proteccion-datos/CLAUDE.md` — perfil de práctica.
2. Identificar el tipo de actuación de la AEPD.
3. Evaluar la situación y opciones.
4. Generar estrategia y borrador de respuesta.

---

## Propósito

Orientar la respuesta ante actuaciones de la AEPD, desde la reclamación inicial hasta el procedimiento sancionador, incluyendo plazos, opciones estratégicas y preparación de escritos. Es un apoyo — la estrategia final requiere decisión letrada.

## Tipos de actuaciones de la AEPD

### 1. Reclamación de un interesado

- **Qué es:** un ciudadano presenta reclamación ante la AEPD por presunta vulneración de sus derechos.
- **Plazo de traslado:** la AEPD traslada la reclamación al responsable y le da **1 mes** para responder.
- **Opciones:** resolver la reclamación (satisfacer al reclamante), contestar con alegaciones, o no contestar (peor opción).

### 2. Actuaciones previas de investigación (art. 67 LOPDGDD)

- **Qué es:** la AEPD investiga de oficio o a instancia de parte antes de decidir si inicia procedimiento sancionador.
- **Requerimientos de información:** la AEPD puede requerir información, documentación o acceso a instalaciones.
- **Plazo de respuesta:** el que fije el requerimiento (habitualmente 10-15 días hábiles).
- **Obligación de colaborar:** la falta de colaboración es infracción (art. 73.o LOPDGDD).

### 3. Procedimiento sancionador

#### Acuerdo de inicio (art. 68 LOPDGDD)

- **Notificación:** la AEPD notifica el acuerdo de inicio con los hechos, la calificación provisional y la sanción propuesta.
- **Plazo de alegaciones:** **15 días hábiles** desde la notificación.
- **Opciones:**
  - Presentar alegaciones (rebatir hechos, calificación o sanción).
  - Reconocer la responsabilidad (reducción del 20% de la sanción — art. 85 LPACAP).
  - Pago voluntario (reducción del 20% — acumulable con el reconocimiento para un total del 36%).

#### Propuesta de resolución

- **Plazo de alegaciones:** **15 días hábiles** si difiere del acuerdo de inicio.
- **Opciones:** alegar, aceptar, o recurrir tras la resolución.

#### Resolución

- **Recurso potestativo de reposición:** 1 mes ante la propia AEPD.
- **Recurso contencioso-administrativo:** 2 meses ante la Audiencia Nacional.

## Régimen sancionador (LOPDGDD arts. 70-78)

### Clasificación de infracciones

| Tipo | Prescripción | Sanción máxima | Ejemplos |
|---|---|---|---|
| Leve (art. 74) | 1 año | Apercibimiento / hasta 40.000 EUR | Incumplimientos formales menores |
| Grave (art. 73) | 2 años | Hasta 300.000 EUR | No notificar brechas, no realizar EIPD, obstaculizar derechos ARCO |
| Muy grave (art. 72) | 3 años | Hasta 20.000.000 EUR o 4% facturación | Tratamiento sin base jurídica, TI sin garantías, obstaculización a la AEPD |

### Criterios de graduación (art. 83.2 RGPD)

- Naturaleza, gravedad y duración de la infracción.
- Intencionalidad o negligencia.
- Medidas adoptadas para mitigar.
- Categorías de datos afectados.
- Infractores reincidentes.
- Grado de cooperación con la AEPD.
- Adhesión a códigos de conducta o certificaciones.

## Estrategia de respuesta

### Ante reclamación

| Escenario | Estrategia recomendada |
|---|---|
| Infracción clara y subsanable | Resolver la reclamación antes de que la AEPD actúe — reduce enormemente el riesgo de sanción |
| Infracción discutible | Contestar con alegaciones fundamentadas + evidencia de cumplimiento |
| Sin infracción | Contestar demostrando cumplimiento con documentación |

### Ante procedimiento sancionador

| Escenario | Estrategia recomendada |
|---|---|
| Infracción clara, sanción proporcionada | Valorar pago voluntario + reconocimiento (36% reducción) |
| Infracción clara, sanción desproporcionada | Alegar sobre la graduación de la sanción |
| Infracción discutible | Alegar sobre los hechos y la calificación jurídica |
| Sin infracción | Alegar con toda la prueba disponible |

## Formato de salida

```markdown
BORRADOR — RESPUESTA A ACTUACIÓN AEPD — REVISIÓN LETRADA OBLIGATORIA

> **Nota para el revisor**
> - **Tipo de actuación:** [reclamación / actuaciones previas / procedimiento sancionador]
> - **Expediente AEPD:** [n.o de expediente]
> - **Plazo de respuesta:** [fecha límite]
> - **Antes de actuar:** verificar plazo exacto; revisar toda la documentación del expediente; validar estrategia con letrado.

## Análisis del expediente AEPD: [N.o expediente]

### Resumen

| Campo | Valor |
|---|---|
| Tipo de actuación | [tipo] |
| Fecha de notificación | [fecha] |
| Plazo de respuesta | [fecha — VERIFICAR] |
| Infracción imputada | [artículos] |
| Sanción propuesta (si aplica) | [importe] |

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
3. **Calcular reducción** — si procede pago voluntario/reconocimiento.
4. **Recurso** — si hay resolución, preparo recurso de reposición o contencioso.
5. **Otra cosa** — dime qué necesitas.
```

## Referencias legislativas

- **RGPD arts. 77-84** — recursos, responsabilidad y sanciones.
- **RGPD art. 83** — condiciones generales para la imposición de multas.
- **LOPDGDD arts. 63-78** — régimen sancionador.
- **LOPDGDD art. 65** — actuaciones previas de investigación.
- **LOPDGDD arts. 72-74** — infracciones leves, graves y muy graves.
- **LPACAP (Ley 39/2015) art. 85** — terminación en procedimientos sancionadores.

## Guardarraíles

- **Los plazos son preclusivos.** Pasado el plazo de alegaciones, se pierde la oportunidad. Marcar siempre `[VERIFICAR PLAZO]`.
- **No ignorar requerimientos de la AEPD.** La falta de colaboración es infracción grave (art. 73.o LOPDGDD) y agrava cualquier sanción.
- **La reducción del 36% (reconocimiento + pago voluntario) es irrenunciable después.** Asegurarse de que el cliente entiende que renuncia a recurrir.
- **No inventar prueba de cumplimiento.** Si no hay RAT, EIPD, cláusulas informativas o contratos de encargado, no fingir que sí los hay — la AEPD lo descubrirá y agravará la sanción.
- **Ante sanciones elevadas, derivar siempre a letrado especializado.** Este skill orienta, pero un procedimiento sancionador de la AEPD con sanción significativa requiere defensa letrada especializada.
- **No aconsejar "no pasa nada".** Las sanciones de la AEPD son reales y ejecutivas. Tomárselas en serio.
