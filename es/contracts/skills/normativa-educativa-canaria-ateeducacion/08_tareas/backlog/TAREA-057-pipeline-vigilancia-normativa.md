---
id: TAREA-057
titulo: "Pipeline de vigilancia semanal de normativa canaria con conversión DocDigester2MD"
estado: "Hecha"
prioridad: "Media"
tipo: "automatizacion"
responsable: "@.agents/skills/control-calidad-documental"
fecha_creacion: 2026-05-22
fecha_actualizacion: 2026-05-22
relacionadas: [FTE-001, FTE-013, FTE-014, FTE-015]
---

# TAREA-057 — Pipeline de vigilancia semanal de normativa canaria

## Objetivo

Detectar automáticamente la normativa nueva publicada en el portal oficial del
Gobierno de Canarias (FTE-001 y normativa clasificada FTE-013/014/015) y abrir un
Pull Request con las novedades para su catalogación supervisada, sin sustituir
nunca la fuente oficial ni afirmar vigencia de forma automática (R1–R5).

## Trabajo realizado

- Creado el scanner `11_calidad/monitor/scan_normativa.py`: lee las URLs a
  vigilar de `06_indices/fuentes.yaml`, extrae enlaces a normas/PDF/boletines,
  los compara contra los índices del corpus y contra el snapshot
  `portal-normativa-canaria.seen.json`, y reporta solo las novedades.
- Añadidos `requirements.txt`, `README.md` y el snapshot inicial (sembrado con
  el baseline de 63 URLs ya presentes el 2026-05-22, modo `--seed`).
- Creado el workflow `.github/workflows/monitor-normativa.yml` (cron semanal
  lunes 06:00 UTC + `workflow_dispatch`): escanea, convierte los PDFs con
  DocDigester2MD (`ghcr.io/ateeducacion/docdigester2md`, GitHub Models por
  defecto), sella los borradores con la cabecera R16 en
  `07_corpus_ia/_borradores-monitor/` y abre un PR etiquetado `monitor-normativa`.

## Criterios de cierre

- `scan_normativa.py` pasa `py_compile` y `--dry-run` lista candidatas sin tocar
  el snapshot; las URLs ya catalogadas no se reportan como nuevas.
- El workflow no toca `main` hasta el merge (trabaja por PR) ni dispara
  `pages.yml` (escribe solo bajo `11_calidad/` y `07_corpus_ia/_borradores-monitor/`).
- Los borradores convertidos llevan aviso expreso de que no sustituyen la fuente
  oficial (R16) y son material no validado.

## Notas

- El alta de fichas `FTE`/`NOR` sigue siendo manual/supervisada; el pipeline solo
  avisa. Las dudas se registran como `PREG-NNN` al catalogar.
- Para reportar de nuevo una URL, basta con borrar su entrada del snapshot.
- LLM por defecto: GitHub Models (gratuito, `GITHUB_TOKEN`). Alternativa:
  OpenRouter free vía secret `AI_API_KEY` + vars `AI_BASE_URL`/`AI_MODEL`.
