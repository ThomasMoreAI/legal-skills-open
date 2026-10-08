# Terceros, transferencias internacionales e IA

Casi toda arquitectura moderna envía datos personales fuera del sistema que los
recolectó: un proveedor cloud, una herramienta de analítica, un modelo de
lenguaje. Nada de eso está prohibido. Lo que exige la ley es que esté
**identificado**: qué sale, hacia dónde, bajo qué respaldo, y con qué
minimización.

Este archivo da el criterio. Dos referencias del skill `implementar-ley-21719`
lo llevan a registro estructurado: `shared/arquitectura/registro-ia.md` para
IA (decisión automatizada, human-in-the-loop, opt-out de entrenamiento) y
`shared/rules/analytics-tracking.md` para las herramientas de analítica y
tracking, que son el caso más frecuente de integración sin revisión.

## El patrón a cazar

Por cada integración de la F1 del skill hermano (`auditoria-ley-21719`) o por
cada dependencia nueva que un cambio agregue, sigue el dato hasta la llamada
real y responde:

```
¿Qué objeto se envía?        el modelo completo, o los campos mínimos?
¿A quién?                     nombre del proveedor y función que cumple
¿Dónde procesa?                región / país del proveedor
¿Bajo qué respaldo?            adecuación, cláusulas contractuales, certificación
¿Hay contrato u encargo de     el proveedor es encargado, no dueño de los datos
  tratamiento vigente?
```

Si no puedes responder las cinco, el hallazgo no es "hay una transferencia
ilícita" — es "hay una transferencia no identificada", que es el hallazgo real
y el más frecuente.

## Transferencias internacionales

Son lícitas, entre otras vías, cuando el país de destino ofrece un nivel
adecuado de protección, cuando median cláusulas contractuales con garantías
suficientes, o mediante modelos de certificación o normas vinculantes
equivalentes. Verifica el listado exacto de vías en el articulado antes de
afirmar cuál aplica a un proveedor concreto — este archivo da el criterio de
ingeniería, no la calificación legal.

Señales a buscar en el código y la infraestructura:

```bash
# regiones cloud — cualquier región fuera de Chile es transferencia
grep -rniE --exclude-dir=.git --exclude-dir=node_modules \
  --include=*.tf --include=*.yml --include=*.yaml --include=*.env* \
  -e '(us|eu|ap|sa)-(east|west|north|south|central)-[0-9]' \
  -e '\b(region|location|zone)\b\s*[:=]' \
  .
```

Casi todo proveedor cloud chileno usa una región fuera de Chile (`us-east-1`,
`sa-east-1` en Brasil, etc.). Eso no es en sí mismo un hallazgo: el hallazgo es
que nadie lo documentó como transferencia internacional con su respaldo.

Registro mínimo por proveedor (alimenta `docs/privacidad/inventario.md`):

```
proveedor            p. ej. AWS S3, SendGrid, OpenAI
funcion              qué hace con el dato
region_procesamiento
datos_que_recibe     categorías, no valores
respaldo             adecuación | cláusulas contractuales | certificación
contrato_vigente     sí / no / fecha de revisión
```

## Encargados de tratamiento

Un proveedor que procesa datos personales por cuenta de la organización es un
**encargado de tratamiento**, no un tercero cualquiera. Eso implica un
instrumento contractual (contrato o cláusulas de encargo) que fije finalidad,
duración, obligaciones de seguridad y destino del dato al terminar la relación.

Que el proveedor tenga su propia política de privacidad no reemplaza el
contrato de encargo entre las partes. Si el proyecto no tiene ese contrato con
un proveedor que procesa datos personales, es `REVISIÓN LEGAL REQUERIDA`, no
un hallazgo técnico que puedas cerrar solo.

## Inteligencia artificial

Dos preguntas separan un uso razonable de un hallazgo:

### Qué entra al prompt

```bash
grep -rnE --exclude-dir=.git --exclude-dir=node_modules \
  -e '\.(send|track|identify|capture|createCompletion)\(\s*(usuario|user|cliente|paciente|data|payload|record)\b' \
  -e '(messages|chat\.completions)\.create\(' \
  .
```

- ¿El prompt incluye el objeto completo de un usuario, o campos seleccionados?
- ¿Hay un `SELECT *` alimentando el contexto de un LLM? Es el patrón más común
  de sobre-exposición: nadie decidió mandar la tabla completa, simplemente era
  lo que ya estaba en memoria.
- ¿El proveedor de IA retiene el prompt para entrenamiento por defecto?
  Verifica la configuración del proveedor (`opt-out` de entrenamiento suele
  requerir un flag explícito o un plan empresarial).

### Qué sale y qué se guarda

- ¿La respuesta del modelo sobre una persona se persiste? Si sí, tiene la
  misma clasificación que el dato de entrada y entra al inventario con su
  propia retención.
- ¿Hay una decisión automatizada con efecto relevante sobre una persona
  (crédito, empleo, beneficio, precio) tomada o influida por el modelo, sin
  revisión humana? Eso es hallazgo ALTO como mínimo y dispara evaluación de
  impacto (ver `revisiones.md`, sección D).
- ¿El resultado se usa para perfilar o puntuar personas de forma sistemática?
  Mismo disparador.

> Un modelo de lenguaje no es una excepción a la minimización: es un
> destinatario más, con el agravante de que el prompt suele armarse rápido y
> sin pasar por el mismo DTO que protege una respuesta HTTP.

## Registro y telemetría hacia terceros

Analítica, monitoreo de errores, grabación de sesión y widgets embebidos son
salidas hacia terceros tan reales como una llamada de API, y las más fáciles de
pasar por alto porque llegan por defecto en el SDK.

```bash
# SDKs con salida de datos por defecto
grep -inE '"@?(sentry|datadog|newrelic|mixpanel|amplitude|segment|hotjar|fullstory|logrocket|posthog|google-analytics|gtag|intercom|zendesk|hubspot)' \
  package.json composer.json requirements.txt pyproject.toml Gemfile

# ¿hay sanitización configurada? — la AUSENCIA es el hallazgo
grep -rnE --exclude-dir=.git --exclude-dir=node_modules \
  -e 'beforeSend|before_send|scrubFields|denyUrls' \
  -e 'maskAllInputs|maskTextSelector|redact' \
  .

# opt-in EXPLÍCITO a enviar PII — lo contrario de sanitizar
grep -rniE --exclude-dir=.git --exclude-dir=node_modules \
  -e 'sendDefaultPii\s*:\s*true|send_default_pii\s*=\s*True' \
  -e 'maskAllInputs\s*:\s*false|recordInputs\s*:\s*true|captureBody' \
  .
```

Reglas concretas:

- **Monitoreo de errores** (Sentry, Datadog, etc.): `sendDefaultPii: false` y un
  `beforeSend` que elimine cookies, cabeceras de autorización y el cuerpo del
  request antes de enviar el evento. La ausencia de `beforeSend` en un proyecto
  que usa uno de estos SDK **es** el hallazgo, no una duda a descartar.
- **Grabación de sesión** (Hotjar, FullStory, LogRocket): `maskAllInputs` y
  enmascaramiento de texto activados por defecto en cualquier página con
  formularios de salud, financieros o de datos sensibles. Desactivarlo para
  "ver mejor los bugs" es una decisión que debería quedar documentada, no
  implícita en la configuración.
- **Analítica** (Google Analytics, Mixpanel, Segment, Amplitude): revisa qué
  propiedades viajan en cada evento. `identify(userId, { email, telefono,
  renta })` manda datos personales y potencialmente sensibles a un tercero de
  analítica sin que nadie lo haya decidido como tal.
- **Widgets embebidos** (chat, mapas, captcha): cargan scripts de terceros que
  ven la página completa, formularios incluidos. Verifica qué proveedor es y
  si hay alternativa que no requiera cargar el script en páginas con datos
  sensibles.

Ver también `derechos-y-ciclo-de-vida.md`, sección de logs de aplicación, para
la lista de campos que nunca deben salir en texto plano hacia ningún destino,
tercero incluido.

## Registro de terceros — qué guardar

Mínimo por integración, para `docs/privacidad/inventario.md`:

```
proveedor
proposito             analítica | monitoreo de errores | pagos | IA | email
datos_enviados        categorías, no el payload real
base_licitud
respaldo_transferencia
configuracion_privacidad   qué sanitización o minimización tiene activada
revisado
```

Este registro es el que responde, en una fiscalización o ante un titular que
pregunta "¿con quién comparten mis datos?", sin tener que reconstruirlo desde
el código.
