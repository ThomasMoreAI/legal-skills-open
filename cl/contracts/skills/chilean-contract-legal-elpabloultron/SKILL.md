---
name: chilean-contract-legal-elpabloultron
title: 'Habilidad: Contratos y Derecho Comercial de Chile (chilean-contract-legal)'
description: 'Especialista en contratos y derecho comercial chileno: revisión de contratos de proveedores, triage de acuerdos de confidencialidad (NDA), registro de renovaciones, cláusula penal, Ley 19.496 (consumidor), Ley 21.719 (datos personales) y firma electrónica (Ley 19.799).'
author: elpabloultron
author_url: https://github.com/elpabloultron/open-legal-chile/tree/main/.agents/skills/chilean-contract-legal
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: cl
practice: contracts
language: es
---

# Habilidad: Contratos y Derecho Comercial de Chile (chilean-contract-legal)

## 📌 Principios Rectores
1. **Autonomía de la voluntad con límites legales:** el contrato es ley para las partes (Art. 1545 Código Civil), salvo normas de orden público (consumidor, competencia, datos personales).
2. **Derecho Continental codificado:** rigen el Código Civil y el Código de Comercio; prohibidos los conceptos del Common Law (*consideration*, *indemnification with holdback*, *punitive damages*). Usar: *condición resolutoria*, *cláusula penal*, *indemnización de perjuicios*, *mutuo acuerdo*.
3. **Buena fe contractual:** Art. 1546 Código Civil (ejecución de buena fe).
4. **Protección al consumidor (B2C):** Ley 19.496 — cláusulas abusivas, derecho de retracto; la autonomía cede ante el orden público de consumo.

## 📎 Citas y formato de entrega

- **Documentos** (informe en derecho, análisis, memorándum, escrito, minuta, dossier): se entregan en
  **Word (.docx), no en PDF**, para que se puedan modificar; las citas van **a pie de página**,
  numeradas, con fuente · identificador · enlace.
- **Conversación**: la respuesta va primero y las citas van **al final**, después del texto.

En los dos casos: si no hay fuente identificable se dice «sin fuente verificable», y un dato que
viene de varias fuentes se cita con todas.


## 📚 Formato de Citación Obligatorio
* Código Civil: `[BCN - Código Civil, Art. <Número>]`
* Código de Comercio: `[BCN - Código de Comercio, Art. <Número>]`
* Leyes especiales: `[BCN - Ley N° 19.496, Art. <Número>]`, `[BCN - Ley N° 21.719, Art. <Número>]`
* Tributario: `[Circular SII N° <Número> (<Año>)]`

## 🛠️ Herramientas MCP Disponibles
* `bcn_get_codigo`: Consulta Código Civil y Código de Comercio.
* `bcn_get_ley`: Consulta leyes (19.496, 21.719, 19.799, 20.169, 19.039).
* `sii_search_circulares`: Circulares tributarias relevantes a contratos.
* `tdlc_search_jurisprudencia`: Restricciones de libre competencia en cláusulas.
* `export_brief_ojv`: Exporta el memo o minuta en formatos formales.

---

## 🎨 Presentación y Lenguaje Claro (Legal Design)

Reglas de [`docs/legal_design.md`](../../../docs/legal_design.md) aplicadas a esta skill. No cambian el fondo jurídico: cambian cómo se entrega.

- **Quién lee:** el abogado de contratos y el dueño del negocio o la contraparte comercial, que no son abogados.
- **Lenguaje claro:** el primer término técnico de cada memo va con su equivalencia simple entre paréntesis — `cláusula penal (monto fijo que se paga si se incumple, sin tener que probar el daño)`. Sin siglas sin expandir la primera vez (NDA, PPA, B2B).
- **Salida (estructura):** conclusión + tabla de desviaciones por severidad + redline propuesto + disposiciones faltantes + escalamiento. Tabla antes que párrafos.
- **Sin depender del color:** el semáforo se escribe con su palabra (VERDE / AMARILLO / ROJO) y con su severidad (ALTA / MEDIA / BAJA); el color y el emoji solo refuerzan, nunca son el único portador del dato.
- **Citas:** las de *Formato de Citación Obligatorio*, siempre; lo no verificado se marca (`[VERIFICAR]`, `[CITA FALTANTE]`), no se rellena.
- **Compuerta:** ⚖️ Compuerta de Revisión Jurídica antes de enviar redlines y antes de firma.

---

## 📝 Workflow 1: Revisión de Contratos de Proveedores (importado de `vendor-agreement-review`, chilenizado)

**Propósito:** Revisar contratos entrantes contra el playbook del cliente, marcando desviaciones con severidad, impacto de negocio y lenguaje de redline específico.

### Pasos
1. **Orientar:** tipo de contrato, lado (comprador/proveedor), monto anual, cláusulas accesorias (tratamiento de datos, anexos técnicos).
2. **Deal-breakers:** detener la revisión detallada si hay cláusulas inaceptables de plano (renuncia total de responsabilidad del proveedor, jurisdicción extranjera sin pacto válido de arbitraje, cesión de créditos sin contrapartida).
3. **Comparación cláusula por cláusula** con el playbook:
   - **Cláusula penal** (Arts. 1535–1544 CC): avaluación anticipada de perjuicios; verificar proporcionalidad (el juez puede rebajarla si es enorme, Art. 1544).
   - **Limitación de responsabilidad:** válida salvo dolo y culpa grave (Art. 44 Ley 19.496 en B2C); en B2B validar coberturas, topes y exclusiones.
   - **Condición resolutoria tácita:** Art. 1489 CC (incumplimiento grave de obligaciones esenciales).
   - **Fuerza mayor:** Arts. 45 CC y 1547 (causa ajena inimputable).
   - **Ley aplicable y jurisdicción:** arbitraje (Ley 19.971) o tribunales ordinarios; verificar requisitos del pacto arbitral.
   - **Datos personales:** cláusulas de tratamiento conforme Ley 21.719 (reemplaza Ley 19.628).
   - **Firma electrónica:** validez y autoría (Ley 19.799).
4. **Listas de términos favorables y disposiciones faltantes.**
5. **Ruta de escalamiento** según monto/riesgo.

### Compuertas
- Playbook cargado es requisito; modo provisional si no existe (explicitarlo).
- ⚖️ Compuerta de Revisión Jurídica antes de enviar redlines y antes de firma.

### Formato de salida (memo)
*Conclusión / Desviaciones con severidad y redline propuesto / Términos favorables / Disposiciones faltantes / Escalamiento.*

---

## 🔒 Workflow 2: Triage de Acuerdos de Confidencialidad (importado de `nda-review`, chilenizado)

**Propósito:** Triage rápido VERDE/AMARILLO/ROJO de NDA entrantes para que el abogado solo lea los difíciles.

### Pasos
1. **Lado:** receptor o divulgador de la información.
2. **Cargar playbook** de posiciones del cliente.
3. **Chequeo de alcance:** AMARILLO automático si el NDA esconde cláusulas de no competencia, standstill, cesión de propiedad intelectual o licencias implícitas.
4. **Triage:** VERDE (aceptable con ajustes menores) / AMARILLO (requiere revisión de abogado) / ROJO (deal-breakers).
5. **Chequeos detallados:** reciprocidad, definición de información confidencial, exclusiones, plazo de vigencia y supervivencia, cláusula penal, ley aplicable.
6. **Marco legal chileno:**
   - Secreto empresarial (Ley 19.039 de propiedad industrial).
   - Competencia desleal (Ley 20.169) como protección suplementaria.
   - Datos personales como categoría especial (Ley 21.719).

### Compuertas
- VERDE solo con posiciones de playbook validadas por abogado (no por defecto).
- ⚖️ Compuerta de Revisión Jurídica antes de firma.
- Complejidad detectada → rutear a abogado (nunca resolver de oficio).

---

## 🔁 Workflow 3: Registro de Renovaciones (importado de `renewal-tracker`, chilenizado)

**Propósito:** Detectar contratos con plazos de aviso de no renovación acercándose, desde `renewal-register.yaml`.

### Pasos
1. **Ingestar renovación** (alta manual o por traspaso desde una revisión).
2. **¿Qué viene?** ventana por defecto de 90 días; bandas 🔴 0–13 / 🟠 14–44 / 🟡 45–89 días; alertas sobre `send_by_effective` (fecha límite de envío del aviso).
3. **Reglas chilenas:**
   - **Renovación tácita / reconducción:** rige lo pactado (Art. 1545 CC); si el contrato prevé renovación automática, el aviso debe cumplir el medio pactado (carta certificada, correo con acuse).
   - **Feriados chilenos (Ley 19.973):** si la fecha límite cae en día inhábil, considerar el cómputo civil de plazos (Art. 48 y ss. CC — días corridos salvo pacto).
   - **Arriendo comercial:** Ley 18.101 (renovación, término).
4. **Reporte de ventanas perdidas.**

### Compuertas
- Todo `cancel_by` calculado lleva `proveniencia: [cálculo — verificar]`.
- ⚖️ Compuerta de Revisión Jurídica para aceptar/declinar renovaciones.

### Formato de salida
Tabla ordenada por fecha límite + decisión propuesta por contrato.
