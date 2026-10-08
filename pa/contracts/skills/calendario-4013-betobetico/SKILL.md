---
name: calendario-4013-betobetico
title: /calendario
description: 'Calendario fiscal — genera el calendario de obligaciones tributarias por tipo de entidad y obligaciones configuradas. Formularios: 430 (ITBMS), 03 (planilla retenciones ISR), 1 (declaración jurada ISR), CAIR, retención de dividendos, tasa única y otros. Muestra formulario, plazo y estado. Usar cuando el usuario diga "calendario fiscal", "¿qué declaración toca?", "plazos tributarios", "obligaciones fiscales".'
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/fiscal/skills/calendario
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: contracts
language: es
---

# /calendario

1. Cargar `~/.claude/plugins/config/claude-para-abogados/fiscal/CLAUDE.md` → tipo de entidad, régimen de ITBMS, obligaciones, régimen de zona especial.
2. Generar calendario según el período solicitado.
3. Cruzar con plazos de la DGI.
4. Marcar estado de cada obligación.

```
/fiscal:calendario --trimestre 2T-2026
```

---

## Propósito

Cumplir los plazos tributarios es una obligación de resultado. Una declaración presentada fuera de plazo genera automáticamente recargos e intereses y potenciales multas conforme al Código Fiscal. Este skill genera el calendario de obligaciones tributarias de la entidad para que nada se escape.

---

## Obligaciones por tipo de formulario

### ITBMS

| Formulario | Descripción | Periodicidad | Plazo |
|---|---|---|---|
| **430** | Declaración-liquidación del ITBMS (tarifa general 7%; especiales 10% bebidas alcohólicas y hospedaje, 15% tabaco; art. 1057-V) | Mensual | Dentro de los 15 días siguientes al cierre del mes |
| **433** | Declaración de retenciones de ITBMS de los agentes de retención (en particular entidades del sector público y demás agentes designados); el proveedor refleja la retención sufrida en el Formulario 430 | Mensual | Dentro de los 15 días siguientes al mes |

### Retenciones del ISR

| Formulario | Descripción | Periodicidad | Plazo |
|---|---|---|---|
| **03** (Planilla 03) | Informe mensual de retenciones del ISR sobre salarios | Mensual | Dentro de los primeros días del mes siguiente [verificar] |
| **Retención a no residentes** (Formulario 5) | Retención del ISR sobre pagos al exterior (servicios, regalías) gravados de fuente panameña: tarifa general (25% jurídicas / progresiva naturales) sobre el 50% de la suma remesada → retención efectiva 12,5% en el caso corporativo (art. 694 lit. e y art. 733-A) | Según pago | Al momento del pago / mes siguiente [verificar] |
| **Retención sobre dividendos** | 10% acciones nominativas (fuente panameña); 5% renta exenta, de fuente extranjera, de exportación o de Zona Libre de Colón / Panamá Pacífico / zonas francas; 20% acciones al portador; impuesto complementario 10% (art. 733) | Según distribución | [verificar] |

### Impuesto sobre la Renta (ISR)

| Formulario | Descripción | Periodicidad | Plazo |
|---|---|---|---|
| **1** | Declaración jurada de rentas de **persona natural** (las personas jurídicas usan otros formularios según actividad) | Anual | Hasta el 31 de marzo siguiente al cierre del período (art. 710); prórroga de hasta 1 mes [verificar] |
| **Estimada / CAIR** | Impuesto estimado del período siguiente; CAIR obligatorio si la renta gravable supera B/.1.500.000 — se compara la tarifa del art. 699 con el 4.67% sobre la renta gravable y se paga el mayor (art. 699) | Anual / cuotas | Junto con la declaración jurada [verificar] |

### Otros tributos habituales

| Formulario | Descripción | Periodicidad | Plazo |
|---|---|---|---|
| **Tasa única** [verificar] | Tasa única anual de sociedades anónimas y fundaciones de interés privado | Anual | Según fecha de inscripción en el Registro Público [verificar] |
| **Aviso de operación** | Impuesto anual del 2% sobre el **capital** de la empresa (mínimo B/.100, máximo B/.60.000; 0,5% con tope B/.50.000 en zonas francas/ZLC) — Ley 5 de 2007 | Anual | [verificar] |
| **Impuesto de inmuebles** | Sobre bienes inmuebles, tarifa progresiva reformada por la Ley 66 de 2017; exención del Patrimonio Familiar Tributario / Vivienda Principal hasta B/.120.000 de base imponible | Trimestral / anual | [verificar] |
| **Planilla CSS** [verificar] | Cuota obrero-patronal de la Caja de Seguro Social (incluye décimo tercer mes) | Mensual | [verificar] |

---

## Regímenes de zona especial

Si la entidad opera bajo un régimen especial, las obligaciones y exenciones varían sustancialmente:

| Régimen | Norma | Tratamiento fiscal típico |
|---|---|---|
| **SEM (Sede de Empresa Multinacional)** | Ley 41 de 2007 | ISR del 5% sobre servicios al grupo; exenciones de ITBMS en ciertos servicios al exterior |
| **Ciudad del Saber** | Decreto Ley 6 de 1998 | Exención de ISR e ITBMS sobre actividades autorizadas [verificar] |
| **Zona Libre de Colón** | Ley 8 de 2016 | Renta de reexportación (origen y destino fuera de Panamá) tratada como de fuente extranjera (no gravada); las ventas locales sí tributan |
| **Panamá Pacífico** | Ley 41 de 2004 | Incentivos de ISR, ITBMS y otros para actividades elegibles [verificar] |

**Recordatorio de territorialidad:** la renta de fuente extranjera no tributa en Panamá. Verificar siempre la fuente de la renta antes de incluir una obligación.

---

## Recargos e intereses por presentación tardía

| Concepto | Tratamiento |
|---|---|
| Recargo por presentación tardía | [verificar — porcentaje sobre el impuesto causado] |
| Intereses moratorios | [verificar — sobre el saldo insoluto] |
| Multa por no presentación / morosidad | [verificar] |

> Los porcentajes y plazos exactos deben confirmarse contra el Código Fiscal y las resoluciones vigentes de la DGI. [verificar]

---

## Formato de salida

```markdown
# Calendario fiscal — [Período]

**Entidad:** [nombre]
**Tipo:** [S.A. / S. de R.L. / persona natural / régimen de zona especial]
**Régimen ITBMS:** [contribuyente ordinario / agente de retención / no obligado]
**Fecha de generación:** [fecha]

---

## Obligaciones del período

| # | Formulario | Descripción | Plazo | Estado | Notas |
|---|---|---|---|---|---|
| 1 | 430 | ITBMS mensual | 15/07/2026 | Pendiente | |
| 2 | 03 | Planilla retenciones ISR | 15/07/2026 | Pendiente | |
| 3 | 1 | Declaración jurada ISR | 31/03/2026 | Presentado | |
| ... | ... | ... | ... | ... | ... |

---

## Próximos vencimientos (7 días)

[Lista de formularios con plazo en los próximos 7 días — si los hay]

---

## Vencidos sin presentar

[Lista de formularios cuyo plazo ha pasado y no consta presentación — si los hay]
```

---

## Legislación de referencia

- **Código Fiscal de Panamá** — ISR (arts. 699, 700, 710), ITBMS (art. 1057-V), dividendos (art. 733), retención a no residentes (arts. 694 lit. e y 733-A) y obligaciones formales
- **Decreto Ejecutivo 170 de 1993** — reglamentación del ISR [verificar]
- **Ley 8 de 2010** — reforma tributaria e ITBMS [verificar]
- **Ley 41 de 2007 (SEM), Ley 41 de 2004 (Panamá Pacífico), Decreto Ley 6 de 1998 (Ciudad del Saber), Ley 8 de 2016 (ZLC)**
- **Ley 5 de 2007** (aviso de operación) y **Ley 66 de 2017** (impuesto de inmuebles)
- Resoluciones de la DGI de aprobación de formularios (actualizadas periódicamente)
- Calendario tributario de la DGI (dgi.mef.gob.pa) [verificar]

---

## Lo que este skill NO hace

- No presenta los formularios ante la DGI — genera el calendario y marca los plazos.
- No calcula las cuotas a pagar — para eso, usar `/fiscal:revision`.
- No sustituye la consulta al calendario oficial de la DGI — se basa en él pero debe verificarse.
