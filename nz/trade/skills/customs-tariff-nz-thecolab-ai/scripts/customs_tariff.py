"""Bounded fetch, validation and query helpers for NZ Customs tariff data."""
from __future__ import annotations

import csv
import datetime as dt
import decimal
import functools
import gzip
import http.client
import io
import re
import tarfile
import urllib.error
import urllib.parse
import urllib.request
import zlib
from collections.abc import Iterator
from dataclasses import dataclass

LANDING_URL = "https://www.customs.govt.nz/business/tariffs/tariff-classifications-and-rates/"
ARCHIVE_URL = "https://www.customs.govt.nz/media/0nmaamqd/tariff.tar.gz"
ALLOWED_HOST = "www.customs.govt.nz"
DEFAULT_TIMEOUT = 10
MAX_DOWNLOAD_BYTES = 16 * 1024 * 1024
MAX_MEMBER_BYTES = 128 * 1024 * 1024
MAX_ARCHIVE_BYTES = 256 * 1024 * 1024
MAX_ARCHIVE_MEMBERS = 32
MAX_DECOMPRESSED_BYTES = MAX_ARCHIVE_BYTES + 4 * 1024 * 1024

DETAILS = "Tariff_Details.csv"
RATES = "Tariff_Rates.csv"
LEVIES = "Tariff_Levies.csv"
FORMULAS = "Tariff_Levy_Formulas.csv"
TIMESTAMP = "time_stamp.txt"

HEADERS = {
    DETAILS: (
        "Tic Tariff Level 1", "Tic Tariff Level 2", "Tic Tariff Level 3",
        "Tic Tariff Level 4", "Tic Tariff Level 5", "Tic Tariff Letter",
        "Tic Tariff Section", "Tic Statistical Unit", "Tic Supplementary Unit",
        "Tic Alternate Tariff Item", "Tic Alternate Ind", "Tic Gst Exempt Ind",
        "Tic Start Date", "Tic Expiry Date", "Tic Tariff Description",
    ),
    RATES: (
        "Tdrc Tariff Level 1", "Tdrc Tariff Level 2", "Tdrc Tariff Level 3",
        "Tdrc Tariff Level 4", "Tdrc Tariff Level 5", "Tdrc Rate Group",
        "Tdrc Start Date", "Tdrc Expiry Date", "Tdrc Excise Factor",
        "Tdrc Rate Formula", "Tdrc Factor A", "Tdrc Factor B", "Tdrc Factor C",
        "Tdrc Factor D", "Tdrc Factor E", "Tdrc Factor F",
    ),
    LEVIES: (
        "Tlrc Tariff Level 1", "Tlrc Tariff Level 2", "Tlrc Tariff Level 3",
        "Tlrc Tariff Level 4", "Tlrc Tariff Level 5", "Tlrc Levy Type Code",
        "Tlrc Levy Formula Code", "Tlrc Start Date", "Tlrc Expiry Date",
    ),
    FORMULAS: ("Lfc Levy Formula Codes", "Lfc Levy Formula Rate"),
}

DUTY_FORMULA_SUMMARIES = {
    "1": "Free",
    "2": "Manual calculation required",
    "3": "Factor A multiplied by value for duty divided by 100",
    "4": "Factor A multiplied by quantity",
    "5": "Value-based Factor A component plus quantity-based Factor B component",
}

ASCII_DIGITS_RE = re.compile(r"[0-9]+")
ASCII_TWO_DIGITS_RE = re.compile(r"[0-9]{2}")
ASCII_CODE_RE = re.compile(r"[A-Z0-9]+")


class SkillError(RuntimeError):
    """Expected CLI failure with a stable repository exit code."""

    def __init__(self, message: str, *, exit_code: int, kind: str):
        super().__init__(message)
        self.exit_code = exit_code
        self.kind = kind


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _clean(value: str | None) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


@functools.lru_cache(maxsize=512)
def parse_date(value: str) -> dt.date | None:
    text = _clean(value)
    if not text:
        return None
    for pattern in ("%b %d %Y %I:%M%p", "%Y-%m-%d %I:%M %p", "%Y-%m-%d"):
        try:
            return dt.datetime.strptime(text, pattern).replace(tzinfo=dt.timezone.utc).date()
        except ValueError:
            pass
    raise SkillError(f"unrecognised source date: {value!r}", exit_code=6, kind="source_schema")


def parse_as_of(value: str) -> dt.date:
    try:
        return dt.date.fromisoformat(value)
    except ValueError as exc:
        raise SkillError("--as-of must be an ISO date (YYYY-MM-DD)", exit_code=2, kind="invalid_input") from exc


def parse_source_timestamp(value: str) -> str:
    text = _clean(value)
    match = re.fullmatch(
        r"[A-Za-z]{3} ([A-Za-z]{3}) (\d{1,2}) (\d{1,2}:\d{2}:\d{2}) (AM|PM) (NZST|NZDT) (\d{4})",
        text,
    )
    if not match:
        raise SkillError(f"unrecognised archive timestamp: {text!r}", exit_code=6, kind="source_schema")
    month, day, clock, am_pm, zone_name, year = match.groups()
    parsed = dt.datetime.strptime(
        f"{month} {day} {year} {clock} {am_pm}", "%b %d %Y %I:%M:%S %p"
    ).replace(tzinfo=dt.timezone.utc)
    offset = dt.timedelta(hours=12 if zone_name == "NZST" else 13)
    return parsed.replace(tzinfo=dt.timezone(offset)).isoformat(timespec="seconds")


def normalise_code(value: str, *, exact: bool) -> str:
    compact = re.sub(r"[.\s-]+", "", value.strip()).upper()
    if re.fullmatch(r"[0-9]+", compact) is None or not (
        len(compact) == 10 if exact else 1 <= len(compact) <= 10
    ):
        requirement = "a 10-digit tariff item" if exact else "a 1-to-10 digit tariff-code prefix"
        raise SkillError(f"expected {requirement}", exit_code=2, kind="invalid_input")
    return compact


def format_code(code: str) -> str:
    return ".".join(code[index:index + 2] for index in range(0, 10, 2))


def _is_active(start: str, expiry: str, as_of: dt.date) -> bool:
    start_date = parse_date(start)
    expiry_date = parse_date(expiry)
    return (start_date is None or start_date <= as_of) and (expiry_date is None or as_of <= expiry_date)


def _source_date(value: str) -> str | None:
    parsed = parse_date(value)
    return parsed.isoformat() if parsed else None


def _source_tariff_code(row: dict[str, str], *, prefix: str, table: str) -> str:
    levels = [row[f"{prefix} Tariff Level {level}"] for level in range(1, 6)]
    for level, value in enumerate(levels, start=1):
        if ASCII_TWO_DIGITS_RE.fullmatch(value) is None:
            raise SkillError(
                f"invalid tariff level {level} in {table}: {value!r}",
                exit_code=6,
                kind="source_schema",
            )
    return "".join(levels)


def _required_source_digits(value: str, *, field: str, table: str) -> str:
    if ASCII_DIGITS_RE.fullmatch(value) is None:
        raise SkillError(
            f"invalid {field} in {table}: {value!r}",
            exit_code=6,
            kind="source_schema",
        )
    return value


def _source_decimal(value: str, *, field: str, table: str, required: bool = False) -> str:
    if not value and not required:
        return value
    try:
        parsed = decimal.Decimal(value)
    except decimal.InvalidOperation as exc:
        raise SkillError(
            f"invalid {field} in {table}: {value!r}",
            exit_code=6,
            kind="source_schema",
        ) from exc
    if not parsed.is_finite():
        raise SkillError(
            f"invalid {field} in {table}: {value!r}",
            exit_code=6,
            kind="source_schema",
        )
    return value


@dataclass(frozen=True)
class TariffArchive:
    blob: bytes
    source_url: str
    retrieved_at: str
    source_timestamp: str
    http_last_modified: str | None = None

    def _iter_csv(self, name: str) -> Iterator[dict[str, str]]:
        try:
            with tarfile.open(fileobj=io.BytesIO(self.blob), mode="r:gz") as archive:
                member = archive.getmember(name)
                raw = archive.extractfile(member)
                if raw is None:
                    raise SkillError(f"archive member is not readable: {name}", exit_code=6, kind="source_schema")
                with io.TextIOWrapper(raw, encoding="cp1252", newline="") as text:
                    # Customs uses balanced literal quotes inside unquoted fields, so treat
                    # quotes as data while still rejecting an unclosed quote on any row.
                    def strict_source_lines() -> Iterator[str]:
                        for physical_line_number, line in enumerate(text, start=1):
                            if line.count('"') % 2:
                                raise SkillError(
                                    f"unclosed quoted field in {name} line {physical_line_number}",
                                    exit_code=6,
                                    kind="source_schema",
                                )
                            yield line

                    reader = csv.DictReader(
                        strict_source_lines(),
                        delimiter="~",
                        quoting=csv.QUOTE_NONE,
                        strict=True,
                    )
                    if tuple(reader.fieldnames or ()) != HEADERS[name]:
                        raise SkillError(f"unexpected header in {name}", exit_code=6, kind="source_schema")
                    for line_number, row in enumerate(reader, start=2):
                        if None in row or any(value is None for value in row.values()):
                            raise SkillError(
                                f"unexpected field count in {name} line {line_number}",
                                exit_code=6,
                                kind="source_schema",
                            )
                        cleaned = {key: _clean(value) for key, value in row.items()}
                        if not any(cleaned.values()):
                            raise SkillError(
                                f"empty record in {name} line {line_number}",
                                exit_code=6,
                                kind="source_schema",
                            )
                        yield cleaned
        except SkillError:
            raise
        except (KeyError, UnicodeDecodeError, csv.Error, tarfile.TarError, OSError) as exc:
            raise SkillError(f"could not parse {name}: {exc}", exit_code=6, kind="source_schema") from exc

    def iter_details(self) -> Iterator[dict[str, object]]:
        for row in self._iter_csv(DETAILS):
            code = _source_tariff_code(row, prefix="Tic", table=DETAILS)
            yield {
                "tariff_code": code,
                "display_code": format_code(code),
                "check_letter": row["Tic Tariff Letter"],
                "section": row["Tic Tariff Section"],
                "statistical_unit": row["Tic Statistical Unit"],
                "supplementary_unit": row["Tic Supplementary Unit"],
                "alternate_tariff_item": row["Tic Alternate Tariff Item"],
                "alternate_indicator": row["Tic Alternate Ind"],
                "gst_exempt_indicator": row["Tic Gst Exempt Ind"],
                "start_date": _source_date(row["Tic Start Date"]),
                "expiry_date": _source_date(row["Tic Expiry Date"]),
                "description": row["Tic Tariff Description"],
                "_start": row["Tic Start Date"],
                "_expiry": row["Tic Expiry Date"],
            }

    @property
    def details(self) -> list[dict[str, object]]:
        return list(self.iter_details())

    def iter_rates(self) -> Iterator[dict[str, object]]:
        for row in self._iter_csv(RATES):
            code = _source_tariff_code(row, prefix="Tdrc", table=RATES)
            formula_code = _required_source_digits(
                row["Tdrc Rate Formula"],
                field="duty formula code",
                table=RATES,
            )
            excise_factor = _source_decimal(
                row["Tdrc Excise Factor"],
                field="excise factor",
                table=RATES,
            )
            for letter in "ABCDEF":
                _source_decimal(
                    row[f"Tdrc Factor {letter}"],
                    field=f"Factor {letter}",
                    table=RATES,
                )
            factors = {
                letter.lower(): row[f"Tdrc Factor {letter}"]
                for letter in "ABCDEF"
                if row[f"Tdrc Factor {letter}"]
            }
            yield {
                "tariff_code": code,
                "rate_group": row["Tdrc Rate Group"],
                "start_date": _source_date(row["Tdrc Start Date"]),
                "expiry_date": _source_date(row["Tdrc Expiry Date"]),
                "excise_factor": excise_factor or None,
                "formula_code": formula_code,
                "formula_summary": DUTY_FORMULA_SUMMARIES.get(formula_code),
                "factors": factors,
                "_start": row["Tdrc Start Date"],
                "_expiry": row["Tdrc Expiry Date"],
            }

    def iter_levies(self) -> Iterator[dict[str, object]]:
        for row in self._iter_csv(LEVIES):
            code = _source_tariff_code(row, prefix="Tlrc", table=LEVIES)
            levy_type_code = row["Tlrc Levy Type Code"]
            if ASCII_CODE_RE.fullmatch(levy_type_code) is None:
                raise SkillError(
                    f"invalid levy type code in {LEVIES}: {levy_type_code!r}",
                    exit_code=6,
                    kind="source_schema",
                )
            formula_code = _required_source_digits(
                row["Tlrc Levy Formula Code"],
                field="levy formula reference",
                table=LEVIES,
            )
            yield {
                "tariff_code": code,
                "levy_type_code": levy_type_code,
                "formula_code": formula_code,
                "start_date": _source_date(row["Tlrc Start Date"]),
                "expiry_date": _source_date(row["Tlrc Expiry Date"]),
                "_start": row["Tlrc Start Date"],
                "_expiry": row["Tlrc Expiry Date"],
            }

    def iter_formulas(self) -> Iterator[dict[str, str]]:
        for row in self._iter_csv(FORMULAS):
            formula_code = _required_source_digits(
                row["Lfc Levy Formula Codes"],
                field="formula code",
                table=FORMULAS,
            )
            formula_rate = _source_decimal(
                row["Lfc Levy Formula Rate"],
                field="formula rate",
                table=FORMULAS,
                required=True,
            )
            yield {
                "formula_code": formula_code,
                "formula_rate": formula_rate,
            }


def _validate_gzip_integrity(blob: bytes) -> None:
    """Consume the gzip stream through its footer without materialising it."""
    decompressed_bytes = 0
    with gzip.GzipFile(fileobj=io.BytesIO(blob), mode="rb") as stream:
        while chunk := stream.read(1024 * 1024):
            decompressed_bytes += len(chunk)
            if decompressed_bytes > MAX_DECOMPRESSED_BYTES:
                raise SkillError(
                    "tariff archive expands beyond safety limits",
                    exit_code=6,
                    kind="source_schema",
                )


def parse_archive(
    blob: bytes,
    source_url: str,
    retrieved_at: str,
    http_last_modified: str | None = None,
) -> TariffArchive:
    if len(blob) > MAX_DOWNLOAD_BYTES:
        raise SkillError("tariff archive exceeds the 16 MiB download limit", exit_code=6, kind="source_schema")
    try:
        _validate_gzip_integrity(blob)
        with tarfile.open(fileobj=io.BytesIO(blob), mode="r:gz") as archive:
            files: list[tarfile.TarInfo] = []
            names: list[str] = []
            total_size = 0
            for count, member in enumerate(archive, start=1):
                if count > MAX_ARCHIVE_MEMBERS:
                    raise SkillError("tariff archive has too many members", exit_code=6, kind="source_schema")
                if not member.isfile():
                    continue
                files.append(member)
                names.append(member.name)
                total_size += member.size
            required = {TIMESTAMP, *HEADERS}
            missing = sorted(required - set(names))
            duplicates = sorted(name for name in required if names.count(name) > 1)
            if missing:
                raise SkillError(f"tariff archive is missing: {', '.join(missing)}", exit_code=6, kind="source_schema")
            if duplicates:
                raise SkillError(f"tariff archive has duplicate members: {', '.join(duplicates)}", exit_code=6, kind="source_schema")
            if any(member.size > MAX_MEMBER_BYTES for member in files) or total_size > MAX_ARCHIVE_BYTES:
                raise SkillError("tariff archive expands beyond safety limits", exit_code=6, kind="source_schema")
            stamp_file = archive.extractfile(TIMESTAMP)
            if stamp_file is None:
                raise SkillError("archive timestamp is unreadable", exit_code=6, kind="source_schema")
            source_timestamp = parse_source_timestamp(stamp_file.read(256).decode("ascii"))
    except SkillError:
        raise
    except (tarfile.TarError, UnicodeDecodeError, csv.Error, EOFError, OSError, zlib.error) as exc:
        raise SkillError(f"invalid tariff archive: {exc}", exit_code=6, kind="source_schema") from exc
    result = TariffArchive(blob, source_url, retrieved_at, source_timestamp, http_last_modified)
    tables = (
        (DETAILS, result.iter_details()),
        (RATES, result.iter_rates()),
        (FORMULAS, result.iter_formulas()),
        (LEVIES, result.iter_levies()),
    )
    formula_codes: set[str] = set()
    for name, records in tables:
        has_records = False
        for record in records:
            has_records = True
            if name == FORMULAS:
                formula_codes.add(str(record["formula_code"]))
            elif name == LEVIES and str(record["formula_code"]) not in formula_codes:
                raise SkillError(
                    f"unknown levy formula reference in {LEVIES}: {record['formula_code']!r}",
                    exit_code=6,
                    kind="source_schema",
                )
        if not has_records:
            raise SkillError(f"required table has no data rows: {name}", exit_code=6, kind="source_schema")
    return result


def _validate_archive_url(url: str) -> None:
    try:
        parsed = urllib.parse.urlparse(url)
        port = parsed.port
    except ValueError as exc:
        raise SkillError("archive redirect URL is invalid", exit_code=7, kind="unsafe_redirect") from exc
    if (
        parsed.scheme != "https"
        or parsed.hostname != ALLOWED_HOST
        or parsed.username is not None
        or parsed.password is not None
        or port not in {None, 443}
    ):
        raise SkillError("archive redirected outside the declared Customs host", exit_code=7, kind="unsafe_redirect")


class ArchiveRedirectHandler(urllib.request.HTTPRedirectHandler):
    """Reject off-host redirects before urllib can issue the next request."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        _validate_archive_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def fetch_archive(timeout: int = DEFAULT_TIMEOUT) -> TariffArchive:
    if not 1 <= timeout <= DEFAULT_TIMEOUT:
        raise SkillError("timeout must be between 1 and 10 seconds", exit_code=2, kind="invalid_input")
    request = urllib.request.Request(
        ARCHIVE_URL,
        headers={"Accept": "application/gzip, application/octet-stream;q=0.9", "User-Agent": "customs-tariff-nz/1.0"},
    )
    try:
        opener = urllib.request.build_opener(ArchiveRedirectHandler())
        with opener.open(request, timeout=timeout) as response:
            final_url = response.geturl()
            _validate_archive_url(final_url)
            content_length = response.headers.get("Content-Length")
            declared_length = int(content_length) if content_length else None
            if declared_length is not None and declared_length > MAX_DOWNLOAD_BYTES:
                raise SkillError("tariff archive exceeds the 16 MiB download limit", exit_code=6, kind="source_schema")
            blob = response.read(MAX_DOWNLOAD_BYTES + 1)
            if declared_length is not None and len(blob) != declared_length:
                raise SkillError(
                    "Customs archive transfer length did not match the declared content length",
                    exit_code=5,
                    kind="upstream_unavailable",
                )
            last_modified = response.headers.get("Last-Modified")
    except urllib.error.HTTPError as exc:
        if exc.code in {403, 429}:
            raise SkillError(f"Customs archive request was blocked (HTTP {exc.code})", exit_code=4, kind="blocked") from exc
        raise SkillError(f"Customs archive returned HTTP {exc.code}", exit_code=5, kind="upstream_unavailable") from exc
    except SkillError:
        raise
    except (urllib.error.URLError, http.client.HTTPException, TimeoutError, OSError, ValueError) as exc:
        raise SkillError(f"Customs archive is unavailable: {exc}", exit_code=5, kind="upstream_unavailable") from exc
    return parse_archive(blob, final_url, utc_now(), last_modified)


def _public(record: dict[str, object]) -> dict[str, object]:
    return {key: value for key, value in record.items() if not key.startswith("_")}


def search_records(archive: TariffArchive, query: str, as_of_value: str, limit: int) -> list[dict[str, object]]:
    query = validate_search_query(query)
    as_of = parse_as_of(as_of_value)
    numeric = re.fullmatch(r"[0-9.\s-]+", query) is not None
    code_prefix = normalise_code(query, exact=False) if numeric else None
    words = query.casefold().split()
    matches: list[dict[str, object]] = []
    for record in archive.iter_details():
        if not _is_active(str(record["_start"]), str(record["_expiry"]), as_of):
            continue
        code_match = code_prefix is not None and str(record["tariff_code"]).startswith(code_prefix)
        text_match = code_prefix is None and all(word in str(record["description"]).casefold() for word in words)
        if code_match or text_match:
            matches.append(_public(record))
            if len(matches) >= limit:
                break
    return matches


def validate_search_query(query: str) -> str:
    query = _clean(query)
    if not query:
        raise SkillError("search query must not be blank", exit_code=2, kind="invalid_input")
    numeric = re.fullmatch(r"[\d.\s-]+", query) is not None
    if numeric:
        normalise_code(query, exact=False)
    return query


def lookup_records(archive: TariffArchive, code_value: str, as_of_value: str) -> dict[str, object]:
    code = normalise_code(code_value, exact=True)
    as_of = parse_as_of(as_of_value)
    classifications = [
        _public(record)
        for record in archive.iter_details()
        if record["tariff_code"] == code and _is_active(str(record["_start"]), str(record["_expiry"]), as_of)
    ]
    rates = [
        _public(record)
        for record in archive.iter_rates()
        if record["tariff_code"] == code and _is_active(str(record["_start"]), str(record["_expiry"]), as_of)
    ]
    levies = [
        _public(record)
        for record in archive.iter_levies()
        if record["tariff_code"] == code and _is_active(str(record["_start"]), str(record["_expiry"]), as_of)
    ]
    formula_codes = {str(record["formula_code"]) for record in levies}
    formula_rates = {record["formula_code"]: record["formula_rate"] for record in archive.iter_formulas() if record["formula_code"] in formula_codes}
    for levy in levies:
        levy["formula_rate"] = formula_rates.get(str(levy["formula_code"]))
    return {
        "tariff_code": code,
        "display_code": format_code(code),
        "as_of": as_of.isoformat(),
        "classification": classifications[0] if classifications else None,
        "classifications": classifications,
        "rates": rates,
        "levies": levies,
    }


def validate_formula_code(code_value: str) -> str:
    query = code_value.strip()
    if query and ASCII_DIGITS_RE.fullmatch(query) is None:
        raise SkillError("formula code must contain digits only", exit_code=2, kind="invalid_input")
    return query


def formula_records(
    archive: TariffArchive,
    code_value: str,
    limit: int,
    *,
    prefix: bool = False,
) -> list[dict[str, str]]:
    query = validate_formula_code(code_value)
    rows = [
        row
        for row in archive.iter_formulas()
        if not query or (row["formula_code"].startswith(query) if prefix else row["formula_code"] == query)
    ]
    rows.sort(key=lambda row: (int(row["formula_code"]), row["formula_code"]))
    return rows[:limit]
