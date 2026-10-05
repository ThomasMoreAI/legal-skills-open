"""
Canadian Court Document Downloader v2.

Lawful public access only. No CAPTCHA/login/bot-detection bypass.
CanLII automated access → REFERENCE_PDF (do not retry Cloudflare).
Rate limit: ≥0.5s between requests.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Optional

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

DEFAULT_BATCH_DELAY = 0.5
MIN_VALID_PDF_BYTES = 5 * 1024  # <5KB → SMALL_FILE
USER_AGENT = (
    "BC-Legal-AI-Associate/0.2 (lawful public case retrieval; research tool)"
)

# citation -> {name, item_id, note?}
SCC_ITEM_IDS: dict[str, dict[str, str]] = {
    "2019 SCC 65": {"name": "Vavilov", "item_id": "18078"},
    "2011 SCC 61": {"name": "Alberta Teachers Association", "item_id": "7979"},
    "2008 SCC 9": {"name": "Dunsmuir", "item_id": "5615"},
    "[1999] 2 SCR 817": {"name": "Baker", "item_id": "1717"},
    "1999 2 SCR 817": {"name": "Baker", "item_id": "1717"},
    "[1985] 2 SCR 643": {"name": "Cardinal v. Kent Institution", "item_id": "2697"},
    "[1978] 1 SCR 369": {"name": "Committee for Justice and Liberty", "item_id": "2265"},
    "[1979] 1 SCR 311": {"name": "Nicholson", "item_id": "2471"},
    "[1992] 1 SCR 623": {"name": "Newfoundland Telephone", "item_id": "1437"},
    "2001 SCC 52": {"name": "Ocean Port Hotel", "item_id": "5176"},
    "2017 SCC 23": {"name": "Pintea v. Johns", "item_id": "16589"},
    "2011 SCC 62": {"name": "Newfoundland Nurses", "item_id": "7980"},
    "2001 SCC 4": {"name": "Ellis-Don", "item_id": "5073"},
    "2001 SCC 44": {"name": "Danyluk", "item_id": "5087"},
    "2011 SCC 52": {"name": "Figliola", "item_id": "8001"},
    "2013 SCC 19": {"name": "Penner", "item_id": "12962"},
    "2002 SCC 79": {"name": "Wewaykum Indian Band", "item_id": "5469"},
    "2003 SCC 63": {"name": "Toronto v. CUPE Local 79", "item_id": "5626"},
    "2004 SCC 5": {"name": "R. v. Lyttle", "item_id": "5707"},
    "2010 SCC 22": {"name": "R. v. Conway", "item_id": "7863"},
    "2015 SCC 5": {"name": "Carter v. Canada", "item_id": "15696"},
    # Provisional IDs — may return HTTP 400; search if needed
    "[1990] 1 SCR 653": {
        "name": "Knight v. Indian Head",
        "item_id": "2998",
        "note": "provisional_id",
    },
    "[1980] 1 SCR 1105": {
        "name": "Kane v. UBC",
        "item_id": "2419",
        "note": "provisional_id",
    },
    "[1993] 2 SCR 756": {
        "name": "Lapointe v. Quebec",
        "item_id": "3688",
        "note": "provisional_id",
    },
}


@dataclass
class DownloaderConfig:
    preferred_sources: list[str] = field(
        default_factory=lambda: ["SCC", "BCCA", "BCSC", "FCA", "REFERENCE"]
    )
    output_dir: Optional[Path] = None
    include_ocr: bool = False
    batch_delay_seconds: float = DEFAULT_BATCH_DELAY
    generate_table_of_authorities: bool = True
    include_reference_pdfs: bool = True
    tag_anchor_cases: bool = True
    matter: str = ""


@dataclass
class DownloadResult:
    tab: int
    citation: str
    case_name: str
    court: str
    status: str
    path: Optional[str] = None
    url: Optional[str] = None
    bytes_size: int = 0
    sha256: Optional[str] = None
    message: str = ""
    jurisdiction: str = ""
    is_scanned: Optional[bool] = None
    ocr_text_path: Optional[str] = None
    version: int = 1
    tags: list[str] = field(default_factory=list)
    retrieved_at: str = ""
    proposition: str = ""
    document_type: str = "judgment"
    access_status: str = "public"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def to_metadata(self) -> dict[str, Any]:
        return {
            "case_name": self.case_name,
            "citation": self.citation,
            "court": self.court,
            "jurisdiction": self.jurisdiction or _jurisdiction(self.court),
            "judge_or_panel": "",
            "decision_date": "",
            "hearing_date": "",
            "document_type": self.document_type,
            "file_number": "",
            "source": self.court,
            "source_url": self.url or "",
            "access_status": self.access_status
            if self.status == "SUCCESS"
            else "reference_pdf",
            "downloaded_file": self.path or "",
            "file_size_bytes": self.bytes_size,
            "checksum": self.sha256 or "",
            "retrieved_at": self.retrieved_at or _utcnow(),
            "is_scanned": self.is_scanned,
            "ocr_text_path": self.ocr_text_path or "",
            "appeal_history": "",
            "tags": list(self.tags),
            "version": self.version,
            "status": self.status,
            "note": self.message,
            "proposition": self.proposition,
        }


def _utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


def _jurisdiction(court: str) -> str:
    if court == "SCC":
        return "federal"
    if court in ("BCCA", "BCSC"):
        return "bc"
    if court in ("ONCA", "ONSC"):
        return "on"
    if court == "FCA":
        return "federal"
    return "unknown"


def identify_court(citation: str) -> str:
    c = (citation or "").upper()
    if "SCC" in c or "SCR" in c:
        return "SCC"
    if "BCCA" in c:
        return "BCCA"
    if "BCSC" in c:
        return "BCSC"
    if "FCA" in c or "CAF" in c:
        return "FCA"
    if "ONCA" in c:
        return "ONCA"
    if "ONSC" in c:
        return "ONSC"
    return "UNKNOWN"


def citation_slug(citation: str) -> str:
    s = re.sub(r"[^\w\s\-]", "", citation)
    s = re.sub(r"\s+", "_", s.strip())
    return s[:80].lower() or "unknown"


def short_name(name: str) -> str:
    s = re.sub(r"[^\w\s\-]", "", name)
    s = re.sub(r"\s+", "_", s.strip())
    # shorten common patterns
    s = s.replace("v_", "v_")
    parts = s.split("_")
    if len(parts) > 4:
        s = "_".join(parts[:4])
    return s[:40] or "Case"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def lookup_scc(citation: str) -> Optional[dict[str, str]]:
    raw = (citation or "").strip()
    if raw in SCC_ITEM_IDS:
        return SCC_ITEM_IDS[raw]
    norm = re.sub(r"\s+", " ", raw.upper())
    for k, v in SCC_ITEM_IDS.items():
        if re.sub(r"\s+", " ", k.upper()) == norm:
            return v
    m = re.search(r"(20\d{2})\s*SCC\s*(\d+)", raw, re.I)
    if m:
        key = f"{m.group(1)} SCC {m.group(2)}"
        if key in SCC_ITEM_IDS:
            return SCC_ITEM_IDS[key]
    m2 = re.search(r"\[?(19\d{2}|20\d{2})\]?\s*(\d)\s*SCR\s*(\d+)", raw, re.I)
    if m2:
        key = f"[{m2.group(1)}] {m2.group(2)} SCR {m2.group(3)}"
        if key in SCC_ITEM_IDS:
            return SCC_ITEM_IDS[key]
        # try without brackets variants already in map
        for k, v in SCC_ITEM_IDS.items():
            if m2.group(3) in k and m2.group(1) in k:
                return v
    return None


def scc_pdf_url(item_id: str, doc: int = 1) -> str:
    return (
        f"https://decisions.scc-csc.ca/scc-csc/scc-csc/en/{item_id}/{doc}/document.do"
    )


def canlii_search_url(citation: str) -> str:
    return (
        "https://www.canlii.org/en/#search/type=decision&text="
        + urllib.parse.quote(citation)
    )


def fca_pdf_url(item_id: str) -> str:
    return f"https://decisions.fca-caf.ca/fca-caf/fca/en/{item_id}/1/document.do"


def _http_get(url: str, timeout: int = 60) -> tuple[int, bytes, str]:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Accept": "application/pdf,*/*"},
        method="GET",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read(), resp.headers.get("Content-Type", "")
    except urllib.error.HTTPError as e:
        body = b""
        try:
            body = e.read()
        except Exception:
            pass
        return e.code, body, ""
    except Exception as e:
        return 0, str(e).encode("utf-8"), "error"


def _is_valid_pdf(data: bytes) -> tuple[bool, str]:
    if not data:
        return False, "EMPTY"
    if data[:4] != b"%PDF":
        return False, "NOT_PDF"
    if len(data) < MIN_VALID_PDF_BYTES:
        # allow small official PDFs only if clearly PDF (some are tiny)
        if len(data) < 500:
            return False, "SMALL_FILE"
        # Lyttle is ~70KB so min 5KB is fine; sub-5KB often HTML error
        if b"html" in data[:200].lower() or b"<!DOCTYPE" in data[:200]:
            return False, "NOT_PDF"
        if len(data) < MIN_VALID_PDF_BYTES and b"Reference document" not in data[:500]:
            return False, "SMALL_FILE"
    if b"<html" in data[:500].lower():
        return False, "NOT_PDF"
    return True, "OK"


def is_scanned_pdf(path: Path) -> bool:
    try:
        from pypdf import PdfReader  # type: ignore

        reader = PdfReader(str(path))
        for page in reader.pages[:3]:
            t = (page.extract_text() or "").strip()
            if t:
                return False
        return True
    except Exception:
        return False


def ocr_pdf(path: Path, output_text_path: Path) -> dict[str, Any]:
    try:
        import pytesseract  # type: ignore
        from pdf2image import convert_from_path  # type: ignore

        images = convert_from_path(str(path))
        text = "\n".join(pytesseract.image_to_string(img) for img in images)
        output_text_path.write_text(text, encoding="utf-8")
        return {"status": "OCR_SUCCESS", "chars": len(text), "path": str(output_text_path)}
    except ImportError:
        return {
            "status": "OCR_UNAVAILABLE",
            "note": "Install pytesseract and pdf2image for OCR",
        }
    except Exception as e:
        return {"status": "OCR_FAILED", "note": str(e)}


def write_reference_pdf(
    path: Path,
    *,
    citation: str,
    case_name: str,
    court: str,
    url: str,
    reason: str,
    proposition: str = "",
    key_passages: Optional[list[str]] = None,
    relevance: str = "",
) -> int:
    """Write REFERENCE.txt (primary) + minimal PDF stub for naming consistency."""
    passages = key_passages or []
    ref_txt = path.with_suffix(".REFERENCE.txt")
    lines = [
        "REFERENCE ONLY — not the official judgment",
        f"Case: {case_name}",
        f"Citation: {citation}",
        f"Court: {court}",
        f"Reason automated download blocked: {reason}",
        f"Manual download / search URL: {url}",
        f"Generated: {_utcnow()}",
        "",
        "Proposition (user-supplied or placeholder):",
        proposition or "(none provided)",
        "",
        "Key passages to locate manually:",
    ]
    for p in passages:
        lines.append(f"  - {p}")
    if not passages:
        lines.append("  - (none listed)")
    lines.extend(
        [
            "",
            "Relevance to proceeding:",
            relevance or "(set by counsel)",
            "",
            "Do not file this reference sheet as the authority itself.",
        ]
    )
    ref_txt.write_text("\n".join(lines), encoding="utf-8")

    # Minimal PDF stub (not court-ready)
    body = f"""%PDF-1.1
1 0 obj<< /Type /Catalog /Pages 2 0 R >>endobj
2 0 obj<< /Type /Pages /Kids [3 0 R] /Count 1 >>endobj
3 0 obj<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792]
/Contents 4 0 R /Resources<< /Font<< /F1 5 0 R >> >> >>endobj
4 0 obj<< /Length 120 >>stream
BT /F1 11 Tf 50 720 Td (REFERENCE ONLY) Tj 0 -18 Td ({case_name[:50]}) Tj ET
endstream endobj
5 0 obj<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>endobj
xref
0 6
0000000000 65535 f 
trailer<< /Size 6 /Root 1 0 R >>
startxref
0
%%EOF
"""
    path.write_bytes(body.encode("latin-1", errors="replace"))
    return path.stat().st_size


def check_duplicate(
    citation: str,
    output_dir: Path,
    *,
    new_hash: Optional[str] = None,
) -> dict[str, Any]:
    slug = citation_slug(citation)
    if not output_dir.is_dir():
        return {"is_duplicate": False}
    for f in output_dir.iterdir():
        if not f.is_file():
            continue
        if slug not in f.name.lower() and citation_slug(citation).replace("_", "") not in f.name.lower().replace("_", ""):
            # also match short citation pieces
            m = re.search(r"(\d{4})_?scc_?(\d+)", slug)
            if m:
                piece = f"{m.group(1)}_scc_{m.group(2)}"
                if piece not in f.name.lower():
                    continue
            else:
                continue
        if f.suffix.lower() not in (".pdf", ".txt"):
            continue
        try:
            existing_hash = sha256_file(f) if f.suffix.lower() == ".pdf" else ""
        except OSError:
            continue
        if new_hash and existing_hash and new_hash == existing_hash:
            return {
                "is_duplicate": True,
                "kind": "EXACT_DUPLICATE",
                "existing_file": str(f),
                "action": "SKIP",
            }
        if f.suffix.lower() == ".pdf" and f.stat().st_size >= MIN_VALID_PDF_BYTES:
            data = f.read_bytes()
            if data[:4] == b"%PDF" and b"REFERENCE ONLY" not in data[:200]:
                return {
                    "is_duplicate": True,
                    "kind": "SAME_CITATION_DIFFERENT_FILE"
                    if new_hash and existing_hash and new_hash != existing_hash
                    else "ALREADY_EXISTS",
                    "existing_file": str(f),
                    "existing_hash": existing_hash,
                    "action": "SKIP" if not new_hash else "VERSION_CHECK",
                }
    return {"is_duplicate": False}


def _next_version_path(base: Path) -> Path:
    """Tab_01_Name_cite.pdf -> _v2, _v3, ..."""
    if not base.exists():
        return base
    stem, suf = base.stem, base.suffix
    # strip existing _vN
    stem = re.sub(r"_v\d+$", "", stem)
    n = 2
    while True:
        cand = base.with_name(f"{stem}_v{n}{suf}")
        if not cand.exists():
            return cand
        n += 1


def download_case(
    citation: str,
    *,
    output_dir: Path,
    tab: int = 1,
    case_name: Optional[str] = None,
    canlii_url: Optional[str] = None,
    proposition: str = "",
    tags: Optional[list[str]] = None,
    config: Optional[DownloaderConfig] = None,
    fca_item_id: Optional[str] = None,
) -> DownloadResult:
    cfg = config or DownloaderConfig()
    output_dir.mkdir(parents=True, exist_ok=True)
    court = identify_court(citation)
    scc = lookup_scc(citation)
    name = case_name or (scc["name"] if scc else "Unknown")
    tags = list(tags or [])
    if cfg.tag_anchor_cases and name.lower() in (
        "cardinal v. kent institution",
        "cardinal",
        "vavilov",
        "dunsmuir",
        "baker",
    ):
        if "ANCHOR" not in tags:
            tags.append("ANCHOR")

    fname = f"Tab_{tab:02d}_{short_name(name)}_{citation_slug(citation)}.pdf"
    dest = output_dir / fname

    # duplicate / already exists
    dup = check_duplicate(citation, output_dir)
    if dup.get("is_duplicate") and dup.get("action") == "SKIP":
        existing = Path(dup["existing_file"])
        data = existing.read_bytes() if existing.suffix == ".pdf" else b""
        return DownloadResult(
            tab=tab,
            citation=citation,
            case_name=name,
            court=court,
            status="ALREADY_EXISTS" if dup.get("kind") != "EXACT_DUPLICATE" else "DUPLICATE",
            path=str(existing),
            bytes_size=existing.stat().st_size if existing.exists() else 0,
            sha256=sha256_file(existing) if existing.suffix == ".pdf" and existing.exists() else None,
            message=f"Skip: {dup.get('kind')}",
            tags=tags,
            retrieved_at=_utcnow(),
            proposition=proposition,
            jurisdiction=_jurisdiction(court),
        )

    # --- SCC path ---
    if court == "SCC" and scc:
        item_id = scc["item_id"]
        last_code = 0
        for doc in (1, 2, 3):
            url = scc_pdf_url(item_id, doc)
            code, data, ctype = _http_get(url)
            last_code = code
            ok, why = _is_valid_pdf(data)
            if code == 200 and ok:
                # version tracking
                write_path = dest
                version = 1
                if dest.exists():
                    old_h = sha256_file(dest)
                    new_h = sha256_bytes(data)
                    if old_h == new_h:
                        return DownloadResult(
                            tab=tab,
                            citation=citation,
                            case_name=name,
                            court=court,
                            status="ALREADY_EXISTS",
                            path=str(dest),
                            url=url,
                            bytes_size=len(data),
                            sha256=new_h,
                            message="Identical file already present",
                            tags=tags,
                            retrieved_at=_utcnow(),
                            version=1,
                            jurisdiction="federal",
                            proposition=proposition,
                        )
                    write_path = _next_version_path(dest)
                    version = int(re.search(r"_v(\d+)$", write_path.stem).group(1)) if re.search(r"_v(\d+)$", write_path.stem) else 2
                write_path.write_bytes(data)
                scanned = is_scanned_pdf(write_path)
                ocr_path = None
                msg = f"Downloaded SCC item {item_id} doc={doc}"
                if scanned and cfg.include_ocr:
                    ocr_out = write_path.with_suffix(".ocr.txt")
                    ocr_res = ocr_pdf(write_path, ocr_out)
                    if ocr_res.get("status") == "OCR_SUCCESS":
                        ocr_path = str(ocr_out)
                        msg += "; OCR_SUCCESS"
                    else:
                        msg += f"; {ocr_res.get('status')}"
                status = "SUCCESS"
                if version > 1:
                    status = "VERSION_UPDATE"
                return DownloadResult(
                    tab=tab,
                    citation=citation,
                    case_name=name,
                    court=court,
                    status=status,
                    path=str(write_path),
                    url=url,
                    bytes_size=len(data),
                    sha256=sha256_bytes(data),
                    message=msg,
                    is_scanned=scanned,
                    ocr_text_path=ocr_path,
                    version=version,
                    tags=tags,
                    retrieved_at=_utcnow(),
                    jurisdiction="federal",
                    proposition=proposition,
                    access_status="public",
                )
            if code in (400, 404):
                continue
            if code == 403:
                break
        url = scc_pdf_url(item_id, 1)
        note = scc.get("note", "")
        reason = f"SCC fetch failed (HTTP {last_code})"
        if note == "provisional_id":
            reason += " — provisional item ID may be wrong; search decisions.scc-csc.ca"
        if not cfg.include_reference_pdfs:
            return DownloadResult(
                tab=tab,
                citation=citation,
                case_name=name,
                court=court,
                status="HTTP_400" if last_code == 400 else "HTTP_404",
                url=url,
                message=reason,
                tags=tags,
                retrieved_at=_utcnow(),
            )
        write_reference_pdf(
            dest,
            citation=citation,
            case_name=name,
            court=court,
            url=url,
            reason=reason,
            proposition=proposition,
        )
        return DownloadResult(
            tab=tab,
            citation=citation,
            case_name=name,
            court=court,
            status="REFERENCE_PDF",
            path=str(dest),
            url=url,
            bytes_size=dest.stat().st_size,
            message=reason,
            tags=tags,
            retrieved_at=_utcnow(),
            proposition=proposition,
            access_status="reference_pdf",
            jurisdiction="federal",
        )

    # --- FCA optional ---
    if court == "FCA" and fca_item_id:
        url = fca_pdf_url(fca_item_id)
        code, data, _ = _http_get(url)
        ok, why = _is_valid_pdf(data)
        if code == 200 and ok:
            dest.write_bytes(data)
            return DownloadResult(
                tab=tab,
                citation=citation,
                case_name=name,
                court=court,
                status="SUCCESS",
                path=str(dest),
                url=url,
                bytes_size=len(data),
                sha256=sha256_bytes(data),
                message="FCA download",
                tags=tags,
                retrieved_at=_utcnow(),
                jurisdiction="federal",
            )

    # --- BC / CanLII / unknown: no Cloudflare bypass ---
    url = canlii_url or canlii_search_url(citation)
    if court in ("BCCA", "BCSC"):
        reason = (
            "BC Courts automated download often blocked — open CanLII/courts.gov.bc.ca manually"
        )
        status = "BLOCKED_CLOUDFLARE"
    elif court == "SCC" and not scc:
        reason = "SCC item ID not in verified database — resolve ID on decisions.scc-csc.ca"
        status = "REFERENCE_PDF"
        url = "https://decisions.scc-csc.ca/"
    else:
        reason = "CanLII automated access blocked (Cloudflare) — do not retry; open URL manually"
        status = "BLOCKED_CLOUDFLARE"

    if not cfg.include_reference_pdfs:
        return DownloadResult(
            tab=tab,
            citation=citation,
            case_name=name,
            court=court,
            status=status,
            url=url,
            message=reason,
            tags=tags,
            retrieved_at=_utcnow(),
        )

    write_reference_pdf(
        dest,
        citation=citation,
        case_name=name,
        court=court,
        url=url,
        reason=reason,
        proposition=proposition,
    )
    return DownloadResult(
        tab=tab,
        citation=citation,
        case_name=name,
        court=court,
        status="REFERENCE_PDF" if status == "BLOCKED_CLOUDFLARE" else status,
        path=str(dest),
        url=url,
        bytes_size=dest.stat().st_size,
        message=reason,
        tags=tags,
        retrieved_at=_utcnow(),
        proposition=proposition,
        access_status="reference_pdf",
        jurisdiction=_jurisdiction(court),
    )


def download_batch(
    cases: list[dict[str, Any]],
    output_dir: Path,
    *,
    config: Optional[DownloaderConfig] = None,
    progress: Optional[Callable[[int, int, DownloadResult], None]] = None,
) -> list[DownloadResult]:
    cfg = config or DownloaderConfig()
    cfg.output_dir = output_dir
    cases_dir = output_dir / "cases"
    cases_dir.mkdir(parents=True, exist_ok=True)
    audit_path = output_dir / "audit.log"
    results: list[DownloadResult] = []
    n = len(cases)

    for i, c in enumerate(cases, 1):
        tab = int(c.get("tab") or i)
        res = download_case(
            str(c["citation"]),
            output_dir=cases_dir,
            tab=tab,
            case_name=c.get("name"),
            canlii_url=c.get("canlii_url"),
            proposition=str(c.get("proposition") or ""),
            tags=list(c.get("tags") or []),
            config=cfg,
            fca_item_id=c.get("fca_item_id"),
        )
        results.append(res)
        line = (
            f"{_utcnow()} | COURT_DOWNLOAD | {res.case_name} | {res.citation} | "
            f"{res.status} | {res.bytes_size} bytes | "
            f"sha256:{(res.sha256 or '')[:16]} | {res.url or ''}\n"
        )
        with audit_path.open("a", encoding="utf-8") as f:
            f.write(line)
        if progress:
            progress(i, n, res)
        else:
            bar = "#" * int(20 * i / max(n, 1)) + "-" * (20 - int(20 * i / max(n, 1)))
            mark = "OK" if res.status in ("SUCCESS", "ALREADY_EXISTS") else "!!"
            print(f"[{bar}] {i}/{n} Tab {tab:02d} | {res.case_name[:20]:20s} | {mark} {res.status}")
        if i < n:
            time.sleep(max(cfg.batch_delay_seconds, DEFAULT_BATCH_DELAY))

    write_reports(output_dir, results, matter=cfg.matter)
    return results


def write_reports(
    output_dir: Path,
    results: list[DownloadResult],
    *,
    matter: str = "",
) -> None:
    counts: dict[str, int] = {}
    for r in results:
        counts[r.status] = counts.get(r.status, 0) + 1

    manifest = {
        "generated_at": _utcnow(),
        "matter": matter,
        "total_tabs": len(results),
        "downloaded": counts.get("SUCCESS", 0) + counts.get("VERSION_UPDATE", 0),
        "reference_pdfs": counts.get("REFERENCE_PDF", 0) + counts.get("BLOCKED_CLOUDFLARE", 0),
        "failed": sum(
            counts.get(k, 0)
            for k in ("HTTP_400", "HTTP_404", "HTTP_403", "SMALL_FILE", "NOT_PDF")
        ),
        "duplicates_skipped": counts.get("DUPLICATE", 0) + counts.get("ALREADY_EXISTS", 0),
        "counts": counts,
        "tabs": [r.to_metadata() for r in results],
    }
    (output_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )

    with (output_dir / "table_of_authorities.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(
            ["Tab", "Case Name", "Citation", "Court", "Status", "File", "CanLII/Source URL"]
        )
        for r in results:
            w.writerow(
                [
                    r.tab,
                    r.case_name,
                    r.citation,
                    r.court,
                    r.status,
                    r.path or "",
                    r.url or "",
                ]
            )

    summary_lines = [
        f"Download summary — {_utcnow()}",
        f"Matter: {matter or '(none)'}",
        f"Total tabs: {len(results)}",
        f"SUCCESS / VERSION_UPDATE: {manifest['downloaded']}",
        f"REFERENCE / BLOCKED: {manifest['reference_pdfs']}",
        f"Duplicates/existing skipped: {manifest['duplicates_skipped']}",
        f"Failed: {manifest['failed']}",
        "",
    ]
    for r in results:
        tag = " (ANCHOR)" if "ANCHOR" in r.tags else ""
        summary_lines.append(
            f"  Tab {r.tab:02d} | {r.case_name}{tag} | {r.status} | {r.bytes_size} bytes"
        )
    (output_dir / "download_summary.txt").write_text(
        "\n".join(summary_lines), encoding="utf-8"
    )

    missing = [
        r
        for r in results
        if r.status
        not in ("SUCCESS", "ALREADY_EXISTS", "DUPLICATE", "VERSION_UPDATE", "REFERENCE_PDF", "BLOCKED_CLOUDFLARE")
    ]
    (output_dir / "missing_authorities.txt").write_text(
        "\n".join(f"{r.citation} | {r.status} | {r.message}" for r in missing) or "(none)",
        encoding="utf-8",
    )
    denied = [
        r
        for r in results
        if r.status in ("REFERENCE_PDF", "BLOCKED_CLOUDFLARE", "HTTP_403")
    ]
    (output_dir / "access_denied.txt").write_text(
        "\n".join(
            f"{r.citation} | {r.url or ''} | {r.message}" for r in denied
        )
        or "(none)",
        encoding="utf-8",
    )
    dups = [r for r in results if r.status in ("DUPLICATE", "ALREADY_EXISTS")]
    (output_dir / "duplicates.txt").write_text(
        "\n".join(f"{r.citation} | {r.path} | {r.status}" for r in dups) or "(none)",
        encoding="utf-8",
    )


if __name__ == "__main__":
    import sys

    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1] / "outputs"
    cits = sys.argv[2:] or ["2019 SCC 65"]
    cases = [{"citation": c, "tab": i + 1} for i, c in enumerate(cits)]
    download_batch(cases, out, config=DownloaderConfig(matter="cli-test"))
