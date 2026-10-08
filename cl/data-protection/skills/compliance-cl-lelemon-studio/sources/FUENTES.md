# Fuentes oficiales (corpus primario)

Objetivo: que la auditoría sea **reproducible y contrastada contra la ley vigente, nada inventado**.
Toda afirmación legal de la skill debe poder rastrearse a uno de estos archivos + el artículo.
Si algo no se puede verificar contra estos textos, se marca `[verificar contra fuente oficial]`.

> Descargado: **2026-06-20**. Re-descargable con los comandos de abajo (User-Agent de navegador).

| Archivo | Norma | idNorma | Tipo | SHA-256 (trunc.) | Fuente oficial |
|---|---|---|---|---|---|
| `ley-21719-diariooficial.pdf` | Ley 21.719 Datos Personales | 1209272 | **PDF texto COMPLETO** | `a760962c…` | Diario Oficial 13-12-2024 |
| `ley-21719-datos.xml` | Ley 21.719 (estructura) | 1209272 | XML abreviado | `4b60e4c8…` | Ley Chile (BCN) |
| `ley-21595-delitos-economicos.xml` | Ley 21.595 Delitos Económicos | 1195119 | XML | `17cac690…` | Ley Chile (BCN) |
| `ley-20393-resp-penal-pj.xml` | Ley 20.393 Resp. Penal PJ | 1008668 | XML | `35d67a14…` | Ley Chile (BCN) |
| `ley-19628-consolidada.xml` | Ley 19.628 (texto base que la 21.719 modifica) | 141599 | XML | `4b4a6d85…` | Ley Chile (BCN) |
| `clausulas-modelo-transferencia-economia.pdf/.txt` | Cláusulas Contractuales Modelo (transferencia internacional) | RAEX202503748 | **PDF + texto** | `55f78aef…` | Diario Oficial 19-12-2025 |

## Códigos que NO se versionan acá (se descargan, no se redistribuyen)

Este repo es **público**, y la licencia de redistribución del texto de Ley Chile **no está confirmada con la
BCN**. Los textos de la 21.719/21.595/20.393/19.628 vienen de arriba por decisión previa; para los códigos
—que son mucho más extensos— se optó por **no publicarlos y dejar la receta de descarga**, que es
reproducible y no redistribuye nada. Bajarlos es una línea y quedan igual de citables.

| Norma | idNorma | SHA-256 esperado (trunc.) | Sostiene |
|---|---|---|---|
| Código Tributario (DL 830) | **6374** | `5951bfb4…` | art. 17 inc. 2° + art. 200 — conservación de libros y el plazo de revisión del SII |
| Código del Trabajo (DFL 1) | **207436** | `b66efa69…` | art. 62 — libro auxiliar de remuneraciones (desde 5 trabajadores) |

```bash
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/124.0 Safari/537.36"
curl -L -A "$UA" "https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma=6374"   -o codigo-tributario-dl830.xml
curl -L -A "$UA" "https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma=207436" -o codigo-del-trabajo.xml
sha256sum codigo-*.xml   # deben partir con los prefijos de la tabla
```

**Si trabajas en Lelemon hay un atajo mejor:** el corpus legal interno ya los tiene **por artículo, en
Markdown, con frontmatter de vigencia e historial de versiones** (`normas/leyes/dl-830-codigo-tributario/`,
`normas/laboral-previsional/dfl-1-codigo-trabajo/`). Es más cómodo de citar que el XML crudo. Es privado, así
que no se referencia por URL acá.

## Notas de validez (IMPORTANTE)
- **La 21.719 MODIFICA la Ley 19.628**: el articulado sustantivo de datos (consentimiento,
  encargado, transferencias, Agencia, sanciones) entra en vigor **1-dic-2026** y se lee del **PDF del
  Diario Oficial** (`ley-21719-diariooficial.pdf`), que es el texto completo. El `ley-19628-consolidada.xml`
  aún NO integra esas modificaciones (vigencia futura) → no usarlo como operativo de la parte nueva.
- Los **XML de Ley Chile (opt=7) son ABREVIADOS** (encabezados/estructura). Para texto íntegro usar el
  PDF del Diario Oficial o el visor de BCN.
  **Excepción comprobada (14-ago-2026):** los de los dos códigos que se agregaron ahora **sí traen el texto
  íntegro** de cada artículo, verificado buscando los incisos citados abajo. Si a futuro un XML no trae el
  texto, no asumas que ninguno lo trae: revisa el archivo.
- La **21.595 ya está vigente** (modifica la 20.393; rige desde 1-sep-2024).

### Por qué están el Código Tributario y el del Trabajo (14-ago-2026)

Una **retención** de datos personales no se sostiene sola: el art. 7 romanito ii) de la 21.719 dice que no
procede la supresión cuando el tratamiento es necesario para cumplir una **obligación legal**, pero la
obligación la pone *otra* ley. Sin estos dos textos, toda negativa a suprimir datos contables o de
remuneraciones quedaba citada de memoria — y el art. 11 exige que la negativa sea **fundada**.

Los tres artículos que sostienen los plazos, **verificados palabra por palabra contra el XML de la BCN**
(descargado con la receta de abajo; el texto no se versiona en este repo público):

- **Código Tributario art. 17 inc. 2°** — *"Los libros de contabilidad deberán ser llevados en lengua
  castellana […] debiendo ser conservados por los contribuyentes, junto con la documentación
  correspondiente, mientras esté pendiente el plazo que tiene el Servicio para la revisión de las
  declaraciones."* El plazo no está acá: está en el art. 200.
- **Código Tributario art. 200** — tres años desde que expiró el plazo legal de pago; **seis** para
  impuestos sujetos a declaración *"cuando ésta no se hubiere presentado o la presentada fuere
  maliciosamente falsa"*.
- **Código del Trabajo art. 62** — *"Todo empleador con cinco o más trabajadores deberá llevar un libro
  auxiliar de remuneraciones, el que deberá ser timbrado por el Servicio de Impuestos Internos"*, y las
  remuneraciones que figuren ahí son las únicas imputables como gasto en la contabilidad.

⚠️ **Dos límites que hay que respetar al citarlos:**
1. El art. 62 aplica **desde 5 trabajadores**. Bajo ese umbral no hay obligación de llevar el libro y la
   retención se sostiene solo en el art. 17 del Tributario — que sí aplica siempre, porque el gasto por
   remuneraciones es parte de la contabilidad. Al fundar una negativa, **citar ambos**.
2. **Ninguno de los dos fija un plazo laboral de conservación en años.** El plazo que se le informa al
   titular es siempre el tributario del art. 200. No inventar uno laboral.

## Pendientes de incorporar (con URL, aún no descargados)
- **DS 662/2025** (reglamento del Modelo de Prevención de Infracciones, Min. Hacienda/Economía):
  estaba en toma de razón en Contraloría — verificar publicación en Diario Oficial.
- **Guía oficial de implementación**: https://wikiguias.digital.gob.cl/es/datos-personales/guia-datos-personales

> Cláusulas modelo de transferencia: ✅ ya descargadas
> (`clausulas-modelo-transferencia-economia.pdf`, Diario Oficial 19-12-2025).

## Cómo re-descargar (reproducibilidad)
```bash
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/124.0 Safari/537.36"
# Texto completo Ley 21.719 (PDF Diario Oficial)
curl -L -A "$UA" "https://www.diariooficial.interior.gob.cl/publicaciones/2024/12/13/44023/01/2583630.pdf" -o ley-21719-diariooficial.pdf
# XML estructurado (cambiar idNorma): 21719=1209272, 21595=1195119, 20393=1008668, 19628=141599
curl -L -A "$UA" "https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma=1209272" -o ley-21719-datos.xml
# Códigos que sostienen los plazos de conservación (traen texto íntegro)
curl -L -A "$UA" "https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma=6374"   -o codigo-tributario-dl830.xml
curl -L -A "$UA" "https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma=207436" -o codigo-del-trabajo.xml
# Cláusulas contractuales modelo (transferencia internacional, Min. Economía)
curl -L -A "$UA" "https://www.diariooficial.interior.gob.cl/publicaciones/2025/12/19/44328/01/2742586.pdf" -o clausulas-modelo-transferencia-economia.pdf
# Verificar integridad
sha256sum *.pdf *.xml
```

## Regla de uso para la skill
1. Antes de afirmar algo legal, búscalo en estos archivos (PDF completo > XML).
2. Cita siempre **ley + artículo + archivo fuente**.
3. Si no está en el corpus o no es verificable, dilo: `[verificar contra fuente oficial / abogado]`.
4. Nunca uses un blog/fuente secundaria como base de una afirmación normativa en el output final.
