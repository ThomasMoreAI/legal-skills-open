---
name: consentimiento-joselito412
title: /frontend-privacy/consentimiento — Auditoría de Consentimiento
description: Audita el flujo de consentimiento de un sistema — formularios de registro, checkboxes, granularidad por finalidad, revocación y registro de consentimiento. Produce un reporte focalizado con hallazgos de UI/UX, risk score parcial FE (0–50) y acciones concretas. Úsala cuando quieras revisar específicamente cómo tu sistema pide y gestiona el consentimiento del usuario.
author: joselito412
author_url: https://github.com/joselito412/Privacy_Compliance_Skills-UE-USA-LATAM/tree/main/skills/frontend-privacy/consentimiento
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: data-protection
language: es
---

# /frontend-privacy/consentimiento — Auditoría de Consentimiento

> ⚠️ Esta skill es una guía informativa. No constituye asesoría jurídica.

**Pilar:** Frontend | **Scope:** Consentimiento granular, revocación, registro  
**Owner:** PM de Producto + UX Designer | **Score:** 0–50 pts (pilar FE)

---

## Comportamiento general

Analiza el input para determinar cómo el sistema obtiene y gestiona el consentimiento. Si el input describe código, pantallas o flujos, extrae toda la información posible. Si es muy breve, haz hasta 3 preguntas enfocadas antes de proceder.

---

## Paso 1: Preguntas de contexto (si el input es insuficiente)

```
Para auditar tu flujo de consentimiento necesito saber:

1. ¿Cómo solicitas el consentimiento en el registro?
   (ej: checkbox único, toggles por finalidad, modal, scroll-to-accept...)

2. ¿Qué finalidades de tratamiento tienes?
   (ej: solo el servicio, más analytics, más marketing, más terceros...)

3. ¿Puede el usuario revocar su consentimiento desde la app?
   ¿Desde dónde y con cuántos clics?

4. ¿En qué países opera el sistema?
```

---

## Paso 2: Dimensiones de auditoría

Evalúa las siguientes 5 dimensiones para cada input:

### Dimensión 1: Forma del consentimiento

| Señal en el input | Estado | Penalizador |
|---|---|---|
| Checkbox pre-marcado por defecto | ❌ Inválido | +15 pts |
| Un solo "Acepto todo" para múltiples finalidades | ❌ No granular | +15 pts |
| Scroll-to-accept sin acción activa | ❌ Inválido | +15 pts |
| Checkbox vacío, el usuario lo marca activamente | ✅ Válido | 0 pts |
| Toggles separados por finalidad | ✅ Granular | 0 pts |
| Consentimiento implícito ("al usar el servicio aceptas") | ❌ Inválido (para datos no públicos) | +15 pts |

### Dimensión 2: Granularidad por finalidad

- **0 pts** — cada finalidad tiene su propio consentimiento (servicio, analytics, marketing, terceros)
- **+10 pts** — hay 2–3 finalidades mezcladas en un consentimiento
- **+15 pts** — todas las finalidades en un solo consentimiento o no se mencionan finalidades

### Dimensión 3: Revocación

| Estado | Penalizador |
|---|---|
| El usuario puede revocar desde su perfil en ≤ 2 clics | 0 pts |
| Revocación posible pero difícil de encontrar (≥ 4 clics o enterrada) | +5 pts |
| Revocación solo por email o contactando soporte | +10 pts |
| No existe mecanismo de revocación | +10 pts |

### Dimensión 4: Registro de consentimiento

| Estado | Penalizador |
|---|---|
| Se guarda: user_id, purpose, versión de política, timestamp, granted/revoked | 0 pts |
| Registro parcial (ej: solo "aceptó los términos", sin granularidad ni versión) | +5 pts |
| Sin registro de consentimiento | +10 pts |

### Dimensión 5: Consentimiento para datos sensibles (si aplica)

Si el sistema trata datos sensibles (salud, biometría, menores, religión, sexual):

| Estado | Penalizador |
|---|---|
| Consentimiento específico y destacado, separado del registro general | 0 pts |
| Consentimiento sensible mezclado con los demás | +10 pts |
| Sin consentimiento específico para datos sensibles | +15 pts |

---

## Paso 3: Cálculo del score FE

```
FE_consent_score = min(50, suma_penalizadores_activos × F_rigor)
```

**F_rigor:**
- Brasil (LGPD) o UE (GDPR): × 1.25
- Resto de LATAM (CO, MX, CL, AR, PE, EC): × 1.00

**Niveles:**
| Score FE | Nivel |
|---|---|
| 0–10 | 🟢 Consentimiento conforme |
| 11–25 | 🟡 Gaps menores — corregir antes del lanzamiento |
| 26–40 | 🔴 Consentimiento inválido — riesgo activo |
| 41–50 | 🚨 Crítico — base legal del tratamiento comprometida |

---

## Paso 4: Output

```
╔══════════════════════════════════════════════════════╗
║  🖥️  Auditoría de Consentimiento — Privacy Compliance Skills  ║
╠══════════════════════════════════════════════════════╣
║  [descripción del flujo auditado]                    ║
║  Países: [lista]   |   Ley más exigente: [ley]       ║
╠══════════════════════════════════════════════════════╣
║                                                      ║
║  Score FE Consentimiento: [XX] / 50   [emoji]        ║
║  [nivel]                                             ║
║                                                      ║
╠══════════════════════════════════════════════════════╣
║  Hallazgos:                                          ║
║  [emoji] [hallazgo #1]                    +XX pts    ║
║  [emoji] [hallazgo #2]                    +XX pts    ║
║  [emoji] [hallazgo N]                     +XX pts    ║
╠══════════════════════════════════════════════════════╣
║  Acción esta semana:                                 ║
║    → [acción #1 — específica con código/pantalla]    ║
║  Antes de lanzar:                                    ║
║    → [acción #2]                                     ║
╚══════════════════════════════════════════════════════╝
```

**Después del box:**
- Supuestos aplicados si los hay
- Si score FE ≥ 26: escalamiento a `/audit` para visión completa
- Recursos: enlace a [consent-form.md](../../../knowledge/pillar-frontend/patterns/consent-form.md) y [checklist-consentimiento.md](../../../knowledge/pillar-frontend/checklists/checklist-consentimiento.md)
- Disclaimer

---

## Paso 5: Reglas de calidad

- **Siempre** verificar si hay datos sensibles — activan penalizadores de Dimensión 5 automáticamente
- **Nunca** reportar un sistema como "conforme" solo porque tiene un checkbox — verificar granularidad
- **Siempre** que se detecte checkbox pre-marcado, marcarlo como hallazgo #1 independientemente del score total
- **Siempre** incluir un ejemplo concreto de cómo corregir el hallazgo (pseudocódigo, texto del checkbox, etc.)
- **Siempre** mencionar que este score es parcial y que `/audit` da la visión completa FE+BE

---

## Casos de prueba

### C1 — Checkbox único pre-marcado, sin revocación
**Input:** "Formulario de registro con un checkbox pre-marcado 'Acepto términos y política'. Opera en México."  
**Score esperado:** +15 (pre-marcado) + +15 (no granular) + +10 (sin revocación) × 1.00 = min(50, 40) = **40 pts 🔴**

### C2 — Toggles granulares + revocación + sin registro
**Input:** "Tres toggles en registro: servicio (obligatorio), analytics (opcional), marketing (opcional). Hay sección de privacidad en el perfil para revocar. No guardamos registro del consentimiento. Brasil."  
**Score esperado:** 0 (granular) + 0 (revocación fácil) + +10 (sin registro) × 1.25 = min(50, 12.5) = **13 pts 🟡**

### C3 — Datos de salud + consentimiento mezclado
**Input:** "App de salud. Al registrarse hay un solo checkbox 'Acepto política de privacidad' que incluye el tratamiento de diagnósticos médicos junto con el newsletter. Colombia."  
**Score esperado:** +15 (no granular) + +15 (sensible sin consentimiento específico) × 1.00 = min(50, 30) = **30 pts 🔴**

### C4 — Consentimiento conforme
**Input:** "Toggles por finalidad: servicio (pre-aceptado, no desmarcable), analytics (vacío, opcional), marketing (vacío, opcional). Revocación desde Configuración > Privacidad en 2 clics. Guardamos user_id, purpose, versión política, timestamp. Opera en Colombia."  
**Score esperado:** 0 (granular) + 0 (revocación) + 0 (registro completo) × 1.00 = **0 pts 🟢**

---

*Skill del Pilar Frontend | Ver también: [/frontend-privacy/transparencia](../transparencia/SKILL.md) | [/audit](../../audit/SKILL.md)*  
*Privacy Compliance Skills — [DISCLAIMER.md](../../../DISCLAIMER.md)*
