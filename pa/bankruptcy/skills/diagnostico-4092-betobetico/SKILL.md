---
name: diagnostico-4092-betobetico
title: /diagnostico
description: 'Analiza la situación de un deudor frente a la Ley 12 de 2016 (proceso concursal de insolvencia de Panamá) para determinar si existe insolvencia o cesación de pagos, evalúa el presupuesto subjetivo y recomienda la vía procesal más adecuada: proceso de reorganización o proceso de liquidación. Usar cuando el usuario dice "diagnóstico de insolvencia", "¿estoy en situación concursal?", "evalúa la situación del deudor", o aporta datos financieros de una empresa en dificultades.'
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/concursal/skills/diagnostico
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: bankruptcy
language: es
---

# /diagnostico

1. Leer `~/.claude/plugins/config/claude-para-abogados/concursal/CLAUDE.md` — perfil de práctica.
2. Recopilar datos del deudor según el flujo de abajo.
3. Analizar presupuestos objetivo y subjetivo.
4. Evaluar opciones procesales.
5. Producir el diagnóstico con plazos y recomendación.

---

## Propósito

Determinar si un deudor se encuentra en situación de insolvencia y, en caso afirmativo, recomendar la vía procesal más adecuada dentro de la Ley 12 de 2016. El diagnóstico es una herramienta de orientación — NO sustituye el análisis completo de un abogado especializado en derecho concursal.

## Datos necesarios

Solicitar al usuario los siguientes datos. Si faltan, preguntar — no inferir:

- **Forma jurídica del deudor** — persona natural, S.A. (sociedad anónima), S. de R.L., fundación de interés privado, otro.
- **Balance de situación** — activo corriente, activo no corriente, pasivo corriente, pasivo no corriente, patrimonio neto.
- **Estado de resultados** — ingresos, gastos, EBITDA, resultado del ejercicio.
- **Vencimientos próximos** — deudas que vencen en los próximos 3, 6 y 12 meses.
- **Incumplimientos actuales** — impagos a proveedores, DGI (Dirección General de Ingresos), CSS (Caja de Seguro Social), entidades financieras, trabajadores (salarios, décimo tercer mes).
- **Embargos o ejecuciones en curso** — si los hay.
- **Planilla** — número de trabajadores.

## Análisis del presupuesto objetivo (Ley 12 de 2016)

### Cesación de pagos / insolvencia actual

El deudor no puede atender el cumplimiento regular de sus obligaciones líquidas y exigibles. Indicios:

| Indicio | Fuente | Peso |
|---|---|---|
| Impagos generalizados a proveedores | Datos del deudor | Alto |
| Deudas con DGI/CSS en cobro coactivo | Datos del deudor | Alto |
| Patrimonio neto negativo | Balance | Medio-alto |
| Ratio de liquidez < 0,5 | Balance | Medio |
| Ejecuciones sin bienes suficientes | Datos del deudor | Alto |
| Impago de salarios o décimo tercer mes | Datos del deudor | Muy alto |

### Insolvencia inminente

El deudor prevé que no podrá cumplir regular y puntualmente sus obligaciones exigibles [verificar]. Generalmente solo el propio deudor puede invocarla.

### Probabilidad de insolvencia

Relevante para la vía de reorganización — probabilidad objetiva de no poder cumplir a medida que venzan las obligaciones [verificar].

## Análisis del presupuesto subjetivo (Ley 12 de 2016)

- **Persona natural** — verificar el ámbito subjetivo de la Ley 12 de 2016.
- **Persona jurídica** — sociedades anónimas, S. de R.L. y demás formas societarias [verificar].
- **Exclusiones** — entidades de derecho público y entidades sujetas a regímenes especiales (p. ej. bancos bajo la Superintendencia de Bancos, aseguradoras) [verificar].

## Evaluación de opciones

### Opción 1: Proceso de reorganización

- **Requisito:** insolvencia, cesación de pagos o riesgo de insolvencia, según la Ley 12 de 2016.
- **Efecto:** protección frente a ejecuciones durante el trámite y negociación de un plan de reorganización con los acreedores [verificar].
- **Plazo:** los plazos de negociación y aprobación del plan conforme a la Ley 12 de 2016.
- **Ventaja:** permite la continuidad de la empresa viable si se aprueba el plan.
- **Riesgo:** si fracasa el plan o se incumple, se abre el proceso de liquidación [verificar].

### Opción 2: Proceso de liquidación (voluntaria)

- **Requisito:** insolvencia o cesación de pagos [verificar].
- **Plazo:** deber de solicitar el proceso dentro del plazo que fije la Ley 12 de 2016 desde que el deudor conoció o debió conocer su insolvencia [verificar].
- **Consecuencia de retraso:** riesgo de responsabilidad de los administradores y, en su caso, consecuencias penales por conducta dolosa o fraudulenta [verificar].

### Opción 3: Proceso a instancia de acreedor

- **Legitimación:** acreedor que acredite hechos reveladores de la insolvencia del deudor [verificar].
- **Hechos reveladores:** sobreseimiento general de pagos, ejecuciones sin bienes, ocultación o alzamiento de bienes, incumplimiento generalizado tributario/CSS/salarial [verificar].

## Formato de salida

```markdown
BORRADOR — DIAGNÓSTICO DE INSOLVENCIA — REVISIÓN LETRADA OBLIGATORIA

> **Nota para el revisor**
> - **Datos analizados:** [qué datos se aportaron y cuáles faltan]
> - **Elementos marcados [verificar]:** [N]
> - **Antes de actuar:** confirmar datos financieros actualizados; verificar plazos en la Ley 12 de 2016; consultar con abogado especializado en derecho concursal.

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

**Conclusión:** [insolvencia actual / cesación de pagos / insolvencia inminente / probabilidad de insolvencia / no apreciada]

### Opciones y plazos

| Opción | Viable | Plazo | Observaciones |
|---|---|---|---|
| Proceso de reorganización | [sí/no] | [plazo — verificar] | [notas] |
| Proceso de liquidación voluntaria | [sí/no] | [plazo — verificar] | [notas] |
| Otras medidas | [descripción] | [plazo] | [notas] |

### Recomendación

[Recomendación motivada — siempre con la advertencia de que requiere validación profesional]

### Plazos críticos

| Plazo | Fecha límite | Consecuencia de incumplimiento |
|---|---|---|
| Deber de solicitar el proceso [verificar] | [fecha — verificar] | Riesgo de responsabilidad de administradores |
| Solicitud de reorganización | [si procede] | [efectos — verificar] |

---

**Qué hacer a continuación:**
1. **Solicitud de reorganización** — preparo el escrito de solicitud ante el juzgado competente.
2. **Solicitud de liquidación voluntaria** — preparo la solicitud con la documentación exigida por la Ley 12 de 2016.
3. **Plan de reorganización** — `/concursal:plan` para estructurar el plan.
4. **Obtener más datos** — faltan [datos] para completar el análisis.
5. **Otra cosa** — dime qué necesitas.
```

## Referencias legislativas

- **Ley 12 de 2016** — por la cual se establece el proceso concursal de insolvencia (reorganización y liquidación) en Panamá [verificar].
- **Presupuestos del proceso concursal** — Ley 12 de 2016.
- **Cesación de pagos / insolvencia** — Ley 12 de 2016.
- **Deber de solicitar el proceso (plazo)** — Ley 12 de 2016.
- **Proceso de reorganización** — Ley 12 de 2016.
- **Responsabilidad por conducta dolosa o fraudulenta** — Ley 12 de 2016 / Código Penal de Panamá [verificar].

## Guardarraíles

- **Nunca afirmar que NO hay insolvencia sin datos completos.** Si faltan datos, el diagnóstico es parcial — decirlo.
- **Nunca recomendar no solicitar el proceso si hay indicios claros de cesación de pagos.** El riesgo de responsabilidad de los administradores es demasiado grave.
- **Los plazos son críticos.** Errar en un plazo puede suponer responsabilidad personal de los administradores. Marcar siempre `[verificar]` en fechas y plazos calculados.
- **No confundir insolvencia con falta de liquidez puntual.** Un impago aislado no es necesariamente insolvencia.
- **No inventar números de artículo ni plazos de la Ley 12 de 2016.** Usar referencia genérica + `[verificar]` cuando no haya certeza.
- **Siempre derivar a abogado especializado en derecho concursal.** Este diagnóstico es orientativo.
