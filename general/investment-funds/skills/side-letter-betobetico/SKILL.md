---
name: side-letter-betobetico
title: Side letter
description: Redacción de side letter desde precedentes propios, cruzando MFN activas y restricciones del LPA. Triggers en "side letter", "carta complementaria", "concesión LP", "MFN".
author: betobetico
author_url: https://github.com/betobetico/claude-para-servicios-financieros/tree/main/plugins/verticales/legal-fondos/skills/side-letter
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: investment-funds
language: es
---

# Side letter

## Paso 0
Carga perfil. **CRÍTICO**: lee también el output más reciente de `tracker-mfn` para conocer MFN activas y side letters previos.

## Paso 1 — Inputs

- LP solicitante (nombre + tipo: institucional, family office, sovereign wealth, fondo de fondos)
- Importe del commitment del LP (afecta concesiones razonables)
- Concesiones solicitadas (lista del LP)
- Vehículo al que aplica
- Fecha del cierre del fondo (si todavía no cerrado, importa para MFN)

## Paso 2 — Análisis de cada concesión

Para cada concesión solicitada:

```markdown
### Concesión: {descripción}

**Tipo:**
- [ ] Fee discount
- [ ] Co-investment rights
- [ ] Advisory board seat (LPAC)
- [ ] Reporting personalizado
- [ ] Excuse / opt-out rights
- [ ] Transfer rights
- [ ] Most Favoured Nation
- [ ] Key person clause adicional
- [ ] Tax-related (ECI, withholding, FATCA carve-outs)
- [ ] ESG-related (sector exclusions adicionales, KPI reporting)

**Verdict:**
- ✅ Estándar — concedida habitualmente por el GP
- 🟡 Negociable — concedida con condiciones, ver `side-letter-playbook`
- 🔴 No estándar — requiere aprobación específica del managing partner

**MFN check:**
- ¿Activaría MFN para LPs anteriores con MFN? Sí/No
- Si sí: lista de LPs a notificar y posible impacto
- Si la concesión es **más generosa** que side letters previos: alerta

**Encaje con LPA:**
- ¿Permitido por el LPA? Sí/No
- Cláusulas del LPA relevantes: ...

**Coste para el fondo:**
- Económico (si fee discount): impacto en management fee ingresos
- Operacional (si reporting personalizado): coste extra del back-office
- Reputacional (si excusión de sectores): mensaje a otros LPs
```

## Paso 3 — MFN sweep

Si el LP solicitante **tiene MFN**, debe poder elegir entre las concesiones de otros LPs en el futuro:

- Lista todas las side letters previos relevantes
- Identifica concesiones específicas que ahora "abren" para este LP
- Documenta para tracking

Si el LP solicitante **NO tiene MFN**, todavía hay que verificar:
- LPs con MFN anteriores: ¿alguna concesión nueva que ahora reciba este LP activaría su MFN?
- Si sí: notificar (típicamente al cierre del side letter)

## Paso 4 — Generar borrador

Estructura tipo:

```markdown
# Side Letter

**Entre:**
- {Gestora SGEIC SL}, con CIF {CIF}, domicilio en {dirección}, en su condición de gestora del fondo {Vehículo} ("Gestora")
- {LP SL / Trust / Persona Física}, con CIF/TIN {ID}, domicilio en {dirección} ("Inversor")

**Fecha:** {fecha}
**Vehículo:** {Fondo}
**Commitment:** EUR {X}

## Antecedentes
[1-2 párrafos]

## Concesiones acordadas

### 1. {Concesión 1, ej: Fee Discount}
**Definición:** ...
**Aplicación:** ...
**Duración:** ...
**Condiciones suspensivas:** ...

### 2. {Concesión 2, ej: Co-investment rights}
**Cuándo se ofrece:** ...
**Tamaño máx co-invest:** ...
**Plazo de aceptación:** ...
**Allocation entre LPs interesados:** ...

### 3. {Concesión 3, ej: Advisory board seat}
...

## Most Favoured Nation
{Si aplica, incluir cláusula MFN estándar}

## Confidencialidad
{Cláusula estándar}

## Ley aplicable y jurisdicción
{Conforme al LPA}

## Firma
- Por la Gestora: {apoderado}
- Por el Inversor: {firmante}
```

## Paso 5 — Outputs adicionales

1. **Side Letter draft** (markdown listo para conversión a Word / PDF)
2. **Resumen ejecutivo para sign-off** del managing partner (1 página: concesiones + coste + riesgo MFN)
3. **Actualización propuesta al `tracker-mfn`** (input listo)
4. **Email para el LP** con la draft adjunta
5. **Lista de comunicaciones requeridas** a LPs anteriores (si MFN se activa)

## Paso 6 — Sign-off matrix

| Tipo concesión | Quién aprueba |
|---|---|
| ✅ Estándar | GC solo |
| 🟡 Negociable | GC + Managing partner |
| 🔴 No estándar | Managing partner + IC + posiblemente asesor externo |

## Casos especiales

- **Anchor LP** (primer cierre, comprometiendo cantidades muy grandes): concesiones más generosas son aceptables, pero documenta razón
- **Side letter "post-cierre"** (LP entra en cierre adicional): MFN puede pedir que reciba concesiones de side letters previos
- **LP cotizado / regulado**: puede requerir disclosure pública de side letter (verificar con su jurisdicción)
- **LP con preocupaciones ESG**: side letter puede crear exclusiones de inversión que reduzcan universo del fondo

## Cierre

> *Borrador de side letter. Firma final requiere autorización del apoderado, aprobación del managing partner y, según política casa, revisión de asesor externo. Concesiones con impacto material económico o de gobernanza requieren aprobación adicional del IC.*
