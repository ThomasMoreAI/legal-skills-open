# Catálogo de controles + crosswalk

Cada **control** es una unidad reutilizable de cumplimiento. Un mismo control satisface
requisitos de **varios marcos a la vez** → se evalúa una vez y se propaga. Esta es la pieza
que hace genérico al motor: para agregar un marco nuevo, se le suman columnas a esta tabla
(o el pack referencia los `id` de control que exige).

> Estado por control: ✅ cumple · ⚠️ parcial · ❌ falta · ❓ no verificable por código.
> `evidencia`: `archivo:línea` o "declarado por el usuario". Anota remediación si no es ✅.

## Crosswalk (control → marcos)

| id | Control | 18.331 (Datos) | 19.574 (LA/FT) | Futuro (ISO 27001 / SOC 2 / RGPD) | Fuente de evidencia |
|----|---------|----------------|----------------|-----------------------------------|---------------------|
| `gov-responsable` | Responsable/oficial designado | DPO si aplica (Dec. 64/020 art. 10) | Oficial de cumplimiento (Dec. 379/018 art. 16) | ISO A.5.3 / SOC2 CC1 | usuario |
| `gov-registro-urcdp` | **Inscripción de bases en la URCDP** | Sí (Art. 29) | — | — | usuario |
| `gov-rat` | Registro de actividades de tratamiento (RAT) | accountability (Dec. 64/020 art. 5) | — | RGPD Art. 30 | usuario + código |
| `gov-registro` | Registro/inventario formal de riesgos | — | Matriz de riesgos (Dec. 379/018 art. 4) | ISO A.5.9 | usuario + código |
| `gov-politicas` | Políticas documentadas | Política de privacidad | Política + manual LA/FT (Dec. 379/018 arts. 5-6) | ISO A.5.1 | docs generados |
| `gov-capacitacion` | Capacitación al personal | buena práctica | Capacitación (Dec. 379/018 art. 18) | ISO A.6.3 | usuario |
| `gov-auditoria` | Auditoría/revisión periódica | revisión del programa | auditoría (financieros: BCU; no fin.: `[verificar]`) | ISO 9.2 / SOC2 CC4 | usuario |
| `gov-disciplinario` | Régimen disciplinario interno | buena práctica | Sí (sanciones internas) | ISO A.6.4 | usuario |
| `data-licitud` | Base de licitud / consentimiento (Art. 9) | Sí | — | RGPD Art.6 | código (formularios) |
| `data-derechos` | Derechos del titular (acceso Art.14; rectif./actual./inclusión/supresión Art.15) | Sí (5 días hábiles) | — | RGPD Art.15-17 | código (endpoints) |
| `data-info` | Deber de información al recabar (Art. 13) | Sí | — | RGPD Art.13 | código + docs |
| `data-minimizacion` | Minimización y retención | Dec. 64/020 art. 9 | conservación 5 años (Ley 19.574 art. 21) | RGPD Art.5 | código |
| `data-dpa` | Contratos con encargados (DPA) | Sí | control de terceros | RGPD Art.28 | docs + usuario |
| `data-transfer` | Transferencia internacional con mecanismo (Art. 23) | Sí | — | RGPD Cap.V | código (.env/proveedores) |
| `data-consent-text` | Texto de consentimiento + revocación | Sí (Art. 9 / 18) | — | RGPD Art.7 | docs + código |
| `data-dpia` | Evaluación de Impacto (alto riesgo) | Sí (Dec. 64/020 art. 6) | — | RGPD Art.35 | docs + usuario |
| `data-privacy-by-design` | Privacidad por diseño y por defecto | Sí (Dec. 64/020 arts. 8-9) | — | ISO A.8.x / RGPD Art.25 | código |
| `data-pseudonym` | Disociación / seudonimización | Sí (Dec. 64/020 art. 8) | — | RGPD Art.32 | código |
| `aml-debida-diligencia` | Debida diligencia / conocimiento del cliente (KYC) | — | Sí (Ley arts. 14-15) | — | usuario + código |
| `aml-beneficiario-final` | Identificación del beneficiario final (≥15%) | — | Sí (Dec. 379/018 art. 11) | — | usuario |
| `aml-pep` | Tratamiento de PEP (DD intensificada) | — | Sí (Ley art. 20) | — | usuario |
| `aml-monitoreo` | Seguimiento continuo de operaciones | — | Sí (Ley art. 15 lit. D) | SOC2 CC7 | código + usuario |
| `aml-ros` | Reporte de operaciones sospechosas (UIAF) + reserva | — | Sí (Ley arts. 12-13, 22) | — | usuario |
| `aml-conservacion` | Conservación de registros (mín. 5 años) | — | Sí (Ley art. 21) | ISO A.8.13 | usuario + infra |
| `sec-tls` | Cifrado en tránsito (TLS/HTTPS) | Sí (Art. 10) | control interno TI | ISO A.8.24 / SOC2 CC6 | código/infra |
| `sec-rest` | Cifrado en reposo (datos sensibles/credenciales) | Sí (Art. 10) | — | ISO A.8.24 / SOC2 CC6 | código/infra |
| `sec-passwords` | Hashing fuerte de contraseñas (bcrypt/argon2) | Sí | — | ISO A.8.5 | código |
| `sec-mfa` | MFA en accesos administrativos | Sí | control de acceso | ISO A.8.5 / SOC2 CC6.1 | código/infra/usuario |
| `sec-logs` | Logs de acceso y auditoría | Sí | control interno | ISO A.8.15 / SOC2 CC7 | código |
| `sec-tenant` | Segregación por tenant/cliente | Sí | — | SOC2 CC6 | código (`organizationId`) |
| `sec-secrets` | Secretos fuera del código | Sí | control interno | ISO A.8.24 | código (.env/secret mgr) |
| `sec-backups` | Backups y borrado/retención | Sí | conservación 5 años | ISO A.8.13 | infra/usuario |
| `inc-brechas` | Gestión de incidentes + notificación de brechas | Sí (≤72h, Dec. 64/020 art. 4) | — | RGPD Art.33 / SOC2 CC7 | docs + usuario |
| `ctrl-interno` | Control interno: segregación de funciones / autorizaciones | — | Sí | ISO A.5.x / SOC2 CC | usuario + código |
| `sec-monitoring` | Monitoreo y alertas (audit log, secretos, errores) | detección de brechas | detección de operaciones inusuales | SOC2 CC7 | infra + usuario |

## Cómo usarlo
1. En Fase 1, junta evidencia para cada `id` que tengan los packs activos.
2. En Fase 2, asigna estado + evidencia + remediación por control.
3. El score de cada marco = % de sus controles requeridos en ✅ (⚠️ cuenta como medio).
4. Guarda el resultado por control en `state.json` (ver `output-model.md`).
