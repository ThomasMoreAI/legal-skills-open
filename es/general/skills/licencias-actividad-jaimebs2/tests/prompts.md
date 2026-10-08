# Tests manuales — licencias-actividad

Preguntas para validar que el agente usa la skill correctamente.

---

## Test 1 — Abrir un bar

**Prompt**: "Quiero abrir un bar en Madrid. ¿Qué licencias necesito?"

**Criterios de aceptación**:
- Indica que un bar es actividad clasificada (molesta por ruido).
- Explica que necesita licencia de actividad previa con proyecto técnico.
- Menciona habilitaciones sectoriales de hostelería/alimentación (manipulador de alimentos, APPCC).
- Advierte que los requisitos concretos dependen del ayuntamiento de Madrid.
- Menciona que puede necesitar licencia de obras si hay que reformar el local.

---

## Test 2 — Abrir una tienda de ropa

**Prompt**: "Voy a abrir una tienda de ropa de 60 m². ¿Necesito licencia?"

**Criterios de aceptación**:
- Indica que es actividad inocua y comercio minorista < 750 m².
- Explica que aplica la Ley 12/2012 y basta con declaración responsable.
- Indica que puede iniciar la actividad desde la presentación.
- Advierte que debe verificar la compatibilidad urbanística del local.

---

## Test 3 — Declaración responsable vs. licencia

**Prompt**: "¿Qué diferencia hay entre declaración responsable y licencia de actividad?"

**Criterios de aceptación**:
- Explica que la declaración responsable permite iniciar de inmediato y la licencia requiere esperar aprobación.
- Indica cuándo aplica cada una (inocuas vs. clasificadas).
- Menciona que el ayuntamiento puede inspeccionar posteriormente con la declaración responsable.

---

## Test 4 — Trabajar desde casa

**Prompt**: "Voy a hacerme autónomo trabajando desde casa como programador. ¿Necesito licencia de actividad?"

**Criterios de aceptación**:
- Indica que generalmente NO se necesita licencia si trabaja desde casa sin atención al público.
- Sugiere verificar con el ayuntamiento por si hay regulación de actividades domiciliarias.
- Remite a la skill alta-autonomo para el proceso de alta como autónomo.
