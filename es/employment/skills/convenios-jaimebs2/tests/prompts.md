# Tests manuales — laboral-convenios

Preguntas para validar que el agente usa la skill correctamente.

---

## Test 1 — Encontrar el convenio aplicable

**Prompt**: "Trabajo en una tienda de ropa en Barcelona. ¿Qué convenio colectivo me aplica y dónde lo encuentro?"

**Criterios de aceptación**:
- Indica que probablemente aplica el convenio de comercio de Barcelona (provincial) o el estatal de comercio.
- Explica cómo buscarlo en REGCON.
- Menciona que el ámbito territorial y el sector de actividad son los criterios clave.
- Proporciona la URL del buscador REGCON.

---

## Test 2 — Ultraactividad

**Prompt**: "Mi convenio colectivo caducó hace un año y no han firmado uno nuevo. ¿Sigue en vigor?"

**Criterios de aceptación**:
- Explica que tras la reforma 2022, el convenio caducado mantiene su vigencia indefinidamente (ultraactividad).
- Indica que esto revirtió la reforma de 2012 que ponía un límite de 1 año.
- Señala que las condiciones del convenio anterior se mantienen hasta que se negocie uno nuevo.
- La empresa no puede reducir condiciones alegando caducidad.

---

## Test 3 — Jerarquía de convenios

**Prompt**: "¿Qué prevalece, el convenio de mi empresa o el del sector?"

**Criterios de aceptación**:
- Explica la prioridad aplicativa del convenio de empresa en determinadas materias (salarios, horarios, etc.).
- Menciona que en otras materias, el convenio sectorial puede establecer mínimos.
- Indica que la reforma 2022 reforzó el convenio sectorial en subcontratación.

---

## Test 4 — Routing a nóminas

**Prompt**: "Según mi convenio me corresponden 1.200 € de salario base pero en mi nómina pone menos. ¿Cómo lo calculo?"

**Criterios de aceptación**:
- Para entender la nómina y las deducciones, redirige a laboral-nominas.
- Puede mencionar que el convenio fija el salario bruto y que las deducciones (SS, IRPF) reducen el neto.
