# Plan de respuesta a incidentes / vulneraciones de seguridad

> **Disclaimer:** Este software no constituye asesoramiento legal ni garantiza cumplimiento. Genera borradores y diagnósticos técnicos fundados en fuentes oficiales para facilitar una primera implementación.

Base: Ley 19.670 art. 38 (sources/ley-19670-arts-37-40.md); Decreto 64/020 arts. 3-4
(sources/decreto-64-020.md); Guía URCDP de vulneraciones (sources/urcdp-guias.md).

## Definición
Vulneración de seguridad que incide en datos personales (Decreto 64/020 art. 3).

## Plazos (Decreto 64/020 art. 4)
- **24 horas:** iniciar procedimientos para minimizar el impacto.
- **72 horas:** comunicar la vulneración a la URCDP desde que se conoce.
- **A los titulares:** comunicar a quienes tengan afectación significativa, en lenguaje claro.
- **Informe final:** una vez solucionada, informe pormenorizado a la URCDP.

## Roles
- Responsable de datos / DPO: {{responsable_datos}}
- Equipo técnico: {{equipo_tecnico}}
- Contacto URCDP: https://www.gub.uy/unidad-reguladora-control-datos-personales
- Coordinación con CERTuy según corresponda `[verificar contra fuente oficial]`.

## Pasos
1. Detección y contención (≤24h).
2. Evaluación de alcance y datos afectados.
3. Notificación a la URCDP (≤72h) con los datos disponibles.
4. Comunicación a titulares afectados significativamente.
5. Remediación.
6. Informe pormenorizado final a la URCDP.
7. Registro en `registro-incidentes.md`.

## Monitoreo detectado
{{herramientas_monitoreo}}  <!-- p.ej. Sentry, Datadog -->
