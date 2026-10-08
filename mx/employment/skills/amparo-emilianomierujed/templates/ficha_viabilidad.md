# Ficha de viabilidad — {acto reclamado, breve}

> Todo lo de "Datos declarados" y "Foro" lo dijo el abogado. Nada se dedujo ni
> se completó. Los huecos de conclusión (interés, definitividad, procedencia)
> son suyos: el sistema no los llena (RH-1, RH-5, RH-20). El plazo se
> localiza; nunca se calcula (RH-13).

**Modo de conexión:** `{CON CONECTOR | SIN CONECTOR}` — declarado al arranque
y fijo para toda la sesión (RH-18).
**Compuerta:** `{PASA | PASA CON NOTAS | FALLA | SIN_MOTOR}` — ver
`reporte-compuerta-viabilidad.md`

---

## Datos declarados por el abogado

- **Quejoso:**
- **Acto reclamado:** {el acto concreto, con fecha, expediente y órgano}
- **Autoridad responsable:**
- **Autoridad ejecutora:** {si la hay}
- **Fecha de notificación / conocimiento:**
- **¿Interpuso ya algún recurso o medio de defensa contra este acto?:**
  {sí/no, cuál, ante quién, fecha, si sigue pendiente — tal como lo dijo}
- **Pretensión:**
- **Material propio:**

## Foro

- **Entidad:**
- **Municipio:** {obligatorio si la entidad devuelve `alcance = 'parcial'`.
  Sin conector se pregunta siempre}
- **Circuito:** {ordinal} — {de su perfil | del estado que indicó | resuelto
  con `municipio_circuito` | `CIRCUITO_NO_DECLARADO`}

{sin conector, la línea de circuito es siempre:}
```
CIRCUITO_NO_DECLARADO — no hay motor para resolverlo, no es que falte el dato.
Municipio registrado: {municipio}. Verifícalo tú antes de invocar obligatoriedad.
```

---

## Eje — Plazo

**Regla localizada:** `REGLA_DE_PLAZO_LOCALIZADA`

> "{artículo 17 de la Ley de Amparo, transcrito literal y completo, con todas
> sus fracciones y excepciones}"
> — Ley de Amparo, art. 17 · Procedencia: `{MOTOR | WEB}`{ ·
> `FUENTE_WEB_NO_COTEJADA` si WEB}

**Cómputo:** `PLAZO_NO_CALCULADO` — el cómputo, incluidos días inhábiles y el
criterio de inicio, es responsabilidad del abogado (RH-13). Este documento no
contiene, en ningún lugar, una fecha de vencimiento.

## Eje — Interés jurídico o legítimo

**▶ TÚ CONCLUYES** — `INTERPRETACION_PENDIENTE_DEL_ABOGADO`

Material verificado disponible (orden: obligatoriedad → vigencia → circuito →
fecha):

- **LA art. 5 fracc. I** — `MOTOR` · `EXISTE` · `LITERAL`
  > "{extracto textual}"

- **Reg. {id_tesis}** — `MOTOR` · `{OBLIGATORIA | ORIENTADORA | ...}` ·
  `{VIGENCIA_NO_VERIFICADA | ...}` · `LITERAL`
  > "{extracto textual}"
  [Ver en el Semanario](https://sjf2.scjn.gob.mx/detalle/tesis/{id_tesis})
  pertinencia: `PERTINENCIA_NO_EVALUADA — corresponde al abogado`

## Eje — Principio de definitividad

**▶ TÚ CONCLUYES** — `INTERPRETACION_PENDIENTE_DEL_ABOGADO`

Material verificado disponible:

- **LA art. 61, fracción sobre definitividad** — {fracción transcrita}
- {fichas de tesis sobre las excepciones reconocidas, si se localizaron}

## Eje — Procedencia (causales de improcedencia)

**▶ TÚ CONCLUYES** — `INTERPRETACION_PENDIENTE_DEL_ABOGADO`

Material verificado disponible:

- **LA art. 61** — {texto completo de las 23 fracciones, transcrito}
- {fichas de tesis sobre la o las causales que podrían tocar este acto}

---

## Material adverso verificado

*(causales, criterios o argumentos que juegan en contra de la viabilidad —
RH-8, adaptado a este modo; sin consejo sobre cómo responderlos)*

{fichas}

{si la ronda adversa no se corrió: `ADVERSO_NO_BUSCADO`, y este documento no
cierra el checkpoint 2 mandatorio}

{sin conector, si se le delegó expresamente:
`ADVERSO_A_CARGO_DEL_ABOGADO`, con las palabras que se le dijeron transcritas}

---

## Sin verificar

{obligatorio sin conector, al final de la ficha. Con números, no con
adjetivos. Se escribe igual cuando N = 0}

```
━━━ Sin verificar ━━━
No se verificó vigencia de {N} criterios.
No se verificó obligatoriedad de {N} criterios.
No se verificó vigencia de la norma citada ({N} artículos de la Ley de Amparo).
Circuito del caso: no resuelto.
━━━━━━━━━━━━━━━━━━━━
```

---

## Autochequeo

- [ ] Los tres huecos de conclusión (interés, definitividad, procedencia)
      están vacíos con `INTERPRETACION_PENDIENTE_DEL_ABOGADO` — ninguno tiene
      una frase que concluya a favor o en contra
- [ ] El eje de plazo tiene `REGLA_DE_PLAZO_LOCALIZADA` **y**
      `PLAZO_NO_CALCULADO` — ninguna fecha de vencimiento aparece en ningún
      lugar del documento
- [ ] Toda fuente tiene sus veredictos completos y su procedencia declarada
      (RH-6, RH-17)
- [ ] La ronda adversa se corrió o se delegó expresamente (RH-8)
- [ ] El modo del encabezado es el que se declaró al arranque (RH-18)
- [ ] Sin conector: ningún artículo de ley aparece sin procedencia `WEB` o
      `MOTOR` declarada; ninguna tesis aparece sin `SIN_MOTOR_DE_VERIFICACION`
      en vigencia y ámbito
