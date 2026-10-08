# compliance-uy

Skill open source para **Claude Code** que audita un repositorio de software y genera un
**paquete inicial de cumplimiento de protección de datos personales para Uruguay**, basado en
la **Ley N° 18.331**, el **Decreto 414/009**, los **arts. 37-40 de la Ley 19.670**, el
**Decreto 64/020** y las guías de la **URCDP**.

> **Este software no constituye asesoramiento legal ni garantiza cumplimiento. Genera
> borradores y diagnósticos técnicos fundados en fuentes oficiales para facilitar una primera
> implementación.**

Inspirado en la idea de [`compliance-cl`](#) pero **reescrito desde cero para Uruguay**: no
contiene texto legal chileno ni de otras jurisdicciones. Toda afirmación normativa cita
**norma + artículo + archivo en `/sources`**. Lo no verificable se marca
`[verificar contra fuente oficial]`.

## Qué hace

1. Pregunta los datos de la empresa (razón social, RUT, domicilio, contacto, representante, responsable de datos).
2. Lee el código con Grep/Glob.
3. Detecta **datos personales** (email, teléfono, cédula, RUT, dirección, IP, ubicación, mensajes, archivos, pagos, salud, menores, biométricos).
4. Detecta **proveedores** (AWS, GCP, Azure, Supabase, Firebase, Vercel, Render, Railway, Stripe, MercadoPago, OpenAI, Anthropic, Twilio, SendGrid, Mailchimp, HubSpot, Analytics, Sentry, New Relic, Datadog, Cloudflare).
5. Mapea **transferencias internacionales**.
6. Evalúa **14 controles** (responsable/encargado, consentimiento/base legítima, finalidad, minimización, seguridad, derechos, retención, contratos, transferencias, incidentes, datos sensibles, DPO, registro).
7. Genera documentos en `.compliance/docs/`.
8. Genera `.compliance/state.json` con controles, estado, evidencia `archivo:línea`, riesgo y remediación.

## Estructura

```
compliance-uy/
├── SKILL.md                      # motor de la skill
├── packs/ley-18331/pack.md       # pack normativo principal
├── references/controls.md        # catálogo de controles (C-01..C-14)
├── sources/                      # fuentes oficiales (citación + índice)
├── templates/                    # plantillas de documentos + state.schema.json
├── examples/                     # ejemplo de salida
├── README.md · LICENSE · CONTRIBUTING.md · NOTICE.md · SECURITY.md · ROADMAP.md
└── .github/                      # plantillas e issues iniciales
```

Salida generada (no versionada):
```
.compliance/
├── empresa.json
├── state.json
└── docs/  (10 documentos)
```

## Uso con Claude Code

1. Instala la skill (copia el repo en tu carpeta de skills de Claude Code o empaquétala como `.skill`).
2. En el repo a auditar: pídele a Claude *"audita el cumplimiento de protección de datos (Uruguay)"*.
3. Responde las preguntas sobre la empresa.
4. Revisa `.compliance/` y **valida con un profesional habilitado**.

## Fuentes oficiales

Ver [`sources/README.md`](sources/README.md). Se citan IMPO, Parlamento, gub.uy/URCDP y la OEA.
El texto íntegro de cada norma debe descargarse del enlace oficial indicado a `/sources`.

## Limitaciones

- Las detecciones en código son **heurísticas**: orientan, no prueban cumplimiento.
- Toda conclusión nace como `requiere_revision` hasta validación humana.
- La numeración de algunos artículos de la Ley 18.331 difiere entre ediciones: ver notas
  `[verificar numeración]` y confirmar contra el texto consolidado de IMPO.

## Licencia

[MIT](LICENSE). Ver también [`NOTICE.md`](NOTICE.md).
