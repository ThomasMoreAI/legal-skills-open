# Política de seguridad

## Reporte de vulnerabilidades

Si encontrás una vulnerabilidad de seguridad en `compliance-uy`, por favor **no abras un issue
público**. Reportala de forma privada a: `security@<dominio-del-proyecto>` `[verificar contacto]`.

Incluí: descripción, pasos para reproducir, impacto estimado y, si es posible, una propuesta de
mitigación. Procuraremos acusar recibo en un plazo razonable.

## Alcance

- La skill **lee** código del repositorio auditado; no debe exfiltrar datos.
- Los datos de la empresa quedan en `.compliance/` del repo del usuario (local).
- No incluir secretos reales en `examples/`.

## Datos sensibles

`compliance-uy` puede procesar indicios de datos personales y sensibles. Tratá la salida
(`.compliance/`) como información confidencial y excluila del control de versiones si contiene
datos reales (ver `.gitignore`).
