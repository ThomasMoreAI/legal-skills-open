---
name: kyc-reglas-betobetico
title: Evaluación KYC contra reglas PBC/FT
description: Evalúa caso KYC contra rules-grid PBC/FT — sanciones, PEP, jurisdicción de riesgo, fuente de fondos. Decisión preliminar + escalación. Triggers en "kyc reglas", "rules grid", "evaluar kyc", "aml screening", "decisión onboarding".
author: betobetico
author_url: https://github.com/betobetico/claude-para-servicios-financieros/tree/main/plugins/verticales/operaciones/skills/kyc-reglas
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: white-collar
language: es
---

# Evaluación KYC contra reglas PBC/FT

## Paso 0
Carga perfil. Requiere JSON del cliente (típicamente generado por `kyc-parser`).

## Paso 1 — Screening contra listas

Listas obligatorias a chequear:

| Lista | Fuente | Frecuencia update |
|---|---|---|
| OFAC SDN | US Treasury | Diaria |
| UE Consolidated | Comisión Europea | Diaria |
| ONU | Comité de Sanciones ONU | Diaria |
| SEPBLAC | Tesoro España | Diaria |
| PEPs comerciales | World-Check / ComplyAdvantage | Continua |
| GAFI High-Risk | GAFI / FATF | Trimestral |

Para cada persona física y UBO del caso:

```json
{
  "nombre": "...",
  "matches": [
    {
      "lista": "OFAC SDN",
      "score": 95,
      "match_name": "...",
      "review": "match exacto - investigar"
    }
  ]
}
```

**Match > 85**: requiere revisión humana antes de continuar.
**Match exacto**: bloqueo automático y notificación MLRO.

## Paso 2 — PEP evaluation

Si la persona es PEP:

| Tipo PEP | Tratamiento |
|---|---|
| **Doméstico** (España) | Diligencia reforzada |
| **Internacional** | Diligencia reforzada + aprobación alta dirección |
| **Familiar/allegado de PEP** | Diligencia reforzada |
| **Ex-PEP (desempeñado en últimos 12 meses)** | Reforzada por 12 meses adicionales |

Documentar:
- Cargo desempeñado o desempeñado en pasado
- Periodo
- País
- Familiares relevantes
- Origen del patrimonio

## Paso 3 — Jurisdicción

Cruzar con lista GAFI / FATF de jurisdicciones de:
- **High-risk jurisdictions** (Black list): operativa muy restringida o prohibida
- **Jurisdicciones bajo monitoreo aumentado** (Grey list): diligencia reforzada

Verificar:
- País de nacionalidad
- País de residencia fiscal
- País de domicilio social (si jurídica)
- País de operaciones principales
- País de origen de fondos

## Paso 4 — Fuente de fondos / patrimonio

Evaluar coherencia:
- Origen declarado por el cliente
- Soportes documentales (cuentas, ventas, herencias, etc.)
- Coherencia con perfil profesional / nivel de ingresos
- ¿Origen legítimo demostrable?

Banderas rojas:
- Origen "no documentable" en cliente HNW
- Estructuras opacas (cascadas de shell companies, jurisdicciones de secreto)
- Patrimonio incoherente con vida profesional declarada
- Fondos de venta de activos en jurisdicciones high-risk

## Paso 5 — Decision matrix

```markdown
## Evaluación final

| Criterio | Resultado | Riesgo |
|---|---|---|
| Sanciones screening | Sin match / Match X / Match exacto | Bajo/Medio/Alto |
| PEP | No / Sí - {tipo} | Bajo/Medio/Alto |
| Jurisdicción | OK / Grey / Black | Bajo/Medio/Alto |
| Fuente de fondos | Coherente / Parcial / No demostrable | Bajo/Medio/Alto |
| Estructura societaria | Transparente / Compleja / Opaca | Bajo/Medio/Alto |
| Productos contratados | Estándar / Reforzada | Bajo/Medio/Alto |

**Riesgo global: Bajo / Medio / Alto / Inaceptable**
```

## Paso 6 — Recomendación

| Riesgo | Acción |
|---|---|
| **Bajo** | Onboardeo estándar — diligencia normal |
| **Medio** | Onboardeo con diligencia reforzada — escalación a Compliance Officer |
| **Alto** | Onboardeo solo con aprobación expresa Comité de Aceptación + MLRO |
| **Inaceptable** | Rechazo de onboardeo — comunicar al cliente, no operar |

Documentación obligatoria en cada caso.

## Paso 7 — Si rechazo: notificación SEPBLAC

Si durante el screening aparecen indicios fundados de blanqueo:
- **Comunicación obligatoria a SEPBLAC** (Form S)
- Plazo: sin demora indebida
- Confidencialidad: prohibido informar al cliente
- MLRO firma la comunicación

## Output

```markdown
# Evaluación KYC — Cliente {ID}

## Datos resumidos
{Bloque resumen}

## Screening
{Resultados}

## Evaluación de riesgo
{Tabla}

## **Recomendación: {Bajo/Medio/Alto/Inaceptable}**

## Acciones requeridas
1. {Acción 1 — owner — deadline}

## Próxima revisión periódica
{Fecha — típicamente anual para Bajo, semestral para Medio, trimestral para Alto}
```

## Casos especiales
- **VASPs / cripto**: aplicar MiCA + medidas adicionales sobre origen de criptoactivos
- **Clientes corporativos en sectores high-risk** (apuestas, joyería, inmobiliario): diligencia reforzada por defecto
- **Trusts y fundaciones**: identificar settlor, trustees y beneficiarios; transparencia obligatoria
- **Onboarding remoto / video-ID**: añade riesgo de fraude — verificación reforzada (eIDAS Qualified, etc.)

## Cierre
> *Evaluación bajo Ley 10/2010 PBC/FT y normativa AML UE. Decisión final del onboarding es del Comité de Aceptación / MLRO. No constituye dictamen legal — el caso debe documentarse íntegramente para auditoría e inspección SEPBLAC.*
