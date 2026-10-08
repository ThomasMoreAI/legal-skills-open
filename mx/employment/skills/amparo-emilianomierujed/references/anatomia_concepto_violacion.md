# Anatomía del concepto de violación

Descripción de la estructura, para que el andamio se arme con las piezas en su
sitio. **No es una plantilla de redacción**: es el mapa de qué va dónde y de
quién es cada parte.

---

## Los ocho puntos

| # | Punto | De quién | Por qué |
|---|---|---|---|
| 1 | Acto reclamado | **transcrito** de la ficha del caso | Es un dato que dio el abogado |
| 2 | Porción normativa u omisión atacada | **transcrito** de la ruta elegida | Ídem |
| 3 | Premisa normativa mayor | **abogado** | Formularla es el primer movimiento argumentativo |
| 4 | Estándar aplicable | **abogado** | Elegir y enunciar el estándar es interpretar |
| 5 | Hechos del caso | **abogado** | Es su caso y su prueba |
| 6 | Subsunción | **abogado** | Es el acto central del litigio |
| 7 | Lo que van a oponer | **transcrito** del material adverso verificado | Son fuentes, sin consejo sobre cómo responderlas |
| 8 | Efecto pedido | **transcrito** de la pretensión del abogado | La tenía desde el inicio |

Los puntos 1, 2, 7 y 8 son transcripción. Los puntos 3 a 6 son del abogado y
salen vacíos con `INTERPRETACION_PENDIENTE_DEL_ABOGADO`.

**Ninguno de los ocho lo redacta la IA.** Los cuatro "transcritos" no son
redacción: son copia de algo que ya existe (lo que dijo el abogado, o lo que dice
una fuente verificada).

---

## Por qué el punto 3 es del abogado

Es la frontera y conviene tenerla clara, porque es tentador cruzarla.

La premisa normativa mayor no es "la tesis dice X". Es **"la norma, correctamente
entendida, exige Y"** — una proposición jurídica que el abogado sostiene y que va
a defender. Las fuentes la respaldan; no la constituyen.

Dos criterios pueden apuntar en la misma dirección general y admitir premisas
mayores muy distintas, con consecuencias distintas para el caso. Elegir cuál se
formula es litigar.

Lo que el andamio pone al lado del hueco 3 es **material verificado**: el
extracto literal de cada fuente, su registro, sus cuatro veredictos y su link. No
una premisa redactada, ni una sugerencia de premisa, ni "la premisa podría ser".

---

## Por qué el punto 7 no lleva consejo

El material adverso se entrega **crudo y verificado**: qué criterio existe, qué
dice literalmente, qué obligatoriedad tiene.

No se acompaña de "cómo responderlo". Anticipar el ataque es información; decidir
la respuesta es estrategia, y la estrategia es del abogado (RH-1).

---

## Orden del material dentro de un hueco

Cuando un hueco tiene varias fuentes al lado, el orden es **declarado y
mecánico** (RH-4). Encima de la lista va la línea del criterio de orden:

```
Material verificado disponible (orden: obligatoriedad → vigencia → circuito → fecha):
```

Nunca "orden: relevancia", "las más fuertes primero" ni nada que implique juicio.

Si el abogado pide otro orden, se aplica el que pida y se declara igual.

---

## Varios conceptos de violación

Cada ruta elegida produce **un** concepto de violación con sus ocho puntos. Si el
abogado eligió dos rutas, hay dos andamios independientes, numerados, sin
material compartido salvo los puntos 1 y 8.

No se fusionan rutas. Fusionarlas sería decidir cuál es principal y cuál
subsidiaria, y ese orden es una decisión de estrategia procesal.

---

## Lo que no cubre este archivo

El proemio, el capítulo de antecedentes, el señalamiento de autoridades
responsables, los preceptos violados, el capítulo de suspensión y los puntos
petitorios **no son concepto de violación**. Son forma, y viven en
`agents/redactor_formal_agent.md`, inactivo en la v1.
