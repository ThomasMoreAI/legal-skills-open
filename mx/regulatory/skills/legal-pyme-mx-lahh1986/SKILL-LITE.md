---
name: legal-pyme-mx (preview)
description: |
  Versión preview pública con validadores que sí funcionan sin corpus
  (RFC, CURP, ISN por estado) y árbol de obligaciones. El corpus legal
  completo (~120 MB, 30+ archivos oficiales) es producto comercial.
---

# legal-pyme-mx — preview

> Cumplimiento legal federal para PyMEs mexicanas.
>
> **Esta versión preview SÍ funciona parcialmente** — incluye los validadores
> RFC/CURP, la matriz ISN por estado, y el árbol de decisión de obligaciones.
> Lo que requiere el corpus legal completo (RMF SAT, reglamentos PROFECO,
> LSS, NOM-035, plantillas de Aviso de Privacidad full) está disponible
> bajo Sistemia. [**Acceso completo + auditoría legal vía WhatsApp**](https://wa.me/525529477307?text=Hola%2C%20me%20interesa%20acceso%20completo%20a%20legal-pyme-mx).

---

## Qué hace este skill

Cuando tienes una PyME mexicana y necesitas saber:
- ¿Este RFC es válido? ¿Está en la lista 69-B SAT (factureras)?
- ¿Esta CURP cuadra con el algoritmo RENAPO?
- ¿Qué obligaciones legales tengo si abro este giro en este estado?
- ¿Cuánto ISN (Impuesto Sobre Nómina) pago según mi entidad?
- ¿Necesito REPSE? ¿NOM-035? ¿Aviso de Privacidad?

`legal-pyme-mx` te responde con info anclada en corpus oficial (SAT, INAI, STPS, Diputados, RENAPO).

---

## Lo que SÍ está en esta versión preview (gratis)

| Módulo | Función | Funciona sin corpus |
|---|---|---|
| **RFC validator** | Estructura (longitud, formato, dígito verificador) | ✅ Sí |
| **CURP validator** | Estructura + algoritmo RENAPO | ✅ Sí |
| **ISN por estado** | Tasa actual del Impuesto Sobre Nómina (1-3% por entidad) | ✅ Sí |
| **Árbol de obligaciones** | "Qué aplica si soy giro X con N empleados en estado Y" — tabla | ✅ Sí |
| **Lista de fuentes oficiales** | `data/catalogo_fuentes.json` con URLs y refresco recomendado | ✅ Sí |

---

## Lo que requiere la versión completa

| Módulo | Función | Por qué requiere corpus |
|---|---|---|
| **Lista 69-B checker** | Busca RFC contra 6 listas SAT vigentes | Listas oficiales actualizadas semanal |
| **Aviso de Privacidad generator** | Plantillas integral / simplificado / corto reales | LFPDPPP 2025 + Manual INAI versionados |
| **Compliance checklist e-commerce** | LFPC reforma 2025 (suscripciones, distintivo digital, contratos adhesión) | LFPC + RCAL + reglamentos |
| **Obligaciones IMSS/INFONAVIT/STPS** | Cálculo de aportaciones por NOM | LSS + LIFNVT + LFT + NOMs |
| **REPSE checker** | Si tu actividad requiere registro federal | Catálogo de servicios especializados oficial |
| **Antilavado LFPIORPI** | Si tu giro es actividad vulnerable | Catálogo + umbrales monetarios |
| **Refresco automático** | Listas SAT semanal, leyes mensual, RMF trimestral | Pipeline de descarga + parse |

---

## Ejemplo de uso (preview)

> **Tú:** "Valida este RFC: GACX950122ABC"

> **Claude Code (con preview):**
>
> ✅ **Estructura RFC válida**
> - Formato: Persona física (4 letras + 6 dígitos fecha + 3 homoclave)
> - Fecha derivada: 1995-01-22
> - Dígito verificador: válido
>
> ⚠️ **Lista 69-B no consultable en esta versión** (requiere acceso al corpus actualizado).
> Para verificar si está en lista negra de PROFECO/SAT, accede a la versión completa.

---

## Los 3 errores más caros de PyMEs (que este skill ayuda a prevenir)

1. **CFDI / RFC mal validado** — pérdida de deducibilidad, rechazos masivos de timbrado
2. **Patrón sin alta correcta IMSS/INFONAVIT** — capitales constitutivos, multas retroactivas que tumban PyMEs
3. **E-commerce sin LFPC / LFPDPPP** — quejas PROFECO, sanciones por datos personales

---

## Cómo conseguir la versión completa

→ [Escríbenos por WhatsApp](https://wa.me/525529477307?text=Hola%2C%20me%20interesa%20acceso%20completo%20a%20legal-pyme-mx).

Opciones:
1. **Bundle skill + corpus** (~120 MB, descarga única + actualización trimestral)
2. **Auditoría legal de tu PyME** — te entregamos el dossier de obligaciones aplicables y el plan de acción
3. **Plantillas listas** — Aviso de Privacidad / Términos / Contratos LFPC integrados a tu negocio

---

## Instalación (preview)

```bash
git clone https://github.com/lahh1986/sistemia-skills-mx.git
cp -r sistemia-skills-mx/skills/legal-pyme-mx ~/.claude/skills/legal-pyme-mx-preview
```

Funciona out-of-the-box para RFC validator, CURP validator, ISN lookup, y árbol de obligaciones. Las funciones que requieren corpus avisan al usuario y refieren a la versión completa.

---

## Disclaimer importante

Este skill (preview o completo) **no es asesoría legal personalizada**. Da información de cumplimiento basada en fuentes oficiales. Para litigios, juicios, demandas laborales específicas → abogado/contador. Para sanciones específicas en curso → abogado fiscal/laboral.

---

*Preview liberado bajo MIT. El corpus legal consolidado, las plantillas de cumplimiento y el pipeline de refresco son producto comercial de Sistemia.*
