# Source-content verifier

The tool that attacks the one problem `url-liveness` structurally cannot: **does the cited page actually say the number the playbook claims?** `url-liveness` proves a source is *alive* (HTTP 200). It says nothing about whether the figure next to the link is still — or ever was — what that page states. CLAUDE.md is explicit: *URL-liveness ≠ data-still-current; don't re-stamp `Last verified` on a 200 alone.* This closes that gap by re-reading source **content** and checking the claimed value against it.

It is **decision-support for a human reviewer**, not an autopilot. It produces evidence + a verdict draft; a person (or the maintainer's own review) decides the edit. It **never** auto-edits a playbook and **never** re-stamps `Last verified`. Internal-consistency tooling cannot establish external accuracy — see "What it cannot do".

## Two layers

| Layer | Where | Does |
|---|---|---|
| **1 · Deterministic harness** | `scripts/source-verify.py` (Python, testable) | Extract claim↔primary-source pairs → sample (fetch-free) → fetch + clean + cache the cited page (reusing `url-liveness.py`'s polite-fetch constraints) → run a **token-presence pre-filter** → emit `worklist.json`. No judgement. |
| **2 · LLM verification** | a Workflow (or Agent fan-out), spec'd below | Read the worklist → for each claim compare the claimed value against the fetched source excerpt → emit a verdict **with a quoted source span** → write a human-review report. |

The split is deliberate: the deterministic layer is unit-tested (`scripts/source-verify-test.py`) and cheap; the expensive, fallible LLM judgement is bounded to a sampled worklist and forced to quote its evidence.

## Layer 1 — the harness (CLI)

```bash
# Extract every primary-source-cited numeric/date/statute claim (no network):
python3 scripts/source-verify.py --extract                      # corpus-wide stats
python3 scripts/source-verify.py --extract --country=fr         # one scope (iso2 or shared/<stem>)
python3 scripts/source-verify.py --extract --json OUT.json      # dump all claim records

# Build a cost-bounded worklist (fetches only the sampled claims' URLs, politely):
python3 scripts/source-verify.py --build-worklist --sample=60   # default sample from config
python3 scripts/source-verify.py --build-worklist --country=fr --section=Tax
python3 scripts/source-verify.py --build-worklist --include-secondary   # also non-primary citations
```

What counts as a **claim**: a markdown link to a **primary** source (gov-suffix `.gov`/`.gouv`/`.gob` **or** an entry in `scripts/primary-source-allowlist.txt`) whose surrounding sentence carries ≥1 **salient** value token — a percentage, money amount, statute id, or specific date. A bare year does not count (too common to verify). Roster/navigation links carrying no figure are filtered out, and so are **"verify at &lt;authority&gt;" pointers** — a clause that exists to say the figure is *not* published at that link can only ever come back `TOKENS_ABSENT`, so it is never a claim (120 of 1,059 links on the 2026-08 corpus; `--extract` reports the count as `skipped_pointer_links`). The pointer test is anchored on the text immediately *before* the link, so "…rate not tabulated on the cited page, verify at INEC" trailing a real citation still counts as a claim. Config: `config/_source-verify.json`. Network politeness is **not** redefined there — the harness reads `config/_url-liveness.json` so both tools share one rate-limit / robots / gov-floor / Cloudflare policy.

Sampling is **fetch-free**: claims are scored from extract metadata only (`stale-marker` > never-verified > oldest `Last verified` stamp > salient statute/money), the top N are chosen, and only *their* URLs are fetched. So the LLM layer cost and the network footprint are both bounded by `--sample`.

### Worklist schema (`_local/source-verify/worklist.json`)

Each item:

```jsonc
{
  "id": "fr:95:1a2b3c4d",          // scope:line:url-hash
  "scope": "fr", "section": "Tax", "line_no": 95,
  "claim_text": "DMTO: 6.32 % default since Apr 2025 …",
  "values": [ {"type":"pct","raw":"6.32 %","needles":["6.32"],"salient":true},
              {"type":"date","raw":"Apr 2025","needles":["2025","Apr","2025-04"],"salient":true} ],
  "source_url": "https://www.service-public.gouv.fr/particuliers/actualites/A18183",
  "source_host": "service-public.gouv.fr", "source_tier": "primary-gov",
  "inline_stamp": {"date":"2026-05-27","kind":"verified"},   // or null
  "fetch_status": "OK",            // OK | DEAD | BINARY | EXCLUDED | ROBOTS | UNAVAILABLE
  "prior": "TOKENS_PRESENT",       // see priors below
  "matched_tokens": ["6.32","2025"], "strong_matched": ["6.32"], "missing_tokens": [],
  "excerpts": ["…le taux de 6,32 % s'applique depuis le 1ᵉʳ avril 2025…"]
}
```

**The deterministic prior** is a coarse, free pre-filter — it is *not* a verdict:

| Prior | Meaning | LLM layer should |
|---|---|---|
| `TOKENS_ABSENT` | **The claimed figure is literally not on the cited page.** Strongest signal — either a wrong citation, a moved figure, or a portal-root link that doesn't substantiate the claim. | Confirm/triage first. High mismatch prior. |
| `WEAK_MATCH` | Only bare 1–2-digit needles matched (noise-prone, e.g. "4" from "Art. 4 B"). | Resolve with the excerpt; treat as unverified until the *specific* figure is found. |
| `TOKENS_PRESENT` | A specific (≥3-char) figure from the claim appears on the page. | Read the excerpt, confirm it's the *same* figure in the *same* context (not a coincidental match). |
| `SOURCE_BINARY` | Cited page is a PDF/binary the harness doesn't parse. | Fetch the URL yourself (WebFetch) and read it. |
| `SOURCE_UNAVAILABLE` | Fetch failed / blocked / dead. | Cross-check with `url-liveness`; may be a Cloudflare challenge, not a dead source. |

`TOKENS_ABSENT` is independently useful **before any LLM runs** — it is a deterministic bug-catch (the `--build-worklist` run prints a `⚠️` count and lists them).

## Layer 2 — verification (the LLM half)

### Verdict schema (per claim)

```jsonc
{
  "id": "fr:95:1a2b3c4d",
  "verdict": "MATCH",   // MATCH | MISMATCH | STALE | PARTIAL | NOT_FOUND | SOURCE_UNAVAILABLE | INDETERMINATE
  "claimed": "6.32 % DMTO default since Apr 2025",
  "source_says": "« le taux de 6,32 % s'applique depuis le 1er avril 2025 »",  // REQUIRED quoted span
  "confidence": "HIGH", // HIGH | MEDIUM | LOW
  "note": "exact match incl. effective date"
}
```

Verdict definitions:
- **MATCH** — source states the same figure in the same context. *Requires a quoted span.*
- **MISMATCH** — source states a **different** figure for the same thing (the dangerous case — a wrong number, possibly wrong "in all six places consistently").
- **STALE** — source states a **newer** figure than the claim; the claim was right once. (Distinct from MISMATCH: direction matters for the fix.)
- **PARTIAL** — figure matches but a qualifier (effective date, scope, threshold) differs or is unconfirmed.
- **NOT_FOUND** — figure is not on this page (the cited URL doesn't substantiate it, even though the page is live).
- **SOURCE_UNAVAILABLE** — couldn't read the source (binary/blocked/dead) — *not* a comment on the claim.
- **INDETERMINATE** — source is ambiguous or the comparison can't be made confidently.

### Non-negotiable guardrails (this tool must not become a fabrication vector)

1. **Quote or abstain.** A `MATCH` / `MISMATCH` / `STALE` verdict **must** carry a verbatim `source_says` span copied from the fetched excerpt or the page. If you cannot quote the source, the verdict is at most `NOT_FOUND` / `INDETERMINATE`. **Never** assert a match "from memory" or because the number "looks right."
2. **Never edit, never re-stamp.** The output is a review report only. Do not modify any playbook and do not touch `Last verified`. A confirmed `MATCH` does **not** authorise a re-stamp on its own — re-stamping is a human decision over the *whole* claim's currency, not one figure (CLAUDE.md).
3. **Currency ≠ context.** A figure appearing on the page is necessary, not sufficient — confirm it describes the *same* tax/threshold/instrument the claim is about (the `WEAK_MATCH` "4" trap). Coincidental number collisions are `INDETERMINATE`, not `MATCH`.
4. **Source tier is fixed by the harness.** Do not "upgrade" a secondary source to primary to make a claim verifiable. If `--include-secondary` surfaced a non-primary citation, a match against it is `PARTIAL` at best.
5. **Report `SOURCE_UNAVAILABLE` honestly.** Don't fill the gap by guessing what a blocked/binary page probably says.

### Workflow orchestration

The Python harness can't run the LLM step (no FS access inside Workflow scripts). Rather than pass the worklist through `args` (large, and `args` arrives JSON-**stringified** — `args.count` reads as `undefined` and the fan-out silently runs zero agents), each agent **reads its own item from the worklist file by index**. Run in **throttled sequential batches of 8** — at the default ~16-wide concurrency the later-launched agents reliably fail with *"completed without calling StructuredOutput"* under load; batches of 8 eliminate it (proven on the 2026-06-02 corpus run: 24/40 failed at 16-wide, 0/24 failed at 8-wide).

```js
// Workflow metadata — phases must match the phase() calls below
export const meta = {
  name: 'verify-sources',
  description: 'Compare each playbook claim against its cited primary source; quote-or-abstain verdicts for human review',
  phases: [{ title: 'Verify' }],
}
const A = typeof args === 'string' ? JSON.parse(args) : (args || {})   // args may arrive stringified
const PATH = A.path || '_local/source-verify/worklist.json'
const COUNT = A.count || 40
const VERDICT = {
  type: 'object', additionalProperties: false,
  required: ['id', 'scope', 'line_no', 'source_url', 'verdict', 'claimed', 'source_says', 'confidence', 'note'],
  properties: {
    id: { type: 'string' }, scope: { type: 'string' }, line_no: { type: 'number' }, source_url: { type: 'string' },
    verdict: { enum: ['MATCH','MISMATCH','STALE','PARTIAL','NOT_FOUND','SOURCE_UNAVAILABLE','INDETERMINATE'] },
    claimed: { type: 'string' }, source_says: { type: 'string' },
    confidence: { enum: ['HIGH','MEDIUM','LOW'] }, note: { type: 'string' },
  },
}
const prompt = i =>
  `Verify ONE due-diligence claim against the PRIMARY source it cites, then OUTPUT THE VERDICT SCHEMA.\n` +
  `1. Read ${PATH}; take items[${i}] (0-based).\n` +
  `2. If item.excerpts is non-empty, use them. Else do AT MOST TWO WebFetch calls on item.source_url ` +
  `(load it via ToolSearch "select:WebFetch" if needed) and read the page (PDFs read fine).\n` +
  `3. Decide if the page substantiates item.claim_text's SPECIFIC figure/date/threshold.\n` +
  `RULES: quote-or-abstain (any MATCH/MISMATCH/STALE/PARTIAL needs a VERBATIM span in source_says, else NOT_FOUND/INDETERMINATE); ` +
  `a number counts only if it describes the SAME instrument the claim is about; never propose an edit; report SOURCE_UNAVAILABLE honestly.\n` +
  `Your FINAL action MUST be the StructuredOutput call. Copy id/scope/line_no/source_url verbatim from the item.`
const out = []
for (let b = 0; b < COUNT; b += 8) {
  const chunk = Array.from({ length: Math.min(8, COUNT - b) }, (_, k) => b + k)
  const res = await parallel(chunk.map(i => () =>
    agent(prompt(i), { agentType: 'general-purpose', schema: VERDICT, label: `verify:item-${i}`, phase: 'Verify' })))
  out.push(...res.filter(Boolean))
}
return out
```

Invoke from the session: `--build-worklist` → call `Workflow({ script, args: { count: <n>, path: '_local/source-verify/worklist.json' } })` → on return, the result is a wrapper `{result: [...verdicts]}` (read `.result`); merge, dedupe by `id`, and write to `_local/reports/source-verify-<scope>-<date>.md`, sorting `MISMATCH` / `STALE` / `NOT_FOUND` to the top. For a small sample, a plain Agent fan-out (one Agent call per item, same prompt + schema) is equivalent and simpler.

For `SOURCE_BINARY` / `SOURCE_UNAVAILABLE` items, the agent `WebFetch`es the URL itself (PDFs read fine; a JS-only SPA or a 403 bot-block stays `SOURCE_UNAVAILABLE`). The deterministic prior is **coarse** — expect it to over-report `TOKENS_ABSENT` for figures rendered in a different format than the needle (a PDF, a thousands-separator variant, a full vs abbreviated month) or behind a build-time SPA/redirect; the LLM layer re-fetches and corrects these to `MATCH`. That's the intended division of labour, not a bug.

## The deterministic audit (no LLM, scheduled, free)

`--audit` is the cheap half — it runs the whole pipeline **without any model** and emits a triage report. It is the payload of the monthly `source-verify.yml` cron and costs **$0** (public-repo runner, ~3–4 min cold / ~2 min warm over the 706 cited URLs).

```bash
# Corpus-wide audit — writes to _local/source-verify/
python3 scripts/source-verify.py --audit            # corpus-wide; writes _local/source-verify/audit/report.md
python3 scripts/source-verify.py --audit --ci       # CI: writes _ci/source-verify/ + GITHUB_OUTPUT
```

It surfaces three deterministic signals (tripwires, **not** verdicts):
- **`TOKENS_ABSENT`** — the claimed figure isn't on its cited page (portal-root, dead-content-behind-200, or a silently-changed number). Now checks **inside PDFs** too (poppler `pdftotext -layout`, falling back to `pypdf`; a scanned-image PDF lands in `PDF_NO_TEXT`, not a false absent).
- **`CONTENT_CHANGED`** — the cited page's content hash differs from last run; **`stale_changed`** (the high-priority bucket) is a page that changed *after* the claim's `Last verified` date. This is the freshness signal `url-liveness` structurally cannot give (it only sees the 200). The audit force-refreshes so it always re-compares; the cache artifact carries only the hashes.
- The **portal-root linter** (`scripts/check-citations.py`, pure-static, no network) flags bare-host citations sitting next to a percentage/money figure — appended to the audit issue as an advisory backlog (it is *not* a per-PR blocker — the standing count would be noise).

The audit **never** judges correctness ("is the number right?") — that's the LLM layer below. It only tells you which citations to *look at*.

## Cadence & cost

| Layer | Cost | Cadence |
|---|---|---|
| **`--audit`** (deterministic) | $0 (no model; free runner) | **Monthly cron** (`source-verify.yml`) → rolling `source-verify` issue |
| **LLM verification** | ~30–40k tokens/claim (pin Haiku/Sonnet, not Opus) | **On-demand / sampled**, human-gated |

The LLM half spends a call per claim, so it runs against a bounded sample (default 60) and is best pointed at:
- a **country about to be re-stamped** (run `--build-worklist --country=<iso2>` before bumping `Last verified` — verify the figures, don't trust the URL-200);
- the monthly audit's **`TOKENS_ABSENT` / `stale_changed`** lists (adjudicate the deterministic flags);
- **stale-marked / oldest-stamped** claims (the sampler already prioritises these).

A future `--update --verify-sources` hook could fold a sampled LLM pass into the Tier-A/B/C refresh cadence, gated behind human review.

## What it cannot do (the honest frame)

- It checks the **cited** source. It does not discover that a claim's *citation itself* is the wrong source, nor find a better one. A `MATCH` means "the page you linked says this," not "this is true of the world."
- It cannot verify claims with **no primary citation**, claims behind auth/paywalls, or figures only in scanned-PDF images.
- A confirmed `MATCH` moves a claim from *internally consistent* toward *externally grounded* — but external accuracy across 121 jurisdictions remains a permanent, never-fully-closed tension. This tool **shrinks the residual**; it does not eliminate it. Keep the decision-support framing and the confidence bands loud (CLAUDE.md § anti-hallucination contract).

## Files

- `scripts/source-verify.py` — the harness (extract / sample / fetch / PDF-extract / pre-filter / worklist / `--audit`)
- `scripts/check-citations.py` — static portal-root citation linter (no network, no deps)
- `scripts/source-verify-test.py` — unit tests (deterministic parts, incl. embedded-PDF extraction)
- `config/_source-verify.json` — extraction + verification + pdf + linter knobs (politeness lives in `config/_url-liveness.json`)
- `.github/workflows/source-verify.yml` — monthly deterministic-audit cron → rolling `source-verify` issue (no LLM, $0)
- `_local/source-verify/` — worklist + content cache + audit report (git-excluded; never committed)
- `_ci/source-verify/` — CI audit output (uploaded as artifact, never committed)
- `_local/reports/source-verify-*.md` — the human-review verdict reports
