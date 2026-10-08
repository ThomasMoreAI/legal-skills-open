# Tests manuales — antecedentes-penales

Preguntas para validar que el agente usa la skill correctamente.

---

## Test 1 — Solicitud básica

**Prompt**: "Necesito un certificado de antecedentes penales para una oposición. ¿Cómo lo pido?"

**Criterios de aceptación**:
- Indica que se puede solicitar online en la sede del Ministerio de Justicia.
- Menciona que necesita certificado digital o Cl@ve.
- Indica que es gratuito e inmediato online (PDF firmado).
- Proporciona la URL de la sede electrónica.

---

## Test 2 — Delitos sexuales para trabajar con menores

**Prompt**: "Voy a trabajar de monitor de campamento, ¿qué certificado necesito?"

**Criterios de aceptación**:
- Identifica que necesita el certificado de delitos de naturaleza sexual.
- Explica que es obligatorio para actividades con contacto habitual con menores.
- Indica que se solicita en el mismo trámite que el de antecedentes penales, marcando la casilla correspondiente.
- Menciona que suelen exigir que tenga menos de 3 meses de antigüedad.

---

## Test 3 — Extranjero que necesita penales para nacionalidad

**Prompt**: "Soy colombiano y estoy tramitando la nacionalidad española. ¿Necesito antecedentes penales de Colombia?"

**Criterios de aceptación**:
- Confirma que para la nacionalidad se piden antecedentes españoles Y del país de origen.
- Indica que el certificado colombiano debe estar apostillado (Colombia es firmante del Convenio de La Haya).
- Menciona que debe estar traducido por traductor jurado si no está en español.
- Redirige a skills **apostilla** y **extranjeria-nacionalidad** para más detalle.

---

## Test 4 — Cancelación de antecedentes

**Prompt**: "Tengo antecedentes penales de hace 6 años por un delito leve. ¿Se pueden borrar?"

**Criterios de aceptación**:
- Explica los requisitos: haber cumplido la pena y haber transcurrido el plazo sin delinquir.
- Indica los plazos según la gravedad de la pena.
- Menciona que se puede solicitar la cancelación de oficio o a instancia de parte.
