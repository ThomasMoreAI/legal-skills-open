"""Compile an explicit, bounded TimeNarratives source packet."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from conversation_units import parse_conversation_for_packet
from email_units import EmailParseError, parse_email
from packet_core import (
    LIMITS,
    container_record,
    finalize_packet,
    root_record,
    unreadable_container_record,
    validate_request,
)
from packet_core import PacketBuildError as PacketBuildError
from packet_docx import parse_docx_for_packet
from packet_filters import (
    apply_selected_source_filter,
    apply_selected_source_type_filter,
    propagate_leaf_uncertainty,
)
from packet_io import compile_to_directory, run_cli
from source_paths import (
    SourcePathError,
    SourceReadError,
    media_type,
    read_bounded_file,
    source_type_for_name,
)
from text_units import TextDecodeError, make_text_units


class _Compiler:
    def __init__(self, request: dict, source_root: Path) -> None:
        self.request = request
        self.source_root = source_root
        self.roots: list[dict] = []
        self.containers: list[dict] = []
        self.mime_leaves: list[dict] = []
        self.parts: list[dict] = []
        self.units: list[dict] = []
        self.errors: list[str] = []
        self.limitations: list[str] = []
        self.seen_hashes: dict[str, str] = {}
        self.selected_bytes = 0
        self.derived_count = 0

    def compile(self) -> dict:
        for index, selection in enumerate(self.request["selections"], start=1):
            root_id = f"S{index:04d}"
            if selection["kind"] == "user_note":
                self._user_note(root_id, index, selection["text"])
            else:
                self._selected_file(root_id, index, selection)
        propagate_leaf_uncertainty(self.roots, self.containers, self.mime_leaves)
        return finalize_packet(
            self.request,
            self.roots,
            self.containers,
            self.mime_leaves,
            self.parts,
            self.units,
            self.errors,
            self.limitations,
        )

    def _selected_file(self, root_id: str, index: int, selection: dict) -> None:
        relative = selection["path"]
        root = root_record(root_id, index, selection["kind"], relative)
        self.roots.append(root)
        source_type = (
            "conversation"
            if selection["kind"] == "conversation"
            else source_type_for_name(relative)
        )
        try:
            selected = read_bounded_file(
                self.source_root, relative, max_bytes=LIMITS["selectedContainerBytes"]
            )
        except (SourcePathError, SourceReadError) as exc:
            root.update(disposition="unreadable", reason=type(exc).__name__)
            self.errors.append("selected_source_unreadable")
            self.containers.append(
                unreadable_container_record(
                    root_id, root_id, relative, source_type, type(exc).__name__
                )
            )
            return
        self.selected_bytes += selected.byte_length
        if self.selected_bytes > LIMITS["selectedPacketBytes"]:
            root.update(
                disposition="unreadable", reason="selected_packet_bytes_exceeded"
            )
            self.errors.append("selected_packet_bytes_exceeded")
            self.containers.append(
                unreadable_container_record(
                    root_id,
                    root_id,
                    selected.display_name,
                    source_type,
                    root["reason"],
                )
            )
            return
        container = container_record(
            root_id,
            root_id,
            None,
            f"selection:{index - 1}",
            source_type,
            media_type(source_type, selected.display_name),
            selected.display_name,
            selected.data,
        )
        self.containers.append(container)
        duplicate_key = selected.sha256
        if source_type == "conversation":
            duplicate_key += ":conversation:" + selection["conversationId"]
        if duplicate_key in self.seen_hashes:
            root.update(disposition="exactDuplicate", reason="raw_sha256_match")
            container.update(disposition="exactDuplicate", reason="raw_sha256_match")
            return
        self.seen_hashes[duplicate_key] = root_id
        if source_type == "conversation":
            parsed = parse_conversation_for_packet(
                selected.data, selection, container, root, self.request["filters"]
            )
            self.parts.extend(parsed["parts"])
            self.units.extend(parsed["units"])
            self.errors.extend(parsed["errors"])
            self.limitations.extend(parsed["limitations"])
            return
        self._parse_container(container, root, selected.data)

    def _user_note(self, root_id: str, index: int, value: str) -> None:
        root = root_record(root_id, index, "user_note", None)
        self.roots.append(root)
        data = value.encode("utf-8")
        container = container_record(
            root_id,
            root_id,
            None,
            f"selection:{index - 1}",
            "user_note",
            "text/plain",
            "user-note",
            data,
        )
        self.containers.append(container)
        self.selected_bytes += len(data)
        reason = None
        if len(data) > LIMITS["selectedContainerBytes"]:
            reason = "selected_container_bytes_exceeded"
        elif self.selected_bytes > LIMITS["selectedPacketBytes"]:
            reason = "selected_packet_bytes_exceeded"
        if reason:
            root.update(disposition="unreadable", reason=reason)
            container.update(disposition="unreadable", reason=reason)
            self.errors.append(reason)
            return
        if not apply_selected_source_filter(container, root, self.request["filters"]):
            return
        root["disposition"] = "requiresConfirmation"
        container.update(
            disposition="requiresConfirmation",
            reason=container["reason"] or "user_attestation",
        )
        units = make_text_units(
            root_id,
            data,
            kind="user_note",
            role="attested",
            eligibility="requires_confirmation",
            source_class="user_attested",
            source_author=self.request["actor"]["name"],
        )
        for unit in units:
            unit["assertedByActorId"] = self.request["actor"]["id"]
        self.units.extend(units)

    def _parse_container(self, container: dict, root: dict, data: bytes) -> None:
        source_type = container["sourceType"]
        if source_type == "unsupported":
            root.update(disposition="unreadable", reason="unsupported_format")
            container.update(disposition="unreadable", reason="unsupported_format")
            self.errors.append("unsupported_format")
            return
        if not apply_selected_source_type_filter(
            container, root, self.request["filters"]
        ):
            return
        if source_type == "text":
            self._parse_text(container, root, data)
        elif source_type == "email":
            self._parse_eml(container, root, data)
        elif source_type == "docx":
            self._parse_docx(container, root, data)

    def _parse_text(self, container: dict, root: dict, data: bytes) -> None:
        if not apply_selected_source_filter(container, root, self.request["filters"]):
            return
        try:
            units = make_text_units(
                container["containerId"],
                data,
                kind="text_block",
                role="current",
                eligibility=(
                    "requires_confirmation"
                    if container["filterDisposition"] == "filter_indeterminate"
                    else "eligible"
                ),
            )
        except TextDecodeError:
            container.update(
                disposition="unreadable", reason="strict_utf8_decode_failed"
            )
            root.update(disposition="unreadable", reason="strict_utf8_decode_failed")
            self.errors.append("strict_utf8_decode_failed")
            return
        for unit in units:
            unit["assertedByActorId"] = None
        self.units.extend(units)

    def _parse_eml(self, container: dict, root: dict, data: bytes) -> None:
        try:
            parsed = parse_email(container["containerId"], data)
        except EmailParseError:
            container.update(disposition="unreadable", reason="malformed_eml")
            root.update(disposition="unreadable", reason="malformed_eml")
            self.errors.append("malformed_eml")
            return
        container.update(
            sourceTime=parsed["sourceTime"],
            sourceTimeKind="eml_date" if parsed["sourceTime"] else None,
            sourceAuthor=parsed["sourceAuthor"],
        )
        if not apply_selected_source_filter(container, root, self.request["filters"]):
            return
        if container["filterDisposition"] == "filter_indeterminate":
            for unit in parsed["units"]:
                if unit["eligibility"] == "eligible":
                    unit["eligibility"] = "requires_confirmation"
        if any(
            unit["eligibility"] == "requires_confirmation" for unit in parsed["units"]
        ):
            if container["disposition"] == "ready":
                container.update(
                    disposition="requiresConfirmation", reason="email_content_ambiguity"
                )
            if root["disposition"] == "ready":
                root.update(
                    disposition="requiresConfirmation", reason="email_content_ambiguity"
                )
        for unit in parsed["units"]:
            unit["assertedByActorId"] = None
        self.mime_leaves.extend(parsed["leaves"])
        self.units.extend(parsed["units"])
        self.limitations.extend(
            x for x in parsed["limitations"] if x not in self.limitations
        )
        for child in parsed["children"]:
            self._derived_container(root, child)

    def _derived_container(self, root: dict, child: dict) -> None:
        self.derived_count += 1
        if self.derived_count > LIMITS["derivedContainers"]:
            root.update(
                disposition="requiresConfirmation", reason="derived_container_cap"
            )
            self.errors.append("derived_container_cap_exceeded")
            return
        data = child.pop("rawBytes")
        container = container_record(
            child["containerId"],
            root["rootId"],
            child["parentContainerId"],
            child["originLocator"],
            child["sourceType"],
            child["mediaType"],
            child["displayName"],
            data,
        )
        self.containers.append(container)
        prior = self.seen_hashes.get(container["rawSha256"])
        if prior:
            container.update(disposition="exactDuplicate", reason="raw_sha256_match")
            for leaf in self.mime_leaves:
                if leaf["childContainerId"] == container["containerId"]:
                    leaf.update(disposition="exactDuplicate", reason="raw_sha256_match")
            return
        self.seen_hashes[container["rawSha256"]] = container["containerId"]
        self._parse_container(container, root, data)

    def _parse_docx(self, container: dict, root: dict, data: bytes) -> None:
        parsed = parse_docx_for_packet(data, container, root, self.request["filters"])
        self.parts.extend(parsed["parts"])
        self.units.extend(parsed["units"])
        self.errors.extend(parsed["errors"])
        self.limitations.extend(
            x for x in parsed["limitations"] if x not in self.limitations
        )


def compile_packet(request: Any, source_root: Path) -> dict:
    return _Compiler(validate_request(request), Path(source_root)).compile()


def compile_packet_to_directory(request: Any, source_root: Path, run_dir: Path) -> dict:
    return compile_to_directory(compile_packet, request, source_root, run_dir)


def main(argv: list[str] | None = None) -> int:
    return run_cli(compile_packet, argv, description=__doc__)


if __name__ == "__main__":
    raise SystemExit(main())
