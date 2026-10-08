# Tests manuales — extranjeria-residencia

Preguntas para validar que el agente usa la skill correctamente.

---

## Test 1 — Nómada digital

**Prompt**: "Soy programador freelance y trabajo para una empresa de EE.UU. ¿Puedo irme a vivir a España con la visa de nómada digital?"

**Criterios de aceptación**:
- Menciona la Ley 28/2022 (Ley de Startups).
- Explica los requisitos: relación laboral con empresa extranjera, titulación o experiencia, ingresos mínimos (200 % del SMI), seguro médico.
- Distingue entre visado de teletrabajo (1 año) y autorización de residencia (3 años).
- Indica que la solicitud se tramita en consulado o UGE-CE.
- No confunde con permiso de trabajo por cuenta propia.

---

## Test 2 — Residencia de larga duración

**Prompt**: "Llevo 5 años viviendo legalmente en España con permiso de trabajo. ¿Puedo pedir la residencia permanente?"

**Criterios de aceptación**:
- Confirma que tras 5 años de residencia legal continuada puede solicitar residencia de larga duración.
- Menciona las ausencias permitidas (máx. 6 meses continuados, 10 meses en total).
- Indica los derechos (trabajar en mismas condiciones que un español).
- Menciona la opción de residencia de larga duración UE.

---

## Test 3 — Residencia no lucrativa

**Prompt**: "Estoy jubilado y quiero mudarme a España. No voy a trabajar. ¿Qué permiso necesito?"

**Criterios de aceptación**:
- Recomienda la residencia no lucrativa.
- Explica que no permite trabajar.
- Menciona los requisitos económicos (referencia al IPREM).
- Indica que necesita seguro médico completo.
- Menciona que se solicita en el consulado de España.

---

## Test 4 — Redireccionamiento a trabajo

**Prompt**: "Quiero saber los requisitos del Catálogo de Ocupaciones de Difícil Cobertura para conseguir un permiso de trabajo."

**Criterios de aceptación**:
- Reconoce que se trata de un tema de permiso de trabajo.
- Redirige a la skill extranjeria-trabajo para detalle sobre CODC.
- No intenta explicar en profundidad el catálogo.
