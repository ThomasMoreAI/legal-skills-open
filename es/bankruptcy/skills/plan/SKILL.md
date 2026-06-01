---
name: plan
title: /plan
description: Estructura un plan de reestructuración conforme al Libro II del TRLC (arts. 614 y ss.). Genera el esqueleto del plan con sus secciones obligatorias, verifica mayorías necesarias y produce un documento base para revisión letrada. Usar cuando el usuario dice "plan de reestructuración", "necesito reestructurar la deuda", "prepara el plan de viabilidad", o tras un diagnóstico que recomiende pre-concurso.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/concursal/skills/plan
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: bankruptcy
language: es
---

# /plan

1. Leer `~/.claude/plugins/config/claude-para-abogados/concursal/CLAUDE.md` — perfil de práctica.
2. Si existe diagnóstico previo (`/concursal:diagnostico`), cargarlo como contexto.
3. Recopilar información de deudor y acreedores.
4. Estructurar el plan conforme al TRLC Libro II.
5. Calcular mayorías necesarias.
6. Producir el documento base del plan.

---

## Propósito

Generar la estructura completa de un plan de reestructuración que cumpla los requisitos formales del TRLC, con contenido base que el letrado pueda completar y adaptar. El plan es un borrador — requiere revisión profesional y negociación con acreedores.

## Datos necesarios

- **Datos del deudor:** forma jurídica, actividad, plantilla, situación financiera (del diagnóstico o nuevos).
- **Lista de acreedores:** nombre, importe, tipo de crédito (privilegiado especial, privilegio general, ordinario, subordinado), garantías.
- **Activos del deudor:** inmuebles, maquinaria, existencias, créditos, participaciones.
- **Propuesta de pagos:** quitas, esperas, conversión en capital, dación en pago.
- **Plan de viabilidad:** proyecciones de ingresos y gastos a 3-5 años.
- **Medidas laborales previstas:** si hay ERE, ERTE, modificaciones sustanciales.

## Estructura del plan (art. 633 TRLC)

### Parte A: Descripción de la situación

- Identificación del deudor.
- Causas de la insolvencia o dificultad financiera.
- Descripción del activo y pasivo.
- Lista de acreedores afectados y no afectados.

### Parte B: Plan de viabilidad

- Descripción de la actividad futura.
- Proyecciones financieras (3-5 años): cuenta de resultados, flujos de caja, balance previsional.
- Hipótesis empleadas y escenarios (base, optimista, pesimista).
- Hitos de cumplimiento.

### Parte C: Propuesta de pagos

| Clase de acreedor | Medida propuesta | Quita | Espera | Otras medidas |
|---|---|---|---|---|
| Privilegio especial (art. 270) | [medida] | [%] | [años] | [conversión/dación] |
| Privilegio general (art. 280) | [medida] | [%] | [años] | [conversión/dación] |
| Ordinarios (art. 284) | [medida] | [%] | [años] | [conversión/dación] |
| Subordinados (art. 281) | [medida] | [%] | [años] | [conversión/dación] |

### Parte D: Medidas laborales

- ERE / ERTE previsto (si aplica).
- Modificaciones sustanciales de condiciones de trabajo.
- Consulta con representantes de los trabajadores.
- Medidas de acompañamiento social.

### Parte E: Garantías de cumplimiento

- Mecanismos de supervisión.
- Fiduciario o experto en reestructuración (art. 672 TRLC).
- Consecuencias de incumplimiento.

## Mayorías necesarias (arts. 629-632 TRLC)

### Clases de acreedores afectados

Los acreedores se agrupan en clases según su crédito. La votación es por clases.

| Clase | Mayoría requerida | Base de cálculo |
|---|---|---|
| Acreedores con privilegio especial | 2/3 del pasivo de la clase | Importe de los créditos de la clase |
| Acreedores con privilegio general | 2/3 del pasivo de la clase | Importe de los créditos de la clase |
| Acreedores ordinarios | 2/3 del pasivo de la clase | Importe de los créditos de la clase |
| Acreedores subordinados | Pueden ser vinculados sin voto | Art. 631 TRLC |

### Homologación judicial (art. 649 TRLC)

- El plan puede homologarse judicialmente para vincular a acreedores disidentes.
- Requisito: aprobación por mayorías en cada clase afectada.
- Arrastre inter-clase (cross-class cram-down): posible si se cumplen los requisitos del art. 654 TRLC y la regla del mejor interés del acreedor.

## Formato de salida

```markdown
BORRADOR — PLAN DE REESTRUCTURACIÓN — REVISIÓN LETRADA OBLIGATORIA

> **Nota para el revisor**
> - **Datos analizados:** [fuentes y datos utilizados]
> - **Elementos marcados [verificar]:** [N]
> - **Antes de actuar:** validar proyecciones financieras con experto; negociar con acreedores; verificar mayorías; consultar con letrado concursalista.

## Plan de reestructuración: [Nombre del deudor]

[Estructura completa con las Partes A-E rellenadas con los datos disponibles y marcadores [COMPLETAR] donde falten datos]

## Cálculo de mayorías

[Tabla con el cálculo de mayorías por clase]

## Calendario estimado

| Hito | Plazo | Fecha estimada |
|---|---|---|
| Comunicación art. 583 | Día 0 | [fecha] |
| Negociación con acreedores | 3 meses | [fecha] |
| Votación del plan | Antes del fin del plazo | [fecha] |
| Solicitud de homologación | Tras aprobación | [fecha] |

---

**Qué hacer a continuación:**
1. **Completar el plan** — relleno las secciones marcadas [COMPLETAR] con datos que aportes.
2. **Calcular mayorías detalladas** — con la lista completa de acreedores.
3. **Calificar créditos** — `/concursal:creditos` para clasificar cada crédito.
4. **Revisar viabilidad** — analizo las proyecciones financieras en detalle.
5. **Otra cosa** — dime qué necesitas.
```

## Referencias legislativas

- **TRLC Libro II** — De la reestructuración (arts. 583-720).
- **Art. 583 TRLC** — comunicación de inicio de negociaciones.
- **Art. 633 TRLC** — contenido del plan de reestructuración.
- **Arts. 629-632 TRLC** — clases de acreedores y mayorías.
- **Art. 649 TRLC** — homologación judicial del plan.
- **Art. 654 TRLC** — arrastre inter-clase (cross-class cram-down).
- **Art. 672 TRLC** — experto en reestructuración.
- **Directiva (UE) 2019/1023** — sobre marcos de reestructuración preventiva.

## Guardarraíles

- **Las proyecciones financieras son del usuario, no del skill.** No inventar cifras. Si no hay proyecciones, marcar [COMPLETAR] y advertir que sin plan de viabilidad creíble el plan fracasará.
- **Las mayorías dependen de la clasificación exacta de créditos.** Si la clasificación es aproximada, advertirlo.
- **El arrastre inter-clase es excepcional.** No presentarlo como la norma — requiere requisitos estrictos (art. 654 TRLC).
- **Las medidas laborales requieren negociación con representantes de los trabajadores.** No se pueden imponer unilateralmente.
- **Siempre derivar a letrado concursalista y, en su caso, a economista para el plan de viabilidad.**
