---
name: diagnostico-betobetico
title: /diagnostico
description: 'Analiza la situación de un deudor frente al Texto Refundido de la Ley Concursal (TRLC) para determinar si existe insolvencia actual o inminente, evalúa el presupuesto subjetivo y recomienda la vía procedimental más adecuada: comunicación del art. 583 (pre-concurso) o solicitud de concurso directo. Usar cuando el usuario dice "diagnóstico de insolvencia", "¿estoy en situación concursal?", "evalúa la situación del deudor", o aporta datos financieros de una empresa en dificultades.'
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/concursal/skills/diagnostico
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: bankruptcy
language: es
---

# /diagnostico

1. Leer `~/.claude/plugins/config/claude-para-abogados/concursal/CLAUDE.md` — perfil de práctica.
2. Recopilar datos del deudor según el flujo de abajo.
3. Analizar presupuestos objetivo y subjetivo.
4. Evaluar opciones procedimentales.
5. Producir el diagnóstico con plazos y recomendación.

---

## Propósito

Determinar si un deudor se encuentra en situación de insolvencia y, en caso afirmativo, recomendar la vía procedimental más adecuada dentro del TRLC. El diagnóstico es una herramienta de orientación — NO sustituye el análisis completo de un letrado concursalista.

## Datos necesarios

Solicitar al usuario los siguientes datos. Si faltan, preguntar — no inferir:

- **Forma jurídica del deudor** — persona física, SL, SA, cooperativa, otro.
- **Balance de situación** — activo corriente, activo no corriente, pasivo corriente, pasivo no corriente, patrimonio neto.
- **Cuenta de resultados** — ingresos, gastos, EBITDA, resultado del ejercicio.
- **Vencimientos próximos** — deudas que vencen en los próximos 3, 6 y 12 meses.
- **Incumplimientos actuales** — impagos a proveedores, AEAT, TGSS, entidades financieras, trabajadores.
- **Embargos o ejecuciones en curso** — si los hay.
- **Plantilla** — número de trabajadores.

## Análisis del presupuesto objetivo (art. 2 TRLC)

### Insolvencia actual (art. 2.3 TRLC)

El deudor no puede cumplir regularmente sus obligaciones exigibles. Indicios:

| Indicio | Fuente | Peso |
|---|---|---|
| Impagos generalizados a proveedores | Datos del deudor | Alto |
| Deudas con AEAT/TGSS en ejecutiva | Datos del deudor | Alto |
| Patrimonio neto negativo | Balance | Medio-alto |
| Ratio de liquidez < 0,5 | Balance | Medio |
| Ejecuciones singulares sin bienes suficientes | Datos del deudor | Alto |
| Impago de nóminas | Datos del deudor | Muy alto |

### Insolvencia inminente (art. 2.3 TRLC)

El deudor prevé que no podrá cumplir regular y puntualmente sus obligaciones exigibles. Solo el propio deudor puede invocarla.

### Insolvencia probable (art. 584.2 TRLC)

Relevante para planes de reestructuración — probabilidad objetiva de no poder cumplir a medida que venzan.

## Análisis del presupuesto subjetivo (arts. 1-2 TRLC)

- **Persona física** — sí, incluidos autónomos.
- **Persona jurídica** — cualquier forma societaria.
- **Herencia yacente** — posible.
- **Exclusiones** — entidades de derecho público, organismos reguladores (regímenes especiales).

## Evaluación de opciones

### Opción 1: Comunicación del art. 583 TRLC (pre-concurso)

- **Requisito:** insolvencia actual, inminente o probable.
- **Efecto:** suspensión del deber de solicitar concurso durante 3 meses (art. 583).
- **Plazo:** 3 meses para negociar plan de reestructuración o alcanzar acuerdos.
- **Ventaja:** evita el concurso si se logra acuerdo; paraliza ejecuciones singulares (art. 588).
- **Riesgo:** si no se alcanza acuerdo, deber de solicitar concurso en el mes siguiente.

### Opción 2: Concurso voluntario

- **Requisito:** insolvencia actual o inminente.
- **Plazo:** deber de solicitar dentro de los 2 meses desde que el deudor conoció o debió conocer su insolvencia (art. 5.1 TRLC).
- **Consecuencia de retraso:** riesgo de calificación culpable (art. 442 TRLC).

### Opción 3: Concurso necesario

- **Legitimación:** cualquier acreedor que acredite hechos externos reveladores de insolvencia (art. 2.4 TRLC).
- **Hechos reveladores:** sobreseimiento general de pagos, embargos sin bienes, alzamiento de bienes, incumplimiento generalizado tributario/SS/salarial.

## Formato de salida

```markdown
BORRADOR — DIAGNÓSTICO DE INSOLVENCIA — REVISIÓN LETRADA OBLIGATORIA

> **Nota para el revisor**
> - **Datos analizados:** [qué datos se aportaron y cuáles faltan]
> - **Elementos marcados [verificar]:** [N]
> - **Antes de actuar:** confirmar datos financieros actualizados; verificar plazos; consultar con letrado concursalista.

## Diagnóstico de insolvencia: [Nombre del deudor]

**Fecha:** [fecha]
**Tipo de deudor:** [forma jurídica]

### Presupuesto subjetivo

[Análisis — cumple / no cumple]

### Presupuesto objetivo

| Indicador | Valor | Conclusión |
|---|---|---|
| Patrimonio neto | [valor] | [positivo/negativo] |
| Ratio de liquidez | [valor] | [suficiente/insuficiente] |
| Impagos actuales | [descripción] | [generalizados/puntuales] |
| Vencimientos próximos | [descripción] | [asumibles/inasumibles] |

**Conclusión:** [insolvencia actual / inminente / probable / no apreciada]

### Opciones y plazos

| Opción | Viable | Plazo | Observaciones |
|---|---|---|---|
| Comunicación art. 583 (pre-concurso) | [sí/no] | [plazo] | [notas] |
| Concurso voluntario | [sí/no] | [plazo] | [notas] |
| Otras medidas | [descripción] | [plazo] | [notas] |

### Recomendación

[Recomendación motivada — siempre con la advertencia de que requiere validación profesional]

### Plazos críticos

| Plazo | Fecha límite | Consecuencia de incumplimiento |
|---|---|---|
| Deber de solicitar concurso (art. 5.1) | [fecha] | Riesgo de calificación culpable |
| Comunicación art. 583 | [si procede] | [efectos] |

---

**Qué hacer a continuación:**
1. **Comunicación pre-concurso** — preparo el escrito de comunicación al juzgado.
2. **Solicitud de concurso voluntario** — preparo la solicitud con la documentación del art. 6 TRLC.
3. **Plan de reestructuración** — `/concursal:plan` para estructurar el plan.
4. **Obtener más datos** — faltan [datos] para completar el análisis.
5. **Otra cosa** — dime qué necesitas.
```

## Referencias legislativas

- **TRLC** — Real Decreto Legislativo 1/2020, de 5 de mayo, por el que se aprueba el Texto Refundido de la Ley Concursal.
- **Arts. 1-7 TRLC** — presupuestos del concurso.
- **Art. 2.3 TRLC** — insolvencia actual e inminente.
- **Art. 5.1 TRLC** — deber de solicitar concurso (plazo de 2 meses).
- **Art. 583 TRLC** — comunicación de inicio de negociaciones (pre-concurso).
- **Art. 442 TRLC** — calificación culpable.

## Guardarraíles

- **Nunca afirmar que NO hay insolvencia sin datos completos.** Si faltan datos, el diagnóstico es parcial — decirlo.
- **Nunca recomendar no solicitar concurso si hay indicios claros de insolvencia actual.** El riesgo de calificación culpable es demasiado grave.
- **Los plazos son críticos.** Errar en un plazo puede suponer responsabilidad personal de los administradores. Marcar siempre `[verificar]` en fechas calculadas.
- **No confundir insolvencia con falta de liquidez puntual.** Un impago aislado no es necesariamente insolvencia.
- **Siempre derivar a letrado concursalista.** Este diagnóstico es orientativo.
