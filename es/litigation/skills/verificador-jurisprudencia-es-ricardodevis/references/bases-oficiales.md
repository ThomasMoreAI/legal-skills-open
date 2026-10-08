# Bases oficiales de consulta

## CENDOJ — Centro de Documentación Judicial del CGPJ

- URL buscador: https://www.poderjudicial.es/search/indexAN.jsp
- Cobertura: TS, AN, TSJ, AP, juzgados que han optado por publicar
- Acceso: público, sin coste, sin autenticación
- Método de búsqueda: parámetros GET con número de recurso, fecha, tipo de órgano
- Formato de resultado: HTML con enlace a PDF de la sentencia
- Limitación: el buscador puede ser inconsistente con fechas; siempre intentar primero por número de recurso si está disponible

## Tribunal Constitucional

- URL buscador: https://hj.tribunalconstitucional.es/es-ES/Busqueda
- Cobertura: STC, ATC desde 1980
- Acceso: público, sin coste
- Búsqueda por número/año o por palabras clave del fallo

## EUR-Lex y CURIA

- EUR-Lex: https://eur-lex.europa.eu (normativa + jurisprudencia)
- CURIA: https://curia.europa.eu (jurisprudencia TJUE específica)
- Búsqueda por número de asunto (C-XXX/YY o T-XXX/YY)
- Idiomas: castellano disponible para sentencias relevantes

## BOE — Boletín Oficial del Estado

- URL: https://www.boe.es
- API documentada: https://www.boe.es/datosabiertos/
- Para normativa consolidada (vigente con todas las modificaciones): https://www.boe.es/buscar/act.php?id=<ID>
- Para texto histórico de un artículo en fecha concreta: usar el enlace "versiones" del BOE consolidado
- El BOE marca claramente la vigencia y modificaciones

## DOUE

- URL: https://eur-lex.europa.eu/oj/direct-access.html
- Búsqueda por número y año

## Boletines autonómicos

- País Vasco: BOPV (https://www.euskadi.eus/bopv2)
- Cataluña: DOGC
- Madrid: BOCM
- (añadir más según necesidad real del despacho)

## REGLAS DE USO

1. **Dominio autorizado**: las URLs que devuelvas como `url_canonica` en el informe deben pertenecer exclusivamente a uno de los dominios listados arriba.

2. **NO uses**: agregadores, espejos, blogs jurídicos, foros, wikis, ni resúmenes de terceros. Aunque el contenido parezca correcto.

3. **Si una base oficial está caída o el buscador da error**: marca la cita como `dudosa` con nota "verificación pendiente, base no disponible en momento de consulta". NO inventes resultado.

4. **Verificación de literalidad**: cuando el escrito transcribe texto entre comillas atribuyéndolo a una sentencia, el sub-agente debe descargar el texto completo de la sentencia y comprobar que la cita literal aparece. Si no aparece exactamente o sustancialmente, marcar como `inexacta`.
