#!/usr/bin/env python3
"""evidence — ground a claim about a member's public work in something actually fetched.

Four stateless subcommands, each stdlib-only, each prints one JSON object and
writes nothing to disk:

  code           --repo OWNER/REPO --path PATH [--ref REF] [--start-line N]
                 [--end-line N]
                 A bounded, cited excerpt of one public GitHub file, pinned to
                 a commit SHA. Used by /lq-connect (a candidate's own linked
                 repo) and, once a build is resolved, by /lq-ask.

  page           --url URL [--max-chars N]
                 A bounded, cited excerpt of one public page's visible text
                 (a Substack post, a personal website). Never used for
                 LinkedIn: an unauthenticated fetch there returns a login
                 wall, not content, so it is not worth attempting.

  search-builds  QUERY [--limit N]
                 Keyword search over the live builds directory
                 (legalquants.com/builds). Confirmed record shape: {id,
                 title, description, practiceArea, by} — no repo link, no
                 profile slug. /lq-ask only.

  resolve-member NAME [--limit N]
                 Look a builder's display name up in the live public
                 directory (legalquants.com/community) to get their real
                 profile slug and, when present, their featuredWork's own
                 live URL. This is what turns a bare name from
                 `search-builds` into a citation instead of a guess — an
                 unresolved or ambiguous name returns ok: false rather than
                 a best-effort slug. /lq-ask only (/lq-connect already has
                 the candidate's slug from its own directory match).

Every subcommand fails honestly: `{"ok": false, "reason": ...}` on anything
unfetchable, unparseable, ambiguous, or excluded — never an invented entry,
slug, or quote. `--fixture-html`/`--fixture-raw` replace the one live fetch
each subcommand makes with a local file, for tests; no other network
isolation is needed because every call here is a single independent GET.

The legalquants.com pages are Next.js App Router pages: the data a viewer
sees is embedded in the initial HTML as an escaped JSON string inside a
`self.__next_f.push(...)` chunk, not a documented API. This is the same
class of dependency Onur's community MCP prototype flagged in its own
design doc: "an undocumented website integration: site changes can break
it." Parsing here is deliberately narrow (a small, specific regex per
confirmed shape) so a change that breaks it fails loudly (no records
parsed) rather than silently returning stale or wrong data.
"""

from __future__ import annotations

import argparse
import html as html_module
import json
import re
import urllib.error
import urllib.request
from datetime import UTC, datetime
from html.parser import HTMLParser
from pathlib import Path

USER_AGENT = (
    "Mozilla/5.0 (compatible; codex-for-legal/companion; member evidence lookup)"
)
TIMEOUT = 20

MAX_EXCERPT_LINES = 120
MAX_EXCERPT_CHARS = 16_000
MAX_PAGE_CHARS_DEFAULT = 4_000
MAX_PAGE_CHARS_CAP = 16_000

# A challenge page is served by the right host with a success status, and is
# not the content — the one failure that looks healthy all the way
# downstream. Same idea, and a slice of the same signature list, as
# skills/core/regulatory/scripts/fetch_source.py; duplicated rather than
# imported because these are separate skills that ship in separate plugins.
BOT_CHALLENGE_SIGNATURES = (
    b"just a moment...",
    b"checking your browser",
    b"cf-browser-verification",
    b"__cf_chl",
    b"captcha",
)

EXCLUDED_PATH_PATTERNS = (
    re.compile(r"(^|/)node_modules/"),
    re.compile(r"(^|/)\.git/"),
    re.compile(
        r"(^|/)(package-lock\.json|pnpm-lock\.yaml|yarn\.lock|Cargo\.lock|poetry\.lock|uv\.lock)$"
    ),
    re.compile(r"(^|/)\.env(\.|$)"),
    re.compile(r"(secret|credential|private[-_]?key|id_rsa)", re.IGNORECASE),
    re.compile(r"\.(pem|key|pfx|p12)$", re.IGNORECASE),
)


def now_iso() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def ok(**fields) -> dict:
    return {"ok": True, **fields}


def fail(reason: str, **fields) -> dict:
    return {"ok": False, "reason": reason, **fields}


def http_get(url: str, accept: str = "*/*") -> tuple[int, bytes, str]:
    """Returns (status, body, final_url). Never raises on an HTTP error status."""
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": accept,
            "Accept-Encoding": "identity",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
            return response.status, response.read(), response.geturl()
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read() or b"", url
    except urllib.error.URLError:
        return 0, b"", url


def bot_challenge(body: bytes) -> str | None:
    lowered = body[:200_000].lower()
    for signature in BOT_CHALLENGE_SIGNATURES:
        if signature in lowered:
            return signature.decode()
    return None


def json_unescape(fragment: str) -> str:
    """A captured field is already valid JSON-string content (minus its
    quotes) — wrap and decode rather than hand-rolling escape rules."""
    try:
        return json.loads(f'"{fragment}"')
    except ValueError:
        return fragment


# --- code -------------------------------------------------------------


def excluded_path(path: str) -> bool:
    return any(pattern.search(path) for pattern in EXCLUDED_PATH_PATTERNS)


def cmd_code(args) -> dict:
    if not re.fullmatch(r"[\w.-]+/[\w.-]+", args.repo or ""):
        return fail("bad_repo", detail="expected owner/repo")
    if ".." in (args.path or "") or (args.path or "").startswith("/"):
        return fail("bad_path")
    if excluded_path(args.path):
        return fail("excluded_path", path=args.path)

    if args.fixture_raw:
        text = Path(args.fixture_raw).read_text(encoding="utf-8", errors="replace")
        ref = args.ref or "fixture"
    else:
        ref = args.ref
        if not ref:
            status, body, _ = http_get(f"https://api.github.com/repos/{args.repo}")
            if status != 200:
                return fail("repo_not_found", repo=args.repo, status=status)
            try:
                ref = json.loads(body)["default_branch"]
            except (ValueError, KeyError):
                return fail("repo_metadata_unparseable", repo=args.repo)
        status, body, final_url = http_get(
            f"https://raw.githubusercontent.com/{args.repo}/{ref}/{args.path}"
        )
        if status != 200:
            return fail(
                "file_not_found", repo=args.repo, path=args.path, ref=ref, status=status
            )
        if bot_challenge(body):
            return fail("bot_challenge", url=final_url)
        text = body.decode("utf-8", errors="replace")

    # Resolve the pinned commit SHA separately so a citation names an exact
    # point in history, not a moving branch — skipped for a fixture read.
    commit_sha = ref
    if not args.fixture_raw and not re.fullmatch(r"[0-9a-f]{40}", ref):
        status, body, _ = http_get(
            f"https://api.github.com/repos/{args.repo}/commits/{ref}"
        )
        if status == 200:
            try:
                commit_sha = json.loads(body)["sha"]
            except (ValueError, KeyError):
                pass  # cite by branch name; don't fail an otherwise-successful fetch

    lines = text.splitlines()
    total = len(lines)
    start = max(1, args.start_line or 1)
    end = min(total, args.end_line or total, start + MAX_EXCERPT_LINES - 1)
    if start > total:
        return fail("line_range_out_of_bounds", total_lines=total)
    excerpt = "\n".join(lines[start - 1 : end])
    truncated = len(excerpt) > MAX_EXCERPT_CHARS or end < (args.end_line or total)
    excerpt = excerpt[:MAX_EXCERPT_CHARS]
    return ok(
        repo=args.repo,
        path=args.path,
        commit_sha=commit_sha,
        start_line=start,
        end_line=end,
        truncated=truncated,
        text=excerpt,
    )


# --- page ---------------------------------------------------------------


class _VisibleTextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self._skip_depth = 0
        self.chunks: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "noscript"):
            self._skip_depth += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript") and self._skip_depth:
            self._skip_depth -= 1

    def handle_data(self, data):
        if not self._skip_depth and data.strip():
            self.chunks.append(data.strip())


def visible_text(html: str) -> str:
    extractor = _VisibleTextExtractor()
    extractor.feed(html)
    return html_module.unescape(" ".join(extractor.chunks))


def cmd_page(args) -> dict:
    if args.fixture_html:
        body = Path(args.fixture_html).read_bytes()
        final_url = args.url or "fixture"
    else:
        if not re.match(r"^https?://", args.url or ""):
            return fail("bad_url")
        status, body, final_url = http_get(args.url, accept="text/html,*/*;q=0.8")
        if status != 200:
            return fail("http_error", status=status)

    challenge = bot_challenge(body)
    if challenge:
        return fail("bot_challenge", matched=challenge)

    text = visible_text(body.decode("utf-8", errors="replace"))
    max_chars = min(args.max_chars or MAX_PAGE_CHARS_DEFAULT, MAX_PAGE_CHARS_CAP)
    truncated = len(text) > max_chars
    return ok(
        url=final_url,
        retrieved_at=now_iso(),
        truncated=truncated,
        text=text[:max_chars],
    )


# --- search-builds --------------------------------------------------------

BUILDS_URL = "https://www.legalquants.com/builds"
BUILD_RECORD_RE = re.compile(
    r'\{\\"id\\":\\"(?P<id>[0-9a-f-]{36})\\",'
    r'\\"title\\":\\"(?P<title>(?:[^"\\]|\\.)*?)\\",'
    r'\\"description\\":\\"(?P<description>(?:[^"\\]|\\.)*?)\\",'
    r'\\"practiceArea\\":(?:null|\\"(?P<practice_area>(?:[^"\\]|\\.)*?)\\"),'
    r'\\"by\\":\\"(?P<by>(?:[^"\\]|\\.)*?)\\"\}'
)


def parse_builds(html: str) -> list[dict]:
    records = []
    for m in BUILD_RECORD_RE.finditer(html):
        records.append(
            {
                "id": m.group("id"),
                "title": json_unescape(m.group("title")),
                "description": json_unescape(m.group("description")),
                "practice_area": json_unescape(m.group("practice_area"))
                if m.group("practice_area")
                else None,
                "by": json_unescape(m.group("by")),
            }
        )
    return records


def rank(
    records: list[dict], query: str, text_fields: tuple[str, ...], limit: int
) -> list[dict]:
    terms = [t for t in re.findall(r"\w+", query.lower()) if t]
    scored = []
    for record in records:
        haystack = " ".join(str(record.get(f) or "") for f in text_fields).lower()
        score = sum(haystack.count(term) for term in terms)
        if score:
            scored.append((score, record))
    scored.sort(key=lambda pair: pair[0], reverse=True)
    return [record for _, record in scored[:limit]]


def cmd_search_builds(args) -> dict:
    if args.fixture_html:
        html = Path(args.fixture_html).read_text(encoding="utf-8", errors="replace")
    else:
        status, body, _ = http_get(BUILDS_URL, accept="text/html")
        if status != 200:
            return fail("http_error", status=status)
        if bot_challenge(body):
            return fail("bot_challenge")
        html = body.decode("utf-8", errors="replace")

    records = parse_builds(html)
    if not records:
        return fail("no_records_parsed", source=BUILDS_URL)
    matches = rank(records, args.query, ("title", "description"), args.limit)
    return ok(source=BUILDS_URL, total_records_parsed=len(records), matches=matches)


# --- resolve-member ---------------------------------------------------------

COMMUNITY_URL = "https://www.legalquants.com/community"
MEMBER_HEAD_RE = re.compile(
    r'\{\\"slug\\":\\"(?P<slug>(?:[^"\\]|\\.)*?)\\",\\"name\\":\\"(?P<name>(?:[^"\\]|\\.)*?)\\",'
)
FEATURED_WORK_RE = re.compile(
    r'\\"featuredWork\\":(?:null|\{'
    r'\\"title\\":\\"(?P<title>(?:[^"\\]|\\.)*?)\\",'
    r'\\"url\\":(?:null|\\"(?P<url>(?:[^"\\]|\\.)*?)\\")'
    r")"  # closes the featuredWork-object alternative; its own \} is not required
)


def parse_members(html: str) -> list[dict]:
    members = []
    for m in MEMBER_HEAD_RE.finditer(html):
        window = html[m.end() : m.end() + 1500]
        featured = None
        fw = FEATURED_WORK_RE.search(window)
        if fw and fw.group("title"):
            featured = {
                "title": json_unescape(fw.group("title")),
                "url": json_unescape(fw.group("url")) if fw.group("url") else None,
            }
        members.append(
            {
                "slug": json_unescape(m.group("slug")),
                "name": json_unescape(m.group("name")),
                "featured_work": featured,
            }
        )
    return members


def cmd_resolve_member(args) -> dict:
    if args.fixture_html:
        html = Path(args.fixture_html).read_text(encoding="utf-8", errors="replace")
    else:
        status, body, _ = http_get(COMMUNITY_URL, accept="text/html")
        if status != 200:
            return fail("http_error", status=status)
        if bot_challenge(body):
            return fail("bot_challenge")
        html = body.decode("utf-8", errors="replace")

    members = parse_members(html)
    if not members:
        return fail("no_records_parsed", source=COMMUNITY_URL)

    target = args.name.strip().lower()
    matches = [m for m in members if m["name"].strip().lower() == target]
    if not matches:
        return fail("not_found", name=args.name)
    if len(matches) > 1:
        return fail(
            "ambiguous", name=args.name, candidates=[m["slug"] for m in matches]
        )

    member = matches[0]
    return ok(
        slug=member["slug"],
        name=member["name"],
        profile_url=f"https://www.legalquants.com/profile/{member['slug']}",
        featured_work=member["featured_work"],
    )


# --- CLI --------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_code = sub.add_parser("code")
    p_code.add_argument("--repo", required=True)
    p_code.add_argument("--path", required=True)
    p_code.add_argument("--ref")
    p_code.add_argument("--start-line", type=int)
    p_code.add_argument("--end-line", type=int)
    p_code.add_argument(
        "--fixture-raw", help="local file standing in for the fetched raw content"
    )

    p_page = sub.add_parser("page")
    p_page.add_argument("--url")
    p_page.add_argument("--max-chars", type=int)
    p_page.add_argument(
        "--fixture-html", help="local file standing in for the fetched page"
    )

    p_search = sub.add_parser("search-builds")
    p_search.add_argument("query")
    p_search.add_argument("--limit", type=int, default=5)
    p_search.add_argument(
        "--fixture-html", help="local file standing in for legalquants.com/builds"
    )

    p_resolve = sub.add_parser("resolve-member")
    p_resolve.add_argument("name")
    p_resolve.add_argument(
        "--fixture-html", help="local file standing in for legalquants.com/community"
    )

    args = parser.parse_args()
    handler = {
        "code": cmd_code,
        "page": cmd_page,
        "search-builds": cmd_search_builds,
        "resolve-member": cmd_resolve_member,
    }[args.cmd]
    print(json.dumps(handler(args)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
