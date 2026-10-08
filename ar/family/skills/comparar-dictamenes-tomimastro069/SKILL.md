---
name: comparar-dictamenes-tomimastro069
title: Procedimiento de Comparación de Dictámenes Sucesivos (`comparar-dictamenes`)
description: 'Trigger: ''/comparar-dictamenes'', ''comparar dictamenes'', ''evolución de dictámenes''. Contrasta dos dictámenes sucesivos (ej. Dictamen 7 vs Dictamen 8) en docs/dictamen/ para analizar la evolución de notas, resolución de condiciones y nuevas observaciones.'
author: tomimastro069
author_url: https://github.com/tomimastro069/Tesis-final/tree/main/.agents/skills/comparar-dictamenes
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ar
practice: family
language: es
---

# Procedimiento de Comparación de Dictámenes Sucesivos (`comparar-dictamenes`)
**Universidad Tecnológica Nacional — Facultad Regional Mendoza**  
*Tecnicatura Universitaria en Programación (TUP)*

Este procedimiento operativo permite al asistente contrastar dos dictámenes institucionales correlativos (por ejemplo, `docs/dictamen/dictamen-7.md` y `docs/dictamen/dictamen-8.md`) para mapear con precisión quirúrgica la evolución de calificaciones, el cierre de observaciones y la aparición de nuevos requerimientos.

---

## 1. Identificación y Carga de Dictámenes

1. **Localizar los documentos a contrastar en `docs/dictamen/`:**
   * **Dictamen Base / Anterior ($D_{ant}$):** ej. `dictamen-7.md` (o versión inmediatamente previa).
   * **Dictamen Reciente / Actual ($D_{act}$):** ej. `dictamen-8.md` (o versión de referencia superior).
2. **Validar consistencia de metadatos:**
   * Verificar versiones del informe evaluadas por cada dictamen (ej. $D_{7}$ evaluó Informe v14; $D_{8}$ evaluó Informe v15).
   * Comprobar correspondencia de autores, directores y tribunal evaluador.

---

## 2. Matriz Evolutiva de Calificaciones (19 Capítulos y Global)

Generar una tabla comparativa exhaustiva que detalle el avance capítulo por capítulo:

| Cap. | Nombre del Capítulo | Nota $D_{ant}$ | Nota $D_{act}$ | Variación ($\Delta$) | Justificación / Criterio del Tribunal |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **1** | Introducción | - | - | - | - |
| **2** | Planteo del Problema | - | - | - | - |
| **3** | Justificación | - | - | - | - |
| **4** | Objetivos | - | - | - | - |
| **5** | Preguntas de Investigación | - | - | - | - |
| **6** | Hipótesis | - | - | - | - |
| **7** | Estado del Arte | - | - | - | - |
| **8** | Marco Teórico y Conceptual | - | - | - | - |
| **9** | Alcances y Limitaciones | - | - | - | - |
| **10** | Metodología | - | - | - | - |
| **11** | Arquitectura | - | - | - | - |
| **12** | Implementación Técnica | - | - | - | - |
| **13** | Resultados Obtenidos | - | - | - | - |
| **14** | Discusión | - | - | - | - |
| **15** | Conclusiones y Trabajos Futuros | - | - | - | - |
| **16** | Consideraciones Éticas | - | - | - | - |
| **17** | Desarrollo Experimental | - | - | - | - |
| **18** | Referencias Bibliográficas | - | - | - | - |
| **19** | Anexos Técnicos | - | - | - | - |
| **GLOBAL** | **Calificación Final Ponderada** | **Nota $D_{ant}$** | **Nota $D_{act}$** | **$\Delta$ Global** | **Evolución del Veredicto Formal** |

*Analizar los factores determinantes que motivaron aumentos, descensos o estancamientos en las notas individuales.*

---

## 3. Auditoría de Transición de Condiciones Previas

Analizar el estado de la o las Condiciones Previas exigidas en $D_{ant}$:
* **Condición Previa en $D_{ant}$:** Citar textualmente el requerimiento bloqueante.
* **Evaluación en $D_{act}$:**
  * Si fue considerada **CUMPLIDA**: documentar las evidencias y cambios que permitieron su levantamiento.
  * Si fue considerada **PARCIAL o NO CUMPLIDA**: identificar las discrepancias pendientes.
  * Si fue **SUSTITUIDA** por una nueva condición previa: registrar los nuevos requerimientos bloqueantes.

---

## 4. Auditoría de Correcciones Recomendadas

Revisar el destino de cada una de las recomendaciones formuladas en la instancia previa:
* Clasificar cada recomendación en:
  * `[SUBSANADA COMPLETA]`: Resuelta satisfactoriamente según el criterio del tribunal.
  * `[SUBSANADA PARCIAL]`: Hubo modificaciones pero el tribunal señaló aspectos inconclusos.
  * `[NO SUBSANADA / PERSISTENTE]`: Sin cambios verificables o desestimada por los autores.

---

## 5. Ciclo de Vida y Transición de Hallazgos

Mapear los hallazgos técnicos tipificados entre ambas instancias (ej. serie $T$ en Dictamen 7 vs. serie $U$ en Dictamen 8):

1. **Hallazgos Subsanados (Cerrados):**
   * Listar códigos resueltos con éxito y su impacto en la calificación del capítulo respectivo.
2. **Hallazgos Reincidentes o No Resueltos:**
   * Identificar hallazgos de $D_{ant}$ que no fueron subsanados y que fueron ratificados o agravados en $D_{act}$.
3. **Hallazgos Nuevos Detectados en $D_{act}$:**
   * Listar los nuevos defectos identificados en la última entrega, clasificados por severidad (*Alta*, *Media*, *Baja*).
   * Determinar si surgieron por profundización del tribunal o si representan **regresiones** introducidas al intentar corregir otros apartados.

---

## 6. Balance Cuantitativo de Subsanación

Construir la tabla consolidada de balance de correcciones:

| Categoría de Observación | Cantidad en $D_{ant}$ | Subsanados en $D_{act}$ | Parciales | No Subsanados | Tasa de Éxito (%) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Condiciones Previas | - | - | - | - | - % |
| Correcciones Recomendadas | - | - | - | - | - % |
| Hallazgos Técnicos Tipificados | - | - | - | - | - % |
| **TOTAL CONSOLIDADO** | **-** | **-** | **-** | **-** | **- %** |

---

## 7. Diagnóstico de Tendencia y Pronóstico Académico

El asistente debe concluir la comparación con una evaluación prospectiva formal:
* **Trayectoria de Calificación:** Análisis de la progresión hacia el umbral de excelencia (meta institucional: 9,0 a 10,0).
* **Camino Crítico para la Defensa Oral:** Puntos prioritarios que los alumnos deben corregir antes de la versión definitiva del informe para asegurar una defensa exitosa ante el tribunal de la UTN FRM.
