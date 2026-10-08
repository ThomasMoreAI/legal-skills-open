# Auditoría de procedencia — el cinturón de seguridad de /legal

Este archivo explica el contrato de marcas que exige `nucleo/legal.mjs`.
Cárgalo cuando el auditor reporte riesgos y no sepas cómo marcarlos.

## Por qué existe

Todo el marco de honestidad de `SKILL.md` es *prompt*: se cumple si el modelo
que lee la skill es bueno y está atento. Un modelo débil, o uno bueno al final
de una sesión larga, produce el fallo característico de la asesoría legal
automática: **una cifra o un artículo inventado que suena perfectamente
creíble.** No es un error visible como un crash; es un número plausible que el
usuario puede terminar reclamando ante un juez.

Por eso la garantía no vive solo en el texto: `nucleo/legal.mjs` audita el
borrador antes de que llegue al usuario. Funciona igual con cualquier modelo,
porque no depende de que el modelo se acuerde de nada.

El auditor **no sabe derecho**. No valida que el artículo 64 diga lo que dices
que dice. Verifica una sola cosa, y es la que importa: que cada afirmación de
riesgo **declare de dónde salió**.

## Cómo se usa

```text
node <RAIZ>/nucleo/legal.mjs auditar <borrador.md>
```

Sale en 0 si todo está marcado; en 1 si hay afirmaciones sin procedencia, con
la línea, el fragmento y por qué es riesgoso. **Si reporta riesgos, corrígelos
antes de entregar — no los expliques ni los justifiques al usuario.**

## Las tres marcas

Toda afirmación de riesgo debe llevar **en su misma línea** una de estas:

| Marca | Cuándo |
|---|---|
| `[verificado: <fuente> <fecha>]` | Se abrió la fuente oficial allowlisted y se leyó el dato ahí |
| `[del documento]` | Sale del contrato/liquidación/carta que aportó el usuario, no es afirmación legal propia |
| `[no verificado]` | Se dice explícitamente que no se pudo comprobar |

Ejemplo de una respuesta que pasa la auditoría:

```text
El salario mínimo para 2026 es 1.300.000 [verificado: mintrabajo.gov.co 2026-07-25]
Tu contrato pactó 2.000.000 mensuales [del documento]
La indemnización saldría del artículo 64 del CST [no verificado] — debo
confirmar el texto vigente antes de calcular nada.
```

Fíjate en la tercera línea: `[no verificado]` es una marca **válida**. La skill
no está obligada a saberlo todo; está obligada a no fingir que lo sabe.

## Qué detecta

| Tipo | Gravedad | Por qué |
|---|---|---|
| Monto en pesos | alto | La falla más dañina: el usuario puede reclamar o aceptar una cifra falsa |
| Porcentaje | alto | Recargos y topes cambian por ley |
| Cita de artículo | alto | La alucinación legal clásica |
| Norma (ley/decreto/sentencia + año) | medio | Número y año deben salir de fuente oficial |
| Afirmación de vigencia | medio | Ignora reformas, derogatorias e inexequibilidades |
| Contradice cifra ya verificada | **crítico** | No es falta de fuente: es afirmar contra la evidencia registrada |

Ignora bloques de código, citas (`>`) y filas de tabla: ahí el texto es
ilustrativo, no una afirmación.

## Consultar la fuente oficial (en vez de recordarla)

`nucleo/fuentes.mjs` trae el texto de una fuente oficial y —lo importante—
comprueba si una cifra **aparece literalmente** en ella:

```text
node <RAIZ>/nucleo/fuentes.mjs consultar <url oficial>
node <RAIZ>/nucleo/fuentes.mjs verificar <valor> <url oficial>
```

La diferencia con preguntarle a un modelo: `verificar` no pregunta *"¿cuál es
el salario mínimo?"* (interpretación, alucinable) sino *"¿el valor 1300000
está en esta página?"* (comparación de strings, verificable). Si no está,
responde `NO VERIFICADO` y devuelve el fragmento vacío — **nunca inventa una
cifra para complacer**. Si está, devuelve el párrafo exacto donde aparece,
para que puedas leerlo tú.

Solo consulta hosts del allowlist, solo HTTPS, respeta `robots.txt`, se
identifica con su propio User-Agent y no toca nada tras un login. El contenido
descargado se envuelve con `no-confiable.mjs` antes de entrar al contexto: es
texto que repofibe no escribió.

## El registro de cifras verificadas

Cuando verifiques un dato en fuente oficial, regístralo para no volver a
buscarlo y para que el auditor detecte contradicciones futuras:

```text
node <RAIZ>/nucleo/legal.mjs registrar "salario mínimo" 2026 1300000 https://www.mintrabajo.gov.co/<ruta> 2026-07-25
node <RAIZ>/nucleo/legal.mjs cifras 2026
```

Rechaza fuentes no oficiales y procedencia incompleta. **Empieza vacío a
propósito**: precargarlo con cifras de memoria sería cometer exactamente el
error que existe para impedir. Y las cifras laborales caducan cada año — una
cifra registrada en 2026 no sirve para un caso de 2027 sin volver a verificar.

## Lo que esto NO reemplaza

El auditor detecta afirmaciones sin procedencia. No detecta:

- Que hayas leído mal la fuente.
- Que la fuente esté desactualizada.
- Que el razonamiento jurídico sea flojo.
- Que faltaran hechos del caso por preguntar.

Sigue siendo obligatorio el intake de `laboral.md`, la verificación real en
fuente allowlisted y el escalamiento a abogado. Esto es un cinturón de
seguridad: reduce el daño de un error, no autoriza a conducir peor.
