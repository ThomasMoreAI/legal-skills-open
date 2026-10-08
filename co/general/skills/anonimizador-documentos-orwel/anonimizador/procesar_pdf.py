"""Anonimización de PDF con texto seleccionable (PyMuPDF)."""

from __future__ import annotations

from pathlib import Path

from motor_anonimizacion import Hallazgo, MotorAnonimizacion


def extraer_texto_pdf(ruta: Path) -> str:
    import fitz

    doc = fitz.open(str(ruta))
    try:
        partes = [page.get_text() for page in doc]
    finally:
        doc.close()
    texto = "\n".join(partes).strip()
    if len(texto) < 20:
        raise ValueError(
            "El PDF parece escaneado o sin texto seleccionable. "
            "Conviértelo a .docx con OCR antes de anonimizar.")
    return texto


def extraer_parrafos_pdf(ruta: Path) -> list[str]:
    texto = extraer_texto_pdf(ruta)
    return [ln for ln in texto.splitlines() if ln.strip()]


def _candidatos_busqueda(h: Hallazgo) -> list[str]:
    vistos: set[str] = set()
    out: list[str] = []
    for c in list(dict.fromkeys((h.variantes or []) + [h.texto])):
        c = c.strip()
        if not c or c in vistos:
            continue
        vistos.add(c)
        out.append(c)
    return out


def procesar_pdf(ruta: Path, motor: MotorAnonimizacion,
                 hallazgos: list[Hallazgo], registro: dict,
                 carpeta_salida: Path | None = None) -> Path:
    import fitz

    doc = fitz.open(str(ruta))
    activos = [h for h in hallazgos if h.activo]
    pares: list[tuple[str, str]] = []
    vistos: set[str] = set()

    for h in activos:
        for buscar in _candidatos_busqueda(h):
            if buscar in vistos:
                continue
            vistos.add(buscar)
            pares.append((buscar, h.reemplazo))
            registro[buscar] = h.reemplazo

    pares.sort(key=lambda x: -len(x[0]))

    try:
        for page in doc:
            for buscar, reemplazo in pares:
                for rect in page.search_for(buscar):
                    page.add_redact_annot(
                        rect, text=reemplazo, fill=(1, 1, 1), text_color=(0, 0, 0))
            page.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE)

        doc.set_metadata({})
        destino = carpeta_salida if carpeta_salida else ruta.parent
        destino.mkdir(parents=True, exist_ok=True)
        salida = destino / f"{ruta.stem}_ANONIMIZADO.pdf"
        doc.save(str(salida), garbage=4, deflate=True)
    finally:
        doc.close()

    return salida
