---
name: chilean-probity-investigation-elpabloultron
title: 'Habilidad: Auditoría de Probidad y Patrimonio Público (chilean-probity-investigation)'
description: Auditoría de probidad administrativa, cruce de Declaraciones de Intereses y Patrimonio (DIP) de InfoProbidad, detección de conflictos de interés y fiscalización bajo la Ley 20.880 y Ley 18.575.
author: elpabloultron
author_url: https://github.com/elpabloultron/open-legal-chile/tree/main/.agents/skills/chilean-probity-investigation
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: cl
practice: administrative
language: es
---

# Habilidad: Auditoría de Probidad y Patrimonio Público (chilean-probity-investigation)

## 📌 Principios Rectores
1. **Principio de Probidad Administrativa:** Consagrado en el Art. 8° de la Constitución y Art. 52 de la Ley N° 18.575 (Bases Generales de la Administración del Estado). Implica una conducta funcionaria moralmente intachable y una entrega honesta y leal al desempeño de su cargo.
2. **Publicidad Obligatoria de Patrimonio e Intereses:** Ley N° 20.880 y su reglamento. Todo sujeto pasivo debe declarar oportunamente sus actividades profesionales, participaciones en sociedades, bienes inmuebles, vehículos y pasivos relevantes.
3. **Inhabilidades e Incompatibilidades:** Prohibición estricta de intervenir en decisiones donde exista interés personal, de cónyuge o parientes hasta el tercer grado de consanguinidad o segundo de afinidad (Art. 62 N° 6 Ley 18.575).

## 📎 Citas y formato de entrega

- **Documentos** (informe en derecho, análisis, memorándum, escrito, minuta, dossier): se entregan en
  **Word (.docx), no en PDF**, para que se puedan modificar; las citas van **a pie de página**,
  numeradas, con fuente · identificador · enlace.
- **Conversación**: la respuesta va primero y las citas van **al final**, después del texto.

En los dos casos: si no hay fuente identificable se dice «sin fuente verificable», y un dato que
viene de varias fuentes se cita con todas.


## 📚 Formato de Citación Obligatorio
* Declaración DIP: `[InfoProbidad - Declaración ID <ID>, Autoridad: <Nombre>]`
* Ley de Probidad: `[BCN - Ley N° 20.880, Art. <Número>]`
* Ley de Bases Generales: `[BCN - Ley N° 18.575, Art. <Número>]`
* Dictamen Contraloría: `[Dictamen CGR N° <Número> de <Año>]`
* Informe de Auditoría CGR: `[CGR - Informe Final de Auditoría N° <Número>/<Año>]`

## 🛠️ Herramientas MCP Disponibles
* `infoprobidad_get_dip`: Descarga y estructura la Declaración de Intereses y Patrimonio de la autoridad.
* `cgr_search_auditorias`: Cruza hallazgos con los informes de auditoría e investigaciones especiales de la CGR.
* `cgr_search_jurisprudencia`: Jurisprudencia administrativa sobre faltas a la probidad, destituciones y sanciones.
* `bcn_get_ley`: Consulta Ley 20.880, Ley 18.575, Ley 19.886 y Ley 21.094.

---

## 🎨 Presentación y Lenguaje Claro (Legal Design)

Reglas de [`docs/legal_design.md`](../../../docs/legal_design.md) aplicadas a esta skill. No cambian el fondo jurídico: cambian cómo se entrega.

- **Quién lee:** el fiscalizador que arma el caso, la Contraloría y —si el informe se publica— la ciudadanía. Sobre personas concretas rige la presunción de inocencia: el informe describe hechos y su tipificación, no culpas.
- **Lenguaje claro:** el primer término técnico va con su equivalencia simple entre paréntesis — `puerta giratoria (paso directo de un cargo que regulaba a una empresa del mismo rubro)`.
- **Salida (estructura):** matriz de hallazgos en tabla (Hecho / Norma / Fuente / Estado) + conclusión; separar en filas distintas la irregularidad formal (un error de llenado) de la falta a la probidad (ocultamiento deliberado). Tabla antes que párrafos.
- **Citas:** las de *Formato de Citación Obligatorio* (`[InfoProbidad - Declaración ID <ID>, Autoridad: <Nombre>]`), siempre; un dato del formulario que no calza se describe como inconsistencia, no como delito.
- **Compuerta:** ⚖️ Compuerta de Revisión Jurídica antes de presentar el informe a la CGR o de formalizar una denuncia.

---

## 🏛️ Workflow 1: Auditoría Patrimonial Integral

### Pasos
1. **Extracción de la Declaración:** Invocar `infoprobidad_get_dip` ingresando la URL o identificador de la autoridad en InfoProbidad.
2. **Revisión de Secciones Clave:**
   - **Actividades y Empleos Anteriores:** Cotejar si existió paso de regulador a regulado ("puerta giratoria") o asesorías incompatibles.
   - **Bienes Inmuebles:** Analizar avalúo fiscal, fecha de adquisición y congruencia con ingresos declarados.
   - **Sociedades y Derechos:** Identificar RUTs de sociedades donde tenga participación él o sus familiares.
   - **Pasivos:** Detectar créditos o deudas con proveedores del Estado o instituciones intervenidas.
3. **Cruce con Compras Públicas y Auditorías:**
   - Buscar en `cgr_search_auditorias` si el organismo público donde ejerce la autoridad ha sido auditado por contrataciones irregulares.
4. **Matriz de Hallazgos:** Redactar reporte estructurado con hechos contrastados y tipificación normativa.

### Compuertas de Seguridad
- Presunción de inocencia administrativa: distinguir entre irregularidades formales (errores de llenado) y faltas graves a la probidad (ocultamiento deliberado de sociedades o conflictos directos).
- ⚖️ **Compuerta de Revisión:** Todo informe pericial o denuncia ante la CGR debe ser visado antes de su presentación oficial.
