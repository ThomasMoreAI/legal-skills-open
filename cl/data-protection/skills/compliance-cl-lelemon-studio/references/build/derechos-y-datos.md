# Receta: derechos del titular y manejo de datos

## 1. Export (acceso / portabilidad) — control `data-derechos`
Endpoint autenticado que junta TODOS los datos del titular de todas las tablas y los entrega en formato
estructurado (JSON; CSV con `@json2csv/node` si conviene).

**Pasos:** validar identidad/ownership → recolectar de cada tabla relacionada (en paralelo) → serializar
→ entregar como descarga → **registrar la solicitud** (audit log, sin loguear el contenido).
**Gotchas:** nunca incluir hashes de contraseña ni secretos; con datasets grandes, **streamear** (no cargar
todo en memoria); cuidado con relaciones lejanas (N+1).

## 2. Borrado / derecho al olvido — control `data-derechos`
Tres estrategias, se combinan según el dato:
- **Soft-delete** (`deletedAt`): reversible; toda query filtra `IS NULL` (índice parcial). Para "no verme más".
- **Anonimización** (hard delete de la PII): reemplazar nombre/RUT/correo por hash o `NULL` manteniendo la
  fila para auditoría/contabilidad. **A nivel de app** (un `UPDATE`), no con la extensión
  `postgresql-anonymizer`: en Postgres manejado solo se instalan las extensiones que el proveedor incluye
  en su lista, así que la extensión es una apuesta a algo que no controlas. Y hacerlo en la app tiene una
  ventaja propia, que vale igual aunque la extensión estuviera disponible: el `UPDATE` va en **la misma
  transacción** que las demás tablas del titular, y el registro de auditoría se escribe al lado.
  *(Antes decía "puede no estar en Railway `[verificar]`" — Railway ya no se usa. En **RDS** la API de
  `describe-db-engine-versions` no expone `SupportedExtensions` para PostgreSQL 17.9, así que la
  comprobación autoritativa es `SELECT * FROM pg_available_extensions` en la instancia:
  `[verificar contra la instancia]`. La recomendación no depende de eso.)*
- **Conservación legal:** lo que la ley obliga a guardar (datos tributarios) NO se borra; se aísla/retiene
  el plazo legal y se anonimiza lo que no sea necesario. La obligación la pone otra ley, no la 21.719:
  **Código Tributario art. 17 inc. 2° + art. 200**, y **Código del Trabajo art. 62** para el libro de
  remuneraciones (desde 5 trabajadores). Esos textos **no se versionan acá** (repo público, licencia de
  redistribución de la BCN sin confirmar): `sources/FUENTES.md` trae el idNorma, el SHA-256 esperado y el
  `curl` para bajarlos, más los límites de cada cita.

### 2 bis. Lecciones de implementarlo (plataforma-contable, ago-2026)

Cuatro cosas que la receta de arriba no decía y costaron tiempo:

- **Antes del export y del borrado va un MAPA declarativo**: qué columna de qué tabla es de quién, y qué
  pasa con ella ante una supresión (`anonymize` con qué reemplazo / `retain` con qué causal / `structural`).
  Sin él, export y borrado son adivinanza y **una columna nueva queda fuera en silencio**. Con un test que
  compara el mapa contra el esquema real, agregar una columna sin clasificarla rompe la suite.
- **La causal de retención es dato, no comentario.** Es lo que se le muestra al titular al denegar, y el
  art. 11 exige que la negativa sea *fundada*. Va en el mapa con su cita, y conviene un test que impida
  mergear una cita marcada `[verificar]`: si llega al PR, es lo mismo que inventarla.
- **Que la columna no cambie no prueba que el cálculo no cambie.** Un test que compara filas antes/después
  no ve que la anonimización mueva un total. Corre el cálculo real (nómina, F29, balance) a los dos lados y
  compara. Al hacerlo apareció que el objeto de la liquidación **arrastraba la fila entera del trabajador**,
  contacto incluido.
- **El bloqueo temporal tiene su propio plazo: 2 días hábiles, no 30.** Y ojo con el alcance: bloquear en
  las operaciones de derechos no impide que el resto del sistema siga tratando al titular. Si el bloqueo
  tiene que ser real, es transversal — dilo explícitamente en vez de dejarlo implícito.

### 2 ter. Sin superficie no hay derecho ejercido

El dominio probado no basta: si el responsable no puede **registrar, exportar, evaluar y responder** desde
la pantalla, el plazo del art. 11 corre igual y nadie lo está atendiendo. Presupuéstala en la misma spec,
no después. De regalo trae la **IP en el audit log**: las funciones de dominio no ven el request, así que la
IP solo se puede capturar en la route o server action (`x-forwarded-for`, primer valor).

**Gotchas:** **no** usar `ON DELETE CASCADE` a ciegas (borra y no deja rastro) → borrado explícito dentro
de una transacción. Backups: no se reescriben; documentar en la política el plazo (ej. "el borrado se
propaga; los backups se rotan en N días"). Hashear PII es reversible si se conoce el salt → para borrado
fuerte, `NULL` es más seguro.

## 3. Captura de consentimiento — control `data-consent-text`
Tabla `consents`: `userId`, `policyVersion`, `policyHash`, `ip`, `userAgent`, `categories` (jsonb),
`givenAt`, `revokedAt`, `method`. La IP del cliente sale de `x-forwarded-for` (primer valor) tras proxy.
**Revocar = crear un nuevo registro** con `revokedAt`/nuevas categorías, **no** sobrescribir el anterior
(la carga de la prueba del consentimiento es del responsable). Servir la versión EXACTA de la política que
se aceptó (versionar el archivo, no editar in-place).

## 4. Retención / purga automática — control `data-minimizacion`
Job programado que borra o anonimiza lo vencido. Opciones de scheduler: **GitHub Action (cron)** o **cron
de Railway** o un worker (`croner` / BullMQ si ya hay cola). Define una tabla de políticas
(`tabla → días → acción`).
**Gotchas:** loguear cada corrida y **alertar si falla** (un cron mudo = datos vencidos acumulándose);
lock si puede correr en paralelo; **timezone explícito**; testear con fecha mockeada (no esperar 90 días).

> Versiones verificadas en npm 2026-06-21 (`@json2csv/node` v7.x). Confirmar con `npm view`.
