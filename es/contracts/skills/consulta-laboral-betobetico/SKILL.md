---
name: consulta-laboral-betobetico
title: Propósito
description: Responde consultas rápidas de derecho laboral con referencia a artículos del ET y convenio colectivo
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/laboral/skills/consulta
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: contracts
language: es
---

## Propósito

Esta skill proporciona respuestas rápidas y estructuradas a consultas de derecho laboral español. Siempre referencia el artículo del ET aplicable y, cuando es relevante, señala si la respuesta depende del convenio colectivo específico.

## Instrucciones

### Paso 1 — Analizar la consulta

1. Identificar el tema: contratación, jornada, vacaciones, permisos, retribución, extinción, Seguridad Social, prevención de riesgos, derechos colectivos, teletrabajo, igualdad.
2. Determinar si la respuesta depende del convenio colectivo aplicable.
3. Verificar si hay normativa especial aplicable (RDL, Ley específica).

### Paso 2 — Buscar la base legal

Orden de fuentes:

1. **Constitución Española** (arts. 28, 35, 37, 40-41): derechos fundamentales laborales.
2. **Estatuto de los Trabajadores** (RDL 2/2015): norma principal.
3. **Leyes especiales**: Ley 10/2021 (teletrabajo), LO 3/2007 (igualdad), LPRL (31/1995), LRJS (36/2011).
4. **Convenio colectivo**: mejoras sobre mínimos legales.
5. **Jurisprudencia del TS y TC**: cuando la interpretación no sea pacífica.

### Paso 3 — Estructurar la respuesta

1. Respuesta directa a la pregunta.
2. Base legal con artículo concreto.
3. Matices o excepciones importantes.
4. Indicación de si el convenio puede mejorar la regulación legal.

### Paso 4 — Evaluar completitud

- Si la respuesta requiere conocer el convenio colectivo y no está en la configuración, indicarlo expresamente.
- Si la pregunta tiene múltiples respuestas posibles según la casuística, presentar todas las opciones.

## Formato de salida

```markdown
## Consulta laboral

**Pregunta:** [pregunta del usuario]

### Respuesta

[Respuesta directa, concisa y precisa]

### Base legal

| Norma | Artículo | Contenido relevante |
|-------|----------|---------------------|
| ET | Art. [X] | [extracto relevante] |
| [otra norma] | Art. [X] | [extracto relevante] |

### Matices y excepciones

- [Matiz 1]
- [Matiz 2]

### Dependencia del convenio colectivo

[Indicar si el convenio puede modificar/mejorar la regulación legal y en qué sentido]

### Referencias adicionales

- [Jurisprudencia relevante si la hay]
- [Criterio de la ITSS si aplica]
```

## Temas frecuentes — Referencia rápida

| Tema | Artículos ET | Normativa especial |
|------|-------------|-------------------|
| Período de prueba | Art. 14 | Convenio colectivo |
| Jornada | Arts. 34-38 | RD 1561/1995 (jornadas especiales) |
| Vacaciones | Art. 38 | Mín. 30 días naturales |
| Permisos retribuidos | Art. 37.3 | Convenio colectivo |
| Excedencias | Art. 46 | Voluntaria, forzosa, cuidado |
| Movilidad geográfica | Art. 40 | Individual y colectiva |
| Modificación sustancial | Art. 41 | Jornada, horario, turnos, salario |
| Teletrabajo | — | Ley 10/2021 (>30% jornada) |
| Igualdad | — | LO 3/2007, RD 901/2020 (plan igualdad) |
| Registro de jornada | Art. 34.9 | Obligatorio desde RDL 8/2019 |

## Referencias normativas

- **ET** (RDL 2/2015): Estatuto de los Trabajadores.
- **LGSS** (RDL 8/2015): Ley General de la Seguridad Social.
- **LPRL** (Ley 31/1995): Prevención de riesgos laborales.
- **LRJS** (Ley 36/2011): Reguladora de la jurisdicción social.
- **Ley 10/2021**: Trabajo a distancia.
- **LO 3/2007**: Igualdad efectiva de mujeres y hombres.
- **LOPDGDD** (LO 3/2018) art. 88: Desconexión digital.

## Guardrails

- **NO** proporciona asesoramiento jurídico vinculante — es orientación general.
- **NO** interpreta convenios colectivos específicos salvo que estén cargados en configuración.
- **NO** sustituye la consulta a un abogado laboralista en casos complejos.
- **AVISAR** siempre que la respuesta dependa del convenio colectivo y este no esté disponible.
- **AVISAR** si la pregunta implica un supuesto de hecho que requiere análisis individualizado.
- **ESCALAR** si la consulta involucra derechos fundamentales (discriminación, libertad sindical, intimidad).
