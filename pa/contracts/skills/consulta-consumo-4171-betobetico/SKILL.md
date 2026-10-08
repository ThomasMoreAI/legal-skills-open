---
name: consulta-consumo-4171-betobetico
title: /consulta
description: 'Consulta rápida de consumo — evaluación rápida de riesgo para preguntas tipo "¿podemos hacer esto?" en materia de consumo. Siempre referencia la Ley 45 de 2007 (ACODECO). Salida en semáforo: VERDE/AMARILLO/ROJO. Usar cuando el usuario pregunte "¿se puede...?", "¿es legal...?", "consulta rápida de consumo" o cualquier duda puntual sobre derecho del consumo.'
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/consumo/skills/consulta
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: contracts
language: es
---

# /consulta

1. Cargar `~/.claude/plugins/config/claude-para-abogados/consumo/CLAUDE.md` → sector, tolerancia al riesgo.
2. Recibir la pregunta.
3. Analizar contra la normativa aplicable.
4. Emitir respuesta con semáforo y referencias.

```
/consumo:consulta
¿Podemos poner un precio de suscripción que solo se ve después de registrarse?
```

---

## Propósito

No toda consulta de consumo necesita una revisión completa. Muchas preguntas son "¿podemos hacer X?" y necesitan una respuesta rápida, fundamentada y con nivel de riesgo claro. Este skill es el filtro rápido: semáforo + fundamento + siguiente paso si hace falta profundizar.

---

## Sistema de semáforo

| Color | Significado | Acción |
|---|---|---|
| **VERDE** | Lícito; cumple la normativa aplicable | Proceder |
| **AMARILLO** | Lícito con matices; depende de la ejecución o hay riesgo bajo | Proceder con precauciones indicadas |
| **ROJO** | Ilícito o riesgo alto de sanción/nulidad | No proceder sin correcciones |

---

## Estructura de la respuesta

Toda respuesta incluye obligatoriamente:

1. **Semáforo** — VERDE / AMARILLO / ROJO
2. **Respuesta directa** — 2-3 frases con la conclusión
3. **Fundamento legal** — siempre citar:
   - Disposición concreta de la Ley 45 de 2007
   - Reglamentación de la ACODECO si aplica [verificar]
   - Código de Comercio de Panamá si refuerza el argumento
   - Resolución de la ACODECO o jurisprudencia de la CSJ relevante si existe [verificar]
4. **Matices** — condiciones, excepciones, dependencias
5. **Siguiente paso** — si necesita análisis más profundo, indicar qué skill usar

---

## Áreas cubiertas

| Área | Normativa principal | Skills relacionados |
|---|---|---|
| Información al consumidor | Ley 45 de 2007 | `/consumo:lanzamiento` |
| Derecho de retracto | Ley 45 de 2007 | `/consumo:lanzamiento` |
| Garantías | Ley 45 de 2007 | `/consumo:lanzamiento` |
| Publicidad y claims | Ley 45 de 2007 | `/consumo:claims` |
| Cláusulas abusivas | Ley 45 de 2007 | `/consumo:condiciones-generales` |
| Prácticas comerciales | Ley 45 de 2007 | `/consumo:claims` |
| Contratación electrónica | Ley 45 de 2007 | `/consumo:lanzamiento` |
| Precios y ofertas | Ley 45 de 2007 | `/consumo:claims` |

---

## Formato de salida

```markdown
# Consulta rápida de consumo

**Pregunta:** [la pregunta del usuario]
**Fecha:** [fecha]

---

## [VERDE / AMARILLO / ROJO]

[2-3 frases con la respuesta directa]

---

## Fundamento legal

- **Ley 45 de 2007:** [disposición — contenido relevante] [verificar]
- **Reglamentación ACODECO:** [referencia — si aplica] [verificar]
- **Código de Comercio de Panamá:** [referencia — si refuerza]
- **Resolución ACODECO / jurisprudencia CSJ:** [si existe resolución relevante] [verificar]

---

## Matices

[Condiciones, excepciones, dependencias que afectan a la respuesta]

---

## Siguiente paso

[Si necesita más análisis: indicar qué skill usar.
Si no: "No requiere análisis adicional."]
```

---

## Ejemplos de consultas tipo

| Pregunta | Semáforo | Clave |
|---|---|---|
| "¿Podemos cobrar por las devoluciones?" | AMARILLO | Sí, los gastos de devolución si se informa previamente (Ley 45 de 2007) |
| "¿Podemos eliminar el derecho de retracto?" | ROJO | No, es irrenunciable para el consumidor (Ley 45 de 2007) |
| "¿Podemos imponer un foro distinto al del consumidor?" | ROJO | Riesgo de nulidad en contratos de adhesión con consumidores (Ley 45 de 2007) |
| "¿Podemos ofrecer descuento del 50%?" | AMARILLO | Sí, si el precio anterior anunciado es real y estuvo vigente (Ley 45 de 2007) |

---

## Legislación de referencia

- Ley 45 de 2007 — normas de protección al consumidor y defensa de la competencia (norma central)
- ACODECO — Autoridad de Protección al Consumidor y Defensa de la Competencia
- Código de Comercio de Panamá — obligaciones de los comerciantes
- Ley 81 de 2019 — protección de datos personales (cuando la consulta toca tratamiento de datos)
- Resoluciones de la ACODECO y jurisprudencia de la CSJ [verificar]

---

## Lo que este skill NO hace

- No sustituye un análisis profundo — si la respuesta es AMARILLO o ROJO con matices, recomendar el skill específico.
- No emite dictámenes — es una orientación rápida marcada con `[revisión]` donde haya duda.
- No cubre normativa sectorial regulada (financiera —Superintendencia de Bancos—, sanitaria, energética) — indicar que se necesita especialista.
