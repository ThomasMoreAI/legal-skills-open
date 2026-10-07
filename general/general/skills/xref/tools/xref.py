#!/usr/bin/env python3
"""
Xref - Cross-reference and defined term resolver for legal documents.

Parses legal documents, identifies cross-references and defined terms,
and produces an interactive HTML viewer where every reference is hoverable/expandable.

Usage:
    python3 xref.py run --source <file> --output <file>
    python3 xref.py extract-structure --source <file>
    python3 xref.py find-references --source <file>
    python3 xref.py resolve-references --structure <json> --references <json>
    python3 xref.py fetch-external --citations <json>
    python3 xref.py build --source <file> --output <file> --resolved <json> --externals <json>
    python3 xref.py setup-check
"""

import argparse
import hashlib
import html
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

try:
    from docx import Document as DocxDocument
except ImportError:
    DocxDocument = None

try:
    import fitz
except ImportError:
    fitz = None

try:
    from bs4 import BeautifulSoup
except ImportError:
    BeautifulSoup = None

try:
    import requests
except ImportError:
    requests = None

try:
    from jinja2 import Template
except ImportError:
    Template = None

try:
    from statutes import (
        fetch_us_code, fetch_cfr, fetch_uk_legislation, fetch_eu_regulation,
        get_cache_key, get_cached, set_cached, FetchError
    )
except ImportError:
    fetch_us_code = None


SECTION_RE = re.compile(r'^((?:\d+\.)*\d+)(\.)?[ \t]+(.+)$')
SCHEDULE_RE = re.compile(r'^(Schedule|Exhibit|Annex)[ \t]+([A-Z]|\d+)[ \t]*(?:[-:.][ \t]*)?(.+)?$', re.IGNORECASE)
ARTICLE_RE = re.compile(r'^(Article)[ \t]+([IVXLCDM]+|\d+)[ \t]*(?:[-:.][ \t]*)?(.+)?$', re.IGNORECASE)
INTERNAL_REF_PATTERNS = [
    (re.compile(r'\b(Section|Clause)[ \t]+((?:\d+\.)*\d+(?:\([a-z]+\))?)', re.IGNORECASE), "numbered"),
    (re.compile(r'\bArticle[ \t]+([IVXLCDM]+|(?:\d+\.)*\d+)', re.IGNORECASE), "article"),
    (re.compile(r'\b(Schedule|Exhibit|Annex)[ \t]+([A-Z]|\d+)', re.IGNORECASE), "schedule"),
]
EXTERNAL_CITATION_PATTERNS = [
    (re.compile(r'\b(\d+)[ \t]+U\.?S\.?C\.?[ \t]+(?:Section[ \t]+|§[ \t]*)?(\d+[a-zA-Z0-9-]*)\b', re.IGNORECASE), "us_code"),
    (re.compile(r'\b(\d+)[ \t]+C\.?F\.?R\.?[ \t]+(?:Section[ \t]+)?(\d+)(?:\.(\d+))?\b', re.IGNORECASE), "cfr"),
    (re.compile(r'\b(GDPR)[ \t]+Article[ \t]+(\d+)\b', re.IGNORECASE), "eu_regulation"),
    (re.compile(r'\b([A-Z][A-Za-z \t]+Act)[ \t]+(\d{4})(?:,?[ \t]+(?:s\.|section)[ \t]*(\d+))?', re.IGNORECASE), "uk_legislation"),
]
ENTITY_SUFFIXES = {"Inc", "Inc.", "LLC", "L.L.C.", "Ltd", "Ltd.", "Corporation", "Corp", "Corp."}
DEFINED_TERM_IGNORE_WORDS = {
    "Agreement", "Article", "Section", "Schedule", "Exhibit", "Annex", "GDPR",
    "U.S.C", "C.F.R", "State", "California", "Delaware", "PowerShell"
}


def error(msg: str, exit_code: int = 1):
    """Print error message and exit."""
    print(f"Error: {msg}", file=sys.stderr)
    sys.exit(exit_code)


def check_core_deps():
    """Check for missing core dependencies."""
    missing = []
    if DocxDocument is None:
        missing.append("python-docx")
    if fitz is None:
        missing.append("pymupdf")
    if BeautifulSoup is None:
        missing.append("beautifulsoup4")
    if requests is None:
        missing.append("requests")
    if Template is None:
        missing.append("jinja2")

    if missing:
        error(f"Missing dependencies: {', '.join(missing)}\n" +
              "Run: bash setup.sh or pip install " + " ".join(missing))


def compute_file_hash(filepath: str) -> str:
    """Compute SHA-256 hash of a file."""
    h = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()


def make_anchor(section_id: str) -> str:
    slug = re.sub(r'[^A-Za-z0-9_.-]+', '-', section_id.strip()).strip('-').lower()
    return f"section-{slug}"


def normalize_key(value: str) -> str:
    value = value.strip().rstrip(".,;:")
    value = re.sub(r'\s+', ' ', value)
    return value.lower()


def flatten_sections(sections: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    flat = []

    def visit(items):
        for item in items:
            flat.append(item)
            visit(item.get("children", []))

    visit(sections)
    return flat


def find_section_for_offset(sections: List[Dict[str, Any]], offset: int) -> Optional[str]:
    best = None
    for section in flatten_sections(sections):
        start = section.get("start")
        end = section.get("end")
        if start is None or end is None:
            continue
        if start <= offset < end:
            if best is None or section.get("level", 0) >= best.get("level", 0):
                best = section
    return best["id"] if best else None


def detect_section_heading(text: str, style_name: str = "") -> Optional[Dict[str, Any]]:
    style_level = None
    if style_name.startswith("Heading"):
        try:
            style_level = int(style_name.replace("Heading", "").strip())
        except ValueError:
            style_level = 1

    schedule_match = SCHEDULE_RE.match(text)
    if schedule_match:
        kind = schedule_match.group(1).title()
        label = schedule_match.group(2).upper()
        title = (schedule_match.group(3) or kind).strip()
        number = f"{kind} {label}"
        return {
            "id": number,
            "number": number,
            "title": title,
            "level": style_level or 1,
            "kind": kind.lower(),
            "lookup_keys": [number, f"{kind.lower()} {label.lower()}"],
        }

    article_match = ARTICLE_RE.match(text)
    if article_match:
        label = article_match.group(2).upper()
        title = (article_match.group(3) or "Article").strip()
        number = f"Article {label}"
        return {
            "id": number,
            "number": number,
            "title": title,
            "level": style_level or 1,
            "kind": "article",
            "lookup_keys": [number, label],
        }

    section_match = SECTION_RE.match(text)
    if section_match:
        number = section_match.group(1)
        trailing_dot = bool(section_match.group(2))
        title = section_match.group(3).strip()
        if style_level is None and trailing_dot and "." not in number and len(title.split()) > 3:
            return None
        return {
            "id": number,
            "number": number,
            "title": title,
            "level": number.count(".") + 1,
            "kind": "section",
            "lookup_keys": [number, f"Section {number}", f"Clause {number}"],
        }

    if style_level is not None:
        anchor_source = re.sub(r'[^A-Za-z0-9]+', '-', text).strip("-") or "heading"
        return {
            "id": anchor_source,
            "number": "",
            "title": text,
            "level": style_level,
            "kind": "heading",
            "lookup_keys": [text],
        }

    return None


def build_section_tree(flat_sections: List[Dict[str, Any]], document_length: int) -> List[Dict[str, Any]]:
    for idx, section in enumerate(flat_sections):
        end = document_length
        for later in flat_sections[idx + 1:]:
            if later["level"] <= section["level"]:
                end = max(section["start"], later["start"] - 1)
                break
        section["end"] = end

    roots = []
    stack = []
    for section in flat_sections:
        while stack and stack[-1]["level"] >= section["level"]:
            stack.pop()
        section["parent_id"] = stack[-1]["id"] if stack else None
        if stack:
            stack[-1]["children"].append(section)
        else:
            roots.append(section)
        stack.append(section)

    def finalize(section: Dict[str, Any]) -> str:
        body = "\n\n".join(section.pop("_body_lines", []))
        own_parts = [section["heading_text"]]
        if body:
            own_parts.append(body)
        own_text = "\n\n".join(own_parts).strip()
        child_text = "\n\n".join(finalize(child) for child in section.get("children", []))
        section["body"] = body
        section["own_text"] = own_text
        section["text"] = "\n\n".join(part for part in [own_text, child_text] if part).strip()
        return section["text"]

    for root in roots:
        finalize(root)

    return roots


def build_structure_from_paragraphs(
    paragraph_items: List[Dict[str, Any]],
    parser_confidence: Dict[str, Any],
    total_pages: Optional[int] = None,
) -> Dict[str, Any]:
    paragraphs = []
    flat_sections = []
    current_section = None
    offset = 0

    for item in paragraph_items:
        text = item["text"].strip()
        if not text:
            continue

        start = offset
        end = start + len(text)
        offset = end + 1

        heading = detect_section_heading(text, item.get("style_name", ""))
        if heading:
            section = {
                **heading,
                "page": item.get("page"),
                "start": start,
                "end": end,
                "heading_text": text,
                "anchor": make_anchor(heading["id"]),
                "children": [],
                "_body_lines": [],
            }
            flat_sections.append(section)
            current_section = section
            paragraphs.append({
                "type": "heading",
                "text": text,
                "section_id": section["id"],
                "anchor": section["anchor"],
                "level": section["level"],
                "start": start,
                "end": end,
                "page": item.get("page"),
            })
        else:
            if current_section is not None:
                current_section["_body_lines"].append(text)
            paragraphs.append({
                "type": "paragraph",
                "text": text,
                "section_id": current_section["id"] if current_section else None,
                "start": start,
                "end": end,
                "page": item.get("page"),
            })

    document_text = "\n".join(paragraph["text"] for paragraph in paragraphs)
    sections = build_section_tree(flat_sections, len(document_text))
    defined_terms = extract_defined_terms(document_text, sections)

    return {
        "sections": sections,
        "flat_sections": flatten_sections(sections),
        "paragraphs": paragraphs,
        "document_text": document_text,
        "defined_terms": defined_terms,
        "numbering_scheme": "decimal",
        "total_pages": total_pages,
        "parser_confidence": parser_confidence,
    }


# ============================================================================
# EXTRACT STRUCTURE
# ============================================================================

def extract_structure_docx(filepath: str) -> Dict[str, Any]:
    """Extract section structure and defined terms from a Word document."""
    if DocxDocument is None:
        error("python-docx is required for Word document parsing")

    doc = DocxDocument(filepath)
    paragraph_items = [
        {
            "text": para.text,
            "style_name": para.style.name if para.style else "",
            "page": None,
        }
        for para in doc.paragraphs
    ]

    return build_structure_from_paragraphs(
        paragraph_items,
        {"overall": "high", "uncertain_regions": []},
        total_pages=None,
    )


def extract_structure_pdf(filepath: str) -> Dict[str, Any]:
    """Extract section structure and defined terms from a PDF."""
    if fitz is None:
        error("pymupdf is required for PDF parsing")

    doc = fitz.open(filepath)
    paragraph_items = []
    for page_num, page in enumerate(doc, 1):
        for line in page.get_text("text").splitlines():
            text = line.strip()
            if text:
                paragraph_items.append({"text": text, "style_name": "", "page": page_num})

    return build_structure_from_paragraphs(
        paragraph_items,
        {
            "overall": "medium",
            "uncertain_regions": [
                {"description": "PDF parsing uses text-layout heuristics. Results may be less reliable than Word documents."}
            ],
        },
        total_pages=len(doc),
    )


def extract_structure(source: str) -> Dict[str, Any]:
    source_lower = source.lower()
    if source_lower.endswith(".docx"):
        return extract_structure_docx(source)
    if source_lower.endswith(".pdf"):
        return extract_structure_pdf(source)
    error("Unsupported file format. Use .docx or .pdf")


def add_defined_term(
    terms: List[Dict[str, Any]],
    seen: Set[Tuple[str, str]],
    text: str,
    sections: List[Dict[str, Any]],
    term: str,
    definition: str,
    match_start: int,
    match_end: int,
    scope: str = "global",
    defined_in: Optional[str] = None,
):
    clean_term = term.strip()
    clean_definition = re.sub(r'\s+', ' ', definition.strip())
    if len(clean_term) < 2 or len(clean_term) > 120 or not clean_definition:
        return

    key = (clean_term.lower(), scope)
    if key in seen:
        return

    term_id = f"term-{len(terms) + 1}"
    terms.append({
        "id": term_id,
        "term": clean_term,
        "definition": clean_definition,
        "defined_in": defined_in or find_section_for_offset(sections, match_start),
        "page": None,
        "scope": scope,
        "character_offset": match_start,
        "definition_span": [match_start, match_end],
    })
    seen.add(key)


def clean_parenthetical_definition(context: str) -> str:
    context = re.sub(r'\s+', ' ', context).strip(" ,.;")
    for splitter in [r'\bby and between\b', r'\band between\b', r'\),\s+and\b', r'\band\b']:
        parts = re.split(splitter, context, flags=re.IGNORECASE)
        if len(parts) > 1 and len(parts[-1].strip()) > 5:
            context = parts[-1].strip(" ,.;")
    return context[-180:] if len(context) > 180 else context


def extract_defined_terms(text: str, sections: List[Dict]) -> List[Dict[str, Any]]:
    """
    Extract defined terms from text.

    The extractor favors explicit legal drafting patterns and records offsets so
    the viewer can distinguish definitions from later uses.
    """
    terms = []
    seen: Set[Tuple[str, str]] = set()

    scoped_pattern = re.compile(
        r'For purposes of this (?:Section|Article|Clause)\s+([^,\s]+),\s+"([^"]+)"\s+means\s+(.+?\.)',
        re.IGNORECASE,
    )
    for match in scoped_pattern.finditer(text):
        section_ref = match.group(1)
        term = match.group(2)
        definition = match.group(3).strip()
        add_defined_term(
            terms, seen, text, sections, term, definition,
            match.start(), match.end(), scope=f"section:{section_ref}", defined_in=section_ref
        )

    explicit_pattern = re.compile(
        r'"([^"\n]{2,120})"\s+(?:means|shall mean|has the meaning)\s+(.+?\.)',
        re.IGNORECASE,
    )
    for match in explicit_pattern.finditer(text):
        add_defined_term(
            terms, seen, text, sections, match.group(1), match.group(2),
            match.start(), match.end(), scope="global"
        )

    parenthetical_pattern = re.compile(r'([^()\n]{3,220}?)\s*\((?:this\s+|the\s+)?"([A-Z][^"()]{1,80})"\)')
    for match in parenthetical_pattern.finditer(text):
        term = match.group(2).strip()
        if term.lower() in {existing["term"].lower() for existing in terms}:
            continue
        definition = clean_parenthetical_definition(match.group(1))
        add_defined_term(
            terms, seen, text, sections, term, definition,
            match.start(2), match.end(), scope="global"
        )

    return terms


# ============================================================================
# FIND REFERENCES
# ============================================================================

def ranges_overlap(a_start: int, a_end: int, b_start: int, b_end: int) -> bool:
    return a_start < b_end and b_start < a_end


def find_external_citations(text: str) -> List[Dict[str, Any]]:
    citations = []
    ref_id = 0

    for pattern, cit_type in EXTERNAL_CITATION_PATTERNS:
        for match in pattern.finditer(text):
            ref_id += 1
            base = {
                "id": f"ext-{ref_id}",
                "text": match.group(0),
                "citation_text": match.group(0),
                "citation_type": cit_type,
                "found_in_section": None,
                "page": None,
                "character_offset": match.start(),
                "end_offset": match.end(),
            }
            if cit_type == "us_code":
                base.update({"title": match.group(1), "section": match.group(2)})
            elif cit_type == "cfr":
                base.update({"title": match.group(1), "part": match.group(2), "section": match.group(3)})
            elif cit_type == "eu_regulation":
                base.update({"regulation": match.group(1).upper(), "article": match.group(2)})
            elif cit_type == "uk_legislation":
                base.update({"act_name": match.group(1), "year": match.group(2), "section": match.group(3)})
            citations.append(base)

    citations.sort(key=lambda c: c["character_offset"])
    return citations


def find_defined_term_usages(text: str, sections: List[Dict], defined_terms: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    usages = []
    usage_id = 0
    unique_terms = sorted({term["term"] for term in defined_terms}, key=len, reverse=True)
    definition_spans = {
        term["term"]: tuple(term.get("definition_span", [None, None]))
        for term in defined_terms
    }

    for term in unique_terms:
        pattern = re.compile(r'\b' + re.escape(term) + r'\b')
        for match in pattern.finditer(text):
            span = definition_spans.get(term)
            if span and span[0] is not None and ranges_overlap(match.start(), match.end(), span[0], span[1]):
                continue
            usage_id += 1
            usages.append({
                "id": f"term-use-{usage_id}",
                "term": term,
                "text": match.group(0),
                "found_in_section": find_section_for_offset(sections, match.start()),
                "character_offset": match.start(),
                "end_offset": match.end(),
            })

    usages.sort(key=lambda usage: usage["character_offset"])
    return usages


def should_ignore_defined_term_candidate(candidate: str, defined_names: Set[str]) -> bool:
    words = candidate.split()
    if len(words) < 2 or len(words) > 5:
        return True
    if candidate.upper() == candidate:
        return True
    if candidate.lower() in defined_names:
        return True
    if any(word.rstrip(".,") in ENTITY_SUFFIXES for word in words):
        return True
    if any(word.rstrip(".,") in DEFINED_TERM_IGNORE_WORDS for word in words):
        return True
    if words[-1].rstrip(".,") in {"Agreement", "Act", "Regulation", "Section", "Schedule"}:
        return True
    return False


def candidate_is_in_heading(candidate_start: int, sections: List[Dict[str, Any]]) -> bool:
    for section in flatten_sections(sections):
        heading_end = section.get("start", 0) + len(section.get("heading_text", ""))
        if section.get("start", 0) <= candidate_start < heading_end:
            return True
    return False


def find_potential_undefined_terms(
    text: str,
    sections: List[Dict],
    defined_terms: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    defined_names = {term["term"].lower() for term in defined_terms}
    candidates = []
    seen: Set[str] = set()
    pattern = re.compile(r'\b[A-Z][A-Za-z0-9&.-]*(?:[ \t]+[A-Z][A-Za-z0-9&.-]*){1,4}\b')

    for match in pattern.finditer(text):
        raw_candidate = match.group(0).strip(" ,.;:")
        leading_article = re.match(r'^(?:The|This|Such)[ \t]+', raw_candidate)
        start_offset = match.start() + (leading_article.end() if leading_article else 0)
        candidate = raw_candidate[leading_article.end():] if leading_article else raw_candidate
        key = candidate.lower()
        if (
            key in seen
            or candidate_is_in_heading(start_offset, sections)
            or should_ignore_defined_term_candidate(candidate, defined_names)
        ):
            continue
        seen.add(key)
        candidates.append({
            "id": f"undef-{len(candidates) + 1}",
            "text": candidate,
            "term": candidate,
            "found_in_section": find_section_for_offset(sections, start_offset),
            "character_offset": start_offset,
            "end_offset": match.end(),
            "context": text[max(0, start_offset - 50):match.end() + 50],
        })

    return candidates


def find_references(
    text: str,
    sections: List[Dict],
    defined_terms: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    """Find all cross-references, defined term usages, and external citations."""
    internal_refs = []
    external_citations = find_external_citations(text)
    external_spans = [(c["character_offset"], c["end_offset"]) for c in external_citations]
    ref_id = 0

    for pattern, ref_type in INTERNAL_REF_PATTERNS:
        for match in pattern.finditer(text):
            if any(ranges_overlap(match.start(), match.end(), start, end) for start, end in external_spans):
                continue
            ref_id += 1
            if ref_type == "schedule":
                target = f"{match.group(1).title()} {match.group(2).upper()}"
            elif ref_type == "article":
                target = f"Article {match.group(1).upper()}"
            else:
                target = match.group(2)
            internal_refs.append({
                "id": f"ref-{ref_id}",
                "text": match.group(0),
                "target_section": target,
                "reference_type": ref_type,
                "found_in_section": find_section_for_offset(sections, match.start()),
                "page": None,
                "character_offset": match.start(),
                "end_offset": match.end(),
                "context": text[max(0, match.start() - 50):match.end() + 50],
            })

    defined_terms = defined_terms or []
    return {
        "internal_references": sorted(internal_refs, key=lambda ref: ref["character_offset"]),
        "defined_term_usages": find_defined_term_usages(text, sections, defined_terms) if defined_terms else [],
        "external_citations": external_citations,
        "potential_undefined_terms": find_potential_undefined_terms(text, sections, defined_terms) if defined_terms else [],
        "unresolved": [],
    }


# ============================================================================
# RESOLVE REFERENCES
# ============================================================================

def build_section_index(sections: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    index = {}
    for section in flatten_sections(sections):
        keys = set(section.get("lookup_keys", []))
        keys.update({
            section.get("id", ""),
            section.get("number", ""),
            f"Section {section.get('number', '')}",
            f"Clause {section.get('number', '')}",
        })
        for key in keys:
            if key:
                index.setdefault(normalize_key(key), section)
    return index


def resolve_section_target(target: str, section_index: Dict[str, Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    target_key = normalize_key(target)
    if target_key in section_index:
        return section_index[target_key]

    compact_target = re.sub(r'\s+', '', target_key)
    for key, section in section_index.items():
        if re.sub(r'\s+', '', key) == compact_target:
            return section

    return None


def expand_defined_term_definitions(resolved: Dict[str, Any], section_index: Dict[str, Dict[str, Any]]):
    forward_ref = re.compile(
        r'has the meaning (?:set forth|given|assigned|specified|defined) in '
        r'(?:Section|Clause|Article)\s+((?:\d+\.)*\d+(?:\([a-z]+\))?)',
        re.IGNORECASE,
    )
    for term in resolved["defined_terms"]:
        definition = term.get("definition", "")
        match = forward_ref.search(definition)
        if match:
            target_id = match.group(1)
            target_sec = resolve_section_target(target_id, section_index)
            if target_sec and target_sec.get("text"):
                term["definition"] = target_sec["text"]
                term["resolved_from"] = f"Section {target_id}"

    term_defs = {term["term"]: term.get("definition", "") for term in resolved["defined_terms"]}
    terms_longest_first = sorted(term_defs.keys(), key=len, reverse=True)

    def expand_definition(definition: str, visited: Set[str]) -> str:
        for term in terms_longest_first:
            if term in visited:
                continue
            pattern = re.compile(r'\b' + re.escape(term) + r'\b')
            match = pattern.search(definition)
            if not match:
                continue
            prefix = definition[:match.start()]
            if prefix.count("(i.e.,") > prefix.count(")"):
                continue
            before = definition[max(0, match.start() - 1):match.start()]
            if before and before[-1].isalpha():
                continue
            preceding_ctx = definition[max(0, match.start() - 30):match.start()]
            if preceding_ctx and re.search(r'[A-Z]\w+[\s-]+$', preceding_ctx):
                if not re.search(r'\b(?:this|the)\s+$', preceding_ctx, re.IGNORECASE):
                    continue
            inner = term_defs.get(term, "")
            if not inner or inner == definition:
                continue
            expanded_inner = expand_definition(inner, visited | {term})
            if len(expanded_inner) > 200:
                expanded_inner = expanded_inner[:197] + "..."
            replacement = match.group(0) + " (i.e., " + expanded_inner + ")"
            definition = definition[:match.start()] + replacement + definition[match.end():]
        return definition

    for term in resolved["defined_terms"]:
        original = term.get("definition", "")
        expanded = expand_definition(original, {term["term"]})
        if expanded != original:
            term["definition_expanded"] = expanded


def resolve_references(structure: Dict, references: Dict) -> Dict[str, Any]:
    """Resolve all references to their targets."""
    sections = structure.get("sections", [])
    section_index = build_section_index(sections)

    resolved = {
        "sections": sections,
        "flat_sections": flatten_sections(sections),
        "paragraphs": structure.get("paragraphs", []),
        "document_text": structure.get("document_text", ""),
        "internal_references": [],
        "defined_terms": list(structure.get("defined_terms", [])),
        "defined_term_usages": references.get("defined_term_usages", []),
        "external_citations": references.get("external_citations", []),
        "unresolved": [],
        "circular_chains": [],
    }

    for ref in references.get("internal_references", []):
        target = resolve_section_target(ref["target_section"], section_index)
        if target:
            resolved["internal_references"].append({**ref, "resolved": True, "target": target})
        else:
            resolved["unresolved"].append({
                **ref,
                "unresolved_type": "broken_reference",
                "reason": f"No section {ref['target_section']} found in document",
            })

    for candidate in references.get("potential_undefined_terms", []):
        resolved["unresolved"].append({
            **candidate,
            "unresolved_type": "undefined_term",
            "reason": f"{candidate['text']} is capitalized like a defined term but no definition was found",
        })

    expand_defined_term_definitions(resolved, section_index)
    return resolved


# ============================================================================
# FETCH EXTERNAL
# ============================================================================

def fetch_external_citations(citations_json: str) -> List[Dict[str, Any]]:
    """Fetch external statutory references."""
    if fetch_us_code is None:
        error("Statute fetcher modules not available")

    citations = json.loads(citations_json)
    results = []

    for citation in citations:
        cit_type = citation.get("citation_type")
        cache_params = {k: v for k, v in citation.items() if k not in {"citation_type", "id", "character_offset", "end_offset", "context"}}
        cache_key = get_cache_key(cit_type, **cache_params)
        cached = get_cached(cache_key)

        if cached:
            merged = merge_external_fetch_result(citation, {**cached, "cached": True})
            results.append(merged)
            continue

        try:
            if cit_type == "us_code":
                result = fetch_us_code(citation["title"], citation["section"])
            elif cit_type == "cfr":
                result = fetch_cfr(citation["title"], citation["part"], citation.get("section"))
            elif cit_type == "uk_legislation":
                result = fetch_uk_legislation(citation["act_name"], citation["year"], citation.get("section"))
            elif cit_type == "eu_regulation":
                result = fetch_eu_regulation(citation["regulation"], citation["article"])
            else:
                result = {**citation, "fetched": False, "error": "Unsupported citation type"}

            if result.get("fetched"):
                set_cached(cache_key, result)

            results.append(merge_external_fetch_result(citation, result))
        except FetchError as exc:
            results.append({
                **citation,
                "citation_text": citation.get("citation_text", citation.get("text", "")),
                "statute_text": "",
                "fetched": False,
                "error": str(exc),
            })

    return results


def merge_external_fetch_result(citation: Dict[str, Any], result: Dict[str, Any]) -> Dict[str, Any]:
    statute_text = result.get("text", "")
    merged = {**citation, **result}
    merged["text"] = citation.get("text", citation.get("citation_text", ""))
    merged["citation_text"] = citation.get("citation_text", merged["text"])
    merged["statute_text"] = statute_text
    return merged


# ============================================================================
# BUILD HTML
# ============================================================================

def annotation_attrs(attrs: Dict[str, str]) -> str:
    return " ".join(f'{html.escape(key)}="{html.escape(str(value), quote=True)}"' for key, value in attrs.items())


def add_annotation(
    annotations: List[Dict[str, Any]],
    start: Optional[int],
    end: Optional[int],
    priority: int,
    class_name: str,
    attrs: Dict[str, str],
):
    if start is None or end is None or end <= start:
        return
    annotations.append({
        "start": start,
        "end": end,
        "priority": priority,
        "class_name": class_name,
        "attrs": attrs,
    })


def collect_annotations(resolved: Dict[str, Any], external_citations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    annotations = []

    for ext in external_citations:
        add_annotation(
            annotations,
            ext.get("character_offset"),
            ext.get("end_offset"),
            1,
            "external-citation",
            {"data-panel-id": f"panel-{ext['id']}", "data-citation-id": ext["id"]},
        )

    for ref in resolved.get("internal_references", []):
        add_annotation(
            annotations,
            ref.get("character_offset"),
            ref.get("end_offset"),
            2,
            "xref-link",
            {"data-panel-id": f"panel-{ref['id']}", "data-ref-id": ref["id"], "data-section": ref["target"]["id"]},
        )

    for item in resolved.get("unresolved", []):
        unresolved_type = item.get("unresolved_type")
        if unresolved_type not in {"broken_reference", "undefined_term", "external_document"}:
            continue
        css_class = {
            "broken_reference": "broken-reference",
            "undefined_term": "undefined-term",
            "external_document": "external-doc-ref",
        }[unresolved_type]
        add_annotation(
            annotations,
            item.get("character_offset"),
            item.get("end_offset"),
            3,
            css_class,
            {"data-panel-id": f"panel-{item['id']}", "data-unresolved-id": item["id"]},
        )

    for usage in resolved.get("defined_term_usages", []):
        add_annotation(
            annotations,
            usage.get("character_offset"),
            usage.get("end_offset"),
            4,
            "defined-term",
            {"data-panel-id": f"panel-term-{slug_for_panel(usage['term'])}", "data-term": usage["term"]},
        )

    selected = []
    current_end = -1
    for annotation in sorted(annotations, key=lambda a: (a["start"], a["priority"], -(a["end"] - a["start"]))):
        if annotation["start"] < current_end:
            continue
        selected.append(annotation)
        current_end = annotation["end"]
    return selected


def slug_for_panel(value: str) -> str:
    return re.sub(r'[^A-Za-z0-9_.-]+', '-', value.strip()).strip('-').lower()


def render_text_with_annotations(text: str, base_offset: int, annotations: List[Dict[str, Any]]) -> str:
    relevant = [
        annotation for annotation in annotations
        if annotation["start"] >= base_offset and annotation["end"] <= base_offset + len(text)
    ]
    relevant.sort(key=lambda annotation: annotation["start"])

    rendered = []
    cursor = 0
    for annotation in relevant:
        local_start = annotation["start"] - base_offset
        local_end = annotation["end"] - base_offset
        if local_start < cursor:
            continue
        rendered.append(html.escape(text[cursor:local_start]))
        attrs = {"class": annotation["class_name"], **annotation["attrs"]}
        rendered.append(f"<span {annotation_attrs(attrs)}>{html.escape(text[local_start:local_end])}</span>")
        cursor = local_end
    rendered.append(html.escape(text[cursor:]))
    return "".join(rendered)


def build_document_html(resolved: Dict[str, Any], external_citations: List[Dict[str, Any]]) -> str:
    annotations = collect_annotations(resolved, external_citations)
    rendered = []

    for paragraph in resolved.get("paragraphs", []):
        text = paragraph.get("text", "")
        if not text:
            continue
        body = render_text_with_annotations(text, paragraph["start"], annotations)
        if paragraph.get("type") == "heading":
            level = min(max(paragraph.get("level", 2) + 1, 2), 6)
            rendered.append(
                f'<h{level} id="{html.escape(paragraph["anchor"])}" '
                f'class="section-heading level-{paragraph.get("level", 1)}" '
                f'data-section="{html.escape(paragraph["section_id"])}">{body}</h{level}>'
            )
        else:
            attrs = {"class": "document-paragraph"}
            if paragraph.get("section_id"):
                attrs["data-section"] = paragraph["section_id"]
            rendered.append(f"<p {annotation_attrs(attrs)}>{body}</p>")

    return "\n".join(rendered)


def merge_external_citations(
    found_citations: List[Dict[str, Any]],
    fetched_citations: Optional[List[Dict[str, Any]]],
    compact: bool,
) -> List[Dict[str, Any]]:
    fetched_by_id = {item.get("id"): item for item in (fetched_citations or []) if item.get("id")}
    merged = []
    for citation in found_citations:
        item = {**citation, **fetched_by_id.get(citation["id"], {})}
        item.setdefault("citation_text", citation.get("citation_text", citation.get("text", "")))
        item.setdefault("statute_text", "")
        if not item.get("source_url"):
            item["source_url"] = official_source_url(item)
        if compact:
            item["statute_text"] = ""
        merged.append(item)
    return merged


def official_source_url(citation: Dict[str, Any]) -> Optional[str]:
    cit_type = citation.get("citation_type")
    if cit_type == "us_code" and citation.get("title") and citation.get("section"):
        return (
            "https://uscode.house.gov/view.xhtml?"
            f"req=granuleid:USC-prelim-title{citation['title']}-section{citation['section']}"
        )
    if cit_type == "cfr" and citation.get("title") and citation.get("part"):
        url = f"https://www.ecfr.gov/current/title-{citation['title']}/part-{citation['part']}"
        if citation.get("section"):
            url += f"#p-{citation['part']}.{citation['section']}"
        return url
    if cit_type == "eu_regulation":
        regulation = str(citation.get("regulation", "")).upper()
        article = citation.get("article")
        if article and regulation in {"GDPR", "2016/679"}:
            return f"https://gdpr-info.eu/art-{article}-gdpr/"
        if citation.get("regulation"):
            return f"https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:{citation['regulation']}"
    if cit_type == "uk_legislation":
        return "https://www.legislation.gov.uk/"
    return None


def build_html_from_resolved(
    source: str,
    output: str,
    resolved: Dict[str, Any],
    externals: Optional[List[Dict[str, Any]]] = None,
    title: str = None,
    compact: bool = False,
):
    """Build the interactive HTML viewer from an in-memory resolved graph."""
    if Template is None:
        error("jinja2 is required for HTML generation")

    external_citations = merge_external_citations(
        resolved.get("external_citations", []),
        externals,
        compact,
    )
    defined_terms = [
        {**term, "panel_id": f"panel-term-{slug_for_panel(term['term'])}"}
        for term in resolved.get("defined_terms", [])
    ]
    document_html = build_document_html(resolved, external_citations)
    file_hash = compute_file_hash(source)
    generated_at = datetime.now().astimezone().isoformat(timespec="seconds")

    template_path = os.path.join(os.path.dirname(__file__), "templates", "viewer.html")
    with open(template_path, 'r', encoding='utf-8') as f:
        template = Template(f.read())

    css_path = os.path.join(os.path.dirname(__file__), "templates", "styles.css")
    js_path = os.path.join(os.path.dirname(__file__), "templates", "viewer.js")
    with open(css_path, 'r', encoding='utf-8') as f:
        css = f.read()
    with open(js_path, 'r', encoding='utf-8') as f:
        js = f.read()

    html_output = template.render(
        title=title or os.path.basename(source),
        source_file=source,
        source_hash=file_hash,
        generated_at=generated_at,
        document_html=document_html,
        sections=resolved.get("sections", []),
        flat_sections=resolved.get("flat_sections", flatten_sections(resolved.get("sections", []))),
        internal_refs=resolved.get("internal_references", []),
        defined_terms=defined_terms,
        defined_term_usages=resolved.get("defined_term_usages", []),
        external_citations=external_citations,
        unresolved=resolved.get("unresolved", []),
        css=css,
        js=js,
        compact=compact,
    )

    output_path = Path(output).expanduser()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_output)

    print(f"Generated: {output_path}")


def build_html(source: str, output: str, resolved_json: str, externals_json: str = None,
               title: str = None, compact: bool = False):
    """Build the interactive HTML viewer."""
    with open(resolved_json, 'r', encoding='utf-8') as f:
        resolved = json.load(f)

    externals = []
    if externals_json:
        with open(externals_json, 'r', encoding='utf-8') as f:
            externals = json.load(f)

    build_html_from_resolved(source, output, resolved, externals, title, compact)


# ============================================================================
# RUN PIPELINE
# ============================================================================

def default_output_path(source: str) -> str:
    desktop = Path.home() / "Desktop"
    base_dir = desktop if desktop.exists() else Path.cwd()
    return str(base_dir / f"{Path(source).stem}-xref.html")


def run_pipeline(
    source: str,
    output: Optional[str] = None,
    title: Optional[str] = None,
    compact: bool = False,
    fetch_externals: bool = True,
) -> Dict[str, Any]:
    """Run the full xref pipeline and build the viewer."""
    structure = extract_structure(source)
    references = find_references(
        structure["document_text"],
        structure["sections"],
        structure.get("defined_terms", []),
    )
    resolved = resolve_references(structure, references)

    externals = []
    if fetch_externals and references.get("external_citations"):
        externals = fetch_external_citations(json.dumps(references["external_citations"]))

    output = output or default_output_path(source)
    build_html_from_resolved(source, output, resolved, externals, title, compact)

    summary = {
        "output": str(Path(output).expanduser()),
        "sections": len(resolved.get("flat_sections", [])),
        "internal_references_resolved": len(resolved.get("internal_references", [])),
        "internal_references_unresolved": len([item for item in resolved.get("unresolved", []) if item.get("unresolved_type") == "broken_reference"]),
        "defined_terms": len(resolved.get("defined_terms", [])),
        "defined_term_usages": len(resolved.get("defined_term_usages", [])),
        "undefined_terms": len([item for item in resolved.get("unresolved", []) if item.get("unresolved_type") == "undefined_term"]),
        "external_citations": len(resolved.get("external_citations", [])),
        "external_citations_fetched": len([item for item in externals if item.get("fetched")]),
    }
    print_summary(summary)
    return {"structure": structure, "references": references, "resolved": resolved, "externals": externals, "summary": summary}


def print_summary(summary: Dict[str, Any]):
    print()
    print(f"Saved to: {summary['output']}")
    print(f"Sections indexed: {summary['sections']}")
    print(
        "Internal references: "
        f"{summary['internal_references_resolved']} resolved, "
        f"{summary['internal_references_unresolved']} unresolved"
    )
    print(
        "Defined terms: "
        f"{summary['defined_terms']} indexed, "
        f"{summary['defined_term_usages']} usages, "
        f"{summary['undefined_terms']} possible undefined terms"
    )
    print(
        "External citations: "
        f"{summary['external_citations']} found, "
        f"{summary['external_citations_fetched']} fetched"
    )


# ============================================================================
# SETUP CHECK
# ============================================================================

def setup_check():
    """Check which dependencies are available."""
    print("Xref setup check:\n")

    deps = [
        ("python-docx", DocxDocument is not None, "Word document support"),
        ("pymupdf", fitz is not None, "PDF support"),
        ("beautifulsoup4", BeautifulSoup is not None, "HTML parsing"),
        ("requests", requests is not None, "External citation fetching"),
        ("jinja2", Template is not None, "HTML generation"),
    ]

    all_ok = True
    for name, available, description in deps:
        status = "OK" if available else "MISSING"
        print(f"  {status:7s} {name:20s} - {description}")
        if not available:
            all_ok = False

    print()

    try:
        import playwright  # noqa: F401
        print("  OK      playwright           - Web URL support (optional)")
    except ImportError:
        print("  SKIP    playwright           - Web URL support (optional, not installed)")

    print()

    if all_ok:
        print("All core dependencies installed")
        return 0
    else:
        print("Missing dependencies. Run: bash setup.sh")
        return 1


# ============================================================================
# CLI
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description="Xref - Legal document cross-reference resolver")
    subparsers = parser.add_subparsers(dest='command', help='Command to run')

    run_parser = subparsers.add_parser('run', help='Run the full pipeline and build an interactive HTML viewer')
    run_parser.add_argument('--source', required=True, help='Source document path')
    run_parser.add_argument('--output', help='Output HTML path (defaults to ~/Desktop/<source>-xref.html)')
    run_parser.add_argument('--title', help='Document title')
    run_parser.add_argument('--compact', action='store_true', help='Compact mode (no external statute text)')
    run_parser.add_argument('--no-fetch-external', action='store_true', help='Do not fetch external statute text')

    extract_parser = subparsers.add_parser('extract-structure', help='Extract document structure')
    extract_parser.add_argument('--source', required=True, help='Source document path')
    extract_parser.add_argument('--ai-assist', action='store_true', help='Reserved for future AI-assisted parsing')

    find_parser = subparsers.add_parser('find-references', help='Find all references')
    find_parser.add_argument('--source', required=True, help='Source document path')

    resolve_parser = subparsers.add_parser('resolve-references', help='Resolve references')
    resolve_parser.add_argument('--structure', required=True, help='Structure JSON file')
    resolve_parser.add_argument('--references', required=True, help='References JSON file')

    fetch_parser = subparsers.add_parser('fetch-external', help='Fetch external citations')
    fetch_parser.add_argument('--citations', required=True, help='Citations JSON string')

    build_parser = subparsers.add_parser('build', help='Build interactive HTML')
    build_parser.add_argument('--source', required=True, help='Source document path')
    build_parser.add_argument('--output', required=True, help='Output HTML path')
    build_parser.add_argument('--resolved', required=True, help='Resolved graph JSON')
    build_parser.add_argument('--externals', help='External citations JSON')
    build_parser.add_argument('--title', help='Document title')
    build_parser.add_argument('--compact', action='store_true', help='Compact mode (no external text)')

    subparsers.add_parser('setup-check', help='Check dependencies')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    if args.command == 'setup-check':
        return setup_check()

    check_core_deps()

    if args.command == 'run':
        run_pipeline(
            args.source,
            output=args.output,
            title=args.title,
            compact=args.compact,
            fetch_externals=not args.no_fetch_external,
        )
    elif args.command == 'extract-structure':
        print(json.dumps(extract_structure(args.source), indent=2))
    elif args.command == 'find-references':
        structure = extract_structure(args.source)
        result = find_references(
            structure["document_text"],
            structure["sections"],
            structure.get("defined_terms", []),
        )
        print(json.dumps(result, indent=2))
    elif args.command == 'resolve-references':
        with open(args.structure, 'r', encoding='utf-8') as f:
            structure = json.load(f)
        with open(args.references, 'r', encoding='utf-8') as f:
            references = json.load(f)
        print(json.dumps(resolve_references(structure, references), indent=2))
    elif args.command == 'fetch-external':
        print(json.dumps(fetch_external_citations(args.citations), indent=2))
    elif args.command == 'build':
        build_html(
            args.source,
            args.output,
            args.resolved,
            args.externals,
            args.title,
            args.compact,
        )

    return 0


if __name__ == '__main__':
    sys.exit(main())
