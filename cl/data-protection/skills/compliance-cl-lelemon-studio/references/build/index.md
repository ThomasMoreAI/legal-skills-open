# Recetas de construcción (build/)

Cuando el diagnóstico encuentra un hueco, no basta decir "te falta X": acá está **cómo construirlo**.
Estas recetas son guías de implementación (librerías + pasos + gotchas), no código completo — el código
exacto lo escribe Claude Code adaptado al stack del repo. La skill puede **ofrecer implementarlo** (corre
en Claude Code) o dejárselo al founder para que lo haga.

## Regla de veracidad (NADA inventado)
- Las **versiones de librerías** de estas recetas se verificaron en npm el **2026-06-21**; igual,
  confirmar la vigente con `npm view <pkg> version` antes de instalar.
- Los **precios y políticas de servicios externos** (HIBP, GitHub) **cambian**: NO se fijan números acá;
  cada receta apunta a la **página oficial** para verificar el plan/precio vigente.
- Si una receta menciona algo no verificable, va marcado `[verificar]`.

## Mapa control → receta
| Hueco / control | Receta |
|---|---|
| `sec-mfa` | `seguridad.md` (MFA/TOTP) |
| `sec-rest`, `data-pseudonym` | `seguridad.md` (cifrado en reposo + blind index) |
| `sec-logs` (+ actor/IP) | `seguridad.md` (audit log + AsyncLocalStorage) |
| `data-derechos` | `derechos-y-datos.md` (export + borrado/anonimización) |
| `data-consent-text` | `derechos-y-datos.md` (captura de consentimiento) |
| `data-minimizacion` | `derechos-y-datos.md` (retención/purga) |
| `sec-monitoring`, `inc-brechas` | `monitoreo.md` (secret scanning, HIBP, alertas, watcher) |

## Principio
Lo **mecánico/reversible** (código) → la skill lo construye. Lo que necesita **criterio o un tercero**
(supervisión externa del MPD, representación) no se construye con código (ver `cuando-acudir-a-abogado.md`).
