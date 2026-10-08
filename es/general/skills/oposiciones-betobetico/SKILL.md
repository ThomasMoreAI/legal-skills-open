---
name: oposiciones-betobetico
title: /oposiciones
description: 'Preparación de oposiciones jurídicas por especialidad: judicatura, fiscalía, notarías, registros, abogacía del estado, LAJ, TAC. Ofrece práctica de temas orales, test y casos prácticos según la especialidad. Usa los temarios oficiales del BOE. NUNCA da contenido genérico — siempre vinculado a un tema concreto del temario. Usar cuando el usuario dice "oposiciones", "preparo judicatura", "tema de oposición", "práctica de test", "caso práctico de notarías", o está preparando una oposición jurídica.'
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/estudiante-derecho/skills/oposiciones
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: general
language: es
---

# /oposiciones

1. Leer `~/.claude/plugins/config/claude-para-abogados/estudiante-derecho/CLAUDE.md` — perfil del estudiante.
2. Identificar la especialidad y el tipo de ejercicio.
3. Identificar el tema concreto del temario.
4. Generar el ejercicio de práctica.

---

## Propósito

Proporcionar práctica estructurada para oposiciones jurídicas, adaptada a la especialidad y al formato real del examen. Cada ejercicio está vinculado a un tema concreto del temario oficial — nada genérico.

## REGLA CARDINAL

> **Todo contenido vinculado a un tema concreto del temario.** Si el opositor dice "practiquemos civil", la respuesta es "qué tema del programa? Dame el número." No hay práctica genérica — las oposiciones son temario, y el temario tiene estructura.

## Especialidades y formatos de examen

| Especialidad | Temas orales | Test | Caso práctico | Temario BOE |
|---|---|---|---|---|
| Judicatura | Sí (cantar temas) | Sí (100 preguntas) | Sí | Acuerdo CGPJ |
| Fiscalía | Sí (cantar temas) | Sí | Sí | Acuerdo CGPJ |
| Notarías | Sí (cantar temas) | No | Sí (dictamen) | RD temario |
| Registros | Sí (cantar temas) | No | Sí (dictamen) | RD temario |
| Abogacía del Estado | Sí | Sí | Sí (dictamen) | BOE |
| LAJ (Letrado de la Adm. de Justicia) | Sí | Sí | Sí | BOE |
| TAC (Tramitación, Auxilio, Gestión) | No | Sí | Sí (supuesto práctico) | BOE |

## Tipos de ejercicio

### 1. Práctica de tema oral (cantar)

- El opositor elige un tema del programa.
- Se le presenta el enunciado del tema.
- Estructura sugerida para exponerlo (según la especialidad).
- Tras la exposición del opositor: feedback sobre estructura, contenido, omisiones.

**Para judicatura/fiscalía/notarías/registros:**

| Fase | Qué evalúa |
|---|---|
| Apertura | Ubicación del tema, relevancia, conexiones |
| Desarrollo | Completitud, orden lógico, precisión normativa |
| Jurisprudencia | Referencias jurisprudenciales relevantes (solo si la especialidad lo valora) |
| Cierre | Síntesis, cuestiones abiertas, tendencias |
| Tiempo | Ajuste al tiempo disponible (15-20 min según especialidad) |

### 2. Test

- Generar preguntas tipo test vinculadas a un tema o grupo de temas.
- Formato: 4 opciones, 1 correcta.
- Nivel de dificultad ajustable.
- Tras responder: explicación de cada opción (correcta e incorrectas).

**Principios del buen test:**

- Las opciones incorrectas deben ser plausibles, no absurdas.
- No preguntar "cuál es falsa" con 3 verdaderas y 1 obviamente falsa.
- Incluir preguntas de aplicación, no solo memorísticas.
- Variar entre "cuál es correcta" y "cuál es incorrecta".

### 3. Caso práctico / Dictamen

- Supuesto de hechos con cuestiones jurídicas.
- Adaptado a la especialidad:
  - **Judicatura:** caso para resolver como juez (sentencia).
  - **Fiscalía:** caso para resolver como fiscal (calificación, acusación).
  - **Notarías:** operación notarial a calificar (dictamen).
  - **Registros:** documento presentado a calificación registral.
  - **TAC:** supuesto procedimental.

## Formato de salida (ejemplo: test)

```markdown
## Test — [Especialidad]: Tema [N] — [Título del tema]

**Dificultad:** [básica / intermedia / avanzada]
**N.o de preguntas:** [N]

---

**1.** [Enunciado de la pregunta]

a) [Opción A]
b) [Opción B]
c) [Opción C]
d) [Opción D]

[Repetir para cada pregunta]

---

## Soluciones

**1.** Correcta: [letra]
- **[Opción correcta]:** [explicación de por qué es correcta]
- **[Opción incorrecta]:** [explicación de por qué es incorrecta]
[Repetir]

### Resumen de resultados

| Correctas | Incorrectas | En blanco | Nota |
|---|---|---|---|
| [N] | [N] | [N] | [puntuación según baremo de la oposición] |

---

**Qué hacer a continuación:**
1. **Repasar errores** — profundizo en las preguntas falladas.
2. **Más test** — genero otro test del mismo tema o de otro.
3. **Tema oral** — practico el tema oralmente.
4. **Caso práctico** — supuesto práctico sobre este tema.
5. **Otra cosa** — dime qué necesitas.
```

## Guardarraíles

- **Nunca contenido genérico.** Siempre vinculado a un tema concreto del temario.
- **No inventar artículos.** Si no estás seguro del número de artículo, decirlo — "busca el artículo del CC que regula esto" es mejor que inventar "art. 1547 CC" (que puede no existir).
- **Los test deben ser realistas.** Las opciones incorrectas deben ser errores que un opositor real cometería, no absurdos evidentes.
- **El caso práctico debe tener nivel de examen real.** Ni demasiado fácil ni imposible — ajustar a la dificultad de la oposición concreta.
- **Respetar el formato de cada especialidad.** Un dictamen de notarías no tiene la misma estructura que un supuesto de TAC.
- **Los temarios cambian.** Advertir al opositor que verifique que el tema corresponde al programa vigente. Marcar `[verificar vigencia del temario]`.
- **No sustituir al preparador.** Este skill es un complemento de práctica, no un sustituto del preparador de oposiciones.
