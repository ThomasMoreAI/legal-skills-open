---
name: irac
title: /irac
description: 'Evalúa el análisis de caso del estudiante usando la estructura IRAC. Rúbrica: identificación del problema (25%), regulación (25%), aplicación (35%), conclusión (15%). Da feedback específico y accionable — NUNCA reescribe el análisis del estudiante. Usar cuando el usuario dice "evalúa mi IRAC", "corrige mi análisis", "revisa mi caso práctico", o presenta un análisis de caso para evaluación.'
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/estudiante-derecho/skills/irac
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: es
---

# /irac

1. Leer `~/.claude/plugins/config/claude-para-abogados/estudiante-derecho/CLAUDE.md` — perfil del estudiante.
2. Recibir el análisis IRAC del estudiante.
3. Evaluar con la rúbrica.
4. Producir feedback.

---

## Propósito

Evaluar el análisis de caso del estudiante con una rúbrica estructurada, proporcionando feedback específico que le ayude a mejorar. No reescribir — el objetivo es que el estudiante mejore su propio análisis.

## REGLA CARDINAL

> **NUNCA reescribas el análisis.** Señala qué falta, qué sobra, qué está mal argumentado y por qué. Pero la reescritura la hace el estudiante. Si reescribes, el estudiante no aprende a escribir.

## Rúbrica de evaluación

### I — Identificación del problema (25%)

| Criterio | 0-2 | 3-5 | 6-8 | 9-10 |
|---|---|---|---|---|
| Formulación como pregunta jurídica | No identifica el problema | Identifica vagamente | Identifica correctamente pero formulación imprecisa | Pregunta jurídica precisa y bien delimitada |
| Completitud | Ignora cuestiones relevantes | Identifica la principal | Identifica principal y alguna secundaria | Identifica todas las cuestiones relevantes |
| Priorización | Sin orden | Mezcla principal con secundarias | Ordena pero con errores | Prioriza correctamente por relevancia |

**Puntuación I:** [X] / 10 (peso: 25%)

### R — Regulación aplicable (25%)

| Criterio | 0-2 | 3-5 | 6-8 | 9-10 |
|---|---|---|---|---|
| Identificación de normas | Norma incorrecta o ausente | Norma correcta pero artículo vago | Artículos correctos | Artículos precisos + jurisprudencia relevante |
| Comprensión de la norma | Cita sin entender | Entiende parcialmente | Entiende la regla general | Entiende la regla, las excepciones y los matices |
| Jerarquía de fuentes | Ignora | Mezcla niveles | Correcta pero incompleta | Correcta y completa |

**Puntuación R:** [X] / 10 (peso: 25%)

### A — Aplicación al caso (35%)

| Criterio | 0-2 | 3-5 | 6-8 | 9-10 |
|---|---|---|---|---|
| Subsunción | No conecta hechos con norma | Conexión superficial | Subsunción correcta pero mecánica | Subsunción rigurosa y argumentada |
| Argumentación | Afirma sin argumentar | Argumenta parcialmente | Argumenta en una dirección | Argumenta en ambas direcciones |
| Hechos relevantes | Ignora hechos clave | Usa algunos hechos | Usa la mayoría | Identifica y usa todos los hechos relevantes |
| Contraargumentos | Ausentes | Menciona | Desarrolla parcialmente | Anticipa y rebate contraargumentos |

**Puntuación A:** [X] / 10 (peso: 35%)

### C — Conclusión (15%)

| Criterio | 0-2 | 3-5 | 6-8 | 9-10 |
|---|---|---|---|---|
| Coherencia con el análisis | Contradice lo anterior | Parcialmente coherente | Coherente | Fluye naturalmente del análisis |
| Concreción | Vaga o genérica | Parcialmente concreta | Concreta | Concreta y con nivel de confianza |
| Recomendación práctica | Ausente | Genérica | Razonable | Específica y accionable |

**Puntuación C:** [X] / 10 (peso: 15%)

## Formato de salida

```markdown
## Evaluación IRAC: [Tema del caso]

### Puntuación global

| Sección | Puntuación | Peso | Ponderada |
|---|---|---|---|
| I — Identificación | [X] / 10 | 25% | [X] |
| R — Regulación | [X] / 10 | 25% | [X] |
| A — Aplicación | [X] / 10 | 35% | [X] |
| C — Conclusión | [X] / 10 | 15% | [X] |
| **TOTAL** | | | **[X] / 10** |

### Feedback por sección

#### I — Identificación del problema

**Lo que haces bien:** [feedback positivo específico]
**Lo que necesitas mejorar:** [feedback específico y accionable]
**Ejemplo de mejora:** [NO reescribir — señalar la dirección. Ej: "Tu pregunta es demasiado amplia. Intenta dividirla en dos preguntas más concretas."]

#### R — Regulación

**Lo que haces bien:** [feedback]
**Lo que necesitas mejorar:** [feedback]

#### A — Aplicación

**Lo que haces bien:** [feedback]
**Lo que necesitas mejorar:** [feedback]

#### C — Conclusión

**Lo que haces bien:** [feedback]
**Lo que necesitas mejorar:** [feedback]

### Resumen

**Fortalezas principales:** [1-2 puntos fuertes]
**Áreas de mejora prioritarias:** [1-2 áreas donde enfocarse]
**Siguiente paso:** [qué hacer para mejorar]

---

**Qué hacer a continuación:**
1. **Reescribir** — corrige y vuelve a presentar para segunda evaluación.
2. **Profundizar en R** — `/estudiante-derecho:investigacion` si necesitas buscar más regulación.
3. **Método socrático** — `/estudiante-derecho:socratico` para trabajar los puntos débiles.
4. **Otro caso** — evalúo otro análisis IRAC.
5. **Otra cosa** — dime qué necesitas.
```

## Guardarraíles

- **Feedback específico, no genérico.** "Necesitas mejorar la argumentación" no sirve. "En el párrafo 3 afirmas que el plazo es de 15 días pero no explicas de dónde sale esa cifra — cita el artículo" sí sirve.
- **No reescribir.** Señalar qué cambiar y por qué. La reescritura la hace el estudiante.
- **Ser honesto pero constructivo.** Si el análisis es malo, decirlo — pero siempre con una vía de mejora.
- **No inflar la nota.** Un 4/10 es un 4/10. El estudiante necesita saber dónde está para mejorar.
- **Reconocer el esfuerzo y los aciertos.** Empezar siempre por lo que hace bien antes de señalar mejoras.
- **Adaptar al nivel.** Un estudiante de primer año no necesita jurisprudencia del TS. Uno de quinto, sí.
