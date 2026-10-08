# Tests manuales — legalizacion-documentos

Preguntas para validar que el agente usa la skill correctamente.

---

## Test 1 — Documento de país del Convenio de La Haya

**Prompt**: "Soy argentino y necesito presentar mi partida de nacimiento en España para la nacionalidad. ¿Qué tengo que hacer?"

**Criterios de aceptación**:
- Identifica que Argentina es firmante del Convenio de La Haya.
- Indica que basta con apostillar el documento en Argentina.
- Dado que el documento está en español, indica que no necesita traducción jurada.
- Menciona que para la nacionalidad se presenta en el Registro Civil.
- Redirige a **extranjeria-nacionalidad** para el proceso completo.

---

## Test 2 — Documento de país sin Convenio

**Prompt**: "Tengo un título universitario de Marruecos. ¿Cómo lo legalizo para homologarlo en España?"

**Criterios de aceptación**:
- Identifica que Marruecos no es firmante del Convenio de La Haya.
- Describe la cadena de legalización consular completa.
- Indica que necesitará traducción jurada al español.
- Menciona que la homologación del título es un trámite aparte (Ministerio de Educación).

---

## Test 3 — Exención por convenio UE

**Prompt**: "Soy francesa y me he casado en Francia. Quiero inscribir el matrimonio en el Registro Civil español. ¿Necesito legalizar la partida de matrimonio?"

**Criterios de aceptación**:
- Indica que Francia tiene convenio bilateral (Convenio de Atenas) con España.
- Explica que los documentos del Registro Civil están exentos de legalización.
- Menciona la opción de formulario multilingüe UE (Reglamento 2016/1191).
- Indica que necesitará traducción jurada o formulario multilingüe.

---

## Test 4 — Routing a apostilla (dirección inversa)

**Prompt**: "Necesito legalizar mi título español para llevarlo a Chile."

**Criterios de aceptación**:
- Identifica que la dirección es España → extranjero (no extranjero → España).
- Redirige a la skill **apostilla** para documentos españoles que van al exterior.
