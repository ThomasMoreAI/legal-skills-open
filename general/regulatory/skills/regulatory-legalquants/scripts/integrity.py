"""Immutable source-lineage checks for the Regulatory skill. Stdlib only."""

from __future__ import annotations

import hashlib
import json
import re
from datetime import date
from pathlib import Path

SCHEMA = "regulatory-integrity/v1"
CONFIRMED = "confirmed"
HISTORICAL_SELECTED = "historical_selected"
UNRESOLVED = "unresolved"
BLOCKED = "blocked"
RELIANCE_STATES = {CONFIRMED, HISTORICAL_SELECTED}
STOP_SEVERITIES = {"superseded", "incomplete"}
EDITORIAL_MARKER = re.compile(r"[►◄▼▲]\s*[A-Z]?\d*")
WHITESPACE = re.compile(r"\s+")
IDENTITY_FIELDS = ("jurisdiction", "profile", "instrument_id")


class IntegrityError(ValueError):
    """The saved evidence chain is incomplete or no longer matches."""


def sha256_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def sha256_file(path: Path) -> str:
    if not path.is_file():
        raise IntegrityError(f"Required saved file is missing: {path.name}")
    return sha256_bytes(path.read_bytes())


NOT_A_SAVED_FILE = (
    "{label} is not a saved file: {path}\n"
    "Every step of this skill reads and re-reads the same bytes — to hash them, "
    "to\nquote from them, and to re-check them later. A pipe, device or "
    "directory yields\nits contents once or never, so nothing downstream can "
    "confirm what was read.\nSave the text to an ordinary file and pass that."
)


def require_saved_file(path: Path, label: str = "Input") -> Path:
    """Refuse anything that cannot be read twice and hashed.

    A named pipe passes `exists()` and then blocks forever on read, which is
    indistinguishable from a slow script. Bounding it here means every consumer
    fails in the first second with a message that names the remedy.
    """
    if not path.is_file():
        raise IntegrityError(NOT_A_SAVED_FILE.format(label=label, path=path))
    return path


def canonical_text(text: str) -> str:
    return WHITESPACE.sub(" ", EDITORIAL_MARKER.sub(" ", text)).strip()


def canonical_sha256(text: str) -> str:
    return sha256_bytes(canonical_text(text).encode("utf-8"))


def identity(jurisdiction: str, profile: str, instrument_id: str) -> dict[str, str]:
    values = {
        "jurisdiction": jurisdiction.strip().upper(),
        "profile": profile.strip().lower(),
        "instrument_id": instrument_id.strip(),
    }
    missing = [name for name, value in values.items() if not value]
    if missing:
        raise IntegrityError("Instrument identity is missing: " + ", ".join(missing))
    return values


def require_identity(value: object) -> dict[str, str]:
    if not isinstance(value, dict):
        raise IntegrityError("No stable instrument identity is recorded.")
    return identity(*(str(value.get(field, "")) for field in IDENTITY_FIELDS))


DESTINATION_OCCUPIED = (
    "Destination is already occupied: {name}. "
    "Use a new destination so the earlier record remains unchanged."
)


def check_destination_free(destination: Path) -> None:
    """Refuse an occupied destination before any work is done for it."""
    if destination.exists():
        raise IntegrityError(DESTINATION_OCCUPIED.format(name=destination.name))


def reserve_destination(destination: Path) -> None:
    """Claim the destination atomically, immediately before the first write."""
    try:
        destination.mkdir(parents=True, exist_ok=False)
    except FileExistsError as error:
        raise IntegrityError(
            DESTINATION_OCCUPIED.format(name=destination.name)
        ) from error


def fetch_integrity(source_bytes: bytes, instrument_identity: dict[str, str]) -> dict:
    return {
        "schema": SCHEMA,
        "instrument": require_identity(instrument_identity),
        "publisher_bytes_sha256": sha256_bytes(source_bytes),
    }


def _read_json(path: Path, label: str) -> dict:
    if not path.is_file():
        raise IntegrityError(f"Missing {label}: {path.name}")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise IntegrityError(f"Unreadable {label}: {path.name}: {error}") from error
    if not isinstance(value, dict):
        raise IntegrityError(f"Invalid {label}: {path.name}")
    return value


def validate_fetch(directory: Path) -> tuple[dict, Path, dict[str, str]]:
    fetch = _read_json(directory / "fetch.json", "fetch receipt")
    record = fetch.get("integrity")
    if not isinstance(record, dict) or record.get("schema") != SCHEMA:
        raise IntegrityError("The fetch receipt has no supported integrity record.")
    instrument_identity = require_identity(record.get("instrument"))
    saved_name = fetch.get("saved_as")
    if not isinstance(saved_name, str) or Path(saved_name).name != saved_name:
        raise IntegrityError("The fetch receipt has an invalid saved source name.")
    source_path = directory / saved_name
    actual = sha256_file(source_path)
    expected = record.get("publisher_bytes_sha256")
    if actual != expected or fetch.get("sha256") != expected:
        raise IntegrityError("Saved publisher text changed after retrieval.")
    return fetch, source_path, instrument_identity


def validate_extraction_input(directory: Path, instrument: Path) -> dict:
    fetch, publisher_path, instrument_identity = validate_fetch(directory)
    input_hash = sha256_file(instrument)
    publisher_hash = fetch["integrity"]["publisher_bytes_sha256"]
    if instrument.resolve() == publisher_path.resolve():
        transformation = {"kind": "direct", "input_name": instrument.name}
    else:
        receipt = _read_json(
            directory / "transformation.json", "transformation receipt"
        )
        if receipt.get("schema") != SCHEMA:
            raise IntegrityError(
                "The transformation receipt uses an unsupported schema."
            )
        if receipt.get("publisher_bytes_sha256") != publisher_hash:
            raise IntegrityError(
                "The transformation receipt names different publisher bytes."
            )
        if receipt.get("derived_text_sha256") != input_hash:
            raise IntegrityError("Derived text changed after transformation.")
        if receipt.get("derived_name") != instrument.name:
            raise IntegrityError(
                "The transformation receipt names a different derived file."
            )
        transformation = {
            "kind": "derived",
            "input_name": instrument.name,
            "receipt": receipt,
        }
    return {
        "schema": SCHEMA,
        "instrument": instrument_identity,
        "publisher_name": publisher_path.name,
        "publisher_bytes_sha256": publisher_hash,
        "extraction_input_sha256": input_hash,
        "transformation": transformation,
    }


def version_state(
    findings: list[dict], historical_effective: str | None, research_date: str | None
) -> str:
    if bool(historical_effective) != bool(research_date):
        raise IntegrityError("Historical selection requires both dates.")
    if historical_effective and research_date:
        try:
            effective, research = (
                date.fromisoformat(historical_effective),
                date.fromisoformat(research_date),
            )
        except ValueError as error:
            raise IntegrityError("Historical dates must be ISO YYYY-MM-DD.") from error
        if effective > research:
            raise IntegrityError(
                "Historical effective date is after the research date."
            )
    if any(item.get("severity") == "incomplete" for item in findings):
        return BLOCKED
    if not findings:
        return UNRESOLVED
    if historical_effective and research_date:
        return HISTORICAL_SELECTED
    if any(item.get("severity") == "superseded" for item in findings):
        return BLOCKED
    # Furniture/disclaimers do not identify the selected version.
    incidental = {
        "revised-may-not-be-current",
        "prospective-provisions",
        "ecfr-unofficial",
    }
    if all(item.get("marker") in incidental for item in findings):
        return UNRESOLVED
    return CONFIRMED


def validate_version(directory: Path, chain: dict) -> dict:
    version = _read_json(directory / "version.json", "version receipt")
    record = version.get("integrity")
    if not isinstance(record, dict) or record.get("schema") != SCHEMA:
        raise IntegrityError("The version receipt has no supported integrity record.")
    if require_identity(record.get("instrument")) != chain["instrument"]:
        raise IntegrityError("The version receipt belongs to a different instrument.")
    for field in ("publisher_bytes_sha256", "extraction_input_sha256"):
        if record.get(field) != chain[field]:
            raise IntegrityError(
                "The version receipt is bound to different source text."
            )
    if version.get("state") not in RELIANCE_STATES:
        raise IntegrityError(
            "The operative version is unresolved; downstream reliance is blocked."
        )
    expected_state = version_state(
        version.get("findings") or [],
        version.get("effective_date"),
        version.get("research_date"),
    )
    if expected_state != version["state"]:
        raise IntegrityError(
            "Version state conflicts with its findings or historical dates."
        )
    return version


def provision_set_sha256(provisions: list[dict]) -> str:
    records = []
    for provision in provisions:
        if "text" in provision and canonical_sha256(provision["text"]) != provision.get(
            "sha256"
        ):
            raise IntegrityError(
                "Extracted text changed for "
                f"{provision.get('id', 'unknown provision')}."
            )
        records.append(
            {
                key: provision.get(key)
                for key in ("id", "label", "heading", "class", "sha256")
            }
        )
    encoded = json.dumps(records, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return sha256_bytes(encoded)


def extraction_integrity(chain: dict, version: dict, provisions: list[dict]) -> dict:
    return {
        **chain,
        "version_state": version["state"],
        "version_effective_date": version.get("effective_date"),
        "research_date": version.get("research_date"),
        "provision_set_sha256": provision_set_sha256(provisions),
    }


def validate_extraction(payload: dict, directory: Path) -> dict:
    record = payload.get("integrity")
    if not isinstance(record, dict) or record.get("schema") != SCHEMA:
        raise IntegrityError("The extraction has no supported integrity record.")
    input_name = record.get("transformation", {}).get("input_name")
    if not isinstance(input_name, str) or Path(input_name).name != input_name:
        raise IntegrityError("The extraction records an invalid source name.")
    chain = validate_extraction_input(directory, directory / input_name)
    version = validate_version(directory, chain)
    expected = extraction_integrity(chain, version, payload.get("provisions") or [])
    if record != expected:
        raise IntegrityError(
            "The extraction no longer matches its source and version chain."
        )
    return record


def require_same_instrument(before: dict, after: dict) -> None:
    if require_identity(before.get("instrument")) != require_identity(
        after.get("instrument")
    ):
        raise IntegrityError(
            "These records identify different instruments; no comparison was made."
        )
