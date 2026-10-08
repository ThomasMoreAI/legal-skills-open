# Tests manuales -- fiscalidad-sucesiones-donaciones

Preguntas para validar que el agente usa la skill correctamente.

---

## Test 1 -- Herencia basica

**Prompt**: "Mi padre ha fallecido en Madrid y me deja un piso valorado en 300.000 EUR. Cuanto tengo que pagar de impuesto de sucesiones?"

**Criterios de aceptacion**:
- Indica que es el Impuesto de Sucesiones (Modelo 650).
- Explica que como heredero Grupo II en Madrid hay bonificacion del 99 %.
- Menciona el plazo de 6 meses desde el fallecimiento.
- Advierte que hay que sumar la plusvalia municipal.
- Recomienda verificar la normativa vigente de la CCAA de Madrid.

---

## Test 2 -- Donacion de dinero

**Prompt**: "Quiero donar 50.000 EUR a mi hijo para la entrada de un piso. Cuanto paga de impuestos?"

**Criterios de aceptacion**:
- Indica que tributa por el Impuesto de Donaciones (Modelo 651).
- Explica que depende de la CCAA de residencia del hijo.
- Menciona que muchas CCAA bonifican donaciones padres-hijos.
- Indica que la escritura publica suele ser necesaria para aplicar bonificaciones.
- Menciona el plazo de 30 dias habiles.

---

## Test 3 -- Diferencias autonomicas

**Prompt**: "Es verdad que en Madrid no se paga impuesto de sucesiones y en otras comunidades si?"

**Criterios de aceptacion**:
- Explica que el ISD es un impuesto cedido a las CCAA.
- Confirma que Madrid tiene bonificacion del 99 % para Grupos I y II.
- Menciona otras CCAA con tratamientos diferentes.
- Aclara que el impuesto existe en todas las CCAA pero las bonificaciones varian enormemente.
- Advierte de que las cifras pueden cambiar con las reformas legislativas.

---

## Test 4 -- Redireccion a ITP

**Prompt**: "Quiero comprar un piso de segunda mano, cuanto pago de impuestos?"

**Criterios de aceptacion**:
- Aclara que la compraventa de segunda mano tributa por ITP, no por ISD.
- Redirige a fiscalidad-itp-ajd.
- No intenta responder con informacion de sucesiones/donaciones.
