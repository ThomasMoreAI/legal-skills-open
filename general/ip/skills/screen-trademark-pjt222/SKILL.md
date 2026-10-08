---
name: screen-trademark-pjt222
title: Screen Trademark
description: Screen a proposed trademark for conflicts and distinctiveness before filing. Covers trademark database searches (TMview, WIPO Global Brand Database, USPTO TESS), distinctiveness analysis using the Abercrombie spectrum, likelihood of confusion assessment using DuPont factors and EUIPO relative grounds, common law rights evaluation, and goods/services overlap analysis. Produces a conflict report with a risk matrix. Use before adopting a new brand name, logo, or slogan — distinct from patent prior art search, which uses different databases, legal frameworks, and analysis methods.
author: pjt222
author_url: https://github.com/pjt222/agent-almanac/tree/main/i18n/es/skills/screen-trademark
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: es
---

# Screen Trademark

Cribar una marca propuesta por conflictos y evaluar su distintividad antes de presentarla. Busca en registros de marcas, evalúa la marca en el espectro Abercrombie, analiza la probabilidad de confusión con marcas previas y produce un reporte de conflicto con calificaciones de riesgo accionables.

## Cuándo Usar

- Antes de adoptar un nuevo nombre de marca, nombre de producto o marca de servicio
- Cuando se hace rebranding o se expande a nuevas clases de bienes/servicios
- Antes de presentar una solicitud de marca (nacional, UE o internacional)
- Al evaluar objetivos de adquisición con portafolios de marcas
- Antes de lanzar un producto en un nuevo mercado geográfico con branding existente
- Cuando se recibe una carta de cease-and-desist y necesitas evaluar la exposición

## Entradas

- **Requerido**: Marca propuesta (marca de palabra, marca figurativa o ambas)
- **Requerido**: Bienes y/o servicios que la marca cubrirá (descripción en lenguaje plano)
- **Requerido**: Alcance geográfico (EE.UU., UE, países específicos o global)
- **Opcional**: Clases de Clasificación de Niza si ya son conocidas
- **Opcional**: Fecha pretendida de primer uso (relevante para prioridad de derecho consuetudinario en EE.UU.)
- **Opcional**: Marcas o brands competidoras conocidas en el espacio
- **Opcional**: Si la marca es una marca de palabra, marca figurativa o compuesta

## Procedimiento

### Paso 1: Definir la Marca y los Bienes/Servicios

Establecer exactamente qué se está cribando y en qué clases.

1. Registrar la marca propuesta precisamente:
   - Marca de palabra: el texto como aparecerá (la mayúscula importa para elementos figurativos)
   - Marca figurativa: describir los elementos visuales, colores, estilización
   - Marca compuesta: tanto los elementos de palabra como figurativos juntos
2. Describir los bienes y/o servicios en lenguaje plano
3. Identificar las clases de Clasificación de Niza aplicables:
   - Usar TMclass (https://tmclass.tmdn.org/) para buscar clases
   - Buscar por palabra clave para encontrar la clase correcta y términos aceptables
   - La mayoría de las marcas necesitan 1-3 clases; identificar todas las relevantes
   - Clases adyacentes donde podría surgir confusión (p. ej., Clase 9 software y Clase 42 SaaS)
4. Documentar el alcance geográfico:
   - EE.UU. (USPTO), UE (EUIPO), internacional (WIPO Madrid) o oficinas nacionales específicas
   - Anotar diferencias jurisdiccionales: EE.UU. es first-to-use; UE es first-to-file

**Esperado:** Un registro claro de la marca, su descripción de bienes/servicios, clases de Niza y jurisdicciones objetivo. Esto define el alcance de búsqueda para todos los pasos subsiguientes.

**En caso de fallo:** Si la clasificación de Niza es ambigua (los bienes/servicios abarcan múltiples clases o no encajan claramente en una), errar del lado de incluir más clases. Cribar un alcance más amplio es más seguro que perder un conflicto en una clase adyacente.

### Paso 2: Buscar Bases de Datos de Marcas

Buscar marcas idénticas y similares entre registros.

1. Buscar **marcas idénticas** primero (coincidencia exacta):
   - **TMview** (https://www.tmdn.org/tmview/): UE y oficinas nacionales participantes
   - **WIPO Global Brand Database** (https://branddb.wipo.int/): registros internacionales
   - **USPTO TESS / Trademark Center** (https://tsdr.uspto.gov/): registros y solicitudes de EE.UU.
   - **Oficinas nacionales** según sea relevante: DPMAregister (Alemania), UKIPO (Reino Unido), CIPO (Canadá)
2. Buscar **marcas similares** — expandir la búsqueda para encontrar:
   - Equivalentes fonéticos: marcas que suenan parecidas ("Kool" vs. "Cool", "Lyft" vs. "Lift")
   - Equivalentes visuales: marcas que se ven parecidas ("Adidaz" vs. "Adidas")
   - Transliteraciones y traducciones de la marca
   - Marcas con prefijos/sufijos comunes añadidos o eliminados
   - Plurales, posesivos y abreviaciones
3. Filtrar resultados por:
   - Estado: marcas vivas/registradas y solicitudes pendientes (ignorar muertas/canceladas)
   - Bienes/servicios: clases de Niza iguales o relacionadas (del Paso 1)
   - Geografía: jurisdicciones objetivo
4. Para cada conflicto potencial, registrar:
   - Texto de la marca y número de registro/solicitud
   - Nombre del propietario y jurisdicción
   - Clases de Niza y descripción de bienes/servicios
   - Estado (registrada, pendiente, opuesta) y fechas
   - Si la marca es idéntica o similar (y cómo: fonética, visual, conceptual)

**Esperado:** Una lista de marcas potencialmente conflictivas de al menos dos bases de datos, cubriendo marcas idénticas y similares en las clases y jurisdicciones relevantes. Cada resultado incluye suficiente detalle para el análisis de confusión en el Paso 4.

**En caso de fallo:** Si una base de datos está temporalmente no disponible, anotar la brecha y proceder con las fuentes disponibles. Si la marca propuesta es una palabra común, esperar un conjunto de resultados grande — priorizar resultados en las mismas clases de Niza o cercanamente relacionadas antes de expandir.

### Paso 3: Evaluar la Distintividad

Evaluar dónde cae la marca propuesta en el espectro Abercrombie.

1. Aplicar el **espectro Abercrombie** (más débil a más fuerte):
   - **Genérico**: El nombre común para los bienes/servicios ("Computer Software" para software). No registrable y no protegible
   - **Descriptivo**: Describe directamente una cualidad, característica o propósito ("Quick Print" para impresión). Registrable solo con evidencia de significado secundario (distintividad adquirida)
   - **Sugestivo**: Sugiere una cualidad pero requiere imaginación para conectar ("Netflix" = internet + flicks). Inherentemente distintivo; registrable sin significado secundario
   - **Arbitrario**: Una palabra real usada en un contexto no relacionado ("Apple" para computadoras). Distintividad inherente fuerte
   - **Fanciful**: Una palabra acuñada sin significado previo ("Xerox", "Kodak"). Distintividad más fuerte
2. Evaluar significado secundario si la marca es descriptiva:
   - Duración y extensión de uso en comercio
   - Gastos de publicidad y exposición al consumidor
   - Encuestas o declaraciones del consumidor
   - Cobertura mediática y reconocimiento no solicitado
3. Verificar marcas que se han vuelto genéricas mediante **genericidio**:
   - ¿La marca fue una vez distintiva pero ahora se usa como un término común? (p. ej., "escalator", "aspirin" en EE.UU.)
4. Documentar la evaluación de distintividad con razonamiento

**Esperado:** Una clasificación clara de la marca en el espectro Abercrombie con justificación de soporte. Si la marca es descriptiva, una evaluación de si se puede establecer significado secundario. Marcas sugestivas, arbitrarias y fanciful proceden con confianza.

**En caso de fallo:** Si la marca cae en la frontera genérico-descriptivo, este es un riesgo significativo de registro. Recomendar modificar la marca para empujarla hacia sugestiva (añadir un giro, combinar con un concepto no relacionado) o preparar una estrategia de evidencia de significado secundario.

### Paso 4: Analizar la Probabilidad de Confusión

Evaluar si la marca propuesta es probable de ser confundida con cualquier marca previa encontrada en el Paso 2.

1. Para cada marca previa potencialmente conflictiva, evaluar los **factores DuPont** (marco EE.UU.) o los **motivos relativos EUIPO**:
   - **Similitud de marcas**:
     - Visual: apariencia lado a lado, composición de letras, longitud, estructura
     - Fonética: pronunciación, conteo de sílabas, patrones de acento, sonidos vocálicos
     - Conceptual: significado, connotación, impresión comercial
   - **Similitud de bienes/servicios**:
     - La misma clase de Niza es un indicador fuerte pero no concluyente
     - Bienes/servicios relacionados en clases diferentes aún pueden conflictuar
     - Considerar canales de comercio y compradores típicos
   - **Fuerza de la marca previa**:
     - Marcas famosas obtienen protección más amplia (doctrina de dilución)
     - Marcas débiles/descriptivas obtienen protección más estrecha
     - Presencia de mercado, gasto en publicidad, encuestas de reconocimiento
   - **Evidencia de confusión real**:
     - Quejas de clientes, comunicaciones mal dirigidas
     - Menciones en redes sociales confundiendo las dos marcas
     - Procedimientos previos de oposición o cancelación
2. Sopesar los factores holísticamente:
   - Ningún factor único es dispositivo; el análisis es una prueba de balance
   - Similitud fuerte en marcas puede compensar similitud débil en bienes (y viceversa)
   - Las marcas famosas inclinan el balance hacia encontrar confusión más fácilmente
3. Calificar cada conflicto potencial:
   - **Bloqueante**: Marca casi-idéntica en mismos bienes/servicios, marca previa fuerte
   - **Alto riesgo**: Marca similar en mismos/relacionados bienes, o marca idéntica en bienes relacionados
   - **Riesgo moderado**: Marca similar en bienes relacionados, o marca idéntica en bienes distantes
   - **Bajo riesgo**: Similitud débil, bienes distantes o marca previa débil

**Esperado:** Una lista calificada de conflictos potenciales con análisis soportando cada calificación. Los conflictos más serios (bloqueante y alto riesgo) están identificados con razonamiento específico.

**En caso de fallo:** Si el análisis es limítrofe (factores apuntando en ambas direcciones), calificar el conflicto conservadoramente (mayor riesgo). Es más seguro marcar un conflicto potencial que resulta manejable que perder uno que bloquea el registro o dispara litigio.

### Paso 5: Evaluar Derechos de Derecho Consuetudinario

Evaluar derechos de marca no registrados que pueden no aparecer en búsquedas de bases de datos.

1. Buscar uso previo sin registro:
   - Registros de nombre comercial y bases de datos estatales/provinciales
   - Registros de nombres de dominio (WHOIS, herramientas de búsqueda de dominio)
   - Handles de redes sociales y perfiles comerciales
   - Directorios de industria y publicaciones comerciales
   - Búsqueda en Google y web general por uso comercial de la marca
2. Considerar reglas jurisdiccionales:
   - **EE.UU.**: Sistema first-to-use — el uso comercial previo crea derechos incluso sin registro
   - **UE**: Sistema first-to-file — el registro tiene prioridad, pero el uso previo puede crear defensas limitadas
   - **Reino Unido**: La doctrina de passing off protege marcas no registradas con goodwill
3. Evaluar el alcance de cualquier derecho de derecho consuetudinario encontrado:
   - Alcance geográfico del mercado del usuario previo
   - Duración y consistencia del uso
   - Si el usuario ha construido goodwill en la marca
4. Documentar hallazgos de derecho consuetudinario y su impacto en la evaluación general de riesgo

**Esperado:** Una lista suplementaria de usos no registrados de la marca (o marcas similares) que podrían crear conflictos no visibles en búsquedas de registros de marca. Particularmente importante para presentaciones en EE.UU.

**En caso de fallo:** Si la búsqueda de derecho consuetudinario produce resultados abrumadores (la marca es una palabra común), enfocarse en usos en la misma industria/categoría de bienes. Los derechos de derecho consuetudinario son típicamente estrechos en alcance — una panadería local llamada "Sunrise" no bloquea un producto de software llamado "Sunrise."

### Paso 6: Evaluar el Solapamiento de Bienes/Servicios

Analizar la proximidad competitiva de bienes/servicios en detalle.

1. Comparar la clasificación de Niza de la marca propuesta contra cada marca previa:
   - Misma clase: solapamiento presuntivo (pero no automático — las clases pueden ser amplias)
   - Clases adyacentes: evaluar si los bienes/servicios son complementarios o competitivos
   - Clases distantes: típicamente seguras a menos que la marca previa sea famosa
2. Analizar canales de comercio:
   - ¿Los bienes se venden a través de los mismos minoristas o plataformas?
   - ¿Apuntan al mismo demográfico de consumidor?
   - ¿Un consumidor encontrando ambas marcas asumiría una fuente común?
3. Evaluar la probabilidad de expansión:
   - ¿El propietario de la marca previa es probable de expandir a los bienes/servicios de la marca propuesta?
   - Doctrina de "zona de expansión natural" (EE.UU.)
4. Documentar el análisis de solapamiento con razonamiento de soporte

**Esperado:** Una evaluación clara de la proximidad de bienes/servicios para cada conflicto potencial, fortaleciendo o debilitando las calificaciones de probabilidad de confusión del Paso 4.

**En caso de fallo:** Si la relación de bienes/servicios no está clara (categorías de productos novedosas, industrias convergentes), aplicar la prueba del consumidor razonable: ¿un comprador típico viendo ambas marcas en el mercado asumiría que vienen de la misma fuente?

### Paso 7: Generar Reporte de Conflicto

Compilar todos los hallazgos en un reporte estructurado y accionable.

1. Escribir el **Reporte de Conflicto de Marca** con secciones:
   - **Resumen ejecutivo**: marca propuesta, hallazgos clave, calificación general de riesgo
   - **Marca y alcance**: descripción de la marca, clases de Niza, jurisdicciones
   - **Evaluación de distintividad**: clasificación Abercrombie, implicaciones de registro
   - **Matriz de conflicto**: todos los conflictos identificados con calificaciones de riesgo

```text
Conflict Risk Matrix:
+----+-------------------+----------+---------+-------+---------+
| #  | Prior Mark        | Classes  | Juris.  | Type  | Risk    |
+----+-------------------+----------+---------+-------+---------+
| 1  | ACMESOFT          | 9, 42    | US, EU  | Ident | BLOCK   |
| 2  | ACME SOLUTIONS    | 42       | US      | Sim   | HIGH    |
| 3  | ACMEX             | 35       | EU      | Phon  | MOD     |
| 4  | ACM               | 16       | US      | Vis   | LOW     |
+----+-------------------+----------+---------+-------+---------+
Risk: BLOCK = blocking | HIGH | MOD = moderate | LOW | CLEAR
Type: Ident = identical | Sim = similar | Phon = phonetic | Vis = visual
```

   - **Hallazgos de derecho consuetudinario**: usos no registrados de relevancia
   - **Análisis de bienes/servicios**: evaluación de solapamiento por conflicto
   - **Recomendaciones**: una de las siguientes conclusiones generales:
     - **Limpio**: No se encontraron conflictos significativos — proceder a presentar
     - **Bajo riesgo**: Conflictos menores improbables de prevenir el registro — proceder con monitoreo
     - **Riesgo moderado**: Existen conflictos pero pueden ser manejables — considerar acuerdo de coexistencia, modificación de marca o estrechamiento de bienes/servicios
     - **Alto riesgo**: Conflictos significativos probables de disparar oposición o rechazo — considerar modificación sustancial de marca o marcas alternativas
     - **Bloqueante**: Marca previa casi-idéntica en mismos bienes/servicios — no proceder sin asesoría legal
2. Incluir limitaciones y advertencias:
   - El cribado no es una opinión legal; consultar con abogado de marcas antes de presentar
   - Pueden existir derechos de derecho consuetudinario más allá de lo que las búsquedas de bases de datos revelan
   - La similitud figurativa requiere inspección visual (más allá de la capacidad de búsqueda de texto)

**Esperado:** Un reporte de conflicto completo con calificaciones de riesgo, evaluación de distintividad y recomendaciones claras. El reporte habilita una decisión go/no-go sobre la marca propuesta.

**En caso de fallo:** Si el análisis es inconcluso (señales mixtas entre jurisdicciones o clases), presentar los hallazgos por jurisdicción y dejar que el tomador de decisiones sopese las consideraciones comerciales junto con el riesgo legal. Un calificado "proceder con cautela" es una conclusión válida.

## Lista de Verificación de Validación

- [ ] Marca y bienes/servicios documentados claramente con clases de Niza
- [ ] Al menos dos bases de datos de marcas buscadas (p. ej., TMview + USPTO TESS)
- [ ] Marcas idénticas y similares buscadas (fonéticas, visuales, conceptuales)
- [ ] Distintividad evaluada en el espectro Abercrombie con razonamiento
- [ ] Probabilidad de confusión analizada usando factores DuPont o motivos relativos EUIPO
- [ ] Derechos de derecho consuetudinario investigados (nombres comerciales, dominios, presencia web)
- [ ] Solapamiento de bienes/servicios evaluado para cada conflicto potencial
- [ ] Matriz de conflicto producida con calificaciones de riesgo por marca
- [ ] Recomendación general provista (limpio / bajo / moderado / alto / bloqueante)
- [ ] Limitaciones declaradas (cribado vs. opinión legal, brechas de cobertura de bases de datos)

## Errores Comunes

- **Búsqueda solo-idéntica**: Buscar coincidencias exactas pierde los conflictos más peligrosos — marcas fonéticamente y visualmente similares que disparan probabilidad de confusión. Siempre buscar variantes
- **Ignorar clases relacionadas**: Una marca de software (Clase 9) puede conflictuar con una marca SaaS (Clase 42) o una marca de consultoría (Clase 35). Las clases de Niza son guías, no muros
- **Saltarse la búsqueda de derecho consuetudinario**: En EE.UU., una marca no registrada con uso previo triunfa sobre un registro federal posterior. Las búsquedas de bases de datos solas son insuficientes
- **Confundir distintividad con disponibilidad**: Una marca puede ser altamente distintiva (fanciful) y aún conflictuar con un registro idéntico existente. Distintividad y disponibilidad son preguntas separadas
- **Sesgo de jurisdicción única**: Una marca que está limpia en EE.UU. puede estar bloqueada en la UE y viceversa. Siempre cribar las jurisdicciones donde la marca será realmente usada
- **Tratar el cribado como opinión legal**: Esta habilidad produce una evaluación estructurada de riesgo, no asesoría legal. Hallazgos bloqueantes y de alto riesgo ameritan revisión por abogado de marcas antes de tomar decisiones finales

## Habilidades Relacionadas

- `assess-ip-landscape` -- Mapeo más amplio de panorama de IP que contextualiza el cribado de marca dentro de una estrategia de IP completa
- `search-prior-art` -- Búsqueda de prior art enfocada en patentes usando bases de datos diferentes y estándares legales (novedad/no-obviedad vs. probabilidad de confusión)
- `file-trademark` -- Procedimiento de presentación que sigue a un cribado exitoso (aún no disponible)
