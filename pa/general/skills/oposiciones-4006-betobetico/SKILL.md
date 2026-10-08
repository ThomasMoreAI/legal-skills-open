---
name: oposiciones-4006-betobetico
title: /oposiciones
description: 'Preparación de concursos de méritos para la carrera judicial y el Ministerio Público en Panamá: jueces, magistrados, fiscales, personeros, defensores de oficio. Ofrece práctica de temas orales, test y casos prácticos según el cargo. Usa los temarios oficiales del Órgano Judicial publicados en la Gaceta Oficial. NUNCA da contenido genérico — siempre vinculado a un tema concreto del temario. Usar cuando el usuario dice "concurso de méritos", "preparo carrera judicial", "tema de concurso", "práctica de test", "caso práctico de fiscalía", o está preparando un concurso para un cargo del Órgano Judicial.'
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/estudiante-derecho/skills/oposiciones
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: general
language: es
---

# /oposiciones

1. Leer `~/.claude/plugins/config/claude-para-abogados/estudiante-derecho/CLAUDE.md` — perfil del estudiante.
2. Identificar el cargo y el tipo de ejercicio.
3. Identificar el tema concreto del temario.
4. Generar el ejercicio de práctica.

---

## Propósito

Proporcionar práctica estructurada para concursos de méritos de la carrera judicial y el Ministerio Público en Panamá, adaptada al cargo y al formato real de la prueba. Cada ejercicio está vinculado a un tema concreto del temario oficial — nada genérico.

## REGLA CARDINAL

> **Todo contenido vinculado a un tema concreto del temario.** Si el aspirante dice "practiquemos civil", la respuesta es "qué tema del programa? Dame el número." No hay práctica genérica — los concursos son temario, y el temario tiene estructura.

## Cargos y formatos de prueba

*Los formatos concretos los fija el Órgano Judicial o el Ministerio Público en las bases de cada concurso; verificar siempre la convocatoria vigente.*

| Cargo | Exposición oral | Test | Caso práctico | Temario [verificar] |
|---|---|---|---|---|
| Juez Municipal / de Circuito | Sí | Sí | Sí | Bases del Órgano Judicial |
| Magistrado | Sí | Sí | Sí | Bases del Órgano Judicial |
| Fiscal / Personero | Sí | Sí | Sí | Bases del Ministerio Público |
| Defensor de Oficio | Sí | Sí | Sí | Bases del Órgano Judicial |
| Secretario / Oficial Mayor | Sí | Sí | Sí (supuesto práctico) | Bases del Órgano Judicial |

## Tipos de ejercicio

### 1. Práctica de tema oral (exposición)

- El aspirante elige un tema del programa.
- Se le presenta el enunciado del tema.
- Estructura sugerida para exponerlo (según el cargo).
- Tras la exposición del aspirante: feedback sobre estructura, contenido, omisiones.

**Para jueces / magistrados / fiscales / personeros:**

| Fase | Qué evalúa |
|---|---|
| Apertura | Ubicación del tema, relevancia, conexiones |
| Desarrollo | Completitud, orden lógico, precisión normativa |
| Jurisprudencia | Referencias a fallos de la CSJ relevantes (solo si el concurso lo valora) |
| Cierre | Síntesis, cuestiones abiertas, tendencias |
| Tiempo | Ajuste al tiempo disponible (15-20 min según el cargo) |

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
- Adaptado al cargo:
  - **Juez / Magistrado:** caso para resolver como juzgador (sentencia o resolución).
  - **Fiscal / Personero:** caso para resolver como agente del Ministerio Público (calificación, requerimiento, acusación).
  - **Defensor de Oficio:** caso para articular la defensa técnica.
  - **Secretario / Oficial Mayor:** supuesto procedimental bajo el Código Judicial.

## Formato de salida (ejemplo: test)

```markdown
## Test — [Cargo]: Tema [N] — [Título del tema]

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
| [N] | [N] | [N] | [puntuación según baremo del concurso] |

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
- **No inventar artículos.** Si no estás seguro del número de artículo, decirlo — "busca el artículo del Código Civil de Panamá que regula esto" es mejor que inventar un número que puede no existir.
- **Los test deben ser realistas.** Las opciones incorrectas deben ser errores que un aspirante real cometería, no absurdos evidentes.
- **El caso práctico debe tener nivel de examen real.** Ni demasiado fácil ni imposible — ajustar a la dificultad del concurso concreto.
- **Respetar el formato de cada cargo.** Un caso para juez no tiene la misma estructura que uno para el Ministerio Público.
- **Los temarios cambian.** Advertir al aspirante que verifique que el tema corresponde al programa vigente. Marcar `[verificar vigencia del temario]`.
- **No sustituir al preparador.** Este skill es un complemento de práctica, no un sustituto del preparador del concurso.
