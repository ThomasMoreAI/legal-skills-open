---
name: comunidad-3799-betobetico
title: /comunidad
description: Propiedad horizontal — revisa estatutos, actas de junta y derramas de comunidades de propietarios. Comprueba quórums (art. 17 LPH), impugnación de acuerdos (art. 18 LPH) y obligaciones de propietarios. Usar cuando el usuario diga "comunidad de propietarios", "junta de vecinos", "derrama", "impugnar acuerdo", "LPH", "propiedad horizontal" o adjunte actas/estatutos.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/inmobiliario/skills/comunidad
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: real-estate
language: es
---

# /comunidad

1. Cargar `~/.claude/plugins/config/claude-para-abogados/inmobiliario/CLAUDE.md` → tipo de práctica, posición habitual.
2. Obtener el documento (acta, estatutos, convocatoria) o descripción.
3. Analizar contra la LPH.
4. Generar informe con hallazgos.

```
/inmobiliario:comunidad
La comunidad ha aprobado una derrama de 50.000 EUR para instalar ascensor.
Votaron a favor 60% de las cuotas. ¿Es válido el acuerdo?
```

---

## Propósito

La Ley de Propiedad Horizontal (LPH 49/1960) regula las comunidades de propietarios con normas imperativas sobre quórums, obligaciones y derechos. Los conflictos en comunidades son frecuentes y muchos acuerdos se impugnan por defectos formales (convocatoria, quórum) o sustantivos (contenido contrario a ley o estatutos). Este skill revisa la validez de acuerdos, analiza estatutos y evalúa la viabilidad de impugnaciones.

---

## Quórums de adopción de acuerdos (art. 17 LPH)

### Unanimidad (art. 17.6)

Exigida para:
- Modificación del título constitutivo o de los estatutos (salvo las excepciones del art. 17.1-5)
- Cambio de uso de elementos comunes
- Constitución de nuevas servidumbres o derechos reales

### Mayorías cualificadas

| Acuerdo | Quórum mínimo | Art. LPH |
|---|---|---|
| **Obras de accesibilidad** (eliminación de barreras) | 3/5 de propietarios y cuotas | Art. 17.2 |
| **Infraestructuras de telecomunicaciones, energía solar, recarga de vehículos eléctricos** | 1/3 de propietarios y cuotas | Art. 17.1 |
| **División, segregación, agregación o agrupación de pisos** | 3/5 de propietarios y cuotas | Art. 17.3 |
| **Arrendamiento de elementos comunes no asignados a uso específico** | 3/5 de propietarios y cuotas | Art. 17.3 |
| **Obras o servicios no exigibles por la LPH** (piscina, jardín, etc.) | 3/5 de propietarios y cuotas | Art. 17.4 |

### Mayoría simple (art. 17.7)

Para todo lo no regulado expresamente: **mayoría de propietarios que representen la mayoría de las cuotas de participación**. En segunda convocatoria: mayoría de los asistentes que representen más de la mitad del valor de las cuotas de los presentes.

### Obligatoriedad sin quórum (art. 10)

Obras de conservación y accesibilidad **obligatorias** no requieren acuerdo de junta:
- Obras necesarias para el adecuado sostenimiento y habitabilidad
- Obras de accesibilidad cuando las solicite un propietario con discapacidad o mayor de 70 años
- Coste máximo sin acuerdo: 12 mensualidades ordinarias de gastos comunes

---

## Impugnación de acuerdos (art. 18 LPH)

### Causas de impugnación

| Causa | Art. 18.1 LPH |
|---|---|
| **Contrarios a la ley o a los estatutos** | Art. 18.1.a |
| **Gravemente lesivos para los intereses de la comunidad en beneficio de uno o varios propietarios** | Art. 18.1.b |
| **Supongan un grave perjuicio para un propietario sin obligación jurídica de soportarlo** | Art. 18.1.c |
| **Adoptados con abuso de derecho** | Art. 18.1.c (jurisprudencial) |

### Legitimación

- Propietarios que **salvaron expresamente su voto** en la junta
- Propietarios **ausentes** que manifiesten su discrepancia en el plazo de 30 días naturales desde la notificación del acta
- Propietarios indebidamente **privados de su derecho de voto**

### Plazos de impugnación (art. 18.3-4 LPH)

| Causa | Plazo |
|---|---|
| Acuerdos contrarios a la ley | **1 año** desde la notificación del acta |
| Acuerdos contrarios a los estatutos | **1 año** desde la notificación del acta |
| Acuerdos gravemente lesivos o perjudiciales | **3 meses** desde la notificación del acta |

### Requisito: estar al corriente de pago (art. 18.2 LPH)

Para impugnar, el propietario debe estar **al corriente en el pago de la totalidad de las deudas vencidas** con la comunidad, o haber **consignado judicialmente** las cantidades adeudadas.

---

## Derramas y gastos extraordinarios

| Aspecto | Norma |
|---|---|
| **Obligación de contribuir** | Art. 9.1.e LPH — según coeficiente de participación (salvo pacto estatutario diferente) |
| **Fondo de reserva** | Mínimo 10% del presupuesto ordinario (art. 9.1.f LPH) |
| **Exención de derrama** | Propietario que no votó a favor de mejoras no exigibles no está obligado a pagar (art. 17.4 LPH) — salvo que la mejora no pueda privársele y sea divisible |
| **Morosos** | Procedimiento monitorio especial (art. 21 LPH); crédito preferente sobre el piso (art. 9.1.e LPH — afección real por anualidad corriente + 3 anteriores) |

---

## Revisión de actas de junta

### Requisitos formales del acta (art. 19 LPH)

- [ ] Fecha, hora y lugar de la junta
- [ ] Indicación de si es primera o segunda convocatoria
- [ ] Nombre y cargo del convocante
- [ ] Lista de asistentes y representados (con cuotas)
- [ ] Orden del día
- [ ] Acuerdos adoptados con indicación de votos a favor, en contra y abstenciones
- [ ] Firma del presidente y del secretario
- [ ] Cierre del acta en plazo (10 días naturales — art. 19.3 LPH)
- [ ] Notificación a ausentes (en plazo)

### Defectos habituales que invalidan acuerdos

| Defecto | Consecuencia |
|---|---|
| Convocatoria defectuosa (falta de orden del día, plazo insuficiente) | Acuerdo impugnable |
| Quórum insuficiente | Acuerdo nulo |
| Acuerdo sobre asunto no incluido en el orden del día | Impugnable (salvo juntas universales) |
| Acta no notificada a ausentes | Los ausentes pueden alegar indefensión |

---

## Formato de salida

```markdown
# Revisión de propiedad horizontal

**Comunidad:** [dirección / nombre]
**Documento revisado:** [acta / estatutos / convocatoria / derrama]
**Fecha del documento:** [fecha]

---

## Hallazgos

| # | Aspecto | Observación | Riesgo | Base legal | Recomendación |
|---|---|---|---|---|---|
| 1 | [Ej., Quórum de la derrama] | [60% de cuotas para instalación de ascensor] | [Conforme] | Art. 17.2 LPH (3/5) | [Se alcanza el quórum] |
| 2 | [Ej., Notificación a ausentes] | [No consta notificación] | Alto | Art. 19.3 LPH | [Notificar en plazo] |
| ... | ... | ... | ... | ... | ... |

---

## Viabilidad de impugnación (si procede)

| Aspecto | Evaluación |
|---|---|
| **Causa de impugnación** | [art. 18.1 LPH — cuál aplica] |
| **Legitimación** | [¿Salvó voto? ¿Ausente? ¿Al corriente de pago?] |
| **Plazo** | [1 año / 3 meses desde notificación del acta] |
| **Viabilidad** | [Alta / Media / Baja] |

---

## Recomendaciones

[Acciones concretas a tomar]
```

---

## Legislación de referencia

- LPH (Ley 49/1960) de Propiedad Horizontal, reformada por:
  - Ley 8/2013, de 26 de junio (rehabilitación, regeneración y renovación urbanas)
  - RDL 7/2019, de 1 de marzo
  - Ley 10/2022, de 14 de junio (eficiencia energética)
- Código Civil arts. 392-406 (comunidad de bienes, supletorio)
- LEC arts. 812-818 (procedimiento monitorio)

---

## Lo que este skill NO hace

- No redacta estatutos de comunidad — revisa los existentes.
- No tramita la impugnación judicial — evalúa la viabilidad y los plazos.
- No gestiona la morosidad — indica el procedimiento monitorio especial y la afección real.
