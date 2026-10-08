---
name: cumplimiento-betobetico
title: Propósito
description: Genera el calendario de obligaciones societarias y rastrea su estado de cumplimiento
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/societario/skills/cumplimiento
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: regulatory
language: es
---

## Propósito

Esta skill genera y mantiene el calendario de obligaciones societarias legales para una entidad mercantil panameña (S.A. o S. de R.L.). Verifica el estado de cumplimiento de cada obligación y alerta sobre plazos próximos o vencidos.

## Instrucciones

### Paso 1 — Identificar la entidad

1. Determinar el tipo de sociedad: S.A. (Sociedad Anónima) o S. de R.L. (Sociedad de Responsabilidad Limitada).
2. Recopilar datos relevantes: fecha de cierre del período fiscal, fecha de constitución, junta directiva, dignatarios y sus fechas de nombramiento.
3. Cargar configuración específica desde `~/.claude/plugins/config/claude-para-abogados/societario/CLAUDE.md`.

### Paso 2 — Generar calendario de obligaciones

Obligaciones comunes a S.A. y S. de R.L.:

1. **Tasa única anual**: B/. 300.00 anuales para sociedades (S.A., S. de R.L. y demás personas jurídicas); vencimiento hasta el 15 de julio si la entidad se inscribió en el 1.er semestre, o hasta el 15 de enero si se inscribió en el 2.º semestre (Código Fiscal, art. 318-A).
2. **Declaración jurada de renta (ISR)**: presentación ante la DGI hasta el 31 de marzo siguiente al cierre del período fiscal ordinario; cabe prórroga de un mes (hasta el 30 de abril), pero el impuesto se paga al 31 de marzo (Código Fiscal, art. 710, modificado por la Ley 6 de 2005).
3. **Mantenimiento del agente residente**: la sociedad debe contar en todo momento con agente residente (abogado o firma de abogados) (Ley 32 de 1927, art. 2, numeral 7; Ley 2 de 2011, art. 2).
4. **Libros sociales**: libro de actas y registro de acciones actualizados, admitiéndose libros físicos o registros electrónicos (Código de Comercio, art. 71, modificado por la Ley 22 de 2015).
5. **Renovación de cargos**: según duración prevista en el pacto social.
6. **Registro de acciones / cuotas de participación**: actualización tras cada traspaso.
7. **Declaración de beneficiario final**: ante el Sistema Privado y Único de Registro de Beneficiarios Finales (Ley 129 de 2020, administrado por la SSNF; Decreto Ejecutivo 13 de 2022); el agente residente es el obligado a reportar.

Obligaciones específicas según régimen:

8. **Estados financieros auditados**: cuando la entidad esté obligada conforme a su régimen o actividad [verificar].
   *(Recargo B/. 50 y multa B/. 300 por morosidad de dos periodos en la tasa única; suspensión de derechos corporativos a los 3 periodos consecutivos; disolución/cancelación registral a los 10 periodos consecutivos — Código Fiscal, art. 318-A.)*
9. **Reporte a la UAF**: si la entidad es sujeto obligado bajo la Ley 23 de 2015.
10. **Junta de accionistas ordinaria**: según lo previsto en el pacto social.

### Paso 3 — Verificar estado

Para cada obligación:

- **Cumplida**: documentación disponible que acredita el cumplimiento.
- **En plazo**: el plazo no ha vencido.
- **Próxima**: vence en los próximos 30 días.
- **Vencida**: el plazo ha expirado sin acreditar cumplimiento.

### Paso 4 — Generar informe

## Formato de salida

```markdown
## Calendario de cumplimiento societario

**Sociedad:** [denominación]
**Tipo:** [S.A. / S. de R.L.]
**Período fiscal:** [año]
**Fecha del informe:** [fecha]

### Estado general

- Obligaciones cumplidas: [n]/[total]
- Próximas (≤30 días): [n]
- Vencidas sin cumplir: [n]

### Calendario de obligaciones

| Obligación | Plazo legal | Fecha límite | Estado | Base legal | Notas |
|------------|-------------|--------------|--------|------------|-------|
| Tasa única anual | Anual (B/. 300; 15 jul o 15 ene) | [fecha] | [estado] | Código Fiscal, art. 318-A | [nota] |
| Declaración de renta (ISR) | Hasta 31 marzo | [fecha] | [estado] | Código Fiscal, art. 710 | [nota] |
| Agente residente | Continuo | [fecha] | [estado] | Ley 32 de 1927, art. 2.7 | [nota] |

### Renovación de cargos

| Cargo | Titular | Fecha nombramiento | Duración | Vencimiento | Estado |
|-------|---------|--------------------|-----------| ------------|--------|
| [cargo] | [nombre] | [fecha] | [años] | [fecha] | [estado] |

### Alertas

[Lista de obligaciones vencidas o próximas con acción recomendada]
```

## Referencias normativas

- **Ley 32 de 1927**: sociedades anónimas — junta directiva, dignatarios y agente residente (art. 2, numeral 7; agente residente obligatorio y permanente).
- **Ley 2 de 2011**: definición y régimen del agente residente.
- **Ley 25 de 1995**: fundaciones de interés privado — obligaciones de mantenimiento.
- **Código de Comercio de Panamá, art. 71 (modificado por la Ley 22 de 2015)**: libros sociales (actas y registro de acciones); admite libros físicos o registros electrónicos.
- **Código Fiscal de Panamá**: declaración de renta (ISR) hasta el 31 de marzo (art. 710, modificado por la Ley 6 de 2005) y tasa única anual de B/. 300.00 (art. 318-A).
- **Ley 129 de 2020**: Sistema Privado y Único de Registro de Beneficiarios Finales (SSNF; Decreto Ejecutivo 13 de 2022); el agente residente reporta.
- **Ley 23 de 2015**: prevención de blanqueo de capitales — debida diligencia y conocimiento del cliente y del beneficiario final por los sujetos obligados (UAF).

## Guardrails

- **NO** presenta ni tramita documentos ante el Registro Público ni la DGI.
- **NO** redacta los estados financieros ni el informe de gestión.
- **NO** verifica la corrección contable de las cuentas.
- **ESCALAR** si se detectan obligaciones vencidas que puedan acarrear sanciones (recargo B/. 50, multa B/. 300, suspensión de derechos corporativos a los 3 periodos consecutivos de morosidad y disolución/cancelación registral a los 10 periodos consecutivos por falta de pago de la tasa única anual; caducidad de cargos) (Código Fiscal, art. 318-A).
- **ESCALAR** si la sociedad debería estar obligada a auditar y no consta auditor nombrado.
- **AVISAR** si faltan datos para calcular algún plazo (ej. fecha de cierre del período fiscal).
