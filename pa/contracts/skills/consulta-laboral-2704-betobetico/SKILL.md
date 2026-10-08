---
name: consulta-laboral-2704-betobetico
title: Propósito
description: Responde consultas rápidas de derecho laboral con referencia a artículos del Código de Trabajo y convención colectiva
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/laboral/skills/consulta
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: contracts
language: es
---

## Propósito

Esta skill proporciona respuestas rápidas y estructuradas a consultas de derecho laboral panameño. Siempre referencia el artículo del Código de Trabajo aplicable y, cuando es relevante, señala si la respuesta depende de la convención colectiva específica.

## Instrucciones

### Paso 1 — Analizar la consulta

1. Identificar el tema: contratación, jornada, vacaciones, licencias y permisos, salario, décimo tercer mes, prima de antigüedad, terminación, Caja de Seguro Social, riesgos profesionales, derechos colectivos, teletrabajo, no discriminación.
2. Determinar si la respuesta depende de la convención colectiva aplicable.
3. Verificar si hay normativa especial aplicable (ley o decreto específico).

### Paso 2 — Buscar la base legal

Orden de fuentes:

1. **Constitución Política de Panamá** — derechos laborales fundamentales [verificar].
2. **Código de Trabajo de Panamá** — norma principal (Decreto de Gabinete 252 de 1971).
3. **Leyes y decretos especiales**: décimo tercer mes (Decreto de Gabinete 221 de 1971), Ley 126 de 2020 (teletrabajo, modifica el art. 151 del Código de Trabajo), Ley 51 de 2005 (CSS) y régimen de riesgos profesionales administrado por la CSS (Ley 51 de 2005).
4. **Convención colectiva**: mejoras sobre los mínimos legales.
5. **Jurisprudencia de la Corte Suprema de Justicia**: cuando la interpretación no sea pacífica [verificar].

### Paso 3 — Estructurar la respuesta

1. Respuesta directa a la pregunta.
2. Base legal con artículo concreto.
3. Matices o excepciones importantes.
4. Indicación de si la convención colectiva puede mejorar la regulación legal.

### Paso 4 — Evaluar completitud

- Si la respuesta requiere conocer la convención colectiva y no está en la configuración, indicarlo expresamente.
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
| Código de Trabajo | Art. [X] [verificar] | [extracto relevante] |
| [otra norma] | Art. [X] [verificar] | [extracto relevante] |

### Matices y excepciones

- [Matiz 1]
- [Matiz 2]

### Dependencia de la convención colectiva

[Indicar si la convención puede modificar/mejorar la regulación legal y en qué sentido]

### Referencias adicionales

- [Jurisprudencia relevante de la Corte Suprema de Justicia si la hay]
- [Criterio de MITRADEL si aplica]
```

## Temas frecuentes — Referencia rápida

| Tema | Código de Trabajo | Normativa especial |
|------|-------------------|-------------------|
| Período de prueba | Art. 78 | Máx. 3 meses, por escrito; convención colectiva |
| Jornada y sobretiempo | Arts. 30-31 | Diurna 8h/48h; nocturna 7h/42h; mixta 7,5h/45h |
| Vacaciones | Art. 54 | 30 días por cada 11 meses de trabajo continuo |
| Décimo tercer mes | — | Decreto de Gabinete 221 de 1971 (15 abr, 15 ago, 15 dic) |
| Prima de antigüedad | Art. 224 | Una semana de salario por año de servicio |
| Indemnización despido injustificado | Art. 225 | 3,4 semanas/año (primeros 10 años) + 1 semana/año desde el año 11 |
| Licencias y permisos | Art. [X] [verificar] | Convención colectiva |
| Maternidad / fuero | Arts. 106-107 | Licencia de 14 semanas (6 antes + 8 después del parto) |
| Riesgos profesionales | — | Administrados por la CSS (Ley 51 de 2005) |
| Teletrabajo | — | Ley 126 de 2020 |
| Seguridad Social | — | Ley 51 de 2005 |

## Referencias normativas

- **Código de Trabajo de Panamá**: norma principal del derecho laboral (Decreto de Gabinete 252 de 1971).
- **Ley 51 de 2005**: seguridad social (CSS).
- **Régimen de riesgos profesionales** administrado por la CSS (Ley 51 de 2005).
- **Décimo tercer mes** — Decreto de Gabinete 221 de 1971 (tres partidas: 15 de abril, 15 de agosto y 15 de diciembre).
- **Ley 126 de 2020**: teletrabajo (modifica el art. 151 del Código de Trabajo).
- **MITRADEL**: resoluciones, salario mínimo y trámites administrativos laborales.

## Guardrails

- **NO** proporciona asesoramiento jurídico vinculante — es orientación general.
- **NO** interpreta convenciones colectivas específicas salvo que estén cargadas en configuración.
- **NO** sustituye la consulta a un abogado laboralista idóneo en casos complejos.
- **AVISAR** siempre que la respuesta dependa de la convención colectiva y esta no esté disponible.
- **AVISAR** si la pregunta implica un supuesto de hecho que requiere análisis individualizado.
- **ESCALAR** si la consulta involucra derechos fundamentales (discriminación, libertad sindical, intimidad).
