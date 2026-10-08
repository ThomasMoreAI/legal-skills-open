---
name: chilean-dossier-assembly-elpabloultron
title: 'Habilidad: Compilación y Ensamblaje de Expedientes Judiciales (chilean-dossier-assembly)'
description: Compilación y ensamblaje de expedientes y dossiers procesales en formato PDF judicial formal A4, foliado digital, inserción de portadas separadoras para anexos y exportación dual (tribunales vs. móvil).
author: elpabloultron
author_url: https://github.com/elpabloultron/open-legal-chile/tree/main/.agents/skills/chilean-dossier-assembly
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: cl
practice: criminal
language: es
---

# Habilidad: Compilación y Ensamblaje de Expedientes Judiciales (chilean-dossier-assembly)

## 📌 Principios Rectores
1. **Estándar de Presentación Procesal:** Los escritos judiciales, denuncias administrativas ante superintendencias (SES, SMA, SUSESO) y presentaciones ante la Contraloría exigen rigurosidad visual y foliado claro.
2. **Separación Correlativa de la Prueba:** Cada anexo probatorio documental debe ir precedido de una portada A4 institucional que indique:
   - Número correlativo de anexo (ej. `ANEXO N° 1`).
   - Título oficial del documento (ej. `Sentencia Definitiva Rol C-373-2024`).
   - Descripción y pertinencia probatoria conforme a las reglas del CPC.
3. **Estrategia de Doble Salida:**
   - **Expediente Completo Consolidado:** Archivo único de 50 a 300+ páginas con el escrito principal y todos los anexos unidos para ingreso formal o juzgados.
   - **Versión Móvil Ligera:** Archivo de 200 a 350 KB que contiene únicamente el escrito principal renderizado con tipografía legible en teléfonos y pantallas táctiles sin superar límites de previsualización.

## 📎 Citas y formato de entrega

- **Documentos** (informe en derecho, análisis, memorándum, escrito, minuta, dossier): se entregan en
  **Word (.docx), no en PDF**, para que se puedan modificar; las citas van **a pie de página**,
  numeradas, con fuente · identificador · enlace.
- **Conversación**: la respuesta va primero y las citas van **al final**, después del texto.

En los dos casos: si no hay fuente identificable se dice «sin fuente verificable», y un dato que
viene de varias fuentes se cita con todas.


## 📚 Formato de Citación Obligatorio
* Folio de Expediente: `[Expediente Consolidado, Anexo N° <X>, Fs. <Y>]`
* Oficinas Digitales: `[OJV Ley N° 20.886 / Plataforma CGR / SES]`

## 🛠️ Herramientas MCP Disponibles
* `compile_legal_dossier`: Compila el Markdown, genera separadores y concatena los PDFs.
* `export_brief_ojv`: Genera la estructura formal procesal en HTML y Markdown.

---

## 🎨 Presentación y Lenguaje Claro (Legal Design)

Reglas de [`docs/legal_design.md`](../../../docs/legal_design.md) aplicadas a esta skill. No cambian el fondo jurídico: cambian cómo se entrega.

- **Quién lee:** el tribunal y quien revisa el escrito en la OJV; la versión móvil la lee el abogado en audiencia o desde el teléfono.
- **Lenguaje claro:** el primer término técnico de la portada y del informe de folios va con su equivalencia simple entre paréntesis — `foliado (numeración correlativa de cada hoja del expediente, que permite citar "foja 42")`.
- **Salida (estructura):** expediente A4 con carátula correlativa (`ANEXO N° 1`) antes de cada documento + versión móvil ligera; tabla de control de calidad (páginas, superposición de texto, peso del archivo).
- **Accesibilidad:** A4 obligatorio (595 × 842 pt), jerarquía por encabezados y no por color, anexos numerados en la portada. Si el PDF consolidado no lleva número de página o algún folio no se pudo verificar, se dice al entregarlo: hoy `compile_legal_dossier` fija A4, carátulas y marcadores TOC, pero el pie no imprime folio.
- **Citas:** las de *Formato de Citación Obligatorio* (`[Expediente Consolidado, Anexo N° <X>, Fs. <Y>]`), siempre.
- **Compuerta:** ⚖️ Compuerta de Revisión Jurídica antes de subir el expediente a la OJV: el ensamblado ordena la prueba, no la acredita.

---

## 📑 Workflow 1: Ensamblaje de Expediente Judicial

### Pasos
1. **Revisión del Escrito Principal:** Asegurar que el Markdown contenga la presuma, comparecencia, capítulos de hechos, derecho, peticiones y la lista ordenada de otrosíes y anexos.
2. **Preparación del Catálogo de Anexos:**
   - Crear una lista con `num`, `title`, `desc` y `path` para cada PDF o imagen probatoria.
   - Verificar que todos los archivos referenciados existan en el sistema de archivos.
3. **Compilación Automatizada:**
   - Ejecutar `compile_legal_dossier` definiendo la ruta del archivo consolidado y la ruta opcional de la versión ligera para móvil.
4. **Control de Calidad:**
   - Verificar el número total de páginas resultantes.
   - Comprobar que no existan errores de superposición de texto en los separadores.
   - Verificar que el peso del archivo sea admisible en las plataformas institucionales.
