---
name: eipd-proteccion-datos-1943-betobetico
title: /eipd
description: 'Realiza una Evaluación de Impacto en la Protección de Datos (EIPD/DPIA) siguiendo la metodología de la AEPD. Cubre: descripción del tratamiento, evaluación de necesidad y proporcionalidad, evaluación de riesgos y medidas de mitigación. Usar cuando el usuario dice "evaluación de impacto", "EIPD", "DPIA", "análisis de riesgos de privacidad", o cuando un tratamiento cumple los criterios del art. 35 RGPD.'
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/proteccion-datos/skills/eipd
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: data-protection
language: es
---

# /eipd

1. Leer `~/.claude/plugins/config/claude-para-abogados/proteccion-datos/CLAUDE.md` — perfil de práctica.
2. Determinar si la EIPD es obligatoria (art. 35 RGPD + lista AEPD).
3. Ejecutar la evaluación siguiendo la metodología AEPD.
4. Producir el documento EIPD completo.

---

## Propósito

Producir un documento de EIPD completo que cumpla los requisitos del art. 35 RGPD, siguiendo la metodología y guía de la AEPD. La EIPD es obligatoria cuando un tratamiento "entrañe probablemente un alto riesgo" para los derechos y libertades de las personas.

## Cuándo es obligatoria (art. 35.3 RGPD + lista AEPD)

### Supuestos del art. 35.3 RGPD

- Evaluación sistemática y exhaustiva de aspectos personales (perfilado con efectos jurídicos).
- Tratamiento a gran escala de categorías especiales (art. 9) o datos penales (art. 10).
- Observación sistemática a gran escala de una zona de acceso público (videovigilancia masiva).

### Lista obligatoria de la AEPD (art. 35.4 RGPD)

La AEPD publicó una lista de tratamientos que requieren EIPD obligatoria. Incluye, entre otros:

- Tratamientos que impliquen perfilado con efectos significativos.
- Tratamientos a gran escala de datos genéticos, biométricos o de salud.
- Uso de tecnologías invasivas (geolocalización, videovigilancia con reconocimiento facial).
- Tratamientos masivos de datos de menores.
- Tratamientos que impliquen transferencias internacionales a países sin adecuación.

### Criterio de los "dos de nueve"

Las directrices del GT29/EDPB establecen que si un tratamiento cumple dos o más de estos nueve criterios, es probable que requiera EIPD:

1. Evaluación o puntuación (scoring, perfilado).
2. Toma de decisiones automatizadas con efectos jurídicos.
3. Observación sistemática.
4. Datos sensibles o altamente personales.
5. Datos tratados a gran escala.
6. Combinación o cruce de conjuntos de datos.
7. Datos de personas vulnerables (menores, empleados, pacientes).
8. Uso innovador de tecnologías.
9. Que el tratamiento impida ejercer un derecho o acceder a un servicio.

## Estructura de la EIPD (metodología AEPD)

### Fase 1: Descripción del tratamiento

- Naturaleza: qué datos se recogen, cómo se tratan, quién tiene acceso.
- Alcance: volumen de datos, categorías de interesados, ámbito geográfico.
- Contexto: relación con los interesados, expectativas razonables.
- Finalidad: para qué se tratan y beneficios esperados.

### Fase 2: Evaluación de necesidad y proporcionalidad

| Principio | Pregunta clave | Evaluación |
|---|---|---|
| Limitación de finalidad (art. 5.1.b) | Son las finalidades concretas, explícitas y legítimas? | [sí/no — detalle] |
| Minimización (art. 5.1.c) | Se recogen solo los datos necesarios? | [sí/no — detalle] |
| Exactitud (art. 5.1.d) | Se garantiza la calidad de los datos? | [sí/no — detalle] |
| Limitación de conservación (art. 5.1.e) | Hay plazos definidos y justificados? | [sí/no — detalle] |
| Base jurídica (art. 6) | Es adecuada y suficiente? | [sí/no — detalle] |
| Derechos de los interesados | Se garantiza el ejercicio efectivo? | [sí/no — detalle] |

### Fase 3: Evaluación de riesgos

Para cada riesgo identificado:

| Riesgo | Descripción | Probabilidad | Impacto | Nivel de riesgo |
|---|---|---|---|---|
| [identificador] | [descripción] | Baja/Media/Alta/Muy alta | Bajo/Medio/Alto/Muy alto | [resultado de la matriz] |

**Matriz de riesgo (probabilidad x impacto):**

| | Impacto bajo | Impacto medio | Impacto alto | Impacto muy alto |
|---|---|---|---|---|
| **Prob. baja** | Bajo | Bajo | Medio | Alto |
| **Prob. media** | Bajo | Medio | Alto | Alto |
| **Prob. alta** | Medio | Alto | Alto | Muy alto |
| **Prob. muy alta** | Alto | Alto | Muy alto | Muy alto |

### Fase 4: Medidas de mitigación

Para cada riesgo con nivel medio o superior:

| Riesgo | Medida de mitigación | Responsable | Plazo | Riesgo residual |
|---|---|---|---|---|
| [id] | [medida] | [quién] | [cuándo] | [nivel tras mitigación] |

## Formato de salida

```markdown
BORRADOR — EVALUACIÓN DE IMPACTO EN PROTECCIÓN DE DATOS — REVISIÓN DPD OBLIGATORIA

> **Nota para el revisor**
> - **Tratamiento evaluado:** [nombre]
> - **EIPD obligatoria:** [sí — motivo / recomendable]
> - **Riesgos altos/muy altos identificados:** [N]
> - **Antes de actuar:** validar evaluación de riesgos con DPD y con IT; consultar con AEPD si el riesgo residual sigue siendo alto (art. 36 RGPD — consulta previa).

## EIPD: [Nombre del tratamiento]

### 1. Descripción del tratamiento
[Fase 1 completa]

### 2. Necesidad y proporcionalidad
[Fase 2 — tabla de evaluación]

### 3. Evaluación de riesgos
[Fase 3 — riesgos identificados con matriz]

### 4. Medidas de mitigación
[Fase 4 — medidas propuestas]

### 5. Conclusión y decisión

**Riesgo residual global:** [bajo/medio/alto/muy alto]
**Decisión recomendada:** [proceder con medidas / consulta previa a AEPD (art. 36) / no proceder]

---

**Qué hacer a continuación:**
1. **Implementar medidas** — detallo las medidas técnicas y organizativas.
2. **Consulta previa AEPD** — si el riesgo residual es alto, preparo la solicitud del art. 36.
3. **Actualizar RAT** — `/proteccion-datos:rat` para reflejar este tratamiento.
4. **Otra cosa** — dime qué necesitas.
```

## Referencias legislativas

- **RGPD art. 35** — evaluación de impacto relativa a la protección de datos.
- **RGPD art. 36** — consulta previa a la autoridad de control.
- **Lista obligatoria de la AEPD** — tratamientos que requieren EIPD (publicada conforme al art. 35.4).
- **Guía práctica de análisis de riesgos y EIPD de la AEPD** — metodología de referencia.
- **Directrices del GT29/EDPB sobre EIPD (WP 248 rev.01).**

## Guardarraíles

- **La EIPD no es un trámite — es un análisis real.** Si el usuario quiere una EIPD "de relleno", advertir que una EIPD que no refleja los riesgos reales es peor que no tenerla (evidencia de que se conocían los riesgos y se ignoraron).
- **Si el riesgo residual es alto tras las medidas, hay que consultar a la AEPD (art. 36 RGPD).** No es opcional.
- **No inventar riesgos ni medidas genéricas.** Los riesgos deben ser específicos del tratamiento evaluado.
- **La EIPD debe hacerse ANTES de iniciar el tratamiento.** Si el tratamiento ya está en marcha, señalar que la EIPD es extemporánea pero sigue siendo necesaria.
- **Involucrar al DPD.** El art. 35.2 RGPD exige recabar el asesoramiento del DPD. Si la organización tiene DPD, el documento debe pasar por su revisión.
