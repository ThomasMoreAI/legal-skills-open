# F2 — Los diez dominios de auditoría

Cada dominio: **qué se pregunta**, **cómo se detecta**, **qué constituye hallazgo**.
Recorre en orden; escribe cada hallazgo a `hallazgos.jsonl` apenas lo confirmes.

Los criterios legales viven en el skill hermano
(`${CLAUDE_PLUGIN_ROOT}/skills/chile-datos-personales/references/`). Aquí está el
método de detección.

Los comandos usan las variables definidas al inicio de `barrido.md` — expórtalas
antes en la misma sesión de shell:

```bash
EXCL="--exclude-dir=.git --exclude-dir=node_modules --exclude-dir=vendor \
--exclude-dir=dist --exclude-dir=build --exclude-dir=coverage --exclude-dir=.next \
--exclude-dir=.venv --exclude-dir=__pycache__"
SRC="--include=*.ts --include=*.js --include=*.py --include=*.php \
--include=*.rb --include=*.sql --include=*.prisma"
```

Y rige la misma regla de `barrido.md`: **un patrón nunca se parte en varias líneas**
(un `-e` por línea, `\` fuera de las comillas). Partirlo hace que grep lo lea como
alternativas, y el comando falla en silencio o devuelve el repositorio entero.

---

## D1 — Inventario de datos personales

**Pregunta:** ¿qué datos de personas trata realmente este sistema?

Es el dominio fundacional: sin inventario, los otros nueve no tienen sobre qué
razonar. Y para muchos equipos es el entregable más valioso de toda la auditoría,
porque nadie lo tenía.

**Método.** Recorre la lista de modelos de la F1. Por cada campo, clasifica con
`clasificacion-datos.md`. Cruza con el esquema real de la base (F1.9) para
encontrar columnas que el código no revela: campos `TEXT` que en producción reciben
RUT, diagnósticos o montos.

Escribe el resultado en `docs/privacidad/inventario.md` (formato en `plantillas.md`
del skill hermano).

**Hallazgos:**

| Condición | Severidad |
|---|---|
| Datos sensibles tratados sin que el equipo los reconozca como tales | ALTA |
| Campo personal sin finalidad identificable | MEDIA |
| Campo de texto libre que recibe datos sensibles sin control | ALTA |
| Sistema sin inventario de datos personales | MEDIA |

> Lo que más aparece: `renta`, `tramo`, `isapre`, `deuda`, `score` tratados como
> campos ordinarios. En Chile son **sensibles**. Casi siempre es el hallazgo ALTO
> más numeroso de la auditoría.

---

## D2 — Bases de licitud y consentimiento

**Pregunta:** ¿por qué el sistema puede tratar estos datos, y puede demostrarlo?

**Método.**

```bash
grep -rniE $EXCL \
  -e '\b(consent|consentimiento|privacy_policy|politica_privacidad)\b' \
  -e '\b(acepta|acepto|terminos|opt_?in|revoke|revoc)\w*\b' \
  .
```

Revisa: ¿existe tabla o campo de consentimiento? ¿es un booleano global o hay una
fila por finalidad? ¿se versiona el texto aceptado? ¿existe camino de revocación, y
la revocación **efectivamente detiene** el tratamiento?

Rastrea la revocación hasta el final: un `revoked_at` que nadie consulta antes de
enviar el correo de marketing es peor que no tenerlo, porque simula cumplimiento.

**Hallazgos:**

| Condición | Severidad |
|---|---|
| Consentimiento como booleano único para varias finalidades | ALTA |
| Consentimiento sin evidencia (sin fecha, versión ni canal) | ALTA |
| Revocación registrada que no detiene el tratamiento | ALTA |
| Dato recolectado para una finalidad y usado para otra | ALTA |
| Casilla premarcada o consentimiento agrupado en la interfaz | ALTA |
| Base de licitud no documentada | MEDIA |
| Datos sensibles sin consentimiento expreso ni excepción identificable | CRÍTICA |

La reutilización de finalidad se detecta cruzando: ¿dónde se usa `email` además de
autenticar? ¿Aparece en un job de campañas, en un export a un CRM, en un webhook?

---

## D3 — Exposición y autorización

**Pregunta:** ¿quién puede ver datos de quién?

El dominio que produce los CRÍTICOS. Un fallo aquí no es un incumplimiento
documental: es exposición efectiva de datos.

**Método.** Para cada endpoint de la F1 con `:id` o que devuelve listados:

```bash
# lecturas por id sin filtro — candidatos a IDOR/BOLA
grep -rnE $EXCL $SRC --exclude-dir=__tests__ \
  -e 'findByPk\(|findById\(|get_object_or_404|findOne\(\s*\{\s*id' \
  -e '\.find\([^)]*params\.id|::find\(|::findOrFail\(' \
  . | grep -vE '\.(test|spec)\.'

# tenant tomado del cliente en vez del contexto autenticado
#   \S{0,3} cubre .tenantId, ["tenantId"] y ['tenantId'] sin pelear con comillas
grep -rniE $EXCL \
  -e '(req|request)\.(body|query|params|headers)\S{0,3}(tenant|company|organization|empresa|club|account|org)_?id' \
  .

# rutas sin middleware de autenticación aparente
grep -rnE $EXCL --include=*.ts --include=*.js \
  -e '(router|app)\.(get|post|put|patch|delete)\(' \
  . | grep -viE 'auth|guard|protect|requiere|verify|jwt|session'
```

Para cada candidato, **abre el archivo y lee el contexto**: puede haber un
middleware global, un guard de clase, o una política de fila. Eso es F3, pero
anótalo aquí.

**Hallazgos:**

| Condición | Severidad |
|---|---|
| Acceso cruzado entre tenants confirmado | CRÍTICA |
| IDOR sobre datos personales o documentos | CRÍTICA |
| Endpoint con datos personales sin autenticación | CRÍTICA |
| `tenant_id` proveniente del cliente | CRÍTICA |
| Rol de administrador con acceso irrestricto no justificado | ALTA |
| Autorización solo en frontend | ALTA |
| Sin registro de accesos a datos sensibles | ALTA |

---

## D4 — Salidas y minimización

**Pregunta:** ¿qué sale del sistema que no debería salir?

**Método.**

```bash
# serialización del modelo completo
grep -rnE $EXCL $SRC \
  -e '(res|response)\.(json|send)\(\s*(usuario|user|paciente|cliente|persona|empleado|alumno|rows?|records?|result)\s*\)' \
  -e 'return\s+(usuario|user|paciente|cliente)\s*;' \
  -e 'JsonResponse\([^)]*__dict__|->toArray\(\)|serialize\(\)|model_to_dict\(' \
  .

# asignación masiva
grep -rnE $EXCL \
  -e '\.(update|create|build|set|bulkCreate)\(\s*(req|request)\.body' \
  -e 'fill\(\$request->all\(\)\)|\$request->all\(\)' \
  -e '\*\*request\.(data|POST)|Object\.assign\(' \
  .

# consultas sin proyección — el origen de la sobre-exposición
grep -rniE $EXCL $SRC \
  -e 'select\s+\*\s+from' \
  -e '\.(findAll|findOne|findByPk)\(' \
  . | grep -viE 'attributes\s*:|select\s*:|\.pluck\(|only\('
```

Revisa además: ¿los endpoints de búsqueda de personas tienen largo mínimo,
paginación con tope y rate limit? ¿las exportaciones exigen un permiso distinto del
de lectura y quedan auditadas con la cantidad de registros?

**Hallazgos:**

| Condición | Severidad |
|---|---|
| Respuesta que incluye `password_hash`, tokens o datos sensibles innecesarios | CRÍTICA |
| Exportación masiva sin auditoría ni permiso específico | ALTA |
| Asignación masiva sobre entidad con campos de privilegio o PII | ALTA |
| Búsqueda de personas sin controles anti-extracción | ALTA |
| Serialización del modelo completo hacia el cliente | MEDIA |
| Respuesta con más campos de los que la vista usa | MEDIA |

---

## D5 — Terceros, transferencias internacionales e IA

**Pregunta:** ¿a dónde salen los datos y bajo qué respaldo?

**Método.** Toma la lista de integraciones de la F1. Por cada una, sigue el código
hasta la llamada real y anota **qué objeto se envía**. El patrón a cazar:

```bash
grep -rnE $EXCL \
  -e '\.(send|track|identify|capture|createCompletion)\(\s*(usuario|user|cliente|paciente|data|payload|record)\b' \
  -e '(messages|chat\.completions)\.create\(' \
  -e '(axios|fetch)\.?(post|put)?\([^)]*,\s*(usuario|user|cliente|paciente|payload|record)\s*[,)]' \
  .
```

Para IA: ¿qué se incluye en el prompt? ¿hay un `SELECT *` alimentándolo? ¿el
resultado del modelo sobre una persona se guarda, y está clasificado?

Para transferencias: región de cada proveedor, y si existe contrato. Casi todo
proveedor cloud implica salida de Chile — el hallazgo no es que ocurra, sino que
**no esté identificada**.

**Hallazgos:**

| Condición | Severidad |
|---|---|
| Datos sensibles enviados a un tercero sin base de licitud identificable | CRÍTICA |
| Objeto completo del usuario enviado a un tercero | ALTA |
| Base de datos o `SELECT *` alimentando un LLM | ALTA |
| Transferencia internacional no identificada ni documentada | ALTA |
| Salida del modelo sobre personas sin clasificar ni retención | MEDIA |
| Decisión automatizada relevante sin revisión humana ni explicación | ALTA + evaluación de impacto |

---

## D6 — Registro: logs y telemetría

**Pregunta:** ¿dónde se está copiando PII sin que nadie lo haya decidido?

El dominio más subestimado. Los logs se replican a agregadores, se retienen meses y
tienen menos control de acceso que la base de datos que protegen.

**Método.** Sobre los puntos de logging de la F1, busca los que registran objetos
completos:

```bash
# logs que registran el objeto completo
grep -rniE $EXCL --include=*.ts --include=*.js --include=*.py --include=*.php \
  -e '(console|logger|log|Log)[^(]{0,20}\([^)]*(req|request)\.(body|headers|query|user)' \
  -e '(console|logger|log|Log)[^(]{0,20}\([^)]*\{\s*(user|usuario|cliente|paciente|data|payload|token)\s*[,}]' \
  -e '(console|logger|log|Log)[^(]{0,20}\([^)]*(error\.response|err\.config|e\.response)' \
  .

# ¿hay sanitización configurada?  La AUSENCIA es el hallazgo
grep -rnE $EXCL -e 'beforeSend|scrubFields|redact|sanitize|mask' .

# opt-in explícito a ENVIAR PII — significa lo contrario que el comando anterior
grep -rniE $EXCL \
  -e 'sendDefaultPii\s*:\s*true|send_default_pii\s*=\s*True' \
  -e 'maskAllInputs\s*:\s*false|recordInputs\s*:\s*true|captureBody' \
  .
```

En monitoreo de errores, la ausencia de `beforeSend` (o equivalente) con un
proyecto que usa Sentry/Datadog **es** el hallazgo.

Revisa también grabación de sesión: `maskAllInputs` desactivado en una página con
formularios de salud o financieros es exposición directa.

**Hallazgos:**

| Condición | Severidad |
|---|---|
| Contraseñas, tokens o cabeceras de autorización en logs | CRÍTICA |
| Datos sensibles en logs o en monitoreo de errores | ALTA |
| Monitoreo de errores sin sanitización configurada | ALTA |
| Grabación de sesión sin enmascarar campos | ALTA |
| RUT completo o correo en logs | MEDIA |
| Telemetría activada sin revisión de qué captura | MEDIA |

---

## D7 — Ciclo de vida: retención, eliminación, ambientes

**Pregunta:** ¿qué pasa con los datos con el tiempo?

**Método.**

```bash
# estados del ciclo de vida — 'estado'/'status' solo como declaración de campo,
# porque sueltos aparecen en cada respuesta HTTP del repositorio
grep -rniE $EXCL $SRC \
  -e '\bdeleted_at\b|soft_?delete|\bparanoid\b|\bdestroy\(\s*\{?\s*force' \
  -e '\b(is_active|activo|habilitado|vigente|bloqueado|anonimizado)\b' \
  -e '\b(estado|status)\b\s*[:=]|\b(estado|status)\s+(VARCHAR|ENUM|CHAR)' \
  .

# retención y anonimización
grep -rniE $EXCL \
  -e '\b(retention|retencion|purge|purgar|cleanup|expire|caduc\w*)\b' \
  -e '\b(anonym\w*|anonim\w*|pseudonym\w*|seudonim\w*)\b' \
  .

# poblamiento de ambientes
grep -rniE $EXCL \
  -e 'pg_dump|mysqldump|dump\.sql|\bbackup\b' \
  -e '\b(seed|seeder|fixture|faker)\w*\b' \
  .
```

Preguntas concretas: ¿hay alguna política de retención implementada, o solo
`deleted_at`? ¿eliminar un titular elimina también sus archivos, exportaciones,
índices y caches? ¿los seeds usan datos sintéticos o un volcado real? ¿los estados
del ciclo de vida (`activo`/`bloqueado`/`anonimizado`/`eliminado`) tienen semántica
definida, o son banderas acumuladas?

**Hallazgos:**

| Condición | Severidad |
|---|---|
| Volcado de producción usado en desarrollo o testing | CRÍTICA |
| Ninguna categoría de datos tiene política de retención | ALTA |
| Eliminación que deja archivos, exportaciones o índices con PII | ALTA |
| "Anonimización" reversible (hash de RUT, seudonimización presentada como anónima) | ALTA |
| `deleted_at` presentado como cumplimiento del derecho de supresión | MEDIA |
| Estados del ciclo de vida sin semántica definida | MEDIA |
| Backups sin cifrado o sin retención documentada | MEDIA |

---

## D8 — Derechos del titular

**Pregunta:** ¿el sistema permite ejercer los seis derechos?

**Método.** No busques pantallas: **prueba el esquema**. Para un titular
cualquiera, intenta responder con consultas reales:

1. ¿Puedo listar todo lo suyo, incluyendo archivos, colas, caches e índices?
2. ¿Puedo eliminarlo sin romper integridad referencial?
3. ¿Puedo **bloquear** sin eliminar? (el que casi nunca existe)
4. ¿Puedo exportarlo en formato estructurado, no solo PDF?
5. ¿Puedo decir quién accedió a sus datos?

Cada "no" es un hallazgo. Anota la consulta que lo demuestra: eso es la evidencia.

**Hallazgos:**

| Condición | Severidad |
|---|---|
| Imposible localizar todos los datos de un titular | ALTA |
| Sin mecanismo de bloqueo (solo activo/eliminado) | MEDIA |
| Portabilidad solo como PDF, o inexistente | MEDIA |
| Sin proceso de eliminación que cubra derivados | ALTA |
| Sin auditoría de accesos → derecho de acceso incompleto | ALTA |
| Datos dispersos en sistemas satélite sin clave común | ALTA |

Sube un nivel cuando los datos involucrados sean sensibles o de NNA.

---

## D9 — Infraestructura, secretos e historial

**Pregunta:** ¿hay datos o credenciales donde no deberían estar?

**Método.** Lo de la F1.7 y F1.8. Además:

```bash
# secretos en el árbol actual — con -i, porque las claves suelen ir en MAYÚSCULAS
grep -rniE $EXCL \
  -e '^[a-z0-9_]*(api_?key|secret|token|password|passwd|dsn|credentials|access_?key)[a-z0-9_]*\s*[:=]\s*\S{12,}' \
  -e '(api[_-]?key|secret|passwd|password|token|private[_-]?key|access[_-]?key)[a-z0-9_]*\s*[:=]\s*.{0,2}[A-Za-z0-9/+=_.@-]{16,}' \
  -e '(AKIA[0-9A-Z]{16}|sk-[A-Za-z0-9-]{20,}|SG\.[A-Za-z0-9_-]{20,}|ghp_[A-Za-z0-9]{30,}|xox[baprs]-[A-Za-z0-9-]{10,})' \
  -e 'BEGIN (RSA |EC |OPENSSH |PGP )?PRIVATE KEY' \
  . | grep -vE '\.example|\.sample|\.dist:|process\.env|os\.environ|ENV\[|getenv|<%=|\$\{'

# buckets y almacenamiento público
grep -rniE $EXCL --include=*.tf --include=*.yml --include=*.yaml --include=*.json \
  -e 'public[_-]?read|acl.{0,10}public|BlockPublicAcls.{0,10}false|allUsers' \
  .
```

**Hallazgos:**

| Condición | Severidad |
|---|---|
| Secreto activo versionado (árbol o historial) | CRÍTICA — avisar de inmediato |
| Almacenamiento con documentos personales expuesto públicamente | CRÍTICA |
| Datos personales en el historial de git | ALTA |
| Ambientes compartiendo credenciales o recursos | ALTA |
| Región cloud fuera de Chile sin identificar como transferencia | ALTA |
| Sin separación entre ambientes | MEDIA |

---

## D10 — Sensibles y NNA (transversal)

**Pregunta:** ¿el sistema trata datos que exigen protección reforzada, y la tiene?

Se recorre **al final**, releyendo los nueve dominios anteriores con este filtro:
cada hallazgo que recae sobre datos sensibles o de NNA **sube un nivel de
severidad**.

**Método adicional.**

```bash
grep -rniE $EXCL \
  -e '\b(menor|nino|nina|adolescente|alumno|estudiante|apoderado|tutor)\w*\b' \
  -e '\b(hijo|representante_legal|fecha_nac|edad|curso|colegio|matricula)\w*\b' \
  .
```

Si aparece cualquiera: ¿se guarda fecha de nacimiento o solo un flag? ¿está modelada
la representación legal y cómo se acredita? ¿hay autorizaciones separadas por
finalidad (foto, ubicación, salud)? ¿qué pasa cuando el titular cumple 18?

**Hallazgos:**

| Condición | Severidad |
|---|---|
| Datos de NNA sin registro de autorización del representante | ALTA |
| Foto, ubicación o salud de menores sin autorización específica | ALTA |
| Representación legal acreditada solo con una casilla declarativa | ALTA |
| `es_menor` como booleano en vez de fecha de nacimiento | MEDIA |
| Sin transición definida al cumplir la mayoría de edad | MEDIA |
| Datos sensibles sin cifrado ni auditoría de acceso | ALTA |

Cuando el sistema haga perfilamiento, biometría, decisiones automatizadas
relevantes, o trate datos de salud o de NNA a escala, agrega al informe una
recomendación de **evaluación de impacto** y marca `REVISIÓN LEGAL REQUERIDA`.

---

## Cobertura

Al cerrar la F2, registra en `estado.json` por dominio: superficies revisadas sobre
el total, hallazgos abiertos, y qué quedó sin revisar. Si un dominio quedó parcial,
**dilo en el informe**: una cobertura declarada al 60% es información útil; una
cobertura silenciosa del 60% presentada como completa es un informe falso.
