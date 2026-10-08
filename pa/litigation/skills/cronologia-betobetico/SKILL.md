---
name: cronologia-betobetico
title: Propósito
description: Construye una línea temporal de hechos relevantes a partir de fuentes declaradas con relevancia procesal
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/procesal/skills/cronologia
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: litigation
language: es
---

## Propósito

Esta skill construye una cronología de hechos jurídicamente relevantes a partir de las fuentes documentales proporcionadas. Cada entrada incluye fecha, hecho, fuente documental y relevancia procesal. Diseñada para preparar la base fáctica de demandas, contestaciones e informes.

## Instrucciones

### Paso 1 — Recopilar fuentes

1. Leer todos los documentos proporcionados por el usuario.
2. Clasificar cada fuente:
   - Contratos y adendas.
   - Correspondencia (emails, burofax, cartas).
   - Documentos públicos (escrituras, certificaciones registrales).
   - Informes periciales.
   - Resoluciones judiciales o administrativas.
   - Documentación interna (actas, informes, notas).
3. Registrar la procedencia y fiabilidad de cada fuente.

### Paso 2 — Extraer hechos

Para cada documento:

1. Identificar hechos con fecha concreta o determinable.
2. Extraer la cita literal o el dato preciso.
3. Asignar relevancia procesal:
   - **Constitutivo**: hecho que funda la pretensión o excepción.
   - **Impeditivo**: hecho que impide el nacimiento del derecho.
   - **Extintivo**: hecho que extingue la obligación.
   - **Excluyente**: hecho que excluye la pretensión (prescripción, caducidad).
   - **Contextual**: aporta contexto sin ser determinante.

### Paso 3 — Ordenar cronológicamente

1. Ordenar todos los hechos por fecha (de más antiguo a más reciente).
2. Agrupar hechos simultáneos o del mismo día.
3. Identificar lagunas temporales significativas.
4. Señalar contradicciones entre fuentes.

### Paso 4 — Detectar hitos procesales

- Fechas que inician cómputo de plazos (prescripción, caducidad).
- Requerimientos fehacientes que interrumpen prescripción.
- Hechos que determinan la competencia territorial.
- Fechas de conocimiento que afectan al dies a quo.

## Formato de salida

```markdown
## Cronología de hechos

**Asunto:** [nombre del asunto]
**Fecha de elaboración:** [fecha]
**Fuentes analizadas:** [número]
**Período cubierto:** [fecha inicio] — [fecha fin]

### Línea temporal

| # | Fecha | Hecho | Fuente | Relevancia procesal | Notas |
|---|-------|-------|--------|---------------------|-------|
| 1 | [fecha] | [descripción del hecho] | [documento, página] | [tipo] | [observación] |

### Hitos procesales clave

| Hito | Fecha | Efecto jurídico | Base legal |
|------|-------|-----------------|------------|
| [hito] | [fecha] | [efecto] | [artículo] |

### Lagunas temporales

| Período | Duración | Documentación esperada | Impacto |
|---------|----------|------------------------|---------|
| [desde-hasta] | [días/meses] | [qué falta] | [valoración] |

### Contradicciones entre fuentes

| Hecho | Fuente A | Fuente B | Discrepancia |
|-------|----------|----------|--------------|
| [hecho] | [versión A] | [versión B] | [detalle] |
```

## Referencias normativas

- **Código Judicial de Panamá**: necesidad y carga de la prueba — los hechos deben probarse [verificar].
- **Código Civil de Panamá**: prescripción de acciones [verificar].
- **Código Judicial de Panamá**: caducidad e improrrogabilidad de los términos procesales [verificar].
- **Código Civil de Panamá**: interrupción de la prescripción (reclamación extrajudicial) [verificar].

## Guardrails

- **NO** valora la prueba ni su admisibilidad — solo documenta hechos.
- **NO** inventa ni presume hechos no documentados.
- **NO** determina si la prescripción ha operado — señala fechas relevantes.
- **NO** sustituye la valoración jurídica del abogado sobre la relevancia de cada hecho.
- **ESCALAR** si se detectan contradicciones graves entre fuentes que afecten a hechos constitutivos.
- **ESCALAR** si las fechas sugieren que la acción puede estar prescrita o caducada.
- **AVISAR** si hay hechos sin fecha precisa que puedan ser relevantes.
- **AVISAR** si faltan fuentes documentales para cubrir períodos significativos.
