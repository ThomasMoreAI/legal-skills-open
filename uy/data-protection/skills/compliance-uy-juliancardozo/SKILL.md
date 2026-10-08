---
name: compliance-uy-juliancardozo
title: compliance-uy — motor de auditoría de protección de datos (Uruguay)
description: Audita un repositorio de software y genera un paquete inicial de cumplimiento de protección de datos personales para Uruguay (Ley N° 18.331, Decreto 414/009, Ley 19.670 arts. 37-40, Decreto 64/020 y guías de la URCDP). Úsala siempre que el usuario pida "auditar protección de datos", "cumplimiento de datos personales", "Ley 18.331", "habeas data", "URCDP", "política de privacidad", "datos personales en Uruguay", "GDPR uruguayo", "DPO", "transferencias internacionales de datos" o quiera detectar qué datos personales y proveedores maneja su código y qué le falta para cumplir la normativa uruguaya, aunque no nombre la ley exacta. Genera borradores y diagnósticos; NO es asesoramiento legal.
author: juliancardozo
author_url: https://github.com/juliancardozo/compliance-uy
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: uy
practice: data-protection
language: es
sources:
- title: Controls
  path: references/controls.md
---

# compliance-uy — motor de auditoría de protección de datos (Uruguay)

> **Disclaimer obligatorio (incluir textualmente en TODO documento generado y en el resumen):**
> "Este software no constituye asesoramiento legal ni garantiza cumplimiento. Genera
> borradores y diagnósticos técnicos fundados en fuentes oficiales para facilitar una primera
> implementación."

Esta skill audita el repositorio actual y produce un paquete inicial de cumplimiento de la
**Ley N° 18.331** y normativa complementaria de Uruguay, en `.compliance/`.

## Principios no negociables

1. **Solo fuentes oficiales uruguayas.** Toda afirmación normativa cita `(Norma, art. — sources/archivo.md)`. **Nunca** se copia texto legal de otras jurisdicciones (incluido `compliance-cl`).
2. **Trazabilidad.** Las fuentes están en `/sources`. El catálogo de controles en `references/controls.md`. El detalle normativo del pack en `packs/ley-18331/pack.md`. Lee esos archivos cuando los necesites; no inventes artículos.
3. **Honestidad epistémica.** Lo que no se pueda verificar contra fuente oficial se marca `[verificar contra fuente oficial]`. Las detecciones en código son **heurísticas**: orientan, no prueban. Toda conclusión nace en estado `requiere_revision`.
4. **No es asesoramiento legal.** Incluir el disclaimer; recomendar validación por profesional habilitado.

## Flujo de trabajo

Ejecuta en orden. Mantén una lista de tareas si tienes esa capacidad.

### Paso 0 — Cargar contexto normativo
- Lee `references/controls.md` (catálogo de controles C-01..C-14).
- Lee `packs/ley-18331/pack.md` (mapa norma→control→evidencia, plazos, definiciones).
- Ten presentes las fuentes de `/sources`. Si falta el texto íntegro de una norma en `/sources`, avísalo y continúa marcando lo afectado como `[verificar contra fuente oficial]`.

### Paso 1 — Datos de la empresa
Pregunta (usa la herramienta de inputs si está disponible, una pregunta clara a la vez; o un solo bloque si el usuario prefiere). Recolecta:
- Razón social
- RUT
- Domicilio
- Contacto (email/teléfono)
- Representante legal
- Responsable de datos / Delegado de Protección de Datos (DPO), si existe

Guarda lo recibido en `.compliance/empresa.json`. Si el usuario no sabe un dato, regístralo como `"[verificar contra fuente oficial]"` y sigue. Nunca inventes RUT, domicilio ni nombres.

### Paso 2 — Leer el código (Grep/Glob)
Usa Glob para mapear el repo y Grep para buscar señales. No abras binarios. Prioriza: modelos/esquemas de datos, migraciones, formularios, configuración, variables de entorno (`.env.example`), dependencias (`package.json`, `requirements.txt`, `go.mod`, etc.), `infra/`, `legal/`, `docs/`.

### Paso 3 — Detectar datos personales
Busca señales (heurísticas) de estas categorías y anota `archivo:línea`:

| Categoría | Señales de ejemplo (regex/keywords) |
|---|---|
| Email | `email`, `correo`, `e_mail`, patrones `@` en validaciones |
| Teléfono | `phone`, `telefono`, `celular`, `mobile`, `whatsapp` |
| Cédula (CI) | `cedula`, `ci`, `documento`, `doc_id`, validadores de CI uruguaya |
| RUT | `rut`, `ruc`, `tax_id`, `registro_unico` |
| Dirección | `direccion`, `address`, `domicilio`, `calle`, `codigo_postal` |
| IP | `ip_address`, `remote_addr`, `x-forwarded-for` |
| Ubicación | `lat`, `lng`, `location`, `geo`, `coordinates`, `gps` |
| Mensajes | `message`, `chat`, `mensaje`, `inbox`, `conversation` |
| Archivos | `upload`, `file`, `attachment`, `document`, `s3`, `storage` |
| Pagos | `card`, `tarjeta`, `payment`, `iban`, `cvv`, `stripe`, `mercadopago` |
| Salud (sensible) | `salud`, `health`, `diagnostico`, `medical`, `historia_clinica` |
| Menores (sensible/especial) | `edad`, `age`, `birthdate`, `menor`, `kid`, `parental` |
| Biométricos (sensible) | `biometric`, `huella`, `fingerprint`, `face`, `iris`, `voiceprint` |
| Origen/ideología/etc. (sensible) | `religion`, `etnia`, `raza`, `sindicato`, `orientacion`, `politica` |

Marca como **sensibles** (art. 18 / art. 4 — `sources/ley-18331.md`) salud, biométricos, origen racial/étnico, opiniones políticas, convicciones religiosas/morales, afiliación sindical y vida sexual. Trata datos de **menores** con especial cuidado.

### Paso 4 — Detectar proveedores
Busca en dependencias, SDKs, variables de entorno y configuración:
AWS, GCP, Azure, Supabase, Firebase, Vercel, Render, Railway, Stripe, MercadoPago, OpenAI,
Anthropic, Twilio, SendGrid, Mailchimp, HubSpot, Google/otros Analytics, Sentry, New Relic,
Datadog, Cloudflare. Para cada uno anota: nombre, para qué se usa (heurístico), `archivo:línea`,
y si probablemente actúa como **encargado del tratamiento**.

### Paso 5 — Mapear transferencias internacionales
Por cada proveedor del Paso 4, estima si los datos salen de Uruguay (la mayoría de estos
servicios alojan fuera del país). Registra: proveedor, país/región estimada, categorías de
datos involucradas, base legal posible (art. 23 — `sources/ley-18331.md`) y si requiere
autorización URCDP o cumple por nivel adecuado/excepción. Marca lo incierto como
`[verificar contra fuente oficial]`.

### Paso 6 — Evaluar controles
Recorre C-01..C-14 de `references/controls.md`. Para cada control determina estado
(`cumple`/`parcial`/`no_cumple`/`no_aplica`/`requiere_revision`), evidencia (`archivo:línea`),
riesgo (`alto`/`medio`/`bajo`) y remediación. Sé conservador: ante duda, `requiere_revision`.

### Paso 7 — Generar documentos
Crea `.compliance/docs/` y genera, a partir de `templates/`, completando con los hallazgos:
- `inventario-datos.md`
- `matriz-tratamientos.md`
- `politica-privacidad.md`
- `contrato-encargado.md`
- `matriz-proveedores-transferencias.md`
- `procedimiento-derechos-titulares.md`
- `plan-respuesta-incidentes.md`
- `registro-incidentes.md`
- `evaluacion-riesgo-privacidad.md`
- `resumen-cumplimiento.md`

Cada documento debe: (a) incluir el disclaimer; (b) citar base legal por afirmación; (c)
marcar lo no verificable con `[verificar contra fuente oficial]`; (d) referenciar evidencia
`archivo:línea` cuando exista.

### Paso 8 — Generar `state.json`
Escribe `.compliance/state.json` siguiendo `templates/state.schema.json`: por cada control,
`id`, `estado`, `evidencia` (lista de `{archivo, linea, nota}`), `riesgo`, `remediacion`,
`base_legal`. Incluye metadatos: `empresa`, `fecha`, `version_skill`, `fuentes` usadas.

### Paso 9 — Cierre
Muestra al usuario el `resumen-cumplimiento.md`: hallazgos por riesgo, controles en
`no_cumple`/`parcial`, y próximos pasos. Reitera el disclaimer y la recomendación de validar
con un profesional habilitado y de inscribir las bases ante la URCDP cuando corresponda.

## Estructura de salida

```
.compliance/
├── empresa.json
├── state.json
└── docs/
    ├── inventario-datos.md
    ├── matriz-tratamientos.md
    ├── politica-privacidad.md
    ├── contrato-encargado.md
    ├── matriz-proveedores-transferencias.md
    ├── procedimiento-derechos-titulares.md
    ├── plan-respuesta-incidentes.md
    ├── registro-incidentes.md
    ├── evaluacion-riesgo-privacidad.md
    └── resumen-cumplimiento.md
```

## Recursos del repo (lee según necesidad)
- `references/controls.md` — catálogo de controles y mapa control→documento.
- `packs/ley-18331/pack.md` — detalle normativo, plazos y definiciones.
- `sources/` — fuentes oficiales y citación canónica.
- `templates/` — plantillas de cada documento y `state.schema.json`.
