# Tests manuales — laboral-desempleo

Preguntas para validar que el agente usa la skill correctamente.

---

## Test 1 — Requisitos y duración

**Prompt**: "Me han despido después de 3 años trabajando. ¿Cuánto tiempo puedo cobrar el paro?"

**Criterios de aceptación**:
- Explica que con 3 años (1.080+ días) cotizados corresponden 360 días (12 meses) de prestación.
- Indica que los primeros 180 días cobra el 70 % de la base reguladora y el resto al 50 %.
- Menciona los topes mínimo y máximo (vinculados al IPREM y cargas familiares).
- Recuerda el plazo de 15 días hábiles para solicitar.

---

## Test 2 — Subsidio tras agotar prestación

**Prompt**: "Se me ha acabado el paro y no encuentro trabajo. ¿Tengo derecho a algo más?"

**Criterios de aceptación**:
- Explica el subsidio por agotamiento de prestación contributiva.
- Indica que la cuantía es el 80 % del IPREM (~480 €/mes).
- Menciona los requisitos (cargas familiares o mayor de 45 años).
- Orienta sobre la RAI y el IMV como siguientes niveles de protección.

---

## Test 3 — Capitalización para emprender

**Prompt**: "Estoy en el paro y quiero montar mi propio negocio. ¿Puedo usar el paro para eso?"

**Criterios de aceptación**:
- Explica la capitalización del desempleo (pago único).
- Indica los requisitos (mínimo 3 meses pendientes, memoria del proyecto).
- Menciona las modalidades (pago único, subvención de cuotas, combinación).
- Indica que se solicita en el SEPE.

---

## Test 4 — Routing a estadísticas de paro

**Prompt**: "¿Cuántas personas están en paro en España ahora mismo?"

**Criterios de aceptación**:
- Indica que la pregunta sobre estadísticas de paro registrado corresponde a la skill sepe.
- No intenta dar cifras de paro.
