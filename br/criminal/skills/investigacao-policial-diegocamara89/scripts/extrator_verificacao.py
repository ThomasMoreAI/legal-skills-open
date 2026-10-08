#!/usr/bin/env python3
"""
extrator_verificacao.py - Extracao direcionada de trechos de documentos

Usado pelo subagente validador para verificar referencias contra fontes brutas.
Extrai uma pagina/secao especifica de um arquivo, sem processar o documento inteiro.

Uso:
    python extrator_verificacao.py --arquivo documento.pdf --pagina 37
    python extrator_verificacao.py --arquivo planilha.xlsx --aba "Sheet1" --celulas "A1:D10"
    python extrator_verificacao.py --arquivo texto.docx --paragrafo 5
    python extrator_verificacao.py --arquivo imagem.png
    python extrator_verificacao.py --arquivo dados.csv --linhas "10-20"
    python extrator_verificacao.py --arquivo dados.txt --linha-inicial 5205 --linha-final 5215
    python extrator_verificacao.py --arquivo documento.pdf --pagina 37 --buscar "187.34.56.78"
    python extrator_verificacao.py --arquivo planilha.xlsx --aba "Plan1" --excel-row 5

Saida: JSON com {texto_extraido, arquivo, pagina, metodo_extracao, hash_arquivo, busca}
"""

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path


# --- Regex deterministicas para entidades investigativas ---

_RE_IPV4 = re.compile(
    r"\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b"
    r"(?::(\d{1,5}))?"
)
_RE_IPV6 = re.compile(
    r"\b(?:[0-9a-fA-F]{1,4}:){2,7}[0-9a-fA-F]{1,4}\b"
)
_RE_CPF = re.compile(
    r"\b(\d{3}[.\s]?\d{3}[.\s]?\d{3}[-.\s]?\d{2})\b"
)
_RE_TELEFONE = re.compile(
    r"(?:\+55\s?)?(?:\(?\d{2}\)?\s?)?\d{4,5}[-.\s]?\d{4}\b"
)
_RE_IMEI = re.compile(
    r"\b\d{15}\b"
)
_RE_EMAIL = re.compile(
    r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"
)
_RE_PIX_CHAVE = re.compile(
    r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b",
    re.IGNORECASE,
)
_RE_VALOR_BRL = re.compile(
    r"R\$\s?[\d.,]+\b"
)


def detectar_entidades(texto):
    """Detecta entidades investigativas via regex no texto extraido.

    Retorna dict com listas de entidades encontradas por tipo.
    Essa camada e deterministica (nao depende da IA) e serve como
    cross-check para o extrator subagente.
    """
    if not texto:
        return {}

    entidades = {}

    ipv4 = [m.group(0).rstrip(":") for m in _RE_IPV4.finditer(texto)]
    if ipv4:
        entidades["ipv4"] = sorted(set(ipv4))

    ipv6 = _RE_IPV6.findall(texto)
    if ipv6:
        entidades["ipv6"] = sorted(set(ipv6))

    cpfs = _RE_CPF.findall(texto)
    if cpfs:
        entidades["cpf"] = sorted(set(cpfs))

    telefones = [m.group(0) for m in _RE_TELEFONE.finditer(texto)]
    if telefones:
        entidades["telefone"] = sorted(set(telefones))

    imeis = _RE_IMEI.findall(texto)
    if imeis:
        entidades["imei"] = sorted(set(imeis))

    emails = _RE_EMAIL.findall(texto)
    if emails:
        entidades["email"] = sorted(set(emails))

    pix = _RE_PIX_CHAVE.findall(texto)
    if pix:
        entidades["chave_pix_uuid"] = sorted(set(pix))

    valores = _RE_VALOR_BRL.findall(texto)
    if valores:
        entidades["valor_brl"] = sorted(set(valores))

    return entidades


def calcular_hash(filepath):
    """Calcula SHA256 do arquivo para integridade."""
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for bloco in iter(lambda: f.read(8192), b""):
            sha256.update(bloco)
    return sha256.hexdigest()


def extrair_pdf_pagina(filepath, pagina):
    """Extrai texto de uma pagina especifica de PDF."""
    try:
        import pdfplumber

        with pdfplumber.open(filepath) as pdf:
            if pagina < 1 or pagina > len(pdf.pages):
                return {
                    "texto_extraido": None,
                    "erro": f"Pagina {pagina} nao existe. PDF tem {len(pdf.pages)} paginas.",
                    "metodo_extracao": "erro",
                }
            page = pdf.pages[pagina - 1]
            texto = page.extract_text()

            # Tentar extrair tabelas tambem
            tabelas = page.extract_tables()
            texto_tabelas = ""
            for i, tab in enumerate(tabelas):
                if tab:
                    texto_tabelas += f"\n[TABELA {i+1}]\n"
                    for row in tab:
                        texto_tabelas += " | ".join(
                            [str(c) if c else "" for c in row]
                        ) + "\n"

            if texto and len(texto.strip()) > 20:
                resultado = texto
                if texto_tabelas:
                    resultado += "\n" + texto_tabelas
                return {
                    "texto_extraido": resultado,
                    "metodo_extracao": "pdfplumber",
                }
            else:
                # Fallback para OCR
                return extrair_pdf_ocr_pagina(filepath, pagina)

    except ImportError:
        return extrair_pdf_ocr_pagina(filepath, pagina)
    except Exception as e:
        return {
            "texto_extraido": None,
            "erro": str(e),
            "metodo_extracao": "erro",
        }


def extrair_pdf_ocr_pagina(filepath, pagina):
    """Fallback OCR para pagina de PDF."""
    try:
        from pdf2image import convert_from_path
        import pytesseract

        images = convert_from_path(
            filepath, first_page=pagina, last_page=pagina, dpi=300
        )
        if images:
            texto = pytesseract.image_to_string(images[0], lang="por")
            if texto and texto.strip():
                return {
                    "texto_extraido": texto,
                    "metodo_extracao": "OCR_pytesseract_300dpi",
                }
        return {
            "texto_extraido": None,
            "erro": "OCR nao extraiu texto legivel",
            "metodo_extracao": "OCR_falha",
        }
    except ImportError as e:
        return {
            "texto_extraido": None,
            "erro": f"Dependencia OCR nao instalada: {e}",
            "metodo_extracao": "OCR_indisponivel",
        }
    except Exception as e:
        return {
            "texto_extraido": None,
            "erro": str(e),
            "metodo_extracao": "erro",
        }


def extrair_xlsx(filepath, aba=None, celulas=None):
    """Extrai dados de planilha XLSX/XLS."""
    try:
        import pandas as pd

        if aba:
            df = pd.read_excel(filepath, sheet_name=aba, header=None)
        else:
            df = pd.read_excel(filepath, header=None)

        if celulas:
            # Formato "A1:D10" ou "B7"
            import re
            match = re.match(r"([A-Z]+)(\d+)(?::([A-Z]+)(\d+))?", celulas.upper())
            if match:
                col_start = _col_to_idx(match.group(1))
                row_start = int(match.group(2)) - 1
                if match.group(3):
                    col_end = _col_to_idx(match.group(3)) + 1
                    row_end = int(match.group(4))
                else:
                    col_end = col_start + 1
                    row_end = row_start + 1
                df = df.iloc[row_start:row_end, col_start:col_end]

        texto = df.to_string(index=True, header=True)
        return {
            "texto_extraido": texto,
            "metodo_extracao": "pandas_openpyxl",
        }
    except Exception as e:
        return {
            "texto_extraido": None,
            "erro": str(e),
            "metodo_extracao": "erro",
        }


def _col_to_idx(col_letter):
    """Converte letra de coluna para indice (A=0, B=1, ..., Z=25, AA=26)."""
    result = 0
    for char in col_letter.upper():
        result = result * 26 + (ord(char) - ord("A") + 1)
    return result - 1


def extrair_docx(filepath, paragrafo=None):
    """Extrai texto de DOCX."""
    try:
        from docx import Document

        doc = Document(filepath)
        paragrafos = [p.text for p in doc.paragraphs if p.text.strip()]

        if paragrafo is not None:
            if paragrafo < 1 or paragrafo > len(paragrafos):
                return {
                    "texto_extraido": None,
                    "erro": f"Paragrafo {paragrafo} nao existe. DOCX tem {len(paragrafos)} paragrafos com texto.",
                    "metodo_extracao": "erro",
                }
            # Retornar o paragrafo + contexto (2 antes, 2 depois)
            inicio = max(0, paragrafo - 3)
            fim = min(len(paragrafos), paragrafo + 2)
            texto = "\n".join(
                [f"[par {i+1}] {paragrafos[i]}" for i in range(inicio, fim)]
            )
            return {
                "texto_extraido": texto,
                "metodo_extracao": "python-docx",
            }
        else:
            texto = "\n".join(paragrafos)
            return {
                "texto_extraido": texto,
                "metodo_extracao": "python-docx",
            }
    except ImportError:
        # Fallback para pandoc
        try:
            import subprocess

            result = subprocess.run(
                ["pandoc", filepath, "-t", "plain"],
                capture_output=True,
                text=True,
                timeout=30,
            )
            return {
                "texto_extraido": result.stdout,
                "metodo_extracao": "pandoc",
            }
        except Exception as e:
            return {
                "texto_extraido": None,
                "erro": str(e),
                "metodo_extracao": "erro",
            }
    except Exception as e:
        return {
            "texto_extraido": None,
            "erro": str(e),
            "metodo_extracao": "erro",
        }


def extrair_imagem(filepath):
    """Extrai texto de imagem via OCR."""
    try:
        import pytesseract
        from PIL import Image

        img = Image.open(filepath)
        texto = pytesseract.image_to_string(img, lang="por")
        if texto and texto.strip():
            return {
                "texto_extraido": texto,
                "metodo_extracao": "OCR_pytesseract",
            }
        return {
            "texto_extraido": None,
            "erro": "OCR nao extraiu texto legivel da imagem",
            "metodo_extracao": "OCR_falha",
        }
    except Exception as e:
        return {
            "texto_extraido": None,
            "erro": str(e),
            "metodo_extracao": "erro",
        }


def _ler_arquivo_texto(filepath):
    """Le arquivo texto tentando multiplos encodings. Retorna lista de linhas ou None."""
    for enc in ["utf-8", "latin-1", "cp1252"]:
        try:
            with open(filepath, "r", encoding=enc) as f:
                return f.readlines()
        except UnicodeDecodeError:
            continue
    return None


def extrair_csv_txt(filepath, linhas=None, linha_inicial=None, linha_final=None,
                    contexto_extra=2):
    """Extrai texto de CSV ou TXT.

    Parametros:
        linhas: range no formato "10-20" ou numero unico "15" (legacy)
        linha_inicial: linha de inicio (1-indexed), alternativa a linhas
        linha_final: linha de fim (1-indexed, inclusivo), alternativa a linhas
        contexto_extra: linhas adicionais antes/apos a faixa (default 2)
    """
    try:
        todas_linhas = _ler_arquivo_texto(filepath)
        if todas_linhas is None:
            return {
                "texto_extraido": None,
                "erro": "Nao foi possivel decodificar o arquivo (tentado utf-8, latin-1, cp1252)",
                "metodo_extracao": "erro",
            }

        total = len(todas_linhas)

        # Resolver faixa de linhas
        if linha_inicial is not None:
            ini = max(1, linha_inicial - contexto_extra)
            fim = min(total, (linha_final if linha_final is not None else linha_inicial) + contexto_extra)
            offset = ini
            trecho = todas_linhas[ini - 1:fim]
        elif linhas:
            parts = str(linhas).split("-")
            ini = int(parts[0])
            fim = int(parts[1]) if len(parts) > 1 else ini
            offset = ini
            trecho = todas_linhas[ini - 1:fim]
        else:
            offset = 1
            trecho = todas_linhas

        texto = "".join(f"[L{offset + i}] {linha}" for i, linha in enumerate(trecho))

        return {
            "texto_extraido": texto,
            "metodo_extracao": "leitura_direta",
            "total_linhas_arquivo": total,
            "faixa_extraida": f"L{offset}-L{offset + len(trecho) - 1}",
        }
    except Exception as e:
        return {
            "texto_extraido": None,
            "erro": str(e),
            "metodo_extracao": "erro",
        }


def buscar_no_texto(texto, termo):
    """Busca um termo no texto e retorna as linhas que contem o termo com contexto."""
    if not texto or not termo:
        return None

    linhas = texto.split("\n")
    resultados = []
    for i, linha in enumerate(linhas):
        if termo.lower() in linha.lower():
            # Contexto: 2 linhas antes e depois
            inicio = max(0, i - 2)
            fim = min(len(linhas), i + 3)
            contexto = "\n".join(linhas[inicio:fim])
            resultados.append({
                "linha": i + 1,
                "texto_linha": linha.strip(),
                "contexto": contexto,
            })

    return resultados if resultados else None


def main():
    parser = argparse.ArgumentParser(
        description="Extracao direcionada de trechos de documentos para verificacao"
    )
    parser.add_argument("--arquivo", required=True, help="Caminho do arquivo")
    parser.add_argument("--pagina", type=int, help="Numero da pagina (PDF, 1-indexed)")
    parser.add_argument("--aba", help="Nome da aba (XLSX)")
    parser.add_argument("--celulas", help="Range de celulas (XLSX, formato A1:D10)")
    parser.add_argument("--paragrafo", type=int, help="Numero do paragrafo (DOCX)")
    parser.add_argument("--linhas", help="Range de linhas (CSV/TXT, formato 10-20)")
    parser.add_argument("--linha-inicial", type=int, dest="linha_inicial",
                        help="Linha inicial para extracao de TXT (1-indexed)")
    parser.add_argument("--linha-final", type=int, dest="linha_final",
                        help="Linha final para extracao de TXT (1-indexed, inclusivo)")
    parser.add_argument("--contexto", type=int, default=2, dest="contexto",
                        help="Linhas de contexto extra antes/apos a faixa (default 2)")
    parser.add_argument("--excel-row", type=int, dest="excel_row",
                        help="Numero da linha Excel real (XLSX, 1-indexed com cabecalho)")
    parser.add_argument("--buscar", help="Termo para buscar no texto extraido")
    parser.add_argument(
        "--formato", default="json", choices=["json", "texto"],
        help="Formato de saida"
    )

    args = parser.parse_args()

    if not os.path.exists(args.arquivo):
        resultado = {
            "texto_extraido": None,
            "arquivo": args.arquivo,
            "pagina": args.pagina,
            "metodo_extracao": "erro",
            "hash_arquivo": None,
            "erro": f"Arquivo nao encontrado: {args.arquivo}",
        }
        print(json.dumps(resultado, ensure_ascii=False, indent=2))
        sys.exit(1)

    ext = Path(args.arquivo).suffix.lower()
    hash_arquivo = calcular_hash(args.arquivo)

    # Roteamento por tipo de arquivo
    if ext == ".pdf":
        pagina = args.pagina or 1
        resultado = extrair_pdf_pagina(args.arquivo, pagina)
        resultado["pagina"] = pagina

    elif ext in [".xlsx", ".xls"]:
        resultado = extrair_xlsx(args.arquivo, aba=args.aba, celulas=args.celulas)
        resultado["pagina"] = None
        resultado["aba"] = args.aba
        resultado["celulas"] = args.celulas

    elif ext == ".docx":
        resultado = extrair_docx(args.arquivo, paragrafo=args.paragrafo)
        resultado["pagina"] = None
        resultado["paragrafo"] = args.paragrafo

    elif ext in [".jpg", ".jpeg", ".png", ".tiff", ".bmp", ".webp"]:
        resultado = extrair_imagem(args.arquivo)
        resultado["pagina"] = None

    elif ext in [".csv", ".txt", ".tsv", ".log"]:
        resultado = extrair_csv_txt(
            args.arquivo,
            linhas=args.linhas,
            linha_inicial=args.linha_inicial,
            linha_final=args.linha_final,
            contexto_extra=args.contexto,
        )
        resultado["pagina"] = None
        resultado["linhas"] = args.linhas

    else:
        resultado = {
            "texto_extraido": None,
            "metodo_extracao": "nao_suportado",
            "erro": f"Formato {ext} nao suportado. Suportados: PDF, XLSX, XLS, DOCX, PNG, JPG, TIFF, BMP, CSV, TXT",
        }

    # Adicionar metadados comuns
    resultado["arquivo"] = args.arquivo
    resultado["hash_arquivo"] = hash_arquivo

    # Detectar entidades via regex (camada deterministica)
    if resultado.get("texto_extraido"):
        entidades = detectar_entidades(resultado["texto_extraido"])
        if entidades:
            resultado["entidades_detectadas"] = entidades

    # Buscar termo no texto extraido (se solicitado)
    if args.buscar and resultado.get("texto_extraido"):
        resultado["busca"] = {
            "termo": args.buscar,
            "resultados": buscar_no_texto(resultado["texto_extraido"], args.buscar),
        }

    # Saida
    if args.formato == "json":
        print(json.dumps(resultado, ensure_ascii=False, indent=2))
    else:
        if resultado.get("texto_extraido"):
            print(resultado["texto_extraido"])
        else:
            print(f"ERRO: {resultado.get('erro', 'Falha na extracao')}")
            sys.exit(1)


if __name__ == "__main__":
    main()
