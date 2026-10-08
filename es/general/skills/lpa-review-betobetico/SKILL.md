---
name: lpa-review-betobetico
title: LPA Review
description: Revisión de LPA — desviaciones vs template casa, clasificación por materialidad, posicionamiento del GP. Triggers en "LPA review", "revisar LPA", "limited partnership agreement", "pacto de fondo".
author: betobetico
author_url: https://github.com/betobetico/claude-para-servicios-financieros/tree/main/plugins/verticales/legal-fondos/skills/lpa-review
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: general
language: es
---

# LPA Review

## Paso 0
Carga perfil. Lee también el template LPA casa del usuario (si no lo tiene, pide que lo proporcione).

## Paso 1 — Inputs

- LPA propuesto a revisar (puede ser borrador inicial, mark-up del LP, versión negociada)
- Contraparte (LP que envía el mark-up, o asesor del LP)
- Fase: pre-cierre / mark-up final / restatement

## Paso 2 — Comparar contra template casa

Cláusulas principales a revisar (lista no exhaustiva):

### Economics
- Management fee: %, base (committed vs invested), step-down post inv. period
- Carried interest: %, hurdle, catch-up, american vs european waterfall
- GP commitment: % del fondo
- Expenses: ¿qué corre a cargo del fondo vs gestora?
- Organizational expenses cap

### Gobernance
- LPAC (Limited Partner Advisory Committee): composición, frecuencia, materias bajo aprobación
- Key person clause: definición, qué ocurre si activado (investment suspension, GP removal)
- GP removal: with cause / without cause, quorum, indemnización
- Defaults LP: triggers, cure period, sanctions
- Transfer of interest: consentimiento GP, derecho de tanteo, transferencias permitidas

### Investment policy
- Investment period (típico 5 años)
- Total fund term (típico 10 años + 2 prórrogas)
- Recycling: % máx, plazo
- Reinvestment of returns
- Concentration limits: máx % por single investment, por sector, por geografía
- Follow-on reserve

### Reporting
- Frecuencia (capital accounts trimestrales, audit anual)
- Formato (ILPA template típico)
- Side letter reporting si aplica

### Tax
- ECI (Effectively Connected Income, US tax)
- UBTI
- FATCA / CRS reps
- Treaty benefits

### Otros
- Indemnification del GP
- Confidencialidad
- Notices
- Ley aplicable y jurisdicción

## Paso 3 — Análisis de desviaciones

Para cada desviación detectada vs template casa:

```markdown
### Cláusula: {Sección N — Título}

**Template casa:**
> {texto del template}

**LPA propuesto:**
> {texto del LPA}

**Diferencia:**
{Resumen de la desviación}

**Materialidad:**
- 🟢 No material — diferencia cosmética / cláusula menor
- 🟡 Materialidad media — cambio operativo o económico de impacto medio
- 🔴 Material — afecta economics, gobernanza o exposición del GP de forma significativa

**Impacto:**
- Económico: {cuantificar si aplica}
- Operacional: ...
- Gobernanza: ...
- Riesgo legal/reputacional: ...

**Posicionamiento sugerido para el GP:**
- ✅ Aceptar — razonable, no daña
- 🤝 Negociar — proponer contra-redacción {x}
- 🛑 Rechazar — fuera de banda casa; ofrecer alternativa {y}

**Negociación esperada:**
{Cómo de probable que el LP ceda, basado en LPs similares}
```

## Paso 4 — Resumen ejecutivo

```markdown
# LPA Review — {Vehículo} — {Versión} — {Fecha}

## Sumario
- Desviaciones materiales (🔴): X
- Desviaciones medias (🟡): Y
- Desviaciones menores (🟢): Z
- Veredicto global: ACEPTABLE / NEGOCIABLE / RECHAZAR

## Top 5 puntos críticos
1. {Cláusula + impacto + posicionamiento}
2. ...

## Posicionamiento por familia
- **Economics:** {posición global}
- **Governance:** {posición global}
- **Investment policy:** {posición global}
- **Reporting:** {posición global}
- **Tax:** {posición global}

## Próximos pasos
1. Discusión interna con managing partner: {qué decisiones tomar}
2. Mark-up: prioridades P1, P2, P3
3. Coordinación con asesor externo: {si caso material}
4. Comunicación al LP: tono y secuencia
```

## Paso 5 — Mark-up generado

Genera un mark-up del LPA con:
- Cambios sugeridos en cláusulas materiales
- Comentarios al margen explicando posicionamiento

## Paso 6 — Compliance regulatoria

Verifica que el LPA cumple:
- AIFMD (si gestora autorizada): contenidos mínimos folleto, gestión riesgo, valoración independiente, depositario
- SFDR: clasificación art. 6/8/9 reflejada
- Ley 22/2014: si vehículo es FCR/FCRE, requisitos específicos
- Disclosures fiscales: ECI, UBTI, FATCA

## Casos especiales

- **First-time fund**: el LP impondrá más concesiones (track record limitado del GP)
- **GP con track record fuerte**: posición más fuerte para resistir cambios
- **Continuation fund**: LPA suele ser más complejo (waterfall específico, conflicto de interés)
- **Co-invest vehicle**: LPA simplificado, foco en allocation y fees especiales
- **PE secondary**: LPA del fondo subyacente + LPA del vehículo SPV

## Cierre

> *LPA Review. Análisis comparado contra template casa. Toda decisión final requiere managing partner + posiblemente IC + asesor legal externo para cambios materiales. No constituye dictamen jurídico vinculante.*
