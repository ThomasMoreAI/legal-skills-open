#!/usr/bin/env node
/**
 * Inventario de lo que el sitio recaba y con quién lo comparte, leído del
 * repositorio: formularios y sus campos, newsletter, medición, píxeles,
 * contenido incrustado de terceros, idiomas, textos legales y la
 * configuración de consentimiento. Es la base de la entrevista de la skill
 * `textos-legales`. No modifica nada.
 *
 * Uso:
 *   node skills/textos-legales/scripts/inventario-datos.mjs [--json]
 *
 * Lee .env y el entorno del proceso. Las variables configuradas solo en
 * Vercel no se ven desde aquí: confírmalas con la persona.
 */
import fs from "node:fs"
import path from "node:path"
import YAML from "yaml"

import { consent } from "../../../src/config/consent.ts"
import { ENABLED_LOCALES } from "../../../src/config/locales.ts"
import { readEnv } from "../../../scripts/lib/env.mjs"
import { walk } from "../../../scripts/lib/output.mjs"

const env = readEnv()
const value = (key) => String(env[key] ?? "").trim()

const TRACKERS = [
  {
    key: "PUBLIC_GTM_ID",
    name: "Google Tag Manager",
    category: "medición y publicidad",
    provider: "Google LLC (EE. UU.)",
  },
  {
    key: "PUBLIC_GA4_ID",
    name: "Google Analytics 4",
    category: "medición",
    provider: "Google LLC (EE. UU.)",
  },
  {
    key: "PUBLIC_GOOGLE_ADS_ID",
    name: "Google Ads",
    category: "publicidad",
    provider: "Google LLC (EE. UU.)",
  },
  {
    key: "PUBLIC_META_PIXEL_ID",
    name: "Píxel de Meta",
    category: "publicidad",
    provider: "Meta Platforms, Inc. (EE. UU.)",
  },
  {
    key: "PUBLIC_TIKTOK_PIXEL_ID",
    name: "Píxel de TikTok",
    category: "publicidad",
    provider: "TikTok (según región)",
  },
]

const EMBEDS = [
  { name: "YouTube", regex: /youtube(-nocookie)?\.com|youtu\.be/i },
  { name: "Vimeo", regex: /vimeo\.com/i },
  { name: "Google Maps", regex: /google\.[a-z.]+\/maps|maps\.google/i },
  { name: "Calendly", regex: /calendly\.com/i },
  { name: "reCAPTCHA", regex: /recaptcha/i },
  { name: "Hotjar", regex: /hotjar/i },
  { name: "Microsoft Clarity", regex: /clarity\.ms/i },
  { name: "WhatsApp", regex: /wa\.me|api\.whatsapp\.com/i },
]

/** Campos visibles de un formulario (sin ocultos ni honeypot). */
function formFields(component) {
  if (!fs.existsSync(component)) return []
  const text = fs.readFileSync(component, "utf8")
  return [...text.matchAll(/<(input|textarea|select)\b([^>]*)>/g)]
    .map(([, , attrs]) => ({
      name: attrs.match(/name="([^"]+)"/)?.[1],
      hidden: /type="hidden"|aria-hidden="true"/.test(attrs),
      required: /\brequired\b/.test(attrs),
    }))
    .filter((field) => field.name && !field.hidden && field.name !== "botcheck")
    .map((field) => `${field.name}${field.required ? "" : " (opcional)"}`)
}

/** Páginas que usan un tipo de sección. */
function pagesWith(type) {
  return walk("src/content/pages")
    .filter((file) => /\.ya?ml$/.test(file))
    .filter((file) =>
      (YAML.parse(fs.readFileSync(file, "utf8"))?.sections ?? []).some(
        (section) => section.type === type,
      ),
    )
}

const formsProvider = value("PUBLIC_FORMS_PROVIDER") || "none"
const newsletter = value("PUBLIC_NEWSLETTER_ENABLED") === "true"

const embeds = new Set()
for (const file of [...walk("src/content"), ...walk("src/components")]) {
  if (!/\.(ya?ml|md|mdx|astro)$/.test(file)) continue
  const text = fs.readFileSync(file, "utf8")
  for (const embed of EMBEDS) if (embed.regex.test(text)) embeds.add(embed.name)
}

const legal = walk("src/content/legal")
  .filter((file) => file.endsWith(".md"))
  .map((file) => {
    const text = fs.readFileSync(file, "utf8")
    return {
      file,
      title: text.match(/^title:\s*(.+)$/m)?.[1] ?? path.basename(file),
      plantilla: /Plantilla de referencia/.test(text),
    }
  })

const report = {
  idiomas: [...ENABLED_LOCALES],
  hosting: fs.existsSync("vercel.json")
    ? "Vercel Inc. (EE. UU.)"
    : "desconocido",
  formularioContacto: {
    proveedor: formsProvider,
    activo: formsProvider !== "none",
    campos: formFields("src/components/sections/SectionContact.astro"),
    paginas: pagesWith("contact"),
    destino:
      formsProvider === "sendgrid"
        ? "Twilio SendGrid (EE. UU.)"
        : formsProvider === "web3forms"
          ? "Web3Forms"
          : "ninguno (solo enlace mailto)",
  },
  newsletter: {
    activo: newsletter,
    campos: formFields("src/components/sections/SectionNewsletter.astro"),
    paginas: pagesWith("newsletter"),
    proveedor: newsletter ? "MailerLite (UAB MailerLite, Lituania)" : "—",
  },
  rastreo: TRACKERS.filter(({ key }) => value(key)).map(
    ({ key, name, category, provider }) => ({
      name,
      category,
      provider,
      variable: key,
    }),
  ),
  terceros: [...embeds],
  consentimiento: consent,
  textosLegales: legal,
}

if (process.argv.includes("--json")) {
  console.log(JSON.stringify(report, null, 2))
  process.exit(0)
}

const yes = (flag) => (flag ? "sí" : "no")
console.log(`Idiomas: ${report.idiomas.join(", ")}`)
console.log(`Alojamiento: ${report.hosting}`)
console.log(
  `\nFormulario de contacto: ${yes(report.formularioContacto.activo)} (${formsProvider} → ${report.formularioContacto.destino})`,
)
console.log(`  campos: ${report.formularioContacto.campos.join(", ") || "—"}`)
console.log(`  páginas: ${report.formularioContacto.paginas.join(", ") || "—"}`)
console.log(`\nNewsletter: ${yes(newsletter)} (${report.newsletter.proveedor})`)
console.log(`  campos: ${report.newsletter.campos.join(", ") || "—"}`)
console.log("\nMedición y publicidad configuradas en .env o el entorno:")
for (const tracker of report.rastreo) {
  console.log(`  - ${tracker.name} (${tracker.category}; ${tracker.provider})`)
}
if (report.rastreo.length === 0)
  console.log("  ninguna (confirma las variables de Vercel)")
console.log(
  `\nContenido de terceros detectado: ${report.terceros.join(", ") || "ninguno"}`,
)
console.log(
  `\nConsentimiento: modo ${consent.mode}, renovación ${
    consent.renewal === "session"
      ? "por sesión"
      : `${consent.renewal.days} días`
  }, rechazo ${consent.rejectionDays} días, versión ${consent.version}`,
)
console.log("\nTextos legales:")
for (const doc of legal) {
  const state = doc.plantilla ? "plantilla sin adaptar" : "adaptado"
  console.log(`  - ${doc.file}: ${doc.title} (${state})`)
}
