---
name: chilean-administrative-legal-elpabloultron
title: 'Habilidad: Derecho Administrativo y Control Público (chilean-administrative-legal)'
description: Especialista en Derecho Administrativo chileno, dictámenes e informes de auditoría de la Contraloría General de la República (CGR), sumarios, probidad, Ley de Compras Públicas (Ley 19.886 / 21.634), vigilancia regulatoria (Diario Oficial, CMF, SII, DT, SMA) y análisis de brechas normativas.
author: elpabloultron
author_url: https://github.com/elpabloultron/open-legal-chile/tree/main/.agents/skills/chilean-administrative-legal
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: cl
practice: administrative
language: es
---

# Habilidad: Derecho Administrativo y Control Público (chilean-administrative-legal)

## 📌 Principios Fundamentales
* **Principio de Legalidad y Juridicidad:** Artículos 6 y 7 de la Constitución Política de la República.
* **Fuerza Vinculante de la CGR:** Los dictámenes de la Contraloría fijan el sentido y alcance de las leyes para toda la Administración del Estado.
* **Doctrina de Confianza Legítima:** Criterio de la CGR y de la Corte Suprema respecto a la renovación de contratas sucesivas.
* **Vigencia de la norma:** la ley obliga desde su publicación en el Diario Oficial y la norma no rige retroactividad (Arts. 6, 7 y 9 Código Civil).

## 📎 Citas y formato de entrega

- **Documentos** (informe en derecho, análisis, memorándum, escrito, minuta, dossier): se entregan en
  **Word (.docx), no en PDF**, para que se puedan modificar; las citas van **a pie de página**,
  numeradas, con fuente · identificador · enlace.
- **Conversación**: la respuesta va primero y las citas van **al final**, después del texto.

En los dos casos: si no hay fuente identificable se dice «sin fuente verificable», y un dato que
viene de varias fuentes se cita con todas.


## 📚 Formato de Citación Obligatorio
* Dictamen CGR: `[Dictamen CGR N° <DocID> (<Año>)]`
* Informe Auditoría: `[CGR - Informe Final N° <Número>/<Año>]`
* Normativa sectorial: `[NCG CMF N° <Número>]`, `[Circular SII N° <Número> (<Año>)]`, `[Dictamen DT N° <Número>/<Año>]`
* Ley: `[BCN - Ley N° <Número>, Art. <Número>]`

## 🛠️ Herramientas MCP Disponibles
* `cgr_search_jurisprudencia`: Busca dictámenes en jurisprudencia administrativa de la CGR.
* `cgr_search_auditorias`: Busca en los 9.600+ informes de auditoría de la CGR.
* `cmf_search_normativa`: NCG y circulares de la CMF.
* `sii_search_circulares`: Circulares del Director del SII (2020-2026).
* `dt_search_doctrina`: Doctrina laboral vinculante DT.
* `sma_search_sancionatorios`: Procedimientos sancionatorios ambientales SNIFA.
* `bcn_get_ley`: Texto oficial de leyes (19.886, 21.634, 19.880, etc.).

---

## 🎨 Presentación y Lenguaje Claro (Legal Design)

Reglas de [`docs/legal_design.md`](../../../docs/legal_design.md) aplicadas a esta skill. No cambian el fondo jurídico: cambian cómo se entrega.

- **Quién lee:** el abogado del servicio y la jefatura de servicio, que no es abogada.
- **Lenguaje claro:** el primer término técnico de cada documento va con su equivalencia simple entre paréntesis — `toma de razón (la Contraloría revisa el decreto antes de que empiece a regir)`. Sin siglas sin expandir la primera vez (CGR, NCG, SII, SNIFA).
- **Salida (estructura):** conclusión + tabla de hallazgos por requisito + detalle + pie de verificación de fuentes. Tabla o lista antes que párrafos.
- **Citas:** las de *Formato de Citación Obligatorio*, siempre; lo no verificado se marca (`[ESTADO DE VIGENCIA NO VERIFICADO]`), no se rellena.
- **Compuerta:** ⚖️ Compuerta de Revisión Jurídica antes de responder a un órgano fiscalizador o de fijar una posición institucional.

---

## 🛰️ Workflow 1: Vigilancia Regulatoria (importado de `reg-feed-watcher`, chilenizado)

**Propósito:** Revisar las fuentes regulatorias chilenas, filtrar por umbral de materialidad y reportar lo nuevo desde la última revisión. (Puede ejecutarse como agente programado.)

### Pasos
1. **Verificación de cobertura** contra el catálogo de fuentes:
   - **Diario Oficial** (toma de razón CGR, decretos y leyes).
   - **CGR:** dictámenes e instructivos (`cgr_search_jurisprudencia`).
   - **CMF:** NCG y circulares (`cmf_search_normativa`).
   - **SII:** circulares del Director (`sii_search_circulares`).
   - **DT:** dictámenes y ordinarios (`dt_search_doctrina`).
   - **SMA:** resoluciones sancionatorias y PdC (`sma_search_sancionatorios`).
2. **Pull:** consultar cada fuente con las herramientas MCP; de-duplicar por identificador oficial.
3. **Clasificar por materialidad:** Siempre material / Revisar / Informativo; marcar consultas públicas con plazo de comentarios (las "NPRM" no existen en Chile; el equivalente son **consultas públicas de reglamentos** y proyectos de ley en tramitación BCN).
4. **Enriquecer:** resumen, gancho de relevancia, enlace oficial y fechas.
5. **Salida:** digest en chat + archivo (agregar si es el mismo día).

### Compuertas
- **Sin silencio suplementario:** citas con su fuente (`[NCG CMF N° X]`, `[Dictamen CGR N° X (AAAA)]`).
- Pie de página de verificación de citas; nunca afirmar vigencia sin verificar fecha de publicación.

---

## 🔀 Workflow 2: Análisis de Brecha Normativa (importado de `policy-diff`, chilenizado)

**Propósito:** Comparar un cambio regulatorio específico contra la biblioteca de políticas/contratos de la organización; produce un análisis de brechas requisito-por-requisito.

### Pasos
1. **Verificar vigencia de la norma:** publicación en el Diario Oficial, regla de vigencia inmediata (Art. 7 CC) o vacancia expresa; verificar toma de razón CGR cuando aplique. Si no se verifica → banner `[ESTADO DE VIGENCIA NO VERIFICADO]`.
2. **Extraer requisitos discretos** de la norma (artículo por artículo).
3. **Mapear cada requisito** a políticas/procedimientos existentes: directo / indirecto / sin coincidencia.
4. **Diferenciar:** Ninguna / Parcial / Total + cambio específico necesario + responsable.
5. **Brechas sin coincidencia:** opciones de política nueva.
6. **Ramas:** pre-consulta (solo pre-posicionamiento), hallazgo negativo (un párrafo), brecha (análisis completo).

### Compuertas
- Integridad del alcance: las exclusiones del usuario se marcan en voz alta y se arrastran al registro de brechas.
- ⚖️ Compuerta de Revisión Jurídica: el análisis es insumo, no sustituye la decisión del abogado.

### Formato de salida
*Conclusión + tabla resumen + análisis detallado por requisito + pie de verificación de fuentes.*
