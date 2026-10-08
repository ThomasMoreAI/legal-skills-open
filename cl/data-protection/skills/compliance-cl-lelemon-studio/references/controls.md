# Catálogo de controles + crosswalk

Cada **control** es una unidad reutilizable de cumplimiento. Un mismo control satisface
requisitos de **varios marcos a la vez** → se evalúa una vez y se propaga. Esta es la pieza
que hace genérico al motor: para agregar un marco nuevo, se le suman columnas a esta tabla
(o el pack referencia los `id` de control que exige).

> Estado por control: ✅ cumple · ⚠️ parcial · ❌ falta · ❓ no verificable por código.
> `evidencia`: `archivo:línea` o "declarado por el usuario". Anota remediación si no es ✅.

## Crosswalk (control → marcos)

| id | Control | 21.719 (Datos) | 21.595 (MPD) | Futuro (ISO 27001 / SOC 2 / GDPR) | Fuente de evidencia |
|----|---------|----------------|--------------|-----------------------------------|---------------------|
| `gov-responsable` | Responsable/oficial designado | DPO si aplica | Oficial de cumplimiento | ISO A.5.3 / SOC2 CC1 | usuario |
| `gov-registro` | Registro/inventario formal | RAT | Matriz de riesgos de delitos | ISO A.5.9 | usuario + código |
| `gov-politicas` | Políticas documentadas | Política de privacidad | Código de ética | ISO A.5.1 | docs generados |
| `gov-capacitacion` | Capacitación al personal | buena práctica | Capacitación (obligatoria) | ISO A.6.3 | usuario |
| `gov-auditoria` | Auditoría/revisión periódica | parte del MPI | Auditoría del modelo | ISO 9.2 / SOC2 CC4 | usuario |
| `gov-disciplinario` | Régimen disciplinario interno | parte del MPI | Sí (sanciones internas) | ISO A.6.4 | usuario |
| `gov-denuncias` | Canal de reporte/denuncias | canal de contacto/derechos | Canal anónimo de denuncias | ISO A.5.x / GDPR Art.38 | código + usuario |
| `data-licitud` | Base de licitud / consentimiento opt-in | Sí | — | GDPR Art.6 | código (formularios) |
| `data-derechos` | Derechos del titular (ARCO+portabilidad+bloqueo) | Sí (30 días) | — | GDPR Art.15-22 | código (endpoints) |
| `data-info` | Deber de información / aviso de privacidad | Sí | — | GDPR Art.13 | código + docs |
| `data-minimizacion` | Minimización y retención | Sí | — | GDPR Art.5 | código |
| `data-dpa` | Contratos con encargados (DPA) | Sí | control de terceros | GDPR Art.28 | docs + usuario |
| `data-transfer` | Transferencias internacionales con mecanismo | Sí | — | GDPR Cap.V | código (.env/proveedores) |
| `data-consent-text` | Texto de consentimiento opt-in + revocación | Sí (Art. 12/16) | — | GDPR Art.7 | docs + código |
| `data-rights-channel` | Canal/formulario para ejercer derechos | Sí (Art. 14 ter) | — | GDPR Art.12 | docs + código |
| `data-eipd` | Evaluación de Impacto (alto riesgo) | Sí (Art. 15 ter) | — | GDPR Art.35 | docs + usuario |
| `data-privacy-by-design` | Privacidad desde el diseño y por defecto | Sí (Art. 14 quáter) | — | ISO A.8.x / GDPR Art.25 | código |
| `data-pseudonym` | Seudonimización de datos | Sí (Art. 14 quinquies) | — | GDPR Art.32 | código |
| `sec-tls` | Cifrado en tránsito (TLS/HTTPS) | Sí | control interno TI | ISO A.8.24 / SOC2 CC6 | código/infra |
| `sec-rest` | Cifrado en reposo (datos sensibles/credenciales) | Sí | — | ISO A.8.24 / SOC2 CC6 | código/infra |
| `sec-passwords` | Hashing fuerte de contraseñas (bcrypt/argon2) | Sí | — | ISO A.8.5 | código |
| `sec-mfa` | MFA en accesos administrativos | Sí | control de acceso | ISO A.8.5 / SOC2 CC6.1 | código/infra/usuario |
| `sec-logs` | Logs de acceso y auditoría | Sí | control interno | ISO A.8.15 / SOC2 CC7 | código |
| `sec-tenant` | Segregación por tenant/cliente | Sí | — | SOC2 CC6 | código (`organizationId`) |
| `sec-secrets` | Secretos fuera del código | Sí | control interno | ISO A.8.24 | código (.env/secret mgr) |
| `sec-backups` | Backups y borrado/retención | Sí | — | ISO A.8.13 | infra/usuario |
| `inc-brechas` | Gestión de incidentes + notificación de brechas | Sí (sin dilaciones indebidas, Art. 14 sexies) | — | GDPR Art.33 / SOC2 CC7 | docs + usuario |
| `ctrl-interno` | Control interno: segregación de funciones / autorizaciones | — | Sí | ISO A.5.x / SOC2 CC | usuario + código |
| `sec-monitoring` | Monitoreo y alertas (audit log, secretos, errores) | detección de brechas | detección delitos informáticos | SOC2 CC7 | infra + usuario |

## Cómo usarlo
1. En Fase 1, junta evidencia para cada `id` que tengan los packs activos.
2. En Fase 2, asigna estado + evidencia + remediación por control.
3. El score de cada marco = % de sus controles requeridos en ✅ (⚠️ cuenta como medio).
4. Guarda el resultado por control en `state.json` (ver `output-model.md`).
