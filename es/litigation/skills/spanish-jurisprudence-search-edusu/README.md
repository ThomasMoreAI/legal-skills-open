# cendoj-search

A thin, well-behaved HTTP client for the public Spanish jurisprudence search
portal operated by the Consejo General del Poder Judicial (CGPJ) at
[`poderjudicial.es/search`](https://www.poderjudicial.es/search/indexAN.jsp).

The portal exposes no public REST API. This tool reproduces, from a script,
the exact request that the portal's own JavaScript frontend sends when a user
clicks **"Buscar"**, and parses the HTML response back into JSON. Nothing more.

## What it is for

- Looking up individual court decisions (sentencias, autos) by topic, ECLI,
  ROJ, tribunal, jurisdicción, autonomous community, date range, or ponente.
- Personal and educational legal research.
- Driving a single search at a time from a terminal or notebook instead of
  clicking through a web form.

## What it is **not**

- **A crawler.** The script has no pagination loop, no concurrency, no IP
  rotation, and no retry-on-WAF. It is a single-shot client.
- **An evasion tool.** The portal has a WAF that throttles rapid requests.
  When it triggers, the script reports `{"error": "server_error_or_waf"}`
  and **stops**. It does not rotate user agents, spoof TLS fingerprints,
  distribute load, or otherwise attempt to bypass rate limits.
- **A bulk exporter.** Output is JSON to stdout intended for ad-hoc display,
  with no persistence layer, cache, or batch mode.

## Defensive behavior baked into the script

The client is deliberately conservative:

| Behavior | Why |
|---|---|
| Bootstraps with a real `GET /search/indexAN.jsp` first | Same handshake the portal expects from a browser; no session forgery |
| Single sequential request per invocation | No concurrency, no batching |
| Default `--delay 0.5s` between bootstrap and search | Avoids hammering the endpoint |
| Stops on WAF response, surfaces error to user | No retry loops, no evasion |
| Standard browser `User-Agent` (Chrome on macOS) | Not impersonating CGPJ infrastructure or another service |
| No persistent cache, no bulk store | Output goes to stdout and disappears |

If you fork this and add aggressive crawling, rotation, or evasion, you are
operating a different tool with a different profile. That is on you.

## Usage

See [`SKILL.md`](./SKILL.md) for full documentation, including filter values
and query strategy for the underlying Autonomy IDOL backend.

Quick example:

```bash
./cendoj_search.py "responsabilidad patrimonial sanitaria" \
  --jurisdiccion CONTENCIOSO --comunidad MADRID \
  --desde 01/01/2023 --hasta 31/12/2024 --per-page 10
```

## Disclaimer

The author is not affiliated with the CGPJ, the Centro de Documentación
Judicial, or the Poder Judicial. This software is provided as-is.

## License

MIT — see [`LICENSE`](./LICENSE). Covers this client code only.
