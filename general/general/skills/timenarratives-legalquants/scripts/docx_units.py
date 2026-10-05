"""Orchestrate fail-closed DOCX extraction and package reconciliation.

A limitation is *degrading* when active story content could not be surfaced:
an altChunk, an OLE object, an unresolved symbol, a referenced note, comment
or header story that is missing, ambiguous, external or unreadable, or a
text-bearing part of unknown role. Only degrading codes decide ``partial``,
and only the story parts they attach to are ``affectedParts``.

A limitation is *informational* when nothing in the story text is affected:
an image, a non-evidential package part, or a core timestamp that could not
be parsed (already reported as ``sourceTime: null``). Those are ``notes``.
"""

from __future__ import annotations

import hashlib
import re
from typing import Any

from docx_package import (  # type: ignore[import-not-found]
    DCTERMS_NAMESPACE,
    DocxPackage,
    PackageError,
    load_docx_package,
)
from docx_references import (  # type: ignore[import-not-found]
    Story,
    active_relationship_issues,
    resolve_stories,
    story_scopes,
)
from docx_text import UnitExtractor, word_elements  # type: ignore[import-not-found]

NON_EVIDENTIAL_PARTS = re.compile(
    r"^(?:customXml/.*"
    r"|word/glossary/.*"
    r"|word/theme/.*"
    r"|word/(?:styles|stylesWithEffects|settings|numbering|fontTable|webSettings"
    r"|people|commentsExtended|commentsIds|commentsExtensible|intelligence\d*)\.xml"
    r"|docProps/(?:core|app|custom|thumbnail)\.[A-Za-z0-9]+"
    r"|\[Content_Types\]\.xml"
    r"|.*\.rels)$"
)
DEGRADING_LIMITATIONS = frozenset(
    {
        "alt_chunk",
        "embedded_ole",
        "font_symbol_unresolved",
        "unparsed_text_part",
        "invalid_referenced_story_relationship",
        "missing_referenced_story_relationship",
        "ambiguous_referenced_story_relationship",
        "missing_referenced_story_content",
        "invalid_referenced_story_part",
        "missing_internal_relationship_target",
        "external_relationship_not_retrieved",
        "missing_relationship_reference",
        "ambiguous_relationship_reference",
        "missing_external_relationship_target",
    }
)
INFORMATIONAL_NOTES = frozenset({"image_not_ocr", "invalid_core_timestamp"})
CONTAINER_ID = re.compile(r"^[A-Za-z][A-Za-z0-9._-]{0,127}$")


def _invalid_core_timestamp(package: DocxPackage) -> bool:
    core = package.xml_roots.get("docProps/core.xml")
    modified_tag = f"{{{DCTERMS_NAMESPACE}}}modified"
    return (
        package.filter_timestamp is None
        and core is not None
        and any(element.tag == modified_tag for element in core.iter())
    )


class _Run:
    def __init__(self, package: DocxPackage, container_id: str) -> None:
        self.package = package
        self.container_id = container_id
        self.extractor = UnitExtractor(package, container_id)
        self.limitations: list[str] = []
        self.notes: list[str] = []
        self.unreadable_parts: dict[str, str] = {}
        self.excluded_parts: dict[str, str] = {}

    def limit(self, code: str, part: str | None = None) -> None:
        if code in INFORMATIONAL_NOTES:
            if code not in self.notes:
                self.notes.append(code)
            if part is not None and part in self.package.members:
                self.excluded_parts.setdefault(part, code)
            return
        if code not in self.limitations:
            self.limitations.append(code)
        if part is not None and part in self.package.members:
            self.unreadable_parts.setdefault(part, code)

    def affected_parts(self) -> list[str]:
        """Story parts whose units are under a degrading limitation.

        A degrading code attached to a part that is not a story (an unknown
        text-bearing part, an imported chunk) cannot be scoped to any story,
        so it affects every story part: the document stays fail-closed.
        """
        stories = self.extractor.parsed_parts
        degrading = {
            part: code
            for part, code in self.unreadable_parts.items()
            if code in DEGRADING_LIMITATIONS
        }
        referenced = {
            relation.get("resolvedTarget")
            for relation in self.package.relationships
            if relation["source"] in stories
        }
        scoped = sorted(part for part in degrading if part in stories)
        unscoped = [p for p in degrading if p not in stories and p not in referenced]
        empty_scoped = [p for p in scoped if not self.extractor.part_units[p]]
        if unscoped or empty_scoped or (not scoped and degrading):
            return sorted(stories)
        return scoped

    def story_parts(self) -> list[Story]:
        stories, unreferenced, issues = resolve_stories(self.package)
        self.excluded_parts.update(
            {part: "unreferenced_story_part" for part in unreferenced}
        )
        for code, part in issues:
            self.limit(code, part)
        return stories

    def inspect_limitations(self, stories: list[Story]) -> None:
        story_parts = {story.part for story in stories}
        for code, part in active_relationship_issues(self.package, stories):
            self.limit(code, part)
        for story in stories:
            for scope in story_scopes(self.package, story):
                if word_elements(scope, "altChunk"):
                    self.limit("alt_chunk", story.part)
                if word_elements(scope, "object", "OLEObject"):
                    self.limit("embedded_ole", story.part)
                if word_elements(scope, "sym"):
                    self.limit("font_symbol_unresolved", story.part)
        for name, media_type in self.package.media_types.items():
            text_bearing = media_type.startswith("text/") or media_type.endswith(
                ("+xml", "/xml")
            )
            control = NON_EVIDENTIAL_PARTS.fullmatch(name) is not None
            if (
                text_bearing
                and name not in story_parts
                and name not in self.excluded_parts
                and not control
            ):
                self.limit("unparsed_text_part", name)
            if media_type.startswith("image/"):
                self.limit("image_not_ocr", name)

    def parts(self) -> list[dict[str, Any]]:
        output = []
        for name, payload in self.package.members.items():
            unit_ids = self.extractor.part_units[name]
            reason = self.unreadable_parts.get(name)
            excluded_reason = self.excluded_parts.get(name)
            if reason:
                disposition = "unreadable"
            elif excluded_reason:
                disposition, reason = "excluded", excluded_reason
            elif unit_ids:
                disposition = "ready"
            elif name in self.extractor.parsed_parts:
                disposition, reason = "unreadable", "no_extractable_text"
            else:
                disposition, reason = "excluded", "package_control_or_non_text"
            output.append(
                {
                    "partId": self.extractor.part_ids[name],
                    "containerId": self.container_id,
                    "locator": f"docx:{name}",
                    "mediaType": self.package.media_types.get(name)
                    or "application/octet-stream",
                    "rawSha256": hashlib.sha256(payload).hexdigest(),
                    "byteLength": len(payload),
                    "role": "story"
                    if name in self.extractor.parsed_parts
                    else "package_part",
                    "disposition": disposition,
                    "reason": reason,
                    "unitIds": unit_ids,
                }
            )
        return output


def _rejected_parts(error: PackageError, container_id: str) -> list[dict[str, Any]]:
    return [
        {
            "partId": f"{container_id}-P{index:04d}",
            "containerId": container_id,
            "locator": f"docx:{name}",
            "mediaType": "application/octet-stream",
            "rawSha256": None,
            "byteLength": 0,
            "role": "unvalidated_package_member",
            "disposition": "unreadable",
            "reason": error.code,
            "unitIds": [],
        }
        for index, name in enumerate(error.member_names, 1)
    ]


def parse_docx(data: bytes, container_id: str) -> dict[str, Any]:
    """Return a fail-closed, container-scoped DOCX evidence inventory."""

    if (
        not isinstance(data, bytes)
        or not isinstance(container_id, str)
        or CONTAINER_ID.fullmatch(container_id) is None
    ):
        raise ValueError("parse_docx requires bytes and a non-empty container_id")
    try:
        package = load_docx_package(data)
    except PackageError as error:
        return {
            "disposition": "unreadable",
            "reason": error.code,
            "filterTimestamp": None,
            "sourceTime": None,
            "sourceTimeKind": None,
            "sourceAuthor": None,
            "parts": _rejected_parts(error, container_id),
            "units": [],
            "limitations": [error.code],
            "notes": [],
            "affectedParts": [],
        }
    run = _Run(package, container_id)
    if _invalid_core_timestamp(package):
        run.limit("invalid_core_timestamp", "docProps/core.xml")
    stories = run.story_parts()
    for story in stories:
        run.extractor.accepted(
            story.part,
            package.xml_roots[story.part],
            story.role,
            story.referenced_ids,
        )
    run.inspect_limitations(stories)
    eligible = any(unit["eligibility"] == "eligible" for unit in run.extractor.units)
    degrading = [code for code in run.limitations if code in DEGRADING_LIMITATIONS]
    if not eligible:
        disposition, reason = "unreadable", "no_extractable_text"
    elif degrading:
        disposition, reason = "partial", "unparsed_text_bearing_content"
    else:
        disposition, reason = "ready", None
    return {
        "disposition": disposition,
        "reason": reason,
        "filterTimestamp": package.filter_timestamp,
        "sourceTime": package.filter_timestamp,
        "sourceTimeKind": "docx_core_modified" if package.filter_timestamp else None,
        "sourceAuthor": None,
        "parts": run.parts(),
        "units": run.extractor.units,
        "limitations": run.limitations,
        "notes": run.notes,
        "affectedParts": run.affected_parts(),
    }
