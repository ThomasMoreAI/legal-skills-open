---
name: busqueda-marca-betobetico
title: Propósito
description: Realiza un screening preliminar de disponibilidad de marca con análisis de riesgo de confusión
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/propiedad-intelectual/skills/busqueda-marca
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: ip
language: es
---

## Propósito

Esta skill realiza un análisis preliminar (knockout check) de disponibilidad de una denominación como marca. Evalúa el riesgo de confusión con marcas anteriores en los registros OEPM, EUIPO y OMPI, aplicando criterios de similitud visual, fonética y conceptual.

## Instrucciones

### Paso 1 — Recopilar datos de la marca candidata

1. **Denominación**: nombre exacto de la marca propuesta.
2. **Tipo de marca**: denominativa, figurativa, mixta, tridimensional, sonora.
3. **Clases de Niza**: productos/servicios que se pretende proteger.
4. **Territorio**: España (OEPM), UE (EUIPO), internacional (OMPI/Madrid).

### Paso 2 — Definir estrategia de búsqueda

Criterios de búsqueda por similitud:

1. **Visual**: comparación gráfica de los signos.
2. **Fonética**: pronunciación similar, sustitución de letras con sonido equivalente.
3. **Conceptual**: significado o asociación semántica equivalente.

Variaciones a considerar:
- Singular/plural.
- Con y sin artículos o preposiciones.
- Traducciones a otros idiomas oficiales de la UE.
- Abreviaturas y acrónimos.
- Errores ortográficos comunes.

### Paso 3 — Analizar resultados

Para cada marca anterior encontrada:

1. Titular y estado (vigente, en trámite, caducada).
2. Clase(s) de Niza y descripción de productos/servicios.
3. Territorio de protección.
4. Similitud: visual + fonética + conceptual = riesgo global.
5. Prioridad (fecha de solicitud/registro).

### Paso 4 — Evaluar riesgo global

- **BAJO**: No se encuentran marcas similares en clases relevantes.
- **MEDIO**: Existen marcas con alguna similitud pero en clases distintas o con diferencias significativas.
- **ALTO**: Marcas similares registradas o en trámite en las mismas clases y territorio.
- **KNOCKOUT**: Marca idéntica vigente para productos/servicios idénticos o similares.

## Formato de salida

```markdown
## Screening de marca

**Marca candidata:** [denominación]
**Tipo:** [denominativa/figurativa/mixta]
**Clases de Niza:** [lista]
**Territorio:** [España/UE/Internacional]
**Fecha del análisis:** [fecha]

### Resultado del knockout check

**Riesgo global:** [BAJO/MEDIO/ALTO/KNOCKOUT]

### Marcas anteriores relevantes

| # | Marca | Titular | Registro | Clases | Estado | Similitud visual | Similitud fonética | Similitud conceptual | Riesgo |
|---|-------|---------|----------|--------|--------|------------------|--------------------|----------------------|--------|
| 1 | [marca] | [titular] | [OEPM/EUIPO/OMPI nº] | [clases] | [estado] | [A/M/B] | [A/M/B] | [A/M/B] | [nivel] |

### Análisis de confusión

[Para cada marca de riesgo ALTO, análisis detallado de la similitud aplicando los criterios EUIPO]

### Recomendaciones

- [Proceder con registro / Modificar denominación / Descartar / Solicitar opinión especializada]

### Limitaciones de este análisis

- Búsqueda preliminar — no sustituye búsqueda profesional de similitudes.
- No cubre marcas no registradas (derechos por uso anterior).
- No incluye nombres comerciales ni denominaciones sociales.
```

## Referencias normativas

- **Ley de Marcas 17/2001**: arts. 6-9 (prohibiciones relativas).
- **Ley de Marcas art. 6.1.b**: Riesgo de confusión incluida la asociación.
- **Reglamento (UE) 2017/1001**: Marca de la Unión Europea.
- **Protocolo de Madrid** y **Arreglo de Madrid**: marcas internacionales.
- **Directrices EUIPO**: Parte C — Oposición, Sección 2 — Doble identidad y riesgo de confusión.
- **Clasificación de Niza** (12ª edición): clasificación de productos y servicios.

## Guardrails

- **NO** accede a bases de datos de registros (OEPM, EUIPO, TMview) — trabaja con datos proporcionados o conocimiento general.
- **NO** sustituye una búsqueda profesional de similitudes realizada por un agente de la propiedad industrial.
- **NO** garantiza la registrabilidad de la marca.
- **NO** presenta solicitudes de registro.
- **AVISAR** que este es un screening preliminar y se recomienda búsqueda profesional antes de solicitar.
- **ESCALAR** si el riesgo es ALTO o KNOCKOUT — recomendar consulta con agente de PI.
- **AVISAR** si la marca candidata puede incurrir en prohibiciones absolutas (art. 5 Ley de Marcas).
