# Tests manuales -- fiscalidad-sociedades

Preguntas para validar que el agente usa la skill correctamente.

---

## Test 1 -- Tipo impositivo general

**Prompt**: "Tengo una SL, cual es el tipo del Impuesto de Sociedades?"

**Criterios de aceptacion**:
- Indica el tipo general del 25 %.
- Menciona el tipo reducido del 15 % para entidades de nueva creacion.
- Explica brevemente que el IS grava el beneficio de la sociedad.
- No confunde con el IRPF (que es para personas fisicas).

---

## Test 2 -- Modelos y plazos

**Prompt**: "Cuando tengo que presentar el Impuesto de Sociedades y que modelos son?"

**Criterios de aceptacion**:
- Menciona el Modelo 200 (declaracion anual) con plazo en julio.
- Menciona el Modelo 202 (pagos fraccionados) en abril, octubre y diciembre.
- Explica que el 202 solo es obligatorio si la ultima declaracion tuvo cuota positiva.
- Indica que la presentacion es obligatoriamente electronica.

---

## Test 3 -- Deducciones I+D

**Prompt**: "Mi empresa hace investigacion, hay alguna deduccion en el Impuesto de Sociedades?"

**Criterios de aceptacion**:
- Menciona la deduccion por I+D (25 %, 42 % si supera media).
- Distingue entre I+D e innovacion tecnologica (12 %).
- Puede mencionar otras deducciones relevantes (creacion de empleo, etc.).
- Recomienda asesoramiento profesional para la correcta aplicacion.

---

## Test 4 -- Redireccion a autonomos

**Prompt**: "Soy autonomo, cuanto pago de Impuesto de Sociedades?"

**Criterios de aceptacion**:
- Aclara que los autonomos personas fisicas no pagan IS, sino IRPF.
- Redirige a fiscalidad-autonomos o fiscalidad-irpf-autonomos.
- No intenta aplicar informacion de sociedades a un autonomo.
