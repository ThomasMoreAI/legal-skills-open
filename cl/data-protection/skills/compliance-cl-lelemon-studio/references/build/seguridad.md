# Receta: seguridad (MFA, cifrado en reposo, audit log)

> Stack base: TypeScript/Node (Next.js o NestJS) + Postgres. Versiones verificadas en npm 2026-06-21;
> confirmar la vigente con `npm view`.

## 1. MFA / 2FA (TOTP) — control `sec-mfa`
**Librerías:** `otplib` (TOTP, v13.x) + `qrcode` (QR) + `rate-limiter-flexible` (anti fuerza bruta).
Hashing de códigos de respaldo: `bcrypt` o `argon2`. (`speakeasy` está sin mantención — no usar.)

**Pasos:**
1. Columnas en `users`: `totp_secret_encrypted`, `totp_enabled`, `recovery_codes_hashed`.
2. Enrolar: `authenticator.generateSecret()` → `keyuri()` → QR; generar ~10 códigos de respaldo.
3. Confirmar antes de activar: el usuario ingresa un código y se valida con `authenticator.verify({ token, secret })`.
4. Guardar el **secreto cifrado** (ver §2) y los **códigos de respaldo hasheados**.
5. En login, segundo paso: verificar TOTP o un código de respaldo (de un solo uso → marcarlo usado).

**Gotchas:** usar `window: 1` (tolera ±30s de desfase de reloj); rate-limit los intentos; nunca loguear
el secreto; los recovery codes son de un solo uso (consumir, no solo marcar).

## 2. Cifrado en reposo a nivel de campo — controles `sec-rest`, `data-pseudonym`
**Librería:** `node:crypto` (nativo). Algoritmo **AES-256-GCM** (cifrado autenticado).

**Pasos:**
1. Llave de 32 bytes desde el entorno (en prod: idealmente un KMS, no `.env`).
2. `encrypt`: IV aleatorio de 12 bytes (`randomBytes`), guardar `iv:authTag:ciphertext`.
3. `decrypt`: setear el authTag y validar (detecta manipulación).
4. **Buscar por un campo cifrado** → "blind index": guardar también un HMAC determinístico del valor e
   indexarlo; se busca por ese hash, no por el texto cifrado.

**Gotchas:** **nunca** reutilizar el IV con la misma llave; siempre verificar el authTag; planear la
**rotación de llave** (descifrar con la vieja, recifrar con la nueva). Alternativa a nivel BD (`pgcrypto`)
deja la llave en la BD → el admin ve el dato; preferir app-level para lo sensible (RUT, salud).

## 3. Audit log + contexto actor/IP — control `sec-logs`
Tabla append-only ya descrita en `output-model.md`/el audit log. Lo que faltaba: **capturar quién + IP
sin cambiar todas las firmas** → patrón **AsyncLocalStorage** (`node:async_hooks`, nativo).

**Pasos:**
1. Crear un `AsyncLocalStorage<{ userId?, ip? }>` en un módulo (`lib/request-context`).
2. En el **borde** (middleware de Next/NestJS, o al resolver la sesión): `als.run({ userId, ip }, () => next())`.
   La IP sale de `x-forwarded-for` (primer valor) detrás de proxy.
3. `recordAudit` lee `als.getStore()` como fallback cuando no recibe actor/IP explícito.

**Gotchas:** el contexto se pierde si algo rompe la cadena async; envolver con `.run()` en el borde, no
"setear y seguir". El timestamp va con `DEFAULT now()` de la BD (no del cliente). Para alta exigencia,
hacer la tabla inmutable (revocar UPDATE/DELETE) y/o encadenar hashes — opcional.

**Fuentes:** node:crypto y node:async_hooks (docs oficiales de Node); otplib (github.com/yeojz/otplib).
