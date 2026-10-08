# F1 — Barrido de superficies

El objetivo no es leer el código: es **enumerar lo que hay que revisar**. Sin esta
lista no existe noción de cobertura, y una auditoría sin cobertura declarada no
sirve como evidencia.

Todos los comandos son de solo lectura.

> ## Regla de edición — no la rompas
>
> **Una expresión regular nunca se parte en varias líneas.** GNU grep interpreta un
> salto de línea dentro del patrón como separador de alternativas, y eso produce
> tres fallas, todas silenciosas o peores:
>
> - un `(` abierto en una línea y cerrado en otra → `Unmatched ( or \(`, salida
>   vacía, exit 2 — y si el comando lleva `2>/dev/null`, **el error desaparece y
>   parece que no hay hallazgos**;
> - una línea que termina en `|` → alternativa vacía → **coincide con todo el
>   repositorio**;
> - el resto → dos patrones independientes que no significan lo que parecen.
>
> Para partir un patrón largo, usa **un `-e` por línea** (grep hace OR entre ellos)
> y continuación de shell `\` **fuera** de las comillas. Todos los comandos de este
> archivo siguen esa forma. Si "mejoras la legibilidad" juntándolos, los rompes.
>
> Usa `--exclude-dir` repetido, nunca `--exclude-dir={a,b,c}`: la expansión de
> llaves no existe en `sh`/dash y el filtro deja de aplicarse **sin avisar**.

Para abreviar, en este archivo:

```bash
EXCL="--exclude-dir=.git --exclude-dir=node_modules --exclude-dir=vendor \
--exclude-dir=dist --exclude-dir=build --exclude-dir=coverage --exclude-dir=.next \
--exclude-dir=.venv --exclude-dir=__pycache__"
SRC="--include=*.ts --include=*.js --include=*.py --include=*.php \
--include=*.rb --include=*.sql --include=*.prisma"
```

Excluir `.git` no es cosmético: sin eso, cada comando agrega cientos o miles de
líneas de objetos internos de git a la salida.

## 0. Identificar el stack

```bash
ls package.json composer.json requirements.txt pyproject.toml go.mod \
   Gemfile pom.xml build.gradle *.csproj 2>/dev/null
head -60 package.json 2>/dev/null
git rev-parse --abbrev-ref HEAD && git log --oneline -1
```

Anota: lenguaje, framework, ORM, motor de base de datos, si es multi-tenant, si hay
frontend separado, si hay app móvil.

## 1. Modelos y esquema

```bash
find . -path ./node_modules -prune -o \
  \( -path '*migrat*' -o -path '*models*' -o -path '*entit*' -o -name 'schema.prisma' \) -print
```

```bash
# columnas candidatas a PII
grep -rniE $EXCL $SRC \
  -e '\b(rut|dni|nombre|apellido|email|correo|telefono|celular|movil)\b' \
  -e '\b(direccion|domicilio|comuna|fecha_nac|birth_?date|edad|foto|firma)\b' \
  -e '\b(ip_address|latitud|longitud|patente|cuenta_banc|iban|tarjeta)\b' \
  -e '\brun\b\s*[:=]|\brun\s+(VARCHAR|CHAR|TEXT)' \
  .
```

```bash
# datos SENSIBLES en Chile — el comando que más rinde de toda la auditoría
grep -rniE $EXCL $SRC \
  -e '\b(salud|diagnostic[oa]s?|medicament|alergi|discapacid|licencia_medica|ficha_clinica)\w*' \
  -e '\b(isapre|fonasa|prevision|afp|renta|sueldo|salario|ingreso|tramo)\w*' \
  -e '\b(deuda|moros|dicom|scoring|subsidio|ficha_social)\w*' \
  -e '\b(credit(o|icio)|(dicom|credit|risk|riesgo)_?score)\w*' \
  -e '\b(biometr|huella|reconocimiento_facial|genetic|religi|sindical|etni)\w*' \
  -e '\b(orientacion_sexual|identidad_gener|afiliacion_politica)\w*' \
  .
```

> `renta`, `tramo`, `isapre`, `deuda` y `score` son datos **sensibles** en Chile, y
> casi siempre están tratados como campos ordinarios. Ver `clasificacion-datos.md`
> del skill hermano.
>
> Nota sobre dos términos acotados a propósito: `diagnostic[oa]s?` exige la vocal
> española porque `diagnostics` en inglés aparece miles de veces en toolchains de
> TypeScript; y `run` solo se busca como declaración de campo, porque `run()` y
> `npm run` inundan cualquier repo. `rut` sí va suelto: casi no genera ruido.

Los campos de texto libre —`observaciones`, `notas`, `comentarios`, `detalle`,
`descripcion`— cuentan como sensibles si el módulo es clínico, de RRHH, de
beneficios o de cobranza. Anótalos aunque el nombre no diga nada.

## 2. Endpoints

```bash
# Express / NestJS / Fastify
grep -rnE $EXCL --include=*.ts --include=*.js \
  -e '(router|app)\.(get|post|put|patch|delete)\(' \
  -e '@(Get|Post|Put|Patch|Delete)\(' \
  .

# Django / DRF / Flask / FastAPI
grep -rnE $EXCL --include=*.py \
  -e 'path\(|re_path\(' \
  -e '@(app|router)\.(get|post|put|patch|delete|route)' \
  .

# Laravel / Rails
grep -rnE 'Route::(get|post|put|patch|delete|resource|apiResource)' routes/ 2>/dev/null
cat config/routes.rb 2>/dev/null
```

Para cada endpoint anota: método, ruta, si recibe o devuelve datos de personas, y si
aparenta estar autenticado. Prioriza los que llevan `:id` —candidatos a IDOR— y los
que devuelven listados.

## 3. Integraciones y salidas hacia terceros

```bash
# SDKs declarados en dependencias — sin 2>/dev/null, que taparía un error de sintaxis
grep -inE '"@?(sentry|datadog|newrelic|mixpanel|amplitude|segment|hotjar|fullstory|logrocket|posthog|google-analytics|gtag|facebook|meta|openai|anthropic|cohere|sendgrid|mailgun|twilio|whatsapp|stripe|mercadopago|transbank|firebase|supabase|algolia|elastic|zendesk|intercom|hubspot)' \
  package.json composer.json requirements.txt pyproject.toml Gemfile
```

```bash
# llamadas salientes en código
grep -rnE $EXCL --include=*.ts --include=*.js --include=*.py --include=*.php \
  -e '(fetch|axios|httpx|HttpClient|curl_exec|RestTemplate)\(' \
  -e 'requests\.(get|post|put|patch|delete)\(' \
  -e 'Http::(get|post|put|patch|delete)\(' \
  . | grep -vE 'localhost|127\.0\.0\.1'

# scripts de terceros incrustados en el frontend
grep -rnE $EXCL --include=*.html --include=*.ejs --include=*.blade.php --include=*.erb \
  -e '<script[^>]+src="https?://' .
```

Cada uno es una salida potencial de datos personales y casi siempre una
**transferencia internacional**. Ver `terceros-y-ia.md` del skill hermano.

## 4. Logging y telemetría

```bash
# puntos de logging
grep -rnE $EXCL --include=*.ts --include=*.js --include=*.py --include=*.php \
  -e 'console\.(log|info|warn|error)\(' \
  -e '(logger|log)\.(info|debug|warn|error|trace)\(' \
  -e '(Log::|Rails\.logger)' \
  . | grep -vE '\.(test|spec)\.'
```

```bash
# ¿hay sanitización configurada?  La AUSENCIA es el hallazgo
grep -rnE $EXCL \
  -e 'beforeSend|before_send|scrubFields|denyUrls' \
  -e 'maskAllInputs|maskTextSelector|redact' \
  .
```

```bash
# opt-in EXPLÍCITO a enviar PII — lo contrario de sanitizar
grep -rniE $EXCL \
  -e 'sendDefaultPii\s*:\s*true|send_default_pii\s*=\s*True' \
  -e 'maskAllInputs\s*:\s*false|maskAllText\s*:\s*false|blockAllMedia\s*:\s*false' \
  -e 'recordInputs\s*:\s*true|captureBody|logRequestBody' \
  .
```

> Los dos últimos comandos se separan a propósito. `sendDefaultPii: true` aparecería
> en una búsqueda conjunta y se leería como "sí hay configuración de privacidad",
> cuando significa exactamente lo opuesto: un opt-in deliberado a mandar IP,
> cookies y cabeceras al proveedor. Cualquier coincidencia del tercer comando es
> hallazgo ALTO.

## 5. Archivos y almacenamiento

```bash
grep -rnE $EXCL --include=*.ts --include=*.js --include=*.py --include=*.php --include=*.rb \
  -e 'multer|formidable|busboy|FileUpload|UploadedFile|move_uploaded_file' \
  -e 'putObject|upload_file|S3Client|BlobClient|GoogleCloudStorage' \
  .

# nombre entregado por el usuario usado como ruta física
grep -rnE $EXCL -e 'originalname|original_filename|\.filename|getClientOriginalName' .
```

## 6. Jobs, exportaciones y reportes

```bash
grep -rniE $EXCL $SRC \
  -e '\b(cron|celery|sidekiq|bull|agenda|scheduler?)\b' \
  -e '(schedule|enqueue|createQueue|new Queue|Queue\()' \
  .
```

```bash
# exportaciones — acotado: buscar "export" suelto devuelve toda la sintaxis ES modules
grep -rniE $EXCL $SRC \
  -e 'export(ar|acion|ación|Csv|Excel|Xlsx|Pdf|Data|All|To[A-Z])' \
  -e '\b(nomina|listado|informes?|reportes?|padron)\b|generate_?report|/export' \
  -e '(Content-Disposition|attachment;\s*filename|csvWriter|createObjectCsv|xlsx\.write|ExcelJS|PDFDocument)' \
  .
```

Las exportaciones son el vector de fuga masiva: un endpoint que devuelve un registro
es un incidente pequeño; uno que devuelve un CSV con toda la base es otra cosa.

## 7. Infraestructura, configuración y secretos

```bash
ls -a | grep -E '^\.env|docker|Dockerfile|\.github|\.gitlab|terraform|k8s|helm'
git ls-files | grep -E '\.env$|\.env\.|credentials|\.pem$|\.key$|serviceAccount'

# regiones cloud → señal de transferencia internacional
grep -rniE $EXCL --include=*.tf --include=*.yml --include=*.yaml --include=*.env* \
  -e '(us|eu|ap|sa)-(east|west|north|south|central)-[0-9]' \
  -e '\b(region|location|zone)\b\s*[:=]' \
  .
```

`git ls-files` mostrando un `.env` real, un `.pem` o un `serviceAccount.json` es un
hallazgo **CRÍTICO inmediato**: informa al usuario antes de seguir auditando.

## 8. Historial de git

Los secretos y datos borrados **siguen en el historial**. Un `git rm` no los elimina.

```bash
git log --all --diff-filter=A --name-only --pretty=format: \
  | sort -u | grep -iE '\.env|\.pem$|\.key$|credential|secret|dump|backup|\.sql$|\.csv$'

git log -p --all -S 'BEGIN RSA PRIVATE KEY' --oneline | head -20
git log -p --all -S 'AKIA' --oneline | head -20
git log --all --format='%H %s' | grep -iE 'secret|password|token|key|credential|dump'
```

Si hay `gitleaks` o `trufflehog` disponibles, úsalos: son mucho más completos. Si no,
**declara el barrido de historial como parcial**.

> Un secreto que estuvo en el historial debe considerarse **comprometido y rotado**,
> aunque hoy no aparezca en el árbol. Reescribir el historial no basta: alguien pudo
> clonarlo.

## 9. Base de datos real (solo dev o staging)

Nunca producción, nunca copiar valores.

```sql
SELECT table_name, column_name, data_type
FROM   information_schema.columns
WHERE  table_schema NOT IN ('pg_catalog','information_schema')
ORDER  BY table_name, ordinal_position;

SELECT relname, n_live_tup FROM pg_stat_user_tables ORDER BY n_live_tup DESC;

-- PII en texto libre: cuenta coincidencias, NO devuelve filas
SELECT count(*) AS con_patron_rut
FROM   observaciones
WHERE  contenido ~ '[0-9]{7,8}-[0-9kK]';
```

Este paso encuentra lo que el código esconde: campos `TEXT` que en producción reciben
RUT, diagnósticos o montos de deuda. Ninguna revisión de código lo detecta.

Si el entorno resultó ser una copia de producción, **eso ya es un hallazgo**: repórtalo
y no lo consultes.

## 10. Superficies que se escapan de lo anterior

Cinco puntos que no aparecen en ninguna de las categorías clásicas y que concentran
fugas reales.

```bash
# A. PII en almacenamiento del navegador, cookies y payload del JWT
#    Un JWT es Base64, no cifrado: lo lee cualquiera que lo intercepte.
grep -rniE $EXCL \
  -e '(localStorage|sessionStorage)\.setItem\(' \
  -e 'document\.cookie\s*=|res\.cookie\(|set_cookie|setCookie\(' \
  -e 'httpOnly\s*:\s*false|secure\s*:\s*false|sameSite\s*:\s*.?none' \
  -e '(jwt|jsonwebtoken)\.sign\(' \
  .
```

```bash
# B. Datos personales viajando en la URL
#    Quedan en el access log del proxy, en el Referer hacia terceros,
#    en el historial del navegador y en la caché del CDN. Cuatro copias.
grep -rniE $EXCL \
  -e '[?&](rut|run|dni|email|correo|telefono|token|password|diagnostic\w*|renta|isapre)=' \
  -e '(url|path|endpoint|href|redirect)\s*[:=].*\$\{?\s*(rut|email|token|usuario)' \
  .
```

```bash
# C. Consultas sin proyección — el origen de la sobre-exposición
#    Trae password_hash, reset_token y 20 columnas de más. También encuentra
#    el SELECT * que alimenta a un LLM.
grep -rniE $EXCL $SRC \
  -e 'select\s+\*\s+from' \
  -e '\.(findAll|findOne|findByPk)\(' \
  . | grep -viE 'attributes\s*:|select\s*:|\.pluck\(|only\('
```

```bash
# D. Fugas por error, CORS abierto y caché pública
grep -rniE $EXCL \
  -e 'stack\s*:\s*(err|error|e)\.|err\.stack|error\.stack' \
  -e 'json\(\s*\{[^}]*(req\.body|request\.body|err\.(message|stack))' \
  -e "origin\s*:\s*.?\*|Access-Control-Allow-Origin.{0,12}\*" \
  -e "Cache-Control.{0,4}[,:].{0,30}public" \
  .
```

```bash
# E. Dependencias con telemetría propia y widgets incrustados
npm ls --all 2>/dev/null | grep -iE 'analytics|tracking|telemetry|sentry|pixel'
pip list 2>/dev/null | grep -iE 'analytics|telemetry|sentry'
```

Widgets de chat, mapas y captchas cargan scripts de terceros que ven la página
completa, formularios incluidos.

## Salida de la fase

`docs/privacidad/auditoria/superficies.md`:

```markdown
# Superficies — <proyecto>
> Barrido: AAAA-MM-DD · Rama: <rama> · Commit: <sha>

## Stack
<lenguaje, framework, ORM, base de datos, multi-tenant sí/no>

## Conteo
| Superficie | N | Con datos personales | Prioridad |
|---|---|---|---|
| Modelos/tablas | | | |
| Endpoints | | | |
| Integraciones | | | |
| Puntos de logging | | | |
| Exportaciones | | | |
| Jobs | | | |
| Manejo de archivos | | | |

## Fuera de alcance
<qué no se revisó y por qué — sé explícito>

## Señales tempranas
<lo que ya salta a la vista y merece atención inmediata>
```

Con eso, cada dominio de la F2 tiene una lista finita que recorrer, y al final puedes
afirmar qué proporción de cada superficie quedó revisada.

## Cuando un comando no devuelve nada

Antes de concluir "no hay hallazgos", descarta que el comando haya fallado:

```bash
grep ... ; echo "exit=$?"     # 0 = hubo coincidencias, 1 = ninguna, 2 = ERROR
```

Un `exit=2` es un error de sintaxis o de permisos, **no** una ausencia de hallazgos.
Y si un comando devuelve el repositorio completo, tampoco lo reportes: el patrón está
roto. En ambos casos, arregla el comando antes de seguir.
