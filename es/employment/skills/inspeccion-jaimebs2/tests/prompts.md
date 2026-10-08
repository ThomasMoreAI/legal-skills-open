# Tests manuales — laboral-inspeccion

Preguntas para validar que el agente usa la skill correctamente.

---

## Test 1 — Cómo denunciar

**Prompt**: "Mi empresa no me paga las horas extra y no me da de alta en la Seguridad Social. ¿Dónde puedo denunciar?"

**Criterios de aceptación**:
- Indica que puede denunciar ante la Inspección de Trabajo (ITSS).
- Explica las vías (buzón electrónico online, presencialmente en la Inspección Provincial).
- Menciona que la denuncia es confidencial (la empresa no sabe quién denuncia).
- Indica qué datos incluir en la denuncia (datos empresa, hechos, fechas).
- Proporciona la URL del buzón electrónico.

---

## Test 2 — Anonimato y represalias

**Prompt**: "Si denuncio a mi empresa, ¿se van a enterar y me van a despedir?"

**Criterios de aceptación**:
- Explica que la ITSS no revela la identidad del denunciante.
- Menciona la garantía de indemnidad (represalias = despido nulo).
- Indica que la visita de inspección se presenta como actuación de oficio.
- Puede mencionar el buzón de fraude para comunicaciones anónimas.

---

## Test 3 — Sanciones

**Prompt**: "¿Qué le pasa a una empresa si la Inspección de Trabajo detecta que tiene trabajadores sin contrato?"

**Criterios de aceptación**:
- Clasifica como infracción grave (no dar de alta en la Seguridad Social).
- Indica el rango de sanción (751 € a 7.500 €).
- Menciona que además se levanta acta de liquidación por cuotas no ingresadas.
- Puede indicar que los contratos se consideran indefinidos.

---

## Test 4 — Routing a convenios

**Prompt**: "Mi empresa no cumple el salario del convenio. ¿Qué convenio me aplica?"

**Criterios de aceptación**:
- Para saber qué convenio aplica, redirige a laboral-convenios.
- Puede indicar que el impago del salario del convenio es motivo de denuncia ante la ITSS.
