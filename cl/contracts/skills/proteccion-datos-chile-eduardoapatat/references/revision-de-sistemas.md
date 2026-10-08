# Construcción y revisión de sistemas

Usa este método para convertir las obligaciones jurídicas en decisiones de producto y controles verificables. No sustituye una auditoría de seguridad completa: la revisión técnica se concentra en los riesgos para datos personales.

## Elegir profundidad

| Nivel | Cuándo | Resultado mínimo |
| --- | --- | --- |
| Cribado | Existen señales, pero no se ha confirmado nexo o dato personal. | Decisión de activación, supuestos y una pregunta decisiva si hace falta. |
| Diseño | El sistema o una función todavía se está definiendo. | Flujo objetivo, requisitos, controles, criterios de aceptación y bloqueos de lanzamiento. |
| Revisión documental | Sólo hay políticas, diagramas o declaraciones. | Brechas documentales y lista explícita de controles técnicos no verificados. |
| Auditoría técnica | Hay código, configuración, infraestructura o acceso a evidencia operativa. | Hallazgos trazables a artefactos, artículo, riesgo, corrección y prueba. |
| Incidente | Existe pérdida, filtración, alteración, destrucción o acceso/comunicación no autorizado. | Aplicar además `incidentes-y-sanciones.md`. |

Declara siempre qué repositorios, servicios, ambientes, fechas y artefactos quedaron dentro y fuera del alcance.

## Modo construcción: privacidad y seguridad desde el inicio

Antes de implementar una función, crea una ficha con:

1. **Titulares:** clientes, prospectos, trabajadores, postulantes, pacientes, estudiantes, menores, contactos de proveedores u otros.
2. **Datos:** campos entregados, observados, derivados e inferidos; incluye metadatos, logs y respaldos.
3. **Finalidad:** una finalidad específica por operación, no “mejorar el servicio” como fórmula vacía.
4. **Necesidad:** por qué cada dato es adecuado, pertinente y estrictamente necesario; alternativa con menos datos.
5. **Licitud:** autorización legal, consentimiento u otra fuente aplicable, con sus requisitos y evidencia.
6. **Recorrido:** origen, API, cola, servicio, base, caché, analítica, exportación, proveedor, país y eliminación.
7. **Roles:** responsable, tercero mandatario o encargado, cesionario y subencargado según sus decisiones reales.
8. **Conservación:** evento inicial, plazo o criterio, excepciones legales, eliminación y efecto en respaldos.
9. **Derechos:** localización, autenticación del solicitante, ejecución, propagación y evidencia de respuesta.
10. **Riesgo:** abuso posible, probabilidad, impacto sobre personas, controles y riesgo residual.

No autorices el paso a producción si falta una finalidad definida, una fuente de licitud plausible, el responsable del tratamiento o una ruta de remediación para un riesgo crítico.

## Modo auditoría: evidencia antes que declaraciones

Prioriza la evidencia en este orden:

1. comportamiento comprobado y configuración efectiva del ambiente pertinente;
2. código, infraestructura como código, esquemas, migraciones y automatizaciones;
3. registros operativos y resultados de pruebas;
4. contratos, procedimientos y políticas aprobadas;
5. declaraciones de responsables técnicos o de negocio.

Una política demuestra una regla organizativa, no que el software la ejecute. Un fragmento de código demuestra intención, no necesariamente su despliegue. Registra cualquier contradicción.

Si el artefacto no está disponible, usa **no verificado**. No conviertas falta de evidencia en **no cumple**, salvo que la obligación consista precisamente en documentar o acreditar el control.

## Seguimiento de cada dato

Para cada categoría, recorre estas estaciones:

| Estación | Preguntas |
| --- | --- |
| Recolección | ¿Quién lo entrega o genera? ¿Es obligatorio? ¿Se informa la finalidad? ¿Se recoge de más? |
| Transporte | ¿Qué canales, APIs, colas, URLs o archivos lo llevan? ¿Puede interceptarse o terminar en trazas? |
| Almacenamiento | ¿Dónde queda, con qué claves, réplicas, índices, cachés y respaldos? |
| Uso | ¿Qué servicio, persona, consulta, modelo o decisión lo utiliza? ¿Coincide con la finalidad? |
| Comunicación | ¿Quién lo recibe? ¿Es encargado, nuevo responsable o mero destinatario? ¿Con qué autorización? |
| Transferencia | ¿Sale de Chile o queda accesible desde otro país mediante nube, soporte o subencargados? |
| Conservación | ¿Qué inicia y termina el plazo? ¿Hay trabajos automáticos y evidencia de ejecución? |
| Derechos | ¿Puede localizarse, entregarse, rectificarse, suprimirse, bloquearse u oponerse cuando proceda? |
| Incidente | ¿Cómo se detecta, contiene, cuantifica y documenta una vulneración? |

No olvides copias en herramientas de soporte, CRM, correo, planillas, chat, observabilidad, data warehouse, dispositivos y ambientes de desarrollo.

## Controles que deben diseñarse o comprobarse

### 1. Inventario, finalidad y minimización

Comprueba:

- formularios, modelos, eventos y respuestas de API frente al inventario declarado;
- campos opcionales que en la práctica son obligatorios;
- recolección anticipada “por si acaso”;
- nuevas inferencias, enriquecimiento o combinación de bases;
- respuestas de API con objetos completos cuando bastan pocos atributos;
- datos personales en nombres de archivos, parámetros URL, códigos QR o identificadores expuestos;
- configuraciones por defecto que maximizan visibilidad, conservación o seguimiento.

Relaciona el análisis actual con los artículos 4, 6, 9 y 11 de la Ley N.º 19.628 vigente, según corresponda. Para el régimen reformado, revisa los principios del artículo 3 y protección desde el diseño y por defecto del artículo 14 quáter.

### 2. Transparencia, consentimiento y preferencias

Comprueba:

- qué aviso y versión ve el titular al recolectarse el dato;
- identidad y canal operativo del responsable;
- finalidad, destinatarios, conservación, transferencias y derechos que deban informarse;
- que una finalidad opcional no se condicione indebidamente al servicio principal;
- registro de la manifestación, texto mostrado, fecha y mecanismo;
- revocación mediante un medio equivalente, expedito y gratuito cuando corresponda;
- propagación de la preferencia a analítica, marketing y terceros.

No llames “consentimiento” a una casilla premarcada, silencio, navegación o texto meramente informativo sin analizar la versión legal aplicable.

### 3. Autenticación, autorización y aislamiento

Comprueba:

- autenticación de usuarios y administradores acorde al riesgo;
- autorización del lado servidor en cada lectura, modificación, descarga y borrado;
- acceso por objeto y aislamiento entre organizaciones o tenants;
- mínimo privilegio, separación de funciones y revisión periódica de accesos;
- altas, cambios y bajas de trabajadores, proveedores y cuentas de servicio;
- sesiones, recuperación de cuenta, enlaces de un solo uso y credenciales expuestas;
- exportaciones masivas, paneles administrativos y soporte con impersonación;
- trazabilidad de accesos privilegiados sin registrar el contenido sensible innecesariamente.

La validación de formato de un RUT no autoriza el acceso a los datos asociados. Prueba el control con usuarios de distinto rol y tenant.

### 4. Confidencialidad, integridad, disponibilidad y resiliencia

Evalúa el control según naturaleza, alcance, contexto, fines, probabilidad e impacto. Comprueba:

- cifrado de transporte y su terminación real;
- necesidad de cifrado de almacenamiento, campos o respaldos y separación de claves;
- gestión, rotación y revocación de secretos y llaves;
- integridad de datos y protección frente a cambios no autorizados;
- respaldos, restauración probada, continuidad y objetivos de recuperación;
- parcheo, dependencias, endurecimiento y exposición de servicios;
- pruebas periódicas de eficacia y evidencia de correcciones.

El artículo 14 quinquies del régimen reformado exige medidas apropiadas al riesgo y menciona, entre otras, seudonimización, cifrado, resiliencia, restauración y evaluación regular. No presentes cada ejemplo como mandato absoluto e idéntico para todo sistema; documenta el análisis de riesgo.

### 5. RUT e identificadores nacionales

Trata el RUT como dato personal e identificador de alto impacto práctico, aunque no sea automáticamente dato sensible.

- No lo uses como contraseña, secreto, prueba única de identidad ni token de autorización.
- No lo expongas innecesariamente en URLs, logs, nombres de archivo, respuestas, objetos públicos o mensajes de error.
- Enmascáralo en interfaces y soporte cuando no se necesite completo.
- Separa su uso operacional de analítica e identificadores internos.
- Si seudonimizas, evita un hash simple y determinista: el espacio de valores facilita enumeración. Prefiere tokenización o una construcción con clave y controles de acceso, según el caso.
- Define quién puede consultar por RUT y limita la enumeración y extracción masiva.

Etiqueta estas medidas como controles técnicos derivados del riesgo y de los deberes generales, no como frases literales de la ley.

### 6. Direcciones IP, cookies, dispositivos y telemetría

Una IP, cookie o identificador de dispositivo es dato personal cuando permite vincular razonablemente actividad con una persona. Comprueba:

- finalidad y necesidad del registro;
- granularidad, truncamiento o agregación posible;
- plazo separado para logs de seguridad, producto y marketing;
- acceso a observabilidad y exportaciones;
- scripts y SDK de terceros realmente cargados;
- correlación entre identificadores y perfiles de cuenta;
- anonimización efectiva, no sólo eliminación del nombre.

No clasifiques toda IP como sensible ni toda estadística como anónima sin analizar la posibilidad razonable de reidentificación.

### 7. Logs, errores y observabilidad

Busca datos personales en:

- cuerpos y cabeceras HTTP;
- parámetros de consulta y rutas;
- volcados, trazas, capturas y mensajes de excepción;
- eventos de analítica y replay de sesiones;
- prompts y respuestas de IA;
- tickets, alertas y canales de chat.

Comprueba filtros o redacción antes de registrar, control de acceso, retención, exportación, ubicación y capacidad de investigar incidentes. No suprimas toda trazabilidad: minimiza el contenido manteniendo evidencia suficiente de seguridad y cumplimiento.

### 8. Conservación, supresión y respaldos

Comprueba:

- una regla por finalidad y categoría, no un único plazo genérico;
- ejecución automática, excepciones y propietario;
- propagación a réplicas, índices, cachés, proveedores y data lakes;
- tratamiento de respaldos hasta su sobreescritura segura;
- bloqueo o restricción cuando borrar inmediatamente sea improcedente;
- pruebas que demuestren que el dato deja de ser accesible por vías normales.

La eliminación lógica de la interfaz no prueba supresión de la base ni de terceros.

### 9. Derechos de titulares

Prueba de extremo a extremo:

- recepción y acuse;
- autenticación proporcionada, sin recolectar datos excesivos;
- búsqueda en todos los sistemas y alias;
- revisión de excepciones;
- respuesta completa y comprensible;
- modificación, supresión, oposición o bloqueo y su propagación;
- portabilidad cuando corresponda al régimen reformado;
- conservación de evidencia de la gestión.

Diseña alertas para los plazos del régimen aplicable. Bajo la reforma, el artículo 11 establece como regla treinta días corridos, prorrogables una vez por hasta treinta días; el bloqueo temporal tiene un plazo especial de dos días hábiles. Verifica el texto vigente antes de implementar.

### 10. Proveedores, nube y transferencias

Comprueba:

- quién decide fines y medios en la práctica;
- inventario de proveedores y subencargados;
- contrato, instrucciones, confidencialidad, seguridad, incidentes y destino al terminar;
- ubicaciones de cómputo, almacenamiento, soporte, telemetría y respaldo;
- accesos remotos transfronterizos;
- mecanismo jurídico de transferencia aplicable y su evidencia;
- cambios de proveedor y eliminación comprobada.

Un contrato no corrige un proveedor configurado para usar los datos con fines propios. Bajo la reforma, revisa los artículos 15, 15 bis y 27 a 29.

### 11. Desarrollo, pruebas e inteligencia artificial

Comprueba:

- sustitución de datos de producción por datos sintéticos o correctamente anonimizados;
- permisos y caducidad de copias temporales;
- prompts, archivos, embeddings, memorias, evaluaciones y logs;
- uso para entrenamiento o mejora por el proveedor;
- extracción, memorización o exposición en salidas;
- perfiles, puntuaciones y decisiones con efectos significativos;
- intervención humana real y capacidad de explicación o revisión;
- cambio de finalidad al reutilizar conversaciones o datasets.

El uso de un modelo externo puede añadir un encargado, un responsable o una transferencia; no lo clasifiques sólo por el nombre comercial del servicio.

### 12. Datos sensibles y categorías de mayor riesgo

Para salud, perfil biológico, biometría, menores, geolocalización, situación socioeconómica, vida sexual, orientación, identidad de género, creencias, afiliación o infracciones:

- confirma la clasificación legal exacta y la edad;
- identifica regla especial y excepción aplicable;
- reduce personas, sistemas y plazos con acceso;
- evita usos secundarios incompatibles;
- aumenta monitoreo, pruebas, segregación y respuesta;
- determina si corresponde evaluación de impacto previa.

No agrupes todas estas categorías bajo la etiqueta “sensible”: la ley distingue datos sensibles y categorías especiales con reglas diferentes.

## Evaluación de impacto

Bajo el régimen reformado, documenta una evaluación previa si el tratamiento probablemente produce alto riesgo. El artículo 15 ter la exige siempre en los supuestos allí enumerados: evaluación sistemática y exhaustiva basada en decisiones automatizadas o perfiles con efectos jurídicos significativos; tratamiento masivo o a gran escala; monitoreo sistemático de una zona pública; y datos sensibles o especialmente protegidos tratados bajo excepciones al consentimiento.

La evaluación debe incluir al menos operaciones y fines, necesidad y proporcionalidad, riesgos para titulares, medidas de mitigación, riesgo residual, responsables y decisión de salida. Verifica las orientaciones que publique la Agencia.

## Formato de hallazgo

Usa una fila por problema verificable:

| Campo | Contenido |
| --- | --- |
| ID y título | Identificador estable y conducta concreta. |
| Componente | Servicio, flujo, archivo, recurso o proveedor. |
| Evidencia | Hecho observado y localización; redacta valores personales o secretos. |
| Datos/titulares | Categorías y población afectada. |
| Estado | Cumple, parcial, no cumple, no verificado o no aplica. |
| Régimen | Vigente, futuro confirmado, proyecto o buena práctica. |
| Norma | Ley, artículo y elemento aplicable. |
| Riesgo | Escenario, probabilidad, impacto y prioridad técnica. |
| Encaje jurídico | Posible, probable o confirmado; categoría legal sólo si corresponde. |
| Corrección | Cambio mínimo y solución estructural. |
| Prueba | Criterio de aceptación reproducible. |

No uses “fuga” para una vulnerabilidad que aún no produjo salida o acceso no autorizado. Llámala exposición o debilidad potencial y explica el escenario.

## Decisión de salida

- **Listo dentro del alcance:** no quedan hallazgos críticos o altos abiertos y existe evidencia suficiente para los controles revisados. No equivale a certificación legal.
- **Listo con condiciones:** hay acciones delimitadas, riesgo residual aceptado por quien corresponde y fecha de cierre.
- **Bloqueado:** existe tratamiento manifiestamente sin fundamento, exposición activa, riesgo crítico no mitigado, falta de control imprescindible o evaluación previa legalmente necesaria no realizada.
- **No evaluable:** faltan artefactos esenciales; enuméralos.

La decisión debe mencionar alcance, fecha y responsable de aceptar el riesgo. Nunca uses una etiqueta de salida para garantizar ausencia de vulnerabilidades o cumplimiento total.
