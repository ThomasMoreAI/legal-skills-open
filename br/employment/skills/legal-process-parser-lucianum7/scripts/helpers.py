from __future__ import annotations

import hashlib
import json
import re
import shutil
import unicodedata
import zipfile
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Iterator, Sequence


INJECTION_PATTERNS = [
    r"ignore\s+(?:suas|as|all)\s+instru(?:ções|ctions)",
    r"reveal\s+(?:your|internal)|reveal\s+informa",
    r"execute\s+(?:este|this)\s+comando",
    r"envie\s+(?:os|these|the)\s+documentos",
    r"system\s+prompt|developer\s+message",
]

DATE_RE = re.compile(r"\b(?:[0-3]?\d)[/.-](?:0?[1-9]|1[0-2])[/.-](?:\d{2}|\d{4})\b")
NUMBER_PROCESS_RE = re.compile(r"\b\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4}\b")
COURT_PAGE_RE = re.compile(r"(?:fl\.?|folha|p[áa]g(?:ina)?\s+dos\s+autos)\s*[:.]?\s*(\d{1,5})", re.I)

PIECE_PATTERNS: list[tuple[str, tuple[str, ...]]] = [
    ("Peti\u00e7\u00e3o Inicial", ("peti\u00e7\u00e3o inicial", "inicial")),
    ("Emenda \u00e0 Inicial", ("emenda", "emenda \u00e0 inicial")),
    ("Contesta\u00e7\u00e3o", ("contesta\u00e7\u00e3o", "defesa")),
    ("Reconven\u00e7\u00e3o", ("reconven\u00e7\u00e3o",)),
    ("R\u00e9plica", ("r\u00e9plica", "impugna\u00e7\u00e3o \u00e0 contesta\u00e7\u00e3o")),
    ("Manifesta\u00e7\u00e3o", ("manifesta\u00e7\u00e3o",)),
    ("Raz\u00f5es Finais", ("raz\u00f5es finais", "alega\u00e7\u00f5es finais")),
    ("Contrarraz\u00f5es", ("contrarraz\u00f5es",)),
    ("Recurso", ("recurso", "raz\u00f5es recursais")),
    ("Senten\u00e7a", ("senten\u00e7a",)),
    ("Ac\u00f3rd\u00e3o", ("ac\u00f3rd\u00e3o",)),
    ("Decis\u00e3o", ("decis\u00e3o", "decis\u00e3o monocr\u00e1tica")),
    ("Despacho", ("despacho",)),
    ("Certid\u00e3o", ("certid\u00e3o",)),
    ("Laudo/Per\u00edcia", ("laudo", "per\u00edcia", "per\u00edcia")),
    ("Contrato", ("contrato",)),
    ("Procura\u00e7\u00e3o", ("procura\u00e7\u00e3o",)),
    ("Documento Financeiro", ("extrato", "holerite", "comprovante", "nota fiscal", "pix")),
    ("Documento M\u00e9dico", ("atestado", "prontu\u00e1rio", "laudo m\u00e9dico", "aso")),
    ("Documento", ("documento",)),
]


@dataclass
class Page:
    pdf_page: int
    text: str
    source: str = "native_text"
    quality: str = "high"
    court_page: int | None = None
    piece: str = "N\u00e3o identificado"
    document_id: str = ""
    dates: list[str] | None = None
    warnings: list[str] | None = None
    summary: str = ""
    entities: dict[str, list[str]] | None = None
    keywords: list[str] | None = None
    content_blocks: list[dict[str, Any]] | None = None
    visuals: list[dict[str, Any]] | None = None
    render: dict[str, Any] | None = None
    vision: dict[str, Any] | None = None
    ocr: dict[str, Any] | None = None
    consolidation: dict[str, Any] | None = None
    status: str = "PARTIAL"

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["dates"] = self.dates or []
        data["warnings"] = self.warnings or []
        data["entities"] = self.entities or {}
        data["keywords"] = self.keywords or []
        data["content_blocks"] = self.content_blocks or []
        data["visuals"] = self.visuals or []
        data["render"] = self.render or {}
        data["vision"] = self.vision or {}
        data["ocr"] = self.ocr or {}
        data["consolidation"] = self.consolidation or {}
        return data


def now_utc() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(chunk_size):
            digest.update(chunk)
    return digest.hexdigest()


def read_text_lossless(path: Path) -> str:
    raw = path.read_bytes()
    for encoding in ("utf-8-sig", "utf-8", "cp1252", "latin-1"):
        try:
            return raw.decode(encoding)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace")


def _extract_pdf_with_library(path: Path) -> list[str] | None:
    reader_cls = None
    try:
        from pypdf import PdfReader  # type: ignore

        reader_cls = PdfReader
    except Exception:
        try:
            from PyPDF2 import PdfReader  # type: ignore

            reader_cls = PdfReader
        except Exception:
            return None
    try:
        reader = reader_cls(str(path))
        return [(page.extract_text() or "") for page in reader.pages]
    except Exception:
        return None


def extract_pages(path: Path) -> tuple[list[str], list[str]]:
    """Return page texts and extraction warnings without invoking document code."""
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        pages = _extract_pdf_with_library(path)
        if pages is None:
            return [], ["PDF sem extrator disponível; instale pypdf ou PyPDF2."]
        return pages, []
    text = read_text_lossless(path)
    # Form feed is a portable page separator for fixtures and exported text.
    pages = text.split("\f") if "\f" in text else [text]
    return pages, []


def _ocr_missing_pdf_pages(path: Path, pages: list[str], language: str, dpi: int) -> tuple[list[str], list[int], list[str]]:
    """OCR only pages that lack useful native text, when explicitly enabled."""
    try:
        from pdf2image import convert_from_path  # type: ignore
        import pytesseract  # type: ignore
    except Exception:
        return pages, [], ["OCR solicitado, mas pdf2image/pytesseract não estão instalados."]
    ocr_pages: list[int] = []
    warnings: list[str] = []
    for number, text in enumerate(pages, start=1):
        if len(normalise_spaces(text)) >= 30:
            continue
        try:
            images = convert_from_path(str(path), dpi=dpi, first_page=number, last_page=number, fmt="png")
            if not images:
                warnings.append(f"PDF p. {number}: OCR não retornou imagem.")
                continue
            recognised = pytesseract.image_to_string(images[0], lang=language) or ""
            if recognised.strip():
                pages[number - 1] = recognised
                ocr_pages.append(number)
            else:
                warnings.append(f"PDF p. {number}: OCR não encontrou texto.")
        except Exception as exc:
            warnings.append(f"PDF p. {number}: falha de OCR ({type(exc).__name__}).")
    return pages, ocr_pages, warnings


def extract_pages_with_ocr(path: Path, use_ocr: bool = False, ocr_language: str = "por+eng", ocr_dpi: int = 200) -> tuple[list[str], list[str], list[int]]:
    """Return page texts, warnings and pages filled by explicitly requested OCR."""
    pages, warnings = extract_pages(path)
    if path.suffix.lower() != ".pdf" or not use_ocr or not pages:
        return pages, warnings, []
    pages, ocr_pages, ocr_warnings = _ocr_missing_pdf_pages(path, pages, ocr_language, ocr_dpi)
    return pages, [*warnings, *ocr_warnings], ocr_pages


def normalise_spaces(value: str) -> str:
    value = value.replace("\x00", "")
    value = unicodedata.normalize("NFC", value)
    return re.sub(r"[ \t]+", " ", value).strip()


def detect_injection(text: str) -> list[str]:
    findings: list[str] = []
    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, text, flags=re.I):
            findings.append(pattern)
    return findings


def page_quality(text: str) -> tuple[str, list[str]]:
    stripped = normalise_spaces(text)
    warnings: list[str] = []
    if not stripped:
        return "unreadable", ["página sem texto extraído; requer visão/OCR"]
    if len(stripped) < 30:
        warnings.append("texto muito curto")
    replacement_ratio = stripped.count("�") / max(1, len(stripped))
    if replacement_ratio > 0.01:
        warnings.append("possível encoding corrompido")
    symbols = sum(1 for char in stripped if not char.isalnum() and not char.isspace())
    if symbols / max(1, len(stripped)) > 0.45:
        warnings.append("alta concentração de símbolos")
    if warnings:
        return "low", warnings
    return "high", []


def detect_piece(text: str, current: str = "N\u00e3o identificado") -> str:
    sample = normalise_spaces(text[:1200]).lower()
    for label, terms in PIECE_PATTERNS:
        if any(term in sample for term in terms):
            return label
    return current


def make_document_id(text: str, page: int) -> str:
    return hashlib.sha256(f"{page}\0{text}".encode("utf-8", errors="replace")).hexdigest()[:12]


def build_pages(
    texts: Sequence[str],
    ocr_pages: Iterable[int] | None = None,
    visuals_by_page: dict[int, list[dict[str, Any]]] | None = None,
    render_by_page: dict[int, dict[str, Any]] | None = None,
    page_descriptions: dict[int, dict[str, Any]] | None = None,
    source_kind: str = "",
    vision_mode: str = "always",
    vision_provider: str = "none",
    ocr_requested: bool = False,
    vision_policy: str = "best_effort",
) -> tuple[list[Page], list[str]]:
    pages: list[Page] = []
    injections: list[str] = []
    current_piece = "N\u00e3o identificado"
    ocr_page_set = set(ocr_pages or [])
    for number, raw in enumerate(texts, start=1):
        text = raw.replace("\r\n", "\n").replace("\r", "\n")
        quality, warnings = page_quality(text)
        piece = detect_piece(text, current_piece)
        if piece != "N\u00e3o identificado":
            current_piece = piece
        match = COURT_PAGE_RE.search(text[:2000])
        dates = DATE_RE.findall(text)
        findings = detect_injection(text)
        if findings:
            injections.extend([f"PDF p. {number}: {pattern}" for pattern in findings])
            warnings = [*warnings, "possível prompt injection tratado como conteúdo documental"]
        page_visuals = (visuals_by_page or {}).get(number, [])
        semantics = extract_page_semantics(number, text, current_piece, page_visuals)
        processing = build_page_processing_state(
            page_number=number,
            text=text,
            page_visuals=page_visuals,
            ocr_pages=ocr_page_set,
            render= (render_by_page or {}).get(number),
            page_description=(page_descriptions or {}).get(number),
            source_kind=source_kind,
            vision_mode=vision_mode,
            vision_provider=vision_provider,
            ocr_requested=ocr_requested,
            vision_policy=vision_policy,
        )
        page = Page(
            pdf_page=number,
            text=text,
            source="ocr" if number in ocr_page_set else ("native_text" if text.strip() else "needs_ocr_or_vision"),
            quality=quality,
            court_page=int(match.group(1)) if match else None,
            piece=current_piece,
            document_id=make_document_id(text, number),
            dates=dates,
            warnings=warnings,
            summary=semantics["summary"],
            entities=semantics["entities"],
            keywords=semantics["keywords"],
            content_blocks=semantics["content_blocks"],
            visuals=page_visuals,
            render=processing["render"],
            vision=processing["vision"],
            ocr=processing["ocr"],
            consolidation=processing["consolidation"],
            status=processing["status"],
        )
        pages.append(page)
    return pages, injections


def page_reference(page: Page) -> str:
    reference = f"PDF p. {page.pdf_page}"
    if page.court_page is not None:
        reference += f" | fl. {page.court_page}"
    return reference


def identify_pieces(pages: Sequence[Page]) -> list[dict[str, Any]]:
    pieces: list[dict[str, Any]] = []
    for page in pages:
        if pieces and pieces[-1]["piece"] == page.piece:
            pieces[-1]["pdf_page_end"] = page.pdf_page
            pieces[-1]["pdf_page_count"] += 1
            pieces[-1]["document_ids"].append(page.document_id)
            continue
        piece_number = len(pieces) + 1
        pieces.append(
            {
                "id": f"P{piece_number:03d}",
                "piece": page.piece,
                "party_or_origin": "Não identificado nos autos",
                "date": page.dates[0] if page.dates else None,
                "pdf_page_start": page.pdf_page,
                "pdf_page_end": page.pdf_page,
                "court_pages": [page.court_page] if page.court_page else [],
                "pdf_page_count": 1,
                "document_ids": [page.document_id],
            }
        )
    for piece in pieces:
        piece["court_page_start"] = min(piece["court_pages"]) if piece["court_pages"] else None
        piece["court_page_end"] = max(piece["court_pages"]) if piece["court_pages"] else None
        piece.pop("court_pages", None)
    return pieces


def build_index_records(pages: Sequence[Page], process_id: str) -> Iterator[dict[str, Any]]:
    for page in pages:
        yield {
            "process": process_id,
            "piece": page.piece,
            "pdf_page": page.pdf_page,
            "court_page": page.court_page,
            "document_id": page.document_id,
            "quality": page.quality,
            "source": page.source,
            "text": page.text,
            "summary": page.summary,
            "entities": page.entities or {},
            "keywords": page.keywords or [],
            "visuals": page.visuals or [],
            "terms": sorted(set(re.findall(r"[\wÀ-ÿ]{3,}", page.text.lower(), flags=re.UNICODE))),
        }


def classify_process(pages: Sequence[Page]) -> dict[str, Any]:
    text = "\n".join(page.text for page in pages)
    lower = text.lower()
    areas: list[str] = []
    for keyword, area in [
        ("trabalh", "Direito do Trabalho"),
        ("previd", "Direito Previdenciário"),
        ("consumidor", "Direito do Consumidor"),
        ("bancár", "Direito Bancário"),
        ("tribut", "Direito Tributário"),
        ("penal", "Direito Penal"),
        ("criminal", "Direito Penal"),
        ("família", "Direito de Família"),
        ("administrativ", "Direito Administrativo"),
        ("ambiental", "Direito Ambiental"),
        ("empresarial", "Direito Empresarial"),
        ("civil", "Direito Civil"),
    ]:
        if keyword in lower and area not in areas:
            areas.append(area)
    process_match = NUMBER_PROCESS_RE.search(text)
    return {
        "sistema_juridico": "Brasil" if any(term in lower for term in ("tribunal", "comarca", "jus.br", "cnj")) else "Não identificado nos autos",
        "pais": "Brasil" if "brasil" in lower or "jus.br" in lower else "Não identificado nos autos",
        "justica": "Não identificado nos autos",
        "tribunal": "Não identificado nos autos",
        "orgao_julgador": "Não identificado nos autos",
        "competencia": "Não identificado nos autos",
        "numero_processo": process_match.group(0) if process_match else "Não identificado nos autos",
        "classe_processual": "Não identificado nos autos",
        "procedimento": "Não identificado nos autos",
        "rito": "Não identificado nos autos",
        "instancia": "Não identificado nos autos",
        "fase_processual": "Não identificado nos autos",
        "area_principal": areas[0] if areas else "Não identificado nos autos",
        "areas_correlatas": areas[1:],
        "autor_requerente": "Não identificado nos autos",
        "reu_requerido": "Não identificado nos autos",
        "terceiros": [],
        "advogados": [],
        "peritos": [],
        "ministerio_publico": "Não identificado nos autos",
        "demais_intervenientes": [],
        "objeto_principal": "Não identificado nos autos",
        "pedidos_principais": [],
        "materias_controvertidas": [],
        "situacao_atual": "Não identificado nos autos",
    }


def build_structured_markdown(pages: Sequence[Page], classification: dict[str, Any]) -> str:
    lines = ["# PROCESSO ESTRUTURADO", "", "## Classificação inicial", "", "```yaml"]
    for key, value in classification.items():
        lines.append(f"{key}: {json.dumps(value, ensure_ascii=False)}")
    lines.extend(["```", "", "## Páginas", ""])
    for page in pages:
        lines.extend(
            [
                "---",
                "",
                f"## [Página PDF {page.pdf_page}]",
                "",
                f"**Folha indicada nos autos:** {page.court_page if page.court_page is not None else 'não identificada'}",
                f"**Peça:** {page.piece}",
                f"**Documento ID:** {page.document_id}",
                f"**Data identificada:** {page.dates[0] if page.dates else 'não identificada'}",
                f"**Qualidade da extração:** {page.quality}",
                "",
                page.text.rstrip() or "[ILEGÍVEL]",
                "",
            ]
        )
        if page.warnings:
            lines.extend([f"**Observações:** {'; '.join(page.warnings)}", ""])
    return "\n".join(lines).rstrip() + "\n"


def build_pieces_markdown(pieces: Sequence[dict[str, Any]]) -> str:
    lines = ["# ÍNDICE PROCESSUAL", "", "| ID | Peça | Parte/Origem | Data | Página inicial | Página final |", "|---|---|---|---|---:|---:|"]
    for piece in pieces:
        lines.append(f"| {piece['id']} | {piece['piece']} | {piece['party_or_origin']} | {piece['date'] or '—'} | {piece['pdf_page_start']} | {piece['pdf_page_end']} |")
    return "\n".join(lines) + "\n"


def build_chronology(pages: Sequence[Page]) -> str:
    events: list[tuple[str, Page]] = []
    for page in pages:
        for date in page.dates or []:
            events.append((date, page))
    lines = ["# CRONOLOGIA PROCESSUAL", "", "| Data | Evento/trecho | Fonte |", "|---|---|---|"]
    for date, page in sorted(events, key=lambda item: (item[0], item[1].pdf_page)):
        snippet = normalise_spaces(page.text).replace("|", "\\|")[:180] or "Data identificada sem texto legível"
        lines.append(f"| {date} | {snippet} | [{page.piece} | {page_reference(page)}] |")
    if not events:
        lines.append("| Não identificado | Nenhuma data inequívoca localizada | — |")
    return "\n".join(lines) + "\n"


def build_controversy_matrix(pages: Sequence[Page]) -> str:
    rows: list[str] = []
    cues = [
        ("pedido", "Pedidos mencionados"),
        ("prova", "Provas mencionadas"),
        ("impugna", "Impugnações mencionadas"),
        ("prescrição", "Prescrição mencionada"),
        ("responsabilidade", "Responsabilidade mencionada"),
    ]
    for cue, label in cues:
        matches = [page for page in pages if cue in page.text.lower()]
        if matches:
            source = "; ".join(f"{page_reference(page)}" for page in matches[:5])
            rows.append(f"| {label} | {len(matches)} página(s) com menção | {source} | Necessita conferência |")
    lines = ["# MATRIZ DE CONTROVÉRSIAS", "", "| Núcleo | Indício documental | Fontes | Status |", "|---|---|---|---|"]
    return "\n".join(lines + (rows or ["| Não identificado | Não foram localizados núcleos por heurística | — | Necessita conferência |"])) + "\n"


def build_audit_report(pages: Sequence[Page], classification: dict[str, Any], pieces: Sequence[dict[str, Any]], coverage: dict[str, Any], mode: str) -> str:
    findings: list[str] = []
    for page in pages:
        for warning in page.warnings or []:
            findings.append(f"- **MÉDIO** — PDF p. {page.pdf_page}: {warning}.")
    if not findings:
        findings = ["- **INFORMATIVO** — Nenhum alerta heurístico de extração foi localizado."]
    pages_with_evidence = [page for page in pages if any(cue in page.text.lower() for cue in ("documento", "prova", "laudo", "contrato", "extrato"))]
    pages_with_decisions = [page for page in pages if any(cue in page.text.lower() for cue in ("sentença", "acórdão", "decisão", "despacho"))]
    lines = [
        "# RESUMO EXECUTIVO",
        "",
        f"**Área:** {classification['area_principal']}",
        f"**Fase:** {classification['fase_processual']}",
        f"**Páginas analisadas:** {coverage['pages_processed']} de {coverage['pages_total']}",
        f"**Modo:** {mode}",
        "",
        "# ACHADOS PRIORITÁRIOS",
        "",
        *findings,
        "",
        "# 1. IDENTIFICAÇÃO DO PROCESSO",
        "",
        f"- Número: {classification['numero_processo']}",
        "- Partes: não identificadas automaticamente; conferir nos autos.",
        "",
        "# 2. CLASSIFICAÇÃO JURÍDICA",
        "",
        "```json",
        json.dumps(classification, ensure_ascii=False, indent=2),
        "```",
        "",
        "# 3. PEÇAS E PROVAS",
        "",
        f"- Peças/segmentos: {len(pieces)}.",
        f"- Páginas com menções probatórias: {len(pages_with_evidence)}.",
        f"- Páginas com decisões: {len(pages_with_decisions)}.",
        "- Alegações não são tratadas como prova; autenticidade não é presumida.",
        "",
        "# 4. DOCUMENTOS AUSENTES OU NÃO LOCALIZADOS",
        "",
        "Registrar manualmente toda referência a anexo não encontrado; esta versão não presume ausência a partir de uma heurística.",
        "",
        "# 5. PONTOS QUE EXIGEM CONFERÊNCIA HUMANA",
        "",
        "- Conferir classificação, partes, fase, autenticidade, documentos ilegíveis e qualquer conclusão estratégica.",
        "- Se a cobertura não for integral, tratar conclusões como provisórias.",
        "",
        "# COBERTURA DA EXTRAÇÃO",
        "",
        f"Páginas existentes: {coverage['pages_total']}",
        f"Páginas processadas: {coverage['pages_processed']}",
        f"Páginas com texto nativo: {coverage['pages_native_text']}",
        f"Páginas submetidas à visão/OCR: {coverage['pages_ocr_or_vision']}",
        f"Páginas com leitura parcial: {coverage['pages_partial']}",
        f"Páginas ilegíveis: {coverage['pages_unreadable']}",
        f"Cobertura: {coverage['coverage_percent']}% das páginas representadas no pipeline.",
    ]
    if coverage["pages_processed"] < coverage["pages_total"]:
        lines.extend(["", "## ATENÇÃO — PROCESSAMENTO INCOMPLETO", "", "As conclusões dependentes das páginas pendentes são provisórias."])
    return "\n".join(lines) + "\n"


def write_json(path: Path, value: Any, encoding: str = "utf-8") -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding=encoding)


def write_jsonl(path: Path, records: Iterable[dict[str, Any]], encoding: str = "utf-8") -> int:
    count = 0
    with path.open("w", encoding=encoding, newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
            count += 1
    return count


def compute_coverage(pages: Sequence[Page], total: int) -> dict[str, Any]:
    processed = len(pages)
    native = sum(page.source == "native_text" and bool(page.text.strip()) for page in pages)
    ocr = sum(page.source != "native_text" for page in pages)
    partial = sum(page.quality == "low" for page in pages)
    unreadable = sum(page.quality == "unreadable" for page in pages)
    return {
        "pages_total": total,
        "pages_processed": processed,
        "pages_native_text": native,
        "pages_ocr_or_vision": ocr,
        "pages_partial": partial,
        "pages_unreadable": unreadable,
        "pages_pending": list(range(processed + 1, total + 1)),
        "coverage_percent": round(100 * processed / total, 2) if total else 0,
    }


def copy_original(source: Path, output: Path) -> Path:
    output.mkdir(parents=True, exist_ok=True)
    digest = sha256_file(source)
    target = output / "original" / f"{digest[:16]}-{source.name}"
    target.parent.mkdir(parents=True, exist_ok=True)
    if not target.exists() or sha256_file(target) != sha256_file(source):
        shutil.copy2(source, target)
    return target


# ASCII-safe overrides keep regex matching reliable on Windows consoles whose
# default code page is not UTF-8. Python's regex engine expands ``\u`` escapes.
INJECTION_PATTERNS = [
    r"ignore\s+(?:suas|as|all)\s+instru(?:\u00e7\u00f5es|ctions)",
    r"reveal\s+(?:your|internal)|reveal\s+informa",
    r"execute\s+(?:este|this)\s+comando",
    r"envie\s+(?:os|these|the)\s+documentos",
    r"system\s+prompt|developer\s+message",
]
COURT_PAGE_RE = re.compile(r"(?:fl\.?|folha|p[\u00e1a]g(?:ina)?\s+dos\s+autos)\s*[:.]?\s*(\d{1,5})", re.I)


IMAGE_MARKDOWN_RE = re.compile(r"!\[([^]]*)\]\(([^)]+)\)")
PROCESS_ID_RE = re.compile(r"\b\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4}\b")
CPF_CNPJ_RE = re.compile(r"\b(?:\d{3}\.\d{3}\.\d{3}-\d{2}|\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2})\b")
CURRENCY_RE = re.compile(r"\bR\$\s?[\d.]+(?:,\d{2})?\b|\b\d+(?:[.,]\d{2})?\s?(?:BRL|reais)\b", re.I)
EMAIL_RE = re.compile(r"\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b")


def _image_dimensions(data: bytes) -> tuple[int | None, int | None]:
    try:
        from PIL import Image  # type: ignore
        from io import BytesIO

        with Image.open(BytesIO(data)) as image:
            return image.width, image.height
    except Exception:
        return None, None


def _ocr_image_bytes(data: bytes, language: str = "por+eng") -> str:
    try:
        from PIL import Image  # type: ignore
        from io import BytesIO
        import pytesseract  # type: ignore

        with Image.open(BytesIO(data)) as image:
            return (pytesseract.image_to_string(image, lang=language) or "").strip()
    except Exception:
        return ""


def _visual_fallback_description(record: dict[str, Any]) -> str:
    if record.get("semantic_description"):
        return str(record["semantic_description"])
    kind = record.get("kind", "elemento visual")
    if record.get("ocr_text"):
        text = normalise_spaces(str(record["ocr_text"]))[:1200]
        return f"{kind.capitalize()} documental associado à página. Texto visual legível identificado por OCR: {text}. A autenticidade e o significado jurídico não são presumidos."
    if kind == "page_scan":
        return "Página representada como imagem/rasterização, sem camada textual nativa suficiente. A descrição visual detalhada requer visão humana ou modelo multimodal; nenhum elemento foi inventado."
    dimensions = ""
    if record.get("width") and record.get("height"):
        dimensions = f" Dimensões extraídas: {record['width']}×{record['height']} px."
    return f"Imagem documental incorporada ao processo.{dimensions} Não foi possível identificar visualmente objetos, pessoas, valores ou texto com segurança neste ambiente; revisar com visão humana ou modelo multimodal."


def load_image_descriptions(path: Path | None) -> dict[str, dict[str, Any]]:
    """Load trusted, human/model-reviewed descriptions without executing their content."""
    if path is None or not path.exists():
        return {}
    try:
        raw = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError):
        return {}
    entries = raw.get("images", raw) if isinstance(raw, dict) else raw
    if isinstance(entries, dict):
        entries = [{"image_id": key, **(value if isinstance(value, dict) else {"semantic_description": value})} for key, value in entries.items()]
    result: dict[str, dict[str, Any]] = {}
    if not isinstance(entries, list):
        return result
    for entry in entries:
        if not isinstance(entry, dict) or not entry.get("image_id"):
            continue
        safe = {key: value for key, value in entry.items() if key in {"image_id", "semantic_description", "visible_text", "objects", "people", "tables", "location", "confidence", "description_source"}}
        if isinstance(safe.get("semantic_description"), str):
            result[str(safe["image_id"])] = safe
    return result


def extract_referenced_visuals(text: str, page_number: int, base_dir: Path | None = None, descriptions: dict[str, dict[str, Any]] | None = None) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for number, match in enumerate(IMAGE_MARKDOWN_RE.finditer(text), start=1):
        alt, reference = match.groups()
        image_id = f"P{page_number:04d}-I{number:03d}"
        record: dict[str, Any] = {
            "image_id": image_id,
            "page_pdf": page_number,
            "kind": "referenced_image",
            "source_reference": reference,
            "alt_text": alt or "não informado",
            "location": "referência Markdown localizada no conteúdo da página",
            "description_source": "alt_text_or_fallback",
        }
        if base_dir and not reference.startswith(("http://", "https://", "data:")):
            candidate = (base_dir / reference).resolve()
            if candidate.is_file() and base_dir.resolve() in candidate.parents:
                record["image_path"] = str(candidate)
                record["relative_path"] = reference.replace("\\", "/")
                data = candidate.read_bytes()
                record["sha256"] = hashlib.sha256(data).hexdigest()
                record["width"], record["height"] = _image_dimensions(data)
        if descriptions and image_id in descriptions:
            record.update(descriptions[image_id])
            record["description_source"] = descriptions[image_id].get("description_source", "external_review")
        record["semantic_description"] = _visual_fallback_description(record)
        records.append(record)
    return records


def extract_pdf_visuals(path: Path, output_dir: Path, use_ocr: bool = False, ocr_language: str = "por+eng", descriptions: dict[str, dict[str, Any]] | None = None) -> dict[int, list[dict[str, Any]]]:
    """Extract embedded PDF images into derived files and create a per-page inventory."""
    try:
        from pypdf import PdfReader  # type: ignore
    except Exception:
        try:
            from PyPDF2 import PdfReader  # type: ignore
        except Exception:
            return {}
    try:
        reader = PdfReader(str(path))
    except Exception:
        return {}
    output_dir.mkdir(parents=True, exist_ok=True)
    by_page: dict[int, list[dict[str, Any]]] = {}
    for page_number, page in enumerate(reader.pages, start=1):
        images = list(getattr(page, "images", []) or [])
        records: list[dict[str, Any]] = []
        for image_number, image in enumerate(images, start=1):
            data = getattr(image, "data", b"") or b""
            if not data:
                continue
            original_name = str(getattr(image, "name", "image.bin"))
            suffix = Path(original_name).suffix.lower() or ".bin"
            image_id = f"P{page_number:04d}-I{image_number:03d}"
            target = output_dir / f"page-{page_number:04d}-{image_id}{suffix}"
            target.write_bytes(data)
            width, height = _image_dimensions(data)
            record: dict[str, Any] = {
                "image_id": image_id,
                "page_pdf": page_number,
                "kind": "embedded_image",
                "source_name": original_name,
                "image_path": str(target),
                "relative_path": f"images/{target.name}",
                "format": suffix.lstrip("."),
                "width": width,
                "height": height,
                "sha256": hashlib.sha256(data).hexdigest(),
                "location": f"imagem incorporada na página PDF {page_number}; coordenadas não expostas pelo extrator",
                "description_source": "technical_inventory",
                "ocr_text": _ocr_image_bytes(data, ocr_language) if use_ocr else "",
            }
            if descriptions and image_id in descriptions:
                record.update(descriptions[image_id])
                record["description_source"] = descriptions[image_id].get("description_source", "external_review")
            record["semantic_description"] = _visual_fallback_description(record)
            records.append(record)
        if not records:
            page_text = page.extract_text() or ""
            if not page_text.strip():
                image_id = f"P{page_number:04d}-SCAN"
                record = {
                    "image_id": image_id,
                    "page_pdf": page_number,
                    "kind": "page_scan",
                    "location": f"área integral da página PDF {page_number}",
                    "description_source": "page_scan_fallback",
                    "ocr_text": "",
                }
                if descriptions and image_id in descriptions:
                    record.update(descriptions[image_id])
                    record["description_source"] = descriptions[image_id].get("description_source", "external_review")
                record["semantic_description"] = _visual_fallback_description(record)
                records.append(record)
        if records:
            by_page[page_number] = records
    return by_page


def extract_page_semantics(page_number: int, text: str, piece: str, visuals: Sequence[dict[str, Any]] | None = None) -> dict[str, Any]:
    normalised = normalise_spaces(text)
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    headings = [line.lstrip("# ").strip() for line in lines if line.startswith("#") or (len(line) > 5 and line.upper() == line and any(char.isalpha() for char in line))]
    table_lines = [line for line in lines if "|" in line]
    blocks: list[dict[str, Any]] = []
    if headings:
        blocks.append({"type": "headings", "items": headings[:20]})
    if table_lines:
        blocks.append({"type": "table_or_tabular_text", "items": table_lines[:30]})
    entities = {
        "process_numbers": sorted(set(PROCESS_ID_RE.findall(text))),
        "dates": sorted(set(DATE_RE.findall(text))),
        "cpf_cnpj": sorted(set(CPF_CNPJ_RE.findall(text))),
        "currency_values": sorted(set(CURRENCY_RE.findall(text))),
        "emails": sorted(set(EMAIL_RE.findall(text))),
    }
    visual_terms = " ".join(str(record.get("ocr_text", "")) for record in visuals or [])
    keywords = sorted(set(re.findall(r"[\wÀ-ÿ]{4,}", f"{text} {visual_terms}".lower(), flags=re.UNICODE)))[:120]
    if normalised:
        summary = f"Página PDF {page_number} da peça '{piece}'. Conteúdo textual localizado: {normalised[:400]}"
    elif visuals:
        summary = f"Página PDF {page_number} da peça '{piece}' sem texto nativo suficiente; {len(visuals)} elemento(s) visual(is) inventariado(s)."
    else:
        summary = f"Página PDF {page_number} da peça '{piece}' sem texto ou elemento visual extraído; requer conferência."
    return {"summary": summary, "entities": entities, "keywords": keywords, "content_blocks": blocks}


# Rich output overrides keep the original public API while adding page-level
# navigation and visual semantics to every generated artifact.
def build_index_records(pages: Sequence[Page], process_id: str) -> Iterator[dict[str, Any]]:
    for page in pages:
        yield {
            "process": process_id,
            "piece": page.piece,
            "pdf_page": page.pdf_page,
            "court_page": page.court_page,
            "document_id": page.document_id,
            "quality": page.quality,
            "source": page.source,
            "text": page.text,
            "terms": sorted(set(re.findall(r"[\w\u00c0-\u00ff]{3,}", page.text.lower(), flags=re.UNICODE))),
            "summary": page.summary,
            "entities": page.entities or {},
            "keywords": page.keywords or [],
            "visuals": page.visuals or [],
        }


def build_structured_markdown(pages: Sequence[Page], classification: dict[str, Any]) -> str:
    lines = ["# PROCESSO ESTRUTURADO", "", "## Classifica\u00e7\u00e3o inicial", "", "```yaml"]
    for key, value in classification.items():
        lines.append(f"{key}: {json.dumps(value, ensure_ascii=False)}")
    lines.extend(["```", "", "## P\u00e1ginas", ""])
    for page in pages:
        entities = page.entities or {}
        entity_lines = [
            f"- {key}: {', '.join(values) if values else 'n\u00e3o identificado nesta p\u00e1gina'}"
            for key, values in entities.items()
        ]
        visual_lines: list[str] = []
        if not page.visuals:
            visual_lines.extend([
                "Nenhuma imagem ou elemento visual foi extra\u00eddo nesta p\u00e1gina.",
                "Se a p\u00e1gina for uma digitaliza\u00e7\u00e3o sem camada textual, revisar com OCR/vis\u00e3o.",
            ])
        else:
            for visual in page.visuals:
                visual_id = visual.get("image_id", "ID n\u00e3o informado")
                kind = visual.get("kind", "elemento visual")
                location = visual.get("location", "localiza\u00e7\u00e3o n\u00e3o informada")
                description = visual.get("semantic_description") or _visual_fallback_description(visual)
                visual_lines.extend([
                    f"#### {visual_id} — {kind}",
                    f"- Localiza\u00e7\u00e3o: {location}",
                    f"- Fonte t\u00e9cnica: {visual.get('source_name') or visual.get('source_reference') or 'n\u00e3o informada'}",
                    f"- Classe/relev\u00e2ncia: {visual.get('asset_class', 'unknown')} / {'relevante' if visual.get('relevant', True) else 'recurso t\u00e9cnico'}",
                    f"- Ocorr\u00eancia: {visual.get('occurrence_index', 1)} / ID \u00fanico: {visual.get('unique_image_id', 'n\u00e3o informado')}",
                    f"- Arquivo derivado: `{visual.get('relative_path') or ('images/' + Path(str(visual.get('image_path', ''))).name)}`" if visual.get("image_path") or visual.get("relative_path") else "- Arquivo derivado: n\u00e3o gerado",
                    f"- Crop ampliado: `{visual.get('zoom_relative_path')}`" if visual.get('zoom_relative_path') else "- Crop ampliado: n\u00e3o gerado ou n\u00e3o necess\u00e1rio",
                    f"- Formato/dimens\u00f5es: {visual.get('format', 'n\u00e3o identificado')} / {visual.get('width') or '?'}×{visual.get('height') or '?'} px",
                    f"- SHA-256: `{visual.get('sha256', 'n\u00e3o calculado')}`",
                    f"- Descri\u00e7\u00e3o sem\u00e2ntica: {description}",
                    f"- Texto vis\u00edvel/OCR: {normalise_spaces(str(visual.get('visible_text') or visual.get('ocr_text') or 'n\u00e3o identificado'))}",
                    f"- Elementos/objetos: {', '.join(map(str, visual.get('objects', []))) if visual.get('objects') else 'n\u00e3o identificados com seguran\u00e7a'}",
                    f"- Pessoas: {', '.join(map(str, visual.get('people', []))) if visual.get('people') else 'n\u00e3o identificadas com seguran\u00e7a'}",
                    f"- Tabelas/gr\u00e1ficos: {', '.join(map(str, visual.get('tables', []))) if visual.get('tables') else 'n\u00e3o identificados com seguran\u00e7a'}",
                    f"- Confian\u00e7a/origem: {visual.get('confidence', 'n\u00e3o informada')} / {visual.get('description_source', 'fallback')}",
                    "",
                ])
        lines.extend([
            "---", "", f"## [P\u00e1gina PDF {page.pdf_page}]", "",
            f"**Folha indicada nos autos:** {page.court_page if page.court_page is not None else 'n\u00e3o identificada'}",
            f"**Pe\u00e7a:** {page.piece}", f"**Documento ID:** {page.document_id}",
            f"**Data identificada:** {page.dates[0] if page.dates else 'n\u00e3o identificada'}",
            f"**Qualidade da extra\u00e7\u00e3o:** {page.quality}", "",
            "### Resumo sem\u00e2ntico e localiza\u00e7\u00e3o r\u00e1pida", "",
            page.summary or "Resumo sem\u00e2ntico n\u00e3o dispon\u00edvel; revisar a p\u00e1gina.", "",
            f"- \u00c2ncora principal: `PDF p. {page.pdf_page}`" + (f" / `fl. {page.court_page}`" if page.court_page is not None else ""),
            f"- Termos-chave: {', '.join(page.keywords or []) or 'n\u00e3o identificados'}",
            "- Entidades identificadas:", *entity_lines, "",
            "### Blocos, t\u00edtulos e tabelas identificados", "",
            *(f"- **{block.get('type', 'bloco')}**: {'; '.join(map(str, block.get('items', [])))}" for block in (page.content_blocks or [])),
            "- Nenhum bloco tabular/t\u00edtulo foi identificado automaticamente." if not page.content_blocks else "", "",
            f"### Imagens e elementos visuais ({len(page.visuals or [])})", "", *visual_lines, "",
            "### Texto integral extra\u00eddo", "", page.text.rstrip() or "[ILEG\u00cdVEL]", "",
        ])
        if page.warnings:
            lines.extend([f"**Observa\u00e7\u00f5es:** {'; '.join(page.warnings)}", ""])
    return "\n".join(lines).rstrip() + "\n"


def compute_coverage(pages: Sequence[Page], total: int) -> dict[str, Any]:
    processed = len(pages)
    native = sum(page.source == "native_text" and bool(page.text.strip()) for page in pages)
    ocr = sum(page.source != "native_text" for page in pages)
    partial = sum(page.quality == "low" for page in pages)
    unreadable = sum(page.quality == "unreadable" for page in pages)
    visual_records = [visual for page in pages for visual in (page.visuals or [])]
    reviewed = sum(visual.get("description_source") in {"external_review", "human_review", "vision_model"} for visual in visual_records)
    return {
        "pages_total": total,
        "pages_processed": processed,
        "pages_native_text": native,
        "pages_ocr_or_vision": ocr,
        "pages_partial": partial,
        "pages_unreadable": unreadable,
        "pages_pending": list(range(processed + 1, total + 1)),
        "coverage_percent": round(100 * processed / total, 2) if total else 0,
        "visual_elements": len(visual_records),
        "pages_with_visuals": sum(bool(page.visuals) for page in pages),
        "visual_descriptions_reviewed": reviewed,
        "visual_descriptions_pending": len(visual_records) - reviewed,
    }


_build_audit_report_legacy = build_audit_report


def build_audit_report(pages: Sequence[Page], classification: dict[str, Any], pieces: Sequence[dict[str, Any]], coverage: dict[str, Any], mode: str) -> str:
    # Keep the established report and append a machine-readable visual coverage section.
    original = _build_audit_report_legacy(pages, classification, pieces, coverage, mode)
    return original.rstrip() + "\n\n## COBERTURA VISUAL E DESCRI\u00c7\u00d5ES SEM\u00c2NTICAS\n\n" + "\n".join([
        f"Elementos visuais inventariados: {coverage.get('visual_elements', 0)}",
        f"P\u00e1ginas com elementos visuais: {coverage.get('pages_with_visuals', 0)}",
        f"Descri\u00e7\u00f5es sem\u00e2nticas completas/revisadas: {coverage.get('visual_descriptions_reviewed', 0)}",
        f"Descri\u00e7\u00f5es de fallback pendentes de revis\u00e3o visual: {coverage.get('visual_descriptions_pending', 0)}",
        "O invent\u00e1rio visual n\u00e3o presume autenticidade, identidade de pessoas ou significado jur\u00eddico; confirme cada item no original.",
    ]) + "\n"


def load_page_descriptions(path: Path | None) -> dict[int, dict[str, Any]]:
    """Load reviewed page-level semantic descriptions from the safe JSON sidecar."""
    if path is None or not path.exists():
        return {}
    try:
        raw = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError):
        return {}
    entries = raw.get("pages", {}) if isinstance(raw, dict) else {}
    if isinstance(entries, list):
        normalised: dict[Any, Any] = {}
        for entry in entries:
            if isinstance(entry, dict) and entry.get("pdf_page") is not None:
                normalised[entry["pdf_page"]] = entry
        entries = normalised
    if not isinstance(entries, dict):
        return {}
    allowed = {
        "pdf_page", "semantic_description", "transcription", "elements", "objects", "people",
        "tables", "location", "confidence", "description_source", "outcome", "limitations",
    }
    result: dict[int, dict[str, Any]] = {}
    for key, value in entries.items():
        try:
            page_number = int(str(key).removeprefix("P").removeprefix("p").split("-")[0])
        except (TypeError, ValueError):
            continue
        if not isinstance(value, dict):
            continue
        safe = {field: item for field, item in value.items() if field in allowed}
        if safe.get("semantic_description") or safe.get("transcription") or safe.get("outcome") == "unreadable":
            result[page_number] = safe
    return result


def render_pdf_pages(path: Path, output_dir: Path, dpi: int = 150) -> tuple[dict[int, dict[str, Any]], list[str]]:
    """Render every PDF page when pdf2image/Poppler are explicitly available."""
    try:
        from pdf2image import convert_from_path  # type: ignore
    except Exception:
        return {}, ["Renderização integral indisponível: instale pdf2image e Poppler."]
    output_dir.mkdir(parents=True, exist_ok=True)
    try:
        paths = convert_from_path(
            str(path), dpi=dpi, fmt="png", output_folder=str(output_dir), paths_only=True,
        )
    except Exception as exc:
        return {}, [f"Falha na renderização integral do PDF ({type(exc).__name__})."]
    rendered: dict[int, dict[str, Any]] = {}
    for page_number, raw_path in enumerate(paths or [], start=1):
        rendered_path = Path(raw_path)
        rendered[page_number] = {
            "created": rendered_path.is_file(),
            "validated": rendered_path.is_file() and rendered_path.stat().st_size > 0,
            "path": str(rendered_path),
            "relative_path": f"rendered_pages/{rendered_path.name}",
            "provider": "pdf2image/Poppler",
            "dpi": dpi,
        }
    return rendered, []


def build_page_processing_state(
    page_number: int,
    text: str,
    page_visuals: Sequence[dict[str, Any]],
    ocr_pages: set[int],
    render: dict[str, Any] | None,
    page_description: dict[str, Any] | None,
    source_kind: str,
    vision_mode: str,
    vision_provider: str,
    ocr_requested: bool,
    vision_policy: str = "best_effort",
) -> dict[str, Any]:
    vision_enabled = vision_policy != "off" and vision_mode != "never"
    render_required = source_kind == ".pdf" and vision_enabled
    render_state = dict(render or {})
    render_state.setdefault("created", False)
    render_state.setdefault("validated", False)
    render_state.setdefault("required", render_required)
    render_state.setdefault("provider", "not_configured")
    render_state["checked"] = bool(render_state.get("validated"))

    vision_required = vision_enabled and (render_required or bool(page_visuals))
    description = page_description or {}
    has_semantic_result = bool(description.get("semantic_description") or description.get("transcription"))
    explicit_unreadable = description.get("outcome") == "unreadable"
    trusted_vision_source = description.get("description_source") in {"vision_model", "human_review", "external_review"}
    semantic_checked = (has_semantic_result or explicit_unreadable) and trusted_vision_source
    vision_state = {
        "required": vision_required,
        "attempted": vision_enabled,
        "available": trusted_vision_source,
        "semantic_checked": semantic_checked,
        "provider": vision_provider if trusted_vision_source else "unavailable",
        "description": description.get("semantic_description", "") if trusted_vision_source else "",
        "transcription": description.get("transcription", "") if trusted_vision_source else "",
        "elements": description.get("elements", []) if trusted_vision_source else [],
        "outcome": description.get("outcome", "completed" if has_semantic_result else "unavailable") if trusted_vision_source else "unavailable",
        "limitations": description.get("limitations", []) if trusted_vision_source else ["Visão semântica não executada ou provider indisponível."],
    }
    ocr_used = page_number in ocr_pages
    ocr_state = {
        "required": not bool(text.strip()),
        "attempted": bool(ocr_requested),
        "used": ocr_used,
        "provider": "pdf2image/pytesseract" if ocr_used else ("requested" if ocr_requested else "not_requested"),
    }
    consolidation = {"completed": True, "layers": ["native_text", "render", "vision", "ocr", "metadata"]}
    text_ok = bool(text.strip()) or ocr_used
    render_ok = (not render_required) or bool(render_state.get("validated"))
    vision_ok = (not vision_required) or semantic_checked
    if text_ok and render_ok and vision_ok:
        status = "COMPLETE_WITH_LIMITATION" if explicit_unreadable or vision_state["limitations"] and semantic_checked else "COMPLETE"
    else:
        status = "PARTIAL"
    return {"render": render_state, "vision": vision_state, "ocr": ocr_state, "consolidation": consolidation, "status": status}


def compute_coverage(pages: Sequence[Page], total: int) -> dict[str, Any]:
    """Report physical, textual, rendering and semantic coverage separately."""
    processed = len(pages)
    native = sum(page.source == "native_text" and bool(page.text.strip()) for page in pages)
    ocr_pages = sum(bool(page.ocr and page.ocr.get("used")) for page in pages)
    partial = sum(page.status == "PARTIAL" or page.quality == "low" for page in pages)
    unreadable = sum(page.quality == "unreadable" for page in pages)
    visual_records = [visual for page in pages for visual in (page.visuals or [])]
    reviewed_images = sum(visual.get("description_source") in {"external_review", "human_review", "vision_model"} for visual in visual_records)
    vision_required = sum(bool(page.vision and page.vision.get("required")) for page in pages)
    vision_attempted = sum(bool(page.vision and page.vision.get("attempted")) for page in pages)
    vision_completed = sum(bool(page.vision and page.vision.get("semantic_checked")) for page in pages)
    render_required = sum(bool(page.render and page.render.get("required")) for page in pages)
    rendered = sum(bool(page.render and page.render.get("validated")) for page in pages)
    failed = sum(page.status == "FAILED" for page in pages)
    textual_complete = bool(pages) and all(bool(page.text.strip()) or bool(page.ocr and page.ocr.get("used")) for page in pages)
    physical_complete = total > 0 and processed == total
    render_complete = render_required == rendered
    semantic_complete = vision_required == vision_completed
    full_complete = physical_complete and textual_complete and render_complete and semantic_complete and failed == 0 and all(page.status == "COMPLETE" for page in pages)
    return {
        "pages_total": total,
        "pages_processed": processed,
        "pages_native_text": native,
        "pages_ocr_or_vision": sum(page.source != "native_text" for page in pages),
        "ocr_pages": ocr_pages,
        "pages_partial": partial,
        "pages_unreadable": unreadable,
        "failed_pages": failed,
        "pages_pending": list(range(processed + 1, total + 1)),
        "coverage_percent": round(100 * processed / total, 2) if total else 0,
        "rendered_pages": rendered,
        "render_required_pages": render_required,
        "native_text_checked": processed,
        "semantic_vision_required": vision_required,
        "semantic_vision_attempted": vision_attempted,
        "semantic_vision_completed": vision_completed,
        "semantic_vision_unavailable": max(0, vision_required - vision_completed),
        "consolidated_pages": sum(bool(page.consolidation and page.consolidation.get("completed")) for page in pages),
        "visual_elements": len(visual_records),
        "pages_with_visuals": sum(bool(page.visuals) for page in pages),
        "visual_descriptions_reviewed": reviewed_images,
        "visual_descriptions_pending": len(visual_records) - reviewed_images,
        "physical_coverage_complete": physical_complete,
        "textual_coverage_complete": textual_complete,
        "render_coverage_complete": render_complete,
        "semantic_visual_coverage_complete": semantic_complete,
        "full_conversion_complete": full_complete,
        "conversion_result": "CONVERSÃO INTEGRAL" if full_complete else ("CONVERSÃO FÍSICA COMPLETA COM LIMITAÇÕES VISUAIS" if physical_complete else "CONVERSÃO PARCIAL"),
    }


_build_audit_report_with_visuals = build_audit_report


def build_audit_report(pages: Sequence[Page], classification: dict[str, Any], pieces: Sequence[dict[str, Any]], coverage: dict[str, Any], mode: str) -> str:
    original = _build_audit_report_with_visuals(pages, classification, pieces, coverage, mode)
    flags = [
        "## RESULTADO DE CONVERSÃO",
        "",
        f"- Resultado: **{coverage.get('conversion_result', 'CONVERSÃO PARCIAL')}**",
        f"- Cobertura física completa: `{str(coverage.get('physical_coverage_complete', False)).lower()}`",
        f"- Cobertura textual completa: `{str(coverage.get('textual_coverage_complete', False)).lower()}`",
        f"- Renderização completa: `{str(coverage.get('render_coverage_complete', False)).lower()}`",
        f"- Visão semântica completa: `{str(coverage.get('semantic_visual_coverage_complete', False)).lower()}`",
        f"- Conversão integral demonstrável: `{str(coverage.get('full_conversion_complete', False)).lower()}`",
        "Renderização, OCR e inspeção técnica não são tratados como equivalentes à visão semântica multimodal.",
    ]
    return original.rstrip() + "\n\n" + "\n".join(flags) + "\n"


_build_structured_markdown_with_semantics = build_structured_markdown


def build_structured_markdown(pages: Sequence[Page], classification: dict[str, Any]) -> str:
    markdown = _build_structured_markdown_with_semantics(pages, classification)
    for page in pages:
        render = page.render or {}
        vision = page.vision or {}
        ocr = page.ocr or {}
        consolidation = page.consolidation or {}
        processing = "\n".join([
            "### Processamento por camada",
            "",
            f"- Texto nativo: {'verificado' if page.text.strip() else 'não disponível'}",
            f"- Renderização: {'concluída' if render.get('validated') else 'não disponível'}",
            f"- Inspeção técnica: {'concluída' if render.get('checked') else 'não executada'}",
            f"- Visão semântica: {'concluída' if vision.get('semantic_checked') else 'não disponível'}",
            f"- Provider de visão: {vision.get('provider', 'none')}",
            f"- OCR: {'utilizado' if ocr.get('used') else ('tentado' if ocr.get('attempted') else 'não utilizado')}",
            f"- Consolidação: {'concluída' if consolidation.get('completed') else 'pendente'}",
            f"- Status: **{page.status}**",
            "",
        ])
        marker = f"**Qualidade da extração:** {page.quality}\n"
        if marker in markdown:
            markdown = markdown.replace(marker, marker + "\n" + processing, 1)
    return markdown


def build_index_records(pages: Sequence[Page], process_id: str) -> Iterator[dict[str, Any]]:
    for page in pages:
        yield {
            "process": process_id,
            "piece": page.piece,
            "pdf_page": page.pdf_page,
            "court_page": page.court_page,
            "document_id": page.document_id,
            "quality": page.quality,
            "source": page.source,
            "text": page.text,
            "terms": sorted(set(re.findall(r"[\w\u00c0-\u00ff]{3,}", page.text.lower(), flags=re.UNICODE))),
            "summary": page.summary,
            "entities": page.entities or {},
            "keywords": page.keywords or [],
            "visuals": page.visuals or [],
            "render": page.render or {},
            "vision": page.vision or {},
            "ocr": page.ocr or {},
            "status": page.status,
        }


_compute_coverage_stateful = compute_coverage


def compute_coverage(pages: Sequence[Page], total: int) -> dict[str, Any]:
    result = _compute_coverage_stateful(pages, total)
    result["conversion_result"] = "CONVERSAO INTEGRAL" if result.get("full_conversion_complete") else (
        "CONVERSAO FISICA COMPLETA COM LIMITACOES VISUAIS" if result.get("physical_coverage_complete") else "CONVERSAO PARCIAL"
    )
    return result


# Procedural progression artifacts. These functions deliberately produce a
# review queue, not legal conclusions: every item carries a page source and is
# marked as heuristic until a professional approves it.
def _page_source(page: Page) -> dict[str, Any]:
    return {
        "pdf_page": page.pdf_page,
        "court_page": page.court_page,
        "piece": page.piece,
        "document_id": page.document_id,
        "anchor": page_reference(page),
    }


def _page_snippet(page: Page, limit: int = 240) -> str:
    value = normalise_spaces(page.text)
    if not value:
        value = normalise_spaces(str((page.vision or {}).get("description", "")))
    return (value or "Conteúdo não legível ou não extraído.").replace("|", "\\|")[:limit]


def build_procedural_summary(
    pages: Sequence[Page],
    classification: dict[str, Any],
    pieces: Sequence[dict[str, Any]],
    coverage: dict[str, Any],
) -> dict[str, Any]:
    events: list[dict[str, Any]] = []
    for page in pages:
        for date_value in page.dates or []:
            events.append({
                "event_id": f"E{len(events) + 1:04d}",
                "date": date_value,
                "description": _page_snippet(page),
                "source": _page_source(page),
                "confidence": "heuristic",
                "review": "needs_review",
            })

    deadline_cues = ("prazo", "dias", "intime-se", "intim", "manifestar", "juntar", "vencimento")
    deadlines: list[dict[str, Any]] = []
    for page in pages:
        lower = page.text.lower()
        if not any(cue in lower for cue in deadline_cues):
            continue
        deadlines.append({
            "deadline_id": f"D{len(deadlines) + 1:04d}",
            "trigger_dates": page.dates or [],
            "trigger": _page_snippet(page),
            "source": _page_source(page),
            "due_date": None,
            "calculation_status": "needs_review",
            "status": "open_review",
        })

    evidence_cues = (
        ("prova", "prova"),
        ("documento", "documento"),
        ("laudo", "laudo/perícia"),
        ("perícia", "laudo/perícia"),
        ("contrato", "contrato"),
        ("extrato", "documento financeiro"),
        ("testemunha", "testemunhal"),
        ("anexo", "anexo"),
    )
    evidence: list[dict[str, Any]] = []
    for page in pages:
        lower = page.text.lower()
        for cue, category in evidence_cues:
            if cue not in lower:
                continue
            evidence.append({
                "evidence_id": f"EV{len(evidence) + 1:04d}",
                "category": category,
                "statement": _page_snippet(page),
                "source": _page_source(page),
                "nature": "documentary_mention",
                "sufficiency": "not_assessed",
                "review": "needs_review",
            })

    pending_pages = [
        {
            "page": page.pdf_page,
            "status": page.status,
            "reason": "; ".join(page.warnings or []) or "camadas obrigatórias pendentes",
            "source": _page_source(page),
        }
        for page in pages
        if page.status != "COMPLETE" or page.warnings
    ]
    tasks: list[dict[str, Any]] = []
    if pending_pages:
        tasks.append({
            "task_id": "T0001",
            "description": "Revisar páginas pendentes e limitações de extração/visão.",
            "priority": "high",
            "owner": "unassigned",
            "status": "open_review",
            "sources": [item["source"] for item in pending_pages[:20]],
        })
    if deadlines:
        tasks.append({
            "task_id": f"T{len(tasks) + 1:04d}",
            "description": "Conferir marcos, calendário aplicável e vencimentos antes de qualquer providência.",
            "priority": "critical",
            "owner": "unassigned",
            "status": "open_review",
            "sources": [item["source"] for item in deadlines],
        })
    if not tasks:
        tasks.append({
            "task_id": "T0001",
            "description": "Revisar fatos, pedidos e classificação antes de usar qualquer peça gerada.",
            "priority": "medium",
            "owner": "unassigned",
            "status": "open_review",
            "sources": [],
        })

    return {
        "schema_version": "0.1",
        "status": "draft",
        "classification": classification,
        "coverage": coverage,
        "pieces": list(pieces),
        "events": events,
        "deadlines": deadlines,
        "evidence": evidence,
        "pending_pages": pending_pages,
        "tasks": tasks,
        "limitations": [
            "Eventos e prazos são identificados por heurística e exigem conferência profissional.",
            "Nenhuma peça gerada por este artefato está pronta para protocolo automático.",
        ],
    }


def build_andamento_report(summary: dict[str, Any]) -> str:
    coverage = summary.get("coverage", {})
    classification = summary.get("classification", {})
    events = summary.get("events", [])
    deadlines = summary.get("deadlines", [])
    pending = summary.get("pending_pages", [])
    tasks = summary.get("tasks", [])
    lines = [
        "# RELATÓRIO DE ANDAMENTO PROCESSUAL",
        "",
        "> Documento de trabalho. Confirme cada item no original antes de tomar providência.",
        "",
        "## Estado atual",
        "",
        f"- Número identificado: {classification.get('numero_processo', 'Não identificado nos autos')}",
        f"- Fase identificada: {classification.get('fase_processual', 'Não identificado nos autos')}",
        f"- Resultado da conversão: **{coverage.get('conversion_result', 'CONVERSAO PARCIAL')}**",
        f"- Cobertura física/textual/visual: {coverage.get('pages_processed', 0)}/{coverage.get('pages_total', 0)} páginas; visão semântica {coverage.get('semantic_vision_completed', 0)}/{coverage.get('semantic_vision_required', 0)}.",
        "",
        "## Últimos eventos localizados",
        "",
        "| Data | Evento/trecho | Fonte | Revisão |",
        "|---|---|---|---|",
    ]
    for event in events[-20:]:
        source = event.get("source", {})
        lines.append(f"| {event.get('date', 'não identificada')} | {event.get('description', '')} | {source.get('anchor', '—')} | {event.get('review', 'needs_review')} |")
    if not events:
        lines.append("| Não identificado | Nenhum evento datado localizado por heurística | — | needs_review |")
    lines.extend([
        "",
        "## Prazos e marcos para conferência",
        "",
        "| Marco encontrado | Fonte | Vencimento calculado | Status |",
        "|---|---|---|---|",
    ])
    for item in deadlines:
        lines.append(f"| {item.get('trigger', '')} | {item.get('source', {}).get('anchor', '—')} | não calculado | {item.get('calculation_status', 'needs_review')} |")
    if not deadlines:
        lines.append("| Nenhum prazo inequívoco localizado | — | não aplicável | revisar autos |")
    lines.extend(["", "## Pendências de revisão", ""])
    if pending:
        lines.extend(f"- PDF p. {item.get('page')}: {item.get('status')} — {item.get('reason')}." for item in pending)
    else:
        lines.append("- Nenhuma pendência técnica registrada; a revisão jurídica continua obrigatória.")
    lines.extend(["", "## Próximas ações sugeridas", ""])
    lines.extend(f"- **{item.get('priority', 'medium').upper()}** — {item.get('description')} (responsável: {item.get('owner', 'unassigned')})." for item in tasks)
    lines.extend(["", "## Limitações", "", *[f"- {item}" for item in summary.get("limitations", [])], ""])
    return "\n".join(lines)


def build_deadlines_report(summary: dict[str, Any]) -> str:
    lines = [
        "# PENDÊNCIAS E PRAZOS",
        "",
        "> Prazos não são calculados automaticamente. Informe marco, calendário e regra aplicável e valide com profissional habilitado.",
        "",
        "| ID | Marco/trecho | Datas encontradas | Fonte | Vencimento | Status |",
        "|---|---|---|---|---|---|",
    ]
    for item in summary.get("deadlines", []):
        lines.append(f"| {item.get('deadline_id')} | {item.get('trigger', '')} | {', '.join(item.get('trigger_dates', [])) or 'não identificada'} | {item.get('source', {}).get('anchor', '—')} | não calculado | {item.get('calculation_status', 'needs_review')} |")
    if not summary.get("deadlines"):
        lines.append("| — | Nenhum marco localizado por heurística | — | — | não aplicável | revisar autos |")
    return "\n".join(lines) + "\n"


def build_document_matrix(pieces: Sequence[dict[str, Any]], pages: Sequence[Page]) -> str:
    lines = [
        "# MATRIZ DOCUMENTAL",
        "",
        "> Classificação heurística. A ausência de uma peça no índice não prova que ela não foi juntada.",
        "",
        "| ID | Peça/segmento | Páginas PDF | Status técnico | Fonte documental |",
        "|---|---|---:|---|---|",
    ]
    for piece in pieces:
        scoped = [page for page in pages if page.pdf_page >= piece.get("pdf_page_start", 0) and page.pdf_page <= piece.get("pdf_page_end", 0)]
        status = "REVISAR" if any(page.status != "COMPLETE" or page.warnings for page in scoped) else "IDENTIFICADO POR HEURÍSTICA"
        lines.append(f"| {piece.get('id')} | {piece.get('piece')} | {piece.get('pdf_page_start')}–{piece.get('pdf_page_end')} | {status} | PDF p. {piece.get('pdf_page_start')}–{piece.get('pdf_page_end')} |")
    if not pieces:
        lines.append("| — | Nenhuma peça identificada | — | REVISAR | — |")
    lines.extend(["", "## Referências a documentos que exigem conferência", ""])
    references = [page for page in pages if re.search(r"não localizado|nao localizado|ausente|faltante|anexo", page.text, re.I)]
    if references:
        lines.extend(f"- {page_reference(page)} — {_page_snippet(page)}" for page in references)
    else:
        lines.append("- Nenhuma referência explícita foi localizada; conferir anexos no original.")
    return "\n".join(lines) + "\n"


def build_evidence_map(summary: dict[str, Any]) -> str:
    lines = [
        "# MAPA DE PROVAS",
        "",
        "> O mapa registra menções documentais; não conclui autenticidade, pertinência ou suficiência probatória.",
        "",
        "| ID | Categoria | Menção localizada | Fonte | Natureza | Revisão |",
        "|---|---|---|---|---|---|",
    ]
    for item in summary.get("evidence", []):
        lines.append(f"| {item.get('evidence_id')} | {item.get('category')} | {item.get('statement')} | {item.get('source', {}).get('anchor', '—')} | {item.get('nature')} | {item.get('review')} |")
    if not summary.get("evidence"):
        lines.append("| — | Não identificado | Nenhuma menção probatória localizada por heurística | — | — | needs_review |")
    return "\n".join(lines) + "\n"


def build_manifestation_checklist(summary: dict[str, Any]) -> str:
    classification = summary.get("classification", {})
    coverage = summary.get("coverage", {})
    checks = [
        ("Identificação do processo", classification.get("numero_processo") != "Não identificado nos autos", "Conferir número no original."),
        ("Partes e representação", False, "Preencher somente após localizar qualificação e procuração."),
        ("Linha do tempo", bool(summary.get("events")), "Conferir datas, duplicidades e conflitos."),
        ("Provas e documentos", bool(summary.get("evidence")), "Distinguir menção, existência e suficiência."),
        ("Prazos", False, "Calcular apenas com marco e calendário confirmados."),
        ("Cobertura integral", bool(coverage.get("full_conversion_complete")), "Resolver páginas PARTIAL antes de concluir."),
        ("Pedidos e providência", False, "Definir com profissional; não inferir pedido ausente."),
    ]
    lines = [
        "# CHECKLIST PARA MANIFESTAÇÃO",
        "",
        "> Checklist de preparação. Não é parecer jurídico nem autorização de protocolo.",
        "",
        "| Item | Estado automático | Ação de conferência |",
        "|---|---|---|",
    ]
    for label, ok, action in checks:
        lines.append(f"| {label} | {'LOCALIZADO' if ok else 'PENDENTE'} | {action} |")
    return "\n".join(lines) + "\n"


def build_piece_draft(summary: dict[str, Any]) -> str:
    classification = summary.get("classification", {})
    source_lines = [
        f"- {event.get('source', {}).get('anchor', '—')}: {event.get('description', '')}"
        for event in summary.get("events", [])[:10]
    ]
    lines = [
        "# MINUTA DE PEÇA — RASCUNHO",
        "",
        "> Não protocolar. Complete, revise e assine somente após conferência profissional.",
        "",
        "## Endereçamento",
        "",
        "[Órgão julgador e número do processo — preencher a partir dos autos]",
        "",
        "## Qualificação",
        "",
        "[Partes, representantes e procurações — não identificados automaticamente]",
        "",
        "## Síntese factual com fontes",
        "",
        *(source_lines or ["[FATO A CONFERIR — nenhuma fonte datada localizada]"]),
        "",
        "## Fundamentos e providência pretendida",
        "",
        "[Inserir fundamentos fornecidos e conferidos pelo profissional responsável. O parser não cria fundamento jurídico.]",
        "",
        "## Pedidos",
        "",
        "[DEFINIR PEDIDOS — não inferir a partir de menções]",
        "",
        f"Processo identificado: {classification.get('numero_processo', 'Não identificado nos autos')}",
        "Status: rascunho com revisão obrigatória.",
        "",
    ]
    return "\n".join(lines)


def build_compliance_report(summary: dict[str, Any]) -> str:
    coverage = summary.get("coverage", {})
    lines = [
        "# RELATÓRIO DE CONFORMIDADE DA EXTRAÇÃO",
        "",
        "| Controle | Resultado |",
        "|---|---|",
        f"| Páginas processadas | {coverage.get('pages_processed', 0)}/{coverage.get('pages_total', 0)} |",
        f"| Cobertura textual | {'OK' if coverage.get('textual_coverage_complete') else 'PENDENTE'} |",
        f"| Renderização | {'OK' if coverage.get('render_coverage_complete') else 'PENDENTE'} |",
        f"| Visão semântica | {'OK' if coverage.get('semantic_visual_coverage_complete') else 'PENDENTE'} |",
        f"| Conversão integral | {'OK' if coverage.get('full_conversion_complete') else 'NÃO DECLARADA'} |",
        f"| Eventos com fonte | {len(summary.get('events', []))} |",
        f"| Prazos para revisão | {len(summary.get('deadlines', []))} |",
        f"| Menções probatórias | {len(summary.get('evidence', []))} |",
        "",
        "## Regras",
        "",
        "- Renderização, OCR e inspeção técnica não substituem visão semântica.",
        "- Heurísticas não constituem conclusão jurídica.",
        "- Minutas e alertas exigem revisão humana e não são protocolados automaticamente.",
        "",
    ]
    return "\n".join(lines)


def archive_current_run(output: Path, manifest: dict[str, Any]) -> Path | None:
    """Copy the current run into an immutable version folder before replacement."""
    source = manifest.get("source", {}) if isinstance(manifest, dict) else {}
    digest = str(source.get("sha256", ""))
    if len(digest) < 16:
        return None
    task = re.sub(r"[^a-z0-9_-]+", "-", str(manifest.get("task", "ingest")).lower()).strip("-") or "ingest"
    base_name = f"{digest[:16]}-{task}"
    versions = output / "versions"
    versions.mkdir(parents=True, exist_ok=True)
    archive_dir = versions / base_name
    suffix = 1
    while archive_dir.exists():
        archive_dir = versions / f"{base_name}-{suffix}"
        suffix += 1
    archive_dir.mkdir(parents=True, exist_ok=False)
    names = ["manifest.json", *list(manifest.get("generated_files", []))]
    if "relatorio_processual.md" not in names:
        names.append("relatorio_processual.md")
    for raw_name in names:
        if not isinstance(raw_name, str) or raw_name.endswith("/"):
            continue
        source_path = output / raw_name
        if not source_path.is_file():
            continue
        target_path = archive_dir / raw_name
        target_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, target_path)
    for directory_name in ("original", "images", "rendered_pages", "assets/pages"):
        source_dir = output / directory_name
        if source_dir.is_dir():
            shutil.copytree(source_dir, archive_dir / directory_name, dirs_exist_ok=True)
    return archive_dir


def build_cumulative_report(output: Path) -> str:
    """Build a searchable Markdown ledger of every preserved upload/version."""
    records: list[tuple[str, dict[str, Any]]] = []
    current_manifest = output / "manifest.json"
    if current_manifest.is_file():
        try:
            records.append((".", json.loads(current_manifest.read_text(encoding="utf-8-sig"))))
        except (OSError, json.JSONDecodeError):
            pass
    versions_dir = output / "versions"
    if versions_dir.is_dir():
        for manifest_path in sorted(versions_dir.glob("*/manifest.json")):
            try:
                records.append((manifest_path.parent.relative_to(output).as_posix(), json.loads(manifest_path.read_text(encoding="utf-8-sig"))))
            except (OSError, json.JSONDecodeError):
                continue
    lines = [
        "# RELATÓRIO PROCESSUAL CONSOLIDADO",
        "",
        "> Índice cumulativo dos uploads preservados. Nenhuma versão anterior é excluída; novos envios são arquivados e acrescentados ao histórico.",
        "",
        "## Histórico de uploads",
        "",
        "| Versão | Arquivo | SHA-256 | Tarefa | Processado em | Páginas | Manifesto |",
        "|---|---|---|---|---|---:|---|",
    ]
    for folder, manifest in records:
        source = manifest.get("source", {})
        digest = str(source.get("sha256", ""))
        label = "atual" if folder == "." else folder
        link = "manifest.json" if folder == "." else f"{folder}/manifest.json"
        filename = str(source.get("name", "não informado")).replace("|", "\\|")
        lines.append(
            f"| {label} | {filename} | {digest[:16] or 'não calculado'}… | "
            f"{manifest.get('task', 'não informado')} | {manifest.get('processed_at', 'não informado')} | "
            f"{source.get('pages', 0)} | [{link}]({link}) |"
        )
    if not records:
        lines.append("| — | Nenhum upload processado | — | — | — | 0 | — |")
    lines.extend([
        "",
        "## Como localizar",
        "",
        "- Use o índice acima para selecionar a versão e abrir o manifesto correspondente.",
        "- Os artefatos históricos ficam em versions/<sha256>-<tarefa>/.",
        "- O upload atual fica na raiz e é substituído somente depois de ser preservado no histórico.",
        "- Use pages.jsonl e index.jsonl da versão escolhida para localizar página, peça, folha e document_id.",
        "",
    ])
    current_report = output / "relatorio_andamento.md"
    if current_report.is_file():
        lines.extend([
            "## Andamento da versão atual",
            "",
            "Consulte [relatorio_andamento.md](relatorio_andamento.md) para o andamento da versão atual.",
            "",
        ])
    return "\n".join(lines)


# Portable visual inventory and delivery helpers. These are intentionally
# provider-neutral: a host IA may create the review sidecar, while the local
# parser validates, classifies and preserves its result.
VISUAL_ASSET_CLASSES = (
    "visual_asset",
    "technical_artifact",
    "qr_code",
    "logo",
    "document_scan",
    "photo",
    "unknown",
)


def classify_visual_asset(record: dict[str, Any]) -> str:
    explicit = record.get("asset_class") or record.get("visual_class")
    if isinstance(explicit, str) and explicit in VISUAL_ASSET_CLASSES:
        return explicit
    kind = str(record.get("kind", "")).lower()
    name = " ".join(
        str(record.get(key, ""))
        for key in ("source_name", "source_reference", "alt_text", "ocr_text", "visible_text")
    ).lower()
    if kind == "page_scan":
        return "document_scan"
    width, height = record.get("width"), record.get("height")
    if isinstance(width, int) and isinstance(height, int) and width <= 2 and height <= 2:
        return "technical_artifact"
    if any(term in name for term in ("qr", "qrcode", "bar code", "barcode", "código de barras", "codigo de barras")):
        return "qr_code"
    if "logo" in name or "logotipo" in name or "marca d'água" in name or "marca dagua" in name:
        return "logo"
    if any(term in name for term in ("foto", "fotografia", "photo", "portrait", "retrato")):
        return "photo"
    if width and height:
        return "visual_asset"
    return "unknown"


def annotate_visual_record(record: dict[str, Any]) -> dict[str, Any]:
    record["asset_class"] = classify_visual_asset(record)
    if not isinstance(record.get("relevant"), bool):
        record["relevant"] = record["asset_class"] != "technical_artifact"
    digest = str(record.get("sha256", ""))
    if digest:
        record.setdefault("unique_image_id", f"IMG-{digest[:16]}")
    else:
        record.setdefault("unique_image_id", record.get("image_id", "IMG-unknown"))
    return record


def _safe_asset_name(value: str) -> str:
    stem = re.sub(r"[^A-Za-z0-9._-]+", "-", Path(value).name).strip(".-")
    return stem or "image.bin"


def _create_zoom_asset(record: dict[str, Any], output_dir: Path) -> None:
    if not record.get("relevant") or record.get("asset_class") == "technical_artifact":
        return
    width, height = record.get("width"), record.get("height")
    source = Path(str(record.get("image_path", "")))
    if not source.is_file() or not isinstance(width, int) or not isinstance(height, int) or min(width, height) >= 200:
        return
    try:
        from io import BytesIO
        from PIL import Image  # type: ignore

        with Image.open(source) as image:
            zoom = image.resize((max(width * 4, 1), max(height * 4, 1)), Image.Resampling.NEAREST)
            crop_dir = output_dir / "crops"
            crop_dir.mkdir(parents=True, exist_ok=True)
            target = crop_dir / f"{record['unique_image_id']}-zoom.png"
            zoom.save(target, format="PNG")
            record["zoom_path"] = str(target)
            record["zoom_relative_path"] = f"images/crops/{target.name}"
    except Exception:
        # A crop is an enhancement; absence must remain explicit, not fatal.
        record.setdefault("limitations", []).append("Ampliação não gerada: Pillow indisponível ou imagem incompatível.")


def consolidate_visual_inventory(by_page: dict[int, list[dict[str, Any]]], output_dir: Path) -> dict[int, list[dict[str, Any]]]:
    """Deduplicate embedded assets by SHA-256 while retaining page occurrences."""
    output_dir.mkdir(parents=True, exist_ok=True)
    canonical_paths: dict[str, Path] = {}
    occurrence_counts: dict[str, int] = {}
    for page_number in sorted(by_page):
        for record in by_page[page_number]:
            annotate_visual_record(record)
            source_path = Path(str(record.get("image_path", "")))
            if not record.get("sha256") and source_path.is_file():
                record["sha256"] = hashlib.sha256(source_path.read_bytes()).hexdigest()
                record["unique_image_id"] = f"IMG-{record['sha256'][:16]}"
            digest = str(record.get("sha256", ""))
            unique_id = str(record.get("unique_image_id", record.get("image_id", "IMG-unknown")))
            occurrence_counts[unique_id] = occurrence_counts.get(unique_id, 0) + 1
            record["occurrence_index"] = occurrence_counts[unique_id]
            if digest and source_path.is_file():
                canonical = canonical_paths.get(digest)
                if canonical is None:
                    canonical = output_dir / f"{digest[:16]}-{_safe_asset_name(str(record.get('source_name', source_path.name)))}"
                    if source_path.resolve() != canonical.resolve():
                        shutil.copy2(source_path, canonical)
                    canonical_paths[digest] = canonical
                if source_path.resolve() != canonical.resolve() and output_dir.resolve() in source_path.resolve().parents:
                    try:
                        source_path.unlink()
                    except OSError:
                        pass
                record["image_path"] = str(canonical)
                record["relative_path"] = f"images/{canonical.name}"
            _create_zoom_asset(record, output_dir)
    return by_page


def build_image_index(pages: Sequence[Page]) -> dict[str, Any]:
    unique: dict[str, dict[str, Any]] = {}
    occurrences: list[dict[str, Any]] = []
    for page in pages:
        for visual in page.visuals or []:
            annotate_visual_record(visual)
            unique_id = str(visual.get("unique_image_id", visual.get("image_id", "IMG-unknown")))
            occurrence = {
                "image_id": visual.get("image_id"),
                "page_pdf": visual.get("page_pdf", page.pdf_page),
                "court_page": page.court_page,
                "location": visual.get("location"),
                "occurrence_index": visual.get("occurrence_index", 1),
            }
            occurrences.append({"unique_image_id": unique_id, **occurrence})
            if unique_id not in unique:
                unique[unique_id] = {
                    "unique_image_id": unique_id,
                    "image_id": visual.get("image_id"),
                    "sha256": visual.get("sha256"),
                    "asset_class": visual.get("asset_class", "unknown"),
                    "relevant": visual.get("relevant", True),
                    "relative_path": visual.get("relative_path"),
                    "zoom_relative_path": visual.get("zoom_relative_path"),
                    "semantic_description": visual.get("semantic_description", ""),
                    "description_source": visual.get("description_source", "fallback"),
                    "occurrences": [],
                }
            unique[unique_id]["occurrences"].append(occurrence)
    return {
        "schema_version": "1.0",
        "unique_images": list(unique.values()),
        "occurrences": occurrences,
        "technical_artifacts": [item for item in unique.values() if item.get("asset_class") == "technical_artifact"],
        "relevant_images": [item for item in unique.values() if item.get("relevant")],
    }


def build_problematic_pages_report(pages: Sequence[Page]) -> str:
    lines = [
        "# PÁGINAS PROBLEMÁTICAS E PENDÊNCIAS",
        "",
        "Lista automática para revisão. Ausência nesta lista não substitui conferência profissional.",
        "",
        "| Página PDF | Status | Texto | Renderização | Visão semântica | Observação |",
        "|---:|---|---|---|---|---|",
    ]
    problematic = [page for page in pages if page.status != "COMPLETE" or page.warnings or (page.vision or {}).get("limitations")]
    for page in problematic:
        render = page.render or {}
        vision = page.vision or {}
        warning = "; ".join(page.warnings or []) or "; ".join(vision.get("limitations", [])) or "revisar"
        lines.append(
            f"| {page.pdf_page} | {page.status} | {'OK' if page.text.strip() else 'PENDENTE'} | "
            f"{'OK' if render.get('validated') else 'PENDENTE'} | {'OK' if vision.get('semantic_checked') else 'PENDENTE'} | {warning.replace('|', '\\|')} |"
        )
    if not problematic:
        lines.append("| — | Nenhuma pendência automática | OK | OK | OK | Revisão humana continua recomendada. |")
    lines.extend(["", "## Critério", "", "`COMPLETE` só é válido quando as camadas exigidas pelo manifesto foram concluídas.", ""])
    return "\n".join(lines)


def write_process_bundle(output: Path, destination: Path | None = None) -> Path:
    destination = destination or (output / "processo_completo.zip")
    destination.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(output.rglob("*")):
            if not path.is_file() or path.resolve() == destination.resolve() or "versions" in path.relative_to(output).parts:
                continue
            archive.write(path, path.relative_to(output).as_posix())
    return destination


def detect_text_encoding(path: Path) -> str:
    if path.suffix.lower() == ".pdf":
        return "binary/pdf"
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        return "utf-8-sig"
    for encoding in ("utf-8", "cp1252", "latin-1"):
        try:
            raw.decode(encoding)
            return encoding
        except UnicodeDecodeError:
            continue
    return "utf-8-replace"


_load_image_descriptions_legacy = load_image_descriptions


def load_image_descriptions(path: Path | None) -> dict[str, dict[str, Any]]:
    """Load legacy descriptions plus classification/relevance metadata safely."""
    result = _load_image_descriptions_legacy(path)
    if path is None or not path.exists():
        return result
    try:
        raw = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError):
        return result
    entries = raw.get("images", raw) if isinstance(raw, dict) else raw
    if isinstance(entries, dict):
        entries = [{"image_id": key, **(value if isinstance(value, dict) else {})} for key, value in entries.items()]
    if not isinstance(entries, list):
        return result
    allowed = {"asset_class", "visual_class", "relevant", "crop_path", "zoom_relative_path", "limitations"}
    for entry in entries:
        if not isinstance(entry, dict) or not entry.get("image_id"):
            continue
        image_id = str(entry["image_id"])
        result.setdefault(image_id, {"image_id": image_id})
        result[image_id].update({key: value for key, value in entry.items() if key in allowed})
    return result


_extract_referenced_visuals_legacy = extract_referenced_visuals


def extract_referenced_visuals(
    text: str,
    page_number: int,
    base_dir: Path | None = None,
    descriptions: dict[str, dict[str, Any]] | None = None,
) -> list[dict[str, Any]]:
    records = _extract_referenced_visuals_legacy(text, page_number, base_dir, descriptions)
    for record in records:
        annotate_visual_record(record)
    return records


_extract_pdf_visuals_legacy = extract_pdf_visuals


def extract_pdf_visuals(
    path: Path,
    output_dir: Path,
    use_ocr: bool = False,
    ocr_language: str = "por+eng",
    descriptions: dict[str, dict[str, Any]] | None = None,
) -> dict[int, list[dict[str, Any]]]:
    records = _extract_pdf_visuals_legacy(path, output_dir, use_ocr, ocr_language, descriptions)
    return consolidate_visual_inventory(records, output_dir)


_build_structured_markdown_legacy = build_structured_markdown


def build_structured_markdown(pages: Sequence[Page], classification: dict[str, Any]) -> str:
    """Render one full block per unique relevant image and keep technical assets indexed."""
    originals: dict[int, list[dict[str, Any]]] = {}
    rendered_unique: set[str] = set()
    technical_count = 0
    for page in pages:
        original = list(page.visuals or [])
        originals[id(page)] = original
        filtered: list[dict[str, Any]] = []
        for visual in original:
            annotate_visual_record(visual)
            if not visual.get("relevant", True):
                technical_count += 1
                continue
            unique_id = str(visual.get("unique_image_id", visual.get("image_id", "IMG-unknown")))
            if unique_id in rendered_unique:
                filtered.append({
                    "image_id": visual.get("image_id"),
                    "kind": "occurrence_repeated",
                    "asset_class": visual.get("asset_class", "unknown"),
                    "unique_image_id": unique_id,
                    "relevant": True,
                    "semantic_description": "Ocorrência repetida; consulte images/index.json para a descrição única.",
                    "description_source": "inventory",
                })
            else:
                rendered_unique.add(unique_id)
                filtered.append(visual)
        page.visuals = filtered
    try:
        markdown = _build_structured_markdown_legacy(pages, classification)
    finally:
        for page in pages:
            page.visuals = originals[id(page)]
    markdown = markdown.replace("### Imagens e elementos visuais (", "### Imagens visuais relevantes (")
    if technical_count:
        markdown = (
            "## Recursos técnicos omitidos dos blocos semânticos\n\n"
            f"{technical_count} ocorrência(s) foram classificadas como recurso técnico. "
            "Consulte `images/index.json` para hashes e páginas.\n\n" + markdown
        )
    return markdown
