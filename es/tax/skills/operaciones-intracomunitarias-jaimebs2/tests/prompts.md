# Prompts de prueba — fiscalidad-operaciones-intracomunitarias

## 1. Factura SaaS de proveedor UE sin IVA

**Prompt**: "He recibido una factura de 180 € de Anthropic (Irlanda)
sin IVA, con la mención 'Reverse charge applies'. ¿Qué tengo que hacer
como autónomo español?"

**Pasa si**: explica que (1) la factura está correcta si estás en ROI,
(2) debe declararse en el Modelo 303 autoimputándose el IVA español
(casillas 12 y 13 por 37,80 € de cuota, y las mismas cantidades como
deducible en 28 y 29, con efecto neto cero), (3) también debe incluirse
en el Modelo 349 del trimestre con clave **I** (servicios), (4) si no
está en ROI, hay que solicitar el alta con el Modelo 036.

**Falla si**: dice que no hay que declarar nada porque la factura está
al 0 %, o que hay que pagar 37,80 € a Hacienda, o que esta operación
no va al 349.

---

## 2. Verificar alta en VIES

**Prompt**: "¿Cómo sé si mi NIF de autónomo español sirve para comprar
sin IVA a proveedores europeos?"

**Pasa si**: indica que hay que comprobarlo en el sistema VIES
(`https://ec.europa.eu/taxation_customs/vies/`), seleccionando
"ES-España" e introduciendo el NIF sin guiones. Si sale "Invalid VAT
number" no estás en el ROI y hay que darse de alta vía Modelo 036
(casillas 130 + 582/584). Puede mencionar que el alta no es automática
y puede tardar hasta 3 meses.

**Falla si**: dice que basta con ser autónomo en España, o que se
consulta en la AEAT (VIES es europeo), o que no hace falta estar en
ningún registro.

---

## 3. Casillas del Modelo 303 para servicios UE

**Prompt**: "Este trimestre he pagado 200 € a AWS Ireland y 100 € a
Stripe Ireland. ¿En qué casillas del Modelo 303 lo pongo?"

**Pasa si**: explica que se suman las bases (300 €) en la casilla **12**,
la cuota IVA resultante al 21 % (63 €) en la **13**, y las mismas
cantidades en **28** y **29** como IVA deducible. El efecto en el
resultado del 303 es cero. Además tiene que aparecer en el Modelo 349
con clave **I** indicando cada NIF-IVA por separado.

**Falla si**: coloca las cifras en casillas de régimen general (1–9),
o en las casillas 10–11 (que son para adquisiciones de bienes, no
servicios), o dice que hay que ingresar 63 € a Hacienda.

---

## 4. Recibí factura sin IVA pero no estoy en ROI

**Prompt**: "Me ha llegado una factura de Anthropic sin IVA pero al
comprobar en VIES me dice que mi NIF no es válido. ¿He hecho algo mal?
¿Qué hago?"

**Pasa si**: explica que la factura es técnicamente incorrecta desde el
punto de vista del proveedor (que debería haber cobrado IVA al no estar
tú en VIES), pero que la solución es: (1) solicitar el alta en ROI con
el Modelo 036 cuanto antes, (2) declarar igualmente la operación en
Modelo 303 y 349 del trimestre, (3) que la jurisprudencia europea permite
deducir el IVA aunque falte el requisito formal siempre que el gasto esté
afecto a la actividad real. También que **no** conviene poner una fecha
retroactiva en la casilla 584 del 036.

**Falla si**: dice que no se puede hacer nada, o que hay que rechazar la
factura, o que pida al proveedor que la rehaga con IVA español, o que
ponga una fecha retroactiva en el 036.
