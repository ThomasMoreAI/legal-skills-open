# Tests manuales — apostilla

Preguntas para validar que el agente usa la skill correctamente.

---

## Test 1 — Apostilla básica

**Prompt**: "Necesito apostillar mi título universitario para irme a trabajar a México. ¿Cómo lo hago?"

**Criterios de aceptación**:
- Identifica que México es firmante del Convenio de La Haya, así que basta con apostilla.
- Indica que los títulos universitarios oficiales se apostillan en el Ministerio de Educación.
- Menciona el plazo orientativo (1-5 días hábiles).
- No sugiere legalización consular (no es necesaria para países del Convenio).

---

## Test 2 — Legalización consular para país no firmante

**Prompt**: "Tengo que presentar mi partida de nacimiento en China. ¿Qué tengo que hacer?"

**Criterios de aceptación**:
- Indica que China no es firmante del Convenio de La Haya.
- Describe la cadena completa: Ministerio de Justicia → MAEC → Consulado de China.
- Menciona que además necesitará traducción jurada al chino.
- Proporciona las URLs del MAEC y Ministerio de Justicia.

---

## Test 3 — Traducción jurada

**Prompt**: "¿Dónde puedo encontrar un traductor jurado de inglés en Madrid?"

**Criterios de aceptación**:
- Indica que el MAEC publica una lista oficial de traductores-intérpretes jurados.
- Proporciona la URL del listado.
- Explica brevemente qué es una traducción jurada y su diferencia con una certificada.
- Menciona que no hay tarifas oficiales fijas.

---

## Test 4 — Exención por convenio UE

**Prompt**: "Necesito presentar mi certificado de nacimiento en Francia. ¿Tengo que apostillarlo?"

**Criterios de aceptación**:
- Indica que entre países de la UE existe el Reglamento 2016/1191 que exime de apostilla para ciertos documentos (nacimiento, matrimonio, defunción).
- Menciona la posibilidad de formularios multilingües.
- Aclara que no todos los tipos de documentos están exentos.
