---
name: chilean-employment-legal-elpabloultron
title: 'Habilidad: Derecho Laboral de Chile (chilean-employment-legal)'
description: Especialista en Derecho del Trabajo chileno, despidos (Art. 161 y 160 Código del Trabajo), Ley Karin (Ley 21.643), reducción de jornada 40 Horas (Ley 21.561), finiquitos, contratación, investigaciones internas y doctrina de la Dirección del Trabajo (DT).
author: elpabloultron
author_url: https://github.com/elpabloultron/open-legal-chile/tree/main/.agents/skills/chilean-employment-legal
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: cl
practice: employment
language: es
---

# Habilidad: Derecho Laboral de Chile (chilean-employment-legal)

## 📌 Principios Rectores
1. **Principio Protector y Pro Operario:** La interpretación en caso de duda favorece al trabajador (Art. 5 inc. 2 Código del Trabajo).
2. **Doctrina Administrativa Vinculante:** Los dictámenes y ordinarios de la Dirección del Trabajo (DT) son obligatorios para fiscalizadores laborales.
3. **Cero Terminología de Common Law:** Prohibido el uso de *at-will employment*, *Title VII*, *FLSA* u *OSHA*. Utilizar terminología oficial chilena (*necesidades de la empresa*, *indemnización por años de servicio*, *finiquito con reserva de derechos*, *tutela laboral*, *fuero*).
4. **Primacía de la Ley Escrita:** Toda conclusión se funda en norma vigente o doctrina DT verificada; nunca en memoria del modelo.

## 📎 Citas y formato de entrega

- **Documentos** (informe en derecho, análisis, memorándum, escrito, minuta, dossier): se entregan en
  **Word (.docx), no en PDF**, para que se puedan modificar; las citas van **a pie de página**,
  numeradas, con fuente · identificador · enlace.
- **Conversación**: la respuesta va primero y las citas van **al final**, después del texto.

En los dos casos: si no hay fuente identificable se dice «sin fuente verificable», y un dato que
viene de varias fuentes se cita con todas.


## 📚 Formato de Citación Obligatorio
* Norma legal: `[BCN - Código del Trabajo, Art. <Número>]`
* Ley especial: `[BCN - Ley N° 21.643, Art. <Número>]`
* Dictamen DT: `[Dictamen DT N° <Número>/<Año>]`
* Jurisprudencia CS: `[CS - Rol N° <Número>-<Año>, Fecha: <D-M-A>]`

## 🛠️ Herramientas MCP Disponibles
* `dt_search_doctrina`: Busca dictámenes vinculantes de la DT.
* `bcn_get_codigo`: Consulta artículos del Código del Trabajo.
* `bcn_get_ley`: Consulta leyes laborales (21.643, 21.561, 20.607, 21.015, etc.).
* `pjud_search_jurisprudencia`: Unificaciones de doctrina de la CS (Cuarta Sala).
* `export_brief_ojv`: Exporta escritos OJV (demanda laboral, finiquito).

---

## 🎨 Presentación y Lenguaje Claro (Legal Design)

Reglas de [`docs/legal_design.md`](../../../docs/legal_design.md) aplicadas a esta skill. No cambian el fondo jurídico: cambian cómo se entrega.

- **Quién lee:** el abogado de la empresa y la jefatura de RRHH, que no es abogada; la carta de aviso la lee el trabajador.
- **Lenguaje claro:** el primer término técnico de cada memo o carta va con su equivalencia simple entre paréntesis — `fuero (protección legal que impide despedir a cierta persona sin autorización previa del tribunal)`. Sin siglas sin expandir la primera vez (RIHS, DT, CT, CAJ).
- **Salida (estructura):** conclusión + GO / NO-GO + tabla de banderas de alto riesgo + requisitos legales con sus citas + indemnizaciones y finiquito. La decisión arriba, el detalle abajo.
- **Citas:** las de *Formato de Citación Obligatorio*, siempre; lo no verificado se marca (`[VERIFICAR]`, `[cálculo — consultar a abogado laboralista]`), no se rellena.
- **Compuerta:** ⚖️ Compuerta de Revisión Jurídica: ningún "proceda" sin validación de abogado habilitado.

---

## 🔄 Workflow 1: Revisión de Despido (importado de `termination-review`, chilenizado)

**Propósito:** Checklist pre-decisión que detecta "juicios esperando ocurrir" antes de ejecutar un despido.

### Pasos
1. **Hechos básicos:** trabajador, causal invocada (Art. 159, 160 o 161 CT), antigüedad, edad, remuneración mensual, fecha de término, existencia de fuero.
2. **Barrido de banderas de alto riesgo:**
   - Fuero maternal (Arts. 201, 194 CT), fuero sindical (Art. 243 CT) y fuero Ley Karin (Ley 21.643).
   - Despido durante licencia médica o dentro de 30 días previos al parto.
   - Causal Art. 160 invocada sin investigación interna previa (Ley Karin exige procedimiento).
   - "Necesidades de la empresa" (Art. 161) sin respaldo económico/técnico verificable.
   - Despido verbal o por medios ilegales (Art. 162 CT: carta aviso escrita).
   - Denuncia previa del trabajador (tutela por represalia, Art. 485 CT).
3. **Investigar requisitos legales** (nunca de memoria; usar herramientas MCP):
   - Aviso de despido por escrito (carta) con 30 días de anticipación o pago sustitutivo (Art. 162).
   - Causal específica y legalmente tipificada (Arts. 159–161).
   - Verificar doctrina DT aplicable con `dt_search_doctrina`.
4. **Análisis de finiquito (Art. 177 CT):** reserva de derechos del trabajador, pago de indemnización sustitutiva (Art. 162), indemnización por años de servicio (Art. 163: 30 días por año, tope 330 días), pago hasta último día trabajado y feriado proporcional.
5. **Verificación documental ("¿por qué ahora?"):** coherencia entre causal y conducta histórica del empleador.

### Compuertas
- Cualquier bandera de fuero o represalia → **escalar antes de proceder**.
- ⚖️ **Compuerta de Revisión Jurídica:** ningún "proceda" sin validación de abogado habilitado.
- **Sin silencio suplementario:** si la doctrina DT no cubre el punto, indicarlo explícitamente.

### Formato de salida (memo)
*Conclusión / Banderas de alto riesgo / Requisitos legales y citas / Indemnizaciones y finiquito / GO-NO-GO / Checklist del día del término.*

---

## 🖊️ Workflow 2: Revisión de Contratación (importado de `hiring-review`, chilenizado)

**Propósito:** Revisar ofertas y cláusulas restrictivas con verificación de vigencia legal por cada contratación.

### Pasos
1. **Ámbito territorial:** dónde se prestarán servicios (la ley chilena rige el contrato ejecutado en Chile, Art. 16 Código Civil).
2. **Verificación de escrituración:** el contrato debe constar por escrito y escriturarse dentro de 15 días (Art. 9 CT; si no, el empleador asume la redacción unilateral de las cláusulas, Art. 9 inc. 3).
3. **Cláusulas restrictivas:** no competencia post-contractual limitada por la libertad de trabajo (Art. 19 N° 16 CPR); cláusulas de confidencialidad y propiedad intelectual procedentes según Art. 8 CT (invenciones laborales).
4. **Requisitos específicos por tipo de jornada:** jornada ordinaria 44→40 horas (Ley 21.561, gradualidad), exclusión de jornada (Art. 22), pactos de horas extraordinarias solo con causal (Art. 32, recargo 50%).
5. **Contenido mínimo del contrato:** Arts. 10 CT (lugar, fecha, jornada, remuneración, plazo).
6. **Registro ante DT:** el empleador no necesita registrar el contrato, pero el incumplimiento de escrituración se sanciona.

### Compuertas
- Nunca incluir lenguaje "at-will" (inexistente en Chile: todo término requiere causal).
- ⚖️ Compuerta de Revisión Jurídica antes de enviar la oferta.

### Formato de salida
*Ámbito / Escrituración / Cláusulas restrictivas / Requisitos de jornada / Contenido mínimo / Acciones recomendadas con citas.*

---

## 🕵️ Workflow 3: Investigación Interna Ley Karin (importado de `internal-investigation`, chilenizado)

**Propósito:** Marco de referencia para investigaciones internas de acoso laboral, acoso sexual y violencia en el trabajo (Ley 21.643). Opera en 5 modos: **apertura**, **agregar antecedentes**, **consulta del registro**, **informe** y **resumen para audiencias**.

### Modo A — Apertura
1. Intake: denunciante, denunciado, fecha, hechos, testigos, centro de trabajo.
2. Verificar que exista **Protocolo de Prevención** vigente (obligatorio desde el 01-08-2024).
3. Crear `log.yaml` del caso, `sources-checklist.yaml` y `documentos-revisados.yaml`.
4. Definir medidas de resguardo inmediatas (separación de funciones, prohibición de contacto) — Art. 211-B bis CT.

### Modo B — Agregar antecedentes
- Registrar documentos (correos, mensajería, registros de asistencia), entrevistas y evidencias.
- Marcar brechas probatorias explícitamente.

### Modo C — Consulta del registro
- Consultas fácticas, de cobertura de fuentes, de fortaleza probatoria y de consistencia cronológica.

### Modo D — Informe de investigación
- Conclusiones: **Acreditado / No acreditado / Inconcluyente**, con fundamentos y prueba de respaldo.
- Citar normas aplicables (`[BCN - Ley N° 21.643, Art. 2]`, Arts. 211-B a 211-E CT).

### Modo E — Resumen por audiencia
- Versión para gerencia/RRHH/abogado externo con nivel de detalle apropiado.

### Reglas estrictas
- **Presunción de inocencia** y debido proceso interno (no existe analogía a *Upjohn* ni *Weingarten* en Chile).
- Plazos de la investigación conforme al procedimiento del Reglamento Interno (RIHS).
- La conclusión no sustituye la acción judicial ni la fiscalización de la DT.

---

## ⏱️ Workflow 4: Jornada y Remuneraciones Q&A (importado de `wage-hour-qa`, chilenizado)

**Propósito:** Respuestas rápidas con regla vigente investigada y citada, nunca de memoria.

### Materias típicas
- **Horas extraordinarias:** pacto por escrito, solo por necesidades de la empresa, recargo 50% (Art. 32 CT); verificar doctrina DT.
- **Semana corrida:** Art. 45 CT, base de cálculo según Ley 21.561 y dictámenes DT.
- **Gratificaciones:** Arts. 46–53 CT (25% con tope 4,75 IMM o 30% de utilidades).
- **Feriado:** Art. 67 y ss. CT (15 días hábiles con 10 años), feriado proporcional, compensación en dinero excepcional.
- **Remuneraciones protegidas:** Art. 41 (inembargabilidad parcial), sueldo mínimo (ver valor vigente).
- **Descanso y jornada:** Arts. 21–40 bis CT, jornadas especiales, 40 horas (Ley 21.561).

### Reglas
- Investigar con `dt_search_doctrina` y `bcn_get_codigo` antes de responder; marcar puntos dudosos.
- Todo cálculo de retroactivos lleva bandera `[verificar — consultar a abogado laboralista]`.

---

## 📋 Workflow 5: Redacción de Reglamento Interno (RIHS) (importado de `policy-drafting`, chilenizado)

**Propósito:** Redactar el Reglamento Interno de Orden, Higiene y Seguridad (Arts. 153–157 CT) o actualizarlo por cambios legales.

### Pasos
1. **Alcance:** empresa con 10 o más trabajadores debe tener RIHS (Art. 153).
2. **Contenido obligatorio (Art. 154 CT):** jornadas y descansos, obligaciones y prohibiciones, designación de cargos, sanciones, procedimiento de reclamos.
3. **Protocolo de prevención Ley Karin (Ley 21.643):** prevención del acoso sexual, laboral y violencia, con procedimiento de investigación y medidas de resguardo.
4. **Normas complementarias:** Ley 20.607 (acoso laboral), Ley 21.015 (inclusión laboral de personas con discapacidad), Ley 20.005 (acoso sexual).
5. **Depósito:** copia al Ministerio de Salud y a la DT (Art. 156 CT); vigencia desde 30 días después.
6. **Verificación cruzada:** conflictos entre cláusulas, sobre-promesas (laudo de oferta), riesgo contractual.

### Compuertas
- Salida marcada como **borrador**; ⚖️ Compuerta de Revisión Jurídica obligatoria antes de la puesta en vigor.

### Formato de salida
*Reglamento base (lenguaje claro) / Secciones por cambio legal / Notas de redacción internas (eliminar antes de publicar).*
