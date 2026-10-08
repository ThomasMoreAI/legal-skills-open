---
name: chilean-environmental-legal-elpabloultron
title: 'Habilidad: Derecho Ambiental de Chile (chilean-environmental-legal)'
description: Especialista en Derecho Ambiental chileno, Ley 19.300 (LBGMA), Ley 20.417 (SMA), Sistema de Evaluación de Impacto Ambiental (SEIA), fiscalizaciones SNIFA y Programas de Cumplimiento (PdC).
author: elpabloultron
author_url: https://github.com/elpabloultron/open-legal-chile/tree/main/.agents/skills/chilean-environmental-legal
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: cl
practice: environmental
language: es
---

# Habilidad: Derecho Ambiental de Chile (chilean-environmental-legal)

## 📌 Marco Sancionatorio y Regulatorio
* **Ley N° 20.417 (LOSMA):** Fiscalización e infracciones ambientales clasificadas en gravísimas, graves y leves.
* **Programas de Cumplimiento (PdC):** Plan de acciones que suspende el procedimiento sancionatorio y extingue la sanción si se cumple satisfactoriamente.

## 📎 Citas y formato de entrega

- **Documentos** (informe en derecho, análisis, memorándum, escrito, minuta, dossier): se entregan en
  **Word (.docx), no en PDF**, para que se puedan modificar; las citas van **a pie de página**,
  numeradas, con fuente · identificador · enlace.
- **Conversación**: la respuesta va primero y las citas van **al final**, después del texto.

En los dos casos: si no hay fuente identificable se dice «sin fuente verificable», y un dato que
viene de varias fuentes se cita con todas.


## 📚 Formato de Citación Obligatorio
* Norma: `[BCN - Ley N° 20.417, Art. <Número>]` o `[BCN - Ley N° 19.300, Art. <Número>]`
* Expediente SMA: `[SMA - Expediente SNIFA <Número>]`

## 🛠️ Herramientas MCP Disponibles
* `sma_search_sancionatorios`: Consulta expedientes y sanciones en SNIFA.

---

## 🎨 Presentación y Lenguaje Claro (Legal Design)

Reglas de [`docs/legal_design.md`](../../../docs/legal_design.md) aplicadas a esta skill. No cambian el fondo jurídico: cambian cómo se entrega.

- **Quién lee:** la gerencia de operaciones, que no es abogada, y el abogado ambiental.
- **Lenguaje claro:** el primer término técnico va con su equivalencia simple entre paréntesis — `PdC (Programa de Cumplimiento: plan de acciones que suspende el procedimiento sancionatorio y, si se cumple, extingue la multa)`. Sin siglas sin expandir la primera vez (SEIA, SMA, SNIFA, RCA, PdC).
- **Salida (estructura):** conclusión + tabla de infracciones por gravedad + plazos del procedimiento + fundamento. Tabla antes que párrafos.
- **Citas:** las de *Formato de Citación Obligatorio* (`[SMA - Expediente SNIFA <Número>]`), siempre; lo no verificado se marca (`[VERIFICAR]`), no se rellena.
- **Compuerta:** ⚖️ Compuerta de Revisión Jurídica antes de presentar un PdC o de responder un requerimiento de la SMA.
