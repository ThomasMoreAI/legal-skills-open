"""Build packet-contract units from validated WordprocessingML story parts."""

from __future__ import annotations

import hashlib
import xml.etree.ElementTree as ET
from collections import Counter
from typing import Any

from docx_package import WORD_NAMESPACES, DocxPackage  # type: ignore[import-not-found]

REVISION_ROLES = {
    "ins": "inserted",
    "del": "deleted",
    "moveTo": "moved_to",
    "moveFrom": "moved_from",
}
MATH_NAMESPACES = {
    "http://schemas.openxmlformats.org/officeDocument/2006/math",
    "http://purl.oclc.org/ooxml/officeDocument/math",
}


def _local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _namespace(tag: str) -> str:
    return tag[1:].split("}", 1)[0] if tag.startswith("{") else ""


def _word(element: ET.Element) -> bool:
    return _namespace(element.tag) in WORD_NAMESPACES


def _attr(element: ET.Element, name: str) -> str | None:
    value = next(
        (
            value
            for key, value in element.attrib.items()
            if _local(key) == name and _namespace(key) in WORD_NAMESPACES
        ),
        None,
    )
    return value if value else None


def word_elements(root: ET.Element, *names: str) -> list[ET.Element]:
    wanted = set(names)
    return [
        element
        for element in root.iter()
        if _word(element) and _local(element.tag) in wanted
    ]


def _text(element: ET.Element, *, accepted: bool) -> str:
    local = _local(element.tag) if _word(element) else ""
    if _namespace(element.tag) in MATH_NAMESPACES and _local(element.tag) == "t":
        return element.text or ""
    if accepted and local in {"del", "moveFrom"}:
        return ""
    if local in {"t", "delText", "instrText"}:
        if accepted and local in {"delText", "instrText"}:
            return ""
        return element.text or ""
    if local == "tab":
        return "\t"
    if local in {"br", "cr"}:
        return "\n"
    return "".join(_text(child, accepted=accepted) for child in element)


def _accepted_paragraphs(root: ET.Element) -> list[ET.Element]:
    paragraphs: list[ET.Element] = []

    def visit(element: ET.Element) -> None:
        local = _local(element.tag) if _word(element) else ""
        if local in {"del", "moveFrom"}:
            return
        if local == "p":
            paragraphs.append(element)
            return
        for child in element:
            visit(child)

    visit(root)
    return paragraphs


def _attribution(author: str | None, *, malformed_move: bool = False) -> str:
    state = (
        "documentary_author_unverified_actor_unestablished"
        if author
        else "author_missing_actor_unestablished"
    )
    return f"{state}_move_pair_malformed" if malformed_move else state


class UnitExtractor:
    """Stateful, deterministic unit allocator for one DOCX container."""

    def __init__(self, package: DocxPackage, container_id: str) -> None:
        self.package = package
        self.container_id = container_id
        self.part_ids = {
            name: f"{container_id}-P{index:04d}"
            for index, name in enumerate(package.members, 1)
        }
        self.units: list[dict[str, Any]] = []
        self.part_units = {name: [] for name in package.members}
        self.parsed_parts: set[str] = set()

    def add(
        self,
        part: str,
        text: str,
        *,
        kind: str,
        role: str,
        eligibility: str,
        locator: str,
        metadata: dict[str, str | None] | None = None,
    ) -> None:
        unit_id = f"{self.container_id}-U{len(self.units) + 1:04d}"
        canonical = text.encode("utf-8")
        details: dict[str, str | None] = {"partName": part}
        details.update(metadata or {})
        self.units.append(
            {
                "unitId": unit_id,
                "containerId": self.container_id,
                "originId": self.part_ids[part],
                "kind": kind,
                "role": role,
                "locator": f"docx:{part}#{locator}",
                "canonicalText": text,
                "canonicalUtf8Sha256": hashlib.sha256(canonical).hexdigest(),
                "utf8Start": 0,
                "utf8End": len(canonical),
                "eligibility": eligibility,
                "coverageDisposition": "pending",
                "sourceClass": "documentary_supported",
                "sourceAuthor": None,
                "sourceTime": self.package.filter_timestamp,
                "assertedByActorId": None,
                "metadata": details,
            }
        )
        self.part_units[part].append(unit_id)

    def accepted(
        self,
        part: str,
        root: ET.Element,
        story: str,
        referenced_ids: frozenset[str] | None = None,
    ) -> None:
        self.parsed_parts.add(part)
        if story in {"footnote", "endnote"}:
            scope = self._notes(part, root, story, referenced_ids)
        elif story == "comment":
            scope = self._comments(part, root, referenced_ids)
        else:
            scope = root
            for index, paragraph in enumerate(_accepted_paragraphs(root), 1):
                text = _text(paragraph, accepted=True)
                if text.strip():
                    self.add(
                        part,
                        text,
                        kind="docx_accepted",
                        role="accepted",
                        eligibility="eligible",
                        locator=f"{story}/p[{index}]",
                    )
        self.revisions(part, scope)
        self.fields(part, scope)

    def _notes(
        self,
        part: str,
        root: ET.Element,
        story: str,
        referenced_ids: frozenset[str] | None,
    ) -> ET.Element:
        selected = ET.Element("selected")
        for index, note in enumerate(word_elements(root, story), 1):
            note_id = _attr(note, "id")
            if (
                _attr(note, "type")
                or (note_id and note_id.startswith("-"))
                or (referenced_ids is not None and note_id not in referenced_ids)
            ):
                continue
            selected.append(note)
            values = [
                _text(paragraph, accepted=True)
                for paragraph in _accepted_paragraphs(note)
            ]
            text = "\n".join(value for value in values if value.strip())
            if text:
                self.add(
                    part,
                    text,
                    kind="docx_accepted",
                    role="accepted",
                    eligibility="eligible",
                    locator=f"{story}[{index}]",
                )
        return selected

    def _comments(
        self,
        part: str,
        root: ET.Element,
        referenced_ids: frozenset[str] | None,
    ) -> ET.Element:
        selected = ET.Element("selected")
        for index, comment in enumerate(word_elements(root, "comment"), 1):
            if (
                referenced_ids is not None
                and _attr(comment, "id") not in referenced_ids
            ):
                continue
            selected.append(comment)
            values = [
                _text(paragraph, accepted=True)
                for paragraph in _accepted_paragraphs(comment)
            ]
            text = "\n".join(value for value in values if value.strip())
            if not text:
                continue
            author = _attr(comment, "author")
            self.add(
                part,
                text,
                kind="docx_annotation",
                role="context",
                eligibility="context_only",
                locator=f"comment[{index}]",
                metadata={
                    "commentId": _attr(comment, "id"),
                    "author": author,
                    "date": _attr(comment, "date"),
                    "attributionState": _attribution(author),
                },
            )
        return selected

    def revisions(self, part: str, root: ET.Element) -> None:
        revisions = word_elements(root, *REVISION_ROLES)
        move_counts = Counter(
            (_local(item.tag), _attr(item, "id"))
            for item in revisions
            if _local(item.tag) in {"moveFrom", "moveTo"}
        )
        for index, item in enumerate(revisions, 1):
            revision_kind = _local(item.tag)
            revision_id = _attr(item, "id")
            malformed = revision_kind.startswith("move") and (
                not revision_id
                or move_counts[("moveFrom", revision_id)] != 1
                or move_counts[("moveTo", revision_id)] != 1
            )
            author = _attr(item, "author")
            self.add(
                part,
                _text(item, accepted=False),
                kind="docx_revision",
                role=REVISION_ROLES[revision_kind],
                eligibility="context_only",
                locator=f"revision[{index}]",
                metadata={
                    "revisionKind": revision_kind,
                    "revisionId": revision_id,
                    "author": author,
                    "date": _attr(item, "date"),
                    "attributionState": _attribution(author, malformed_move=malformed),
                    "acceptedEffect": "included_in_accepted_text"
                    if revision_kind in {"ins", "moveTo"}
                    else "excluded_from_accepted_text",
                },
            )
        self._property_revisions(part, root)

    def _property_revisions(self, part: str, root: ET.Element) -> None:
        changes = [
            element
            for element in root.iter()
            if _word(element) and _local(element.tag).endswith("PrChange")
        ]
        for index, item in enumerate(changes, 1):
            author = _attr(item, "author")
            self.add(
                part,
                "",
                kind="docx_revision",
                role="context",
                eligibility="ineligible",
                locator=f"property-revision[{index}]",
                metadata={
                    "revisionKind": _local(item.tag),
                    "revisionId": _attr(item, "id"),
                    "author": author,
                    "date": _attr(item, "date"),
                    "attributionState": _attribution(author),
                    "acceptedEffect": "property_only",
                },
            )

    def fields(self, part: str, root: ET.Element) -> None:
        instructions = [
            value.strip()
            for item in word_elements(root, "fldSimple")
            if (value := _attr(item, "instr")) and value.strip()
        ]
        instructions.extend(
            (item.text or "").strip()
            for item in word_elements(root, "instrText")
            if (item.text or "").strip()
        )
        for index, instruction in enumerate(instructions, 1):
            self.add(
                part,
                instruction,
                kind="docx_annotation",
                role="context",
                eligibility="ineligible",
                locator=f"field-instruction[{index}]",
                metadata={"fieldInstructions": instruction},
            )
