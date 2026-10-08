# Receta: monitoreo y detección de filtraciones — controles `sec-monitoring`, `inc-brechas`

La skill **no es** un servicio de monitoreo 24/7. Lo que hace: **recomendar el stack, generar las reglas y
ayudar a desplegarlo** sobre herramientas existentes, para que el founder quede con detección/alertas. Es
detección **periódica**, no DLP ni vigilancia en vivo (eso es otra categoría de producto).

> Favorece lo que ya usan: **BetterStack** (logs/alertas) y **GitHub**. Casi todo gratis; el único de pago
> es el monitoreo de dominio en HIBP.

## 1. Secretos filtrados en el repo
- **GitHub secret scanning + push protection**: bloquea pushes con secretos. **Gratis en repos públicos**;
  en privados es parte de un plan de pago de GitHub → **verificar política/precio vigente** en
  docs.github.com (no fijar números acá). Activar en `Settings > Code security`.
- Alternativa open source: **Gitleaks** (CLI + GitHub Action) en cada PR. Gratis.

## 2. Credenciales/datos filtrados en internet (HIBP)
- **Pwned Passwords** (k-anonymity, por hash): **gratis**.
- **Búsqueda por correo / monitoreo de dominio**: de **pago** → **verificar plan y precio vigente** en
  https://haveibeenpwned.com/Subscription (cambian; no fijar el número acá).
- Librería: `hibp` (v15.x, verificado 2026-06-21). Requiere `userAgent` y, para dominio/correo, API key.
- **NO scrapear la dark web** uno mismo: impráctico y legalmente riesgoso → usar el agregador (HIBP u otro).

## 3. Alertas sobre eventos sensibles (lo de "adentro")
Apoyado en el **audit log**: emitir los eventos sensibles al logger (BetterStack, vía Pino/@logtail) con un
tag (`security`), y crear una **regla de alerta** → Slack/correo. Eventos a vigilar: borrado masivo, MFA
desactivado, export masivo, acceso/uso de la clave SII, registro de brecha.

## 4. Watcher periódico
Un **GitHub Action programado (cron)** que cada cierto tiempo: consulta HIBP (dominio), lee las alertas de
secret scanning (gh API) y revisa el audit log, y **avisa a Slack**. Para una startup, el Action gana al
cron dentro de la app (sin overhead de servidor, logs propios). Si se hace in-app: `croner` (v10.x, verificado).

**Honesto:** es **periódico, no tiempo real**. Para HIBP da igual (las filtraciones aparecen en dumps, no
al instante). Un cron/Action determinista es más barato y confiable que un "LLM en cron" para los chequeos;
el LLM solo aporta en **resumir/razonar** el resultado, no en correr la verificación.

## Límite honesto
Esto es **detección y alerta de primera línea**, no DLP completo ni un SOC. Para exfiltración en vivo,
correlación o respuesta automática hay productos dedicados. Esto cubre ~80% de los casos reales barato.
