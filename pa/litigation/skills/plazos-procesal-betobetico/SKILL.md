---
name: plazos-procesal-betobetico
title: Propósito
description: Calcula términos procesales en días hábiles según el Código Judicial de Panamá, considerando días feriados y de duelo nacional
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/procesal/skills/plazos
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: litigation
language: es
---

## Propósito

Esta skill calcula términos procesales en el orden jurisdiccional civil, laboral, contencioso-administrativo y penal de Panamá. Aplica las reglas de cómputo del Código Judicial de Panamá: días hábiles, exclusión de sábados, domingos y días feriados o de duelo nacional, y reglas especiales por jurisdicción.

> **Aviso — régimen civil.** Desde el 11 de octubre de 2025 rige el Código Procesal Civil (Ley 402 de 2023) para los procesos civiles nuevos; el Código Judicial (Libro II) solo se aplica a procesos en transición (iniciados antes). Los términos civiles que siguen provienen del Código Judicial y deben confirmarse contra el Código Procesal Civil antes de aplicarlos a un proceso nuevo.

## Instrucciones

### Paso 1 — Recopilar datos de entrada

1. **Tipo de proceso**: ordinario, sumario, oral, ejecutivo, laboral, contencioso, penal.
2. **Fecha de notificación**: fecha en que se recibe la comunicación.
3. **Jurisdicción**: civil, laboral, contencioso-administrativo, penal.
4. **Provincia/distrito judicial**: para identificar días feriados locales o de duelo.
5. **Acción procesal**: contestación, recurso, oposición, etc.

### Paso 2 — Identificar término aplicable

**Jurisdicción civil (Código Judicial de Panamá; confirmar en el Código Procesal Civil para procesos nuevos):**

| Acción | Término | Base legal |
|--------|---------|------------|
| Contestación demanda (proceso ordinario) | 10 días | Código Judicial (coincide con el Código Procesal Civil) |
| Contestación (proceso sumario) | 5 días (confirmar en el Código Procesal Civil) | Código Judicial |
| Recurso de reconsideración | 2 días (confirmar en el Código Procesal Civil) | Código Judicial, art. 1129 |
| Recurso de apelación (anuncio 2 días / sustentación 5 días) | anuncio 2 días, sustentación 5 días (confirmar en el Código Procesal Civil) | Código Judicial |
| Oposición/excepciones en proceso ejecutivo | 8 días; traslado al ejecutante 5 días (confirmar en el Código Procesal Civil) | Código Judicial |
| Recurso de casación (ante la CSJ) | anuncio 3 días (art. 1173), formalización 10 días (el Código Procesal Civil podría elevarla a 15 días — confirmar) | Código Judicial |
| Recurso de hecho | 2 días para solicitar copias (art. 1152) y 3 días para alegatos (art. 1154) | Código Judicial |
| Excepción de incompetencia / excepciones | dentro del traslado de la demanda (10 días en el ordinario); en el Código Procesal Civil se ventilan en el saneamiento/audiencia preliminar | Código Judicial |

**Jurisdicción laboral (Código de Trabajo de Panamá):**

| Acción | Término | Base legal |
|--------|---------|------------|
| Recurso de apelación laboral | 3 días desde la notificación | Código de Trabajo, art. 915 |
| Recurso de casación laboral (ante la Sala Tercera de la CSJ) | 5 días | Código de Trabajo, arts. 925-927 |
| Conciliación administrativa individual ante el MITRADEL | Voluntaria (no requisito previo obligatorio general); la conciliación obligatoria es la fase dentro de la audiencia ante la Junta de Conciliación y Decisión o el Juzgado de Trabajo | Código de Trabajo |

**Jurisdicción contencioso-administrativa (Sala Tercera de la CSJ):**

| Acción | Término | Base legal |
|--------|---------|------------|
| Demanda contencioso-administrativa de plena jurisdicción | 2 meses desde la publicación/notificación/ejecución del acto | Ley 135 de 1943, art. 42-B |
| Demanda de nulidad | Sin término de caducidad (en cualquier tiempo) | Ley 135 de 1943, art. 42-A |

### Paso 3 — Aplicar reglas de cómputo

1. **Dies a quo**: los términos de días corren desde el día siguiente a la notificación; el día de la notificación NO cuenta (art. 511 del Código Judicial).
2. **Días hábiles**: solo se cuentan días hábiles; se excluyen sábados, domingos, feriados, fiesta y duelo nacional (arts. 509 y 512 del Código Judicial; art. 267 sobre días de despacho).
3. **No hay vacancia judicial general** equivalente al agosto inhábil español; los términos corren salvo declaratoria de feriado o duelo nacional. Verificar el calendario oficial del Órgano Judicial.
4. **Jurisdicción penal**: el Sistema Penal Acusatorio se rige por el Código Procesal Penal (Ley 63 de 2008); sus plazos por DÍAS también se cuentan en días hábiles (art. 142 CPP), no en días corridos. Lo que corre sin interrupción son los plazos por HORAS.
5. **Si el último día es inhábil**: se prorroga al próximo día hábil (art. 509 del Código Judicial).
6. **Términos perentorios**: los términos legales son perentorios e improrrogables (art. 507 del Código Judicial), salvo los fijados por el juez, que son prorrogables una vez (art. 510).
7. **Hora límite de presentación**: el vencimiento se produce a las 5:00 p.m. del último día del término (art. 511 del Código Judicial).

### Paso 4 — Calcular y presentar resultado

## Formato de salida

```markdown
## Cálculo de término procesal

### Datos de entrada

| Concepto | Valor |
|----------|-------|
| Proceso | [tipo] |
| Jurisdicción | [civil/laboral/contencioso/penal] |
| Acción procesal | [tipo] |
| Fecha de notificación | [fecha] |
| Término aplicable | [n] días [hábiles/calendario] |
| Base legal | [artículo del Código Judicial — verificar] |

### Cómputo

- Dies a quo (no cuenta): [fecha notificación]
- Primer día del cómputo: [fecha]
- Días inhábiles en el período: [lista de fechas con motivo]
- Feriado o duelo nacional en el período: [SÍ/NO — motivo]
- Último día del término: [fecha]
- Si cae en inhábil, prórroga a: [fecha]

### Resultado

| Fecha límite | Hora límite | Forma |
|--------------|-------------|-------|
| **[fecha]** | Hasta las 5:00 p.m. del [fecha] (art. 511) | Tribunal / sistema de notificaciones del Órgano Judicial |

### Advertencias

- [Verificar días feriados o de duelo nacional en [provincia/distrito] no incluidos en este cálculo]
- [Este cálculo es orientativo — verificar con el calendario oficial del Órgano Judicial]
```

## Referencias normativas

- **Código Judicial de Panamá, arts. 509 y 512**: días hábiles (exclusión de sábados, domingos, feriados, fiesta y duelo nacional); art. 267 sobre días de despacho.
- **Código Judicial de Panamá, art. 509**: prórroga al próximo día hábil si el último día es inhábil.
- **Código Judicial de Panamá, arts. 507 y 510**: términos perentorios e improrrogables, salvo los fijados por el juez (prorrogables una vez).
- **Código Judicial de Panamá, art. 511**: cómputo desde el día siguiente a la notificación y vencimiento a las 5:00 p.m. del último día.
- **Código Procesal Penal (Ley 63 de 2008), art. 142**: cómputo de plazos en el Sistema Penal Acusatorio (días por días hábiles; horas sin interrupción).
- **Código de Trabajo de Panamá, art. 915** (apelación, 3 días) **y arts. 925-927** (casación laboral, 5 días).
- **Ley 135 de 1943, arts. 42-A y 42-B**: términos en lo contencioso-administrativo (Sala Tercera de la CSJ).

## Guardrails

- **NO** garantiza la exactitud del cómputo — es orientativo y debe verificarse.
- **NO** tiene acceso al calendario oficial del Órgano Judicial ni a los días feriados o de duelo nacional declarados.
- **NO** presenta escritos ni gestiona términos en el sistema de notificaciones del Órgano Judicial.
- **AVISAR** siempre: "Este cálculo es orientativo. Verifique con el calendario oficial del Órgano Judicial."
- **AVISAR** si el término puede verse afectado por días feriados o de duelo nacional y hay duda.
- **ESCALAR** si el término vence en menos de 3 días hábiles.
- **ESCALAR** si hay duda sobre la habilidad de un día para el caso concreto.
