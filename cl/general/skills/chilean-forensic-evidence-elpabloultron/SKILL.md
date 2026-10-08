---
name: chilean-forensic-evidence-elpabloultron
title: 'Habilidad: Peritaje Documental y OCR Judicial (chilean-forensic-evidence)'
description: Peritaje documental, extracción de texto digital y OCR sobre expedientes judiciales escaneados, actas notariales y resoluciones públicas de Chile (CPC, Ley 20.886).
author: elpabloultron
author_url: https://github.com/elpabloultron/open-legal-chile/tree/main/.agents/skills/chilean-forensic-evidence
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: cl
practice: general
language: es
---

# Habilidad: Peritaje Documental y OCR Judicial (chilean-forensic-evidence)

## 📌 Principios Rectores
1. **Fidelidad y Cadena de Custodia:** La prueba instrumental en Chile (Arts. 341 y 342 del Código de Procedimiento Civil) exige transcripción fidedigna. Si un documento está escaneado, se debe individualizar la página y el método de procesamiento (texto nativo vs. OCR pericial).
2. **Doble Capa de Verificación:** En fojas judiciales con sellos, firmas manuscritas o texto borroso, se debe priorizar la extracción de texto nativo si supera el umbral de legibilidad (>80 caracteres); en caso contrario, se aplica OCR neuronal o Tesseract a 150-300 DPI.
3. **Prohibición de Supuestos:** Si una cifra, fecha o nombre no es legible en el expediente, se debe marcar `[ILEGIBLE EN ORIGINAL: Fs. X]` y nunca inventar datos probatorios.

## 📎 Citas y formato de entrega

- **Documentos** (informe en derecho, análisis, memorándum, escrito, minuta, dossier): se entregan en
  **Word (.docx), no en PDF**, para que se puedan modificar; las citas van **a pie de página**,
  numeradas, con fuente · identificador · enlace.
- **Conversación**: la respuesta va primero y las citas van **al final**, después del texto.

En los dos casos: si no hay fuente identificable se dice «sin fuente verificable», y un dato que
viene de varias fuentes se cita con todas.


## 📚 Formato de Citación Obligatorio
* Documento Judicial: `[Expediente PJUD - Rol N° <Rol>, Foja <Fs.>]`
* Acta Notarial: `[Notaría <Nombre> - Repertorio N° <Rep.>, Fecha: <D-M-A>]`
* Código de Procedimiento Civil: `[BCN - Código de Procedimiento Civil, Art. <Número>]`

## 🛠️ Herramientas MCP Disponibles
* `ocr_extract_pdf`: Extrae texto nativo u OCR página por página de expedientes escaneados.
* `pjud_search_jurisprudencia`: Busca fallos y doctrina procesal sobre valor probatorio de instrumentos públicos y privados.
* `bcn_get_codigo`: Consulta normas de prueba en el CPC y Código Civil.

---

## 🎨 Presentación y Lenguaje Claro (Legal Design)

Reglas de [`docs/legal_design.md`](../../../docs/legal_design.md) aplicadas a esta skill. No cambian el fondo jurídico: cambian cómo se entrega.

- **Quién lee:** el abogado que incorpora la prueba al proceso y el perito que firma el informe.
- **Lenguaje claro:** el primer término técnico del informe va con su equivalencia simple entre paréntesis — `foja (cada hoja del expediente judicial, numerada)`.
- **Salida (estructura):** informe con el texto íntegro pagina por página (`=== PÁGINA X [NATIVE/OCR] ===`) + tabla de verificaciones (nombres, RUT, fechas, montos) + notas de ilegibilidad.
- **Fidelidad primero:** si un dato no es legible, se marca `[ILEGIBLE EN ORIGINAL: Fs. X]` y no se completa con un valor plausible. La tabla de verificaciones dice qué se cotejó y qué no.
- **Citas:** las de *Formato de Citación Obligatorio*, siempre.
- **Compuerta:** ⚖️ Compuerta de Revisión Jurídica: la transcripción debe ser cotejada por el perito o el abogado antes de entrar a la demanda o querella.

---

## 🔍 Workflow 1: Procesamiento Pericial de Expedientes

### Pasos
1. **Identificación de la Fuente:** Verificar existencia del archivo PDF y cantidad total de páginas.
2. **Muestreo Inicial:** Procesar las primeras 5 a 10 páginas para evaluar si el expediente cuenta con texto seleccionable o si requiere OCR forzado (`force_ocr=True`).
3. **Segmentación Temática:** Identificar fojas clave (autos de prueba, resoluciones, contratos adjuntos, actas de directorio, sentencias).
4. **Extracción y Foliado:** Generar informe con el texto íntegro, individualizando cada página con su encabezado `=== PÁGINA X [NATIVE/OCR] ===`.
5. **Verificación Forense:** Contrastar nombres de personas naturales, RUTs, fechas de escrituración y montos dinerarios contra el escaneo original.

### Compuertas de Seguridad
- Si el documento contiene información protegida o reservada (ej. causas de familia o datos sensibles), aplicar anonimización previa.
- ⚖️ **Compuerta de Revisión:** Las transcripciones de prueba instrumental deben ser cotejadas por el perito o abogado antes de su incorporación a la demanda o querella.
