---
name: plan-betobetico
title: /plan
description: Estructura un plan de reorganización conforme a la Ley 12 de 2016 (proceso concursal de insolvencia de Panamá). Genera el esqueleto del plan con sus secciones, verifica las mayorías necesarias y produce un documento base para revisión letrada. Usar cuando el usuario dice "plan de reorganización", "necesito reestructurar la deuda", "prepara el plan de viabilidad", o tras un diagnóstico que recomiende la reorganización.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/concursal/skills/plan
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: bankruptcy
language: es
---

# /plan

1. Leer `~/.claude/plugins/config/claude-para-abogados/concursal/CLAUDE.md` — perfil de práctica.
2. Si existe diagnóstico previo (`/concursal:diagnostico`), cargarlo como contexto.
3. Recopilar información de deudor y acreedores.
4. Estructurar el plan conforme a la Ley 12 de 2016.
5. Calcular mayorías necesarias.
6. Producir el documento base del plan.

---

## Propósito

Generar la estructura completa de un plan de reorganización que cumpla los requisitos formales de la Ley 12 de 2016, con contenido base que el abogado pueda completar y adaptar. El plan es un borrador — requiere revisión profesional y negociación con acreedores.

## Datos necesarios

- **Datos del deudor:** forma jurídica, actividad, planilla, situación financiera (del diagnóstico o nuevos).
- **Lista de acreedores:** nombre, importe, tipo de crédito (con garantía real, privilegiado/preferente, ordinario, subordinado), garantías.
- **Activos del deudor:** inmuebles, maquinaria, inventario, cuentas por cobrar, participaciones.
- **Propuesta de pagos:** quitas, esperas, conversión en capital, dación en pago.
- **Plan de viabilidad:** proyecciones de ingresos y gastos a 3-5 años.
- **Medidas laborales previstas:** si hay reducciones de planilla, modificaciones de condiciones (sujetas al Código de Trabajo de Panamá).

## Estructura del plan (Ley 12 de 2016)

### Parte A: Descripción de la situación

- Identificación del deudor.
- Causas de la insolvencia o dificultad financiera.
- Descripción del activo y pasivo.
- Lista de acreedores afectados y no afectados.

### Parte B: Plan de viabilidad

- Descripción de la actividad futura.
- Proyecciones financieras (3-5 años): estado de resultados, flujos de caja, balance previsional.
- Hipótesis empleadas y escenarios (base, optimista, pesimista).
- Hitos de cumplimiento.

### Parte C: Propuesta de pagos

| Clase de acreedor | Medida propuesta | Quita | Espera | Otras medidas |
|---|---|---|---|---|
| Con garantía real / privilegio especial | [medida] | [%] | [años] | [conversión/dación] |
| Privilegiado / preferente (laboral, fiscal, CSS) | [medida] | [%] | [años] | [conversión/dación] |
| Ordinarios / comunes | [medida] | [%] | [años] | [conversión/dación] |
| Subordinados | [medida] | [%] | [años] | [conversión/dación] |

### Parte D: Medidas laborales

- Reducciones de planilla o terminaciones (si aplica), conforme al Código de Trabajo de Panamá.
- Modificaciones de condiciones de trabajo.
- Tratamiento de salarios, prestaciones y décimo tercer mes.
- Coordinación con el MITRADEL cuando proceda [verificar].

### Parte E: Garantías de cumplimiento

- Mecanismos de supervisión.
- Administrador o restructurador del proceso [verificar].
- Consecuencias de incumplimiento (apertura de liquidación).

## Mayorías necesarias (Ley 12 de 2016)

### Clases de acreedores afectados

Los acreedores se agrupan por categoría de crédito. La votación del plan se hace conforme a la Ley 12 de 2016.

| Clase | Mayoría requerida | Base de cálculo |
|---|---|---|
| Acreedores con garantía real / privilegio especial | Mayoría conforme a la Ley 12 de 2016 | Importe de los créditos de la clase |
| Acreedores privilegiados / preferentes | Mayoría conforme a la Ley 12 de 2016 | Importe de los créditos de la clase |
| Acreedores ordinarios / comunes | Mayoría conforme a la Ley 12 de 2016 | Importe de los créditos de la clase |
| Acreedores subordinados | Tratamiento conforme a la Ley 12 de 2016 | [verificar] |

### Confirmación / aprobación judicial del plan

- El plan aprobado por los acreedores se somete a confirmación del juez [verificar].
- Requisito: aprobación por las mayorías legales en las clases afectadas [verificar].
- Posibilidad de vincular a acreedores disidentes conforme a la Ley 12 de 2016 — verificar requisitos y alcance [verificar].

## Formato de salida

```markdown
BORRADOR — PLAN DE REORGANIZACIÓN — REVISIÓN LETRADA OBLIGATORIA

> **Nota para el revisor**
> - **Datos analizados:** [fuentes y datos utilizados]
> - **Elementos marcados [verificar]:** [N]
> - **Antes de actuar:** validar proyecciones financieras con experto; negociar con acreedores; verificar mayorías en la Ley 12 de 2016; consultar con abogado especializado en derecho concursal.

## Plan de reorganización: [Nombre del deudor]

[Estructura completa con las Partes A-E rellenadas con los datos disponibles y marcadores [COMPLETAR] donde falten datos]

## Cálculo de mayorías

[Tabla con el cálculo de mayorías por clase]

## Calendario estimado

| Hito | Plazo | Fecha estimada |
|---|---|---|
| Solicitud de reorganización | Día 0 | [fecha] |
| Negociación con acreedores | [plazo — verificar] | [fecha] |
| Votación del plan | [plazo — verificar] | [fecha] |
| Solicitud de confirmación judicial | Tras aprobación | [fecha] |

---

**Qué hacer a continuación:**
1. **Completar el plan** — relleno las secciones marcadas [COMPLETAR] con datos que aportes.
2. **Calcular mayorías detalladas** — con la lista completa de acreedores.
3. **Clasificar créditos** — `/concursal:creditos` para clasificar cada crédito.
4. **Revisar viabilidad** — analizo las proyecciones financieras en detalle.
5. **Otra cosa** — dime qué necesitas.
```

## Referencias legislativas

- **Ley 12 de 2016** — proceso concursal de insolvencia (reorganización y liquidación) en Panamá [verificar].
- **Solicitud y trámite de la reorganización** — Ley 12 de 2016.
- **Contenido del plan de reorganización** — Ley 12 de 2016.
- **Clases de acreedores y mayorías** — Ley 12 de 2016.
- **Confirmación judicial del plan** — Ley 12 de 2016.
- **Administrador / restructurador del proceso** — Ley 12 de 2016.
- **Código de Trabajo de Panamá** — medidas laborales, prelación de créditos laborales.

*Nota: la Directiva (UE) 2019/1023 de reestructuración no es derecho aplicable en Panamá; en su caso, solo referencia comparada internacional.*

## Guardarraíles

- **Las proyecciones financieras son del usuario, no del skill.** No inventar cifras. Si no hay proyecciones, marcar [COMPLETAR] y advertir que sin plan de viabilidad creíble el plan fracasará.
- **Las mayorías dependen de la clasificación exacta de créditos.** Si la clasificación es aproximada, advertirlo. No inventar el porcentaje de mayoría: usar referencia a la Ley 12 de 2016 + `[verificar]`.
- **El arrastre de disidentes es excepcional.** No presentarlo como la norma — requiere requisitos legales que deben verificarse en la Ley 12 de 2016.
- **Las medidas laborales requieren cumplir el Código de Trabajo de Panamá.** No se pueden imponer unilateralmente sin observar el procedimiento aplicable.
- **Siempre derivar a abogado especializado en derecho concursal y, en su caso, a un contador/experto financiero para el plan de viabilidad.**
