# Tests manuales — extranjeria-nie

Preguntas para validar que el agente usa la skill correctamente.

---

## Test 1 — Qué es el NIE y cómo obtenerlo

**Prompt**: "Soy brasileño y voy a comprar un piso en Madrid. ¿Necesito un NIE? ¿Cómo lo consigo?"

**Criterios de aceptación**:
- Confirma que sí necesita NIE para la compraventa de un inmueble.
- Explica las dos vías: en España (comisaría con cita previa) o desde el extranjero (consulado).
- Menciona la documentación necesaria: formulario EX-15, pasaporte, justificación, foto, tasa 790-012.
- Indica cómo pedir cita previa.
- No confunde NIE con TIE ni con permiso de residencia.

---

## Test 2 — Diferencia NIE y TIE

**Prompt**: "¿Cuál es la diferencia entre el NIE y la TIE?"

**Criterios de aceptación**:
- Explica que el NIE es un número y la TIE es un documento físico (tarjeta de plástico).
- Indica que los ciudadanos UE obtienen NIE + certificado de registro, no TIE.
- Menciona que el número NIE no caduca pero la TIE sí.
- Distingue correctamente entre comunitarios y no comunitarios.

---

## Test 3 — NIE para ciudadano UE

**Prompt**: "Soy italiano y me acabo de mudar a Barcelona para trabajar. ¿Qué trámites necesito?"

**Criterios de aceptación**:
- Indica que como ciudadano UE debe inscribirse en el Registro Central de Extranjeros.
- Explica que obtiene un certificado de registro (tarjeta verde) con su NIE.
- Menciona que no necesita permiso de trabajo.
- Indica los requisitos (empadronamiento, contrato de trabajo o medios económicos).
- Si pregunta sobre alta laboral, redirige a seguridad-social.

---

## Test 4 — Redireccionamiento a residencia

**Prompt**: "Soy colombiano y quiero venir a vivir a España. ¿Me vale con el NIE?"

**Criterios de aceptación**:
- Explica que el NIE solo es un número de identificación fiscal.
- Indica que para residir legalmente necesita un permiso de residencia.
- Redirige a la skill extranjeria-residencia para detalle sobre permisos.
- No intenta explicar en profundidad los tipos de permisos de residencia.
