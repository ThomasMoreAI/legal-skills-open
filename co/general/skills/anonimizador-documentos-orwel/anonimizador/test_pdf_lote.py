"""Pruebas de PDF y recolección de rutas — datos ficticios."""

import tempfile
from pathlib import Path

import fitz

from anonimizador import es_formato_soportado, extraer_texto, procesar, recolectar_rutas
from motor_anonimizacion import MotorAnonimizacion


def _crear_pdf_ficticio(ruta: Path, texto: str) -> None:
    doc = fitz.open()
    page = doc.new_page()
    page.insert_text((72, 72), texto, fontsize=11)
    doc.save(str(ruta))
    doc.close()


def test_extraer_y_anonimizar_pdf():
    texto = (
        "El señor CARLOS MENDOZA identificado con cédula 12.345.678 "
        "solicita la tutela. Correo: carlos.mendoza@ejemplo.com"
    )
    with tempfile.TemporaryDirectory() as tmp:
        entrada = Path(tmp) / "expediente_ficticio.pdf"
        _crear_pdf_ficticio(entrada, texto)

        extraido = extraer_texto(entrada)
        assert "CARLOS MENDOZA" in extraido

        motor = MotorAnonimizacion()
        hallazgos = motor.analizar(extraido)
        activos = [h for h in hallazgos if h.activo]
        assert activos

        salida, tabla, n, fugas = procesar(entrada, hallazgos)
        assert salida.exists()
        assert salida.suffix == ".pdf"
        assert tabla.exists()
        assert n > 0

        texto_salida = extraer_texto(salida)
        assert "CARLOS MENDOZA" not in texto_salida.upper()
        assert "carlos.mendoza@ejemplo.com" not in texto_salida.lower()


def test_rechaza_pdf_escaneado():
    with tempfile.TemporaryDirectory() as tmp:
        entrada = Path(tmp) / "escaneado.pdf"
        doc = fitz.open()
        doc.new_page()
        doc.save(str(entrada))
        doc.close()
        try:
            extraer_texto(entrada)
            assert False, "Debía rechazar PDF sin texto"
        except ValueError as e:
            assert "escaneado" in str(e).lower() or "texto" in str(e).lower()


def test_recolectar_rutas_carpeta():
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        (base / "a.txt").write_text("texto a", encoding="utf-8")
        (base / "b.md").write_text("texto b", encoding="utf-8")
        (base / "foto.jpg").write_bytes(b"\xff\xd8\xff")
        _crear_pdf_ficticio(base / "c.pdf", "Documento ficticio con suficiente texto para pasar.")

        rutas = recolectar_rutas([str(base)])
        nombres = {p.name for p in rutas}
        assert "a.txt" in nombres
        assert "b.md" in nombres
        assert "c.pdf" in nombres
        assert "foto.jpg" not in nombres
        assert es_formato_soportado(base / "c.pdf")


if __name__ == "__main__":
    test_extraer_y_anonimizar_pdf()
    print("OK  test_extraer_y_anonimizar_pdf")
    test_rechaza_pdf_escaneado()
    print("OK  test_rechaza_pdf_escaneado")
    test_recolectar_rutas_carpeta()
    print("OK  test_recolectar_rutas_carpeta")
