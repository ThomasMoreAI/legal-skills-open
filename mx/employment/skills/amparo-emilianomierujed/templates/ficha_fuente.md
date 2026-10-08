# Ficha de fuente — plantilla

## La línea de procedencia

**Toda ficha la lleva, en los cuatro bloques, antes que nada más.** Valores:
`MOTOR` · `APORTADA` · `WEB` · `MEMORIA_NORMATIVA` (definiciones en
`references/estados_honestos.md`).

**Una ficha sin procedencia es una ficha recordada, y se borra entera** — no se
le agrega la línea después (RH-17). Si no consta de dónde vino, no lo sabes.

Sin conector, además: ejes de vigencia y ámbito en `SIN_MOTOR_DE_VERIFICACION`, y
`FUENTE_WEB_NO_COTEJADA` pegado a toda ficha de origen web hasta el andamio.

---

## Criterio nacional (tesis / jurisprudencia)

```markdown
### {rubro}
- **Procedencia:** `{MOTOR | APORTADA | WEB}`{ · fuente: {url o descripción de lo que aportó el abogado}}
- **Registro:** {id_tesis} · [Ver en el Semanario](https://sjf2.scjn.gob.mx/detalle/tesis/{id_tesis})
- **Tesis:** {tesis_codigo} · {tipo_tesis} · {epoca} · {instancia}
- **Órgano:** {organo_juris}

**Veredictos de compuerta**
- Existencia: `EXISTE`
- Vigencia: `{VIGENCIA_NO_VERIFICADA | SUPERADA | INTERRUMPIDA | SUSTITUIDA | ABANDONADA | SIN_EFECTOS}` — método `{vigencia_metodo}`{, confianza {superacion_confianza} si es nota_scjn}{ · superada por el registro NNNNNNN}
- Ámbito: `{OBLIGATORIA | OBLIGATORIA_POR_ANALOGIA | ORIENTADORA | AMBITO_NO_DETERMINADO}` — {ambito literal} · art. 217 LA · circuito del caso: {ordinal}
- Correspondencia textual: `{LITERAL | PARAFRASEADA | ATRIBUCION_NO_LOCALIZADA}`
- Pertinencia: `PERTINENCIA_NO_EVALUADA — corresponde al abogado`

**Extracto textual**
> "{cita literal del texto, sin parafrasear}"

**Motivo del ámbito:** {ambito_motivo, copiado}
**Evidencia de vigencia:** {vigencia_evidencia, transcrita literal cuando hay superación}
```

### Variante sin conector

Las dos líneas que cambian:

```markdown
- Vigencia: `SIN_MOTOR_DE_VERIFICACION` — no se consultó el grafo{ · salvo nota de superación visible en la ficha oficial → `SUPERADA`, método `nota_web`, nota transcrita literal}
- Ámbito: `SIN_MOTOR_DE_VERIFICACION` — no se consultó `v_autoridad_criterio`; circuito del caso: `CIRCUITO_NO_DECLARADO`
```

Existencia, correspondencia textual y pertinencia **se llenan igual**. El eje 4
es el que sostiene el modo: se coteja contra el texto que el abogado entregó o
que se abrió en el portal, con el mismo rigor.

## Sentencia / engrose

```markdown
### {expediente} — {organo_resolvio} ({fecha_resolucion})
- **Procedencia:** `{MOTOR | APORTADA | WEB}`
- **Tipo:** {tipo_asunto}
- **Ponencia:** {ministro_ponente}
- **Resolución:** {resolucion}
- **Documento oficial:** [{url_docx}]({url_docx})

**Veredictos de compuerta**
- Existencia: `EXISTE`
- Correspondencia textual: `{LITERAL | PARAFRASEADA | ATRIBUCION_NO_LOCALIZADA}`
- Pertinencia: `PERTINENCIA_NO_EVALUADA — corresponde al abogado`

**Fragmento**
> "{snippet o substr acotado}"
```

Si `url_docx` es NULL se dice; no se inventa liga.

## Voto particular / concurrente / de minoría

Igual que la sentencia, más:

- **Procedencia:** `{MOTOR | APORTADA | WEB}`
- **Autor del voto:** {v_votos_meta.autor_voto} — **quien formula el voto**, no el ponente del engrose
- **Clasificación:** {particular | concurrente | de minoría}
- **Advertencia obligatoria:** un voto no vincula a nadie. Es argumento, y así se presenta.

## Fuente internacional

```markdown
### {título / caso / artículo}
- **Procedencia:** `{MOTOR | APORTADA | WEB | MEMORIA_NORMATIVA}`
- **Fuente:** {Corte IDH | Tratado | Comité X | CIDH | OIT | Relatoría | UHRI}
- **Identificador:** {serie C No. | símbolo ONU | No. de convenio}
- **Link oficial:** [{descriptivo}]({url})

**Veredictos de compuerta**
- Existencia: `EXISTE`
- Correspondencia textual: `{LITERAL | TEXTO_NO_DISPONIBLE_EN_BASE}`
- Pertinencia: `PERTINENCIA_NO_EVALUADA — corresponde al abogado`

**Estándar**
> "{cita literal SOLO si la tabla tiene cuerpo de texto}"
```

**Si la tabla no guarda el texto** (`oit_convenios`, `relatores_informes`,
`cidh_informes`, filas de `comite_dictamenes` con `texto_completo` NULL): ficha
con link, **sin comillas**, y la línea literal *"el texto íntegro no está en la
base; verifica en el link"*.

**Si viene de UHRI**: se cita el original en inglés y se marca la traducción como
propia.

## Artículo de ley federal (`leyes_federales`)

Mapeo de los cinco veredictos, distinto del de tesis: una ley no se supera y
no tiene circuito. Detalle completo en
`references/compuerta_fuentes.md` ("Fuentes normativas — artículo de ley
federal").

```markdown
### Ley de Amparo, art. {n}
- **Procedencia:** `{MOTOR | WEB | APORTADA}`{ · fuente: {url o descripción}}
- **Ley:** {nombre completo} · clave `{id_ley}`

**Veredictos de compuerta**
- Existencia: `EXISTE`
- Vigencia de la norma: `{vigente | revisar_abrogacion | abrogada}` — `leyes.estatus`, transcrito literal
- Ámbito: `N/A — norma federal, aplicación general`
- Correspondencia textual: `{LITERAL | PARAFRASEADA | ATRIBUCION_NO_LOCALIZADA}`
- Pertinencia: `PERTINENCIA_NO_EVALUADA — corresponde al abogado`

**Texto**
> "{artículo completo, con todas sus fracciones — no se resume}"
```

Sin conector: procedencia `WEB` (portal `diputados.gob.mx`), vigencia de la
norma no verificable — se transcribe la versión que muestra el portal al
momento de la consulta y se arrastra `FUENTE_WEB_NO_COTEJADA` hasta la ficha
final, igual que cualquier otra fuente de origen web.

### Texto normativo reproducido de memoria

Única forma de `MEMORIA_NORMATIVA`, y **solo** para texto normativo de la
Constitución o de un tratado ratificado. Jurisprudencia, sentencias, rubros y
registros, jamás (`references/modo_sin_conector.md` §7):

```markdown
> "{texto del artículo}"
> — {instrumento}, art. {n} · Procedencia: `MEMORIA_NORMATIVA` · `TEXTO_NO_COTEJADO`
> Verifica contra el DOF o el portal del instrumento antes de citarlo en el escrito.
```
