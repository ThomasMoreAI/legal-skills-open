#!/usr/bin/env python3
"""Query Public Service Commission six-monthly OIA compliance statistics.

No auth, no browser automation, stdlib-only HTTP/CSV parsing.
"""
from __future__ import annotations

import argparse
import csv
import html
import io
import hashlib
import os
import tempfile
import time
import unicodedata
import zipfile
from concurrent.futures import ThreadPoolExecutor
import json
import pathlib
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from typing import Any

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "lib"))
import nzfetch  # noqa: E402
from oia_workbooks import MAX_BYTES, parse_release

UA = "oia-statistics-nz/1.0 (+https://github.com/thecolab-ai/.skills)"
LANDING_URL = "https://www.publicservice.govt.nz/data/oia-statistics"
CSV_URLS = [
    "https://www.publicservice.govt.nz/assets/DirectoryFile/v_OIAStatisticsAllDataResults-1.csv",
    "https://www.publicservice.govt.nz/assets/v_OIAStatisticsAllDataResults-1.csv",
]
DEFAULT_TIMEOUT = 10
CACHE_DIR = pathlib.Path(__file__).resolve().parents[1] / ".cache"
CACHE_TTL = 24 * 60 * 60
RECOVERY_WARNINGS = []
RECOVERY_SOURCES = {}
UNMATCHED_IDENTITY_WARNING = ('No stable PSC OrgID: this official release record did not match the all-data CSV; '
                              'counts and date come from the release workbook. Use the exact agency name.')


class UpstreamUnavailable(RuntimeError):
    """Raised when PSC upstream cannot be reached in a blocking/outage state."""


def die(message: str, code: int = 1) -> None:
    print(f"oia-statistics-nz: {message}", file=sys.stderr)
    raise SystemExit(code)


def fetch_text(url: str, timeout: int) -> str:
    try:
        return nzfetch.fetch_text(
            url,
            timeout=timeout,
            accept="text/html,*/*;q=0.9",
            headers={"Accept-Language": "en-NZ,en;q=0.9"},
        )
    except nzfetch.Blocked as exc:
        raise UpstreamUnavailable(f"network error fetching {url}: {exc}") from exc
    except nzfetch.FetchError as exc:
        raise UpstreamUnavailable(str(exc)) from exc


def load_csv_rows(timeout: int) -> tuple[list[dict[str, str]], str]:
    last_error = None
    for csv_url in CSV_URLS:
        try:
            raw, _ct, source = nzfetch.fetch_bytes(
                csv_url,
                timeout=timeout,
                accept="text/csv,application/csv,text/plain,*/*;q=0.8",
                headers={"Accept-Language": "en-NZ,en;q=0.9"},
            )
            try:
                decoded = raw.decode("utf-8-sig")
            except UnicodeDecodeError:
                decoded = raw.decode("cp1252", "replace")
            reader = csv.DictReader(io.StringIO(decoded))
            if not {'OrgID', 'Agency', 'SurveyPeriodEndDate', 'OIA_RequestsHandled'} <= set(reader.fieldnames or []):
                raise ValueError('OIA CSV header schema changed')
            rows = [row for row in reader if row]
            if rows:
                return rows, source
            raise UpstreamUnavailable(f"{csv_url} returned no rows")
        except nzfetch.Blocked as exc:
            last_error = f"network error fetching {csv_url}: {exc}"
        except nzfetch.FetchError as exc:
            last_error = str(exc)
        except csv.Error as exc:
            last_error = f"invalid CSV from {csv_url}: {exc}"

    raise UpstreamUnavailable(last_error or f"Unable to load OIA CSV from {', '.join(CSV_URLS)}")


def _first(row: dict[str, str], *keys: str) -> str:
    for key in keys:
        if key in row and row[key] not in (None, ""):
            return str(row[key]).strip()
    return ""


def _as_int(value: Any) -> int | None:
    if value is None:
        return None
    text = str(value).strip().replace(",", "")
    if not text:
        return None
    try:
        return int(round(float(text)))
    except ValueError:
        return None


def _as_float(value: Any) -> float | None:
    if value is None:
        return None
    text = str(value).strip().replace(",", "")
    if not text:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def _as_percent(value: Any) -> float | None:
    raw = _as_float(value)
    if raw is None:
        return None
    if raw < 0:
        return 0.0
    if raw <= 1:
        return round(raw * 100.0, 4)
    return round(raw, 4)


def _norm_period(raw: str | None) -> str:
    if not raw:
        return ""
    match = re.match(r"^\s*(\d{4}-\d{2}-\d{2})", str(raw).strip())
    if not match:
        return ""
    try:
        datetime.strptime(match.group(1), "%Y-%m-%d")
    except ValueError:
        return ""
    return match.group(1)


def parse_period_arg(value: str | None, available: set[str]) -> str:
    if not value:
        raise ValueError("--period requires a value")
    normalized = value.strip()
    if normalized.lower() == "latest":
        if not available:
            raise ValueError("no periods available")
        return sorted(available)[-1]

    match = re.match(r"^(\d{4})-(\d{2})-(\d{2})$", normalized)
    if match:
        period = match.group(0)
        if period in available:
            return period

    match = re.match(r"^(\d{4})-(\d{2})$", normalized)
    if match:
        year, month = match.groups()
        if month in {"06", "12"}:
            period = f"{year}-{month}-30" if month == "06" else f"{year}-{month}-31"
            if period in available:
                return period

    match = re.match(r"^(\d{4})[-_/\s]?H([12])$", normalized, re.IGNORECASE)
    if match:
        year, half = match.groups()
        period = f"{year}-06-30" if half == "1" else f"{year}-12-31"
        if period in available:
            return period

    raise ValueError("period must be latest, YYYY-MM-DD, YYYY-06, YYYY-12, YYYY-H1, or YYYY-H2")


def period_label(period_end: str) -> str:
    try:
        parsed = datetime.strptime(period_end, "%Y-%m-%d")
    except ValueError:
        return period_end
    return f"{parsed.year} {'Jan-Jun' if parsed.month == 6 else 'Jul-Dec' if parsed.month == 12 else period_end}"


def _rows_by_period(rows: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    grouped = defaultdict(list)
    for row in rows:
        period_end = _norm_period(_first(row, "SurveyPeriodEndDate"))
        if not period_end:
            continue
        grouped[period_end].append(row)
    return grouped


def row_enriched(row: dict[str, str]) -> dict[str, object]:
    period_end = _norm_period(_first(row, "SurveyPeriodEndDate"))
    handled = _as_int(_first(row, "OIA_RequestsHandled")) or 0
    # A blank on-time cell means the agency did not report it (e.g. NZ Police
    # Jul-Dec 2018); it must stay null rather than read as 0% on time.
    timely = _as_int(_first(row, "OIAs_CompletedWithinTimeframe"))
    completed_pct = _as_percent(_first(row, "Percent_OIAs_CompletedWithinTimeframe"))
    refused = _as_int(_first(row, "OIA_refused"))
    refusals_pct = _as_percent(_first(row, "Percent_OIAs_refused", "Percent_OIA_refused"))
    extension_pct = _as_percent(_first(row, "Percent_OIA_extension", "Percent_OIAs_extension"))
    transfer_pct = _as_percent(_first(row, "Percent_OIA_transfer", "Percent_OIAs_transfer"))

    return {
        **({"source_url": row['_source_url'], "publisher": "Public Service Commission",
            "retrieved_at": row['_retrieved_at'], "latest_data": period_end} if row.get('_source_url') else {}),
        **({'identity_warning': row['_identity_warning']} if row.get('_identity_warning') else {}),
        "org_id": _as_int(_first(row, "OrgID")),
        "agency": _first(row, "Agency"),
        "agency_preferred_name": _first(row, "Agency_Preffered_Name", "Agency_Preferred_Name"),
        "agency_type": _first(row, "Agency_Type"),
        "survey_period_end": period_end,
        "period_label": period_label(period_end),
        "requests_handled": handled,
        "requests_completed_within_timeframe": timely,
        "timeliness_pct": completed_pct if completed_pct is not None else (
            round((timely / handled) * 100, 4) if handled and timely is not None else None),
        "responses_published": _as_int(_first(row, "OIAs_Published")) or 0,
        "extensions": _as_int(_first(row, "OIA_extension")) or 0,
        "extensions_pct": extension_pct,
        "transfers": _as_int(_first(row, "OIA_transfer")) or 0,
        "transfers_pct": transfer_pct,
        "refusals": refused or 0,
        "refusals_pct": refusals_pct if refusals_pct is not None else (
            round(refused / handled * 100, 4) if handled and refused is not None else None),
        "complaints": _as_int(_first(row, "Ombudsman_Complaints")) or _as_int(_first(row, "Ombudsman Complaints")) or 0,
        "final_opinions": _as_int(_first(row, "FinalOpinionsbyOmbudsman")) or 0,
        "response_average_days": _as_float(_first(row, "OIA_average")),
        "response_median_days": _as_float(_first(row, "OIA_median")),
    }


def is_agency_row(row: dict[str, str]) -> bool:
    if _first(row, "Agency_Type").lower() == "agency type totals":
        return False
    # Release-workbook records (parse_release already drops total rows) count
    # even when no stable OrgID could be matched from the all-data CSV.
    return bool(_as_int(_first(row, "OrgID"))) or bool(row.get("_source_url") and _first(row, "Agency"))


def agency_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    return [row for row in rows if is_agency_row(row)]


def sort_by_key(rows: list[dict[str, object]], key: str, descending: bool = False) -> list[dict[str, object]]:
    def to_number(value: Any) -> float:
        if value is None:
            return float("-inf") if descending else float("inf")
        if isinstance(value, (int, float)):
            return float(value)
        try:
            return float(value)
        except (TypeError, ValueError):
            return 0.0

    if key == "name":
        return sorted(rows, key=lambda item: str(item.get("agency", "")).lower())
    if key in {"requests", "requests_handled"}:
        return sorted(rows, key=lambda item: to_number(item.get("requests_handled", 0)), reverse=True)
    return sorted(rows, key=lambda item: to_number(item.get(key, 0)), reverse=descending)


def list_agencies(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    """Agencies with a PSC OrgID; release records merged by name count toward their periods."""
    grouped: dict[str, dict[str, Any]] = {}
    inferred = infer_org_ids(rows)
    # Rows with their own OrgID first, so names/types come from the CSV identity.
    for row in sorted(agency_rows(rows), key=lambda item: id(item) in inferred):
        org_id = _as_int(_first(row, "OrgID")) or inferred.get(id(row))
        if not org_id:
            continue
        key = str(org_id)
        bucket = grouped.setdefault(
            key,
            {
                "org_id": org_id,
                "agency": _first(row, "Agency"),
                "agency_preferred_name": _first(row, "Agency_Preffered_Name", "Agency_Preferred_Name"),
                "agency_type": _first(row, "Agency_Type"),
                "periods": set(),
                "period_count": 0,
            },
        )
        period = _norm_period(_first(row, "SurveyPeriodEndDate"))
        if period:
            bucket["periods"].add(period)

    result: list[dict[str, object]] = []
    for item in grouped.values():
        item["period_count"] = len(item["periods"])
        del item["periods"]
        result.append(item)
    return sorted(result, key=lambda item: str(item.get("agency", "")).lower())


def on_time_summary(period_rows: list[dict[str, str]], period_end: str) -> dict[str, Any]:
    """Aggregate on-time counts over agencies that reported them.

    Agencies with a blank on-time count are excluded from both the numerator
    and the denominator, and the coverage is reported explicitly.
    """
    covered_requests = missing_requests = on_time = 0
    covered_agencies = 0
    missing: list[str] = []
    for row in period_rows:
        handled = _as_int(_first(row, "OIA_RequestsHandled")) or 0
        timely = _as_int(_first(row, "OIAs_CompletedWithinTimeframe"))
        if timely is None:
            missing_requests += handled
            missing.append(_first(row, "Agency"))
            continue
        covered_agencies += 1
        covered_requests += handled
        on_time += timely
    coverage = {
        "agency_count": covered_agencies,
        "requests_handled": covered_requests,
        "missing_agency_count": len(missing),
        "missing_requests_handled": missing_requests,
        "missing_agencies": sorted(missing, key=str.lower),
    }
    warning = None
    if missing:
        warning = (f"{len(missing)} {'agency' if len(missing) == 1 else 'agencies'} ({missing_requests} requests) "
                   f"reported no on-time count for "
                   f"{period_end} ({', '.join(coverage['missing_agencies'][:5])}"
                   f"{', ...' if len(missing) > 5 else ''}); on-time totals and percentages cover "
                   f"{covered_agencies} agencies and {covered_requests} of {covered_requests + missing_requests} requests.")
    return {
        "requests_completed_within_timeframe": on_time if covered_agencies else None,
        "timeliness_pct": round((on_time / covered_requests) * 100, 4) if covered_requests else None,
        "on_time_coverage": coverage,
        "warning": warning,
    }


def periods_summary(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    grouped = _rows_by_period(rows)
    items: list[dict[str, object]] = []
    for period_end, raw_period_rows in grouped.items():
        period_rows = agency_rows(raw_period_rows)
        requests = sum((_as_int(_first(row, "OIA_RequestsHandled")) or 0) for row in period_rows)
        on_time = on_time_summary(period_rows, period_end)
        published = sum((_as_int(_first(row, "OIAs_Published")) or 0) for row in period_rows)
        items.append(
            {
                **({'source_url': period_rows[0]['_source_url'], 'publisher': 'Public Service Commission',
                    'retrieved_at': period_rows[0]['_retrieved_at'], 'latest_data': period_end}
                   if period_rows and period_rows[0].get('_source_url') else {}),
                "period_end": period_end,
                "period_label": period_label(period_end),
                "rows": len(period_rows),
                "agency_count": len({(_first(r, "OrgID"), _first(r, "Agency")) for r in period_rows}),
                "requests_handled": requests,
                "responses_published": published,
                "requests_completed_within_timeframe": on_time["requests_completed_within_timeframe"],
                "timeliness_pct": on_time["timeliness_pct"],
                "on_time_coverage": on_time["on_time_coverage"],
                **({"warning": on_time["warning"]} if on_time["warning"] else {}),
            }
        )
    items.sort(key=lambda item: str(item["period_end"]), reverse=True)
    return items


def _rows_for_period(rows: list[dict[str, str]], period_arg: str | None) -> tuple[list[dict[str, str]], str]:
    by_period = _rows_by_period(rows)
    period = parse_period_arg(period_arg, set(by_period))
    return by_period.get(period, []), period


REUSED_ID_WARNING_PREFIX = 'The published sources reuse'


def _name_key(value: str) -> str:
    """Casefold, strip macrons/diacritics and punctuation; keep the CSV '?' placeholder."""
    text = unicodedata.normalize("NFKD", (value or "").casefold().replace("&", " and "))
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    return " ".join(re.sub(r"[^\w?]", " ", text).split())


def _name_pattern(key: str) -> re.Pattern[str]:
    # The all-data CSV replaces some Māori letters with '?', so each letter of
    # the release name may also match a '?' in a CSV name.
    return re.compile("".join(f"[{re.escape(ch)}?]" if ch.isalpha() else re.escape(ch) for ch in key))


def _has_reused_id(row: dict[str, str]) -> bool:
    return str(row.get("_identity_warning") or "").startswith(REUSED_ID_WARNING_PREFIX)


def infer_org_ids(rows: list[dict[str, str]]) -> dict[int, int]:
    """Map dated release records without an OrgID to an OrgID agency by name.

    Keyed by ``id(row)``. A record is merged only when its normalised name
    equals (or, for names of 12+ characters, is a whole-word part of) the names
    of exactly one OrgID agency, that agency has no record of its own in the
    same period, and no other unmatched record claims the same agency/period.
    """
    names: dict[int, set[str]] = defaultdict(set)
    occupied: set[tuple[int, str]] = set()
    unmatched: list[tuple[dict[str, str], str]] = []
    for row in agency_rows(rows):
        org_id = _as_int(_first(row, "OrgID"))
        period = _norm_period(_first(row, "SurveyPeriodEndDate"))
        if org_id:
            if period:
                occupied.add((org_id, period))
            if not _has_reused_id(row):
                for name in (_first(row, "Agency"), _first(row, "Agency_Preffered_Name", "Agency_Preferred_Name")):
                    if _name_key(name):
                        names[org_id].add(_name_key(name))
        elif period and _name_key(_first(row, "Agency")):
            unmatched.append((row, period))

    claims: dict[tuple[int, str], list[int]] = defaultdict(list)
    for row, period in unmatched:
        key = _name_key(_first(row, "Agency"))
        pattern = _name_pattern(key)
        exact = {org for org, known in names.items() if any(pattern.fullmatch(name) for name in known)}
        within = set()
        if not exact and len(key) >= 12:
            bounded = re.compile(r"(?<![\w?])" + pattern.pattern + r"(?![\w?])")
            within = {org for org, known in names.items() if any(bounded.search(name) for name in known)}
        candidates = exact or within
        if len(candidates) == 1:
            org_id = next(iter(candidates))
            if (org_id, period) not in occupied:
                claims[(org_id, period)].append(id(row))
    return {row_id: org_id for (org_id, _period), row_ids in claims.items() if len(row_ids) == 1
            for row_id in row_ids}


def _agency_identity(row: dict[str, str], inferred: dict[int, int]) -> int | str:
    """Stable OrgID (CSV or name-inferred), else the normalised release name."""
    return _as_int(_first(row, "OrgID")) or inferred.get(id(row)) or "name:" + _name_key(_first(row, "Agency"))


def _match_agency_rows(rows: list[dict[str, str]], query: str,
                       inferred: dict[int, int] | None = None) -> list[dict[str, str]]:
    norm_query = re.sub(r"\s+", " ", query or "").strip().lower()
    if not norm_query:
        return []
    if inferred is None:
        inferred = infer_org_ids(rows)
    if norm_query.isdigit():
        exact = [row for row in rows if _as_int(_first(row, "OrgID")) == _as_int(norm_query)
                 or inferred.get(id(row)) == _as_int(norm_query)]
        if exact:
            return exact

    matched = _match_agency_names(rows, norm_query)
    identities = {_agency_identity(row, inferred) for row in matched}
    if len(identities) != 1 or not isinstance(next(iter(identities)), int):
        return matched
    # One agency matched: return its full dated history, including release
    # records merged by name, but not other agencies' records that reuse its ID.
    org_id = next(iter(identities))
    seen = {id(row) for row in matched}
    return matched + [row for row in agency_rows(rows)
                      if id(row) not in seen and _agency_identity(row, inferred) == org_id
                      and _norm_period(_first(row, "SurveyPeriodEndDate")) and not _has_reused_id(row)]


def _match_agency_names(rows: list[dict[str, str]], norm_query: str) -> list[dict[str, str]]:
    exact_matches: list[dict[str, str]] = []
    contains_matches: list[dict[str, str]] = []
    for row in rows:
        agency = re.sub(r"\s+", " ", _first(row, "Agency").lower())
        preferred = re.sub(r"\s+", " ", _first(row, "Agency_Preffered_Name", "Agency_Preferred_Name").lower())
        if not agency and not preferred:
            continue
        if norm_query == agency or norm_query == preferred:
            exact_matches.append(row)
        elif norm_query in agency or norm_query in preferred:
            contains_matches.append(row)

    if exact_matches:
        return exact_matches
    return contains_matches


def cached_release(url, timeout):
    key = hashlib.sha256(url.encode()).hexdigest()
    target = CACHE_DIR / (key + '.xlsx')
    try:
        age = time.time() - target.stat().st_mtime
        if 0 <= age < CACHE_TTL and target.stat().st_size <= MAX_BYTES:
            body = target.read_bytes()
            if zipfile.is_zipfile(io.BytesIO(body)):
                return body, datetime.fromtimestamp(target.stat().st_mtime, timezone.utc).isoformat().replace('+00:00', 'Z')
    except OSError:
        pass
    try:
        body, _ct, _source = nzfetch.fetch_bytes(url, timeout=timeout, max_bytes=MAX_BYTES,
                                                allowed_hosts={'www.publicservice.govt.nz'})
    except nzfetch.FetchError as exc:
        raise UpstreamUnavailable(str(exc)) from exc
    if not zipfile.is_zipfile(io.BytesIO(body)):
        raise ValueError('OIA release download was not a valid XLSX workbook')
    stamp = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    try:
        CACHE_DIR.mkdir(exist_ok=True)
        with tempfile.NamedTemporaryFile(dir=CACHE_DIR, delete=False) as handle:
            temporary = pathlib.Path(handle.name)
            handle.write(body)
        os.replace(temporary, target)
    except OSError:
        pass
    return body, stamp


def recover_release_periods(rows, releases):
    """Use exact agency identity and published counts, never CSV row order."""
    count_fields = ('OIA_RequestsHandled', 'OIAs_CompletedWithinTimeframe',
                    'OIAs_Published', 'Ombudsman_Complaints', 'FinalOpinionsbyOmbudsman')
    index = defaultdict(list)
    for row in agency_rows(rows):
        signature = tuple(_as_int(row.get(key)) for key in count_fields[:3])
        index[signature].append(row)
    consumed = set()
    recovered = []
    agency_identities = {(row['OrgID'], row['Agency']): row for row in agency_rows(rows)}
    def name_matches(row, name):
        def normal(value):
            return ' '.join(re.sub(r'[^\w?]', ' ', value.casefold().replace('&', ' and ')).split())
        name = normal(name)
        names = [_first(row, 'Agency'), _first(row, 'Agency_Preffered_Name', 'Agency_Preferred_Name')]
        for original in names:
            candidate = normal(original)
            if not candidate:
                continue
            # The source CSV explicitly replaces some Māori letters with '?'.
            # Match each such placeholder to exactly one letter, with all other
            # words exact. This is combined with exact published count matches.
            pattern = re.escape(candidate).replace(r'\?', r'[^\W\d_]')
            if re.fullmatch(pattern, name) or (len(candidate) >= 12
                    and re.search(r'(?<!\w)' + pattern + r'(?!\w)', name)):
                return True
        return False
    for period, url, stamp, records in releases:
        for record in records:
            signature = tuple(_as_int(record.get(key)) for key in count_fields[:3])
            candidates = [] if None in signature else [
                row for row in index.get(signature, [])
                if all(_as_int(record.get(key)) is None
                       or _as_int(row.get(key)) == _as_int(record[key])
                       for key in count_fields[3:])]
            identity_rows = [row for row in agency_identities.values() if name_matches(row, record['Agency'])]
            if len(identity_rows) == 1:
                resolved = identity_rows[0]
                record = dict(record, OrgID=resolved['OrgID'])
                candidates = [row for row in candidates if row['OrgID'] == resolved['OrgID']]
            elif record.get('OrgID'):
                candidates = [row for row in candidates if row.get('OrgID') == record['OrgID']]
            else:
                candidates = []
            ids = {row['OrgID'] for row in candidates}
            if len(ids) == 1:
                original = next((row for row in candidates if id(row) not in consumed), candidates[0])
                consumed.add(id(original))
                # Published metrics and dates come from the release; the CSV
                # supplies the stable ID and backwards-compatible agency names.
                restored = dict(original, **{key: value for key, value in record.items()
                    if key not in {'Agency', 'Agency_Type', 'OrgID'} and not key.startswith('_')})
                restored.update(Agency=record['Agency'], _source_url=url, _retrieved_at=stamp)
                recovered.append(restored)
            else:
                # Every release record is dated and counted by its official
                # workbook, so it always contributes to that period. Without a
                # CSV match it simply has no stable OrgID.
                kept = dict(record, _source_url=url, _retrieved_at=stamp)
                if not kept.get('OrgID'):
                    kept['_identity_warning'] = kept.get('_identity_warning') or UNMATCHED_IDENTITY_WARNING
                recovered.append(kept)
    identities = defaultdict(list)
    for row in recovered:
        if row.get('OrgID'):
            identities[(row['OrgID'], row['SurveyPeriodEndDate'])].append(row)
    for group in identities.values():
        if len(group) > 1:
            for row in group:
                row['_identity_warning'] = 'The published sources reuse this ID for different agencies in this period; use the exact agency name.'
    # Identical source counts across releases do not create ambiguous dates:
    # each dated record is independently stated in its official workbook.
    repaired = recovered + [row for row in rows if id(row) not in consumed]
    if not _rows_by_period(repaired):
        raise ValueError('OIA source contained no recoverable survey periods')
    return repaired


def load_rows(timeout: int) -> tuple[list[dict[str, str]], str]:
    rows, source = load_csv_rows(timeout)
    if _rows_by_period(rows):
        return rows, source
    tables = [table for table in discover_tables(timeout)
              if table['format'] == 'xlsx' and table['period']]
    if not tables:
        raise ValueError('OIA CSV reporting dates are invalid and no dated release workbooks were found')
    if len(tables) > 40:
        raise ValueError('OIA release listing exceeds the bounded recovery limit')
    def read(table):
        body, stamp = cached_release(table['url'], timeout)
        return table['period'], table['url'], stamp, parse_release(body, table['period'])
    with ThreadPoolExecutor(max_workers=4) as executor:
        releases = list(executor.map(read, tables))
    repaired = recover_release_periods(rows, releases)
    RECOVERY_SOURCES.update({period: (url, stamp) for period, url, stamp, records in releases})
    undated = sum(not _norm_period(row.get('SurveyPeriodEndDate')) for row in agency_rows(repaired))
    unmatched = sum(1 for row in repaired if row.get('_source_url') and not _as_int(_first(row, 'OrgID')))
    RECOVERY_WARNINGS[:] = [f'The all-data CSV has lost its reporting dates. Official release workbooks restore exact agency/count matches; {undated} historical agency rows remain undated.',
                           'Published tables and the CSV contain conflicting or reused IDs and some missing counts. Dates use the dated releases; use exact agency names where identity_warning is present. Undated records are excluded from period totals.',
                           f'{unmatched} official release records have no CSV match; they are included in their release period with org_id null so period totals equal the release workbooks.']
    return repaired, source


def infer_period_from_text(text: str) -> str | None:
    value = re.sub(r"\s+", " ", (text or "").lower()).strip()
    matches = [
        (r"(jan|january)\s*[-–—]?\s*(jun|june)\s+(\d{4})", "06-30"),
        (r"(jul|july)\s*[-–—]?\s*(dec|december)\s+(\d{4})", "12-31"),
        (r"1\s*jan(?:uary)?\s*(?:\d{4}\s*)?(?:to|[-–—])\s*30\s*jun(?:e)?\s+(\d{4})", "06-30"),
        (r"1\s*jul(?:y)?\s*(?:\d{4}\s*)?(?:to|[-–—])\s*31\s*dec(?:ember)?\s+(\d{4})", "12-31"),
    ]
    for pattern, suffix in matches:
        m = re.search(pattern, value)
        if m:
            year = m.group(1) if m.lastindex == 1 else m.group(3)
            if year:
                return f"{year}-{suffix}"
    return None


def _table_payload(url: str, label: str, period: str | None, ext: str, note: str | None = None) -> dict[str, object]:
    return {
        "id": re.sub(r"[^a-z0-9-]+", "-", f"{label}-{ext}".lower())[:90] or f"{period or 'all'}-{ext}",
        "format": ext,
        "label": label,
        "filename": url.rsplit("/", 1)[-1],
        "period": period,
        "source": LANDING_URL,
        "url": url,
        "note": note,
    }


def discover_tables(timeout: int) -> list[dict[str, object]]:
    try:
        html_text = fetch_text(LANDING_URL, timeout=timeout)
    except UpstreamUnavailable as exc:
        return [
            {
                "id": "all-data-csv-fallback",
                "format": "csv",
                "label": "OIA Statistics All Data CSV",
                "filename": "v_OIAStatisticsAllDataResults-1.csv",
                "period": None,
                "source": LANDING_URL,
                "url": CSV_URLS[0],
                "note": f"landing page unavailable; using stable CSV source ({exc})",
            }
        ]

    anchor_re = re.compile(r"<a[^>]+href=['\"]([^'\"]+)['\"][^>]*>(.*?)</a>", re.IGNORECASE | re.S)
    tables: list[dict[str, object]] = []
    seen: set[str] = set()

    for href, label_html in anchor_re.findall(html_text):
        href = html.unescape(href)
        if not href:
            continue
        if href.startswith("/"):
            href = "https://www.publicservice.govt.nz" + href
        if not href.startswith("http://") and not href.startswith("https://"):
            continue
        if "publicservice.govt.nz/assets" not in href:
            continue

        extension_match = re.search(r"\.([a-z0-9]+)(?:[?#].*)?$", href, re.I)
        if not extension_match:
            continue
        ext = extension_match.group(1).lower()
        if ext not in {"csv", "xlsx", "pdf"}:
            continue

        label = html.unescape(re.sub(r"<[^>]+>", "", label_html))
        label = re.sub(r"\s+", " ", label).strip()
        period = infer_period_from_text(label)
        if not period:
            period = infer_period_from_text(href)

        if not label or "oia" not in label.lower():
            if not any(token in href.lower() for token in ("oia", "statistics", ".xlsx", ".csv", ".pdf")):
                continue

        if href in seen:
            continue
        seen.add(href)

        tables.append(
            _table_payload(
                url=href,
                label=label or href.split("/", 1)[-1],
                period=period,
                ext=ext,
                note=("Dated agency release tables support stdlib ZIP/XML parsing when CSV dates are unavailable." if ext in {"xlsx"} else None),
            )
        )

    if not tables:
        tables.append(
            {
                "id": "all-data-csv-fallback",
                "format": "csv",
                "label": "OIA Statistics All Data CSV",
                "filename": "v_OIAStatisticsAllDataResults-1.csv",
                "period": None,
                "source": LANDING_URL,
                "url": CSV_URLS[0],
                "note": "no table links discovered; using stable all-data CSV source",
            }
        )
    return tables


def command_list_agencies(args: argparse.Namespace) -> dict[str, object]:
    rows, source_url = load_rows(args.timeout)
    agencies = list_agencies(rows)
    limit = args.limit
    if limit and limit > 0:
        agencies = agencies[:limit]
    return {
        "kind": "oia-list-agencies",
        "source": source_url,
        "count": len(agencies),
        "agencies": agencies,
    }


def command_periods(args: argparse.Namespace) -> dict[str, object]:
    rows, source_url = load_rows(args.timeout)
    periods = periods_summary(rows)
    limit = args.limit
    if limit and limit > 0:
        periods = periods[:limit]
    warnings = [str(item["warning"]) for item in periods if item.get("warning")]
    return {
        "kind": "oia-periods",
        "source": source_url,
        "count": len(periods),
        "periods": periods,
        "latest_period": periods[0]["period_end"] if periods else None,
        **({"warnings": warnings} if warnings else {}),
    }


def command_tables(args: argparse.Namespace) -> dict[str, object]:
    tables = discover_tables(args.timeout)
    if args.format != "all":
        tables = [t for t in tables if t["format"] == args.format]

    format_order = {"csv": 0, "xlsx": 1, "pdf": 2}
    tables.sort(
        key=lambda item: (
            format_order.get(str(item.get("format", "pdf")), 99),
            str(item.get("period") or "0000-00-00"),
            str(item.get("label", "")),
        )
    )

    limit = args.limit
    if limit and limit > 0:
        tables = tables[:limit]

    return {
        "kind": "oia-tables",
        "landing_page": LANDING_URL,
        "source": LANDING_URL,
        "count": len(tables),
        "tables": tables,
    }


def command_agency(args: argparse.Namespace) -> dict[str, object]:
    rows, source_url = load_rows(args.timeout)
    by_period = _rows_by_period(rows)
    inferred = infer_org_ids(rows)
    matches = _match_agency_rows(rows, args.agency_query, inferred)
    if not matches:
        raise ValueError(f"no agency matched query: {args.agency_query}")

    if args.period:
        period = parse_period_arg(args.period, set(by_period))
        matches = [row for row in matches if _norm_period(_first(row, "SurveyPeriodEndDate")) == period]
        if not matches:
            raise ValueError(f"no data for {args.agency_query} in period {period}")

    # Release records merged into an OrgID by name are that agency, not another.
    agency_ids = {_agency_identity(row, inferred) for row in matches}
    if not args.period and len(agency_ids) > 1 and not str(args.agency_query).strip().isdigit():
        raise ValueError(
            "ambiguous agency query; multiple agencies matched. Use OrgID for exact match or a more specific name."
        )

    period_rows = sorted(matches, key=lambda row: _norm_period(_first(row, "SurveyPeriodEndDate")), reverse=True)
    series = []
    for row in period_rows:
        record = row_enriched(row)
        if id(row) in inferred:
            record["inferred_org_id"] = inferred[id(row)]
        series.append(record)
    if args.limit and args.limit > 0:
        series = series[: args.limit]
    identity = next(iter(agency_ids)) if len(agency_ids) == 1 else None

    return {
        "kind": "oia-agency",
        "source": source_url,
        "count": len(series),
        "agency": {
            "org_id": identity if isinstance(identity, int) else series[0]["org_id"],
            "agency": series[0]["agency"],
            "agency_preferred_name": series[0]["agency_preferred_name"],
            "agency_type": series[0]["agency_type"],
        },
        "period": args.period or "all",
        "records": series,
    }


def command_period(args: argparse.Namespace) -> dict[str, object]:
    rows, source_url = load_rows(args.timeout)
    period_rows, period = _rows_for_period(rows, args.period)
    if not period_rows:
        raise ValueError(f"no rows for period {period}")

    records = [row_enriched(row) for row in agency_rows(period_rows)]
    if args.sort == "worst":
        records = sort_by_key(records, "timeliness_pct", descending=False)
    elif args.sort == "best":
        records = sort_by_key(records, "timeliness_pct", descending=True)
    elif args.sort == "requests":
        records = sort_by_key(records, "requests", descending=True)
    else:
        records = sort_by_key(records, "name")

    limit = args.limit
    if limit and limit > 0:
        records = records[:limit]

    on_time = on_time_summary(agency_rows(period_rows), period)
    return {
        "kind": "oia-period",
        "source": source_url,
        "period_end": period,
        "period_label": period_label(period),
        "sort": args.sort,
        "count": len(records),
        "records": records,
        "on_time_coverage": on_time["on_time_coverage"],
        **({"warnings": [on_time["warning"]]} if on_time["warning"] else {}),
    }


def command_totals(args: argparse.Namespace) -> dict[str, object]:
    rows, source_url = load_rows(args.timeout)
    period_rows, period = _rows_for_period(rows, args.period)
    if not period_rows:
        raise ValueError(f"no rows for period {period}")

    totals: dict[str, Any] = {
        "period_end": period,
        "period_label": period_label(period),
        "agency_count": 0,
        "requests_handled": 0,
        "requests_completed_within_timeframe": 0,
        "responses_published": 0,
        "extensions": 0,
        "transfers": 0,
        "refusals": 0,
        "complaints": 0,
        "final_opinions": 0,
        "weighted_average_days": None,
        "weighted_median_days": None,
    }

    agency_ids = set()
    weighted_total = 0
    weighted_avg_sum = 0.0
    weighted_median_sum = 0.0

    for row in agency_rows(period_rows):
        agency_ids.add((_first(row, "OrgID"), _first(row, "Agency")))
        enriched = row_enriched(row)
        handled = enriched.get("requests_handled") or 0
        totals["requests_handled"] += int(handled)
        totals["responses_published"] += int(enriched["responses_published"] or 0)
        totals["extensions"] += int(enriched["extensions"] or 0)
        totals["transfers"] += int(enriched["transfers"] or 0)
        totals["refusals"] += int(enriched["refusals"] or 0)
        totals["complaints"] += int(enriched["complaints"] or 0)
        totals["final_opinions"] += int(enriched["final_opinions"] or 0)

        weight = int(handled) if int(handled) > 0 else 0
        if weight:
            if enriched["response_average_days"] is not None:
                weighted_avg_sum += float(enriched["response_average_days"]) * weight
            if enriched["response_median_days"] is not None:
                weighted_median_sum += float(enriched["response_median_days"]) * weight
            weighted_total += weight

    totals["agency_count"] = len(agency_ids)
    on_time = on_time_summary(agency_rows(period_rows), period)
    totals["requests_completed_within_timeframe"] = on_time["requests_completed_within_timeframe"]
    totals["timeliness_pct"] = on_time["timeliness_pct"]
    totals["on_time_coverage"] = on_time["on_time_coverage"]
    totals["extensions_pct"] = round((totals["extensions"] / totals["requests_handled"]) * 100, 4) if totals["requests_handled"] else None
    totals["transfers_pct"] = round((totals["transfers"] / totals["requests_handled"]) * 100, 4) if totals["requests_handled"] else None
    totals["refusals_pct"] = round((totals["refusals"] / totals["requests_handled"]) * 100, 4) if totals["requests_handled"] else None

    if weighted_total:
        if weighted_avg_sum:
            totals["weighted_average_days"] = round(weighted_avg_sum / weighted_total, 4)
        if weighted_median_sum:
            totals["weighted_median_days"] = round(weighted_median_sum / weighted_total, 4)

    return {
        "kind": "oia-totals",
        "source": source_url,
        "period_end": period,
        "period_label": period_label(period),
        "total_row_count": len(agency_rows(period_rows)),
        "totals": totals,
        **({"warnings": [on_time["warning"]]} if on_time["warning"] else {}),
    }


def _metric_records(
    rows: list[dict[str, str]],
    period: str,
    limit: int,
    metric_key: str,
    sort: str,
) -> tuple[list[dict[str, object]], str]:
    period_rows, period_end = _rows_for_period(rows, period)
    records = [row_enriched(row) for row in agency_rows(period_rows)]
    if sort == "name":
        records = sort_by_key(records, "name")
    elif metric_key == "timeliness_pct":
        records = sort_by_key(records, metric_key, descending=(sort == "best"))
    else:
        records = sort_by_key(records, metric_key, descending=(sort != "best"))

    if limit and limit > 0:
        records = records[:limit]

    return records, period_end


def command_timeliness(args: argparse.Namespace) -> dict[str, object]:
    rows, source_url = load_rows(args.timeout)
    records, period = _metric_records(
        rows=rows,
        period=args.period,
        limit=args.limit,
        metric_key="timeliness_pct",
        sort=args.sort,
    )
    # Agencies without a reported on-time count keep timeliness_pct null and
    # sort after every ranked agency (never as 0%).
    on_time = on_time_summary(agency_rows(_rows_by_period(rows).get(period, [])), period)
    return {
        "kind": "oia-timeliness",
        "source": source_url,
        "period_end": period,
        "period_label": period_label(period),
        "sort": args.sort,
        "count": len(records),
        "records": records,
        "on_time_coverage": on_time["on_time_coverage"],
        **({"warnings": [on_time["warning"]]} if on_time["warning"] else {}),
    }


def command_refusals(args: argparse.Namespace) -> dict[str, object]:
    rows, source_url = load_rows(args.timeout)
    records, period = _metric_records(
        rows=rows,
        period=args.period,
        limit=args.limit,
        metric_key="refusals_pct",
        sort=args.sort,
    )
    return {
        "kind": "oia-refusals",
        "source": source_url,
        "period_end": period,
        "period_label": period_label(period),
        "sort": args.sort,
        "count": len(records),
        "records": records,
    }


def command_extensions(args: argparse.Namespace) -> dict[str, object]:
    rows, source_url = load_rows(args.timeout)
    records, period = _metric_records(
        rows=rows,
        period=args.period,
        limit=args.limit,
        metric_key="extensions_pct",
        sort=args.sort,
    )
    return {
        "kind": "oia-extensions",
        "source": source_url,
        "period_end": period,
        "period_label": period_label(period),
        "sort": args.sort,
        "count": len(records),
        "records": records,
    }


def command_complaints(args: argparse.Namespace) -> dict[str, object]:
    rows, source_url = load_rows(args.timeout)
    period_rows, period = _rows_for_period(rows, args.period)
    if not period_rows:
        raise ValueError(f"no rows for period {period}")

    records = [row_enriched(row) for row in agency_rows(period_rows)]
    if args.sort == "name":
        records = sort_by_key(records, "name")
    elif args.sort == "final_opinions":
        records = sort_by_key(records, "final_opinions", descending=True)
    elif args.sort == "best":
        records = sort_by_key(records, "complaints", descending=False)
    else:
        records = sort_by_key(records, "complaints", descending=True)

    if args.limit and args.limit > 0:
        records = records[:args.limit]

    return {
        "kind": "oia-complaints",
        "source": source_url,
        "period_end": period,
        "period_label": period_label(period),
        "sort": args.sort,
        "count": len(records),
        "records": records,
    }


def emit(payload: dict[str, object], as_json: bool) -> None:
    if as_json:
        print(json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False))
        return

    if payload.get("kind"):
        print(f"{payload['kind']}: {payload.get('count', 'n/a')}")
    else:
        print(json.dumps(payload, indent=2, ensure_ascii=False))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Query PSC six-monthly OIA compliance statistics.")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT, help="network timeout seconds")
    subparsers = parser.add_subparsers(dest="command", required=True)

    def _common_limit_argument(target: argparse.ArgumentParser, default: int = 0) -> None:
        target.add_argument("--limit", type=int, default=default, help="max rows (0 = all)")

    list_agencies = subparsers.add_parser("list-agencies", help="list distinct agencies in the OIA all-data CSV")
    list_agencies.add_argument("--limit", type=int, default=200, help="max agencies")
    list_agencies.add_argument("--json", action="store_true", help="print machine-readable JSON output")
    list_agencies.set_defaults(func=command_list_agencies)

    agency = subparsers.add_parser("agency", help="full series for one agency by name or OrgID")
    agency.add_argument("agency_query", help="agency name (partial or full) or OrgID")
    agency.add_argument("--period", help="optional period in YYYY-MM-DD, YYYY-06/12, YYYY-H1/2, latest")
    agency.add_argument("--limit", type=int, default=0, help="max periods in response (0 = all)")
    agency.add_argument("--json", action="store_true", help="print machine-readable JSON output")
    agency.set_defaults(func=command_agency)

    period = subparsers.add_parser("period", help="all agencies for one period, including computed on-time percentage")
    period.add_argument("period", help="YYYY-MM-DD, YYYY-06/12, YYYY-H1/2, or latest")
    period.add_argument("--sort", choices=["name", "worst", "best", "requests"], default="name")
    _common_limit_argument(period, default=0)
    period.add_argument("--json", action="store_true", help="print machine-readable JSON output")
    period.set_defaults(func=command_period)

    periods = subparsers.add_parser("periods", help="list available survey periods")
    periods.add_argument("--limit", type=int, default=0, help="max periods returned (0 = all)")
    periods.add_argument("--json", action="store_true", help="print machine-readable JSON output")
    periods.set_defaults(func=command_periods)

    tables = subparsers.add_parser("tables", help="discover OIA table assets from PSC landing page")
    tables.add_argument("--format", choices=["all", "csv", "xlsx", "pdf"], default="all", help="filter by asset format")
    tables.add_argument("--limit", type=int, default=200, help="max table rows returned")
    tables.add_argument("--json", action="store_true", help="print machine-readable JSON output")
    tables.set_defaults(func=command_tables)

    def add_metric_parser(name: str, help_text: str) -> argparse.ArgumentParser:
        parser_metric = subparsers.add_parser(name, help=help_text)
        parser_metric.add_argument("--period", default="latest", help="period YYYY-MM-DD, YYYY-06/12, YYYY-H1/2, or latest")
        parser_metric.add_argument("--sort", choices=["worst", "best", "name"], default="worst")
        parser_metric.add_argument("--limit", type=int, default=50, help="max agencies")
        parser_metric.add_argument("--json", action="store_true", help="print machine-readable JSON output")
        return parser_metric

    add_metric_parser("timeliness", "worst-to-best agency completion-time ratio for one period").set_defaults(func=command_timeliness)
    add_metric_parser("refusals", "top refusal rows for one period").set_defaults(func=command_refusals)
    add_metric_parser("extensions", "top extension rows for one period").set_defaults(func=command_extensions)

    complaints = subparsers.add_parser("complaints", help="ombudsman complaints and final-opinion metrics")
    complaints.add_argument("--period", default="latest", help="period YYYY-MM-DD, YYYY-06/12, YYYY-H1/2, or latest")
    complaints.add_argument("--sort", choices=["complaints", "final_opinions", "worst", "best", "name"], default="complaints")
    complaints.add_argument("--limit", type=int, default=50, help="max agencies")
    complaints.add_argument("--json", action="store_true", help="print machine-readable JSON output")
    complaints.set_defaults(func=command_complaints)

    totals = subparsers.add_parser("totals", help="sector-wide totals for one period")
    totals.add_argument("--period", default="latest", help="period YYYY-MM-DD, YYYY-06/12, YYYY-H1/2, or latest")
    totals.add_argument("--json", action="store_true", help="print machine-readable JSON output")
    totals.set_defaults(func=command_totals)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.timeout < 1:
        die("--timeout must be a positive integer")

    try:
        payload = args.func(args)
        payload['meta'] = {'source_url': payload.get('source', LANDING_URL),
                           'publisher': 'Public Service Commission',
                           'retrieved_at': datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')}
        latest = payload.get('latest_period') or payload.get('period_end')
        if latest:
            payload['meta']['latest_data'] = latest
            if latest in RECOVERY_SOURCES:
                url, stamp = RECOVERY_SOURCES[latest]
                payload['meta'].update(source_url=url, retrieved_at=stamp)
        if RECOVERY_WARNINGS:
            payload['warnings'] = list(RECOVERY_WARNINGS) + list(payload.get('warnings') or [])
        emit(payload, bool(args.json))
        return 0
    except ValueError as exc:
        die(str(exc), code=6 if str(exc).startswith('OIA ') else 1)
    except UpstreamUnavailable as exc:
        if getattr(args, "json", False):
            print(
                json.dumps(
                    {
                        "error": "upstream_unavailable",
                        "message": str(exc),
                        "command": args.command,
                    },
                    indent=2,
                    ensure_ascii=False,
                ),
                file=sys.stdout,
            )
            return 2
        die(f"upstream unavailable: {exc}", code=2)
    return 1


if __name__ == "__main__":
    sys.exit(main())
