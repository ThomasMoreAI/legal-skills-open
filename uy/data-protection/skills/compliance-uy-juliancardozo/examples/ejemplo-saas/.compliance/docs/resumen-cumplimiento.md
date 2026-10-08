# Resumen de cumplimiento — Pyme Demo SRL

> **Disclaimer:** Este software no constituye asesoramiento legal ni garantiza cumplimiento. Genera borradores y diagnósticos técnicos fundados en fuentes oficiales para facilitar una primera implementación.

- **RUT:** 210000000000 · **Fecha:** 2026-06-23 · **Versión skill:** 0.1.0

## Estado por control (extracto)
| Control | Estado | Riesgo | Base legal |
|---|---|---|---|
| C-02 Consentimiento | no_cumple | alto | Ley 18.331 art. 9 |
| C-06 Seguridad | parcial | alto | Ley 18.331 art. 12 / D.64/020 |
| C-10 Transferencias int. | requiere_revision | alto | Ley 18.331 art. 23 |
| C-13 DPO | no_aplica | bajo | Ley 19.670 art. 40 |

## Hallazgos de mayor riesgo
1. Recolección de email/teléfono sin base legítima documentada (C-02).
2. Secretos en texto plano en ejemplo de configuración (C-06).
3. Transferencias internacionales (AWS us-east-1, Stripe) sin base legal mapeada (C-10).

## Próximos pasos
1. Implementar captura de consentimiento y registrar base legal por tratamiento.
2. Mapear transferencias internacionales y completar `matriz-proveedores-transferencias.md`.
3. Validar con profesional habilitado y evaluar inscripción de bases ante la URCDP (Ley 18.331 art. 6 — sources/ley-18331.md).
