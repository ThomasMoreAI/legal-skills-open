---
name: calendario-betobetico
title: /calendario
description: 'Calendario fiscal — genera el calendario de obligaciones tributarias por tipo de entidad y obligaciones configuradas. Modelos: 303 (IVA), 111 (retenciones), 200 (IS), 100 (IRPF), 347, 349, 390 y otros. Muestra modelo, plazo y estado. Usar cuando el usuario diga "calendario fiscal", "¿qué modelo toca?", "plazos tributarios", "obligaciones fiscales".'
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/fiscal/skills/calendario
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: contracts
language: es
---

# /calendario

1. Cargar `~/.claude/plugins/config/claude-para-abogados/fiscal/CLAUDE.md` → tipo de entidad, régimen de IVA, obligaciones, SII.
2. Generar calendario según el período solicitado.
3. Cruzar con plazos de la AEAT.
4. Marcar estado de cada obligación.

```
/fiscal:calendario --trimestre 2T-2026
```

---

## Propósito

Cumplir los plazos tributarios es una obligación de resultado. Un modelo presentado fuera de plazo genera automáticamente recargos (art. 27 LGT) y potenciales sanciones. Este skill genera el calendario de obligaciones tributarias de la entidad para que nada se escape.

---

## Obligaciones por tipo de modelo

### IVA

| Modelo | Descripción | Periodicidad | Plazo |
|---|---|---|---|
| **303** | Autoliquidación de IVA | Trimestral (mensual si SII o gran empresa) | 1-20 del mes siguiente al trimestre (1-30 enero para 4T). Mensual: 1-30 del mes siguiente |
| **390** | Resumen anual de IVA | Anual | 1-30 de enero |
| **349** | Declaración recapitulativa de operaciones intracomunitarias | Trimestral/Mensual | 1-20 del mes siguiente al período |
| **347** | Declaración anual de operaciones con terceras personas (>3.005,06 EUR) | Anual | 1-28 de febrero |

### Retenciones e ingresos a cuenta

| Modelo | Descripción | Periodicidad | Plazo |
|---|---|---|---|
| **111** | Retenciones e ingresos a cuenta — rendimientos del trabajo y actividades profesionales | Trimestral (mensual si gran empresa) | 1-20 del mes siguiente al trimestre |
| **115** | Retenciones — rentas o rendimientos de arrendamientos de inmuebles urbanos | Trimestral/Mensual | 1-20 del mes siguiente |
| **123** | Retenciones — rendimientos del capital mobiliario | Trimestral/Mensual | 1-20 del mes siguiente |
| **190** | Resumen anual de retenciones (trabajo y profesionales) | Anual | 1-31 de enero |
| **180** | Resumen anual de retenciones (arrendamientos) | Anual | 1-31 de enero |
| **193** | Resumen anual de retenciones (capital mobiliario) | Anual | 1-31 de enero |

### Impuesto sobre Sociedades

| Modelo | Descripción | Periodicidad | Plazo |
|---|---|---|---|
| **200** | Declaración del Impuesto sobre Sociedades | Anual | 25 días naturales siguientes a los 6 meses posteriores al cierre del ejercicio (julio para ejercicio natural) |
| **202** | Pago fraccionado del IS | Trimestral (abril, octubre, diciembre) | 1-20 de abril, octubre, diciembre |

### IRPF

| Modelo | Descripción | Periodicidad | Plazo |
|---|---|---|---|
| **100** | Declaración de la renta (IRPF) | Anual | Abril-junio (campaña de renta) |
| **130/131** | Pago fraccionado IRPF (estimación directa/objetiva) | Trimestral | 1-20 del mes siguiente al trimestre |

### Otros modelos habituales

| Modelo | Descripción | Periodicidad | Plazo |
|---|---|---|---|
| **036/037** | Declaración censal | Según hechos | 1 mes desde el hecho |
| **840** | IAE | Anual (si aplica) | Según ayuntamiento |
| **720** | Declaración de bienes y derechos en el extranjero | Anual | 1 de enero - 31 de marzo |

---

## SII (Suministro Inmediato de Información)

Si la entidad está acogida al SII (obligatorio para grandes empresas, grupos de IVA, inscritos en REDEME):

| Obligación SII | Plazo |
|---|---|
| Facturas emitidas | 4 días hábiles desde expedición (8 días si factura por destinatario) |
| Facturas recibidas | 4 días hábiles desde registro contable |
| Bienes de inversión | Último período de liquidación del año |
| Operaciones intracomunitarias | 4 días hábiles |

**Si SII → los modelos 303 son mensuales y no se presenta el 390.**

---

## Recargos por presentación extemporánea (art. 27 LGT)

| Retraso | Recargo | Intereses |
|---|---|---|
| Hasta 1 mes | 1% | No |
| 1-2 meses | 2% | No |
| 2-3 meses | 3% | No |
| ... | +1% por cada mes adicional | No |
| Más de 12 meses | 15% | Sí (intereses de demora) |

---

## Formato de salida

```markdown
# Calendario fiscal — [Período]

**Entidad:** [nombre]
**Tipo:** [sociedad / autónomo / grupo fiscal]
**Régimen IVA:** [general / SII / recargo de equivalencia]
**Fecha de generación:** [fecha]

---

## Obligaciones del período

| # | Modelo | Descripción | Plazo | Estado | Notas |
|---|---|---|---|---|---|
| 1 | 303 | IVA trimestral 2T | 20/07/2026 | Pendiente | |
| 2 | 111 | Retenciones 2T | 20/07/2026 | Pendiente | |
| 3 | 202 | Pago fraccionado IS | 20/10/2026 | Futuro | |
| ... | ... | ... | ... | ... | ... |

---

## Próximos vencimientos (7 días)

[Lista de modelos con plazo en los próximos 7 días — si los hay]

---

## Vencidos sin presentar

[Lista de modelos cuyo plazo ha pasado y no consta presentación — si los hay]
```

---

## Legislación de referencia

- LGT (Ley 58/2003) — arts. 27 (recargos), 29 (obligaciones formales)
- LIVA (Ley 37/1992) — régimen de IVA
- LIS (Ley 27/2014) — Impuesto sobre Sociedades
- LIRPF (Ley 35/2006) — IRPF
- RD 1065/2007 — obligaciones de información
- Órdenes ministeriales de aprobación de modelos (actualizadas anualmente)
- Calendario del contribuyente de la AEAT (sede.agenciatributaria.gob.es)

---

## Lo que este skill NO hace

- No presenta los modelos ante la AEAT — genera el calendario y marca los plazos.
- No calcula las cuotas a ingresar — para eso, usar `/fiscal:revision`.
- No sustituye la consulta al calendario oficial de la AEAT — se basa en él pero debe verificarse.
