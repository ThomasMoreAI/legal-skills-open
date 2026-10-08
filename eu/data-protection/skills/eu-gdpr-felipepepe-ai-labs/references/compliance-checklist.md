# Checklist de Compliance — GDPR

## Schema de Base de Datos

### Columnas obligatorias para datos personales
- [ ] `created_at` — fecha de creación de los datos
- [ ] `updated_at` — fecha de última modificación
- [ ] `deleted_at` — fecha de eliminación (soft delete) para soporte de derecho al olvido
- [ ] `consent_version` — versión de la política de privacidad aceptada
- [ ] `consent_given_at` — fecha de consentimiento (si aplica)

### Nombres de columnas
- [ ] No usar nombres identificables para datos anónimos
- [ ] Campos sensibles cifrados en la base de datos
- [ ] Separar datos de authentication de datos de profile

```sql
-- ✅ CORRECTO — Separación de concerns
CREATE TABLE users (
    id UUID PRIMARY KEY,
    email_hash VARCHAR(64) NOT NULL,  -- hash, no plaintext
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at TIMESTAMPTZ,  -- soft delete for right to erasure
    consent_version INTEGER NOT NULL DEFAULT 1,
    consent_given_at TIMESTAMPTZ,
    data_retention_until TIMESTAMPTZ NOT NULL  -- auto-delete deadline
);

-- ❌ INCORRECTO — Datos sensibles en plaintext
CREATE TABLE users (
    email TEXT,  -- plaintext email — violates minimization
    health_data TEXT,  -- special category data — needs encryption
    ip_address TEXT,  -- stored without purpose limitation
    consent BOOLEAN DEFAULT FALSE  -- pre-checked — invalid consent
);
```

## APIs / Endpoints

### Endpoints obligatorios para Data Subject Rights
- [ ] `GET /api/profile` — Derecho de acceso
- [ ] `PATCH /api/profile` — Derecho de rectificación
- [ ] `DELETE /api/profile` — Derecho al olvido
- [ ] `GET /api/data-export` — Derecho a portabilidad (formato estructurado, machine-readable)
- [ ] `POST /api/consent/revoke` — Derecho a retirar consentimiento

```typescript
// ✅ Incluye rate limiting para proteger contra scraping de datos
app.get('/api/profile', rateLimit({ windowMs: 60_000, max: 30 }), getUserProfile);
app.post('/api/data-export', rateLimit({ windowMs: 300_000, max: 5 }), exportUserData);
```

### Validación de entrada
- [ ] Validar que los datos recibidos sean necesarios para la finalidad declarada
- [ ] Sanitizar inputs para prevenir injection
- [ ] No almacenar más datos de los necesarios (principio de minimización)

## Cookies y Tracking

- [ ] Banner de cookies con opciones Granular (no solo aceptar/rechazar todo)
- [ ] Consentimiento granular por categoría de cookies
- [ ] Registro del consentimiento (qué, cuándo, cómo)
- [ ] Mecanismo de retiro de consentimiento tan fácil como otorgarlo
- [ ] No cargar cookies antes del consentimiento (cookie consent prior to setting)

```html
<!-- ✅ Correcto — Opciones granulares -->
<div class="cookie-consent">
  <label><input type="checkbox" name="cookies_necessary" checked disabled /> Necesarias</label>
  <label><input type="checkbox" name="cookies_analytics" /> Analytics</label>
  <label><input type="checkbox" name="cookies_marketing" /> Marketing</label>
  <button type="submit">Guardar preferencias</button>
</div>

<!-- ❌ Incorrecto — Pre-checkeado -->
<input type="checkbox" name="cookies_all" checked /> Aceptar todas las cookies
```

## Infraestructura y Servidores

- [ ] Datos de usuarios de la UE almacenados en servidores dentro de la UE/EEE
- [ ] Si hay transferencia internacional: SCCs (Standard Contractual Clauses) o decisión de adecuación
- [ ] Cifrado en reposo (AES-256 o similar)
- [ ] Cifrado en tránsito (TLS 1.2+)
- [ ] Logs de acceso con retención limitada (máx. 12 meses)
- [ ] Política de acceso al dato (solo personal autorizado)

## Documentación Obligatoria

- [ ] Registro de actividades de tratamiento (Art. 30)
- [ ] Evaluación de impacto de protección de datos (DPIA, Art. 35) si hay alto riesgo
- [ ] Política de retención de datos con fechas de eliminación automática
- [ ] Política de violaciones de datos con procedimientos de notificación
- [ ] Acuerdo de procesamiento de datos (DPA, Art. 28) con cada proveedor externo

## Retención de Datos

```typescript
// ✅ Incluir lógica de eliminación automática
const RETENTION_POLICIES = {
  'user_profiles': { days: 730, after: 'delete' },  // 2 años
  'login_logs': { days: 365, after: 'anonymize' },  // 1 año, anonimizar
  'email_logs': { days: 180, after: 'delete' },     // 6 meses
  'analytics_data': { days: 27, after: 'anonymize' }, // 27 días (Google Analytics standard)
};
```

## Provisores externos (Art. 28 — Data Processors)

Para CADA proveedor externo que procese datos en nombre del responsable:
- [ ] DPA (Data Processing Agreement) firmado
- [ ] Verificar que el proveedor tiene medidas de seguridad adecuadas
- [ ] Verificar que el proveedor permite auditorías
- [ ] Verificar que el proveedor notifica violaciones de datos
- [ ] Listar los sub-procesadores del proveedor

## Privacidad por diseño (Privacy by Design)

Principios a aplicar en TODO el código:

| Principio | Implementación en código |
|------ | -------- |
| **Proactividad** | Detectar riesgos de privacidad ANTES de desarrollar |
| **Privacidad por defecto** | Configuración más protectora es el default |
| **Privacidad integrada** | La privacidad no es un addon — es parte del core |
| **Full functionality** | No sacrificar funcionalidad por privacidad |
| **Seguridad end-to-end** | Cifrado desde la entrada hasta el almacenamiento |
| **Visibilidad y transparencia** | El usuario puede ver qué datos se procesan |
| **Minimización** | Solo los datos estrictamente necesarios |
