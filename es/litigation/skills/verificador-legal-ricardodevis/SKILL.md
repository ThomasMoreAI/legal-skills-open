---
name: verificador-legal-ricardodevis
title: 'Skill local: Verificador legal'
description: Skill local que activa el sistema de verificación de citas jurídicas españolas y europeas. Activar AUTOMÁTICAMENTE cuando el usuario aporta un escrito procesal (recurso, demanda, contestación, alegaciones, dictamen, informe jurídico), un contrato con cláusulas que invocan normativa, o cualquier texto con referencias a sentencias del Tribunal Supremo, Tribunal Constitucional, TJUE, TSJ, Audiencia Nacional, Audiencia Provincial; o normas estatales, autonómicas o europeas (leyes, reales decretos, reglamentos UE, directivas). También activar cuando el usuario diga "verifica las citas", "audita este escrito", "comprueba esta sentencia", "está bien transcrita esta cita" o cualquier petición equivalente. No activar si el documento es de otra naturaleza (técnica, financiera no regulatoria, literaria).
author: ricardodevis
author_url: https://github.com/ricardodevis/verificador-legal/tree/main/src/cowork-plugin/verificador-legal-bilbao/skills/verificador-legal
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: litigation
language: es
---

# Skill local: Verificador legal

Esta es la skill de Cowork que se carga cuando se detecta material
jurídico. Su trabajo es orientar a Claude para que invoque el comando
`/verificar-legal`, que a su vez orquesta el sistema desplegado en el
workspace de Anthropic.

## Cuándo activarte

Activación automática ante:

- Documentos con extensión `.docx`, `.pdf`, `.md` o `.txt` cuyo
  contenido incluya citas jurídicas (ver listado de patrones abajo).
- Mensajes del usuario que mencionen verificación, auditoría,
  comprobación o revisión de citas jurídicas, sentencias o normativa.
- El usuario teclea explícitamente `/verificar-legal`.

## Patrones de cita que disparan activación

- Jurisprudencia española: STS, ATS, STC, ATC, SAN, STSJ, SAP, SJPI,
  SJM, SJS, SJCA (con o sin número de recurso o fecha).
- Jurisprudencia europea: STJUE, asunto C-XXX/YY, STEDH.
- Normativa estatal: Ley X/YYYY, Ley Orgánica X/YYYY, Real Decreto
  X/YYYY, RDL X/YYYY, RD X/YYYY.
- Normativa europea: Reglamento (UE) YYYY/X, Directiva YYYY/X/UE,
  Directiva YYYY/X/CE.
- Doctrina: APELLIDOS, X., "obra entre comillas", Editorial, año, p. N.
- Doctrina administrativa: consultas vinculantes DGT V-XXXX-YY,
  resoluciones AEPD/CNMV/CNMC.

## Qué hacer al activarte

1. Si todavía no se ha llamado, invoca el comando `/verificar-legal`
   con el documento adjunto o la ruta que el usuario haya indicado.
2. Si el usuario solo te ha mostrado un fragmento de cita en chat (sin
   documento adjunto), pregunta: "¿Quieres que verifique solo esta cita
   o tienes un escrito completo? Te recomiendo subir el escrito
   completo para que la auditoría salga consistente."
3. **No improvises verificación tú mismo**. No vayas a buscar la
   sentencia con WebSearch directamente; eso lo hacen los sub-agentes
   especializados del sistema desplegado, que verifican contra
   dominios oficiales y producen un informe estructurado.

## Qué NO hacer

- No marcar como verificada una cita basándote en tu conocimiento
  general. Tu trabajo es delegar al sistema, no contestar tú.
- No interpretar la rúbrica del Outcome ni discutir con el grader;
  el grader es independiente y autoritativo en esta v1.
- No leer la API key del `.env` para nada.
- No alterar el documento original.

## Configuración esperada en el sistema del usuario

- Proyecto en `~/Documents/verificador-juris-bilbao/` (o ruta
  configurada en `VERIFICADOR_JURIS_HOME`).
- Variables `ANTHROPIC_API_KEY` en `.env` del proyecto.
- `.agent-ids.json` con coordinador, 5 sub-agentes, skill y memory
  store ya desplegados.
- Python 3.11+ con `requirements.txt` instalado.

Si falta cualquiera de esos, avisa al usuario antes de intentar
ejecutar.
