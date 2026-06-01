---
name: cumplimiento-societario
title: Propósito
description: Genera el calendario de obligaciones societarias y rastrea su estado de cumplimiento
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/societario/skills/cumplimiento
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: corporate
language: es
---

## Propósito

Esta skill genera y mantiene el calendario de obligaciones societarias legales para una entidad mercantil española (SL o SA). Verifica el estado de cumplimiento de cada obligación y alerta sobre plazos próximos o vencidos.

## Instrucciones

### Paso 1 — Identificar la entidad

1. Determinar el tipo de sociedad: SL (Sociedad Limitada) o SA (Sociedad Anónima).
2. Recopilar datos relevantes: fecha de cierre del ejercicio, fecha de constitución, órgano de administración, consejeros y sus fechas de nombramiento.
3. Cargar configuración específica desde `~/.claude/plugins/config/claude-para-abogados/societario/CLAUDE.md`.

### Paso 2 — Generar calendario de obligaciones

Obligaciones comunes a SL y SA:

1. **Formulación de cuentas anuales**: 3 meses desde el cierre del ejercicio (art. 253 LSC).
2. **Aprobación de cuentas anuales**: 6 meses desde el cierre (art. 164 LSC) — 30 de junio para ejercicios naturales.
3. **Depósito de cuentas en el RM**: 1 mes desde la aprobación (art. 279 LSC).
4. **Legalización de libros**: 4 meses desde el cierre del ejercicio (art. 18 C.Com).
5. **Impuesto sobre Sociedades**: 25 días naturales tras 6 meses del cierre (25 de julio).
6. **Renovación de cargos**: según duración estatutaria (máx. 6 años SL art. 221, máx. 6 años SA art. 222).
7. **Libro registro de socios/accionistas**: actualización tras cada transmisión.

Obligaciones específicas de SA:

8. **Informe de gestión**: obligatorio (art. 262 LSC).
9. **Verificación de cuentas por auditor**: si procede (art. 263 LSC).
10. **Junta general ordinaria**: obligatoria dentro de los 6 primeros meses.

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
**Tipo:** [SL/SA]
**Ejercicio:** [año]
**Fecha del informe:** [fecha]

### Estado general

- Obligaciones cumplidas: [n]/[total]
- Próximas (≤30 días): [n]
- Vencidas sin cumplir: [n]

### Calendario de obligaciones

| Obligación | Plazo legal | Fecha límite | Estado | Base legal | Notas |
|------------|-------------|--------------|--------|------------|-------|
| Formulación cuentas | 3 meses cierre | [fecha] | [estado] | Art. 253 LSC | [nota] |
| Aprobación cuentas | 6 meses cierre | [fecha] | [estado] | Art. 164 LSC | [nota] |
| Depósito cuentas RM | 1 mes aprobación | [fecha] | [estado] | Art. 279 LSC | [nota] |

### Renovación de cargos

| Cargo | Titular | Fecha nombramiento | Duración | Vencimiento | Estado |
|-------|---------|--------------------|-----------| ------------|--------|
| [cargo] | [nombre] | [fecha] | [años] | [fecha] | [estado] |

### Alertas

[Lista de obligaciones vencidas o próximas con acción recomendada]
```

## Referencias normativas

- **LSC art. 253**: Formulación de cuentas anuales.
- **LSC art. 164**: Aprobación de cuentas por la junta general.
- **LSC art. 279**: Depósito de cuentas en el Registro Mercantil.
- **LSC arts. 221-222**: Duración del cargo de administrador.
- **Código de Comercio art. 18**: Legalización de libros.
- **LSC art. 378**: Consecuencias del incumplimiento del depósito de cuentas (cierre registral).
- **RRM arts. 365-378**: Depósito de cuentas anuales.

## Guardrails

- **NO** presenta ni deposita documentos ante el Registro Mercantil ni la AEAT.
- **NO** redacta las cuentas anuales ni el informe de gestión.
- **NO** verifica la corrección contable de las cuentas.
- **ESCALAR** si se detectan obligaciones vencidas que puedan acarrear sanciones (cierre registral por falta de depósito, caducidad de cargos).
- **ESCALAR** si la sociedad debería estar obligada a auditar y no consta auditor nombrado.
- **AVISAR** si faltan datos para calcular algún plazo (ej. fecha de cierre del ejercicio).
