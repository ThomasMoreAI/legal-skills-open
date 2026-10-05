"""Resolve active DOCX stories from evidentially meaningful references."""

from __future__ import annotations

import xml.etree.ElementTree as ET
from dataclasses import dataclass

from docx_package import WORD_NAMESPACES, DocxPackage  # type: ignore[import-not-found]

OFFICE_RELATIONSHIP_NAMESPACES = {
    "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "http://purl.oclc.org/ooxml/officeDocument/relationships",
}
STORY_RELATIONS = {
    "header": "header",
    "footer": "footer",
    "footnotes": "footnote",
    "endnotes": "endnote",
    "comments": "comment",
}
REFERENCE_ELEMENTS = {
    "footnotes": "footnoteReference",
    "endnotes": "endnoteReference",
    "comments": "commentReference",
}
EXTERNAL_CONTENT_RELATIONS = set(STORY_RELATIONS) | {"aFChunk", "image", "oleObject"}


@dataclass(frozen=True)
class Story:
    """One active story and any referenced child identifiers within it."""

    part: str
    role: str
    referenced_ids: frozenset[str] | None = None


def local_name(name: str) -> str:
    return name.rsplit("}", 1)[-1]


def namespace(name: str) -> str:
    return name[1:].split("}", 1)[0] if name.startswith("{") else ""


def relation_kind(relation: dict[str, str]) -> str:
    return relation["type"].rstrip("/").rsplit("/", 1)[-1]


def _attribute(
    element: ET.Element, name: str, allowed_namespaces: set[str]
) -> str | None:
    return next(
        (
            value
            for key, value in element.attrib.items()
            if local_name(key) == name and namespace(key) in allowed_namespaces
        ),
        None,
    )


def word_attribute(element: ET.Element, name: str) -> str | None:
    return _attribute(element, name, WORD_NAMESPACES)


def relationship_attribute(element: ET.Element, name: str) -> str | None:
    return _attribute(element, name, OFFICE_RELATIONSHIP_NAMESPACES)


def _reference_ids(root: ET.Element, element_name: str) -> frozenset[str]:
    return frozenset(
        identifier
        for element in root.iter()
        if namespace(element.tag) in WORD_NAMESPACES
        and local_name(element.tag) == element_name
        and (identifier := word_attribute(element, "id")) is not None
    )


def _section_relationship_ids(root: ET.Element, kind: str) -> tuple[str, ...]:
    return tuple(
        dict.fromkeys(
            identifier
            for element in root.iter()
            if namespace(element.tag) in WORD_NAMESPACES
            and local_name(element.tag) == f"{kind}Reference"
            and (identifier := relationship_attribute(element, "id")) is not None
        )
    )


def _story_candidates(package: DocxPackage) -> list[dict[str, str]]:
    return [
        relation
        for relation in package.relationships
        if relation["source"] == package.main_document
        and relation_kind(relation) in STORY_RELATIONS
    ]


def _media_story_parts(package: DocxPackage) -> set[str]:
    tokens = tuple(f".{kind}+xml" for kind in STORY_RELATIONS)
    return {
        name
        for name, media_type in package.media_types.items()
        if media_type.casefold().endswith(tokens)
    }


def story_scopes(package: DocxPackage, story: Story) -> list[ET.Element]:
    """Return only the XML scopes whose content is active for a story."""

    root = package.xml_roots[story.part]
    if story.referenced_ids is None:
        return [root]
    return [
        element
        for element in root.iter()
        if namespace(element.tag) in WORD_NAMESPACES
        and local_name(element.tag) == story.role
        and word_attribute(element, "id") in story.referenced_ids
    ]


def resolve_stories(
    package: DocxPackage,
) -> tuple[list[Story], set[str], list[tuple[str, str]]]:
    """Return active stories and recognized story parts that are unreferenced."""

    main = package.main_document
    main_root = package.xml_roots[main]
    candidates = _story_candidates(package)
    stories = [Story(main, "body")]
    issues: list[tuple[str, str]] = []
    unreferenced = _media_story_parts(package)
    unreferenced.update(
        target
        for relation in candidates
        if (target := relation.get("resolvedTarget")) in package.members
    )

    for kind in ("header", "footer"):
        referenced = _section_relationship_ids(main_root, kind)
        for identifier in referenced:
            matches = [
                relation
                for relation in package.relationships
                if relation["source"] == main and relation["id"] == identifier
            ]
            if len(matches) != 1:
                continue
            relation = matches[0]
            if relation_kind(relation) != kind:
                issues.append(("invalid_referenced_story_relationship", main))
                continue
            target = relation.get("resolvedTarget")
            story = Story(target or "", kind)
            if target in package.xml_roots and story not in stories:
                stories.append(story)

    active_roots = [package.xml_roots[story.part] for story in stories]
    for kind, element_name in REFERENCE_ELEMENTS.items():
        referenced = frozenset().union(
            *(_reference_ids(root, element_name) for root in active_roots)
        )
        if not referenced:
            continue
        matches = [item for item in candidates if relation_kind(item) == kind]
        if len(matches) != 1:
            code = (
                "missing_referenced_story_relationship"
                if not matches
                else "ambiguous_referenced_story_relationship"
            )
            issues.append((code, main))
            continue
        relation = matches[0]
        target = relation.get("resolvedTarget")
        if relation.get("external") == "true":
            issues.append(("external_relationship_not_retrieved", main))
        elif target not in package.members:
            issues.append(("missing_internal_relationship_target", main))
        elif target not in package.xml_roots:
            issues.append(("invalid_referenced_story_part", main))
        else:
            story = Story(target, STORY_RELATIONS[kind], referenced)
            stories.append(story)
            if not story_scopes(package, story):
                issues.append(("missing_referenced_story_content", target))

    unreferenced.difference_update(story.part for story in stories)
    return stories, unreferenced, issues


def _active_relationship_references(
    package: DocxPackage, stories: list[Story]
) -> list[tuple[str, str, str]]:
    references: list[tuple[str, str, str]] = []
    for story in stories:
        for scope in story_scopes(package, story):
            for element in scope.iter():
                for attribute, identifier in element.attrib.items():
                    if (
                        namespace(attribute) in OFFICE_RELATIONSHIP_NAMESPACES
                        and local_name(attribute) in {"id", "embed", "link"}
                        and identifier
                    ):
                        references.append(
                            (story.part, identifier, local_name(attribute))
                        )
    return references


def active_relationship_issues(
    package: DocxPackage, stories: list[Story]
) -> list[tuple[str, str]]:
    """Close every relationship identifier used by active story content."""

    issues: list[tuple[str, str]] = []
    for source, identifier, attribute in _active_relationship_references(
        package, stories
    ):
        matches = [
            relation
            for relation in package.relationships
            if relation["source"] == source and relation["id"] == identifier
        ]
        if len(matches) != 1:
            code = (
                "missing_relationship_reference"
                if not matches
                else "ambiguous_relationship_reference"
            )
            issues.append((code, source))
            continue
        relation = matches[0]
        target = relation.get("target", "")
        kind = relation_kind(relation)
        if relation.get("external") == "true":
            if not target:
                issues.append(("missing_external_relationship_target", source))
            elif attribute in {"embed", "link"} or kind in EXTERNAL_CONTENT_RELATIONS:
                issues.append(("external_relationship_not_retrieved", source))
        elif relation.get("resolvedTarget") not in package.members:
            issues.append(("missing_internal_relationship_target", source))
    return issues
