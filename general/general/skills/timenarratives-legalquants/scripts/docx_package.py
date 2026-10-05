"""Validate and inventory an OOXML Word package without extracting files."""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET
import zipfile
from dataclasses import dataclass
from datetime import datetime
from io import BytesIO
from pathlib import PurePosixPath

MAX_MEMBERS = 512
MAX_MEMBER_BYTES = 32 * 1024 * 1024
MAX_TOTAL_BYTES = 128 * 1024 * 1024
MAX_COMPRESSION_RATIO = 500.0
MAX_PATH_DEPTH = 16
MAX_XML_ELEMENTS = 250_000
MAX_XML_DEPTH = 128
WORD_NAMESPACES = {
    "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "http://purl.oclc.org/ooxml/wordprocessingml/main",
}
CONTENT_TYPES_NAMESPACE = "http://schemas.openxmlformats.org/package/2006/content-types"
RELATIONSHIPS_NAMESPACE = "http://schemas.openxmlformats.org/package/2006/relationships"
DCTERMS_NAMESPACE = "http://purl.org/dc/terms/"
MAIN_CONTENT_TYPE = (
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"
)
RFC3339 = re.compile(
    r"\d{4}-\d{2}-\d{2}T(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d(?:\.\d+)?(?:Z|[+-](?:[01]\d|2[0-3]):[0-5]\d)"
)


class PackageError(ValueError):
    """Stable fail-closed package error with any safely inventoried names."""

    def __init__(self, code: str, member_names: tuple[str, ...] = ()) -> None:
        self.code = code
        self.member_names = member_names
        super().__init__(code)


@dataclass(frozen=True)
class DocxPackage:
    """Validated in-memory view used by the semantic unit reader."""

    members: dict[str, bytes]
    xml_roots: dict[str, ET.Element]
    media_types: dict[str, str]
    main_document: str
    filter_timestamp: str | None
    relationships: tuple[dict[str, str], ...]
    external_relationships: tuple[dict[str, str], ...]


def _local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _namespace(tag: str) -> str:
    return tag[1:].split("}", 1)[0] if tag.startswith("{") else ""


def _is_directory_entry(item: zipfile.ZipInfo) -> bool:
    """A zero-length member whose name ends in '/' is a directory marker."""
    return item.orig_filename.endswith("/") and item.file_size == 0


def _validate_infos(infos: list[zipfile.ZipInfo]) -> tuple[str, ...]:
    names = tuple(item.orig_filename for item in infos)
    if len(infos) > MAX_MEMBERS:
        raise PackageError("member_count_limit", names)
    seen: set[str] = set()
    folded: set[str] = set()
    total = 0
    for item in infos:
        name = item.orig_filename
        parts = name.split("/")
        if (
            not name
            or "\\" in name
            or name.startswith("/")
            or ":" in parts[0]
            or any(part in ("", ".", "..") for part in parts)
        ):
            raise PackageError("unsafe_member_path", names)
        if len(parts) > MAX_PATH_DEPTH:
            raise PackageError("member_depth_limit", names)
        if name in seen:
            raise PackageError("duplicate_member", names)
        if name.casefold() in folded:
            raise PackageError("member_case_collision", names)
        seen.add(name)
        folded.add(name.casefold())
        if item.flag_bits & 1:
            raise PackageError("encrypted_package", names)
        if item.compress_type not in (zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED):
            raise PackageError("unsupported_compression", names)
        if item.file_size > MAX_MEMBER_BYTES:
            raise PackageError("member_size_limit", names)
        total += item.file_size
        if total > MAX_TOTAL_BYTES:
            raise PackageError("package_size_limit", names)
        if item.file_size and (
            not item.compress_size
            or item.file_size / item.compress_size > MAX_COMPRESSION_RATIO
        ):
            raise PackageError("compression_ratio_limit", names)
    return names


def _parse_xml(payload: bytes, names: tuple[str, ...]) -> ET.Element:
    declaration_probe = payload.upper().replace(b"\x00", b"")
    if b"<!DOCTYPE" in declaration_probe or b"<!ENTITY" in declaration_probe:
        raise PackageError("forbidden_xml_declaration", names)
    try:
        root = ET.fromstring(payload)
    except ET.ParseError as exc:
        raise PackageError("malformed_xml", names) from exc
    stack = [(root, 1)]
    elements = 0
    while stack:
        element, depth = stack.pop()
        elements += 1
        if depth > MAX_XML_DEPTH:
            raise PackageError("xml_depth_limit", names)
        if elements > MAX_XML_ELEMENTS:
            raise PackageError("xml_element_limit", names)
        stack.extend((child, depth + 1) for child in element)
    return root


def _valid_timestamp(value: str | None) -> str | None:
    if value is None or RFC3339.fullmatch(value) is None:
        return None
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return value


def _relationship_source(name: str) -> str:
    if name == "_rels/.rels":
        return ""
    parent, filename = name.rsplit("/_rels/", 1)
    return f"{parent}/{filename.removesuffix('.rels')}"


def _resolve_target(source: str, target: str) -> str:
    if (
        not target
        or "\\" in target
        or target.startswith("/")
        or ":" in target.split("/", 1)[0]
    ):
        raise ValueError("unsafe relationship target")
    base = PurePosixPath(source).parent if source else PurePosixPath()
    parts: list[str] = []
    for part in (base / target).parts:
        if part == "..":
            if not parts:
                raise ValueError("relationship target escapes package")
            parts.pop()
        elif part not in ("", "."):
            parts.append(part)
    return "/".join(parts)


def _content_types(root: ET.Element, names: list[str]) -> dict[str, str]:
    defaults: dict[str, str] = {}
    overrides: dict[str, str] = {}
    for child in root:
        if _local(child.tag) == "Default":
            defaults[child.attrib.get("Extension", "").casefold()] = child.attrib.get(
                "ContentType", ""
            )
        elif _local(child.tag) == "Override":
            overrides[child.attrib.get("PartName", "").lstrip("/")] = child.attrib.get(
                "ContentType", ""
            )
    return {
        name: overrides.get(
            name, defaults.get(PurePosixPath(name).suffix.lstrip(".").casefold(), "")
        )
        for name in names
    }


def load_docx_package(data: bytes) -> DocxPackage:
    """Load an in-memory DOCX package; no member is written to disk."""

    if not data.startswith(b"PK\x03\x04"):
        raise PackageError("invalid_zip_magic")
    try:
        archive = zipfile.ZipFile(BytesIO(data))
        infos = [item for item in archive.infolist() if not _is_directory_entry(item)]
    except (OSError, zipfile.BadZipFile) as exc:
        raise PackageError("invalid_zip") from exc
    names = _validate_infos(infos)
    try:
        members = {item.filename: archive.read(item) for item in infos}
    except (OSError, RuntimeError, zipfile.BadZipFile) as exc:
        raise PackageError("corrupt_member", names) from exc
    finally:
        archive.close()
    if "[Content_Types].xml" not in members:
        raise PackageError("missing_content_types", names)
    if "_rels/.rels" not in members:
        raise PackageError("missing_root_relationships", names)
    roots = {
        name: _parse_xml(payload, names)
        for name, payload in members.items()
        if name.casefold().endswith((".xml", ".rels"))
    }
    content_root = roots["[Content_Types].xml"]
    if (
        _local(content_root.tag) != "Types"
        or _namespace(content_root.tag) != CONTENT_TYPES_NAMESPACE
    ):
        raise PackageError("invalid_content_types", names)
    relationships_root = roots["_rels/.rels"]
    if (
        _local(relationships_root.tag) != "Relationships"
        or _namespace(relationships_root.tag) != RELATIONSHIPS_NAMESPACE
    ):
        raise PackageError("invalid_root_relationships", names)
    media_types = _content_types(roots["[Content_Types].xml"], list(names))
    for name, media_type in media_types.items():
        if media_type.casefold().endswith(("+xml", "/xml")) and name not in roots:
            roots[name] = _parse_xml(members[name], names)
    folded_names = {name.casefold() for name in names}
    if folded_names & {"encryptioninfo", "encryptedpackage"}:
        raise PackageError("encrypted_package", names)
    if any(
        "macroenabled" in value.casefold() or "vbaproject" in value.casefold()
        for value in media_types.values()
    ) or any(name.endswith("vbaproject.bin") for name in folded_names):
        raise PackageError("macro_enabled_package", names)
    relationships: list[dict[str, str]] = []
    for name, root in roots.items():
        if not name.casefold().endswith(".rels"):
            continue
        if name != "_rels/.rels" and "/_rels/" not in name:
            raise PackageError("invalid_relationship_part", names)
        if (
            _local(root.tag) != "Relationships"
            or _namespace(root.tag) != RELATIONSHIPS_NAMESPACE
        ):
            raise PackageError("invalid_relationships", names)
        source = _relationship_source(name)
        for element in root:
            if (
                _local(element.tag) != "Relationship"
                or _namespace(element.tag) != RELATIONSHIPS_NAMESPACE
            ):
                continue
            relation = {
                "id": element.attrib.get("Id", ""),
                "source": source,
                "target": element.attrib.get("Target", ""),
                "type": element.attrib.get("Type", ""),
            }
            if element.attrib.get("TargetMode", "").casefold() != "external":
                try:
                    relation["resolvedTarget"] = _resolve_target(
                        source, relation["target"]
                    )
                except ValueError as exc:
                    raise PackageError("unsafe_relationship_target", names) from exc
            else:
                relation["external"] = "true"
            relationships.append(relation)
    main_relation = next(
        (
            relation
            for relation in relationships
            if not relation["source"]
            and relation["type"].rstrip("/").endswith("/officeDocument")
            and "resolvedTarget" in relation
        ),
        None,
    )
    if main_relation is None:
        raise PackageError("missing_main_document_relationship", names)
    main_document = main_relation["resolvedTarget"]
    if main_document not in members:
        raise PackageError("missing_main_document", names)
    if media_types[main_document].casefold() != MAIN_CONTENT_TYPE.casefold():
        raise PackageError("invalid_main_document_content_type", names)
    main_root = roots.get(main_document)
    if (
        main_root is None
        or _local(main_root.tag) != "document"
        or _namespace(main_root.tag) not in WORD_NAMESPACES
    ):
        raise PackageError("invalid_main_document_root", names)
    modified = None
    core = roots.get("docProps/core.xml")
    if core is not None:
        modified = _valid_timestamp(
            next(
                (
                    element.text
                    for element in core.iter()
                    if _local(element.tag) == "modified"
                    and _namespace(element.tag) == DCTERMS_NAMESPACE
                ),
                None,
            )
        )
    external = tuple(
        {key: relation[key] for key in ("id", "source", "target", "type")}
        for relation in relationships
        if relation.get("external") == "true"
    )
    return DocxPackage(
        members=members,
        xml_roots=roots,
        media_types=media_types,
        main_document=main_document,
        filter_timestamp=modified,
        relationships=tuple(relationships),
        external_relationships=external,
    )
