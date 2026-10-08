# Estados honestos

Vocabulario **cerrado**. Un estado no es una puntuación ni una impresión: es el
nombre exacto de lo que se sabe y de lo que no.

Principio de propagación: **se propagan como constante, no como default
calculado.** Ningún agente downstream puede subir el estado que otro emitió. Si
el buscador marcó `VIGENCIA_NO_VERIFICADA`, el agente de andamio lo transcribe;
no lo resuelve, no lo omite, no lo suaviza.

---

## Estados de la compuerta de fuentes

| Estado | Significa | No significa |
|---|---|---|
| `SUPERADA` | `vigencia` dice `superada`, `sustituida` o `abandonada` | Que se conozca el sucesor |
| `INTERRUMPIDA` | `vigencia` dice `interrumpida` | — |
| `SIN_EFECTOS` | `vigencia` dice `sin_efectos` | — |
| `VIGENCIA_NO_VERIFICADA` | `vigencia` dice `sin_evidencia_de_superacion` | **No** significa vigente. Nadie encontró nada, que no es haber verificado |
| `OBLIGATORIA` | `ambito` nacional, o de región/circuito que coincide con el del caso | — |
| `OBLIGATORIA_POR_ANALOGIA` | `ambito` de otro circuito o región | Que la analogía se sostenga — eso lo juzga el abogado |
| `ORIENTADORA` | `ambito = orientadora` | Que sea débil o descartable |
| `AMBITO_NO_DETERMINADO` | Se consultó `v_autoridad_criterio` pero no se pudo fijar el circuito del caso | Que el criterio no obligue. **No se usa sin motor**: ahí nadie consultó, y corresponde `SIN_MOTOR_DE_VERIFICACION` |
| `LITERAL` | La frase atribuida existe textualmente en el registro | Que sea pertinente al caso |
| `PARAFRASEADA` | La idea está, pero la frase citada no es textual | Que sea falsa |
| `ATRIBUCION_NO_LOCALIZADA` | La frase atribuida **no aparece** en el texto de la fuente | — |
| `PERTINENCIA_NO_EVALUADA` | El sistema no juzga si la fuente sostiene la premisa | Que no sirva |
| `SIN_MOTOR_DE_VERIFICACION` | No hay conector: los ejes de vigencia y ámbito no se pudieron correr | **No** significa `VIGENCIA_NO_VERIFICADA`. Ahí alguien consultó y no halló nada; aquí nadie consultó |
| `FUENTE_WEB_NO_COTEJADA` | La fuente se abrió en su portal oficial, no en la base | Que su vigencia o su ámbito se hayan verificado |
| `TEXTO_NO_COTEJADO` | Texto normativo constitucional o convencional reproducido sin cotejo contra fuente | Que sea inexacto. Tampoco que esté verificado |

> **No existe el veredicto `VIGENTE`.** El grafo nunca afirma que un criterio
> esté vivo: solo puede decir que no encontró evidencia de superación. Un estado
> `VIGENTE` sería una afirmación que ninguna consulta respalda, así que no está
> en el vocabulario.

### Veredictos globales de la compuerta

Los estados de arriba califican **una fuente**. Estos cuatro califican **la
corrida entera** y son igual de cerrados. Protocolo en `compuerta_fuentes.md`.

| Veredicto | Significa | No significa |
|---|---|---|
| `PASA` | Toda fuente con sus cinco ejes resueltos y sin nota ni falla | Que las fuentes sirvan para el caso — eso es pertinencia, y no se evalúa |
| `PASA CON NOTAS` | Hay notas que no bloquean, y se transcriben íntegras en el andamio | Que las notas sean menores |
| `FALLA` | Hallazgo **positivo** de problema en alguna fuente de la ruta | Que la ruta sea mala. Falla la fuente, no la ruta |
| `SIN_MOTOR` | Se corrió sin conector: los ejes 2 y 3 no se pudieron correr | **No** es `PASA`. Tampoco `FALLA`: nadie halló nada porque nadie consultó |

**`FALLA` gana sobre `SIN_MOTOR`.** Sin conector todavía se puede fallar — por
nota de superación vista en el portal oficial, o por `ATRIBUCION_NO_LOCALIZADA`
contra el material que aportó el abogado.

**Cero fuentes no es `PASA`.** Un dossier vacío cierra en `SIN_MOTOR` con el
conteo en cero. Un verde por no tener nada que reprobar es la forma más limpia de
mentir que tiene disponible una compuerta.

### Procedencia — de dónde vino cada fuente

Campo **obligatorio en toda ficha**, junto a los cinco veredictos. Sin él, el eje
de existencia no significa nada: una cita sin procedencia declarada es una cita
recordada hasta que se demuestre lo contrario (RH-17).

| Procedencia | Significa |
|---|---|
| `MOTOR` | La trajo una consulta al conector |
| `APORTADA` | La entregó el abogado — expediente, PDF, texto pegado |
| `WEB` | Se abrió en un portal oficial de la lista de `modo_sin_conector.md` |
| `MEMORIA_NORMATIVA` | Texto normativo reproducido sin cotejo. Solo CPEUM y tratados; nunca jurisprudencia |

### Estado del engrose — habla de la base, no del criterio

Se declara junto a la ficha cuando el abogado va a citar la sentencia de origen.

| Estado | Significa | No significa |
|---|---|---|
| `ENGROSE_EN_BASE` | `v_expediente_origen_tesis.estado_engrose` lo dice; el texto se puede leer y citar | Que el engrose sostenga la premisa |
| `ENGROSE_NO_ESTA_EN_LA_BASE` | El expediente está identificado (órgano, número/año, fecha) pero la sentencia no está descargada, **por diseño de la fuente**: la API SCJN solo publica Pleno y Salas | **No** que la sentencia no exista. Tampoco autoriza a citar el engrose: lo que se cita es la **ficha del expediente** |
| `EXPEDIENTE_NO_IDENTIFICADO` | No hay fila en `v_expediente_origen_tesis` (4.5% de las tesis) | Que la tesis no tenga asunto de origen: que `precedentes` no permitió extraerlo |

> **Nunca se degrada la obligatoriedad de un criterio por no tener su engrose
> descargado.** El ámbito lo fija `v_autoridad_criterio`, no la disponibilidad
> del texto. Los criterios sin engrose son precisamente los **17,538 obligatorios
> de circuito y 869 de región**: tratar su ausencia como debilidad invertiría el
> sentido del dato.

Sin conector no hay ficha: eso es `SIN_MOTOR_DE_VERIFICACION`, nunca
`EXPEDIENTE_NO_IDENTIFICADO` — ahí nadie consultó.

### Por qué `SIN_MOTOR_DE_VERIFICACION` es un estado aparte

`VIGENCIA_NO_VERIFICADA` es un resultado: se consultó `v_autoridad_criterio` y no
había evidencia de superación. `SIN_MOTOR_DE_VERIFICACION` es la ausencia de la
consulta.

Se parecen en pantalla y son opuestos en información. Reusar el primero cuando
corresponde el segundo sería mentir con el vocabulario propio de la skill, que es
la peor forma de mentir que tiene disponible este sistema.

### Por qué `VIGENCIA_NO_VERIFICADA` no bloquea

Medición 2026-08-19 sobre `v_autoridad_criterio` (311,738 criterios):

| Estado | Criterios | Obligatorios | Sin sucesor anclado |
|---|---|---|---|
| `sin_evidencia_de_superacion` | **305,055 (97.9%)** | 48,997 | 305,055 |
| `superada` | 6,362 | 1,284 | 157 |
| `interrumpida` | 182 | 155 | 86 |
| `abandonada` | 114 | 50 | 35 |
| `sustituida` | 23 | 23 | 22 |
| `sin_efectos` | 2 | 2 | 2 |

`VIGENCIA_NO_VERIFICADA` es el estado del **97.9%** del universo. Si bloqueara,
la compuerta reprobaría casi todo y el abogado la desactivaría al segundo uso —
que es el peor resultado posible para una compuerta de integridad.

Bloquean los **6,683 criterios (2.1%)** con hallazgo positivo de superación, de
los cuales **1,514 son obligatorios**. Ahí es donde está el daño real.

`PERTINENCIA_NO_EVALUADA` **siempre** acompaña a cada fuente. No es un caso
excepcional: es la constante que declara dónde termina la máquina. Se escribe
completa: `PERTINENCIA_NO_EVALUADA — corresponde al abogado`.

---

## Estados de proceso

| Estado | Significa | Dónde aparece |
|---|---|---|
| `SIN_CRITERIO_LOCALIZADO` | La búsqueda no arrojó criterios sobre el punto | Ficha de premisa, dossier |
| `SIN_CRITERIO_OBLIGATORIO_EN_EL_FORO` | Ninguna fuente del dossier obliga en el circuito del caso | Encabezado del reporte de compuerta |
| `ADVERSO_NO_BUSCADO` | La ronda de criterios adversos no se ha corrido | Bloquea el avance al andamio (RH-8) |
| `ADVERSO_A_CARGO_DEL_ABOGADO` | Sin motor, la ronda adversa se delegó expresamente y él lo sabe | No bloquea. **No** es `ADVERSO_NO_BUSCADO`: ese sigue bloqueando |
| `RUTA_NO_ATERRIZADA` | La ruta no nombra acto concreto ni porción normativa | Compuerta de aterrizaje, fase de rutas |
| `CIRCUITO_NO_DECLARADO` | No hay dato de circuito ni se dedujo. **Lleva su causa dicha**: *no se dedujo* y *no había con qué deducirlo* son cosas distintas y en la ficha se ven iguales | No bloquea; se advierte en el encabezado |
| `PLAZO_NO_CALCULADO` | El sistema no computa plazos | Ficha del caso, siempre |
| `REGLA_DE_PLAZO_LOCALIZADA` | Se localizó y transcribió el artículo de la Ley de Amparo que fija el plazo aplicable al acto descrito, con sus excepciones, sin calcular fecha | Ficha de viabilidad, eje Plazo — **siempre junto a** `PLAZO_NO_CALCULADO`, nunca lo sustituye. Si no se localizó ninguna regla aplicable, corresponde `SIN_CRITERIO_LOCALIZADO` en su lugar |
| `INTERPRETACION_PENDIENTE_DEL_ABOGADO` | Un paso interpretativo está vacío esperando al humano | Control difuso pasos 2-5, andamio puntos 3-6, ficha de viabilidad (huecos de conclusión de interés, definitividad y procedencia, RH-20) |
| `TEXTO_NO_DISPONIBLE_EN_BASE` | La tabla no guarda el cuerpo del documento | Fuentes de `corpus_iuris` sin texto |
| `CONTEO_NO_DEDUPLICADO` | La cifra viene de una vista relacional y no se pudo contar por criterio | Prohíbe presentar el número como cantidad de criterios (RH-19) |
| `MODO_SIN_CONECTOR` | La sesión corre sin acceso a las bases | Encabezado de toda ficha, todo reporte y el cierre (RH-18) |

---

## Formulaciones prohibidas

Ninguna de estas es un estado. Si aparece una, se sustituye por el estado que
corresponda:

- ❌ "parece seguir vigente" → `VIGENCIA_NO_VERIFICADA`
- ❌ "es difícil de verificar" → `VIGENCIA_NO_VERIFICADA` + qué consulta faltó
- ❌ "probablemente aplica al caso" → `PERTINENCIA_NO_EVALUADA`
- ❌ "es la tesis más fuerte para tu argumento" → viola RH-4, no se dice
- ❌ "criterio sólido / débil" → no es un eje mecánico, no se dice
- ❌ "plausible pero no confirmado" → no existe esa bandeja
- ❌ "no hay jurisprudencia sobre esto" cuando solo se consultó una tabla sin
  cuerpo de texto → `TEXTO_NO_DISPONIBLE_EN_BASE`, que no es ausencia del estándar
- ❌ "406 criterios respaldan esta ruta" contando filas de una vista con JOIN →
  cuenta criterios (RH-19) o marca `CONTEO_NO_DEDUPLICADO`
- ❌ "según recuerdo", "si mal no recuerdo", "hay una tesis que dice" → RH-17: o
  tiene procedencia declarada, o no entra
- ❌ "la tesis de rubro aproximado…" → un rubro aproximado es un rubro inventado
- ❌ un registro de siete dígitos sin línea de procedencia → se borra la ficha
  entera, no solo el registro
- ❌ "no pude verificar" a secas → `SIN_MOTOR_DE_VERIFICACION` y el conteo de
  cuántas fuentes quedaron así

---

## Por qué estados y no puntuaciones

Una puntuación inventada ("relevancia 8/10", "fuerza del criterio: alta") tiene
dos defectos: no se puede auditar y esconde un juicio interpretativo detrás de un
número que parece medido.

El estado dice exactamente qué se sabe. Cuando no se sabe, lo dice también, y esa
es la información útil — porque es donde el abogado tiene que mirar.
