# Sub-agentes de verificación

Cada sub-agente es independiente. El coordinador los invoca por delegación
(`send_to_parent` returns), no por API directa. Los resultados se consolidan
en el contexto del coordinador, que renderiza el informe final en
`/mnt/session/outputs/informe.md`.

## verificador-cendoj

- **Modelo**: claude-sonnet-4-6
- **Toolset**: agent_toolset_20260401 con `configs: [{name: web_search}, {name: web_fetch}, {name: write}]`
- **Dominio único permitido**: poderjudicial.es
- **Input que recibe**: cita normalizada en texto con campos {tipo, numero, fecha, sala, ponente, texto_original}
- **Política de fallos**: 3 reintentos con backoff 3 s / 8 s / 20 s
  ante 5xx o timeout. Tras los 3, devolver
  `dudosa_por_infraestructura` con código HTTP y nota de retry.
- **Trabajo**:
  1. Construye query para el buscador CENDOJ con los datos disponibles.
  2. Ejecuta web_search o web_fetch contra el buscador.
  3. Si encuentra resultado único: descarga el HTML/PDF, extrae texto, verifica que coincide con los datos de entrada.
  4. Si la cita original incluye texto literal entre comillas: busca el texto en el documento. Si aparece, `verificada`. Si no aparece literalmente pero el sentido coincide, `inexacta` con propuesta de redacción correcta. Si no se encuentra el sentido, `no_encontrada` con sugerencia.
  5. Si no encuentra resultado: `no_encontrada`. Sugerir alternativa por búsqueda semántica del holding si lo hay.
- **Estados posibles**: verificada, inexacta, no_encontrada,
  dudosa_por_contenido (ambigüedad real), dudosa_por_infraestructura
  (CENDOJ no responde tras 3 reintentos).
- **Output `send_to_parent`** (JSON): `{cita_original, estado, url_canonica, cita_literal_localizada, observaciones, sugerencia_alternativa}`

## verificador-tc

- **Modelo**: claude-sonnet-4-6
- **Toolset**: agent_toolset_20260401 con `configs: [{name: web_search}, {name: web_fetch}, {name: write}]`
- **Dominio único permitido**: hj.tribunalconstitucional.es
- **Input**: `{tipo, numero, año, tipo_proceso, texto_original}`
- **Trabajo**: idem CENDOJ adaptado al buscador del TC
- **Output**: igual estructura

## verificador-eurlex

- **Modelo**: claude-sonnet-4-6
- **Toolset**: agent_toolset_20260401 con `configs: [{name: web_search}, {name: web_fetch}, {name: write}]`
- **Dominios permitidos**: eur-lex.europa.eu, curia.europa.eu
- **Input**: `{tipo, asunto, año, nombre_caso, texto_original}`
- **Trabajo**: para jurisprudencia europea, búsqueda en CURIA por número de asunto. Para normativa europea, EUR-Lex por número y año.
- **Output**: igual estructura

## verificador-boe

- **Modelo**: claude-haiku-4-5 (búsqueda estructural, menos coste)
- **Toolset**: agent_toolset_20260401 con `configs: [{name: web_fetch}, {name: write}]`
- **Dominio único permitido**: boe.es
- **Input**: `{norma, articulo, fecha_referencia_escrito, texto_original}`
- **Trabajo**:
  1. Localiza la norma en el BOE consolidado.
  2. Verifica que el artículo citado existe.
  3. Verifica si el artículo estaba vigente en la fecha de referencia del escrito (importante: una demanda puede invocar la redacción vigente en la fecha del hecho, no la actual).
  4. Si hubo modificaciones intermedias, lista las versiones afectadas.
- **Output**: `{cita_original, estado, vigente_en_fecha, redaccion_vigente, modificaciones, url_consolidada, alerta_vigencia, observaciones}`

## verificador-doctrina

- **Modelo**: claude-opus-4-6 (semántico, más fino, más caro)
- **Toolset**: agent_toolset_20260401 completo (web_search, web_fetch, read, write)
- **Dominios permitidos**: dialnet.unirioja.es y catálogos editoriales reconocibles
- **Input**: `{autor, obra, año, pagina, editorial, cita_literal, texto_original}`
- **Trabajo**:
  1. Búsqueda en Dialnet (https://dialnet.unirioja.es) primero.
  2. Catálogo de editorial si está identificada (Aranzadi, Tirant, Civitas, Marcial Pons).
  3. Google Scholar como fallback.
  4. Si el escrito atribuye cita literal: comprobar paginación.
- **Output**: `{cita_original, estado, existencia_obra, cita_literal_localizada, paginacion_exacta, sugerencia_referencia_correcta, observaciones}`
- **NOTA**: la verificación de doctrina es la más difícil de automatizar. Si el sub-agente no consigue verificación firme, devolver `dudosa` con nota explícita "verificación bibliográfica manual recomendada".
