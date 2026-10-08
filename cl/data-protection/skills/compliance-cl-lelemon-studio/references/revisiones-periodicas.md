# Revisiones periódicas (automatizar la re-corrida)

El cumplimiento **se degrada solo**: agregas una tabla, un proveedor nuevo, una feature que toca datos, y
la postura cambia sin que nadie lo note. Por eso conviene **re-correr la skill cada cierto tiempo**: cada
corrida reescribe `.compliance/` y muestra el **diff vs la anterior** (qué mejoró, qué se rompió).

Como la skill corre en Claude Code, se puede automatizar de tres formas. **Lo más importante es entender
quién se autentica y quién paga** en cada una (lo verifican mal seguido):

## 1. `/loop` — dentro de una sesión abierta
Repite un prompt mientras la terminal está abierta. Útil para algo puntual, no para dejar corriendo.
```
/loop 1d /compliance-cl
```
- Sin intervalo Claude elige uno; con intervalo (`5m`, `1h`, `1d`) corre fijo.
- **Cuenta:** corre en tu sesión, con la credencial que ya usa tu Claude Code.
- **Gotcha:** muere al cerrar la terminal y expira a los ~7 días. No es para producción.

## 2. Headless por cron / GitHub Action
Claude Code corre sin interacción con el flag de impresión (`claude -p "..."`), así que entra en un cron
del sistema o un **GitHub Action programado** (no depende de tu máquina).
**Pero ojo con la cuenta:** en CI no hay login interactivo → necesitas una credencial no interactiva, y
**esto NO sale de tu suscripción Claude.ai**:
- **`ANTHROPIC_API_KEY`** → se factura por la **API de Anthropic, pago por token** (cuenta de billing
  distinta de Pro/Max). Pagas cada corrida según tokens.
- o un token OAuth generado con `claude setup-token` (`CLAUDE_CODE_OAUTH_TOKEN`).
- Lo soportado oficialmente es la GitHub Action **`anthropics/claude-code-action@v1`** (instala con
  `claude /install-github-app`). También factura por la API.

```yaml
# .github/workflows/compliance.yml — esquema (verificar inputs vigentes en la doc oficial de la action)
name: Revisión de cumplimiento
on:
  schedule:
    - cron: "0 9 1 * *"   # día 1 de cada mes, 9:00 UTC
jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: anthropics/claude-code-action@v1
        with:
          prompt: "audita el cumplimiento de este repo con la skill compliance-cl"
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
      # luego: subir el .compliance/ actualizado como artifact o abrir un PR con el diff
```
- **Costo:** pago por token (API), **no** tu suscripción. Ideal si quieres cron real y costo por uso.
- Acá mismo se engancha el **watcher** de `build/monitoreo.md` (HIBP + secret scanning + audit log).

## 3. `/schedule` — rutina en la nube (usa tu suscripción Claude.ai)
Crea una rutina gestionada que corre en cron (o por evento de GitHub) en infraestructura de Anthropic, sin
tu máquina prendida.
- **Cuenta/costo:** corre contra tu **suscripción Claude.ai (Pro/Max/Team)** vía OAuth, **sin API key**.
- **Cuota diaria** de ejecuciones (aprox. Pro 5 / Max 15 / Team 25 al día — verificar vigente en
  claude.ai/settings/usage). Las corridas one-off no cuentan contra la cuota.
- Está en **research preview** (desde ~abril 2026); los límites pueden cambiar.
- **Gotcha:** corre sobre un **clon fresco del repo** (no ve archivos locales) → la skill y el repo deben
  estar versionados.

## Resumen de costo (lo que más se confunde)
| Forma | Auth | Quién paga |
|---|---|---|
| `/loop` | tu sesión actual | lo que ya use tu Claude Code |
| Headless CI | `ANTHROPIC_API_KEY` / OAuth token | **API de Anthropic, pago por token** (aparte de tu plan) |
| `/schedule` | OAuth Claude.ai | **tu suscripción** Pro/Max/Team (con cuota diaria) |

> **Gotcha global:** si tienes `ANTHROPIC_API_KEY` seteado en el entorno, **manda el API key y te cobra por
> API aunque estés logueado en Pro/Max**. Verifica con `/status` en Claude Code.

## Cadencia sugerida
- **Re-auditoría completa** (`/compliance-cl`): mensual o trimestral, y antes de un release grande.
- **Watcher** (filtraciones/secretos/eventos del audit log): más seguido (diario/semanal) — ver `build/monitoreo.md`.
- **Disparada por evento:** además del cron, correrla cuando cambia el modelo de datos o se suma un proveedor.

> Todo esto es **periódico**, no tiempo real. Para el límite honesto de la detección, ver `build/monitoreo.md`.
> Fuentes (doc oficial): code.claude.com/docs (routines, github-actions), support.claude.com (API key vs Pro/Max).
