---
name: eipd-proteccion-datos-betobetico
title: /eipd
description: 'Realiza una Evaluación de Impacto en la Protección de Datos (EIPD/DPIA) siguiendo la metodología de la ANTAI y la Ley 81 de 2019. Cubre: descripción del tratamiento, evaluación de necesidad y proporcionalidad, evaluación de riesgos y medidas de mitigación. Usar cuando el usuario dice "evaluación de impacto", "EIPD", "DPIA", "análisis de riesgos de privacidad", o cuando un tratamiento entrañe probablemente un alto riesgo para los titulares.'
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/proteccion-datos/skills/eipd
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: data-protection
language: es
---

# /eipd

1. Leer `~/.claude/plugins/config/claude-para-abogados/proteccion-datos/CLAUDE.md` — perfil de práctica.
2. Determinar si conviene la EIPD (buena práctica voluntaria, art. 8 de la Ley 81 de 2019; obligatoria solo si la ANTAI la ordena, art. 41 del Decreto Ejecutivo 285 de 2021; factores de riesgo en el art. 36).
3. Ejecutar la evaluación siguiendo la metodología de la ANTAI.
4. Producir el documento EIPD completo.

---

## Propósito

Producir un documento de EIPD completo que cumpla los requisitos de la Ley 81 de 2019 y el Decreto Ejecutivo 285 de 2021, siguiendo la metodología y guías de la ANTAI. En Panamá la EIPD está definida (Decreto Ejecutivo 285 de 2021, art. 1.9) pero **NO es obligatoria con carácter general** (no rige el modelo del art. 35 del RGPD): es una **buena práctica voluntaria** del responsable (art. 8 de la Ley 81 de 2019) y **solo deviene exigible si la ANTAI la ORDENA** en función de la gravedad del riesgo o la novedad tecnológica (art. 41 del Decreto Ejecutivo 285 de 2021).

## Cuándo conviene la EIPD

No hay una lista cerrada de "supuestos de alto riesgo" que obliguen a EIPD: el Decreto Ejecutivo 285 de 2021 fija **9 factores de evaluación del riesgo (art. 36)** y la ANTAI puede ordenar la EIPD (art. 41).

### Factores de riesgo a valorar (art. 36 del Decreto Ejecutivo 285 de 2021)

- Evaluación sistemática y exhaustiva de aspectos personales (perfilado con efectos significativos para el titular).
- Tratamiento a gran escala de datos sensibles.
- Observación sistemática a gran escala de una zona de acceso público (videovigilancia masiva).

### Tratamientos típicos que justifican una EIPD

Entre otros:

- Tratamientos que impliquen perfilado con efectos significativos.
- Tratamientos a gran escala de datos genéticos, biométricos o de salud.
- Uso de tecnologías invasivas (geolocalización, videovigilancia con reconocimiento facial).
- Tratamientos masivos de datos de menores.
- Tratamientos que impliquen transferencias internacionales a destinos que no ofrezcan un nivel de protección equivalente o superior (Ley 81 de 2019 y Decreto Ejecutivo 285 de 2021).

### Criterio de los "dos de nueve"

Como referencia comparada internacional (no vinculante en Panamá), las directrices del GT29/EDPB establecen que si un tratamiento cumple dos o más de estos nueve criterios, es probable que requiera EIPD:

1. Evaluación o puntuación (scoring, perfilado).
2. Toma de decisiones automatizadas con efectos jurídicos.
3. Observación sistemática.
4. Datos sensibles o altamente personales.
5. Datos tratados a gran escala.
6. Combinación o cruce de conjuntos de datos.
7. Datos de personas vulnerables (menores, empleados, pacientes).
8. Uso innovador de tecnologías.
9. Que el tratamiento impida ejercer un derecho o acceder a un servicio.

## Estructura de la EIPD (metodología ANTAI)

### Fase 1: Descripción del tratamiento

- Naturaleza: qué datos se recogen, cómo se tratan, quién tiene acceso.
- Alcance: volumen de datos, categorías de interesados, ámbito geográfico.
- Contexto: relación con los interesados, expectativas razonables.
- Finalidad: para qué se tratan y beneficios esperados.

### Fase 2: Evaluación de necesidad y proporcionalidad

| Principio | Pregunta clave | Evaluación |
|---|---|---|
| Limitación de finalidad | Son las finalidades concretas, explícitas y legítimas? | [sí/no — detalle] |
| Minimización / proporcionalidad | Se recogen solo los datos necesarios? | [sí/no — detalle] |
| Exactitud y calidad | Se garantiza la calidad de los datos? | [sí/no — detalle] |
| Limitación de conservación | Hay plazos definidos y justificados? | [sí/no — detalle] |
| Base de legitimación | Es adecuada y suficiente? | [sí/no — detalle] |
| Derechos de los titulares | Se garantiza el ejercicio efectivo? | [sí/no — detalle] |

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
BORRADOR — EVALUACIÓN DE IMPACTO EN PROTECCIÓN DE DATOS — REVISIÓN OBLIGATORIA DEL RESPONSABLE DE PROTECCIÓN DE DATOS

> **Nota para el revisor**
> - **Tratamiento evaluado:** [nombre]
> - **EIPD:** [voluntaria — buena práctica / ordenada por la ANTAI ex art. 41 del Decreto Ejecutivo 285 de 2021]
> - **Riesgos altos/muy altos identificados:** [N]
> - **Antes de actuar:** validar evaluación de riesgos con el responsable de protección de datos y con IT. Nota: en Panamá NO existe la "consulta previa" a la ANTAI del art. 36 del RGPD; si el riesgo residual sigue siendo alto, reforzar las medidas (la ANTAI puede ordenar una EIPD ex art. 41).

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
**Decisión recomendada:** [proceder con medidas / reforzar medidas si el riesgo residual sigue siendo alto / no proceder] (en Panamá no existe la "consulta previa" a la ANTAI del RGPD; la ANTAI puede ordenar la EIPD ex art. 41 del Decreto Ejecutivo 285 de 2021)

---

**Qué hacer a continuación:**
1. **Implementar medidas** — detallo las medidas técnicas y organizativas.
2. **Reforzar medidas** — si el riesgo residual sigue siendo alto (en Panamá no existe la "consulta previa" del RGPD; la ANTAI puede ordenar la EIPD ex art. 41 del Decreto Ejecutivo 285 de 2021).
3. **Actualizar RAT** — `/proteccion-datos:rat` para reflejar este tratamiento.
4. **Otra cosa** — dime qué necesitas.
```

## Referencias legislativas

- **Ley 81 de 2019** — principios de tratamiento; datos sensibles (art. 4; régimen reforzado art. 13); la EIPD como buena práctica voluntaria del responsable (art. 8).
- **Decreto Ejecutivo 285 de 2021** — reglamento; definición de EIPD (art. 1.9); factores de evaluación del riesgo (art. 36); la ANTAI puede ordenar la EIPD (art. 41).
- **Guías de la ANTAI** — metodología de referencia para análisis de riesgos y EIPD.
- **Referencia comparada internacional:** Directrices del GT29/EDPB sobre EIPD (WP 248 rev.01), no vinculantes en Panamá.

## Guardarraíles

- **La EIPD no es un trámite — es un análisis real.** Si el usuario quiere una EIPD "de relleno", advertir que una EIPD que no refleja los riesgos reales es peor que no tenerla (evidencia de que se conocían los riesgos y se ignoraron).
- **Si el riesgo residual es alto tras las medidas, reforzar las medidas y documentarlo.** En Panamá no existe la "consulta previa" a la ANTAI del RGPD; la ANTAI puede ordenar una EIPD (art. 41 del Decreto Ejecutivo 285 de 2021).
- **No inventar riesgos ni medidas genéricas.** Los riesgos deben ser específicos del tratamiento evaluado.
- **La EIPD debe hacerse ANTES de iniciar el tratamiento.** Si el tratamiento ya está en marcha, señalar que la EIPD es extemporánea pero sigue siendo necesaria.
- **Involucrar al responsable de protección de datos.** Si la organización lo tiene designado, el documento debe pasar por su revisión.
