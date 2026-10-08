---
name: file-trademark-pjt222
title: File Trademark
description: Trademark filing procedures covering EUIPO (EU), USPTO (US), and WIPO Madrid Protocol (international). Walks through pre-filing conflict checks, Nice classification, descriptiveness assessment, mark type decisions, filing basis strategy, office-specific e-filing procedures, Madrid Protocol extension, post- filing monitoring, and open-source trademark policy drafting. Use after running screen-trademark to confirm the mark is clear, when ready to secure trademark rights in one or more jurisdictions.
author: pjt222
author_url: https://github.com/pjt222/agent-almanac/tree/main/i18n/es/skills/file-trademark
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: es
---

# File Trademark

Presentar una solicitud de marca con EUIPO (UE), USPTO (EE.UU.) o el Protocolo de Madrid de la WIPO (internacional). Esta habilidad cubre el procedimiento real de presentación — desde la verificación pre-presentación hasta el monitoreo post-registro y la política de marca para open-source. Asume que el cribado de conflictos ya se ha completado vía `screen-trademark`.

## Cuándo Usar

- Listo para presentar una solicitud de marca después de que el cribado de conflictos esté limpio
- Eligiendo entre estrategias de presentación UE, EE.UU. o internacionales
- Presentando una marca UE y reclamando prioridad para una presentación posterior en EE.UU.
- Extendiendo una marca nacional existente internacionalmente vía Protocolo de Madrid
- Redactando una política de uso de marca open-source después del registro
- Respondiendo a acciones de oficina o procedimientos de oposición durante el examen

## Entradas

- **Requerido**: Marca a presentarse (palabra, logo o combinada)
- **Requerido**: Descripción de bienes y servicios
- **Requerido**: Jurisdicciones objetivo (UE, EE.UU., internacional o combinación)
- **Requerido**: Nombre y dirección del solicitante
- **Opcional**: Resultados de screen-trademark (reporte de búsqueda de conflictos)
- **Opcional**: Archivos de logo (si se presenta una marca figurativa o combinada)
- **Opcional**: Reclamación de prioridad (presentación anterior en otra jurisdicción, dentro de 6 meses)
- **Opcional**: Prueba de uso en comercio (requerido para base USPTO 1(a))
- **Opcional**: Contexto del proyecto open-source (para política de marca en el Paso 10)

## Referencia de Costos de Presentación

| Oficina | Tarifa Base | Por Clase | Notas |
|---|---|---|---|
| EUIPO | 850 EUR | +50 EUR (2da), +150 EUR (3ra+) | Fondo SME: 75% reembolso |
| USPTO (TEAS Plus) | $250 | por clase | Solicitantes extranjeros necesitan abogado de EE.UU. |
| USPTO (TEAS Standard) | $350 | por clase | Descripción de bienes más flexible |
| Protocolo de Madrid | 653 CHF | varía por país | Depende de la marca base por 5 años |

## Procedimiento

### Paso 1: Verificaciones Pre-Presentación

Verificar que la marca esté limpia para presentación antes de invertir en tarifas de solicitud.

1. Confirmar que `screen-trademark` se ha ejecutado:
   - Revisar el reporte de búsqueda de conflictos para marcas idénticas o confusamente similares
   - Verificar que todas las jurisdicciones objetivo fueron cubiertas en el cribado
   - Verificar que el cribado sea reciente (idealmente dentro de los últimos 30 días)
2. Ejecutar verificaciones finales de conflictos contra bases de datos oficiales:
   - **EUIPO TMview**: Buscar en todos los registros de estados miembros de la UE
   - **WIPO Global Brand Database**: Registros internacionales
   - **USPTO TESS**: Registro federal de EE.UU. (usar búsqueda estructurada: `"mark text"[BI]`)
   - **DPMAregister**: Registro nacional alemán (si se presenta en UE, cubre el mercado más grande de la UE)
3. Verificar que el nombre de dominio y handles de redes sociales estén disponibles o asegurados:
   - La disponibilidad del dominio refuerza argumentos de distintividad si se desafía
   - Handles coincidentes reducen el riesgo de confusión del consumidor
4. Documentar los resultados de búsqueda como el **Registro de Limpieza Pre-Presentación**

**Esperado:** Confirmación de que no existen marcas bloqueantes en las jurisdicciones objetivo. El Registro de Limpieza Pre-Presentación documenta la diligencia y soporta cualquier defensa futura de oposición.

**En caso de fallo:** Si se encuentran marcas conflictivas, evaluar la severidad: marca idéntica + bienes idénticos = no presentar. Marca similar + bienes relacionados = buscar consejo legal sobre probabilidad de confusión. Si los conflictos están limitados a una sola jurisdicción, considerar presentar solo en jurisdicciones limpias.

### Paso 2: Selección de Clasificación de Niza

Identificar las clases correctas de bienes y servicios bajo el sistema de Clasificación de Niza.

1. Consultar la herramienta TMclass (tmclass.tmdn.org) para identificación de clases:
   - Ingresar la descripción de bienes/servicios
   - TMclass sugiere términos armonizados aceptados por la mayoría de las oficinas
   - Usar términos pre-aprobados de la base de datos TMclass reduce los retrasos de examen
2. Clases comunes para tecnología y software:
   - **Clase 9**: Software descargable, apps móviles, hardware de computadora
   - **Clase 35**: Publicidad, gestión empresarial, administración de plataforma SaaS
   - **Clase 42**: SaaS, computación en la nube, servicios de desarrollo de software
   - **Clase 38**: Telecomunicaciones, plataformas en línea, servicios de mensajería
3. Redactar la descripción de bienes y servicios:
   - Ser específico suficientemente para definir tu uso real pero amplio suficientemente para expansión futura
   - TEAS Plus (USPTO) requiere términos del ID Manual — usar términos pre-aprobados
   - EUIPO acepta términos armonizados de TMclass directamente
4. Equilibrar costo contra cobertura:
   - Cada clase adicional añade tarifas (ver tabla de costos arriba)
   - Presentar en clases donde actualmente usas o pretendes usar la marca
   - Presentaciones excesivamente amplias sin uso pueden ser desafiadas (especialmente en EE.UU.)

**Esperado:** Una lista finalizada de clases de Niza con descripciones específicas y pre-aprobadas de bienes y servicios para cada clase. Las descripciones coinciden con el uso comercial real.

**En caso de fallo:** Si TMclass no sugiere una coincidencia clara, consultar las notas explicativas de la Clasificación de Niza (página WIPO Niza). Bienes ambiguos a veces abarcan múltiples clases — presentar en todas las clases relevantes en lugar de arriesgar la exclusión.

### Paso 3: Evaluación de Descriptividad

Evaluar si la marca es registrable o probable de enfrentar objeciones de descriptividad.

1. Evaluar la marca en el **espectro Abercrombie** (estándar EE.UU., ampliamente aplicado):
   - **Genérico**: El nombre común para el producto (p. ej., "Computer" para computadoras) — nunca registrable
   - **Descriptivo**: Describe directamente una cualidad o característica (p. ej., "QuickBooks") — registrable solo con significado secundario
   - **Sugestivo**: Sugiere pero no describe directamente (p. ej., "Netflix") — registrable sin significado secundario
   - **Arbitrario**: Una palabra real usada en un contexto no relacionado (p. ej., "Apple" para electrónica) — protección fuerte
   - **Fanciful**: Una palabra inventada (p. ej., "Xerox") — protección más fuerte
2. Verificar contra los motivos absolutos del EUTMR (Artículo 7(1)):
   - Art. 7(1)(b): Carente de carácter distintivo
   - Art. 7(1)(c): Descriptivo de características de los bienes/servicios
   - Art. 7(1)(d): Habitual en el comercio (genérico en el sector relevante)
3. Si la marca es descriptiva limítrofe:
   - Reunir evidencia de distintividad adquirida (gasto en publicidad, cifras de ventas, encuestas a consumidores)
   - Considerar añadir un elemento distintivo (logo, estilización)
   - Modificar la marca de palabra para moverla hacia sugestiva o arbitraria
4. Documentar la evaluación con razonamiento

**Esperado:** La marca se clasifica en el espectro Abercrombie como sugestiva, arbitraria o fanciful — todas registrables sin significado secundario. Casos limítrofes están marcados con una estrategia de mitigación.

**En caso de fallo:** Si la marca es descriptiva o genérica, no presentar — será rechazada. Rediseñar la marca para subir en el espectro de distintividad. Si existe historial de uso significativo, considerar una reclamación bajo la Sección 2(f) (distintividad adquirida) para EE.UU. o una reclamación similar bajo el Art. 7(3) EUTMR para la UE.

### Paso 4: Decisión de Tipo de Marca

Elegir el tipo de registro que mejor protege la marca.

1. **Marca de palabra** (caracteres estándar):
   - Protege la palabra misma independientemente de la fuente, color o estilo
   - Protección más amplia — cubre cualquier representación visual
   - No puede incluir elementos de diseño
   - Mejor elección cuando el valor de la marca está en el nombre, no en el logo
2. **Marca figurativa** (logo o diseño):
   - Protege la representación visual específica
   - Protección más estrecha — no cubre la palabra en otros estilos
   - Requerido cuando el logo mismo es el identificador primario de la marca
   - Debe enviar un archivo de imagen claro (JPG/PNG, EUIPO: max 2 MB, min 945x945 px)
3. **Marca combinada** (palabra + logo juntos):
   - Protege la combinación específica como se presentó
   - Más estrecha que una marca de palabra sola — limitada a la combinación específica
   - Común pero estratégicamente subóptima: si el logo cambia, el registro puede no cubrir la nueva versión
4. **Recomendación estratégica**:
   - Presentar primero una marca de palabra (protección más amplia, más rentable)
   - Presentar una marca figurativa separada para el logo solo si el logo tiene valor de marca independiente significativo
   - Evitar marcas combinadas a menos que las restricciones de presupuesto impidan presentaciones separadas

**Esperado:** Una decisión clara del tipo de marca con razonamiento estratégico. La marca de palabra es la recomendación predeterminada a menos que el logo cargue valor de marca independiente.

**En caso de fallo:** Si no estás seguro de si el nombre solo es lo suficientemente distintivo, probar preguntando: "¿Reconocerían los consumidores este nombre en texto plano, sin el logo?" Si sí, presentar la marca de palabra. Si el logo es inseparable de la identidad de marca, considerar presentar marcas de palabra y figurativa por separado.

### Paso 5: Selección de Base de Presentación

Determinar la base legal para la solicitud (principalmente relevante para USPTO).

1. **Uso en comercio — Sección 1(a)**:
   - La marca ya está en uso en comercio interestatal (EE.UU.) o uso genuino (UE)
   - Debe enviar un specimen mostrando la marca como se usa (screenshot, empaque, publicidad)
   - Camino más rápido al registro
2. **Intención de uso — Sección 1(b)**:
   - La marca aún no está en uso pero el solicitante tiene intención bona fide de usar
   - Requiere una Declaración de Uso antes del registro (tarifas adicionales, fechas límite)
   - Permite asegurar prioridad antes del lanzamiento
   - Extensiones de tiempo disponibles (hasta 36 meses en total)
3. **Prioridad extranjera — Sección 44(d)**:
   - Reclamar prioridad de una presentación extranjera hecha dentro de los últimos 6 meses
   - **Estrategia**: Presentar EUIPO primero (menor costo, más rápido), luego reclamar prioridad 44(d) para USPTO
   - Esto da a la presentación de EE.UU. la misma fecha de prioridad que la presentación UE
   - Requiere una copia certificada de la solicitud extranjera
4. **Registro extranjero — Sección 44(e)**:
   - Basado en un registro extranjero (no solo una solicitud)
   - No se requiere uso en comercio de EE.UU. al presentar (pero eventualmente debe usarse)
5. **Extensión de Protocolo de Madrid — Sección 66(a)**:
   - Designando EE.UU. a través del sistema de Madrid
   - Ver Paso 8 para detalles de Madrid

**Esperado:** Base de presentación seleccionada con cronograma y requisitos de specimen documentados. Si se usa la estrategia UE-primero (EUIPO luego 44(d) a USPTO), la ventana de prioridad de 6 meses está calendarizada.

**En caso de fallo:** Si no existe uso en comercio y no hay presentación extranjera pendiente, la Sección 1(b) (intención de uso) es la única opción para USPTO. Tener en cuenta los costos adicionales de Declaración de Uso y fechas límite. Para EUIPO, no se requiere uso al presentar — la declaración de intención es suficiente.

### Paso 6: Procedimiento de E-Filing EUIPO

Presentar la solicitud de marca de la UE en línea.

1. Navegar al portal de e-filing de EUIPO (euipo.europa.eu):
   - Crear una cuenta de usuario EUIPO si no está ya registrado
   - Usar la presentación "Fast Track" para términos TMclass pre-aprobados (examen más rápido)
2. Completar el formulario de solicitud:
   - **Detalles del solicitante**: Nombre, dirección, forma legal, nacionalidad
   - **Representante**: Opcional para solicitantes con base en UE; requerido para solicitantes no-UE
   - **Marca**: Ingresar texto de marca de palabra o subir imagen de marca figurativa
   - **Bienes y servicios**: Seleccionar términos TMclass o ingresar descripciones personalizadas
   - **Idioma de presentación**: Elegir entre EN, FR, DE, ES, IT (segundo idioma requerido)
   - **Reclamación de prioridad**: Ingresar número y fecha de solicitud extranjera si se reclama prioridad
3. Revisar el resumen de tarifas:
   - 1 clase: 850 EUR
   - 2 clases: 900 EUR (+50 EUR)
   - 3+ clases: 900 EUR + 150 EUR por clase adicional
   - **Fondo SME (EUIPOIdeaforIP)**: Pequeñas y medianas empresas pueden reclamar 75% de reembolso
4. Pagar en línea (tarjeta de crédito, transferencia bancaria o cuenta corriente EUIPO)
5. Guardar el recibo de presentación con número de solicitud y fecha de presentación

**Esperado:** Solicitud EUIPO presentada con recibo de confirmación. Número de solicitud y fecha de presentación registrados. Si se usa Fast Track, el examen típicamente se completa dentro de 1 mes.

**En caso de fallo:** Si el portal en línea rechaza la presentación (error técnico), guardar un screenshot e intentar de nuevo. Si la descripción de bienes/servicios es rechazada, cambiar a términos TMclass pre-aprobados. Si el pago falla, la solicitud se guarda como borrador por 30 días.

### Paso 7: Procedimiento de Presentación USPTO

Presentar la solicitud federal de marca de EE.UU. en línea.

1. Navegar a USPTO TEAS (Trademark Electronic Application System):
   - Elegir TEAS Plus ($250/clase) o TEAS Standard ($350/clase)
   - TEAS Plus requiere términos pre-aprobados del ID Manual; TEAS Standard permite descripciones de forma libre
2. **Requisito de solicitante extranjero**:
   - Solicitantes domiciliados fuera de EE.UU. DEBEN designar un abogado licenciado en EE.UU.
   - El abogado debe ser miembro en buen estado del colegio de abogados de un estado de EE.UU.
   - Este requisito aplica incluso si se presenta a través del Protocolo de Madrid
3. Completar el formulario de solicitud:
   - **Información del solicitante**: Nombre, dirección, tipo de entidad, ciudadanía/estado de organización
   - **Información del abogado**: Nombre, membresía del colegio, email de correspondencia
   - **Marca**: Ingresar marca de palabra en caracteres estándar o subir imagen de marca de diseño
   - **Bienes y servicios**: Seleccionar del ID Manual (TEAS Plus) o redactar personalizado (TEAS Standard)
   - **Base de presentación**: Seleccionar Sección 1(a), 1(b), 44(d) o 44(e) (ver Paso 5)
   - **Specimen** (solo base 1(a)): Subir mostrando la marca como se usa en comercio
   - **Declaración**: Verificar precisión bajo pena de perjurio
4. Pagar la tarifa de presentación ($250 o $350 por clase)
5. Guardar el recibo de presentación con número de serie y fecha de presentación

**Esperado:** Solicitud USPTO presentada con número de serie asignado. Recibo de presentación guardado. El examen típicamente toma 8-12 meses para la primera acción de oficina.

**En caso de fallo:** Si el sistema TEAS rechaza la presentación, revisar los mensajes de error — problemas comunes incluyen tipo de entidad incorrecto, specimen faltante (para presentaciones 1(a)) o descripciones de bienes que no coinciden con términos del ID Manual (TEAS Plus). Si un solicitante extranjero presenta sin abogado de EE.UU., la solicitud será rechazada.

### Paso 8: Extensión de Protocolo de Madrid

Extender la protección internacionalmente a través del Sistema de Madrid de WIPO.

1. **Prerrequisitos**:
   - Una marca base (solicitud o registro) en la oficina de origen
   - El solicitante debe ser nacional de, domiciliado en o tener un establecimiento real y efectivo en un país miembro de Madrid
   - La marca base debe cubrir los mismos bienes/servicios o más estrechos
2. Presentar a través de la oficina de origen (no directamente con WIPO):
   - **EUIPO como origen**: Usar la herramienta de e-filing Madrid de EUIPO
   - **USPTO como origen**: Presentar vía formulario TEAS International Application
3. Completar la solicitud de Madrid (formulario MM2):
   - **Detalles del solicitante**: Deben coincidir con el titular de la marca base exactamente
   - **Representación de la marca**: Debe ser idéntica a la marca base
   - **Bienes y servicios**: Seleccionar de la especificación de la marca base (puede estrechar, no ampliar)
   - **Partes Contratantes Designadas**: Seleccionar países/regiones objetivo
   - **Idioma**: Inglés, francés o español
4. Calcular tarifas:
   - Tarifa base: 653 CHF (blanco y negro) o 903 CHF (color)
   - Tarifa suplementaria: 100 CHF por clase más allá de la primera
   - Tarifas individuales: Varían por país designado (verificar calculadora de tarifas WIPO)
   - Tarifas individuales comunes: EE.UU. ~$400+/clase, Japón ~$500+/clase, China ~$150+/clase
5. **Dependencia de ataque central**:
   - Por los primeros 5 años, el registro internacional depende de la marca base
   - Si la marca base es cancelada (oposición, no-uso), todas las designaciones caen
   - Después de 5 años, cada designación se vuelve independiente
   - Estrategia: Proteger la marca base vigorosamente durante el período de dependencia

**Esperado:** Solicitud de Madrid presentada a través de la oficina de origen. Países designados seleccionados con cálculos de tarifas documentados. El riesgo de dependencia de 5 años está reconocido y el plan de protección de la marca base está en su lugar.

**En caso de fallo:** Si la oficina de origen rechaza la solicitud de Madrid (p. ej., desajuste con la marca base), corregir la discrepancia y volver a presentar. Si un país designado rechaza la protección, responder a través del sistema de Madrid dentro del plazo de la oficina designada (típicamente 12-18 meses).

### Paso 9: Monitoreo Post-Presentación

Rastrear la solicitud a través del examen y responder a las acciones.

1. **Monitoreo EUIPO**:
   - Publicación en la Parte A del Boletín de Marcas de la UE
   - **Período de oposición**: 3 meses desde la publicación (extendible por 1 mes de cooling-off)
   - Si no hay oposición: el registro emite automáticamente
   - Defensa de oposición: presentar observaciones dentro de 2 meses de la notificación
2. **Monitoreo USPTO**:
   - Verificar TSDR (Trademark Status and Document Retrieval) regularmente
   - **Revisión del abogado examinador**: 8-12 meses después de la presentación
   - **Acciones de oficina**: El plazo de respuesta es típicamente 3 meses (extendible una vez por $125)
   - **Publicación para oposición**: Período de 30 días en la Gaceta Oficial
   - **Declaración de Uso** (presentaciones 1(b)): Debe presentarse dentro de 6 meses del Aviso de Permitido (extendible hasta 36 meses en total, $125 por extensión)
3. **Monitoreo de Madrid**:
   - WIPO notifica a cada oficina designada
   - Cada oficina examina independientemente (ventana de 12-18 meses)
   - Las negativas provisionales deben responderse a través de los procedimientos de la oficina local
4. **Calendarizar todas las fechas límite**:
   - Plazos de respuesta de oposición
   - Plazos de Declaración de Uso (USPTO 1(b))
   - Plazos de renovación (10 años EUIPO, 10 años USPTO, 10 años Madrid)
   - USPTO Sección 8/71 Declaración de Uso: entre el 5to y 6to año
5. Monitorear presentaciones de terceros de marcas confusamente similares:
   - Configurar alertas de vigilancia TMview/TESS para marcas similares en tus clases
   - Considerar un servicio profesional de vigilancia de marcas para marcas críticas

**Esperado:** Todas las fechas límite están calendarizadas con recordatorios. El estado de la solicitud se monitorea a través del sistema en línea de cada oficina. Las estrategias de respuesta a oposición o acción de oficina están preparadas con anticipación.

**En caso de fallo:** Perder un plazo puede ser fatal — la mayoría de los plazos de las oficinas de marcas no son extendibles. Si un plazo se pierde, verificar si el reavivamiento o reincorporación está disponible (USPTO permite petición para reavivar por demora no intencional). Para EUIPO, los plazos de oposición perdidos son generalmente finales.

### Paso 10: Política de Marca Open-Source

Redactar una política de uso de marca si la marca cubre un proyecto open-source.

1. Estudiar modelos establecidos:
   - **Linux Foundation**: Permite el uso del nombre del proyecto en referencias factuales; restringe logos a licenciatarios
   - **Mozilla**: Pautas detalladas distinguiendo distribuciones no modificadas de builds modificados
   - **Rust Foundation**: Permiso amplio para uso comunitario con restricciones específicas en productos comerciales
   - **Apache Software Foundation**: Política de nombres permisiva con restricciones en implicar respaldo
2. Definir categorías de uso:
   - **Uso justo** (siempre permitido): Referirse al proyecto por nombre en artículos, reseñas, comparaciones, papers académicos
   - **Uso comunitario/contribuyente** (ampliamente permitido): Grupos de usuarios, conferencias, materiales educativos, distribuciones no modificadas
   - **Uso comercial** (requiere licencia o restricciones): Productos incorporando el software, servicios basados en el proyecto, reclamaciones de certificación/compatibilidad
   - **Uso prohibido**: Implicar respaldo oficial, uso en versiones sustancialmente modificadas sin divulgación, nombres de dominio que causan confusión
3. Redactar el documento de política de marca:
   - Declaración clara de propiedad de marca
   - Qué usos están permitidos sin permiso
   - Qué usos requieren permiso por escrito
   - Cómo solicitar permiso (contacto, proceso)
   - Consecuencias de mal uso
4. Colocar el archivo de política en el repositorio del proyecto:
   - Ubicaciones comunes: `TRADEMARKS.md`, `TRADEMARK-POLICY.md` o una sección en `CONTRIBUTING.md`
   - Enlazar desde `README.md` y el sitio web del proyecto
5. Registrar la marca antes de publicar la política:
   - Una política de marca sin un registro es inaplicable en la mayoría de los casos
   - Como mínimo, presentar la solicitud antes de publicar — "TM" puede usarse inmediatamente, "(R)" solo después del registro

**Esperado:** Una política de marca clara y justa que protege la marca mientras habilita el uso comunitario saludable. La política sigue los modelos establecidos de fundaciones open-source y es accesible desde la documentación principal del proyecto.

**En caso de fallo:** Si el proyecto no tiene registro o solicitud de marca, presentar primero (Pasos 6-8) antes de redactar la política. Una marca no registrada tiene aplicabilidad limitada. Si la comunidad da pushback en la política, estudiar el enfoque de la Rust Foundation — fue revisado después del feedback de la comunidad y es considerado un buen modelo para equilibrar protección con apertura.

## Lista de Verificación de Validación

- [ ] Verificaciones de conflicto pre-presentación completadas y documentadas (Paso 1)
- [ ] Clases de Niza seleccionadas con descripciones pre-aprobadas de bienes y servicios (Paso 2)
- [ ] Descriptividad evaluada en el espectro Abercrombie (Paso 3)
- [ ] Tipo de marca decidido con razonamiento estratégico (Paso 4)
- [ ] Base de presentación seleccionada con cronograma y requisitos de specimen documentados (Paso 5)
- [ ] Solicitud presentada en al menos una jurisdicción objetivo (Pasos 6-8)
- [ ] Recibo de presentación guardado con número de solicitud y fecha de presentación
- [ ] Todos los plazos post-presentación calendarizados con recordatorios (Paso 9)
- [ ] Alertas de vigilancia de marca configuradas para marcas confusamente similares (Paso 9)
- [ ] Política de marca open-source redactada si aplica (Paso 10)

## Errores Comunes

- **Presentar sin cribado**: Saltarse `screen-trademark` e ir directo a presentar desperdicia tarifas si existe una marca conflictiva. Siempre cribar primero
- **Base de presentación incorrecta**: Reclamar uso en comercio (1(a)) cuando la marca aún no está en uso resulta en una presentación fraudulenta. Usar intención de uso (1(b)) si no ha ocurrido el lanzamiento
- **Descripciones de bienes excesivamente amplias**: Reclamar bienes y servicios que no usas o pretendes usar invita a la cancelación por no-uso (especialmente en la UE después de 5 años)
- **Perder la ventana de prioridad**: La prioridad extranjera bajo la Sección 44(d) debe reclamarse dentro de 6 meses de la primera presentación. Perder esta ventana significa perder la fecha de prioridad anterior
- **Ignorar el requisito de abogado extranjero**: Solicitantes no-EE.UU. presentando en USPTO sin un abogado licenciado en EE.UU. tendrán su solicitud rechazada — esta es una regla dura desde 2019
- **Exposición de ataque central de Madrid**: Confiar únicamente en designaciones de Madrid sin entender la dependencia de 5 años en la marca base. Si la marca base cae, todas las designaciones caen con ella
- **Sin monitoreo post-presentación**: Presentar la solicitud y olvidarse de ella. Las acciones de oficina y plazos de oposición pasan, y la solicitud queda abandonada
- **Política de marca antes del registro**: Publicar una política de marca sin tener al menos una solicitud pendiente socava la aplicabilidad. Presentar primero, luego redactar la política

## Habilidades Relacionadas

- `screen-trademark` — Cribado de conflictos que debe preceder este procedimiento de presentación
- `assess-ip-landscape` — Análisis más amplio del panorama de IP incluyendo mapeo de panorama de marcas
- `search-prior-art` — Metodología de búsqueda de prior art aplicable a la investigación de distintividad de marcas
