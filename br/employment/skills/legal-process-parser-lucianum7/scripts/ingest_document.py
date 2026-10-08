from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path
from typing import Any

try:
    from .helpers import (
        archive_current_run,
        build_audit_report,
        build_andamento_report,
        build_chronology,
        build_compliance_report,
        build_cumulative_report,
        build_controversy_matrix,
        build_deadlines_report,
        build_document_matrix,
        build_evidence_map,
        build_image_index,
        build_index_records,
        build_manifestation_checklist,
        build_pages,
        build_problematic_pages_report,
        build_piece_draft,
        build_pieces_markdown,
        build_procedural_summary,
        build_structured_markdown,
        classify_process,
        compute_coverage,
        consolidate_visual_inventory,
        copy_original,
        detect_text_encoding,
        extract_pdf_visuals,
        extract_referenced_visuals,
        extract_pages_with_ocr,
        identify_pieces,
        load_image_descriptions,
        load_page_descriptions,
        now_utc,
        render_pdf_pages,
        sha256_file,
        write_json,
        write_jsonl,
        write_process_bundle,
    )
except ImportError:  # direct execution: python scripts/ingest_document.py
    from helpers import (  # type: ignore
        archive_current_run,
        build_audit_report,
        build_andamento_report,
        build_chronology,
        build_compliance_report,
        build_cumulative_report,
        build_controversy_matrix,
        build_deadlines_report,
        build_document_matrix,
        build_evidence_map,
        build_image_index,
        build_index_records,
        build_manifestation_checklist,
        build_pages,
        build_problematic_pages_report,
        build_piece_draft,
        build_pieces_markdown,
        build_procedural_summary,
        build_structured_markdown,
        classify_process,
        compute_coverage,
        consolidate_visual_inventory,
        copy_original,
        detect_text_encoding,
        extract_pdf_visuals,
        extract_referenced_visuals,
        extract_pages_with_ocr,
        identify_pieces,
        load_image_descriptions,
        load_page_descriptions,
        now_utc,
        render_pdf_pages,
        sha256_file,
        write_json,
        write_jsonl,
        write_process_bundle,
    )


MODES = (
    "INGEST",
    "AUDIT_FULL",
    "QUERY",
    "COMPARE",
    "EVIDENCE_ANALYSIS",
    "DECISION_ANALYSIS",
    "PLEADING_AUDIT",
    "CALCULATION_SUPPORT",
    "PETITION_DRAFT",
    "PROCEDURAL_ANALYSIS",
    "UPDATE",
)

TASKS = (
    "ingest",
    "audit",
    "analyze",
    "petition",
    "deadlines",
    "evidence",
)

BASE_ARTIFACTS = (
    "manifest.json",
    "processo_estruturado.md",
    "processo_completo.md",
    "pages.jsonl",
    "index.jsonl",
    "image_inventory.json",
    "images/index.json",
    "checkpoints.jsonl",
    "indice_pecas.md",
    "paginas_problematicas.md",
    "relatorio_processual.md",
    "processo_completo.zip",
)

ANALYSIS_ARTIFACTS = (
    "andamento_processual.json",
    "relatorio_andamento.md",
    "cronologia.md",
    "matriz_controversias.md",
    "matriz_documental.md",
    "mapa_provas.md",
    "relatorio_conformidade.md",
)

TASK_ARTIFACTS = {
    "ingest": BASE_ARTIFACTS,
    "audit": BASE_ARTIFACTS + ANALYSIS_ARTIFACTS + ("relatorio_auditoria.md", "pendencias_e_prazos.md", "checklist_manifestacao.md", "minuta_peca.md"),
    "analyze": BASE_ARTIFACTS + ANALYSIS_ARTIFACTS,
    "petition": BASE_ARTIFACTS + ANALYSIS_ARTIFACTS + ("checklist_manifestacao.md", "minuta_peca.md"),
    "deadlines": BASE_ARTIFACTS + ("andamento_processual.json", "relatorio_andamento.md", "pendencias_e_prazos.md"),
    "evidence": BASE_ARTIFACTS + ("andamento_processual.json", "mapa_provas.md", "matriz_documental.md"),
}

TASK_BY_MODE = {
    "AUDIT_FULL": "audit",
    "PETITION_DRAFT": "petition",
    "PROCEDURAL_ANALYSIS": "analyze",
    "EVIDENCE_ANALYSIS": "evidence",
    "CALCULATION_SUPPORT": "deadlines",
}

VISION_POLICIES = ("required", "best_effort", "off")
VISION_PROVIDERS = ("none", "sidecar", "agent_review")


def resolve_task(mode: str, task: str | None) -> str:
    selected = task or TASK_BY_MODE.get(mode, "ingest")
    if selected not in TASKS:
        raise ValueError(f"Tarefa inválida: {selected}. Escolha: {', '.join(TASKS)}")
    return selected


def resolve_vision_configuration(
    source: Path,
    output: Path,
    vision_policy: str,
    vision_provider: str,
    image_descriptions: Path | None,
    vision_review: Path | None,
) -> tuple[str, Path | None]:
    """Resolve a provider-neutral semantic-vision sidecar before processing."""
    if vision_policy not in VISION_POLICIES:
        raise ValueError(f"Política de visão inválida: {vision_policy}")
    if vision_provider not in VISION_PROVIDERS:
        raise ValueError(f"Provider de visão inválido: {vision_provider}")
    if vision_policy == "off":
        return "none", None
    candidate = vision_review if vision_provider == "agent_review" else image_descriptions
    if candidate is None and vision_provider == "agent_review":
        default_review = output / "vision_review.json"
        if default_review.is_file():
            candidate = default_review
    if candidate is not None:
        candidate = candidate.resolve()
    needs_provider = source.suffix.lower() == ".pdf"
    if vision_policy == "required" and needs_provider:
        if vision_provider == "none":
            raise ValueError(
                "Visão semântica obrigatória, mas nenhum provider foi escolhido. "
                "Use --vision-provider sidecar --image-descriptions arquivo.json "
                "ou --vision-provider agent_review --vision-review vision_review.json."
            )
        if candidate is None or not candidate.is_file():
            raise ValueError(
                f"Visão semântica obrigatória, mas o provider '{vision_provider}' não possui "
                "um sidecar disponível. Forneça --image-descriptions/--vision-review."
            )
    if candidate is None or not candidate.is_file():
        return "none", None
    if vision_policy == "required":
        try:
            payload = json.loads(candidate.read_text(encoding="utf-8-sig"))
        except (OSError, json.JSONDecodeError) as exc:
            raise ValueError(f"Sidecar de visão semântica inválido: {candidate} ({exc})") from exc
        if not isinstance(payload, dict) or not isinstance(payload.get("pages"), (dict, list)):
            raise ValueError(
                "Sidecar obrigatório precisa conter a coleção 'pages' com a descrição da página inteira; "
                "consulte templates/vision_review.json."
            )
    return vision_provider, candidate


def _load_json(path: Path) -> dict[str, Any] | None:
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError):
        return None


def query_index(index_path: Path, query: str) -> list[dict[str, Any]]:
    terms = [term.lower() for term in query.split() if term.strip()]
    results: list[dict[str, Any]] = []
    if not index_path.exists():
        return results
    for line in index_path.read_text(encoding="utf-8-sig").splitlines():
        if not line.strip():
            continue
        record = json.loads(line)
        haystack = f"{record.get('text', '')} {' '.join(record.get('terms', []))}".lower()
        if all(term in haystack for term in terms):
            results.append(record)
    return results


def run_ingest(
    source: Path,
    output: Path,
    mode: str = "INGEST",
    chunk_size: int = 50,
    force: bool = False,
    use_ocr: bool = False,
    ocr_language: str = "por+eng",
    ocr_dpi: int = 200,
    image_descriptions: Path | None = None,
    vision_mode: str = "always",
    render_dpi: int = 150,
    task: str | None = None,
    confirmed_scope: bool = False,
    vision_policy: str = "best_effort",
    vision_provider: str = "sidecar",
    vision_review: Path | None = None,
    output_encoding: str = "utf-8",
) -> dict[str, Any]:
    task = resolve_task(mode, task)
    source = source.resolve()
    output = output.resolve()
    if not source.is_file():
        raise FileNotFoundError(f"Arquivo de entrada não encontrado: {source}")
    if output_encoding not in {"utf-8", "utf-8-sig"}:
        raise ValueError("A codificação de saída deve ser utf-8 ou utf-8-sig")
    if vision_mode == "never":
        vision_policy = "off"
    active_vision_provider, vision_sidecar = resolve_vision_configuration(
        source, output, vision_policy, vision_provider, image_descriptions, vision_review
    )
    output.mkdir(parents=True, exist_ok=True)
    digest = sha256_file(source)
    image_descriptions = vision_sidecar
    image_descriptions_digest = sha256_file(image_descriptions) if image_descriptions and image_descriptions.is_file() else None
    existing = _load_json(output / "manifest.json")
    required = list(TASK_ARTIFACTS[task])
    if (
        not force
        and existing
        and existing.get("source", {}).get("sha256") == digest
        and existing.get("schema_version") == "1.2"
        and existing.get("task") == task
        and existing.get("ocr_requested", False) == use_ocr
        and existing.get("image_descriptions_sha256") == image_descriptions_digest
        and existing.get("vision_mode", "always") == vision_mode
        and existing.get("vision_policy", "best_effort") == vision_policy
        and existing.get("vision_provider", "none") == active_vision_provider
        and existing.get("render_dpi", 150) == render_dpi
        and existing.get("encoding", {}).get("output", "utf-8") == output_encoding
        and all((output / name).exists() for name in required)
    ):
        return {"status": "reused", "manifest": existing}

    if existing:
        archive_current_run(output, existing)

    all_artifacts = set(BASE_ARTIFACTS + ANALYSIS_ARTIFACTS + (
        "relatorio_auditoria.md",
        "pendencias_e_prazos.md",
        "checklist_manifestacao.md",
        "minuta_peca.md",
        "assets/pages/",
        "rendered_pages/",
        "images/",
    ))
    for stale_name in sorted(all_artifacts - set(required)):
        stale_path = output / stale_name
        if stale_path.is_file():
            stale_path.unlink()
        elif stale_path.is_dir():
            shutil.rmtree(stale_path)

    preserved_original = copy_original(source, output)
    texts, extraction_warnings, ocr_pages = extract_pages_with_ocr(source, use_ocr=use_ocr, ocr_language=ocr_language, ocr_dpi=ocr_dpi)
    description_overrides = load_image_descriptions(image_descriptions)
    page_descriptions = load_page_descriptions(image_descriptions)
    render_by_page: dict[int, dict[str, Any]] = {}
    render_warnings: list[str] = []
    assets_pages = output / "assets" / "pages"
    assets_pages.mkdir(parents=True, exist_ok=True)
    if source.suffix.lower() == ".pdf" and vision_policy != "off" and vision_mode != "never":
        render_by_page, render_warnings = render_pdf_pages(source, output / "rendered_pages", dpi=render_dpi)
        if (output / "rendered_pages").is_dir():
            shutil.copytree(output / "rendered_pages", assets_pages, dirs_exist_ok=True)
    visuals_by_page: dict[int, list[dict[str, Any]]] = {}
    if source.suffix.lower() == ".pdf":
        visuals_by_page = extract_pdf_visuals(
            source,
            output / "images",
            use_ocr=use_ocr,
            ocr_language=ocr_language,
            descriptions=description_overrides,
        )
    else:
        for page_number, page_text in enumerate(texts, start=1):
            referenced = extract_referenced_visuals(page_text, page_number, source.parent, description_overrides)
            if referenced:
                visuals_by_page[page_number] = referenced
        visuals_by_page = consolidate_visual_inventory(visuals_by_page, output / "images")
    pages, injection_findings = build_pages(
        texts,
        ocr_pages=ocr_pages,
        visuals_by_page=visuals_by_page,
        render_by_page=render_by_page,
        page_descriptions=page_descriptions,
        source_kind=source.suffix.lower(),
        vision_mode=vision_mode,
        vision_provider=active_vision_provider,
        vision_policy=vision_policy,
        ocr_requested=use_ocr,
    )
    process_id = str(classify_process(pages).get("numero_processo")) if pages else f"sha256:{digest[:16]}"
    classification = classify_process(pages)
    pieces = identify_pieces(pages)
    coverage = compute_coverage(pages, len(texts))
    procedural_summary = build_procedural_summary(pages, classification, pieces, coverage)
    checkpoints: list[dict[str, Any]] = []
    for start in range(1, len(pages) + 1, max(1, chunk_size)):
        chunk = pages[start - 1 : start - 1 + max(1, chunk_size)]
        checkpoints.append(
            {
                "checkpoint": {
                    "inicio": start,
                    "fim": chunk[-1].pdf_page if chunk else start - 1,
                    "sucesso": bool(chunk),
                    "paginas_texto": sum(bool(page.text.strip()) for page in chunk),
                    "paginas_visao": sum(page.source != "native_text" for page in chunk),
                    "text_done": [page.pdf_page for page in chunk if page.text.strip()],
                    "render_done": [page.pdf_page for page in chunk if (page.render or {}).get("validated")],
                    "vision_done": [page.pdf_page for page in chunk if (page.vision or {}).get("semantic_checked")],
                    "ocr_done": [page.pdf_page for page in chunk if (page.ocr or {}).get("used")],
                    "consolidated": [page.pdf_page for page in chunk if (page.consolidation or {}).get("completed")],
                    "paginas_problematicas": [page.pdf_page for page in chunk if page.warnings],
                },
                "created_at": now_utc(),
            }
        )
    if extraction_warnings or render_warnings:
        checkpoints.append({"checkpoint": {"inicio": None, "fim": None, "sucesso": False, "erro": [*extraction_warnings, *render_warnings]}, "created_at": now_utc()})

    confidentiality = "restricted" if any(marker in "\n".join(texts).lower() for marker in ("segredo de justiça", "segredo de justica", "sigilo processual")) else "normal"
    limitations = [*extraction_warnings, *render_warnings]
    if coverage.get("semantic_vision_unavailable"):
        limitations.append("Visão semântica não concluída em uma ou mais páginas; conversão integral não foi declarada.")
    manifest: dict[str, Any] = {
        "schema_version": "1.2",
        "process_id": process_id,
        "processed_at": now_utc(),
        "mode": mode,
        "task": task,
        "scope_confirmation": bool(confirmed_scope),
        "available_tasks": list(TASKS),
        "vision_policy": vision_policy,
        "vision_provider": active_vision_provider,
        "vision_review_path": vision_sidecar.name if vision_sidecar else None,
        "encoding": {
            "input": detect_text_encoding(source),
            "output": output_encoding,
        },
        "ocr_requested": use_ocr,
        "image_descriptions_sha256": image_descriptions_digest,
        "vision_mode": vision_mode,
        "render_dpi": render_dpi,
        "source": {
            "name": source.name,
            "path": str(source),
            "size_bytes": source.stat().st_size,
            "sha256": digest,
            "pages": len(texts),
            "preserved_path": preserved_original.relative_to(output).as_posix(),
            "extraction_backend": ("pypdf/PyPDF2 + OCR" if ocr_pages else "pypdf/PyPDF2") if source.suffix.lower() == ".pdf" else "plain-text",
        },
        "confidentiality": confidentiality,
        "coverage": coverage,
        "classification": classification,
        "pieces": pieces,
        "warnings": [*extraction_warnings, *render_warnings],
        "prompt_injection_findings": injection_findings,
        "visual_inventory": [visual for page in pages for visual in (page.visuals or [])],
        "visual_coverage": {
            "elements": coverage.get("visual_elements", 0),
            "pages": coverage.get("pages_with_visuals", 0),
            "reviewed": coverage.get("visual_descriptions_reviewed", 0),
            "pending": coverage.get("visual_descriptions_pending", 0),
            "semantic_required": coverage.get("semantic_vision_required", 0),
            "semantic_completed": coverage.get("semantic_vision_completed", 0),
            "semantic_unavailable": coverage.get("semantic_vision_unavailable", 0),
        },
        "checkpoints": checkpoints,
        "generated_files": list(required) + ["images/", "rendered_pages/", "assets/pages/"],
        "procedural_artifacts": {
            "events": len(procedural_summary["events"]),
            "deadlines": len(procedural_summary["deadlines"]),
            "evidence_mentions": len(procedural_summary["evidence"]),
            "pending_pages": len(procedural_summary["pending_pages"]),
            "tasks": len(procedural_summary["tasks"]),
            "status": procedural_summary["status"],
        },
        "limitations": [
            *limitations,
            *(["Páginas sem camada textual útil foram marcadas para OCR/visão."] if any(page.source == "needs_ocr_or_vision" for page in pages) else []),
        ],
    }

    image_index = build_image_index(pages)
    problematic_pages = build_problematic_pages_report(pages)
    structured_markdown = build_structured_markdown(pages, classification)

    write_json(output / "manifest.json", manifest, encoding=output_encoding)
    if "andamento_processual.json" in required:
        write_json(output / "andamento_processual.json", procedural_summary, encoding=output_encoding)
    write_jsonl(output / "pages.jsonl", (page.to_dict() for page in pages), encoding=output_encoding)
    write_jsonl(output / "index.jsonl", build_index_records(pages, process_id), encoding=output_encoding)
    write_json(
        output / "image_inventory.json",
        {"images": manifest["visual_inventory"], "coverage": manifest["visual_coverage"], "index": image_index},
        encoding=output_encoding,
    )
    (output / "images").mkdir(parents=True, exist_ok=True)
    write_json(output / "images" / "index.json", image_index, encoding=output_encoding)
    write_jsonl(output / "checkpoints.jsonl", checkpoints, encoding=output_encoding)
    (output / "processo_estruturado.md").write_text(structured_markdown, encoding=output_encoding)
    (output / "processo_completo.md").write_text(structured_markdown, encoding=output_encoding)
    (output / "indice_pecas.md").write_text(build_pieces_markdown(pieces), encoding=output_encoding)
    (output / "paginas_problematicas.md").write_text(problematic_pages, encoding=output_encoding)
    if "relatorio_andamento.md" in required:
        (output / "relatorio_andamento.md").write_text(build_andamento_report(procedural_summary), encoding=output_encoding)
    if "cronologia.md" in required:
        (output / "cronologia.md").write_text(build_chronology(pages), encoding=output_encoding)
    if "matriz_controversias.md" in required:
        (output / "matriz_controversias.md").write_text(build_controversy_matrix(pages), encoding=output_encoding)
    if "matriz_documental.md" in required:
        (output / "matriz_documental.md").write_text(build_document_matrix(pieces, pages), encoding=output_encoding)
    if "mapa_provas.md" in required:
        (output / "mapa_provas.md").write_text(build_evidence_map(procedural_summary), encoding=output_encoding)
    if "pendencias_e_prazos.md" in required:
        (output / "pendencias_e_prazos.md").write_text(build_deadlines_report(procedural_summary), encoding=output_encoding)
    if "checklist_manifestacao.md" in required:
        (output / "checklist_manifestacao.md").write_text(build_manifestation_checklist(procedural_summary), encoding=output_encoding)
    if "minuta_peca.md" in required:
        (output / "minuta_peca.md").write_text(build_piece_draft(procedural_summary), encoding=output_encoding)
    if "relatorio_conformidade.md" in required:
        (output / "relatorio_conformidade.md").write_text(build_compliance_report(procedural_summary), encoding=output_encoding)
    if "relatorio_auditoria.md" in required:
        (output / "relatorio_auditoria.md").write_text(build_audit_report(pages, classification, pieces, coverage, mode), encoding=output_encoding)
    (output / "relatorio_processual.md").write_text(build_cumulative_report(output), encoding=output_encoding)
    write_process_bundle(output)
    return {"status": "processed", "manifest": manifest}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Ingere e estrutura um processo sem alterar o original.")
    parser.add_argument("input", type=Path, help="PDF, TXT ou MD; no modo QUERY, diretório de saída")
    parser.add_argument("--output", type=Path, default=Path("processo_saida"), help="Diretório de saída")
    parser.add_argument("--mode", choices=MODES, default="INGEST")
    parser.add_argument("--task", choices=TASKS, help="Executa somente a tarefa solicitada; se omitido, deriva do modo")
    parser.add_argument("--confirm-scope", action="store_true", help="Confirma que a IA perguntou e o usuário aprovou o escopo")
    parser.add_argument("--chunk-size", type=int, default=50, help="Páginas por checkpoint")
    parser.add_argument("--ocr", action="store_true", help="Tenta OCR apenas em páginas PDF sem texto útil")
    parser.add_argument("--ocr-language", default="por+eng", help="Idiomas do Tesseract, por exemplo por+eng")
    parser.add_argument("--ocr-dpi", type=int, default=200, help="DPI usado ao rasterizar páginas para OCR")
    parser.add_argument("--image-descriptions", type=Path, help="JSON com descrições semânticas revisadas por image_id")
    parser.add_argument("--vision-mode", choices=("always", "auto", "never"), default="always", help="Política de visão semântica; sempre é o padrão")
    parser.add_argument("--render-dpi", type=int, default=150, help="DPI da renderização integral das páginas PDF")
    parser.add_argument("--vision-policy", choices=VISION_POLICIES, default="best_effort", help="Política: required, best_effort ou off")
    parser.add_argument("--require-semantic-vision", action="store_const", const="required", dest="vision_policy", help="Atalho para --vision-policy required")
    parser.add_argument("--vision-provider", choices=VISION_PROVIDERS, default="sidecar", help="Provider: sidecar ou agent_review")
    parser.add_argument("--vision-review", type=Path, help="vision_review.json preenchido pelo agente")
    parser.add_argument("--encoding", choices=("utf-8", "utf-8-sig"), default="utf-8", dest="output_encoding", help="Codificação dos arquivos de saída")
    parser.add_argument("--query", help="Termos exatos para o modo QUERY")
    parser.add_argument("--force", action="store_true", help="Reprocessa mesmo com o mesmo SHA-256")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.mode == "QUERY":
            index = args.input / "index.jsonl" if args.input.is_dir() else args.input
            if not args.query:
                raise ValueError("--query é obrigatório no modo QUERY")
            results = query_index(index, args.query)
            print(json.dumps({"query": args.query, "matches": results}, ensure_ascii=False, indent=2))
            return 0
        result = run_ingest(
            args.input,
            args.output,
            args.mode,
            args.chunk_size,
            args.force,
            args.ocr,
            args.ocr_language,
            args.ocr_dpi,
            args.image_descriptions,
            args.vision_mode,
            args.render_dpi,
            task=args.task,
            confirmed_scope=args.confirm_scope,
            vision_policy=args.vision_policy,
            vision_provider=args.vision_provider,
            vision_review=args.vision_review,
            output_encoding=args.output_encoding,
        )
        print(json.dumps({"status": result["status"], "manifest": result["manifest"]}, ensure_ascii=False, indent=2))
        return 0
    except Exception as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
