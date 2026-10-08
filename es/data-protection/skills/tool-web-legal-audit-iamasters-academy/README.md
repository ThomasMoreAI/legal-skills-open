<div align="center">

# ⚖️ web-legal-audit

**Auditoría legal black-box de cualquier web — RGPD · LSSI-CE · cookies (AEPD) · accesibilidad WCAG 2.2 / EAA · seguridad HTTP · publicidad engañosa**

Una *skill* para Claude Code que audita una URL desde todos los ángulos de cumplimiento legal y genera dos entregables listos para usar: un **informe `.docx` para abogados** (con sanciones estimadas y precedentes reales de la AEPD) y un **plan de remediación** con textos modelo y snippets de código.

![version](https://img.shields.io/badge/version-1.0.0-1e3a5f) ![license](https://img.shields.io/badge/license-MIT-d4a73a) ![status](https://img.shields.io/badge/status-stable-65a30d)

</div>

---

## ¿Qué hace?

Le pasas una URL y la skill:

1. **Escanea** la web sin acceso interno (black-box): cookies, trackers, formularios, banner de consentimiento, política de privacidad, aviso legal, cabeceras de seguridad, accesibilidad y claims publicitarios.
2. **Clasifica** cada hallazgo por marco legal y severidad, con la **sanción estimada** basada en precedentes públicos de la AEPD.
3. **Entrega**:
   - 📄 Un **informe `.docx`** estructurado para que lo lea un abogado.
   - 🛠️ Un **plan de remediación** con textos modelo (política de privacidad, cookies, aviso legal) y snippets (banner de cookies, capa informativa de formularios, cabeceras de seguridad).

## Cobertura

| Marco | Qué revisa |
|-------|-----------|
| **RGPD** | Bases legales, consentimiento, minimización, derechos |
| **LSSI-CE** | Aviso legal, identificación del prestador |
| **Cookies (Guía AEPD)** | Banner, consentimiento real, no premarcado |
| **Accesibilidad** | WCAG 2.2 / EAA |
| **Seguridad HTTP** | Cabeceras (CSP, X-Frame-Options, etc.) |
| **Publicidad** | Claims engañosos, garantías |

## Instalación

Clona dentro de tu carpeta de skills de Claude Code:

```bash
git clone https://github.com/angelapaia/web-legal-audit.git ~/.claude/skills/web-legal-audit
```

El generador de `.docx` usa Node:

```bash
cd ~/.claude/skills/web-legal-audit && npm install   # si scripts/generate-docx.mjs requiere dependencias
```

Luego, en Claude Code: *"audita legalmente esta URL: https://ejemplo.com"*.

## Estructura

```
web-legal-audit/
├── SKILL.md                  # Lógica e instrucciones de la skill
├── assets/templates/         # Textos modelo + snippets (privacidad, cookies, banner, headers)
├── references/               # Checklists por marco + precedentes AEPD + base de trackers
├── scripts/generate-docx.mjs # Genera el informe .docx
└── evals/                    # Casos de evaluación
```

## ⚠️ Aviso legal

Esta skill produce un **análisis orientativo** de cumplimiento. **No es asesoramiento jurídico.** Las sanciones estimadas son aproximaciones sobre precedentes públicos. Revisa siempre con un profesional antes de tomar decisiones legales.

---

<div align="center">

Creado por **Angel Aparicio** · **IA Masters Academy** / AASC Associates
· `aaparicio@iamastersacademy.com` ·
Licencia [MIT](LICENSE)

</div>
