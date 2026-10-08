# Tests manuales — herencias

Preguntas para validar que el agente usa la skill correctamente.

---

## Test 1 — Pasos tras fallecimiento

**Prompt**: "Mi madre ha fallecido, ¿qué pasos tengo que seguir para tramitar la herencia?"

**Criterios de aceptación**:
- Lista los pasos en orden: certificado de defunción, certificado de últimas voluntades (esperar 15 días hábiles), obtener copia del testamento, inventario de bienes, escritura de adjudicación ante notario.
- Menciona los impuestos: Sucesiones (6 meses) y plusvalía municipal si hay inmuebles.
- Indica la inscripción en Registro de la Propiedad.
- Menciona el cambio de titularidad en bancos.

---

## Test 2 — Herencia sin testamento

**Prompt**: "Mi tío ha fallecido sin testamento y no tenía hijos. ¿Quién hereda?"

**Criterios de aceptación**:
- Explica el orden de sucesión intestada: hijos > padres > cónyuge > hermanos > colaterales.
- Indica que en este caso heredarían los padres (si viven), si no el cónyuge, y luego los hermanos.
- Explica que se necesita una declaración de herederos abintestato.
- Indica que si los herederos son colaterales, la declaración se hace ante el juzgado.

---

## Test 3 — Aceptación a beneficio de inventario

**Prompt**: "Me han dicho que mi padre tenía muchas deudas. ¿Puedo heredar sin arriesgar mi dinero?"

**Criterios de aceptación**:
- Explica la aceptación a beneficio de inventario.
- Indica que el heredero solo responde con los bienes heredados.
- Menciona el plazo de 30 días para solicitarla.
- Contrasta con la aceptación pura y simple (se responde con patrimonio propio).
- Menciona la opción de renuncia (irrevocable).

---

## Test 4 — Routing a fiscalidad

**Prompt**: "¿Cuánto tengo que pagar de Impuesto de Sucesiones en Madrid?"

**Criterios de aceptación**:
- Indica que el cálculo detallado del Impuesto de Sucesiones corresponde a otra skill.
- Redirige a **fiscalidad-sucesiones-donaciones**.
- Puede mencionar orientativamente que Madrid bonifica hasta el 99 % para herederos directos.
