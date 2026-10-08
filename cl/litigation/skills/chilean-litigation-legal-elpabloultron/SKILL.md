---
name: chilean-litigation-legal-elpabloultron
title: 'Habilidad: Litigación Procesal Chilena (chilean-litigation-legal)'
description: Especialista en litigación civil, comercial y constitucional en Chile, tramitación digital OJV (Ley 20.886), intake de causas, redacción de demandas y escritos, cronologías de hechos, tablas de elementos y recursos (protección, apelación, casación).
author: elpabloultron
author_url: https://github.com/elpabloultron/open-legal-chile/tree/main/.agents/skills/chilean-litigation-legal
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: cl
practice: litigation
language: es
---

# Habilidad: Litigación Procesal Chilena (chilean-litigation-legal)

## 📌 Principios Rectores
1. **Proceso civil de Derecho Continental:** no existe discovery, subpoena, deposition ni privilege log (institutos del Common Law, prohibidos). La prueba es documental, confesional, testimonial, pericial e inspección personal del tribunal (CPC).
2. **Tramitación digital obligatoria:** Ley 20.886 (OJV) — todo escrito se presenta por la Oficina Judicial Virtual con firma electrónica avanzada (Ley 19.799).
3. **Efecto relativo de las sentencias:** Art. 3 inc. 2 Código Civil; la jurisprudencia orienta pero no vincula (salvo unificaciones en materia laboral, que vinculan a los tribunales laborales).
4. **Carga de la prueba:** Art. 1698 Código Civil (quien alega debe probar).

## 📎 Citas y formato de entrega

- **Documentos** (informe en derecho, análisis, memorándum, escrito, minuta, dossier): se entregan en
  **Word (.docx), no en PDF**, para que se puedan modificar; las citas van **a pie de página**,
  numeradas, con fuente · identificador · enlace.
- **Conversación**: la respuesta va primero y las citas van **al final**, después del texto.

En los dos casos: si no hay fuente identificable se dice «sin fuente verificable», y un dato que
viene de varias fuentes se cita con todas.


## 📚 Formato de Citación Obligatorio
* Constitución: `[CPR 1980 - Art. <Artículo> N° <Numeral>]`
* Código de Procedimiento Civil: `[BCN - Código de Procedimiento Civil, Art. <Número>]`
* Código Civil: `[BCN - Código Civil, Art. <Número>]`
* Jurisprudencia Corte Suprema: `[CS - Rol N° <Número>-<Año>, Fecha: <D-M-A>]`
* Corte de Apelaciones: `[C.A. de <Ciudad> - Rol N° <Número>-<Año>]`

## 🛠️ Herramientas MCP Disponibles
* `export_brief_ojv`: Genera y exporta el escrito formal (`.html`, `.md`, `.txt`, `.json`).
* `bcn_get_codigo`: Consulta CPC, Código Civil o Código Penal.
* `bcn_get_ley`: Consulta leyes procesales (20.886, 19.966, 20.720, etc.).
* `pjud_search_jurisprudencia`: Fallos rectores de la CS y TC.

---

## 🎨 Presentación y Lenguaje Claro (Legal Design)

Reglas de [`docs/legal_design.md`](../../../docs/legal_design.md) aplicadas a esta skill. No cambian el fondo jurídico: cambian cómo se entrega.

- **Quién lee:** dos registros distintos, y no se mezclan. El escrito judicial y los recursos van en forma procesal de rigor para el tribunal; el resumen de estado y la explicación de escenarios van en lenguaje claro para el cliente.
- **Lenguaje claro (para el cliente):** el primer término técnico va con su equivalencia simple entre paréntesis — `preclusión (se venció el plazo y ya no se puede hacer ese trámite)`.
- **Salida (estructura):** resumen de estado en tabla (plazo, fecha, días restantes) + cronología en tabla + tabla de elementos (Elemento / Norma / Evidencia / Fuente / Brecha). Tabla antes que párrafos.
- **Sin depender del color:** la significancia de los hitos se escribe con su palabra (CLAVE / RELEVANTE / CONTEXTUAL) junto al marcador; el color y el emoji solo refuerzan.
- **Citas:** las de *Formato de Citación Obligatorio*, siempre; lo no verificado se marca (`[VERIFICAR]`, `[CITA FALTANTE]`, `[EVIDENCIA FALTANTE]`), no se rellena. Nunca se inventan plazos.
- **Compuerta:** ⚖️ Compuerta de Revisión Jurídica antes de ingresar cualquier escrito a la OJV.

---

## 📥 Workflow 1: Intake de Causas (importado de `matter-intake`, chilenizado)

**Propósito:** Alta uniforme de un nuevo asunto litigioso. Escribe `materia.md`, `historia.md` y una fila en `_log.yaml`.

### Pasos
1. **Identificación:** nombre del cliente, contraparte, tipo de causa, rol (demandante/demandado), tribunal y jurisdicción.
2. **Verificación de conflictos de interés:** consulta del registro interno (normas de ética profesional del Colegio de Abogados). Un "no ejecutado" es **STOP duro** (ejecutar ahora / pendiente con responsable / bypass documentado).
3. **Fuente:** demanda notificada, resolución, denuncia o requerimiento.
4. **Triage de riesgo** contra la calibración del perfil de práctica.
5. **Plazos fatales:** contestación de demanda (reglas por procedimiento), prescripción extintiva (Art. 2492 y ss. CC; Art. 510 CT en laboral), recursos (reposición 5 días, apelación 5/10 días, casación 15 días).
6. **Teoría inicial del caso** marcada `[VERIFICAR]`.

### Compuertas
- Conflicto de intereses no resuelto → no continuar.
- Nunca inventar plazos: verificar con `bcn_get_codigo` (CPC/CT).
- ⚖️ Compuerta de Revisión Jurídica en todo documento derivado.

---

## ⚔️ Workflow 2: Redacción de Demanda (importado de `demand-draft`, chilenizado)

**Propósito:** Redactar una demanda desde un intake completo, con compuertas previas y post-envío.

### Pasos
1. **Cargar intake** (negarse si no existe) y configurar postura (tono, plazo, signatario).
2. **Compuerta pre-redacción (7 ítems):** privilegio de la información, riesgo de admisiones, transacción en curso, postura frente a conciliación, escaneo de renuncias, tono, exactitud fáctica.
3. **Estructura obligatoria (Ley 20.886 / CPC):**
   - Presuma (PROCEDIMIENTO, MATERIA, partes, RUTs, abogado).
   - Designación del tribunal y comparecencia.
   - **EN LO PRINCIPAL:** demanda — *I. Los Hechos* (cronológicos y numerados), *II. El Derecho* (normas citadas), *III. Peticiones Concretas* ("POR TANTO, A US. PIDO...").
   - **PRIMER OTROSÍ:** patrocinio y poder (Ley 18.120).
   - **SEGUNDO OTROSÍ:** documentos acompañados con custodia (Art. 30 CPC).
4. **Gestiones previas si aplican:** gestión preparatoria de vía ejecutiva (Arts. 273+ CPC), mediación prejudicial (Art. 106 Ley 19.966; laboral: reclamación administrativa ante la DT en tutela).
5. **Prescripción:** verificar cómputo antes de presentar.
6. **Post-presentación:** checklist (certificado de ingreso OJV, folio, distribución).

### Compuertas
- Compuerta pre-redacción detiene la redacción si hay banderas.
- Verbatim: las citas textuales jamás se inventan; usar `[CITE:___]` y completar solo con fuente verificada.
- ⚖️ Compuerta de Revisión Jurídica antes de ingresar a la OJV.

---

## 🗓️ Workflow 3: Cronología de Hechos (importado de `chronology`, chilenizado)

**Propósito:** Construir/actualizar una línea de tiempo desde fuentes documentales declaradas.

### Pasos
1. **Identificar fuentes:** rutas de archivos del usuario, carpeta del asunto, expediente OJV descargado.
2. **Leer y extraer eventos fechados** (contrato, notificaciones, correos, resoluciones).
3. **De-duplicar** (un evento, múltiples fuentes).
4. **Etiquetar significancia** según la teoría del caso (🔴 clave / 🟡 relevante / ⚪ contextual).
5. **Redactar cronología** versionada con sección de brechas probatorias.

### Reglas chilenas
- Sin números Bates: usar **foliación del expediente** y fecha del documento.
- Sin deposiciones: la prueba testimonial se rinde en audiencia; la cronología usa solo documentos declarados.
- Marcar cada entrada con su documento fuente; brechas con `[EVIDENCIA FALTANTE]`.

---

## ✍️ Workflow 4: Redacción de Escritos (importado de `brief-section-drafter`, chilenizado)

**Propósito:** Redactar una sección de escrito (hechos, derecho, argumento, peticiones) en estilo del estudio y coherente con la teoría del caso.

### Pasos
1. Definir qué sección se redacta y para qué instancia.
2. **Chequeo de teoría:** negarse si la sección contradice la teoría del caso.
3. Redactar en estilo de casa (lenguaje forense chileno: "A US. respetuosamente digo", "Por tanto", otrosíes).
4. **Disciplina de citas:** todo hecho con fuente; `[VERIFICAR]`, `[CITA FALTANTE]` explícitos; las normas citadas se verifican con `bcn_get_codigo`/`bcn_get_ley`.
5. **Recursos:** estructura de apelación (Arts. 186+ CPC), casación en la forma/fondo (Arts. 764–786 CPC), reposición (Art. 181 CPC), recurso de protección (Art. 20 CPR, autos acordados).

### Compuertas
- Honestidad sobre argumentos débiles (regla de franqueza con el tribunal y con el cliente).
- ⚖️ Compuerta de Revisión Jurídica antes de la presentación.

---

## 🧩 Workflow 5: Tabla de Elementos Civil (importado de `claim-chart`, chilenizado)

**Propósito:** Construir la tabla elemento-por-elemento de una pretensión civil, con cada celda citable y detección de brechas probatorias como salida prioritaria.

### Pasos
1. **Identificar la acción:** resolución de contrato (Art. 1489 CC), cumplimiento forzado (Art. 1553), indemnización extracontractual (Arts. 2314/2329), nulidad (Arts. 1681+), reivindicatoria, etc.
2. **Cargar elementos de la acción** desde la norma (nunca de memoria): obligación válida, incumplimiento grave, imputabilidad, daño, relación causal.
3. **Mapear evidencia por elemento:** documentos, testigos, confesión (absolución de posiciones), peritajes.
4. **Lista de brechas:** elementos sin prueba disponible → plan de prueba en audiencia preparatoria.
5. **Marco probatorio:** carga de la prueba (Art. 1698 CC), medios de prueba (Arts. 341+ CPC).

### Compuertas
- Banner permanente: "una tabla es un borrador, no una conclusión ni una pretensión".
- ⚖️ Compuerta de Revisión Jurídica.

### Salida
Markdown + CSV con columnas: Elemento / Norma / Evidencia / Fuente (folio) / Brecha.
