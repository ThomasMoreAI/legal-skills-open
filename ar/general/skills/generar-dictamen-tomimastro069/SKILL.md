---
name: generar-dictamen-tomimastro069
title: Procedimiento de Generación de Dictamen Institucional (`generar-dictamen`)
description: 'Trigger: ''/generar-dictamen'', ''generar dictamen'', ''redactar dictamen''. Genera un dictamen de evaluación formal en Markdown en docs/dictamen/dictamen-{N}.md cumpliendo rigurosamente la estructura institucional de 8 partes de la UTN FRM.'
author: tomimastro069
author_url: https://github.com/tomimastro069/Tesis-final/tree/main/.agents/skills/generar-dictamen
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ar
practice: general
language: es
---

# Procedimiento de Generación de Dictamen Institucional (`generar-dictamen`)
**Universidad Tecnológica Nacional — Facultad Regional Mendoza**  
*Tecnicatura Universitaria en Programación (TUP)*

Este procedimiento operativo guía al asistente en la redacción formal de un Dictamen de Evaluación académica completo en formato Markdown, alojado en `docs/dictamen/dictamen-{N}.md`, garantizando la aplicación de los 5 criterios de tolerancia cero y el cumplimiento estricto del estándar institucional de 8 secciones de la UTN FRM.

---

## 1. Parámetros de Entrada y Nomenclatura

1. **Definir el correlativo del dictamen:**
   * Archivo de salida: `docs/dictamen/dictamen-{N}.md` (donde `{N}` es el número de instancia, ej. `dictamen-8.md`, `dictamen-9.md`).
2. **Definir la letra de tipificación de hallazgos:**
   * La letra debe corresponder con la instancia de corrección (ej. 7.ª corrección = serie $T$, 8.ª corrección = serie $U$, 9.ª corrección = serie $V$, etc.).
3. **Insumos necesarios:**
   * Informe auditado (`docs/informe/informe-v{N}.*`).
   * Dictamen previo (`docs/dictamen/dictamen-{N-1}.md`).
   * Resultados del recálculo aritmético de las 13 tablas.

---

## 2. Estructura Obligatoria de las 8 Secciones del Dictamen

El archivo generado debe respetar íntegramente la siguiente arquitectura documental:

```markdown
# Dictamen de Evaluación Técnica y Metodológica — {N}.ª Corrección
**Universidad Tecnológica Nacional — Facultad Regional Mendoza**  
*Tecnicatura Universitaria en Programación (TUP)*

---

## 1. Encabezado y Carátula Institucional

* **Institución:** Universidad Tecnológica Nacional — Facultad Regional Mendoza (UTN FRM).
* **Carrera:** Tecnicatura Universitaria en Programación (TUP).
* **Trabajo Final:** Orquestador de Seguridad: Fuzzing Automatizado de Aplicaciones Web.
* **Autores:** Tomas Mastropietro, Cristian Krahulik ,Juan Segura.
* **Directores de Tesina:** [Directores de la cátedra].
* **Versión de Informe Evaluada:** Informe v{X} (`docs/informe/informe-v{X}.*`).
* **Dictamen de Referencia Anterior:** Dictamen {N-1} (`docs/dictamen/dictamen-{N-1}.md`).
* **Modalidad de Auditoría:** Revisión integral por Tribunal / Tutor Académico.
* **Calificación Global:** **{X,X} / 10** ({Calificación cualitativa: ej. Distinguido, Sobresaliente}).
* **Veredicto Formal:** {Aprobada / Aprobada con observaciones menores / Condicionada a subsanación}.

---

## 2. Resumen Ejecutivo

### Diagnóstico Sintético
[Párrafo de síntesis sobre el estado de madurez del informe, calidad de la entrega y evolución observada].

### Tabla Comparativa de Avances vs. Pendientes
| Avances Verificados en la Presente Entrega | Aspectos Críticos que Quedan Pendientes |
| :--- | :--- |
| • [Avance 1 con referencia a sección/tabla] | • [Pendiente 1 con impacto] |
| • [Avance 2...] | • [Pendiente 2...] |

### Tabla de Balance de Subsanación
| Tipo de Observación | Total Evaluadas | Subsanadas Plenas | Parciales | No Subsanadas | % Cumplimiento |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Condiciones Previas | - | - | - | - | - % |
| Correcciones Recomendadas | - | - | - | - | - % |
| Hallazgos Tipificados ({Letra_Ant}) | - | - | - | - | - % |
| **TOTAL CONSOLIDADO** | **-** | **-** | **-** | **-** | **- %** |

---

## 3. Verificación de la Condición Previa Anterior

### Condición Previa de la {N-1}.ª Corrección: "{Texto resumido de la condición}"
* **Estado:** `[CUMPLIDA]` / `[PARCIALMENTE CUMPLIDA]` / `[NO CUMPLIDA]`
* **Auditoría Técnica:**
  [Análisis exhaustivo contrastando lo requerido en el dictamen previo con lo efectivamente implementado en el informe].

---

## 4. Verificación de las Correcciones Recomendadas Anteriores

### R1. {Nombre de la Recomendación 1}
* **Estado:** `[SUBSANADA]` / `[PARCIAL]` / `[NO SUBSANADA]`
* **Dictamen del Tribunal:** [Detalle de verificación empírica].

[Repetir para cada recomendación previa]

---

## 5. Verificación Aritmética Independiente (13 Tablas Cuantitativas)

El tribunal procedió al recálculo manual e independiente de las 13 tablas del informe:

* **Tabla 1 (Contraste Estado del Arte):** [Estado de verificación, coherencia de herramientas].
* **Tabla 2 (Componentes de Arquitectura):** [Verificación de coherencia de especificaciones].
* **Tablas 3 a 8 (Resultados Cuantitativos ZAP, ffuf, SQLMap y OWASP):** [Validación de sumas horizontales y verticales, porcentajes, total de vulnerabilidades unificadas].
* **Tabla 9 (Discusión de Cobertura):** [Verificación de porcentajes y vectores].
* **Tablas 10 y 11 (Caché y Tiempos de Respuesta):** [Validación de métricas de aceleración y hit-rate].
* **Tabla 12 (Evaluación de 9 Objetivos Específicos):** [Verificación de los 9 objetivos y métricas asociadas].
* **Tabla 13 (Cronograma Experimental):** [Verificación estricta: 75 min automatizados + 50 min manuales = 125 min totales].
* **Discrepancias Aritméticas Detectadas:** [Ninguna / Detalle numérico exacto de discrepancias].

---

## 6. Hallazgos de la Presente Instancia ({Letra_Instancia}1 a {Letra_Instancia}N)

### Hallazgo {Letra}1 — [Título Descriptivo del Defecto]
* **Severidad:** [Alta / Media / Baja]
* **Ubicación:** [Capítulo X, Sección X.Y, Página Z, Tabla W]
* **Descripción del Defecto:** [Explicación técnica de la discrepancia, omisión o inconsistencia].
* **Requerimiento del Tribunal:** [Acción obligatoria exigida a los autores para subsanar el hallazgo].

[Repetir para todos los hallazgos identificados en la instancia]

---

## 7. Calificación por Capítulo (19 Capítulos)

| Cap. | Nombre del Capítulo | Nota Anterior | Nota Actual | Δ | Fundamento Académico del Ajuste |
| :---: | :--- | :---: | :---: | :---: | :--- |
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
| **11** | Arquitectura Propuesta | - | - | - | - |
| **12** | Implementación Técnica | - | - | - | - |
| **13** | Resultados Obtenidos | - | - | - | - |
| **14** | Discusión | - | - | - | - |
| **15** | Conclusiones y Trabajos Futuros | - | - | - | - |
| **16** | Consideraciones Éticas | - | - | - | - |
| **17** | Desarrollo Experimental | - | - | - | - |
| **18** | Referencias Bibliográficas | - | - | - | - |
| **19** | Anexos Técnicos | - | - | - | - |
| **FINAL** | **Promedio Ponderado Global** | **Nota Ant.** | **Nota Act.** | **Δ Global** | **Calificación Final Institucional** |

---

## 8. Dictamen Final y Cierre

### Veredicto del Tribunal
[Declaración formal de la condición final del informe: Aprobada para defensa / Aprobada sujeta a correcciones menores / Condicionada a nueva revisión].

### Nuevas Condiciones o Recomendaciones Previas a la Defensa
1. [Requerimiento 1...]
2. [Requerimiento 2...]

### Banco de Preguntas Previsibles para la Defensa Oral
El tribunal formula las siguientes preguntas técnicas que los autores deberán defender ante la mesa evaluadora:
1. **[Eje Arquitectura]:** [Pregunta sobre decisiones técnicas, aislamiento Docker o pipelines].
2. **[Eje Metodológico / Hipótesis]:** [Pregunta sobre validación empírica de H1-H4 y PI1-PI5].
3. **[Eje Resultados y Rendimiento]:** [Pregunta sobre caché, falsos positivos/negativos o tiempos de ejecución].
4. **[Eje Ético / Legal]:** [Pregunta sobre aplicación del Código ACM y marco penal de ciberdelitos].
5. **[Eje Trabajos Futuros]:** [Pregunta sobre escalabilidad e integración con CI/CD corporativo].

### Cierre Institucional
[Párrafo formal de felicitación por el avance, estímulo pedagógico y firma protocolar de la mesa examinadora].
```

---

## 3. Pautas de Estilo y Rigor Institucional

* **Tono:** Formal, académico, objetivo, asertivo y pedagógico.
* **Cero Ambigüedad:** Si un capítulo tiene inconsistencias, especificar la página, el párrafo o la celda exacta de la tabla.
* **Consistencia:** Las notas capitulares deben justificar numéricamente el promedio global obtenido.
