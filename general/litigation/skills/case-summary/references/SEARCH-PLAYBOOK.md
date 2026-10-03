# Search Playbook — Base Queries

Practice-agnostic search queries for the eight core dimensions in `CORE-DIMENSIONS.md`. Every query below is a plain-text phrase the agent issues against the corpus. Backends (see `BACKENDS.md`) expose the queries through various modes — hybrid, semantic, keyword, entity, global overview, graph — and the agent chooses the mode that best fits the question (see **Query modes** below). This file does not embed tool-specific flags.

For practice-area specialization, see `PLAYBOOK-*.md`. A playbook extends the base queries with domain-specific variants.

---

## Query modes (conceptual)

| Mode | When it helps |
|---|---|
| **Hybrid** (semantic + keyword) | General factual queries — use as the default |
| **Semantic only** | Paraphrase-tolerant queries where exact wording varies (e.g., "admission against interest") |
| **Keyword only** | Specific strings (case numbers, dates, exhibit labels, proper names) |
| **Entity-focused** | "Who is X?", "What is Exhibit 4?" — canonical mentions of a named thing |
| **Global overview** | One-shot "what is this case about?" framing before deep-diving |
| **Graph / relational** | Cross-document relationships (party → event → document) |
| **Local neighborhood** | Tight context around a single known entity |

See `BACKENDS.md` for how a specific backend exposes each mode.

---

## 1. Parties & posture

- `"caption parties plaintiff defendant"`
- `"case number docket venue jurisdiction"`
- `"attorney of record appearance counsel"`
- `"party identity entity legal name"`
- `"related case consolidated coordinated"`

Use entity mode for canonical mentions of named parties or counsel.

## 2. Timeline

- `"date of incident occurrence event"`
- `"material event chronology"`
- `"notice deadline period expiration"`

Use keyword mode once a specific date is known — narrow with the date string itself.

## 3. Evidence inventory

- `"exhibit list attachment"`
- `"document produced Bates"`
- `"expert report opinion"`
- `"photograph video recording"`
- `"business record regularly kept"`

Use global-overview mode first on large corpora to discover document-type clusters.

## 4. Claims & legal theories

- `"cause of action claim count"`
- `"element prima facie case"`
- `"statute regulation governing"`
- `"legal theory claim relief"`

## 5. Exposure / remedies

- `"damages loss harm compensation"`
- `"relief requested prayer"`
- `"injunction declaratory"`
- `"attorneys fees costs"`
- `"prejudgment interest"`

## 6. Defenses

- `"affirmative defense denial"`
- `"statute of limitations repose"`
- `"release waiver settlement"`
- `"estoppel laches unclean hands"`
- `"answer defense verified"`

## 7. Procedural status

- `"scheduling order deadline"`
- `"pending motion brief"`
- `"discovery cutoff"`
- `"trial date hearing"`
- `"pre-suit notice prerequisite"`

## 8. Red flags & open threads

- `"admission statement against interest"`
- `"inconsistent statement prior"`
- `"spoliation missing evidence destroyed"`
- `"waiver consent ratification"`

---

## Composing queries from a loaded playbook

When the **Diagnose practice area** step loads one or more `PLAYBOOK-*.md` modules, combine queries in this order:

1. **Overview sweep first.** Run a single global-overview query ("what is this case about?") to anchor the rest.
2. **Base queries by dimension.** Walk the eight dimensions above. For each, issue the relevant base queries.
3. **Module queries layered on.** For each loaded playbook, issue the module-specific queries under the same dimension headings.
4. **Follow-ups driven by hits.** Re-query to narrow when a base or module query returns a load-bearing hit — e.g., after finding a key deposition, issue entity-mode queries for the witness name; after finding a damages document, issue keyword queries for the specific amounts.

Do not brute-force every query mechanically. The loop is: query → read 3–10 top chunks → decide whether to follow up, to move on, or to route the cluster to a sibling skill per `ROUTING.md`.

---

## Tuning tips

- Queries returning nothing relevant: try a semantic-only mode for paraphrase tolerance, or a shorter, more specific phrasing.
- Queries returning too many noisy hits: add a keyword anchor (party name, date, case number), or scope to a specific object/objects once inventory is done.
- Unfamiliar domain: run **global overview** first to discover the vocabulary the documents use, then re-issue queries with that vocabulary.
- Always cite hits by object name + page (or chunk ID). A hit that can't be cited is not a hit.
