# Tests manuales — justicia-gratuita

Preguntas para validar que el agente usa la skill correctamente.

---

## Test 1 — Requisitos económicos

**Prompt**: "No tengo trabajo y necesito un abogado. ¿Puedo pedir justicia gratuita? ¿Cuáles son los requisitos?"

**Criterios de aceptación**:
- Explica que la justicia gratuita es un derecho constitucional.
- Indica los umbrales económicos en relación con el IPREM (2× para persona sola, 2,5× para familia 2-3 miembros, 3× para 4+).
- Menciona que se tienen en cuenta los ingresos brutos anuales de la unidad familiar.
- Indica que hay excepciones para circunstancias especiales.

---

## Test 2 — Cómo solicitarla

**Prompt**: "¿Dónde y cómo tengo que pedir un abogado de oficio?"

**Criterios de aceptación**:
- Indica que se solicita en el Colegio de Abogados de la localidad.
- Menciona la documentación necesaria (DNI, renta, certificado Catastro, etc.).
- Explica los plazos: designación provisional en 15 días, resolución en 30 días hábiles.
- Menciona el silencio administrativo positivo.

---

## Test 3 — Derecho automático

**Prompt**: "Soy víctima de violencia de género, ¿tengo derecho a un abogado gratis?"

**Criterios de aceptación**:
- Confirma que las víctimas de violencia de género tienen derecho automático a justicia gratuita.
- Indica que no necesitan acreditar ingresos.
- Menciona otros colectivos con derecho automático (terrorismo, trata, menores).
- Indica que cubre todos los procesos relacionados.

---

## Test 4 — Routing a otra skill

**Prompt**: "Necesito pedir un certificado de últimas voluntades, ¿cómo se hace?"

**Criterios de aceptación**:
- Indica que la pregunta no corresponde a justicia gratuita.
- Redirige a la skill **registro-civil**.
