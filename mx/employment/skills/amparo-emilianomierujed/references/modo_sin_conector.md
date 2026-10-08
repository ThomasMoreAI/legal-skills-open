# Modo sin conector

La skill corre de dos formas. Este archivo describe la segunda y **es el único
lugar donde vive esa descripción**: los agentes lo citan, no lo reescriben.

| | **Con conector** | **Sin conector** |
|---|---|---|
| Origen de las fuentes | 750,000+ documentos vía `run_sql` | Lo que aporta el abogado + portales oficiales |
| Vigencia y obligatoriedad | Grafo de superación y `v_autoridad_criterio` | `SIN_MOTOR_DE_VERIFICACION` |
| Método, fases, checkpoints | Íntegros | Íntegros |

**El método es el mismo. Lo que cambia es qué se puede verificar.** No hay una
versión reducida de la skill: hay una capacidad ausente, y se dice cuál es.

---

## 1 · Detección

**Primer acto de la sesión, antes de la Fase 0.**

Verifica si están disponibles las tools del conector — `list_databases`,
`run_sql`, `fts_help`. **No asumas el prefijo**: el mismo servidor se registra
como `mcp__legal__*` en configuración local y `mcp__claude_ai_Consulto__*` como
conector de Claude.ai. Busca las tools por su nombre final, nunca por el prefijo
escrito en duro.

Declara el resultado en una línea y **fíjalo para toda la sesión**:

```
Modo: SIN CONECTOR — vigencia y obligatoriedad no se van a poder verificar.
Todo lo demás corre igual.
```

Si el abogado esperaba tener conector, esa línea es su aviso de que algo falló en
la instalación. Por eso va arriba y no al final.

**No vuelvas a detectar a media corrida.** Un modo que cambia entre fases produce
un reporte donde unas fichas están verificadas y otras no, sin que se note cuál
es cuál.

---

## 2 · Qué corre y qué no

| Fase | Sin conector |
|---|---|
| 0 · Registro del caso | **Igual**, salvo el circuito: ver §6 |
| 1 · Rutas de ataque | **Igual.** No dependía del motor en nada |
| 2 · Recolección | **Cambia de naturaleza**: acopio y web, no recuperación. Ver §4 y §5 |
| 2.5 · Compuerta | **Ejes 1 y 4 sí. Ejes 2 y 3 no.** Veredicto global `SIN_MOTOR` |
| 3-bis · Control difuso | Sin par convencional. Los pasos del abogado, iguales. Ver §7 |
| 3 · Andamio | **Igual en estructura.** El material que va bajo los huecos arrastra sus estados degradados |
| 4 · Contraste | **Igual**, salvo que no puede traer criterios adversos que el abogado no tenga |

Los checkpoints no se relajan. La compuerta no se salta. Lo único que se degrada
son los dos ejes que necesitan las bases.

---

## 3 · Procedencia — la línea que sostiene todo

Toda ficha declara de dónde vino: `MOTOR` · `APORTADA` · `WEB` ·
`MEMORIA_NORMATIVA`. Definiciones en `estados_honestos.md`.

Sin motor, **la procedencia es lo primero que se escribe en una ficha**, antes
que el rubro. Una ficha sin procedencia es una ficha recordada, y una ficha
recordada se borra entera — no se le agrega la línea después (RH-17).

> **El modo de fallo número uno de este modo** es el registro recordado. El
> criterio existe, el tema es correcto, el rubro suena bien, y el registro está
> mal en un dígito. Nada dentro del modelo se siente mal al escribirlo. Por eso
> la regla no es "ten cuidado": es que sin línea de procedencia la ficha no
> existe.

---

## 4 · Protocolo de acopio

Sustituye a la recolección. El material lo tiene el abogado: expediente,
constancias, PDFs del Semanario, tesis que ya copió, la ley aplicable.

1. **Pídelo por ruta, no en abstracto.** "Para la ruta A necesito lo que tengas
   sobre la distinción por sexo en el acceso a la pensión" funciona; "mándame lo
   que tengas" no.
2. **Fichea lo que llegue** con `templates/ficha_fuente.md`, procedencia
   `APORTADA`.
3. **Ejes 2 y 3**: `SIN_MOTOR_DE_VERIFICACION`, sin excepción, aunque el
   documento que él pegó diga que es jurisprudencia firme.
4. **Eje 4 se corre de verdad.** Es el eje que sí funciona sin bases: cotejas que
   cada frase que se le atribuye a esa fuente exista literalmente en el texto que
   él entregó. `LITERAL` / `PARAFRASEADA` / `ATRIBUCION_NO_LOCALIZADA`.
5. **Lo que no llegue se dice.** `SIN_CRITERIO_LOCALIZADO` no aplica aquí: no
   buscaste y no encontraste, simplemente no te lo dieron. Se pide otra vez o se
   anota el hueco.

El eje 4 es el corazón del modo sin conector. Atribuirle a una tesis una frase
que no dice es el error más frecuente y el más caro en audiencia, y para
atraparlo no hacen falta las bases: hace falta el texto y la disciplina de
compararlo.

---

## 5 · Protocolo web

Permitido, con una asimetría que no se negocia:

> ## La web puede condenar. Nunca puede absolver.

**Puede:**

- Confirmar que un registro existe y traer su rubro y su texto → procedencia
  `WEB`, eje 1 `EXISTE`.
- Aportar el texto para correr el eje 4.
- **Transcribir una nota de superación visible en la ficha oficial** → veredicto
  `SUPERADA`, método `nota_web`, con la nota transcrita literal.

> **Medido el 2026-08-20: esta última vía casi nunca se va a poder ejecutar.**
> `sjf2.scjn.gob.mx` devuelve **403** a la herramienta de fetch, y la búsqueda web
> no expone el apartado «Nota:» de la ficha — ni buscándolo a propósito con los
> números exactos de la contradicción. La regla se queda escrita porque cuando la
> nota **sí** aparezca hay que actuar sobre ella; pero **no cuentes con
> encontrarla**, y sobre todo no leas su ausencia como señal. Así se midió en la
> simulación sin conector del 2026-08-20.

**No puede:**

- Emitir ningún veredicto de vigencia por **ausencia** de nota. Que la ficha no
  diga nada no es información: es que no la buscaste donde se guarda.

  > Probado con un caso real: el registro **2019531** —jurisprudencia de la
  > Segunda Sala, ámbito **nacional**, superada con confianza 0.95— sale en web
  > con su rubro y su fecha correctos y **ninguna señal de estar superada**. Un
  > sistema que dedujera «no hay nota, luego sigue viva» habría dado por vigente
  > un criterio nacional muerto, y lo habría hecho con apariencia de rigor. Esto
  > es lo que la asimetría existe para impedir.
- Determinar ámbito de obligatoriedad. El art. 217 LA aplicado a un circuito
  concreto no se lee de una ficha del Semanario.
- Sustituir `v_autoridad_criterio` por un razonamiento propio sobre el órgano
  emisor. Eso es el antipatrón 7.

**Dominios permitidos** — fuera de esta lista, no se cita:

`sjf2.scjn.gob.mx` · `scjn.gob.mx` · `corteidh.or.cr` · `oas.org` ·
`ohchr.org` · `diputados.gob.mx` · `dof.gob.mx`

> **`sjf2.scjn.gob.mx` está cerrado al acceso automatizado.** Devuelve **403** en
> todas sus rutas, incluida la raíz (medido 2026-08-20). Las dos cosas que el
> protocolo esperaba de él —confirmar que un criterio existe y traer su texto—
> **no son ejecutables**.
>
> La búsqueda web sí encuentra el rubro de una tesis, pero en sitios de terceros:
> despachos, boletines, PDFs universitarios. **No se citan, y no se añaden a la
> lista.** Son copias sin control de versión, y meterlas reintroduce justo la
> cita incomprobable que la compuerta existe para cerrar.
>
> **Consecuencia:** sin conector, la jurisprudencia entra prácticamente solo como
> `APORTADA`. Pídesela al abogado; él la tiene. Lo que no se hace es rellenar el
> hueco con un rubro encontrado en un blog.
>
> Los demás dominios sí responden: `diputados.gob.mx` entregó la LISSSTE completa
> y su art. 136 se citó literal. El texto normativo y el eje 4 están vivos.

Toda fuente de origen web arrastra `FUENTE_WEB_NO_COTEJADA` hasta el andamio.
Ningún agente downstream se la quita.

**Los PDF se leen bajando el archivo, no convirtiendo la página.** Las leyes de
`diputados.gob.mx` vienen en PDF y la conversión automática a texto devuelve
basura binaria. Se descarga y se lee el archivo. Verificado el 2026-08-20 con la
LISSSTE (128 págs.): el texto del art. 136 se recuperó literal, con sus dos
fracciones derogadas en 2023 — dato que cambia el caso y que sí está al alcance
sin conector.

**La escalera de búsqueda de `consultas_mcp.md` sigue sirviendo aquí**: los
términos precisos primero, el `OR` amplio al final. Es método de búsqueda, no
sintaxis de SQL.

---

## 6 · El circuito, sin grafo

Sin conector no puedes consultar `grafo.entidad_circuito`. Consecuencias:

1. **Pregunta el municipio siempre**, no solo cuando la entidad esté partida
   entre circuitos — porque sin el grafo **no sabes cuáles están partidas**. Ese
   es el punto: el dato que se pierde sin motor es el saber que hacía falta
   preguntar.
2. **No traduzcas entidad a circuito de memoria.** Ni de una lista escrita en
   ningún archivo de esta skill: esas listas son ilustración, no fuente.
3. Estado: `CIRCUITO_NO_DECLARADO`, **con la razón dicha**:

   ```
   CIRCUITO_NO_DECLARADO — no hay motor para resolverlo, no es que falte el dato.
   Municipio registrado: {municipio}. Verifícalo tú antes de invocar obligatoriedad.
   ```

4. Efecto en cascada: sin circuito, el eje 3 quedaría muerto de todos modos. Se
   dice una vez, en el encabezado, y no se repite en cada ficha.

---

## 7 · Texto normativo de memoria

Única excepción a RH-17.

**Sí:** Constitución, tratados ratificados por México (CADH, PIDCP, PIDESC, CEDAW,
Convención de los Derechos del Niño y demás), en su texto normativo.

**No, jamás:** jurisprudencia, tesis, rubros, registros, sentencias, votos, leyes
secundarias, reglamentos, criterios administrativos. Nada que tenga número de
registro o de expediente.

Marca obligatoria: `TEXTO_NO_COTEJADO`, con esta forma:

```
> "{texto del artículo}"
> — {instrumento}, art. {n} · Procedencia: MEMORIA_NORMATIVA · TEXTO_NO_COTEJADO
> Verifica contra el DOF o el portal del instrumento antes de citarlo en el escrito.
```

Por qué la excepción existe: sin ella la Fase 3-bis queda inservible, y el
parámetro de regularidad constitucional es justo el material que un modelo
reproduce con fidelidad alta y que el abogado puede cotejar en treinta segundos.
Por qué no se extiende a la jurisprudencia: un rubro mal recordado se ve idéntico
a uno correcto, y nadie lo coteja en treinta segundos.

---

## 8 · La ronda adversa

RH-8 sigue vigente: sin ronda adversa no se avanza al andamio.

Sin motor, la ronda cambia de ejecutor pero no desaparece:

1. Corre la búsqueda adversa en web, si la ruta lo permite, **con los términos
   del lado contrario** — no con los tuyos negados.
2. **Pregúntale al abogado, expresamente**, qué le van a oponer, y dile que sin
   conector esa búsqueda queda de su lado:

   > "Sin las bases no puedo barrer los criterios que juegan en contra de esta
   > ruta. ¿Qué crees que te van a oponer? Y si tienes algo en contra, pásamelo:
   > lo fichero igual que lo demás."

3. Estado: `ADVERSO_A_CARGO_DEL_ABOGADO`. **No bloquea.**
4. Si **no se le preguntó**: `ADVERSO_NO_BUSCADO`, y sí bloquea. La delegación
   vale porque él la sabe; una delegación silenciosa es solo un hueco.

---

## 9 · El cierre contable

Al final de la compuerta y al final de la corrida. **Con números, no con
adjetivos** — el hueco se cuenta, no se describe:

```
━━━ Sin verificar ━━━
No se verificó vigencia de {N} criterios.
No se verificó obligatoriedad de {N} criterios.
Circuito del caso: no resuelto.

Estos dos ejes se resuelven contra 311,738 criterios calificados y 6,683 con
hallazgo positivo de superación — 1,514 de ellos obligatorios (medición
2026-08-19, ver `estados_honestos.md`).
━━━━━━━━━━━━━━━━━━━━
```

Se escribe igual cuando N = 0. Un dossier vacío es el caso donde más importa
decirlo.

**Lo que este bloque no es:** un anuncio. No lleva llamada a la acción, no dice
"suscríbete", no adjetiva lo que falta. Dice cuántos criterios quedaron sin
verificar y contra qué se habrían verificado. Un abogado sabe leer eso solo, y si
se le vende encima deja de creerle al resto del reporte.
