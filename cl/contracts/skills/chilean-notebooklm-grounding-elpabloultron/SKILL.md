---
name: chilean-notebooklm-grounding-elpabloultron
title: 'Habilidad: Investigación Estratégica con NotebookLM y Grafos de Vínculos (chilean-notebooklm-grounding)'
description: Investigación jurídica compleja y síntesis probatoria fundamentada utilizando Google NotebookLM, ingesta documental masiva y generación de grafos de vínculos relacionales.
author: elpabloultron
author_url: https://github.com/elpabloultron/open-legal-chile/tree/main/.agents/skills/chilean-notebooklm-grounding
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: cl
practice: contracts
language: es
---

# Habilidad: Investigación Estratégica con NotebookLM y Grafos de Vínculos (chilean-notebooklm-grounding)

## 📌 Principios Rectores
1. **Razonamiento Fundado (Grounded Reasoning):** Toda afirmación o conclusión jurídica compleja debe estar respaldada por fuentes documentales indexadas en un cuaderno de NotebookLM. Si una premisa no figura en las fuentes, no debe presumirse.
2. **Citas Explícitas y Trazables:** Al consultar la base de conocimiento con `notebooklm_query`, se deben respetar las citas y referencias directas provistas por el modelo hacia los números de página de las sentencias, contratos o balances.
3. **Mapeo Relacional de Redes de Poder:** Las investigaciones sobre fraude, simulación absoluta o desvío de fondos públicos exigen representar visualmente las redes corporativas y políticas mediante grafos de nodos y aristas (Mermaid / JSON).

## 📎 Citas y formato de entrega

- **Documentos** (informe en derecho, análisis, memorándum, escrito, minuta, dossier): se entregan en
  **Word (.docx), no en PDF**, para que se puedan modificar; las citas van **a pie de página**,
  numeradas, con fuente · identificador · enlace.
- **Conversación**: la respuesta va primero y las citas van **al final**, después del texto.

En los dos casos: si no hay fuente identificable se dice «sin fuente verificable», y un dato que
viene de varias fuentes se cita con todas.


## 📚 Formato de Citación Obligatorio
* Cuaderno de Investigación: `[NotebookLM - Cuaderno ID: <ID>, Fuente: <Título>]`
* Diagrama de Vínculos: `[Grafo Relacional - Nodo: <ID_Nodo> -> Relación: <Vínculo>]`

## 🛠️ Herramientas MCP Disponibles
* `notebooklm_create_notebook`: Crea un cuaderno temático de caso.
* `notebooklm_add_source`: Sube escritos, sentencias o peritajes en PDF al cuaderno.
* `notebooklm_query`: Ejecuta consultas complejas con citaciones directas a las fuentes.
* `generar_grafo_vinculos`: Modela y genera diagramas Mermaid de relaciones societarias y políticas.

---

## 🎨 Presentación y Lenguaje Claro (Legal Design)

Reglas de [`docs/legal_design.md`](../../../docs/legal_design.md) aplicadas a esta skill. No cambian el fondo jurídico: cambian cómo se entrega.

- **Quién lee:** el abogado que investiga y quien lea después el informe final o el reportaje.
- **Lenguaje claro:** el primer término técnico del informe va con su equivalencia simple entre paréntesis — `absolución de posiciones (declaración de una parte en juicio, citada por la contraria, bajo juramento)`.
- **Salida (estructura):** conclusión + tabla de hallazgos con su cita a número de página de la fuente + diagrama de vínculos (Mermaid / JSON) + brechas. Tabla antes que párrafos.
- **Transparencia de IA y datos:** NotebookLM es un servicio externo de Google: antes de subir un documento a un cuaderno hay que decir qué se sube y a dónde, y no subir antecedentes confidenciales de la causa sin autorización. La cita de la fuente no se reemplaza por el resumen del modelo.
- **Citas:** las de *Formato de Citación Obligatorio* (`[NotebookLM - Cuaderno ID: <ID>, Fuente: <Título>]`), siempre; lo que no está en las fuentes subidas no se presume.
- **Compuerta:** ⚖️ Compuerta de Revisión Jurídica antes de usar el informe como respaldo probatorio o de publicarlo.

---

## 🧠 Workflow 1: Ciclo Completo de Investigación con IA

### Pasos
1. **Creación del Entorno del Caso:** Invocar `notebooklm_create_notebook` asignando un título descriptivo a la causa.
2. **Carga Estratégica de Evidencia:**
   - Ingestar la sentencia de primera instancia, recursos y dictámenes relevantes con `notebooklm_add_source`.
   - Ingestar el escrito principal de la denuncia o demanda.
3. **Interrogación y Detección de Inconsistencias:**
   - Realizar consultas orientadas a identificar contradicciones entre testimonios, cláusulas de contratos y fechas críticas usando `notebooklm_query`.
4. **Construcción del Grafo de Vínculos:**
   - Identificar las entidades clave (autoridades, sociedades compradoras, intermediarios, fondos públicos).
   - Generar el diagrama relacional con `generar_grafo_vinculos` para incrustar en el informe final o reporte de prensa.
