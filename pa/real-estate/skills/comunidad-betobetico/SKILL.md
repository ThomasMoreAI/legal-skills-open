---
name: comunidad-betobetico
title: /comunidad
description: Propiedad horizontal — revisa reglamento de copropiedad, actas de asamblea y cuotas extraordinarias de propiedades horizontales bajo la Ley 284 de 2022. Comprueba quórums y mayorías de asamblea, impugnación de acuerdos y obligaciones de propietarios. Usar cuando el usuario diga "propiedad horizontal", "asamblea de propietarios", "cuota extraordinaria", "impugnar acuerdo", "Ley 31", "PH" o adjunte actas/reglamento de copropiedad.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/inmobiliario/skills/comunidad
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: real-estate
language: es
---

# /comunidad

1. Cargar `~/.claude/plugins/config/claude-para-abogados/inmobiliario/CLAUDE.md` → tipo de práctica, posición habitual.
2. Obtener el documento (acta, reglamento de copropiedad, convocatoria) o descripción.
3. Analizar contra la Ley 284 de 2022.
4. Generar informe con hallazgos.

```
/inmobiliario:comunidad
La PH aprobó una cuota extraordinaria de 50.000 USD para instalar ascensor.
Votaron a favor el 60% de los coeficientes. ¿Es válido el acuerdo?
```

---

## Propósito

La Ley 284 de 2022 regula el régimen de propiedad horizontal en Panamá: constitución, reglamento de copropiedad, asamblea de propietarios, administración, cuotas y resolución de conflictos. Los conflictos en propiedades horizontales son frecuentes y muchos acuerdos se impugnan por defectos formales (convocatoria, quórum) o sustantivos (contenido contrario a la ley o al reglamento). Este skill revisa la validez de acuerdos, analiza el reglamento de copropiedad y evalúa la viabilidad de impugnaciones.

La Ley 284 de 2022 subroga a la Ley 31 de 2010. La autoridad competente es la **Dirección de Propiedad Horizontal del MIVIOT** (incorporación al régimen, aprobación de reglamentos).

> **Nota de verificación:** Los porcentajes de mayorías que se indican abajo provienen de fuentes secundarias fiables; verificar en el texto oficial de la Ley 284 de 2022 antes de aplicarlos a un caso concreto.

---

## Quórums y mayorías de adopción de acuerdos (Ley 284 de 2022)

> En la Ley 284 de 2022 **cada unidad inmobiliaria tiene un voto** (no es el sistema español de doble mayoría de propietarios + coeficientes). Las unidades **morosas quedan inhabilitadas para votar** (solo voz). Los porcentajes calificados se indican abajo (verificar en el texto oficial de la Ley 284).

### Asuntos ordinarios

Los asuntos ordinarios de administración sin umbral especial se aprueban por **mayoría de las unidades presentes/al día** (un voto por unidad; las morosas no votan).

### Mayorías calificadas

| Acuerdo | Quórum / mayoría | Base legal |
|---|---|---|
| **Variación de la cuota / coeficiente de participación** | 51% de la totalidad de unidades (verificar en el texto oficial) | Ley 284 de 2022 |
| **Mejoras adicionales sobre bienes comunes** | 51% de la totalidad de unidades (verificar en el texto oficial) | Ley 284 de 2022 |
| **Modificación de fachadas** | 66% de las unidades (verificar en el texto oficial) | Ley 284 de 2022 |
| **Reforma del Reglamento de Copropiedad** | 66% de las unidades que representen ≥75% del valor (verificar en el texto oficial) | Ley 284 de 2022 |

### Obras necesarias de conservación

Lo obligatorio es la **contribución de los propietarios** a la conservación, seguridad y mantenimiento del edificio. Los gastos urgentes no presupuestados se canalizan vía **Desembolso Extraordinario** y el **Fondo para Imprevistos (art. 46 de la Ley 284 de 2022)**. No existe una facultad general de ejecutar obras sin acuerdo de la asamblea.

---

## Impugnación de acuerdos de asamblea

### Causas de impugnación

| Causa |
|---|
| Acuerdos contrarios a la Ley 284 de 2022 o a su reglamentación |
| Acuerdos contrarios al reglamento de copropiedad |
| Acuerdos gravemente lesivos para la PH en beneficio de uno o varios propietarios |
| Acuerdos que causen grave perjuicio a un propietario sin obligación de soportarlo / abuso de derecho |

### Legitimación

- Propietarios que votaron en contra y dejaron constancia de su voto en el acta
- Propietarios indebidamente privados de su derecho de voto

> **Importante:** bajo la Ley 284 de 2022 los acuerdos válidamente adoptados en asamblea vinculan tanto a los presentes como a los ausentes. No existe en Panamá el régimen español de adhesión/discrepancia de ausentes dentro de un plazo (art. 17.8 LPH española): no hay un plazo legal para que el ausente se adhiera o discrepe a efectos de quedar vinculado.

### Plazos de impugnación

| Aspecto | Plazo |
|---|---|
| Impugnación de acuerdos de asamblea | Plazo establecido en la Ley 284 de 2022 |

### Requisito: estar al corriente de pago

Para ejercer ciertos derechos (incluido a veces el voto y la impugnación), el propietario debe estar al corriente en el pago de las cuotas de la PH, o consignar lo adeudado. Verificar el alcance en la Ley 284 de 2022.

---

## Cuotas y gastos extraordinarios

| Aspecto | Norma |
|---|---|
| **Obligación de contribuir** | Según el coeficiente de participación, salvo regla distinta del reglamento de copropiedad (Ley 284 de 2022) |
| **Fondo para Imprevistos** | Obligatorio, mínimo el 1% del total de ingresos anuales de la PH; cuenta bancaria separada (art. 82); embargo limitado al 20% (art. 47) — art. 46 de la Ley 284 de 2022 |
| **Cuotas extraordinarias** | Aprobadas por la asamblea con la mayoría que corresponda a la materia; gastos urgentes no presupuestados vía Desembolso Extraordinario y Fondo para Imprevistos (art. 46) |
| **Morosos** | Cobro por proceso ejecutivo (título ejecutivo = estado de cuenta / recibos no pagados, a partir de 2 meses de mora); la obligación tiene carácter real (recae sobre la unidad con independencia del propietario); recargo de hasta 20% (Ley 284 de 2022) |

---

## Revisión de actas de asamblea

### Requisitos formales del acta

- [ ] Fecha, hora y lugar de la asamblea
- [ ] Indicación de si es primera o segunda convocatoria
- [ ] Identificación del convocante / administrador
- [ ] Lista de asistentes y representados (con coeficientes)
- [ ] Orden del día
- [ ] Acuerdos adoptados con indicación de votos a favor, en contra y abstenciones
- [ ] Firma de quien preside y del secretario
- [ ] Comunicación del acta a los propietarios ausentes (a efectos informativos; los acuerdos los vinculan sin plazo de adhesión)

### Defectos habituales que invalidan acuerdos

| Defecto | Consecuencia |
|---|---|
| Convocatoria defectuosa (falta de orden del día, plazo insuficiente) | Acuerdo impugnable |
| Quórum / mayoría insuficiente | Acuerdo nulo o impugnable |
| Acuerdo sobre asunto no incluido en el orden del día | Impugnable (salvo asamblea con presencia total) |

---

## Formato de salida

```markdown
# Revisión de propiedad horizontal

**PH:** [dirección / nombre del edificio o conjunto]
**Documento revisado:** [acta / reglamento de copropiedad / convocatoria / cuota extraordinaria]
**Fecha del documento:** [fecha]

---

## Hallazgos

| # | Aspecto | Observación | Riesgo | Base legal | Recomendación |
|---|---|---|---|---|---|
| 1 | [Ej., Quórum de la cuota] | [60% de unidades para instalación de ascensor] | [Verificar] | Ley 284 de 2022 | [Confirmar mayoría exigida; un voto por unidad, morosos no votan] |
| 2 | [Ej., Cobro de morosos] | [Estado de cuenta con 3 meses de mora] | Medio | Ley 284 de 2022 | [Proceso ejecutivo; obligación de carácter real] |
| ... | ... | ... | ... | ... | ... |

---

## Viabilidad de impugnación (si procede)

| Aspecto | Evaluación |
|---|---|
| **Causa de impugnación** | [contraria a ley / reglamento / lesiva] |
| **Legitimación** | [¿Votó en contra? ¿Ausente? ¿Al corriente de pago?] |
| **Plazo** | [plazo de la Ley 284 de 2022 — verificar] |
| **Viabilidad** | [Alta / Media / Baja] |

---

## Recomendaciones

[Acciones concretas a tomar]
```

---

## Legislación de referencia

- Ley 284 de 2022 — Régimen de propiedad horizontal en Panamá (subroga la Ley 31 de 2010); Dirección de Propiedad Horizontal del MIVIOT
- Art. 46 de la Ley 284 de 2022 — Fondo para Imprevistos (mínimo 1% de ingresos anuales; cuenta separada art. 82; embargo limitado al 20% art. 47)
- Código Civil de Panamá — copropiedad / comunidad de bienes (supletorio) [verificar]
- Código Judicial de Panamá — proceso ejecutivo para el cobro de cuotas morosas (título ejecutivo = estado de cuenta) e impugnaciones [verificar]

---

## Lo que este skill NO hace

- No redacta el reglamento de copropiedad — revisa los existentes.
- No tramita la impugnación judicial — evalúa la viabilidad y los plazos.
- No gestiona el cobro de la morosidad — indica el procedimiento aplicable bajo la Ley 284 de 2022.
