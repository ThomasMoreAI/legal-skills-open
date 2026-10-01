#!/usr/bin/env bash
# Mutation proof for spec_check.
#
# Each mutant is a semantic WEAKENING of exactly one check. A mutant that
# survives means the suite passes with that check disabled — the check is
# decorative and the tests that "cover" it prove nothing.
#
# The whole skill directory is copied to a scratch dir and mutated THERE. The
# working tree is never written to, so an interrupted run cannot destroy
# uncommitted work and there is no revert step that could restore a stale mtime.
#
# THREE THINGS THIS HARNESS DOES THAT THE OBVIOUS ONE DOES NOT. The first cut
# had all three holes and a cross-model review found them:
#
#   1. A nonzero exit is NOT a kill. `PYTEST_ADDOPTS=--bogus` made the first
#      version report "killed 14/14" while pytest collected nothing. A kill now
#      requires pytest to have RUN the same number of tests as the clean
#      baseline and to report at least one FAILED.
#   2. A crash is NOT a kill. Mutating `if not m:` to `if False:` leaves a None
#      dereferenced two lines later, so the "kill" was an AttributeError, not an
#      assertion detecting weakened behaviour. Mutants now disable the FINDING,
#      never the guard that makes the finding reachable, and any mutant killed
#      only by an unexpected exception is reported CRASH and fails the run.
#   3. The harness needs its own positive control. A NULL mutant — a comment
#      change that alters nothing — must SURVIVE. If it is reported killed, the
#      harness is broken and every other verdict is worthless.
#
# Usage:  tests/mutation.sh [python]
set -uo pipefail

PY="${1:-/usr/bin/python3}"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONDONTWRITEBYTECODE=1   # a same-length mutant is otherwise masked by a stale .pyc
unset PYTEST_ADDOPTS               # an inherited addopts can break collection silently

if ! "$PY" -c 'import pytest' 2>/dev/null; then
  echo "mutation.sh: $PY has no pytest" >&2; exit 2
fi

# --- baseline: how many tests must run, and do they all pass clean? ----------
base="$(mktemp -d)"; cp -R "$HERE/scripts" "$HERE/tests" "$base/"; cp "$HERE/SKILL.md" "$base/"
if ! "$PY" -m pytest "$base/tests/test_spec_check.py" -q >"$base/out.txt" 2>&1; then
  echo "mutation.sh: the UNMUTATED suite does not pass — fix that first" >&2
  tail -20 "$base/out.txt" >&2; rm -rf "$base"; exit 2
fi
BASELINE=$(grep -oE '^[0-9]+ passed' "$base/out.txt" | grep -oE '^[0-9]+' | head -1)
rm -rf "$base"
if [ -z "${BASELINE:-}" ] || [ "$BASELINE" -lt 1 ]; then
  echo "mutation.sh: could not read a baseline test count" >&2; exit 2
fi
echo "baseline: $BASELINE tests pass clean"
echo

# name<TAB>from<TAB>to  — `from` must appear EXACTLY once in the source, which is
# asserted per mutant; a substitution that silently matches zero or many places
# would report a fake survivor.
#
# NULL is the harness's own positive control and must appear first.
read -r -d '' MUTANTS <<'EOF' || true
NULL-control-must-survive	"""spec_check — the deterministic half	"""spec_check (null) — the deterministic half
C1-required-empty	    return PROFILES[profile]["required"]	    return ()
C1-required-downgraded-to-warn	                "C1-missing-section", "fail",	                "C1-missing-section", "warn",
C2-status-finding-suppressed	        add(Finding("C2-no-status", "fail",	        _ = (Finding("C2-no-status", "fail",
C2-supersede-finding-suppressed	                add(Finding("C2-dangling-supersede", "fail",	                _ = (Finding("C2-dangling-supersede", "fail",
C2-status-line-unanchored	[·|])[ \t]{0,8}	])[ \t]{0,8}
C3-reversal-finding-suppressed	        add(Finding("C3-no-reversal-cost", sev,	        _ = (Finding("C3-no-reversal-cost", sev,
C3-placeholder-accepted	    if rm is not None and PLACEHOLDER.match(rm_val.strip()):	    if False:
C4-negation-never-matches	            if NEGATION_HEAD.match(head):	            if False:
C5-one-alternative-is-enough	        if len(entries) < 2:	        if len(entries) < 1:
C5-rejection-never-required	        if not REJECTION_MARKERS.search(" ".join(b for _, b in entries)):	        if False:
C6-cost-always-found	        if dsec and not COST_LANGUAGE.search(prose(dsec)):	        if False:
C7-next-step-always-found	        if not NEXT_STEP.search(body):	        if False:
C8-acceptance-always-measurable	        if asec and not MEASURABLE.search(prose(asec)):	        if False:
C9-manual-never-detected	    if hits < MIN_TRADEOFF_HITS and words > MIN_WORDS:	    if False:
C9-zero-hits-is-enough	MIN_TRADEOFF_HITS = 1	MIN_TRADEOFF_HITS = 0
C9-reads-metadata-too	    hits = len(TRADEOFF_LANGUAGE.findall(body_prose(sections)))	    hits = len(TRADEOFF_LANGUAGE.findall(text))
C10-size-never-warns	    if pages > MAX_PAGES:	    if False:
C11-links-never-checked	        for url in URL_RE.findall(text):	        for url in []:
subtree-is-a-noop	            parts.append(nxt.body)	            pass
subtree-body-includes-titles	            bodies.append(nxt.body)	            bodies.append(nxt.title)
profile-downgrades-short-docs	    prof = profile or infer_profile(path)	    prof = profile or ("note" if words < 700 else infer_profile(path))
fenced-code-not-stripped	        raw = FENCE_RE.sub("", raw)	        pass
html-comments-not-stripped	    raw = re.sub(r"(?s)<!--.*?-->", " ", raw)	    raw = raw
front-matter-not-hoisted	        front = hoist_front_matter(raw)	        front = ""
typographic-quotes-not-folded	    raw = fold_quotes(raw)	    pass
r2-front-matter-appended	        return sections, front + _strip_html(raw)	        return sections, _strip_html(raw) + front
r2-suffix-not-preferred	                score = 700 + len(name)	                score = 500 + len(name)
r2-continuations-dropped	            if cont and bullets:	            if False:
r2b-md-comments-not-stripped	    raw = strip_comments(raw)	    pass
r2b-unterminated-comment-kept	    return re.sub(r"(?s)<!--.*\Z", " ", raw)	    return raw
r2b-li-without-newline	    s = re.sub(r"(?is)<li[^>]*>", "\n- ", s)	    s = s
r2b-first-status-wins	    m = candidates[-1] if candidates else None	    m = candidates[0] if candidates else None
r2b-comma-not-a-separator	                    for x in re.split(r"\s*[,;]\s*|\s+(?:and|&|/|\+)\s+", t)	                    for x in re.split(r"(?!x)x", t)
r3-no-word-boundary-suffix	            elif t.endswith(name) and _boundary_before(t, len(t) - len(name)):	            elif t.endswith(name):
r3-tables-unreadable	        rows = table_rows(src)	        rows = []
r3-status-region-ignored	    head_end = _metadata_region_end(sections, text)	    head_end = len(text)
r3-front-matter-any-comment	    if not keys & FRONT_MATTER_KEYS:	    if False:
r3-metadata-headings-ignored	        if t in METADATA_HEADINGS:	        if False:
r4-region-fails-open	        if sec.offset >= 0:	        if False:
r4-offset-not-recorded	            sec.offset = base + len(_strip_html(raw[:_s]))	            sec.offset = -1
r4-only-first-comment	    for cand in ONE_COMMENT.findall(block.group(1)):	    for cand in ONE_COMMENT.findall(block.group(1))[:1]:
r4-status-heading-unread	    if m is None and heading_status:	    if False:
r4-span-not-lowered	    s = re.sub(r"(?is)</(p|div|li|h[1-6]|blockquote|span|strong|em|b|i)>", "\n", s)	    s = re.sub(r"(?is)</(p|div|li|h[1-6]|blockquote)>", "\\n", s)
cr-ssrf-guard-disabled	            blocked = _unsafe_target(url)	            blocked = ""
cr-directory-accepted	        if not doc.is_file():	        if not doc.exists():
cr-th-not-marked	    s = re.sub(r"(?is)</th>", " |\u241f ", s)	    s = re.sub(r"(?is)</th>", " | ", s)
classify-single-class-only	)[:max(1, len(segments))]	)[:1]
EOF

killed=0; survived=0; broken=0; crashed=0; null_ok=0
printf '%-36s %s\n' "MUTANT" "VERDICT"
printf '%-36s %s\n' "------------------------------------" "-------"

while IFS=$'\t' read -r name from to; do
  [ -z "${name:-}" ] && continue
  scratch="$(mktemp -d)"
  cp -R "$HERE/scripts" "$HERE/tests" "$scratch/"
  cp "$HERE/SKILL.md" "$scratch/"   # a test asserts SKILL.md against PROFILES
  src="$scratch/scripts/spec_check.py"

  # Refuse a substitution that is not unique: zero matches makes an inert mutant
  # that survives for the wrong reason, many matches changes more than one check.
  n=$("$PY" - "$src" "$from" <<'PY'
import sys
print(open(sys.argv[1], encoding="utf-8").read().count(sys.argv[2]))
PY
)
  if [ "$n" != "1" ]; then
    printf '%-36s BROKEN (anchor matched %s times)\n' "$name" "$n"
    broken=$((broken + 1)); rm -rf "$scratch"; continue
  fi

  "$PY" - "$src" "$from" "$to" <<'PY'
import sys
p, a, b = sys.argv[1], sys.argv[2], sys.argv[3]
s = open(p, encoding="utf-8").read()
open(p, "w", encoding="utf-8").write(s.replace(a, b, 1))
PY

  "$PY" -m pytest "$scratch/tests/test_spec_check.py" -q --tb=line \
      >"$scratch/out.txt" 2>&1
  rc=$?
  ran=$(grep -oE '[0-9]+ (passed|failed)' "$scratch/out.txt" \
        | grep -oE '^[0-9]+' | paste -sd+ - | bc 2>/dev/null || echo 0)
  nfail=$(grep -cE '^FAILED' "$scratch/out.txt" || true)

  if [ "$name" = "NULL-control-must-survive" ]; then
    if [ "$rc" -eq 0 ]; then
      printf '%-36s survived (correct — harness is live)\n' "$name"; null_ok=1
    else
      printf '%-36s KILLED  <-- HARNESS BROKEN: a no-op mutant failed the suite\n' "$name"
    fi
    rm -rf "$scratch"; continue
  fi

  if [ "$rc" -eq 0 ]; then
    printf '%-36s SURVIVED  <-- the suite does not test this\n' "$name"
    survived=$((survived + 1))
  elif [ "${ran:-0}" != "$BASELINE" ]; then
    # pytest exited nonzero without running the whole suite: a usage error, a
    # collection error, an import failure. Not a kill, and the single most
    # dangerous false positive this harness can produce.
    printf '%-36s BROKEN (ran %s/%s tests, rc=%s — not a kill)\n' \
      "$name" "${ran:-0}" "$BASELINE" "$rc"
    broken=$((broken + 1))
  elif [ "$nfail" -eq 0 ]; then
    printf '%-36s BROKEN (rc=%s but no FAILED line)\n' "$name" "$rc"
    broken=$((broken + 1))
  elif grep -qE '(AttributeError|TypeError|NameError|IndexError|KeyError)' \
         "$scratch/out.txt"; then
    # The mutant crashed rather than producing wrong-but-valid output. That
    # proves the code path executes, not that any assertion is sensitive to it.
    printf '%-36s CRASH   <-- killed by an exception, not an assertion\n' "$name"
    crashed=$((crashed + 1))
  else
    printf '%-36s killed (%s assertion failure(s))\n' "$name" "$nfail"
    killed=$((killed + 1))
  fi
  rm -rf "$scratch"
done <<< "$MUTANTS"

total=$((killed + survived + crashed))
echo
echo "killed $killed/$total   survived $survived   crash-kills $crashed   broken-anchor $broken"
rc=0
[ "$null_ok" -ne 1 ] && { echo "FAIL: the null control did not survive — every verdict above is void"; rc=1; }
[ "$broken" -gt 0 ] && { echo "FAIL: a mutant did not run cleanly (see BROKEN above)"; rc=1; }
[ "$crashed" -gt 0 ] && { echo "FAIL: a mutant was killed by a crash, not an assertion"; rc=1; }
[ "$survived" -gt 0 ] && { echo "FAIL: a check survived its own mutant"; rc=1; }
[ "$rc" -eq 0 ] && echo "OK: null control survived; every check killed by an assertion"
exit "$rc"
