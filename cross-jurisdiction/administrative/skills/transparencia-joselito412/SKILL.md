---
name: transparencia-joselito412
title: /frontend-privacy/transparencia — Auditoría de Transparencia
description: Audita la transparencia de un sistema hacia sus usuarios — política de privacidad, aviso de cookies, datos de contacto del responsable, transferencias internacionales mencionadas y gestión de cambios en la política. Produce un reporte focalizado con risk score parcial FE (0–40 pts) y acciones concretas. Úsala cuando quieras verificar si tu política de privacidad cumple con los requisitos de cada jurisdicción.
author: joselito412
author_url: https://github.com/joselito412/Privacy_Compliance_Skills-UE-USA-LATAM/tree/main/skills/frontend-privacy/transparencia
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: administrative
language: es
---

# /frontend-privacy/transparencia — Auditoría de Transparencia

> ⚠️ Esta skill es una guía informativa. No constituye asesoría jurídica.

**Pilar:** Frontend | **Scope:** Política de privacidad, cookies, avisos, datos de contacto del responsable  
**Owner:** PM de Producto + UX Designer | **Score:** 0–40 pts (pilar FE)

---

## Comportamiento general

Analiza la política de privacidad, el aviso de cookies y los elementos de transparencia de la UI descritos en el input. Si se proporciona una URL, analiza la descripción. Si el input menciona un sistema sin detalles de transparencia, infiere que no existe política y aplica penalizadores.

---

## Paso 1: Preguntas de contexto (si el input es insuficiente)

```
Para auditar tu transparencia necesito saber:

1. ¿Tienes política de privacidad publicada? ¿Desde dónde se accede?
   (footer, onboarding, formularios...)

2. ¿Tienes aviso de cookies? ¿Permite rechazar cookies no necesarias?

3. ¿En qué países opera el sistema?

4. ¿Mencionas en la política los terceros que reciben datos
   (analytics, CRM, pagos) y en qué países están sus servidores?
```

---

## Paso 2: Dimensiones de auditoría

### Dimensión 1: Existencia y accesibilidad de la política

| Estado | Penalizador |
|---|---|
| Política publicada, accesible desde footer en toda la app, con fecha de actualización | 0 pts |
| Política existe pero no está en el footer o requiere ≥ 3 clics | +5 pts |
| Política existe pero está desactualizada (> 12 meses sin cambios con actividad en el sistema) | +5 pts |
| Sin política de privacidad | +10 pts |

### Dimensión 2: Contenido mínimo de la política

Evaluar si la política cubre estos elementos. Cada ausencia suma:

| Elemento | Penalizador si falta |
|---|---|
| Identidad y contacto del responsable del tratamiento | +5 pts |
| Finalidades del tratamiento | +5 pts |
| Base legal de cada finalidad | +5 pts (solo si F_rigor = 1.25) |
| Lista de terceros que reciben datos | +5 pts |
| Período de retención de datos | +5 pts |
| Derechos del usuario y cómo ejercerlos | +5 pts |
| Transferencias internacionales (países y mecanismo) | +5 pts (solo si hay transferencias) |

**Cap:** máximo +15 pts de esta dimensión independientemente del número de ausencias.

### Dimensión 3: Aviso de cookies (si el sistema usa cookies de terceros)

| Estado | Penalizador |
|---|---|
| Banner granular (categorías: necesarias/analytics/marketing), con "Rechazar" igual de visible | 0 pts |
| Banner con solo "Aceptar todo" sin opción de rechazar | +10 pts |
| Sin banner de cookies pero usa cookies de analytics/marketing | +10 pts |
| Scripts de terceros cargan antes del consentimiento | +5 pts adicionales |

Si el sistema solo usa cookies propias técnicas (sesión, CSRF): 0 pts en esta dimensión.

### Dimensión 4: Datos de contacto del responsable y DPO

| Estado | Penalizador |
|---|---|
| Email de privacidad visible en política y/o footer | 0 pts |
| Solo formulario genérico de contacto (no canal específico de privacidad) | +5 pts |
| Sin datos de contacto del responsable | +5 pts |
| DPO/Encarregado requerido (F_rigor=1.25) pero no designado/publicado | +5 pts adicionales |

---

## Paso 3: Cálculo del score FE

```
FE_transparency_score = min(40, suma_penalizadores_activos × F_rigor)
```

**F_rigor:**
- Brasil (LGPD) o UE (GDPR): × 1.25
- Resto de LATAM: × 1.00

**Niveles:**
| Score FE | Nivel |
|---|---|
| 0–8 | 🟢 Transparencia adecuada |
| 9–20 | 🟡 Gaps de transparencia — corregir antes del lanzamiento |
| 21–35 | 🔴 Incumplimiento activo de transparencia |
| 36–40 | 🚨 Crítico — sin política en mercados regulados |

---

## Paso 4: Output

```
╔══════════════════════════════════════════════════════╗
║  🖥️  Auditoría de Transparencia — Privacy Compliance Skills   ║
╠══════════════════════════════════════════════════════╣
║  [descripción del sistema / política auditada]       ║
║  Países: [lista]   |   Ley más exigente: [ley]       ║
╠══════════════════════════════════════════════════════╣
║                                                      ║
║  Score FE Transparencia: [XX] / 40   [emoji]         ║
║  [nivel]                                             ║
║                                                      ║
╠══════════════════════════════════════════════════════╣
║  Hallazgos:                                          ║
║  [emoji] [hallazgo #1]                    +XX pts    ║
║  [emoji] [hallazgo #2]                    +XX pts    ║
╠══════════════════════════════════════════════════════╣
║  Acción esta semana:                                 ║
║    → [acción #1 específica]                          ║
║  Antes de lanzar:                                    ║
║    → [acción #2]                                     ║
╚══════════════════════════════════════════════════════╝
```

**Después del box:**
- Supuestos aplicados si los hay
- Si score FE ≥ 21: escalamiento a `/audit` para visión completa
- Recursos: enlace a [checklist-transparencia-ui.md](../../../knowledge/pillar-frontend/checklists/checklist-transparencia-ui.md) y [privacy-policy-widget.md](../../../knowledge/pillar-frontend/patterns/privacy-policy-widget.md)
- Si hay cookies de terceros: enlace a [cookies-avisos.md](../../../knowledge/pillar-frontend/matrices/cookies-avisos.md)
- Disclaimer

---

## Paso 5: Reglas de calidad

- **Siempre** verificar si hay transferencias internacionales — si existen y no están mencionadas en la política, es hallazgo crítico
- **Nunca** reportar como conforme un sistema sin política publicada aunque tenga otros controles
- **Siempre** distinguir entre "política existente con gaps" y "sin política" — son severidades distintas
- **Siempre** si el sistema usa Google Analytics, Meta Pixel o Hotjar sin aviso de cookies, marcarlo explícitamente
- **Siempre** mencionar que este score es parcial y que `/audit` da visión completa FE+BE

---

## Casos de prueba

### T1 — Sin política, sistema con analytics
**Input:** "App web con plataforma de analytics web (tipo A) y píxel de red social (tipo B). Sin política de privacidad publicada. Opera en Colombia y Brasil."  
**Score esperado:** +10 (sin política) + +10 (sin banner de privacidad) + +5 (trackers activos antes del consentimiento asumido) × 1.25 (Brasil) = min(40, 31.25) = **31 pts 🔴**

### T2 — Política existente con gaps de contenido
**Input:** "Política de privacidad en el footer. No menciona terceros ni períodos de retención. Sin datos de contacto del responsable. Opera en México."  
**Score esperado:** 0 (política existe) + +5 (sin terceros) + +5 (sin retención) + +5 (sin contacto) × 1.00 = min(40, 15) = **15 pts 🟡**

### T3 — Transparencia conforme (GDPR)
**Input:** "Política en footer con índice, fecha actualización, base legal por finalidad, lista de terceros con países, DPO designado con email. Banner de cookies granular con Aceptar/Rechazar igual de visible. Herramienta de analytics solo carga tras consentimiento. Opera en España (GDPR)."  
**Score esperado:** 0 en todas las dimensiones × 1.25 = **0 pts 🟢**

### T4 — Cookies no conformes (UE)
**Input:** "Política completa publicada. Banner de privacidad pero solo tiene botón 'Aceptar todo', sin opción de rechazar. Los trackers de analytics se cargan inmediatamente al entrar al sitio. Usuarios en Alemania."  
**Score esperado:** 0 (política OK) + +10 (banner sin rechazo) + +5 (trackers antes del consentimiento) × 1.25 = min(40, 18.75) = **19 pts 🟡**

---

*Skill del Pilar Frontend | Ver también: [/frontend-privacy/consentimiento](../consentimiento/SKILL.md) | [/audit](../../audit/SKILL.md)*  
*Privacy Compliance Skills — [DISCLAIMER.md](../../../DISCLAIMER.md)*
