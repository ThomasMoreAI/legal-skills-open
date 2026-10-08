---
name: consulta-consumo-betobetico
title: /consulta
description: 'Consulta rápida de consumo — evaluación rápida de riesgo para preguntas tipo "¿podemos hacer esto?" en materia de consumo. Siempre referencia LGDCU + LCD + directiva aplicable. Salida en semáforo: VERDE/AMARILLO/ROJO. Usar cuando el usuario pregunte "¿se puede...?", "¿es legal...?", "consulta rápida de consumo" o cualquier duda puntual sobre derecho del consumo.'
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/consumo/skills/consulta
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
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
   - Artículo concreto de la LGDCU (RDL 1/2007)
   - Artículo de la LCD (Ley 3/1991) si aplica
   - Directiva UE aplicable si refuerza el argumento
   - Jurisprudencia relevante si existe
4. **Matices** — condiciones, excepciones, dependencias
5. **Siguiente paso** — si necesita análisis más profundo, indicar qué skill usar

---

## Áreas cubiertas

| Área | Normativa principal | Skills relacionados |
|---|---|---|
| Información precontractual | LGDCU arts. 60-63 | `/consumo:lanzamiento` |
| Derecho de desistimiento | LGDCU arts. 102-108 | `/consumo:lanzamiento` |
| Garantías | LGDCU arts. 114-126 | `/consumo:lanzamiento` |
| Publicidad y claims | LCD arts. 4-8, 10 | `/consumo:claims` |
| Cláusulas abusivas | LGDCU arts. 82-91 | `/consumo:condiciones-generales` |
| Prácticas comerciales desleales | LCD arts. 4-8, 19-31 | `/consumo:claims` |
| Contratación electrónica | LSSI-CE arts. 23-29 | `/consumo:lanzamiento` |
| Precios y ofertas | LGDCU art. 60; Dir. Ómnibus | `/consumo:claims` |

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

- **LGDCU:** [art. X — contenido relevante]
- **LCD:** [art. X — si aplica]
- **Directiva UE:** [referencia — si refuerza]
- **Jurisprudencia:** [si existe resolución relevante]

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
| "¿Podemos cobrar por las devoluciones?" | AMARILLO | Sí, los gastos de devolución si se informa previamente (art. 107.1 LGDCU) |
| "¿Podemos eliminar el desistimiento?" | ROJO | No, es irrenunciable para el consumidor (art. 10 LGDCU) |
| "¿Podemos poner fuero en Madrid?" | ROJO | Nulo en contratos con consumidores (art. 90.2 LGDCU) |
| "¿Podemos ofrecer descuento del 50%?" | AMARILLO | Sí, si el precio anterior es el más bajo en 30 días (Dir. Ómnibus) |

---

## Legislación de referencia

- LGDCU (RDL 1/2007) — Ley General para la Defensa de los Consumidores y Usuarios
- LCD (Ley 3/1991) — Ley de Competencia Desleal
- LCGC (Ley 7/1998) — Ley sobre Condiciones Generales de la Contratación
- LSSI-CE (Ley 34/2002) — Ley de Servicios de la Sociedad de la Información
- Directiva 2011/83/UE — derechos de los consumidores
- Directiva 93/13/CEE — cláusulas abusivas
- Directiva (UE) 2019/2161 — Ómnibus
- Directiva (UE) 2024/825 — greenwashing

---

## Lo que este skill NO hace

- No sustituye un análisis profundo — si la respuesta es AMARILLO o ROJO con matices, recomendar el skill específico.
- No emite dictámenes — es una orientación rápida marcada con `[revisión]` donde haya duda.
- No cubre normativa sectorial regulada (financiera, sanitaria, energética) — indicar que se necesita especialista.
