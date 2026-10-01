#!/usr/bin/env python3
"""NZ AI policy public-source CLI.

Read-only stdlib helper for official New Zealand public-sector AI policy,
guidance, privacy, algorithm-governance, and national strategy sources.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import html
import json
import re
import pathlib
import sys
import textwrap
from dataclasses import dataclass, asdict
from typing import Any

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "lib"))
import nzfetch  # noqa: E402

UA = "nz-ai-policy-skill/1.0 (+https://github.com/thecolab-ai/.skills)"
DEFAULT_TIMEOUT = 15
DISCLAIMER = (
    "Not legal advice. New Zealand AI policy and guidance changes over time; "
    "check the cited official source and date before relying on it."
)


@dataclass(frozen=True)
class Source:
    id: str
    title: str
    agency: str
    category: str
    url: str
    kind: str = "html"
    status_note: str = "Official public source."
    guidance_type: str = "guidance"
    applicability: str = "Check source scope."
    key_terms: tuple[str, ...] = ()


SOURCES: tuple[Source, ...] = (
    Source(
        "digital-ai-framework",
        "Public Service Artificial Intelligence Framework",
        "Department of Internal Affairs / Digital Public Service",
        "public-service-framework",
        "https://www.digital.govt.nz/standards-and-guidance/technology-and-architecture/artificial-intelligence/public-service-artificial-intelligence-framework",
        status_note="Digital.govt.nz official framework page. Direct HTTP may return bot-protection rather than content.",
        guidance_type="public-sector framework",
        applicability="Public Service organisations; verify exact scope on the page.",
        key_terms=("framework", "public service", "human oversight", "risk", "governance"),
    ),
    Source(
        "digital-gcdo-role",
        "Government Chief Digital Officer role in AI",
        "Department of Internal Affairs / Government Chief Digital Officer",
        "public-service-framework",
        "https://www.digital.govt.nz/standards-and-guidance/technology-and-architecture/artificial-intelligence/gcdo-role",
        status_note="Digital.govt.nz official GCDO role page. Direct HTTP may return bot-protection rather than content.",
        guidance_type="role statement",
        applicability="Central government digital leadership context; verify scope on source.",
        key_terms=("GCDO", "system leadership", "digital", "AI work programme"),
    ),
    Source(
        "digital-responsible-ai-overview",
        "Responsible AI Guidance for the Public Service: overview",
        "Department of Internal Affairs / Digital Public Service",
        "responsible-ai-guidance",
        "https://www.digital.govt.nz/standards-and-guidance/technology-and-architecture/artificial-intelligence/responsible-ai-guidance-for-the-public-service-genai/overview",
        status_note="Digital.govt.nz responsible AI guidance overview. Direct HTTP may return bot-protection rather than content.",
        applicability="Public Service generative AI guidance; do not assume wider binding effect without checking.",
        key_terms=("responsible AI", "generative AI", "overview", "public service"),
    ),
    Source("digital-governance", "Responsible AI Guidance: governance", "Department of Internal Affairs / Digital Public Service", "genai-foundations", "https://www.digital.govt.nz/standards-and-guidance/technology-and-architecture/artificial-intelligence/responsible-ai-guidance-for-the-public-service-genai/genai-foundations/governance", status_note="Direct HTTP may return bot-protection rather than content.", applicability="Public Service GenAI foundation guidance.", key_terms=("governance", "risk", "accountability", "oversight")),
    Source("digital-security", "Responsible AI Guidance: security", "Department of Internal Affairs / Digital Public Service", "genai-foundations", "https://www.digital.govt.nz/standards-and-guidance/technology-and-architecture/artificial-intelligence/responsible-ai-guidance-for-the-public-service-genai/genai-foundations/security", status_note="Direct HTTP may return bot-protection rather than content.", applicability="Public Service GenAI foundation guidance.", key_terms=("security", "cyber", "information security", "data protection")),
    Source("digital-procurement", "Responsible AI Guidance: procurement", "Department of Internal Affairs / Digital Public Service", "genai-foundations", "https://www.digital.govt.nz/standards-and-guidance/technology-and-architecture/artificial-intelligence/responsible-ai-guidance-for-the-public-service-genai/genai-foundations/procurement", status_note="Direct HTTP may return bot-protection rather than content.", applicability="Public Service GenAI procurement guidance; pair with NZ Government Procurement rules where relevant.", key_terms=("procurement", "supplier", "contract", "vendor", "assurance")),
    Source("digital-accountability", "Responsible AI Guidance: accountability and responsibility", "Department of Internal Affairs / Digital Public Service", "genai-foundations", "https://www.digital.govt.nz/standards-and-guidance/technology-and-architecture/artificial-intelligence/responsible-ai-guidance-for-the-public-service-genai/genai-foundations/accountability-responsibility", status_note="Direct HTTP may return bot-protection rather than content.", applicability="Public Service GenAI foundation guidance.", key_terms=("accountability", "responsibility", "human oversight", "decision")),
    Source("digital-transparency", "Responsible AI Guidance: transparency", "Department of Internal Affairs / Digital Public Service", "customer-experience", "https://www.digital.govt.nz/standards-and-guidance/technology-and-architecture/artificial-intelligence/responsible-ai-guidance-for-the-public-service-genai/customer-experience/transparency", status_note="Direct HTTP may return bot-protection rather than content.", applicability="Public Service GenAI customer-experience guidance.", key_terms=("transparency", "disclosure", "explain", "customer")),
    Source("digital-privacy", "Responsible AI Guidance: privacy", "Department of Internal Affairs / Digital Public Service", "customer-experience", "https://www.digital.govt.nz/standards-and-guidance/technology-and-architecture/artificial-intelligence/responsible-ai-guidance-for-the-public-service-genai/customer-experience/privacy", status_note="Direct HTTP may return bot-protection rather than content.", applicability="Public Service GenAI customer-experience guidance; pair with Privacy Act and OPC guidance.", key_terms=("privacy", "personal information", "PIA", "customer")),
    Source("digital-bias", "Responsible AI Guidance: bias and discrimination", "Department of Internal Affairs / Digital Public Service", "customer-experience", "https://www.digital.govt.nz/standards-and-guidance/technology-and-architecture/artificial-intelligence/responsible-ai-guidance-for-the-public-service-genai/customer-experience/bias-and-discrimination", status_note="Direct HTTP may return bot-protection rather than content.", applicability="Public Service GenAI customer-experience guidance.", key_terms=("bias", "fairness", "discrimination", "equity")),
    Source("digital-communities", "Responsible AI Guidance: Māori, Pacific and ethnic communities", "Department of Internal Affairs / Digital Public Service", "customer-experience", "https://www.digital.govt.nz/standards-and-guidance/technology-and-architecture/artificial-intelligence/responsible-ai-guidance-for-the-public-service-genai/customer-experience/maori-pacific-and-ethnic-communities", status_note="Direct HTTP may return bot-protection rather than content.", applicability="Public Service GenAI customer-experience guidance; check source for Treaty, Māori data, Pacific and ethnic community framing.", key_terms=("Māori", "Maori", "Pacific", "ethnic communities", "Te Tiriti", "equity")),
    Source("digital-work-programme", "Public Service AI Work Programme", "Department of Internal Affairs / Digital Public Service", "work-programme", "https://www.digital.govt.nz/standards-and-guidance/technology-and-architecture/artificial-intelligence/public-service-ai-work-programme", status_note="Direct HTTP may return bot-protection rather than content.", guidance_type="work programme", applicability="Public Service AI system work programme context.", key_terms=("work programme", "public service", "system", "capability")),
    Source("digital-toolkit", "Public Service AI Toolkit: about the AI Toolkit", "Department of Internal Affairs / Digital Public Service", "toolkit", "https://www.digital.govt.nz/standards-and-guidance/technology-and-architecture/artificial-intelligence/public-service-ai-toolkit/about-the-ai-toolkit", status_note="Direct HTTP may return bot-protection rather than content.", guidance_type="toolkit", applicability="Public Service AI toolkit material.", key_terms=("toolkit", "templates", "public service", "policy")),
    Source("digital-policy-template", "Use of Artificial Intelligence policy template", "Department of Internal Affairs / Digital Public Service", "toolkit", "https://www.digital.govt.nz/standards-and-guidance/technology-and-architecture/artificial-intelligence/public-service-ai-toolkit/use-of-artificial-intelligence-policy-template", status_note="Direct HTTP may return bot-protection rather than content.", guidance_type="template", applicability="Agency AI policy template for public-service use; adapt, do not treat as legal advice.", key_terms=("policy template", "agency policy", "acceptable use", "GenAI")),
    Source("digital-records", "Records management for AI", "Department of Internal Affairs / Digital Public Service", "toolkit", "https://www.digital.govt.nz/standards-and-guidance/technology-and-architecture/artificial-intelligence/public-service-ai-toolkit/records-managements-for-ai", status_note="Direct HTTP may return bot-protection rather than content.", guidance_type="records guidance", applicability="Public Service toolkit material; pair with Archives NZ/public records requirements where relevant.", key_terms=("records", "recordkeeping", "information management", "audit trail")),
    Source("data-algorithm-charter", "Algorithm Charter for Aotearoa New Zealand", "Stats NZ / data.govt.nz", "algorithm-governance", "https://data.govt.nz/toolkit/data-ethics/government-algorithm-transparency-and-accountability/algorithm-charter", status_note="Data.govt.nz official Algorithm Charter page. Direct HTTP may return bot-protection rather than content.", guidance_type="charter", applicability="Government agencies that have signed/adopted the Algorithm Charter; check agency status and charter scope.", key_terms=("Algorithm Charter", "algorithm", "transparency", "accountability", "human oversight")),
    Source("data-aia-guide", "Algorithm Impact Assessment user guide", "Stats NZ / data.govt.nz", "algorithm-governance", "https://data.govt.nz/docs/algorithm-impact-assessment-user-guide", status_note="Data.govt.nz official AIA guide. Direct HTTP may return bot-protection rather than content.", guidance_type="assessment guide", applicability="Algorithm impact assessment support; check if mandated by the relevant agency/process.", key_terms=("Algorithm Impact Assessment", "AIA", "impact assessment", "risk", "algorithm")),
    Source("privacy-ai", "Artificial intelligence and privacy", "Office of the Privacy Commissioner", "privacy", "https://www.privacy.org.nz/resources-and-learning/a-z-topics/ai/", guidance_type="regulator guidance", applicability="Privacy Act 2020 and OPC guidance context; relevant beyond central government where privacy law applies.", key_terms=("privacy", "Privacy Act", "personal information", "AI", "generative AI")),
    Source("mbie-ai-strategy", "Artificial Intelligence Strategy and business guidance now available", "Ministry of Business, Innovation and Employment", "national-strategy", "https://www.mbie.govt.nz/about/news/artificial-intelligence-strategy-and-business-guidance-now-available", guidance_type="strategy announcement", applicability="National AI Strategy/business guidance context; not itself a public-service operational control.", key_terms=("strategy", "business guidance", "AI", "investment")),
    Source("mbie-regulatory-posture", "Addressing barriers to AI uptake in New Zealand", "Ministry of Business, Innovation and Employment", "national-strategy", "https://www.mbie.govt.nz/business-and-employment/economic-growth/digital-policy/new-zealands-ai-strategy-investing-with-confidence/addressing-barriers-to-ai-uptake-in-new-zealand", guidance_type="policy/regulatory posture", applicability="National AI uptake and regulatory posture context; distinguish from binding law.", key_terms=("regulatory", "AI uptake", "barriers", "confidence", "investment")),
    Source("psc-oia-ai-policy", "OIA 2025-0123 information request regarding government's use of AI", "Public Service Commission", "official-information", "https://www.publicservice.govt.nz/assets/DirectoryFile/OIA-2025-0123-Information-request-regarding-the-governments-use-of-artificial-intelligence-AI.pdf", kind="pdf", guidance_type="OIA release PDF", applicability="PSC released document; use as evidence of disclosed policy/material, not as a whole-of-government rule unless the PDF says so.", key_terms=("OIA", "Public Service Commission", "AI policy", "government use")),
)

SOURCE_BY_ID = {s.id: s for s in SOURCES}

BRIEFINGS: dict[str, dict[str, Any]] = {
    "public-sector": {
        "title": "NZ public-sector AI guidance briefing",
        "sources": ["digital-ai-framework", "digital-gcdo-role", "digital-responsible-ai-overview", "digital-work-programme", "digital-toolkit", "psc-oia-ai-policy"],
        "points": [
            "Start with the official Digital Public Service AI Framework and Responsible AI Guidance; treat them as public-service guidance whose current wording and scope should be checked at source.",
            "Separate governance foundations (governance, security, procurement, accountability) from customer-experience topics (transparency, privacy, bias, Māori/Pacific/ethnic communities).",
            "Use the Public Service AI Toolkit and policy template for agency-level operating controls, but adapt to the organisation's statutory role, risk profile, information holdings, and procurement settings.",
            "Avoid overclaiming: applicability may differ for local government, Crown entities, schools, health organisations, council-controlled organisations, or vendors.",
        ],
    },
    "procurement": {
        "title": "AI procurement briefing",
        "sources": ["digital-procurement", "digital-security", "digital-accountability", "digital-privacy", "mbie-regulatory-posture"],
        "points": [
            "For AI procurement, cite Digital.govt.nz procurement guidance alongside security, accountability, and privacy guidance rather than treating procurement as only a commercial exercise.",
            "Ask suppliers for model/data provenance, privacy and security controls, human oversight options, logging/audit support, incident processes, and change-management commitments.",
            "Distinguish vendor claims from agency accountability: public-sector organisations generally remain responsible for how AI-supported services are used and explained.",
        ],
    },
    "privacy": {
        "title": "AI privacy briefing",
        "sources": ["privacy-ai", "digital-privacy", "digital-transparency", "digital-accountability"],
        "points": [
            "Use the Office of the Privacy Commissioner AI page as the regulator source for privacy framing, and pair it with Digital.govt public-service privacy guidance for agency practice.",
            "Before using personal information with AI, check purpose, necessity, transparency, collection/use/disclosure authority, retention, security, human review, and whether a privacy impact assessment is needed.",
            "Generative AI use should avoid entering sensitive or personal information into tools unless the organisation has approved the tool and assessed privacy/security controls.",
        ],
    },
    "algorithm-charter": {
        "title": "Algorithm governance briefing",
        "sources": ["data-algorithm-charter", "data-aia-guide", "digital-bias", "digital-transparency", "digital-accountability"],
        "points": [
            "For algorithmic decision support, use the Algorithm Charter and Algorithm Impact Assessment guide as core source-map items, then add AI-specific public-service guidance where generative AI or AI systems are involved.",
            "Focus on transparency, human oversight, fairness/bias, explainability, monitoring, and clear accountability for decisions affecting people or groups.",
            "Check whether the agency has signed/adopted the Algorithm Charter and whether the relevant system is within the charter or AIA guide scope.",
        ],
    },
}

CHECKLISTS: dict[str, dict[str, Any]] = {
    "agency-genai-policy": {
        "title": "Agency generative-AI policy checklist",
        "sources": [
            "digital-policy-template", "digital-governance", "digital-security", "digital-procurement",
            "digital-accountability", "digital-transparency", "digital-privacy", "digital-bias",
            "digital-communities", "digital-records", "privacy-ai", "data-algorithm-charter",
        ],
        "items": [
            "Define approved, restricted, and prohibited AI use cases, including treatment of personal, confidential, legally privileged, commercially sensitive, and classified information.",
            "Assign named governance/accountability roles for AI approval, risk acceptance, incidents, monitoring, and review.",
            "Require human oversight for consequential decisions and state when AI output must not be used as the sole basis for action.",
            "Set privacy checks: lawful purpose, minimisation, transparency, PIA triggers, retention/deletion, and controls for personal information entered into AI tools.",
            "Set security checks: approved tools, data residency/hosting where relevant, access control, logging, supplier security assurance, and incident response.",
            "Set procurement/supplier requirements for AI functionality, data/model use, auditability, IP, confidentiality, change notices, performance, bias testing, and exit/portability.",
            "Address transparency: when people are told AI is being used, what can be explained, and how complaints or review requests are handled.",
            "Address bias, discrimination, Māori data interests, Pacific and ethnic community impacts, accessibility, and inclusive testing before deployment.",
            "Set records-management expectations for prompts, outputs, approvals, model/system versions, decisions, and audit trails.",
            "Schedule periodic review because AI capability, vendor terms, law, and government guidance are changing quickly.",
        ],
    }
}


def die(message: str, code: int = 1) -> None:
    print(f"nz-ai-policy: {message}", file=sys.stderr)
    raise SystemExit(code)


def now_utc() -> str:
    return _dt.datetime.now(_dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def output(data: Any, as_json: bool) -> None:
    if as_json:
        print(json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True))
    else:
        print_human(data)


def strip_html(text: str) -> str:
    text = re.sub(r"(?is)<(script|style|noscript|svg).*?</\1>", " ", text)
    text = re.sub(r"(?is)<!--.*?-->", " ", text)
    text = re.sub(r"(?is)<br\s*/?>", "\n", text)
    text = re.sub(r"(?is)</(p|div|li|h[1-6]|tr|section|article|main|header|footer)>", "\n", text)
    text = re.sub(r"(?is)<[^>]+>", " ", text)
    text = html.unescape(text)
    text = re.sub(r"[ \t\r\f\v]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n", text)
    return text.strip()


def is_blocked_html(text: str) -> bool:
    lower = text.lower()
    return (
        "incapsula" in lower
        or "request unsuccessful" in lower
        or "noindex,nofollow" in lower and "/_incap" in lower
        or "access denied" in lower and len(strip_html(text)) < 1000
    )


def fetch_source(source: Source, timeout: int = DEFAULT_TIMEOUT, max_chars: int = 4000) -> dict[str, Any]:
    fetched_at = now_utc()
    try:
        body, content_type, final_url = nzfetch.fetch_bytes(
            source.url,
            timeout=timeout,
            accept="text/html,application/pdf,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        )
    except nzfetch.Blocked as e:
        return {"id": source.id, "title": source.title, "url": source.url, "fetched_at": fetched_at, "ok": False, "blocked": True, "error": "source_blocked_plain_http", "detail": f"The official site returned bot-protection or access-control HTML. {e}", "source": source_record(source)}
    except nzfetch.FetchError as e:
        return {"id": source.id, "title": source.title, "url": source.url, "fetched_at": fetched_at, "ok": False, "error": "network_error", "detail": str(e), "source": source_record(source)}
    except TimeoutError:
        return {"id": source.id, "title": source.title, "url": source.url, "fetched_at": fetched_at, "ok": False, "error": "timeout", "source": source_record(source)}

    if source.kind == "pdf" or "application/pdf" in content_type.lower():
        blob = body[:4096]
        return {
            "id": source.id,
            "title": source.title,
            "url": source.url,
            "final_url": final_url,
            "fetched_at": fetched_at,
            "ok": True,
            "kind": "pdf",
            "content_type": content_type,
            "metadata_only": True,
            "bytes_previewed": len(blob),
            "note": "PDF reached; stdlib skill reports metadata only and does not extract full PDF text.",
            "source": source_record(source),
        }
    raw = body[:max(max_chars * 8, 12000)].decode("utf-8", "replace")

    if is_blocked_html(raw):
        return {
            "id": source.id,
            "title": source.title,
            "url": source.url,
            "fetched_at": fetched_at,
            "ok": False,
            "blocked": True,
            "error": "source_blocked_plain_http",
            "detail": "The official site returned bot-protection or access-control HTML to plain urllib. Use the source URL in a browser or cite the source-map metadata only.",
            "source": source_record(source),
        }
    text = strip_html(raw)
    return {
        "id": source.id,
        "title": source.title,
        "url": source.url,
        "final_url": final_url,
        "fetched_at": fetched_at,
        "ok": True,
        "kind": "html",
        "content_type": content_type,
        "preview": text[:max_chars],
        "text_length_previewed": min(len(text), max_chars),
        "source": source_record(source),
    }


def source_record(source: Source) -> dict[str, Any]:
    data = asdict(source)
    data["key_terms"] = list(source.key_terms)
    return data


def command_sources(args: argparse.Namespace) -> None:
    rows = [source_record(s) for s in SOURCES]
    if args.category:
        rows = [r for r in rows if r["category"] == args.category]
    data = {"fetched_at": now_utc(), "count": len(rows), "sources": rows, "disclaimer": DISCLAIMER}
    output(data, args.json)


def command_fetch(args: argparse.Namespace) -> None:
    source = SOURCE_BY_ID.get(args.source)
    if not source:
        die(f"unknown source id {args.source!r}; run sources for valid ids")
    assert source is not None
    output(fetch_source(source, timeout=args.timeout, max_chars=args.max_chars), args.json)


def snippets(text: str, query: str, limit: int) -> list[str]:
    terms = [t.lower() for t in re.findall(r"[\wāēīōūĀĒĪŌŪ-]+", query) if len(t) > 1]
    if not terms:
        return []
    clean = re.sub(r"\s+", " ", text)
    lower = clean.lower()
    hits: list[tuple[int, str]] = []
    for term in terms:
        start = 0
        while len(hits) < limit * max(2, len(terms)):
            idx = lower.find(term, start)
            if idx < 0:
                break
            lo = max(0, idx - 160)
            hi = min(len(clean), idx + 260)
            hits.append((idx, clean[lo:hi].strip()))
            start = idx + len(term)
            break
    dedup: list[str] = []
    seen = set()
    for _, s in sorted(hits):
        key = s[:120]
        if key not in seen:
            seen.add(key)
            dedup.append(s)
        if len(dedup) >= limit:
            break
    return dedup


def static_corpus(source: Source) -> str:
    return " ".join([
        source.id, source.title, source.agency, source.category, source.guidance_type,
        source.applicability, source.status_note, " ".join(source.key_terms), source.url,
    ])


def command_search(args: argparse.Namespace) -> None:
    terms = [t.lower() for t in re.findall(r"[\wāēīōūĀĒĪŌŪ-]+", args.query) if len(t) > 1]
    results: list[dict[str, Any]] = []
    for source in SOURCES:
        hay = static_corpus(source).lower()
        score = sum(1 for t in terms if t in hay)
        live = None
        live_snippets: list[str] = []
        if args.live:
            live = fetch_source(source, timeout=args.timeout, max_chars=12000)
            if live.get("ok") and live.get("preview"):
                live_snippets = snippets(live["preview"], args.query, args.snippets)
                if live_snippets:
                    score += 5 + len(live_snippets)
        if score:
            results.append({
                "source": source_record(source),
                "score": score,
                "static_match": any(t in hay for t in terms),
                "snippets": live_snippets or snippets(static_corpus(source), args.query, args.snippets),
                "live_status": None if live is None else {k: live.get(k) for k in ("ok", "blocked", "error", "fetched_at") if k in live},
            })
    results.sort(key=lambda r: (-r["score"], r["source"]["id"]))
    data = {"query": args.query, "searched_at": now_utc(), "live": args.live, "count": min(len(results), args.limit), "results": results[: args.limit], "disclaimer": DISCLAIMER}
    output(data, args.json)


def cited_sources(ids: list[str]) -> list[dict[str, str]]:
    rows = []
    for sid in ids:
        s = SOURCE_BY_ID[sid]
        rows.append({"id": s.id, "title": s.title, "agency": s.agency, "url": s.url, "guidance_type": s.guidance_type, "applicability": s.applicability})
    return rows


def command_briefing(args: argparse.Namespace) -> None:
    item = BRIEFINGS.get(args.topic)
    if not item:
        die(f"unknown briefing {args.topic!r}; choose one of: {', '.join(sorted(BRIEFINGS))}")
    assert item is not None
    data = {"topic": args.topic, "title": item["title"], "generated_at": now_utc(), "points": item["points"], "sources": cited_sources(item["sources"]), "disclaimer": DISCLAIMER}
    output(data, args.json)


def command_checklist(args: argparse.Namespace) -> None:
    item = CHECKLISTS.get(args.name)
    if not item:
        die(f"unknown checklist {args.name!r}; choose one of: {', '.join(sorted(CHECKLISTS))}")
    assert item is not None
    data = {"checklist": args.name, "title": item["title"], "generated_at": now_utc(), "items": item["items"], "sources": cited_sources(item["sources"]), "disclaimer": DISCLAIMER}
    output(data, args.json)


def print_human(data: Any) -> None:
    if isinstance(data, dict) and "sources" in data and "points" in data:
        print(data["title"])
        print(DISCLAIMER)
        print()
        for i, point in enumerate(data["points"], 1):
            print(f"{i}. {point}")
        print("\nSources:")
        for s in data["sources"]:
            print(f"- [{s['id']}] {s['title']} — {s['url']}")
        return
    if isinstance(data, dict) and "items" in data:
        print(data["title"])
        print(DISCLAIMER)
        print()
        for i, item in enumerate(data["items"], 1):
            print(f"{i}. {item}")
        print("\nSources:")
        for s in data["sources"]:
            print(f"- [{s['id']}] {s['title']} — {s['url']}")
        return
    if isinstance(data, dict) and "sources" in data:
        print(f"{data['count']} official NZ AI policy/guidance sources")
        for s in data["sources"]:
            print(f"- {s['id']}: {s['title']} ({s['agency']}; {s['category']})")
            print(f"  {s['url']}")
        print(f"\n{DISCLAIMER}")
        return
    if isinstance(data, dict) and "preview" in data:
        print(f"{data['title']}\n{data['url']}\nFetched: {data['fetched_at']}\n")
        print(textwrap.shorten(data["preview"], width=1800, placeholder=" ..."))
        return
    if isinstance(data, dict) and data.get("metadata_only"):
        print(f"{data['title']}\n{data['url']}\nFetched: {data['fetched_at']}\n{data['note']}")
        return
    if isinstance(data, dict) and data.get("ok") is False:
        print(f"{data.get('title', 'Source')}\n{data.get('url', '')}\nStatus: {data.get('error')} {data.get('detail', '')}")
        return
    if isinstance(data, dict) and "results" in data:
        print(f"Search: {data['query']} ({data['count']} results)")
        for r in data["results"]:
            s = r["source"]
            print(f"- {s['id']}: {s['title']} — {s['url']}")
            for snip in r.get("snippets", []):
                print(f"  … {snip} …")
        print(f"\n{DISCLAIMER}")
        return
    print(json.dumps(data, indent=2, ensure_ascii=False))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Official NZ AI policy/guidance source-map and briefing CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("sources", help="list and categorise official sources")
    p.add_argument("--category", help="filter by category")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=command_sources)

    p = sub.add_parser("fetch", help="fetch/source-preview one official page or PDF metadata")
    p.add_argument("source", help="source id from sources")
    p.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    p.add_argument("--max-chars", type=int, default=4000)
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=command_fetch)

    p = sub.add_parser("search", help="search source map and optionally fetched official text snippets")
    p.add_argument("query")
    p.add_argument("--limit", type=int, default=8)
    p.add_argument("--snippets", type=int, default=2)
    p.add_argument("--live", action="store_true", help="attempt live fetches; blocked sources are reported gracefully")
    p.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=command_search)

    p = sub.add_parser("briefing", help="generate a concise cited briefing")
    p.add_argument("topic", choices=sorted(BRIEFINGS))
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=command_briefing)

    p = sub.add_parser("checklist", help="generate a source-backed checklist")
    p.add_argument("name", choices=sorted(CHECKLISTS))
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=command_checklist)
    return parser


def main(argv: list[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
