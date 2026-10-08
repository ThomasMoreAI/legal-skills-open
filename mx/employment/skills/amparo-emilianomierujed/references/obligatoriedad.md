# Obligatoriedad y vigencia — la consulta manda, no el criterio

Este archivo cubre los dos ejes **mecánicos** de la compuerta de fuentes que
dependen de la base `grafo`. Determinar si un criterio obliga y si sigue vivo es
recuperación y cotejo, no interpretación: se consulta y se copia.

Fundamento normativo del ámbito: **artículo 217 de la Ley de Amparo**.

> **Requiere motor.** Todo lo mecánico de este archivo depende de la base
> `grafo`. **Sin conector, los ejes 2 y 3 salen `SIN_MOTOR_DE_VERIFICACION`** —
> no `VIGENCIA_NO_VERIFICADA` ni `AMBITO_NO_DETERMINADO`, que significan *se
> consultó y no se halló*. Ver `references/modo_sin_conector.md`.
>
> **El contenido metodológico sigue sirviendo sin conector**: el art. 217 LA, la
> tabla de traducción de ámbito y las trampas de lectura son lo que el abogado
> necesita para verificarlo a mano. Lo que no puede hacerse sin motor es
> automatizarlo — y por eso el sistema declara el hueco en vez de llenarlo.

---

## Regla base: no deduzcas el ámbito

Con los `id_tesis` que vayan a citarse, se consulta `v_autoridad_criterio` y se
usa lo que devuelva:

```sql
SELECT id_tesis, tipo_tesis, caracter, ambito, ambito_motivo, vigencia,
       vigencia_evidencia, vigencia_metodo, superada_por, superacion_confianza,
       epoca, sistema_epoca
FROM v_autoridad_criterio
WHERE id_tesis IN ('2024847', '2027280', '2007679');
```

**Por qué la consulta y no el razonamiento:** una medición de grounding del
2026-08-01 encontró que el **53%** de los criterios citados presentaba tesis
**aisladas** como
obligatorias, aun cuando la versión anterior de la skill ya ordenaba lo contrario
en prosa. Razonarlo bien no bastó. Por eso el ámbito se copia, no se infiere.

---

## Eje ÁMBITO

**Copia `ambito` literalmente.** Viene derivado de forma determinista de
`tipo_tesis`, `instancia`, `organo_juris` y `tesis_codigo`. Si dice
`orientadora`, el criterio es orientador aunque venga de la Primera Sala y
aunque encaje perfecto con el caso.

Valores posibles de `ambito`:
`nacional` · `nacional:competencia-economica` · `region:CENTRO-NORTE` ·
`region:CENTRO-SUR` · `circuito:<ORDINAL>` · `materia-electoral` · `orientadora`

Traducción a veredicto de la compuerta:

| `ambito` devuelto | Veredicto | Condición |
|---|---|---|
| `nacional` (o `nacional:*` aplicable) | `OBLIGATORIA` | siempre |
| `region:X` / `circuito:X` que **coincide** con el del caso | `OBLIGATORIA` | circuito del caso determinado |
| `region:X` / `circuito:X` que **no coincide** | `OBLIGATORIA_POR_ANALOGIA` | circuito del caso determinado |
| `orientadora` | `ORIENTADORA` | siempre |
| cualquiera, con circuito del caso **sin determinar** | `AMBITO_NO_DETERMINADO` | falta el dato |

**`AMBITO_NO_DETERMINADO` no bloquea la búsqueda.** Si no se pudo fijar el
circuito del caso, se busca igual y se entrega todo, con la advertencia escrita:
*"Circuito no determinado: los criterios nacionales se presentan como
obligatorios y los de circuito quedan sin calificar para tu foro."* Nunca se
cancela ni se pospone una búsqueda por falta de este dato.

**`ambito_motivo` está escrito para citarse**: es el "y por qué" de la ficha.

### Lo que el grafo NO decide

El grafo dice **si un criterio obliga y a quién**. No sabe cuál es el circuito
del caso, ni si una analogía se sostiene, ni cuál criterio conviene. Eso es del
abogado (RH-1, RH-4).

En particular, **`OBLIGATORIA_POR_ANALOGIA` es una etiqueta de ámbito, no un
juicio de que la analogía funcione.** El sistema marca que el criterio obliga en
otro circuito; si los supuestos y la razón jurídica son los mismos lo decide
quien litiga.

---

## Eje VIGENCIA

### `vigencia` nunca dice "vigente"

- `sin_evidencia_de_superacion` → significa que **no se encontró nota de
  superación**, no que el criterio esté confirmado vivo. Nunca se presenta como
  garantía. Veredicto de compuerta: `VIGENCIA_NO_VERIFICADA`.
  Es el estado del **97.9%** del universo (305,055 de 311,738, medición
  2026-08-19), así que **no bloquea**: genera nota, no falla. Lo que bloquea es
  el hallazgo positivo de superación.
- `revisar` → hay señal sin clasificar. Se advierte. (Hoy no hay ninguna: la cola
  de desambiguación las resolvió, pero el estado existe y puede reaparecer.)
- `superada` / `interrumpida` / `sustituida` / `abandonada` / `sin_efectos` →
  veredicto homónimo, y **falla la compuerta**. Son 6,683 criterios en total
  (2.1%), de los cuales **1,514 obligatorios** (medición 2026-08-19). Ahí está el
  daño real que la compuerta existe para atrapar.

### La regla del estado sobre el vacío

**`superada_por` vacío NO significa vigente.** La vista puede decir `superada`,
`interrumpida`, `sustituida` o `abandonada` y dejar `superada_por` en blanco: el
estado salió de la evidencia, pero el ancla no resolvió a qué `id_tesis` apunta
la nota.

Son **302 criterios, 190 de ellos obligatorios** (medición 2026-08-19; la
medición anterior, 2026-08-06, daba 599 y 245 — la cola de desambiguación avanzó,
y por eso estas cifras se remiden, no se recuerdan). Leer ese blanco como "no hay
superación" es el peor error posible aquí, porque **invierte el sentido del
dato**.

> **El estado manda sobre el vacío.**

Veredicto correcto: `SUPERADA — sucesor no identificado`, que **falla la
compuerta**. Nunca `VIGENCIA_NO_VERIFICADA`.

`vigencia_evidencia` **nunca viene vacía** en estos casos (verificado 2026-08-19:
0 de 302): siempre hay algo que transcribir aunque no se consiga el registro del
sucesor.

### Declara `vigencia_metodo`, no solo el estado

Dice de dónde salió la conclusión:

| `vigencia_metodo` | Qué significa |
|---|---|
| `nota_scjn` | Nota de la propia Corte — el más fuerte, normalmente una contradicción resuelta |
| `regex_evidencia` | Voz pasiva detectada en `precedentes` |
| `apartamiento_texto` | Un órgano declara en su tesis que se aparta de un criterio anterior |
| `regla_determinista` | Estado por defecto: **nadie encontró nada**, que no es lo mismo que haber verificado |

### `nota_scjn` tiene dos calidades: léelas en `superacion_confianza`

- **`0.95`** → la nota declara que *este* criterio contendió en la contradicción.
  Es la Corte hablando de su vigencia. Se cita como tal.
- **`0.8`** → la nota menciona una contradicción resuelta sobre el mismo tema
  **sin decir que esta tesis fuera parte de ella**. Suele ser superación material
  igualmente (una jurisprudencia de Sala desplaza a un criterio de circuito),
  pero **no es una declaración formal sobre este criterio**. Con `0.8` se dice
  con esas palabras y se transcribe `vigencia_evidencia` para que el abogado
  juzgue.

**Nunca se presenta un `0.8` como si la Corte hubiera declarado superado el
criterio.**

### Advertencia obligatoria de ausencia de evidencia

Cuando `vigencia` sea `sin_evidencia_de_superacion` **y** la tesis sea de Novena
Época o anterior, se dice explícitamente que la ausencia de evidencia no equivale
a vigencia confirmada y que corresponde verificar en el Semanario.

Son **18,208 criterios obligatorios pre-Novena**. Bajo el artículo 217 de la Ley
de Amparo siguen obligando mientras no se superen: **no se descartan por
antigüedad**, se transcriben con la reserva dicha.

---

## Rescate del sucesor: dos vías, y solo valen si devuelven UNA fila

Las tasas de recuperación se midieron sobre la población de 599 casos que existía
el 2026-08-06: recuperaban **163 (27%)**, y 42 de los 245 obligatorios. **La
población cambió a 302 el 2026-08-19, así que esas tasas hay que remedirlas.** La
regla operativa, en cambio, no depende de la tasa y sigue igual: una fila =
sucesor; más de una fila = no hay sucesor identificado.

```sql
-- Vía 1 — clave de tesis citada en la evidencia. Recupera 114. Es la buena.
SELECT id_tesis, tesis_codigo, rubro FROM tesis
WHERE tesis_codigo = 'PR.P.CN. J/11 P (11a.)' AND id_tesis <> '2030502';
--  -> 2026999, fila única. Ese es el sucesor de 2030502.

-- Vía 2 — rubro citado en la evidencia. Recupera solo 49, y exige el rubro COMPLETO.
SELECT id_tesis, tesis_codigo, rubro FROM tesis
WHERE rubro LIKE '{rubro entero tal como aparece en la evidencia}%'
  AND id_tesis <> '{la tesis que se está analizando}';
```

El `id_tesis <> ...` no es adorno: sin él una tesis se recupera a sí misma como
su propio sucesor.

### Por qué la vía 2 casi nunca sirve, y cuándo miente

La evidencia se trunca a **520 caracteres**, así que el rubro suele venir
cortado; y los rubros de la SCJN comparten encabezados largos. En **331 de los
599** el `LIKE` devuelve **más de una fila**.

Caso real: el rubro que cita la evidencia de la 2026753, cortado a sus primeros
105 caracteres (`DEMANDA DE AMPARO DIRECTO PRESENTADA A TRAVÉS DEL TRIBUNAL
ELECTRÓNICO PARA LA JUSTICIA ADMINISTRATIVA (TEJA)%`), devuelve **2029051 y
2029052** — dos jurisprudencias del mismo Pleno Regional, consecutivas. Con el
rubro completo (250 caracteres) devuelve solo la 2029051, que es la correcta.

> **Si vuelve más de una fila, no elijas: no hay sucesor identificado.** Elegir
> la primera es fabricar una cita con apariencia de rigor, que es peor que el
> vacío.

### Nunca uses el número de contradicción para identificar al sucesor

Es tentador —la evidencia casi siempre lo trae— y está mal: los Plenos Regionales
numeran sus contradicciones por su propio índice, así que
`precedentes LIKE '%contradicción de criterios 169/2024%'` devuelve tesis de
facturas electrónicas, de competencia territorial y de carpetas de investigación
a la vez.

El número sirve para **citar** la contradicción en la ficha, nunca para resolver
a qué tesis apunta.

### Un sucesor rescatado así lo identificó la máquina leyendo prosa — y hay que decirlo

Se escribe con estas palabras:

> *"superada; el sucesor (registro NNNNNNN) se identificó leyendo la nota de la
> Corte, no por el grafo"*

Ese eslabón es la lectura de un texto, no una arista determinista, y quien va a
firmar el escrito tiene derecho a saber cuál de los dos está citando.

### Cuando no hay rescate, no se completa el hueco

Se dice que el criterio está superado, se transcribe `vigencia_evidencia` literal
y se remite al Semanario. Hay notas que simplemente no nombran al sucesor
(*"quedó superada"*, o remiten a un recurso de queja del índice del propio
tribunal). Ahí un registro plausible inventado es exactamente el error que esta
skill existe para evitar.

---

## Época: ordena y advierte, nunca excluyas

Un criterio viejo no deja de obligar por serlo. Filtrar por época descartaría en
silencio criterios obligatorios vigentes, y eso viola RH-4 (no priorizar) y la
regla de bitácora.

- Preferencia de presentación: 11ª y 12ª; la 10ª sigue citable; de 9ª o anterior,
  con la reserva expresa del apartado de vigencia.
- **`orden_epoca` solo es comparable dentro del mismo `sistema_epoca`.** El TEPJF
  numera sus épocas por su cuenta y su "Tercera Época" no es la de la SCJN.
  Nunca se ordena ni filtra mezclando los dos sistemas.
- En 11ª época la jurisprudencia de la SCJN también se forma **por precedentes**
  (sentencias con votación calificada): no se descarta un criterio por no decir
  "por reiteración".

---

## Un criterio superado nunca entra al andamio

Aunque encaje perfecto con el caso y aunque su `ambito` diga `nacional`. Va al
apartado de riesgos: es lo que la contraparte usará para tumbar el escrito si se
cita, y es lo que hay que saber que ya no sirve.

Si el criterio superado era el único material localizado, se dice así —
`SIN_CRITERIO_LOCALIZADO` para la premisa — en vez de rellenar con él.
