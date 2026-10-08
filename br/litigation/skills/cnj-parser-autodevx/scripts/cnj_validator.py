#!/usr/bin/env python3
"""
CNJ Case Number Parser and Validator

Validates and parses Brazilian judicial case numbers (CNJ format) according to
Resolution CNJ nº 65/2008. Supports single and batch processing with flexible
output formats (JSON, CSV).

Format: NNNNNNN-DD.AAAA.J.TT.OOOO (20 digits)
"""

import argparse
import csv
import json
import re
import sys
from typing import Dict, List, Optional, Tuple


# Maps for justice segments (J field)
JUSTICA_MAP: Dict[str, str] = {
    "1": "Supremo Tribunal Federal",
    "2": "Conselho Nacional de Justiça",
    "3": "Superior Tribunal de Justiça",
    "4": "Justiça Federal",
    "5": "Justiça do Trabalho",
    "6": "Justiça Eleitoral",
    "7": "Justiça Militar da União",
    "8": "Justiça dos Estados e DF",
    "9": "Justiça Militar Estadual",
}

# Maps for tribunal codes (TT field) - organized by justice type
TRIBUNAL_MAP: Dict[str, Dict[str, str]] = {
    # Justice 4: Federal Courts (TRF)
    "4": {
        "01": "TRF-1",
        "02": "TRF-2",
        "03": "TRF-3",
        "04": "TRF-4",
        "05": "TRF-5",
        "06": "TRF-6",
        "07": "STJ",  # Special case
    },
    # Justice 5: Labor Courts (TRT)
    "5": {
        "01": "TRT-1",
        "02": "TRT-2",
        "03": "TRT-3",
        "04": "TRT-4",
        "05": "TRT-5",
        "06": "TRT-6",
        "07": "TRT-7",
        "08": "TRT-8",
        "09": "TRT-9",
        "10": "TRT-10",
        "11": "TRT-11",
        "12": "TRT-12",
        "13": "TRT-13",
        "14": "TRT-14",
        "15": "TRT-15",
        "16": "TRT-16",
        "17": "TRT-17",
        "18": "TRT-18",
        "19": "TRT-19",
        "20": "TRT-20",
        "21": "TRT-21",
        "22": "TRT-22",
        "23": "TRT-23",
        "24": "TRT-24",
    },
    # Justice 8: State Courts (TJ)
    "8": {
        "01": "TJAC",
        "02": "TJAL",
        "03": "TJAP",
        "04": "TJAM",
        "05": "TJBA",
        "06": "TJCE",
        "07": "TJDF",
        "08": "TJES",
        "09": "TJGO",
        "10": "TJMA",
        "11": "TJMT",
        "12": "TJMS",
        "13": "TJMG",
        "14": "TJPA",
        "15": "TJPB",
        "16": "TJPR",
        "17": "TJPE",
        "18": "TJPI",
        "19": "TJRJ",
        "20": "TJRN",
        "21": "TJRS",
        "22": "TJRO",
        "23": "TJRR",
        "24": "TJSC",
        "25": "TJSE",
        "26": "TJSP",
        "27": "TJTO",
    },
}


def validate_check_digits(
    sequencial: str, dd: str, ano: str, j: str, tt: str, oooo: str
) -> bool:
    """
    Validates CNJ check digits using modulo 97 algorithm per Resolution 65/2008.

    Args:
        sequencial: 7-digit sequential number
        dd: 2-digit check digit (to validate)
        ano: 4-digit year
        j: 1-digit justice segment
        tt: 2-digit tribunal code
        oooo: 4-digit judicial body

    Returns:
        True if check digit is valid, False otherwise
    """
    try:
        # Step 1: Calculate r1
        r1 = int(sequencial) % 97

        # Step 2: Calculate r2
        r2 = int(f"{r1:02d}{ano}{j}{tt}") % 97

        # Step 3: Calculate expected check digit
        dv_calculated = 98 - (int(f"{r2:02d}{oooo}") % 97)

        # Compare with provided check digit
        return dv_calculated == int(dd)
    except (ValueError, IndexError):
        return False


def parse_cnj_number(input_str: str) -> Dict:
    """
    Parses and validates a single CNJ case number.

    Accepts formats:
    - With mask: 0002150-34.2023.8.13.0024
    - Without mask: 00021503420238130024
    - With extra chars: 0002150-34.2023.8.13.0024 (TJMG)

    Args:
        input_str: Raw input string potentially containing a CNJ number

    Returns:
        Dictionary with parsing result including validity, components, and errors
    """
    original_input = input_str.strip()

    # Normalize: extract only digits
    digits_only = re.sub(r"\D", "", input_str)

    # Validate length
    if len(digits_only) != 20:
        return {
            "input_original": original_input,
            "valido": False,
            "numero_formatado": None,
            "componentes": None,
            "erro": f"Tamanho inválido: {len(digits_only)} dígitos (esperado 20)",
        }

    # Segment the number
    sequencial = digits_only[0:7]
    dd = digits_only[7:9]
    ano = digits_only[9:13]
    j = digits_only[13:14]
    tt = digits_only[14:16]
    oooo = digits_only[16:20]

    # Validate check digit
    if not validate_check_digits(sequencial, dd, ano, j, tt, oooo):
        return {
            "input_original": original_input,
            "valido": False,
            "numero_formatado": f"{sequencial}-{dd}.{ano}.{j}.{tt}.{oooo}",
            "componentes": {
                "sequencial": sequencial,
                "digito_verificador": dd,
                "ano": ano,
                "justica_codigo": j,
                "justica_nome": JUSTICA_MAP.get(j, "Desconhecido"),
                "tribunal_codigo": tt,
                "tribunal_sigla": TRIBUNAL_MAP.get(j, {}).get(tt, "N/A"),
                "orgao_julgador": oooo,
            },
            "erro": "Dígito verificador inválido",
        }

    # Valid number - enrich with additional information
    tribunal_sigla = TRIBUNAL_MAP.get(j, {}).get(tt, "N/A")

    return {
        "input_original": original_input,
        "valido": True,
        "numero_formatado": f"{sequencial}-{dd}.{ano}.{j}.{tt}.{oooo}",
        "componentes": {
            "sequencial": sequencial,
            "digito_verificador": dd,
            "ano": ano,
            "justica_codigo": j,
            "justica_nome": JUSTICA_MAP.get(j, "Desconhecido"),
            "tribunal_codigo": tt,
            "tribunal_sigla": tribunal_sigla,
            "orgao_julgador": oooo,
        },
        "erro": None,
    }


def extract_cnj_numbers(text: str) -> List[str]:
    """
    Extracts potential CNJ numbers from text.

    Looks for sequences of exactly 20 digits (with or without mask).

    Args:
        text: Input text potentially containing one or more CNJ numbers

    Returns:
        List of potential CNJ number strings
    """
    # Pattern: 20 digits with optional separators
    pattern = r"\b[\d\-\.]+\b"
    candidates = re.findall(pattern, text)

    cnj_candidates = []
    for candidate in candidates:
        digits = re.sub(r"\D", "", candidate)
        if len(digits) == 20:
            cnj_candidates.append(candidate)

    return cnj_candidates


def process_batch(input_source: Optional[str]) -> List[Dict]:
    """
    Processes multiple CNJ numbers from stdin or file.

    Args:
        input_source: File path or None for stdin

    Returns:
        List of parsing results for each number found
    """
    if input_source:
        try:
            with open(input_source, "r", encoding="utf-8") as f:
                content = f.read()
        except (FileNotFoundError, IOError) as e:
            print(f"Erro ao ler arquivo: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        content = sys.stdin.read()

    # Extract all potential CNJ numbers
    numbers = extract_cnj_numbers(content)

    if not numbers:
        print("Nenhum número CNJ encontrado no input.", file=sys.stderr)
        return []

    # Parse each number
    results = []
    seen = set()

    for num in numbers:
        # Skip duplicates
        normalized = re.sub(r"\D", "", num)
        if normalized in seen:
            continue
        seen.add(normalized)

        result = parse_cnj_number(num)
        results.append(result)

    return results


def output_json(results: List[Dict], pretty: bool = True) -> str:
    """
    Formats results as JSON.

    Args:
        results: List of parsing results
        pretty: If True, pretty-print with indentation

    Returns:
        JSON string
    """
    indent = 2 if pretty else None
    return json.dumps(results, indent=indent, ensure_ascii=False)


def output_csv(results: List[Dict]) -> str:
    """
    Formats results as CSV table.

    Args:
        results: List of parsing results

    Returns:
        CSV string
    """
    output = []

    # Header
    output.append(
        "# | Número CNJ | Válido | Justiça | Tribunal | Ano | Órgão | Erro"
    )

    # Rows
    for i, result in enumerate(results, 1):
        numero = result["numero_formatado"] or result["input_original"]
        valido = "Sim" if result["valido"] else "Não"
        comp = result["componentes"]

        if comp:
            justica = comp.get("justica_nome", "N/A")
            tribunal = comp.get("tribunal_sigla", "N/A")
            ano = comp.get("ano", "N/A")
            orgao = comp.get("orgao_julgador", "N/A")
        else:
            justica = tribunal = ano = orgao = "N/A"

        erro = result["erro"] or ""

        output.append(
            f"{i} | {numero} | {valido} | {justica} | {tribunal} | {ano} | {orgao} | {erro}"
        )

    return "\n".join(output)


def output_table(results: List[Dict]) -> str:
    """
    Formats results as markdown table.

    Args:
        results: List of parsing results

    Returns:
        Markdown table string
    """
    output = []

    # Header
    output.append(
        "| # | Número CNJ | Válido | Justiça | Tribunal | Ano | Órgão | Erro |"
    )
    output.append("|---|---|---|---|---|---|---|---|")

    # Rows
    for i, result in enumerate(results, 1):
        numero = result["numero_formatado"] or result["input_original"]
        valido = "✓" if result["valido"] else "✗"
        comp = result["componentes"]

        if comp:
            justica = comp.get("justica_nome", "N/A")
            tribunal = comp.get("tribunal_sigla", "N/A")
            ano = comp.get("ano", "N/A")
            orgao = comp.get("orgao_julgador", "N/A")
        else:
            justica = tribunal = ano = orgao = "N/A"

        erro = result["erro"] or ""

        output.append(
            f"| {i} | `{numero}` | {valido} | {justica} | {tribunal} | {ano} | {orgao} | {erro} |"
        )

    return "\n".join(output)


def main() -> None:
    """Main entry point for CLI."""
    parser = argparse.ArgumentParser(
        description="Valida e extrai componentes de números de processo CNJ",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:

  # Validar um número direto na linha de comando
  %(prog)s "0002150-34.2023.8.13.0024"

  # Processar múltiplos números de um arquivo
  %(prog)s --batch processos.txt --format table

  # Ler de stdin e retornar JSON
  cat processos.txt | %(prog)s --batch --format json

  # Validar número sem máscara
  %(prog)s "00021503420238130024"
        """,
    )

    parser.add_argument(
        "numero",
        nargs="?",
        help="Número CNJ a validar (formato com ou sem máscara)",
    )

    parser.add_argument(
        "-b",
        "--batch",
        action="store_true",
        help="Modo lote: lê do arquivo especificado ou stdin",
    )

    parser.add_argument(
        "-f",
        "--format",
        choices=["json", "csv", "table"],
        default="table",
        help="Formato de saída (default: table)",
    )

    parser.add_argument(
        "--input",
        type=str,
        help="Arquivo de entrada para modo lote (padrão: stdin)",
    )

    args = parser.parse_args()

    # Batch mode
    if args.batch or not args.numero:
        results = process_batch(args.input)

        if args.format == "json":
            print(output_json(results, pretty=True))
        elif args.format == "csv":
            print(output_csv(results))
        else:  # table
            print(output_table(results))
    else:
        # Single number mode
        result = parse_cnj_number(args.numero)

        if args.format == "json":
            print(output_json([result], pretty=True))
        elif args.format == "csv":
            print(output_csv([result]))
        else:  # table
            print(output_table([result]))


if __name__ == "__main__":
    main()
