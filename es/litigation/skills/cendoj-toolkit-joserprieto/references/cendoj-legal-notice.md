# CENDOJ Legal Notice (Verbatim)

Source: <https://www.poderjudicial.es/search/indexAN.jsp> (modal "Aviso legal") Retrieved:
2026-05-22

---

## Texto literal del aviso legal

Las resoluciones que componen esta base de datos se difunden a efectos de conocimiento y consulta de
los criterios de decisión de los Tribunales, en cumplimiento de la competencia otorgada al Consejo
General del Poder Judicial por el art. 560.1.10º de la Ley Orgánica del Poder Judicial.

El usuario de la base de datos podrá consultar los documentos siempre que lo haga **para su uso
particular**.

**No está permitida la utilización de la base de datos para usos comerciales, ni la descarga masiva
de información.** La reutilización de esta información para la elaboración de bases de datos o con
fines comerciales debe seguir el procedimiento y las condiciones establecidas por el CGPJ a través
de su Centro de Documentación Judicial.

Cualquier actuación que contravenga las indicaciones anteriores podrá dar lugar a la adopción de las
medidas legales que procedan.

---

## Robots.txt

Source: <https://www.poderjudicial.es/robots.txt> Retrieved: 2026-05-22

```
User-agent: *
Crawl-delay: 5
Disallow: /portal/site/prontuario
Disallow: /search_old/
[... non-search paths omitted ...]
```

Relevant to this toolkit: `/search/` is **not in the Disallow list** → indexing and downloading from
`/search/` is permitted by `robots.txt`, subject to:

1. `Crawl-delay: 5` (5 seconds minimum between requests)
2. The legal notice constraints above (uso particular only)

---

## Interpretation by this skill

| Aspect             | Interpretation                                            | Enforced by skill                                                                             |
| ------------------ | --------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `Crawl-delay: 5`   | Minimum 5s between requests                               | YES — hard minimum, cannot be lowered                                                         |
| "Uso particular"   | Personal legal cases, academic research, individual study | Documented; user must self-attest in script confirmation                                      |
| "Descarga masiva"  | Indiscriminate bulk extraction (vaguely defined)          | Hard cap of 50 docs per execution default; 200 with `--force-large` and explicit confirmation |
| "Usos comerciales" | Reselling, commercial DB, AI training data                | Forbidden; documented in SKILL.md                                                             |

---

## Reutilization for commercial purposes

To request authorization for commercial reuse or large-scale database building, contact CGPJ through
their Centro de Documentación Judicial:

<https://www.poderjudicial.es/cgpj/es/Servicios/Centro-de-Documentacion-Judicial>

---

_This document preserves the CENDOJ legal notice as captured 2026-05-22. Verify periodically against
the source for updates._
