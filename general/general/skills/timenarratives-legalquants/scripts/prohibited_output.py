"""Deterministic authored-text guard for TimeNarratives output."""

from __future__ import annotations

import re
import unicodedata
from collections.abc import Iterator

Issue = dict[str, str]
AuthoredText = tuple[str, str]

APOSTROPHES = str.maketrans(
    {
        "\u02bc": "'",
        "\u2018": "'",
        "\u2019": "'",
        "\u201b": "'",
        "\uff07": "'",
    }
)
WORD = re.compile(r"[^\W_]+(?:'[^\W_]+)?", re.UNICODE)
COMPACT_DURATION = re.compile(
    r"(?<!\w)(?:\d+(?:[.,]\d+)?(?:h\d{1,2}m?|h|m|s)|"
    r"\d{1,2}(?::|\.)\d{2})(?!\w)",
    re.IGNORECASE,
)
BILLING_CODE = re.compile(r"(?<!\w)[a-z]\d{3,4}(?!\w)", re.IGNORECASE)

NUMBER_WORDS = frozenset(
    """
    zero one two three four five six seven eight nine ten eleven twelve thirteen
    fourteen fifteen sixteen seventeen eighteen nineteen twenty thirty forty
    fifty sixty seventy eighty ninety hundred thousand million billion trillion
    quadrillion half quarter dozen score couple first second third fourth fifth
    sixth seventh eighth ninth tenth eleventh twelfth thirteenth fourteenth
    fifteenth sixteenth seventeenth eighteenth nineteenth twentieth thirtieth
    fortieth fiftieth sixtieth seventieth eightieth ninetieth hundredth
    thousandth millionth billionth trillionth once twice thrice single double
    triple
    """.split()
)
DURATION_WORDS = frozenset(
    """
    time times duration durations clock clocks hour hours hr hrs minute minutes
    min mins second seconds sec secs day days week weeks month months year years
    morning mornings afternoon afternoons evening evenings noon midnight am pm
    elapsed timesheet timesheets
    """.split()
)
MONEY_WORDS = frozenset(
    """
    currency currencies monetary rate rates fee fees value values amount amounts
    budget budgets price prices total totals pound pounds sterling pence penny
    dollar dollars cent cents euro euros yen gbp usd eur aud cad nzd chf jpy
    """.split()
)
BILLING_WORDS = frozenset(
    """
    bill bills billed billing code codes coded coding classification
    classifications classify classified classifying utbms ledes taskcode
    activitycode
    """.split()
)
BILLABILITY_WORDS = frozenset(
    """
    billable unbillable nonbillable billability chargeable unchargeable
    nonchargeable
    """.split()
)
POSTING_WORDS = frozenset(
    """
    post posts posted posting submit submits submitted submitting submission
    submissions record records recorded recording enter enters entered entering
    entry entries invoiced invoicing lodge lodges lodged lodging
    """.split()
)

# Invoice(s) can name the object of legal work. Match instructions/predicates
# separately rather than treating the noun as proof of a posting decision.
# This lexical check supplements semantic review; it cannot prove intent.
INVOICE_ACTION = re.compile(
    r"(?:^|[.!?;:]\s*|\b(?:please|then|must|should|will|can|could|would|shall)\s+)"
    r"invoice\b(?!\s+(?:response|dispute|provision|clause|defence|claim)\b)|"
    r"\b(?:i|we|you|they|he|she)\s+invoices?\b|"
    r"\b(?:rais(?:e[ds]?|ing)|creat(?:e[ds]?|ing)|prepar(?:e[ds]?|ing)|"
    r"generat(?:e[ds]?|ing)|draft(?:s|ed|ing)?|issu(?:e[ds]?|ing)|"
    r"send(?:s|ing)?|sent|produc(?:e[ds]?|ing))\s+"
    r"(?:(?:an?|the|our|your|final|new|revised|client)\s+)*invoices?\b"
    r"(?!\s+(?:response|dispute|provision|clause|defence|claim)\b)"
)


def normalize_authored(text: str) -> str:
    """Apply the exact normalization shared by output and copy guards."""
    normalized = unicodedata.normalize("NFKC", text).casefold()
    without_format = "".join(
        character for character in normalized if unicodedata.category(character) != "Cf"
    )
    return " ".join(without_format.translate(APOSTROPHES).split())


def _tokens(text: str) -> set[str]:
    return set(WORD.findall(normalize_authored(text)))


def _has_unicode_numeric(text: str) -> bool:
    for character in text:
        try:
            unicodedata.numeric(character)
        except (TypeError, ValueError):
            continue
        return True
    return False


def scan_text(text: str, path: str) -> list[Issue]:
    """Return controlled-vocabulary category/path faults without echoing text."""
    tokens = _tokens(text)
    normalized = normalize_authored(text)
    rules = (
        (
            "numeric_data",
            _has_unicode_numeric(text) or bool(tokens & NUMBER_WORDS),
        ),
        (
            "duration_data",
            bool(tokens & DURATION_WORDS)
            or COMPACT_DURATION.search(normalized) is not None,
        ),
        (
            "money_data",
            any(unicodedata.category(char) == "Sc" for char in text)
            or bool(tokens & MONEY_WORDS),
        ),
        (
            "billing_code",
            bool(tokens & BILLING_WORDS) or BILLING_CODE.search(normalized) is not None,
        ),
        ("billability_decision", bool(tokens & BILLABILITY_WORDS)),
        (
            "posting_decision",
            bool(tokens & POSTING_WORDS)
            or INVOICE_ACTION.search(normalized) is not None,
        ),
    )
    return [{"code": code, "path": path} for code, matched in rules if matched]


def _authored_fields(
    value: object, collection: str, fields: tuple[str, ...]
) -> Iterator[AuthoredText]:
    if not isinstance(value, dict):
        return
    records = value.get(collection)
    if not isinstance(records, list):
        return
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            continue
        for field in fields:
            text = record.get(field)
            if isinstance(text, str):
                yield f"$.{collection}[{index}].{field}", text


def iter_model_authored_text(value: object) -> Iterator[AuthoredText]:
    """Yield only fields authored by the model in a semantic map."""
    yield from _authored_fields(value, "events", ("action", "object", "purpose"))
    yield from _authored_fields(value, "workstreams", ("label",))
    yield from _authored_fields(value, "clauses", ("text",))


def _markdown_narratives(deliverable: object, markdown: str) -> Iterator[AuthoredText]:
    if not isinstance(deliverable, dict):
        return
    narratives = deliverable.get("narratives")
    if not isinstance(narratives, list):
        return
    lines = markdown.splitlines()
    search_from = 0
    for index, narrative in enumerate(narratives):
        if not isinstance(narrative, dict):
            continue
        workstream_id = narrative.get("workstreamId")
        if not isinstance(workstream_id, str):
            continue
        heading = f"### {workstream_id}"
        try:
            heading_at = lines.index(heading, search_from)
        except ValueError:
            continue
        body: list[str] = []
        for line_at in range(heading_at + 1, len(lines)):
            line = lines[line_at]
            if line.startswith("Support: "):
                search_from = line_at + 1
                break
            body.append(line)
        text = "\n".join(body).strip()
        if text:
            yield f"$markdown.narratives[{index}].text", text


def iter_rendered_authored_text(
    deliverable: object, markdown: str
) -> Iterator[AuthoredText]:
    """Yield narrative text only, excluding identifiers and receipt metadata."""
    yield from _authored_fields(deliverable, "narratives", ("text",))
    yield from _markdown_narratives(deliverable, markdown)


def _scan_fields(fields: Iterator[AuthoredText]) -> list[Issue]:
    return [issue for path, text in fields for issue in scan_text(text, path)]


def scan_model_output(value: object) -> list[Issue]:
    return _scan_fields(iter_model_authored_text(value))


def scan_rendered(deliverable: object, markdown: str) -> list[Issue]:
    return _scan_fields(iter_rendered_authored_text(deliverable, markdown))
