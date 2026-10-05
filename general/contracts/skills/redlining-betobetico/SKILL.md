---
name: redlining-betobetico
title: Redlining contractual
description: Diff de dos versiones de un contrato — identifica cambios, los clasifica por riesgo (favorable / neutral / desfavorable al fondo), justifica con referencia al playbook. Triggers en "redlining", "redline", "diff contractual", "comparar versiones", "tracked changes".
author: betobetico
author_url: https://github.com/betobetico/claude-para-servicios-financieros/tree/main/plugins/verticales/legal-fondos/skills/redlining
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: es
---

# Redlining contractual

## Paso 0
Carga perfil del usuario y el playbook aplicable al tipo de contrato (NDA / side letter / LPA / subscription / vesting).

## Paso 1 — Inputs

- Versión 1 del contrato (la nuestra o la previa)
- Versión 2 del contrato (la nueva, normalmente devuelta por la contraparte)
- Tipo de contrato (afecta cláusulas críticas)
- Contexto (quién hizo los cambios y por qué)

## Paso 2 — Detección de cambios

Identifica todas las diferencias:

1. **Texto añadido** (en v2, no en v1)
2. **Texto eliminado** (en v1, no en v2)
3. **Texto modificado** (presente en ambas pero distinto)
4. **Estructura modificada** (cláusulas reordenadas, secciones nuevas, secciones removidas)

## Paso 3 — Clasificación por riesgo

Por cada cambio detectado:

```markdown
### Cambio {N}: {Sección, ej: Cláusula 3.2 — Confidencialidad}

**Antes (v1):**
> {Texto original}

**Después (v2):**
> {Texto modificado}

**Tipo:** Añadido / Eliminado / Modificado

**Clasificación:**
- ✅ **Favorable al fondo** — reduce obligaciones / aumenta derechos / mejora protecciones del GP
- ⚖️ **Neutral** — sin impacto material (formato, typo, clarificación menor)
- ❌ **Desfavorable al fondo** — aumenta obligaciones / reduce derechos / debilita posición

**Justificación:**
{Por qué se clasifica así, contra qué punto del playbook}

**Severidad (si desfavorable):**
- 🟢 Baja — aceptable como concesión
- 🟡 Media — negociable, intentar revertir o mitigar
- 🔴 Alta — línea roja, rechazar

**Posicionamiento sugerido:**
- ✅ Aceptar
- 🤝 Contrarredacción propuesta: {texto alternativo}
- 🛑 Rechazar y proponer mantener v1
```

## Paso 4 — Resumen consolidado

```markdown
# Redlining — {Contrato} — {Contraparte} — {Fecha}

## Estadísticas
- Total cambios detectados: N
- Favorables al fondo: A
- Neutrales: B
- Desfavorables al fondo: C (de los cuales 🔴 X, 🟡 Y, 🟢 Z)

## Tendencia global
- {Comentario sobre dirección general de los cambios: favorable, neutral o desfavorable}
- {¿La contraparte está siendo razonable o presionando?}

## Top cambios desfavorables a negociar
1. **{Sección}** — {resumen + posición}
2. ...

## Aceptables sin pelea
- {Lista de cambios menores que el GP puede aceptar para mostrar buena fe}

## Cambios favorables al fondo
- {Cosas que mejoraron — agradecérselas / aceptar sin reservas}

## Cambios neutros
- {Lista breve}
```

## Paso 5 — Mark-up para discutir

Genera versión mark-up donde:
- ✅ Cambios favorables o neutrales: mantener
- 🟢 🟡 Cambios desfavorables manageables: contrarredacción inline
- 🔴 Líneas rojas: volver al v1 con comentario explicativo

## Paso 6 — Email para enviar a la contraparte

```markdown
**Para:** {asesor del LP / GC contraparte}
**Asunto:** Comentarios — {Contrato}

Estimado/a {nombre},

Adjuntamos nuestro mark-up del {Contrato} v2 con nuestras propuestas. En resumen:

- **Aceptamos** sin cambios la mayoría de tu redacción
- **Proponemos contraredacciones** en {N} puntos donde creemos podemos llegar a un punto medio (ver inline)
- **Pedimos volver al texto original** en {M} puntos donde nuestro playbook nos limita

Estamos disponibles para llamar y discutir cualquiera de los puntos si ayuda.

Un saludo,
{firma}
```

## Paso 7 — Archivo

Guarda el análisis en:

```
legal/redlining/{año}/{tipo-contrato}-{contraparte}-{fecha}.md
```

Con: estadísticas + clasificación cambio a cambio + mark-up generado. Para tracking de negociaciones.

## Casos especiales

- **Diff muy largo (>50 cambios)**: prioriza por severidad, agrupa neutrales
- **Diff con re-estructuración** (secciones movidas): el diff "puro" puede ser ruidoso; identifica primero la re-estructuración y compara contenido equivalente
- **Diff de versión asesor externo vs versión interna**: el asesor puede haber introducido cambios bona fide que valoramos positivamente; no asumas mala fe
- **Diff en otro idioma**: si v1 ES y v2 EN, primero alinear traducciones, luego comparar

## Cierre

> *Análisis de redlining. Clasificación basada en playbook configurado. Toda decisión final requiere validación del GC. Para contratos materiales (LPA, side letters con LPs grandes), confirma con asesor legal externo antes de cerrar negociación.*
