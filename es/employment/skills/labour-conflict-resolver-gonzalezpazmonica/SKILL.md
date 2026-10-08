---
name: labour-conflict-resolver-gonzalezpazmonica
title: labour-conflict-resolver — Asistente de Resolución de Conflictos Laborales
description: Analiza conflictos laborales (individuales y colectivos) y propone mínimo 3 opciones de resolución con base legal, coste estimado y recomendación. Incluye cálculo de improcedente.
author: gonzalezpazmonica
author_url: https://github.com/gonzalezpazmonica/savia/tree/main/.claude/skills/professional-domain/labour/labour-conflict-resolver
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: employment
language: es
---

# labour-conflict-resolver — Asistente de Resolución de Conflictos Laborales

## Cuándo usar esta skill

- Ante un conflicto laboral individual (despido, sanción, modificación sustancial).
- Cuando la empresa recibe una demanda o papeleta de conciliación SMAC.
- Para evaluar si merece la pena negociar, conciliar o ir a juicio.
- Para calcular el coste estimado de un despido improcedente.
- Ante un conflicto colectivo (huelga, descuelgue, modificación de condiciones).

## Inputs requeridos

| Campo | Descripción | Ejemplo |
|---|---|---|
| `descripcion` | Situación del conflicto en detalle | "Trabajador despedido el 20/06 por falta muy grave, lleva 8 años" |
| `partes` | Empresa y trabajador / sindicato implicados | "Empresa 50 trabajadores, trabajador con delegado de personal" |
| `situacion_actual` | Estado del proceso | "Papeleta SMAC presentada el 25/06/2026" |
| `resultado_deseado` | Qué quiere conseguir quien consulta | "Evitar juicio con acuerdo razonable" |

## Inputs opcionales

| Campo | Descripción |
|---|---|
| `salario_bruto_anual` | Para calcular coste de improcedente |
| `antiguedad_anos` | Años de servicio para calcular indemnización |
| `tipo_contrato` | Indefinido / temporal / fijo-discontinuo |
| `convenio` | Para verificar régimen disciplinario aplicable |

## Outputs producidos

1. **Análisis del conflicto** — calificación jurídica probable, fortalezas/debilidades de cada parte
2. **Tres opciones de resolución** (mínimo), cada una con:
   - Descripción del camino
   - Base legal aplicable
   - Pros / contras
   - Riesgo estimado (ALTO / MEDIO / BAJO)
   - Coste económico estimado (si se proporcionan datos salariales)
3. **Camino recomendado** — con justificación objetiva
4. **Consideraciones legales críticas** — plazos, papeleta SMAC, garantías sindicales
5. **Fórmula de cálculo de improcedente** (si aplica)
6. **Disclaimer laboral** — obligatorio al final

## Outputs excluidos

- Representación en juicio ni en SMAC
- Predicción del resultado judicial con garantía
- Redacción de demandas o escritos procesales

## Relación con otras skills

- **Upstream**: `labour-convention-analyzer` (identificar régimen disciplinario del convenio)
- **Downstream**: `labour-document-drafter` (redactar acuerdo de extinción si se negocia)
- **Paralelo**: `labour-onboarding-offboarding` (documentación de salida tras resolución)

## Ver también

- `DOMAIN.md` — fases del proceso laboral, cálculo de indemnizaciones, criterios de proporcionalidad
- `prompt.md` — instrucciones de análisis y producción de opciones para el modelo
