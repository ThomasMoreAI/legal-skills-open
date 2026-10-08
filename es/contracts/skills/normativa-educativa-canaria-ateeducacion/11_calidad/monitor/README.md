# Monitor de vigilancia de normativa canaria

Control de calidad **recurrente** que detecta normativa nueva publicada en el
portal oficial del Gobierno de Canarias y abre un Pull Request para que se
catalogue de forma supervisada. No crea fichas ni afirma vigencia: solo avisa.

## Qué hace

1. Lee las URLs a vigilar de `06_indices/fuentes.yaml` (por defecto FTE-001 y la
   normativa clasificada FTE-013/014/015).
2. Descarga esas páginas, extrae enlaces a normas/PDF/boletines y los normaliza.
3. Compara contra lo ya catalogado (`fuentes.yaml`, `normativa.yaml`,
   `textos-oficiales.yaml`) y contra el snapshot `portal-normativa-canaria.seen.json`.
4. Reporta solo las **novedades**: descarga sus PDFs a `input/`, escribe
   `nuevas.json` y `nuevas.md`, y actualiza el snapshot.
5. El workflow [`.github/workflows/monitor-normativa.yml`](../../.github/workflows/monitor-normativa.yml)
   convierte los PDFs a Markdown con **DocDigester2MD** (org `ateeducacion`),
   los sella con la cabecera de aviso **R16** en `07_corpus_ia/_borradores-monitor/`
   y abre un PR etiquetado `monitor-normativa`.

Frecuencia: **semanal** (lunes 06:00 UTC) + ejecución manual (`workflow_dispatch`).

## Ejecutar en local

```bash
pip install -r 11_calidad/monitor/requirements.txt
python3 11_calidad/monitor/scan_normativa.py --dry-run   # lista sin tocar nada
python3 11_calidad/monitor/scan_normativa.py             # actualiza snapshot + descargas
```

Conversión de un PDF de prueba (opcional, requiere Docker y credenciales LLM):

```bash
export AI_API_KEY=...        # token GitHub Models o clave OpenRouter free
export AI_BASE_URL=https://models.github.ai/inference
export AI_MODEL=openai/gpt-4o-mini
docker run --rm -e AI_API_KEY -e AI_BASE_URL -e AI_MODEL \
  -v "$PWD/input:/app/input" -v "$PWD/output:/app/output" \
  ghcr.io/ateeducacion/docdigester2md:latest
```

## Configuración del LLM

- **Por defecto: GitHub Models** — gratuito, usa el `GITHUB_TOKEN` del workflow
  (permiso `models: read`). No requiere configurar nada.
- **Alternativa: OpenRouter free** — define en el repositorio el secret
  `AI_API_KEY` y los *variables* `AI_BASE_URL` (`https://openrouter.ai/api/v1`)
  y `AI_MODEL`.
- Si la inferencia falla o no hay cuota, el paso de conversión se omite
  (`continue-on-error`) y el PR se abre igualmente solo con las URLs.

## Añadir o quitar páginas vigiladas

Edita la lista `--watch-ids` del paso «Escanear portal de normativa» en el
workflow, o el valor `DEFAULT_WATCH_IDS` en `scan_normativa.py`. Cada ID debe
existir en `06_indices/fuentes.yaml` con su `url_oficial`.

## Snapshot

`portal-normativa-canaria.seen.json` mapea cada URL detectada a su fecha de
primera detección. Está versionado para que el diff sea estable y auditable.
Para forzar que una URL vuelva a reportarse, borra su entrada del snapshot.

## Deuda de catalogación

El snapshot silencia una URL en cuanto se ve una vez. Es lo que se quiere para no
repetir avisos, pero tiene un efecto secundario: **una disposición detectada y
nunca catalogada desaparece del radar para siempre**. En agosto de 2026 se
descubrió así que 15 disposiciones del BOC y 7 del BOE llevaban meses vistas y
sin ficha, entre ellas el Real Decreto 659/2023, que cuatro fichas del corpus
citaban sin poder enlazar.

Para que esa deuda sea visible:

```bash
python3 11_calidad/monitor/scan_normativa.py --pendientes
```

Lista las URL del snapshot que siguen sin rastro en el corpus, clasificadas en
disposiciones del BOC, disposiciones del BOE, PDF de la Consejería y páginas de
portal. Estas últimas son navegación, no normas, y no requieren ficha. Devuelve
código 1 si queda alguna disposición sin catalogar.

Conviene ejecutarlo de vez en cuando, no sólo al recibir un aviso de novedad.

### Comparación por identificador

Tanto este modo como el escaneo normal comparan por **identificador oficial**
(`BOC-A-AAAA-NNN-NNNN`, `BOE-A-AAAA-NNNNN`) además de por URL. La misma
disposición se publica como PDF de la sede, como HTML del boletín y como texto
consolidado, y el corpus guarda sólo una de esas formas; comparar URL contra URL
hacía que una norma ya catalogada se contara como pendiente.

### Exclusiones razonadas

`descartados.yaml` recoge las URL detectadas que **no procede catalogar**, cada una con su motivo
escrito y la decisión editorial que lo respalda (`DEC-0012`). El informe las muestra en su propia
sección, separadas de la deuda real.

Existe para que el informe siga siendo útil. Un listado que repite en cada ejecución los mismos
cinco documentos ya descartados acaba siendo ruido que nadie lee, y entonces deja de servir para
lo único que importa: ver lo que sí falta.

Añadir una URL aquí es una decisión editorial, no un atajo. Exige motivo escrito.
