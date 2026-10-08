# Compuerta de fuentes — protocolo

Parada obligatoria entre la recolección y el andamio. No se salta (RH-16).

## Qué problema resuelve

**Con conector**, el motor no inventa fuentes: todo sale de `run_sql` contra
bases reales. El riesgo no es la cita fabricada de la nada. Es otro, y es peor
porque tiene apariencia de rigor:

1. Citar un criterio **superado**.
2. Citar uno que **no obliga** en el circuito del caso, presentándolo como
   obligatorio.
3. Atribuirle a una fuente una frase que **no dice**.

**Sin conector reaparece un cuarto riesgo, y pasa al primer lugar:**

0. Citar un criterio **recordado** — que existe, cuyo tema es correcto, cuyo
   rubro suena bien, y cuyo registro está mal en un dígito.

Ese es el modo de fallo número uno del modo sin conector, y por eso el eje 1
cambia de pregunta: de "¿la trajo `run_sql`?" a "¿de dónde vino, y consta?".

Los cuatro son verificables sin interpretar. Por eso hay compuerta.

Lo que la compuerta **no** hace: juzgar si la fuente sostiene el argumento del
abogado. Eso es interpretar (RH-5).

---

## Orden de los ejes — es obligatorio y no se altera

Cada eje se resuelve completo antes de pasar al siguiente. **No se cotejan frases
de una fuente cuya vigencia todavía no tiene veredicto** — el mismo error que ARS
documenta en su Gray-Zone Prevention Rule.

### Eje 1 — Existencia y procedencia

**La pregunta no es "¿la trajo `run_sql`?" sino "¿de dónde vino, y consta?".**

| Procedencia | Origen | Veredicto |
|---|---|---|
| `MOTOR` | La trajo `run_sql` | `EXISTE` |
| `APORTADA` | La entregó el abogado | `EXISTE` |
| `WEB` | Se abrió en un portal oficial de la lista de `modo_sin_conector.md` §5 | `EXISTE` + `FUENTE_WEB_NO_COTEJADA` |
| `MEMORIA_NORMATIVA` | Texto de la Constitución o de un tratado, reproducido sin cotejo | `TEXTO_NO_COTEJADO` |

Nada recordado, nada deducido, nada "que suele decirse". La única excepción es
`MEMORIA_NORMATIVA`, acotada al texto normativo constitucional o convencional y
prohibida para todo lo que tenga registro o expediente (RH-17).

**Una ficha sin línea de procedencia es una ficha recordada y se borra entera.**
No se le agrega la línea después: si no consta de dónde vino, no lo sabes.

### Fuentes normativas — artículo de ley federal (`leyes_federales`)

Los cuatro ejes de abajo (2 a 5) están descritos para tesis y jurisprudencia,
apoyados en `v_autoridad_criterio`. Un artículo de ley (típicamente de la Ley
de Amparo, localizado por el modo `viabilidad`) **no tiene ese vocabulario**:
no se supera, no tiene circuito. Mapeo mecánico, sin forzar los veredictos de
tesis:

| Eje | Cómo se resuelve para un artículo de ley |
|---|---|
| 1 · Existencia y procedencia | Igual que cualquier fuente: fila encontrada en `articulos` → `MOTOR`; abierto en `diputados.gob.mx`/`dof.gob.mx` → `WEB` + `FUENTE_WEB_NO_COTEJADA`; aportado por el abogado → `APORTADA` |
| 2 · Vigencia | **No es el vocabulario de tesis.** Se transcribe literal `leyes.estatus` (`vigente` \| `revisar_abrogacion` \| `abrogada`). `revisar_abrogacion` o `abrogada` es hallazgo positivo de problema y **falla la compuerta**, igual que `SUPERADA` en una tesis |
| 3 · Ámbito | `N/A — norma federal, aplicación general`. Una ley federal no tiene circuito que declarar; no se usa `OBLIGATORIA`/`ORIENTADORA` ni se fuerza el art. 217 LA, que es para jurisprudencia |
| 4 · Correspondencia textual | Igual que cualquier fuente: se coteja la cita contra `articulos.texto` con `substr()`/`snippet()`. `LITERAL` / `PARAFRASEADA` / `ATRIBUCION_NO_LOCALIZADA` |
| 5 · Pertinencia | Igual: `PERTINENCIA_NO_EVALUADA — corresponde al abogado`, constante |

Sin conector, el eje 2 no tiene con qué correr (`leyes_federales` no es
accesible sin motor): la versión del artículo que se transcribe es la que
muestra el portal oficial en el momento de la consulta, y arrastra
`FUENTE_WEB_NO_COTEJADA` — no se inventa un veredicto de vigencia de la norma
que nadie consultó.

### Eje 2 — Vigencia

Consulta a `v_autoridad_criterio`. Reglas completas en
`references/obligatoriedad.md`. **Requiere motor**; sin él, ver "Los ejes 2 y 3
sin conector" más abajo.

Veredictos: `SUPERADA` · `INTERRUMPIDA` · `SUSTITUIDA` · `ABANDONADA` ·
`SIN_EFECTOS` · `VIGENCIA_NO_VERIFICADA`

**No existe el veredicto `VIGENTE`**: el grafo nunca afirma que un criterio esté
vivo, solo que no encontró evidencia de superación.

**El estado manda sobre el vacío (RH-7).** Si `vigencia` declara superación y
`superada_por` viene NULL, el veredicto es `SUPERADA — sucesor no identificado`,
**no** `VIGENCIA_NO_VERIFICADA`. Son 302 criterios en esa situación (medición
2026-08-19), 190 de ellos obligatorios. Leer ese blanco como "no hay superación"
invierte el sentido del dato.

Cada veredicto se acompaña de `vigencia_metodo` y, si es `nota_scjn`, de
`superacion_confianza`. Un `0.8` nunca se presenta como declaración formal de la
Corte sobre ese criterio.

### Eje 3 — Ámbito de obligatoriedad

Consulta a `v_autoridad_criterio`, campo `ambito`, **copiado literalmente**.
Tabla de traducción a veredicto en `references/obligatoriedad.md`.

Veredictos: `OBLIGATORIA` · `OBLIGATORIA_POR_ANALOGIA` · `ORIENTADORA` ·
`AMBITO_NO_DETERMINADO`

Siempre se nombra el circuito y el fundamento (art. 217 LA) — RH-10.

### Eje 4 — Correspondencia textual

Este es el eje nuevo, y el que atrapa el fraude más difícil de ver.

Para cada frase que el dossier atribuye a una fuente, se coteja contra el texto
recuperado:

| Veredicto | Condición |
|---|---|
| `LITERAL` | La frase aparece textualmente en `texto`, `texto_completo`, `contenido` o el campo que corresponda |
| `PARAFRASEADA` | La idea está en el texto pero la frase citada no es textual |
| `ATRIBUCION_NO_LOCALIZADA` | La frase **no aparece** en el texto de la fuente |

Cómo se hace, mecánicamente: se recupera el pasaje con `substr()` o `snippet()`
sobre el registro concreto y se compara la cadena. No se compara "el sentido" —
eso sería interpretar.

**Una llamada por tabla fuente, no por cita.** Si el dossier tiene varias citas
de `tesis`, tráelas todas en un solo `run_sql` con
`WHERE id_tesis IN ('2024847', '2027280', ...)` (mismo patrón que
`references/obligatoriedad.md`), y compara cada frase contra su fila
correspondiente ya en memoria. Repite por cada tabla fuente distinta
(`sentencias`, `metadata_unificada`, etc.) — no una consulta por cita.

**`ATRIBUCION_NO_LOCALIZADA` es fallo de compuerta.** Es exactamente el caso en
que un escrito cita una tesis real diciendo algo que la tesis no dice, que es la
forma de error más difícil de detectar para un juez y la más costosa cuando la
detecta.

Caso especial: fuentes de `corpus_iuris` en tablas **sin cuerpo de texto**
(`oit_convenios`, `relatores_informes`, `cidh_informes`, filas de
`comite_dictamenes` con `texto_completo` NULL). Ahí no se puede cotejar nada:
veredicto `TEXTO_NO_DISPONIBLE_EN_BASE`, la fuente se entrega como ficha con link
y **sin comillas**. Nunca se entrecomilla lo que no se leyó.

### Eje 5 — Pertinencia: NO SE EVALÚA

Constante, en toda ficha, sin excepción:

```
pertinencia: PERTINENCIA_NO_EVALUADA — corresponde al abogado
```

Decidir si un criterio sostiene la premisa del caso es el acto interpretativo
central del litigio. El sistema no lo emite nunca, y lo declara en vez de fingir
que la pregunta no existe.

---

## Los ejes 2 y 3 sin conector

Protocolo completo en `references/modo_sin_conector.md`. Lo que la compuerta
necesita saber:

**Ambos salen `SIN_MOTOR_DE_VERIFICACION`.** No `VIGENCIA_NO_VERIFICADA`, no
`AMBITO_NO_DETERMINADO`. Esos dos significan *se consultó y no se halló*; aquí
nadie consultó nada, y usar el vocabulario de la verificación para nombrar su
ausencia es la mentira más fácil de cometer en este modo.

### La asimetría de la web

> ## La web puede condenar. Nunca puede absolver.

Una nota de superación **visible** en la ficha oficial del Semanario produce
veredicto `SUPERADA`, método `nota_web`, con la nota transcrita literal. Eso
falla la compuerta igual que si viniera del grafo.

**En la práctica va a pasar poco:** el portal bloquea el acceso automatizado y la
búsqueda web no expone ese apartado (medición 2026-08-20). La vía se conserva
para cuando la nota sí aparezca. Lo que **no** cambia por eso es la otra mitad de
la regla — al contrario, la refuerza: si la condena casi nunca llega por web, leer
su ausencia como absolución sería justo el error más caro.

La **ausencia** de nota no produce ningún veredicto de vigencia. Que la ficha no
diga nada no es información: es que no la buscaste donde se guarda.

La asimetría es deliberada, y es lo que permite abrir la web sin reintroducir el
fraude que la compuerta existe para cerrar. Un hallazgo positivo se sostiene
solo; una ausencia solo vale si el barrido fue exhaustivo, y el de web no lo es.

El eje 3 no tiene equivalente web: el art. 217 LA aplicado a un circuito concreto
no se lee de una ficha del Semanario, y sin `entidad_circuito` el circuito del
caso además está en `CIRCUITO_NO_DECLARADO`. Sale `SIN_MOTOR_DE_VERIFICACION`
siempre, sin excepción.

**Los ejes 1 y 4 corren completos**, y el 4 con el mismo rigor que con motor: se
coteja contra el texto que el abogado entregó o que se abrió en el portal.

---

## Prohibición de zona gris

Formulaciones **prohibidas** en el reporte de compuerta:

- ❌ "es difícil verificar si sigue vigente" → `VIGENCIA_NO_VERIFICADA`, y se
  nombra qué consulta faltó
- ❌ "parece aplicable al caso" → eso es interpretar; no se dice
- ❌ una bandeja de "plausibles pero no confirmados"
- ❌ cotejar correspondencia textual antes de dar veredicto de vigencia
- ❌ dejar una fuente sin alguno de los cuatro veredictos
- ❌ dejar una fuente sin línea de procedencia (RH-17)
- ❌ "verificación no disponible en este modo" a secas → el hueco se cuenta, no
  se describe: cuántas fuentes, en el bloque contable de `modo_sin_conector.md` §9
- ❌ `VIGENCIA_NO_VERIFICADA` sin haber consultado el grafo → eso es
  `SIN_MOTOR_DE_VERIFICACION`

**Toda fuente del dossier tiene los cuatro veredictos explícitos**, más su línea
de procedencia. Una fuente sin veredicto completo no pasa, aunque sea obviamente
buena.

---

## Veredicto global y qué hace el checkpoint

| Veredicto | Condición | Efecto |
|---|---|---|
| `PASA` | Toda fuente: `EXISTE` + ámbito determinado + `LITERAL`, y ninguna condición de nota ni de falla | Avanza al andamio |
| `PASA CON NOTAS` | Hay `VIGENCIA_NO_VERIFICADA`, `ORIENTADORA`, `OBLIGATORIA_POR_ANALOGIA`, `AMBITO_NO_DETERMINADO`, `PARAFRASEADA` o `TEXTO_NO_DISPONIBLE_EN_BASE` | Avanza; **las notas se transcriben íntegras en el andamio** |
| `FALLA` | Alguna fuente de la ruta tiene `SUPERADA`, `INTERRUMPIDA`, `SUSTITUIDA`, `ABANDONADA`, `SIN_EFECTOS` o `ATRIBUCION_NO_LOCALIZADA` | **No se construye andamio** |
| `SIN_MOTOR` | Se corrió sin conector: los ejes 2 y 3 no se pudieron correr | Avanza; se imprime en el reporte, en el encabezado del andamio y en el cierre contable |

### Por qué `SIN_MOTOR` es un veredicto y no una nota

Sin él, la compuerta no tiene salida correcta sin conector. `PASA` con los ejes 2
y 3 en blanco es un falso verde — el peor resultado posible para una compuerta,
porque el abogado lee un visto bueno que nadie dio. `FALLA` por no haberlos
corrido reprueba todas las corridas siempre, y una compuerta que reprueba
siempre deja de usarse.

`SIN_MOTOR` dice lo que pasó: el método corrió completo, dos de los cinco ejes
no tenían con qué correr, y aquí está el conteo.

**`FALLA` gana sobre `SIN_MOTOR`.** Sin conector se puede fallar: por nota de
superación en web, o por `ATRIBUCION_NO_LOCALIZADA` contra el material aportado.
Eso importa — es lo que impide que el modo sin conector sea decorativo.

**Cero fuentes no es `PASA`.** Un dossier vacío es `SIN_MOTOR` con el conteo en
cero. Un verde por no tener nada que reprobar es la forma más limpia de mentir.

### Señal aparte: `SIN_CRITERIO_OBLIGATORIO_EN_EL_FORO`

Cuando **ninguna** fuente del dossier tiene ámbito `OBLIGATORIA` para el circuito
del caso —todo es orientador o por analogía— eso se declara en el **encabezado**
del reporte, no enterrado entre las notas.

No es una falla: es un hecho sobre el terreno, y de los más útiles que la
compuerta puede entregar. Cambia la estrategia entera —hay que construir la
analogía explícitamente, o asumir que se litiga sin criterio vinculante— y no
puede quedar en la misma cubeta que una nota de paráfrasis.

Verificado en prueba (2026-08-19): un caso de prisión preventiva oficiosa en el
Octavo Circuito devolvió 7 criterios pertinentes y **cero obligatorios en el
foro** — tres jurisprudencias de los circuitos Noveno y Décimo, cuatro aisladas.
`PASA CON NOTAS` a secas no comunicaba esa situación.

**Sin conector esta señal no se emite nunca.** Requiere haber barrido el ámbito
de todo el dossier, que es justo lo que el eje 3 no pudo hacer. Su ausencia no
significa que sí haya criterio obligatorio en el foro: significa que no se sabe.

Bloquea el **hallazgo positivo de problema**, no la ausencia de confirmación.
`VIGENCIA_NO_VERIFICADA` es el estado del 97.9% del universo (ver
`references/estados_honestos.md`): si bloqueara, la compuerta reprobaría todo y
dejaría de usarse, que es la peor forma de fallar para una compuerta.

**Nota reforzada obligatoria:** cuando una fuente con `VIGENCIA_NO_VERIFICADA`
sea de **Novena Época o anterior**, la nota dice expresamente que la ausencia de
evidencia no equivale a vigencia confirmada y que corresponde verificar en el
Semanario. Son 18,208 criterios obligatorios pre-Novena que siguen obligando bajo
el art. 217 LA: no se descartan por antigüedad, se transcriben con la reserva.

`FALLA` no tiene escotilla (RH-16). Las salidas son:

1. Volver a la fase de recolección a buscar sustituto para la fuente que falló.
2. Cambiar de ruta.
3. Que el abogado decida seguir con la fuente marcada — decisión suya, que se
   registra literalmente en el reporte con sus palabras y bajo su nombre, y que
   **no cambia el veredicto**: la ficha sigue diciendo `SUPERADA`.

La opción 3 existe porque el abogado manda. Pero el sistema no borra el hallazgo
para acomodarla, y el andamio se construye con la marca visible.

---

## Bucle de corrección acotado

Máximo **3 rondas** de vuelta a recolección por la misma ruta. Después de la
tercera, se entrega lo que hay con las fuentes marcadas y se le dice al abogado
que esa ruta no tiene sustento localizable en las bases — que es información útil
sobre la ruta, no un fracaso de la búsqueda.
