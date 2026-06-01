---
name: memo-betobetico
title: /memo
description: Genera un memo de caso con estructura IRAC (Identificación del problema, Regulación aplicable, Aplicación al caso, Conclusión) para revisión del supervisor. Señala lagunas de investigación y cuestiones pendientes. Usar cuando el usuario dice "memo de caso", "análisis del caso", "IRAC", "prepara el memo para el supervisor", o necesita estructurar el análisis jurídico de un asunto de la clínica.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/clinica-juridica/skills/memo
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: general
language: es
---

# /memo

1. Leer `~/.claude/plugins/config/claude-para-abogados/clinica-juridica/CLAUDE.md` — perfil de la clínica.
2. Cargar la ficha de intake si existe.
3. Estructurar el análisis en formato IRAC.
4. Señalar lagunas de investigación.
5. Producir el memo para revisión del supervisor.

---

## Propósito

Producir un memo de caso estructurado en formato IRAC que el alumno pueda presentar al supervisor para revisión. El memo identifica las cuestiones jurídicas, la regulación aplicable, la aplicación a los hechos del caso y las conclusiones preliminares. Señala explícitamente lo que falta por investigar.

## Estructura IRAC

### I — Identificación del problema (Issue)

- Formular las cuestiones jurídicas como preguntas concretas.
- Ejemplo: "Tiene el arrendatario derecho a la prórroga del contrato de arrendamiento conforme al art. 9 LAU?"
- Separar cuestiones principales de cuestiones secundarias.
- Si hay varias cuestiones, ordenar por relevancia o cronología procesal.

### R — Regulación aplicable (Rule)

- Para cada cuestión, identificar:
  - **Legislación aplicable:** artículos concretos (no "la LAU dice que...").
  - **Jurisprudencia relevante:** sentencias del TS o AP que establezcan criterio.
  - **Doctrina:** si aporta (indicar autor y obra).
- **Marcar lo que es seguro y lo que es dudoso.** Si la regulación no es clara o hay jurisprudencia contradictoria, decirlo.
- **Señalar lagunas:** "No he encontrado jurisprudencia sobre este punto concreto" es una conclusión valiosa.

### A — Aplicación al caso (Application)

- Aplicar la regulación a los hechos concretos del caso.
- Argumentar en ambas direcciones — qué favorece al cliente y qué le perjudica.
- Identificar los hechos que son determinantes y los que son irrelevantes.
- Si faltan hechos para concluir, listarlos como "hechos pendientes de confirmar".

### C — Conclusión (Conclusion)

- Respuesta a cada cuestión planteada en la I.
- Nivel de confianza: alta / media / baja — con explicación.
- Recomendación preliminar de actuación.
- Cuestiones abiertas que requieren más investigación o decisión del supervisor.

## Formato de salida

```markdown
BORRADOR — MEMO DE CASO — PARA REVISIÓN DEL SUPERVISOR

> **Nota para el supervisor**
> - **Alumno/a:** [nombre]
> - **Fecha:** [fecha]
> - **Caso:** [referencia]
> - **Lagunas de investigación:** [N cuestiones pendientes]
> - **Antes de actuar:** este memo es un borrador del alumno/a para su revisión. No se ha contrastado con el cliente ni se ha actuado en base a él.

## Memo de caso: [Referencia del caso]

**Cliente:** [nombre]
**Asunto:** [descripción breve]
**Área(s) del derecho:** [áreas]

---

### ISSUE — Cuestiones jurídicas

1. **[Cuestión principal]** — [formulación como pregunta]
2. **[Cuestión secundaria]** — [formulación como pregunta]

---

### RULE — Regulación aplicable

#### Cuestión 1: [título]

**Legislación:**
- [Artículo] — [contenido relevante]

**Jurisprudencia:**
- [Sentencia] — [criterio establecido] [verificar cita]

**Lagunas:**
- [Qué no se ha encontrado]

#### Cuestión 2: [título]

[Misma estructura]

---

### APPLICATION — Aplicación al caso

#### Cuestión 1: [título]

**A favor del cliente:**
- [Argumento 1]

**En contra del cliente:**
- [Argumento 1]

**Hechos determinantes:** [lista]
**Hechos pendientes de confirmar:** [lista]

#### Cuestión 2: [título]

[Misma estructura]

---

### CONCLUSION — Conclusiones

| Cuestión | Conclusión preliminar | Confianza | Acción recomendada |
|---|---|---|---|
| [cuestión 1] | [conclusión] | [alta/media/baja] | [acción] |
| [cuestión 2] | [conclusión] | [alta/media/baja] | [acción] |

### Cuestiones abiertas

1. [Cuestión que requiere más investigación]
2. [Cuestión que requiere decisión del supervisor]

---

**Qué hacer a continuación:**
1. **Investigar lagunas** — `/clinica-juridica:investigacion` para las cuestiones pendientes.
2. **Registrar plazos** — `/clinica-juridica:plazos` si hay plazos procesales.
3. **Carta al cliente** — `/clinica-juridica:carta` para informar del estado.
4. **Reunión con supervisor** — llevar este memo a la tutoría.
5. **Otra cosa** — dime qué necesitas.
```

## Guardarraíles

- **El memo es del alumno, no de la IA.** La IA estructura y ayuda, pero el análisis jurídico es del alumno. No producir un memo "llave en mano" que el alumno no haya pensado.
- **Señalar lagunas honestamente.** "No sé" o "no he encontrado" son respuestas válidas y necesarias en un memo de clínica.
- **Argumentar en ambas direcciones.** Un memo que solo argumenta a favor del cliente no es un buen memo — el supervisor necesita ver los riesgos.
- **Las citas jurisprudenciales deben verificarse.** Marcar `[verificar cita]` en toda referencia a sentencia. Las citas fabricadas en un memo de clínica son un problema grave.
- **Este memo NO se envía al cliente.** Es un documento interno de trabajo para revisión del supervisor.
- **El supervisor tiene la última palabra.** Las conclusiones del memo son preliminares y están sujetas a la revisión y corrección del supervisor.
