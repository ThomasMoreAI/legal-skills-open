# Receta: derechos del titular y manejo de datos

## 1. Export (acceso) — control `data-derechos`
Endpoint autenticado que junta TODOS los datos del titular de todas las tablas y los entrega en formato
estructurado (JSON; CSV con `@json2csv/node` si conviene).

**Pasos:** validar identidad/ownership → recolectar de cada tabla relacionada (en paralelo) → serializar
→ entregar como descarga → **registrar la solicitud** (audit log, sin loguear el contenido).
**Gotchas:** nunca incluir hashes de contraseña ni secretos; con datasets grandes, **streamear** (no cargar
todo en memoria); cuidado con relaciones lejanas (N+1).

## 2. Supresión / borrado — control `data-derechos`
Tres estrategias, se combinan según el dato:
- **Soft-delete** (`deletedAt`): reversible; toda query filtra `IS NULL` (índice parcial). Para "no verme más".
- **Anonimización** (hard delete de la PII): reemplazar nombre/CI/correo por hash o `NULL` manteniendo la
  fila para auditoría/contabilidad. **A nivel de app** (un `UPDATE`), NO depender de la extensión
  `postgresql-anonymizer` (puede no estar disponible en Postgres manejado como Railway — `[verificar]`).
- **Conservación legal:** lo que la ley obliga a guardar (datos tributarios, registros de PLA/FT) NO se
  borra; se aísla/retiene el plazo legal y se anonimiza lo que no sea necesario.

**Gotchas:** **no** usar `ON DELETE CASCADE` a ciegas (borra y no deja rastro) → borrado explícito dentro
de una transacción. Backups: no se reescriben; documentar en la política el plazo (ej. "el borrado se
propaga; los backups se rotan en N días"). Hashear PII es reversible si se conoce el salt → para borrado
fuerte, `NULL` es más seguro.

> **Anonimización con consistencia (lo difícil):** disociar de verdad y a la vez **mantener la
> relacionabilidad** para análisis/auditoría es un problema de arquitectura, no un `UPDATE`. Si necesitás que
> los registros sigan cruzando entre tablas tras anonimizar, usá un **seudónimo determinístico** (HMAC con
> llave separada) en vez de `NULL`, y guardá la llave fuera de la BD. Ojo: un seudónimo determinístico **no es
> anonimización plena** (es seudonimización, reversible con la llave) → para datos sensibles, evaluá si el fin
> analítico justifica conservar el vínculo. Esto excede a la skill: es diseño de gobierno de datos.

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

> Versiones verificadas en npm 2026-06-23 (`@json2csv/node` v7.x). Confirmar con `npm view`.
