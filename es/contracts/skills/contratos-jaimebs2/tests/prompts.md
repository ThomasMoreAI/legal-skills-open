# Tests manuales — laboral-contratos

Preguntas para validar que el agente usa la skill correctamente.

---

## Test 1 — Tipos de contrato post-reforma

**Prompt**: "¿Qué tipos de contrato temporal existen ahora en España?"

**Criterios de aceptación**:
- Menciona que la reforma laboral de 2022 eliminó el contrato de obra y servicio.
- Indica que solo quedan dos causas temporales: circunstancias de la producción y sustitución.
- Explica la duración máxima del temporal por circunstancias de la producción (6 meses, ampliable a 1 año).
- Menciona que el contrato indefinido es ahora el contrato por defecto.

---

## Test 2 — Despido e indemnización

**Prompt**: "Me quieren despedir de mi empresa. ¿Qué indemnización me corresponde?"

**Criterios de aceptación**:
- Diferencia entre despido disciplinario procedente (0), objetivo procedente (20 días/año) e improcedente (33 días/año).
- Menciona los topes (12 y 24 mensualidades respectivamente).
- No confunde con indemnización de fin de contrato temporal (12 días/año).
- Sugiere consultar con un profesional para el caso concreto.

---

## Test 3 — Contrato formativo

**Prompt**: "Acabo de terminar la carrera, ¿me pueden hacer un contrato en prácticas?"

**Criterios de aceptación**:
- Explica el contrato para la obtención de práctica profesional (post-reforma).
- Indica que debe celebrarse dentro de los 3 años siguientes al título.
- Menciona duración (6 meses a 1 año) y que la retribución es la del convenio, nunca inferior al SMI.
- Distingue del contrato de formación en alternancia.

---

## Test 4 — Routing a desempleo

**Prompt**: "He terminado mi contrato temporal. ¿Cuánto me dan de paro?"

**Criterios de aceptación**:
- Indica que la pregunta sobre cuantía de la prestación corresponde a la skill laboral-desempleo.
- Puede mencionar que el fin de contrato temporal genera derecho a desempleo, pero no entra en detalle de cuantías.
