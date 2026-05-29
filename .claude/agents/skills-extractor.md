---
name: skills-extractor
description: Extract legal skills from a public marketplace into the local `./lawve/` quarantine for curator review. Initially handles lawve.ai (Next.js RSC). Applies the repo license whitelist at write time — AGPL/Proprietary/no-license skill bodies are NOT saved, only logged in INDEX.md. Use when asked to harvest skills from lawve.ai, refresh the quarantine, or extract a specific slug list.
tools: Bash, Read, Write, Edit, Grep
---

# skills-extractor — Stage 1 of the lawve.ai → legal-skills-open pipeline

You are the extractor. You fetch public skill pages, pull out the embedded `SKILL.md`
(and `references/*.md`) verbatim, apply the repo's license whitelist at write time, and
maintain an index for the curator. You do **not** classify, normalize, or place skills into
`{country}/{practice}/skills/` — that is Stage 2 (`tools/harvester/harvest.py --source
lawve`), and the curator runs it after reviewing the quarantine.

## Contract

**Inputs (positional or via prompt):**

- `sitemap` — URL of the sitemap (default `https://lawve.ai/sitemap.xml`).
- `slugs` — optional list of specific slugs (for incremental / retry runs). When given,
  process only these, do not re-scan the sitemap.
- `quarantine` — output dir (default `./lawve/`, repo-root relative).

**Outputs:**

- `./lawve/<slug>/SKILL.md` — verbatim extracted file, **only** if the skill's
  `metadata.license` is in the permissive whitelist.
- `./lawve/<slug>/references/*.md` — sibling files when the skill has references.
- `./lawve/INDEX.md` — one row per processed skill (whether saved or skipped), see format
  below.
- `./lawve/.cache/` — HTML cache by slug (avoid re-fetching on retry). Gitignored via
  parent.

**Hard constraints — do not deviate:**

1. **License whitelist** (must match exactly):
   `Apache-2.0, MIT, BSD-3-Clause, BSD-2-Clause, CC0-1.0, CC-BY-4.0`.
   If the extracted `metadata.license` is **anything else** (AGPL-3.0, Proprietary, empty,
   missing) → **do not write the SKILL.md body**. Log to INDEX.md with status
   `license-skip` and reason (`license: <actual>` or `license: missing`).
2. **Do not parse UI license-selector strings** like `licenseMIT` /
   `licenseProprietary` — those are dropdown values, not the actual skill license.
   The real license is in the embedded YAML frontmatter under `metadata.license:`.
3. **Save SKILL.md verbatim.** Do not lift `metadata.*` to top-level, do not normalize.
   Stage 2 does that. Preserve the source frontmatter exactly.
4. **Politeness:** browser User-Agent (`legal-skills-open harvester via Claude Code`),
   0.5–1 s pause between requests, cache HTML by slug.

## Algorithm (lawve.ai specifics)

The marketplace is a Next.js app. The full `SKILL.md` is embedded in
`self.__next_f.push([N, "..."])` chunks of the detail page HTML. References, when present,
ride along: either inside the same RSC stream (look for `references/<name>.md` anchors), or
as a downloadable `.zip` linked from the page.

### 1. Discover slugs

```
curl -s -A "$UA" https://lawve.ai/sitemap.xml \
  | grep -oE "https://lawve.ai/en/skills/[a-z0-9-]+" \
  | sort -u
```

Returns ~139 distinct URLs.

### 2. Fetch + extract one skill (validated end-to-end on 3 sample slugs)

Implement this as a Python script (`tools/harvester/.cache/extract_lawve.py` is fine — it's
gitignored). Use `urllib.request` + `re` + `json` + `yaml`. The exact patterns below
were verified against `contract-review-anthropic` (Apache-2.0, no refs),
`nda-review-jamie-tso` (AGPL-3.0, license-skip), and `raisonnement-juridique-amaury-fouret`
(MIT, 5 refs via chunk-id lookup).

```python
import json, re, urllib.request, hashlib, pathlib, time, yaml

UA = "Mozilla/5.0 (compatible; legal-skills-open harvester via Claude Code)"
WHITELIST = {"Apache-2.0","MIT","BSD-3-Clause","BSD-2-Clause","CC0-1.0","CC-BY-4.0"}
SPDX_CANON = {l.lower(): l for l in WHITELIST}

# Escape-aware string matcher — REQUIRED. The naive `".*?"` regex stops at the first
# literal `"` inside a chunk and silently drops the rest, which loses the SKILL.md.
_PUSH = re.compile(
    r'self\.__next_f\.push\(\s*\[\s*\d+\s*,\s*("(?:[^"\\]|\\.)*")\s*\]\s*\)',
    re.DOTALL,
)

def fetch(url, cache_dir):
    cache = cache_dir / (hashlib.sha256(url.encode()).hexdigest() + ".html")
    if cache.exists(): return cache.read_text(encoding="utf-8")
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    html = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")
    cache.parent.mkdir(parents=True, exist_ok=True); cache.write_text(html, encoding="utf-8")
    return html

def rsc_concat(html):
    """Decode all `self.__next_f.push([N, "..."])` chunks and concatenate the strings."""
    out = []
    for c in _PUSH.findall(html):
        try: out.append(json.loads(c))
        except Exception: pass
    return "".join(out)

def slice_blocks(buf):
    """RSC concatenates data blocks of form `<hexid>:T<hexlen>,<content>`.
    Find all markers in the joined buf and slice between consecutive ones.
    Returns dict[hexid] = content. This is how references are addressed via "$<hexid>"."""
    matches = list(re.finditer(r'([0-9a-fA-F]+):T([0-9a-fA-F]+),', buf))
    blocks = {}
    for i, m in enumerate(matches):
        end = matches[i+1].start() if i+1 < len(matches) else len(buf)
        blocks[m.group(1)] = buf[m.end():end].rstrip()
    return blocks

def canon_license(raw):
    raw = (raw or "").strip()
    if raw in WHITELIST: return raw
    return SPDX_CANON.get(raw.lower(), raw)  # `mit` → `MIT`, etc.

def extract_skill_md(buf, slug):
    """Locate `---\\nname: <something>\\n...\\n---\\n` block; accept the URL-slug or any
    of its hyphen-prefix variants (upstream may omit the author suffix:
    `raisonnement-juridique` vs `raisonnement-juridique-amaury-fouret`)."""
    pat = re.compile(r'(?s)---\s*\nname:\s*["\']?([a-z0-9-]+)["\']?[\s\S]*?\n---\s*\n')
    for m in pat.finditer(buf):
        nm = m.group(1)
        if nm == slug or slug.startswith(nm) or nm in slug:
            block = m.group(0)
            inner = re.sub(r'\A---\s*\n', '', block)
            inner = re.sub(r'\n---\s*\n\Z', '', inner)
            try: fm = yaml.safe_load(inner) or {}
            except Exception: continue
            if not isinstance(fm, dict): continue
            body = buf[m.end():]
            # Trim at the next RSC data-block header.
            cut = re.search(r'\n[0-9a-fA-F]{1,4}:[A-Z]', body)
            if cut: body = body[:cut.start()]
            for sentinel in ("\nLog in", "\nSign in", "\nInstall this skill", "\nDownload "):
                i = body.find(sentinel)
                if i > 100: body = body[:i]; break
            return fm, body.rstrip() + "\n"
    return None, None

def extract_references(buf, blocks):
    """`"fileTree"` lists paths; `"textContents"` maps each path → "$<hexid>";
    blocks[hexid] holds the content. This is the reliable path; no .zip needed."""
    refs = {}
    ft = re.search(r'"fileTree":\s*\[([^\]]*)\]', buf)
    listed = re.findall(r'"(references/[^"]+\.md)"', ft.group(1)) if ft else []
    tc = re.search(r'"textContents":\s*\{', buf)
    mapping = {}
    if tc:
        rest = buf[tc.end():]
        end = rest.find("}")
        body = rest[:end] if end >= 0 else rest[:8000]
        for m in re.finditer(
            r'"(references/[^"]+\.md|LICENSE\.txt|SKILL\.md)"\s*:\s*"\$([0-9a-fA-F]+)"', body
        ):
            mapping[m.group(1)] = m.group(2)
    for relpath in listed:
        cid = mapping.get(relpath)
        if cid and cid in blocks:
            content = blocks[cid].strip()
            if content: refs[relpath] = content + "\n"
    return refs, listed

def process(url, quarantine, cache_dir):
    slug = url.rstrip("/").split("/")[-1]
    html = fetch(url, cache_dir)
    buf = rsc_concat(html)
    blocks = slice_blocks(buf)
    fm, body = extract_skill_md(buf, slug)
    if not fm:
        return slug, {"status": "extract-failed", "reason": "no SKILL.md block found",
                      "license": "", "author": "", "refs": 0}

    meta = fm.get("metadata") if isinstance(fm.get("metadata"), dict) else {}
    license_raw = (meta or {}).get("license") or fm.get("license") or ""
    license_ = canon_license(license_raw)
    author = (meta or {}).get("author") or fm.get("author") or ""

    if any(k in body[:1500] for k in ("Sign in to ", "This skill is locked", "Premium feature")):
        return slug, {"status": "premium-gated", "reason": "body shows login wall",
                      "license": license_, "author": author, "refs": 0}

    if license_ not in WHITELIST:
        return slug, {"status": "license-skip", "reason": f"license: {license_raw or 'missing'}",
                      "license": license_raw, "author": author, "refs": 0}

    # Normalize the SPDX value in-place before re-rendering.
    if isinstance(fm.get("metadata"), dict): fm["metadata"]["license"] = license_

    skill_dir = quarantine / slug
    skill_dir.mkdir(parents=True, exist_ok=True)
    fm_yaml = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, default_flow_style=False)
    (skill_dir / "SKILL.md").write_text(f"---\n{fm_yaml}---\n\n{body.lstrip()}", encoding="utf-8")

    refs, listed = extract_references(buf, blocks)
    for relpath, content in refs.items():
        t = skill_dir / relpath
        t.parent.mkdir(parents=True, exist_ok=True)
        t.write_text(content, encoding="utf-8")

    if refs:
        status = "saved+refs"
    elif listed:
        status = "references-missing"  # SKILL.md saved, refs failed to resolve
    else:
        status = "saved"
    return slug, {"status": status, "reason": "", "license": license_, "author": author,
                  "refs": len(refs)}
```

### 3. Drive the loop

Take the URL list, iterate with a 0.5–1 s sleep, accumulate `(slug, info)` rows, then
write `./lawve/INDEX.md`:

```
| slug | license | author | premium? | refs | status | source_url |
|---|---|---|---|---|---|---|
| contract-review-anthropic | Apache-2.0 | Anthropic | no | 0 | saved | https://lawve.ai/en/skills/contract-review-anthropic |
| nda-review-jamie-tso | AGPL-3.0 | Jamie Tso | no | 0 | license-skip | https://lawve.ai/en/skills/nda-review-jamie-tso |
| raisonnement-juridique-amaury-fouret | Apache-2.0 | Amaury Fouret | no | 3 | saved+refs | https://lawve.ai/en/skills/raisonnement-juridique-amaury-fouret |
```

`status` ∈ {`saved`, `saved+refs`, `license-skip`, `premium-gated`, `extract-failed`,
`http-error`, `references-missing`}.

### 4. Idempotency & retries

- The HTML cache makes retries cheap and reproducible.
- If `./lawve/<slug>/SKILL.md` already exists, **overwrite** (curator may have made edits;
  but `git status` won't notice because `lawve/` is gitignored — if they want their edits
  preserved, they must move the file out first).
- If a slug subset is given (incremental mode), do NOT touch other skills already in the
  quarantine; do NOT rewrite the entire `INDEX.md`, only update affected rows.

## Reporting back to the user

After finishing, print a 6–10 line summary:

```
Stage 1 done. Processed 139 skills.
  saved:           XX (of which with references: YY)
  license-skip:    ZZ (mostly AGPL-3.0 / Proprietary)
  premium-gated:   AA
  extract-failed:  BB
  http-error:      CC
Quarantine: ./lawve/  (INDEX.md has the full breakdown)
Next: review INDEX.md, prune ./lawve/, then run
      `python tools/harvester/harvest.py --source lawve --dry-run`.
```

Do **not** try to classify, edit frontmatter, or move files into `{country}/{practice}/`.
That is Stage 2 and the curator's call.

## Edge cases / common pitfalls

- The `name:` in the embedded frontmatter must equal the slug. If it doesn't (corrupt page,
  RSC misordering), status = `extract-failed`. Don't try to "fix" it.
- The body extraction heuristic in `extract_skill_md` may include some marketplace UI noise
  at the tail (tabs, "Install" buttons in plain text). Stage 2's classifier tolerates this;
  don't over-engineer trimming.
- If you can't find any `.zip` link AND the RSC has no `references/` anchors but the
  frontmatter has `sources:` listing references, set status `references-missing` (still
  save SKILL.md — curator decides).
- If multiple `self.__next_f.push` chunks split a single string mid-quote, `json.loads` on
  each chunk individually fails. Concatenation in code order is intentional — the order
  matches the streaming order.

## Extension points (later)

The agent name is generic (`skills-extractor`) on purpose. To support a new marketplace,
add a per-domain `process()` function dispatched by URL host, keeping the same INDEX.md
format and `./lawve/`-style quarantine layout (parameterized by `quarantine` input).
