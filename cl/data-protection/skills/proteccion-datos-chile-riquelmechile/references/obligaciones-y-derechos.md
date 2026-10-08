# Obligaciones, licitud y derechos — Ley 21.719

Usa esta referencia para el régimen que comienza el **01-DIC-2026**. Para hechos anteriores, vuelve a `marco-y-vigencia.md`.

## Principios — artículo 3

Convierte cada principio en una pregunta de evidencia:

| Principio | Pregunta de auditoría | Evidencia útil |
|---|---|---|
| licitud y lealtad | ¿puede acreditarse por qué cada tratamiento es lícito? | matriz finalidad/base de licitud, contratos, consentimiento |
| finalidad | ¿la finalidad es específica, explícita y lícita? | aviso, especificación funcional, registro de cambios |
| proporcionalidad | ¿se recolecta sólo lo necesario y se conserva sólo lo necesario? | esquema de datos, retención, purgas, anonimización |
| calidad | ¿los datos son exactos, completos, actuales y pertinentes? | validaciones, rectificación, reconciliación |
| responsabilidad | ¿el responsable puede demostrar cumplimiento? | controles, owners, evidencias, revisiones |
| seguridad | ¿el nivel de protección corresponde al riesgo? | IAM, cifrado, backups, pruebas, incidentes |
| transparencia e información | ¿el titular entiende qué ocurre y puede ejercer derechos? | política, avisos, canales, trazabilidad |
| confidencialidad | ¿acceso y uso están limitados y sujetos a secreto? | NDA/cláusulas, RBAC, logs, formación |

## Consentimiento — artículo 12

Cuando sea la base de licitud, verifica que el consentimiento sea:

- libre;
- informado;
- específico respecto de su finalidad o finalidades;
- previo;
- inequívoco, mediante declaración o acción afirmativa clara.

Debe poder revocarse por medios similares o equivalentes a los usados para otorgarlo; esos medios deben ser expeditos, fidedignos, gratuitos y permanentemente disponibles. El responsable debe poder probar que contó con consentimiento y que el tratamiento fue lícito, leal y transparente.

**Anti-pattern:** no fuerces consentimiento dentro de un contrato o servicio cuando el tratamiento no sea necesario para esa prestación y luego lo presentes como libre.

## Otras bases de licitud — artículo 13

No preguntes siempre “¿hay consentimiento?”. Evalúa la base correcta por finalidad. La ley contempla, entre otros supuestos:

- tratamiento de obligaciones económicas/financieras/bancarias/comerciales sujeto al Título III;
- obligación legal o disposición de la ley;
- celebración/ejecución de contrato o medidas precontractuales solicitadas por el titular;
- interés legítimo del responsable o de un tercero, sujeto a que no prevalezcan derechos y libertades del titular y al deber de informar;
- formulación, ejercicio o defensa de derechos ante tribunales u órganos públicos.

El responsable debe **acreditar la licitud**. En un gap analysis, una base escrita sin justificación ni evidencia queda `NO VERIFICADO`.

## Derechos — artículos 4 a 10

El titular dispone, según condiciones legales, de:

- acceso;
- rectificación;
- supresión;
- oposición;
- portabilidad;
- bloqueo temporal del tratamiento.

Los derechos son personales, intransferibles e irrenunciables. La portabilidad exige revisar los requisitos específicos del artículo 9 y no equivale automáticamente a supresión.

## Procedimiento y plazos — artículo 11

### Solicitud ordinaria

El canal puede ser correo electrónico, formulario de contacto o medio electrónico equivalente. Debe existir autenticación conforme al marco que establezca la Agencia.

**Plazo del responsable:** debe acusar recibo y pronunciarse **a más tardar dentro de 30 días corridos** desde el ingreso. El plazo puede ser **prorrogado una sola vez hasta por otros 30 días corridos**.

Conserva evidencia de:

- recepción;
- identidad/autenticación aplicada;
- fecha de respuesta;
- destinatario;
- contenido íntegro enviado;
- fundamento de una denegación total o parcial.

Si se deniega o no se responde dentro del plazo, el titular puede reclamar ante la Agencia dentro de los plazos legales; la respuesta negativa debe informar esa posibilidad.

### Bloqueo temporal asociado a rectificación, supresión u oposición

Cuando se solicita fundadamente bloqueo temporal, el responsable debe responder **dentro de 2 días hábiles** desde la recepción. Mientras resuelve esa solicitud, no debe tratar los datos comprendidos en el requerimiento; el bloqueo no impide su almacenamiento.

**No mezcles** este plazo especial de 2 días hábiles con el plazo ordinario de 30 días corridos.

## Transparencia — artículo 14 ter

El responsable debe mantener permanentemente disponible, en web o medio equivalente, información que permita entender y ejercer derechos. El inventario de transparencia debe cubrir, como mínimo legalmente pertinente:

- política de tratamiento, fecha y versión;
- identidad del responsable y representante legal;
- identificación del encargado de prevención si existe;
- domicilio/correo/formulario u otro canal accesible para solicitudes;
- categorías de datos y universo de titulares;
- destinatarios previstos;
- finalidades y bases de legitimidad, incluidos intereses legítimos cuando corresponda;
- política y medidas de seguridad comunicables sin degradar la seguridad;
- derechos del titular y posibilidad de recurrir a la Agencia;
- transferencias internacionales, adecuación o garantías cuando proceda;
- periodo de conservación;
- origen de los datos y si provienen de fuentes de acceso público;
- posibilidad de retirar consentimiento cuando ésa sea la base;
- existencia de decisiones automatizadas/perfilamiento y la información exigible sobre su lógica y consecuencias.

No publiques secretos de seguridad para “cumplir transparencia”. Describe controles al nivel necesario sin crear una vulnerabilidad.

## Privacidad desde el diseño y por defecto — artículo 14 quáter

Antes y durante el tratamiento, exige medidas técnicas y organizativas considerando estado de la técnica, costos, naturaleza, ámbito, contexto, finalidades y riesgo. Por defecto deben tratarse sólo los datos específicos y estrictamente necesarios, considerando cantidad, extensión, retención y accesibilidad.

En software, esto se traduce en requisitos verificables: campos mínimos, defaults restrictivos, retención explícita, permisos mínimos y diseño de derechos antes de producción.

## Categorías especiales

### Datos sensibles

No trates “dato sensible” como sinónimo informal de “dato confidencial”. Usa la definición legal y las reglas especiales aplicables. Salud, perfil biológico, biometría, origen étnico/racial, afiliaciones, convicciones y aspectos de vida/orientación/identidad sexual, entre otros definidos por la ley, requieren análisis reforzado.

### Biometría — artículo 16 ter

Cuando corresponda, verifica información específica sobre:

- sistema biométrico utilizado;
- finalidad específica;
- periodo de utilización;
- forma de ejercer derechos.

No almacenes plantillas o imágenes biométricas “por si acaso”. La minimización y la necesidad deben poder demostrarse.

### Niños, niñas y adolescentes — artículo 16 quáter

- Todo tratamiento debe atender al interés superior y autonomía progresiva.
- Para **niños y niñas menores de 14 años**, el consentimiento corresponde a padres, representantes legales o quien tenga su cuidado personal, salvo autorización o mandato legal.
- Los datos de adolescentes se rigen en general por las reglas de autorización de adultos.
- Para **datos sensibles de adolescentes menores de 16 años**, se requiere el consentimiento de padres, representantes legales o quien tenga el cuidado personal, salvo autorización o mandato legal.
- A efectos de esta ley, adolescente es la persona mayor de 14 y menor de 18 años.

En productos digitales, verifica edad, experiencia de consentimiento, lenguaje, perfilamiento, publicidad, defaults, compartición con terceros y seguridad. No inventes métodos de verificación de edad si la Agencia o norma sectorial debe definirlos.
