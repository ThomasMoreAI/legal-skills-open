---
name: nda-betobetico
title: Triaje y redacción de NDA
description: Triaje VERDE/AMARILLO/ROJO de NDA recibido + redacción de contra-borrador si encaja con plantilla casa. Adaptado al playbook del GP (líneas rojas vs negociables). Triggers en "NDA", "non-disclosure", "acuerdo confidencialidad", "triaje NDA", "revisar NDA".
author: betobetico
author_url: https://github.com/betobetico/claude-para-servicios-financieros/tree/main/plugins/verticales/legal-fondos/skills/nda
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: contracts
language: es
---

# Triaje y redacción de NDA

## Paso 0 — Cargar perfil
Lee `~/.claude/plugins/config/servicios-financieros/legal-fondos/CLAUDE.md`. Extrae **playbook NDA**: líneas rojas, bandas negociables, plantilla casa.

Si no existe playbook → pide `/legal-fondos:entrevista-inicial` modo completo (sección NDA).

## Paso 1 — Contexto del NDA

Pregunta o usa de la sesión:

- ¿Es NDA **enviado por nosotros** o **recibido de contraparte**?
- ¿Mutual o unilateral? ¿En qué dirección?
- ¿Contexto?
  - DD a una potencial inversión (típico VC/PE)
  - Comercial / partnership
  - Empleado / consultor
  - Talking with a competitor
  - Otros
- ¿Quién es la contraparte? (sector, tamaño, geografía)
- ¿Hay timing crítico?

## Paso 2 — Análisis cláusula por cláusula

Para cada cláusula relevante:

| Cláusula | Valor en el NDA | Valor en playbook | Veredicto |
|---|---|---|---|
| Definición Información Confidencial | ... | ... | ✅ / 🟡 / 🔴 |
| Duración obligación confidencialidad | X años | máx Y años | ... |
| Periodo de retención | X años | Y años | ... |
| Excepciones (info públicas, ya conocida, etc.) | Lista | Lista standard | ... |
| Devolución / destrucción | Tipo | Tipo aceptado | ... |
| Jurisdicción | ... | ES / Lux / UK | ... |
| Ley aplicable | ... | ... | ... |
| **Standstill** (cláusula no-acercamiento) | Sí/No, duración | Aceptable? | ... |
| **Non-circumvention** | Sí/No | Aceptable? | ... |
| **Non-solicit empleados** | Sí/No, duración | Aceptable? | ... |
| **Penalty / liquidated damages** | Sí/No, importe | Aceptable? | ... |
| Cesibilidad | ... | ... | ... |
| Firma electrónica admitida | Sí/No | ... | ... |

## Paso 3 — Triaje

Asigna verdict global:

### 🟢 VERDE — Firmar directo
- Todas las cláusulas dentro de bandas aceptables del playbook
- Sin líneas rojas
- Acción: aprobar para firma del apoderado

### 🟡 AMARILLO — Negociar puntos concretos
- 1-3 cláusulas fuera de banda pero negociables
- Sin líneas rojas
- Acción: generar contra-borrador con cambios concretos + email de envío

### 🔴 ROJO — Escalar
- Líneas rojas presentes
- Cláusulas exóticas / no estándar
- Penalty clauses con cifras materiales
- Standstill largo o sin compensación
- Acción: escalar a GC + posiblemente asesor externo. NO firmar.

## Paso 4 — Generar output

### Si VERDE
```markdown
# NDA — {Contraparte} — {Fecha} — 🟢 VERDE

## Veredicto
Firma directa autorizada por GC. Sin desviaciones del playbook.

## Resumen
- Mutual / unilateral
- Duración: X años
- Jurisdicción: ES
- Sin standstill / non-solicit problemáticos

## Acción
Reenviar al apoderado para firma vía {DocuSign / etc.}.

## Archivo
Guardar en `legal/ndas/{año}/{contraparte}-{fecha}.pdf` tras firma.
```

### Si AMARILLO
```markdown
# NDA — {Contraparte} — {Fecha} — 🟡 AMARILLO

## Veredicto
Negociar antes de firmar. {N} cláusulas requieren ajuste.

## Cambios solicitados
1. **Cláusula X (duración):** "5 años" → "3 años máx"
   - Justificación: política casa
2. **Cláusula Y (standstill):** "Standstill 12 meses sin excepciones" → "6 meses con excepción de fund-of-funds y processos de venta competitivos"
   - Justificación: limitación operativa

## Contra-borrador
{Genera versión redlined del NDA — texto del NDA con cambios marcados}

## Email para contraparte
{Genera email cortés explicando los cambios}

## Próximo paso
Tras acuerdo, firmar vía {DocuSign}.
```

### Si ROJO
```markdown
# NDA — {Contraparte} — {Fecha} — 🔴 ROJO

## Veredicto
**No firmar.** Escalación obligatoria.

## Líneas rojas detectadas
1. {Cláusula X — descripción del problema}
2. ...

## Riesgos
- Reputacional: ...
- Operacional: ...
- Legal: ...

## Acción
1. Notificar al GC: {nombre}
2. Si caso material, contratar asesor externo: {firma habitual}
3. Comunicar a la contraparte que necesitamos revisar internamente — sin compromiso de firmar
4. Si la contraparte presiona, escalar al managing partner antes de cualquier decisión

## Borrador de email para ganar tiempo
{Email cortés que pide tiempo sin comprometer}
```

## Paso 5 — Archivo

Independientemente del veredicto, guarda el análisis en:

```
legal/ndas-triaje/{año}/{contraparte}-{fecha}-{verdict}.md
```

Para futura reutilización (si la misma contraparte vuelve, partir del análisis previo).

## Paso 6 — Si vamos a enviar el NDA nosotros

Genera versión casa del NDA:
- Plantilla del playbook
- Datos rellenados (nuestra entidad, contraparte, contexto, fecha, duración)
- Listo para enviar por DocuSign

## Casos especiales

- **NDA con cotizada / gestora cotizada**: aplicar MAR — el NDA debe incluir cláusulas sobre información privilegiada y prohibiciones de trading
- **NDA tripartito o multilateral**: análisis más complejo, pasos adicionales
- **NDA con jurisdicción exótica** (offshore, paraísos): líneas rojas adicionales
- **NDA con cláusula de IP**: puede ir más allá de confidencialidad (asignación de IP); separar análisis

## Cierre

> *Triaje NDA. Veredicto orientativo basado en playbook configurado. Toda firma final requiere apoderado autorizado. Cualquier caso 🔴 requiere validación del GC y posiblemente asesor externo. No constituye dictamen jurídico vinculante.*
