---
name: argentina-diagnostico-bitcoindefi
title: Diagnóstico previo de escritos · Derecho argentino
description: 'Revisión crítica de un escrito judicial o administrativo argentino YA redactado, antes de presentarlo: competencia, legitimación y personería, admisibilidad y vía procesal, plazos, hechos, prueba, fundamentación normativa verificada, petitorio, formalidades y riesgos (costas, preclusión). Usar cuando el abogado aporta una demanda, contestación, recurso o presentación para control de calidad previo a la presentación.'
author: Bitcoindefi
author_url: https://github.com/Bitcoindefi/agente-smith/tree/main/skills/argentina-diagnostico
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ar
practice: litigation
language: es
---

# Diagnóstico previo de escritos · Derecho argentino

Skill original de Agente Smith (MIT). Opera sobre un escrito **ya redactado** que el
abogado aporta. Objetivo: detectar defectos que causen rechazo, nulidad o riesgo,
ANTES de presentar. No reescribe el escrito (eso es `argentina-bucles`); lo audita.

## Método: auditoría en 9 secciones con semáforo

Revisar el escrito completo y calificar cada sección 🟢 (firme) / 🟡 (mejorable) /
🔴 (defecto que puede causar rechazo). Citar la parte exacta del escrito en cada
observación.

**A0. Tipo de pieza y formato.** Control previo a todo: ¿el escrito tiene la
estructura propia de su tipo de presentación y de su destinatario (skill
`argentina-formatos`)? Un descargo de faltas con formato de demanda (objeto,
capítulo de derecho, petitorio solemne) es 🔴 aunque el contenido sea correcto.

**A. Competencia.** ¿Tribunal/organismo correcto en lo material, territorial y por
grado? ¿Federal vs. provincial vs. CABA bien elegido? ¿Se fundó la competencia?

**B. Legitimación y personería.** ¿Legitimación activa/pasiva explicada? ¿Poder o
patrocinio en regla, ratificación necesaria, representación invocada correctamente?

**C. Vía y admisibilidad.** ¿La vía procesal elegida es la que corresponde a la
pretensión? ¿Instancias previas obligatorias cumplidas según jurisdicción y materia
(reclamo o agotamiento administrativo, mediación u otra instancia prejudicial)?
¿Requisitos de admisión del recurso (plazo, forma, fundamentación autónoma)?

**D. Plazos.** ¿La presentación está en término? Computar con la skill
`argentina-plazos` (jurisdicción primero). Si la notificación de origen es
cuestionable, señalar el doble escenario.

**E. Hechos.** ¿Relato claro, cronológico, completo y consistente con la prueba?
¿Alguna afirmación fáctica sin respaldo documental? Marcar cada una (riesgo:
juramento/temeridad).

**F. Prueba.** ¿Toda la prueba ofrecida y bien individualizada? ¿Pertinente y
conducente? ¿Obtención lícita? ¿Falta prueba clave para algún hecho esencial?

**G. Derecho (auditoría sistemática de citas).** La sección más auditada. Usar skill
`argentina-auditoria-citas` (auditoría obligatoria):

1. Si existe tabla de fuentes en `jurisprudencia/fuentes-*.md`: correr auditoría contra esa tabla.
2. Si NO existe tabla: crear una provisional conforme se verifiquen citas en SAIJ
   (`saij_buscar_legislacion` / `saij_buscar_jurisprudencia` / `saij_documento`).
3. Resultado de auditoría:
   - 🟢 (firme): todas las citas son ✅ (verificadas en tabla) o 🔲 (pendientes deliberadas).
   - 🟡 (mejorable): hay citas verificadas pero tabla incompleta u hay dudas de vigencia.
   - 🔴 (defecto): hay citas 🔴 bloqueantes sin resolver (no en tabla, sin marca 🔲).
4. Entregar tabla de fuentes completa + reporte de auditoría (generado por argentina-auditoria-citas).

Verificar: ¿La norma dice lo que el escrito le atribuye? ¿Está vigente? ¿El fallo
existe y sostiene lo que se le atribuye? Toda cita bloqueante 🔴: rechazo potencial.

**H. Petitorio y congruencia.** ¿Pide todo lo que el desarrollo sostiene (y nada que
no sostenga)? ¿Montos, intereses, costas? ¿Reservas necesarias (caso federal, vías
ulteriores) formuladas?

**I. Formalidades y riesgos.** Firma, copias, tasa/bono/aportes según jurisdicción,
domicilio constituido (electrónico si aplica), traducciones/legalizaciones. Riesgos:
condena en costas, sanciones por temeridad, preclusión de planteos no introducidos
ahora, y todo efecto irreversible de presentar (p. ej. pérdida de beneficios de pago
voluntario, consentimiento de actos que se querían impugnar).

## Salida

1. **Tabla semáforo** de las 9 secciones con observación puntual por sección.
2. **Lista priorizada de correcciones**: primero lo que causa rechazo (🔴), después lo
   que debilita (🟡), después estilo.
3. **Citas verificadas**: tabla norma/fallo → qué dice realmente → uuid SAIJ → veredicto
   (confirma / no confirma / 🔲 pendiente).
4. **Decisiones que no son del asistente**: si el escrito implica una opción
   estratégica irreversible, señalarla expresamente y devolverla al abogado.

## Reglas duras

- No "aprobar en general": cada sección se pronuncia.
- **Auditoría de citas obligatoria:** toda sección G se pronuncia usando `argentina-auditoria-citas`.
  No hay 🟢 sin verificación completa; no hay cierre sin reporte de auditoría.
- Ninguna cita se da por buena sin verificación en fuente primaria (SAIJ) o marca 🔲.
- El diagnóstico no reemplaza el juicio del profesional firmante.
