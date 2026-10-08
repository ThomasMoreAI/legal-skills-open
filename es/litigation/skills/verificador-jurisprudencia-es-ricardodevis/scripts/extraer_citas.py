"""
Pre-procesado de extracción de citas mediante regex.

Apoya al sub-agente coordinador pero NO sustituye su juicio semántico.
Diseñado para ser determinista, testeable, y conservador (prefiere
falsos positivos a falsos negativos: nunca descarta silenciosamente
algo que pueda ser cita).
"""
from __future__ import annotations
import re
import json
import sys
from typing import List, Dict


PATRONES: Dict[str, re.Pattern] = {
    "STS": re.compile(
        r"\b(STS|ATS)\s+"
        r"(?:n[úu]m\.?\s*)?"
        r"(?P<numero>\d+/\d{4})?"
        r"(?:\s*,?\s*(?:de\s+)?(?P<fecha>\d{1,2}\s+de\s+\w+\s+de\s+\d{4}))?",
        re.IGNORECASE,
    ),
    "STC": re.compile(
        r"\b(STC|ATC)\s+(?P<numero>\d+/\d{4})",
        re.IGNORECASE,
    ),
    "STJUE": re.compile(
        r"(?:STJUE|Sentencia\s+del\s+TJUE|Sentencia\s+del\s+Tribunal\s+de\s+Justicia)"
        r"[^.]*?[Aa]sunto\s+(?P<asunto>C-\d+/\d{2,4})",
        re.IGNORECASE | re.DOTALL,
    ),
    "STSJ": re.compile(
        r"\bSTSJ\s+(?:de\s+)?(?P<ccaa>[A-ZÁÉÍÓÚÑ][a-záéíóúñ ]+?)?\s*(?P<numero>\d+/\d{4})?",
        re.IGNORECASE,
    ),
    "SAP": re.compile(
        r"\bSAP\s+(?:de\s+)?(?P<provincia>[A-ZÁÉÍÓÚÑ][a-záéíóúñ ]+?)?\s*(?P<numero>\d+/\d{4})?",
        re.IGNORECASE,
    ),
    "LEY": re.compile(
        r"\b(?:Ley\s+Org[áa]nica|Ley|LO)\s+(?P<numero>\d+/\d{4})",
        re.IGNORECASE,
    ),
    "RD": re.compile(
        r"\b(?:Real\s+Decreto(?:-[Ll]ey)?|RDL?)\s+(?P<numero>\d+/\d{4})",
        re.IGNORECASE,
    ),
    "REGLAMENTO_UE": re.compile(
        r"Reglamento\s+\(UE\)\s+(?P<numero>\d{4}/\d+)",
        re.IGNORECASE,
    ),
    "DIRECTIVA": re.compile(
        r"Directiva\s+(?P<numero>\d{4}/\d+/(?:UE|CE))",
        re.IGNORECASE,
    ),
    "ARTICULO": re.compile(
        r"\b(?:art\.?|art[íi]culo)\s+(?P<articulo>\d+(?:\.\d+)?(?:\.[a-z])?)"
        r"(?:\s+(?:de\s+(?:la|el)\s+)?(?P<norma>[A-Z][^,.;\n]{2,80}))?",
        re.IGNORECASE,
    ),
    "DGT": re.compile(
        r"\b(?:consulta\s+vinculante\s+)?V(?P<numero>\d{4}-\d{2})",
        re.IGNORECASE,
    ),
    "DOCTRINA": re.compile(
        # Apellido(s) en mayúsculas + obra entre comillas + (editorial|año|página)
        r"\b(?P<autor>[A-ZÁÉÍÓÚÑ]{2,}(?:\s+[A-ZÁÉÍÓÚÑ]{2,})?(?:,\s+[A-Z]\.?)?)"
        r"\s*,?\s*"
        r"[\"«](?P<obra>[^\"»]{5,150})[\"»]"
        r"[^.]{0,200}?"
        r"(?:(?P<editorial>Aranzadi|Tirant|Civitas|Marcial\s+Pons|La\s+Ley|Bosch|Wolters\s+Kluwer))?"
        r"[^.]{0,80}?"
        r"(?:(?P<anio>\b(?:19|20|21)\d{2}\b))?",
    ),
}


def extraer(texto: str) -> List[Dict]:
    """Extrae todas las citas detectables del texto.

    Devuelve una lista de dicts con campos:
      - tipo: categoría (STS, STC, LEY, etc.)
      - texto_original: fragmento literal del match
      - posicion: índice del inicio en el texto
      - datos: dict con los named groups del regex que matchearon
    """
    resultados: List[Dict] = []
    posiciones_vistas: set = set()
    for tipo, patron in PATRONES.items():
        for match in patron.finditer(texto):
            pos = match.start()
            if pos in posiciones_vistas:
                continue
            datos = {k: v for k, v in match.groupdict().items() if v}
            # Filtrar matches vacíos (sin datos útiles)
            if not datos and tipo not in ("STS", "STSJ", "SAP"):
                continue
            resultados.append({
                "tipo": tipo,
                "texto_original": match.group(0).strip(),
                "posicion": pos,
                "datos": datos,
            })
            posiciones_vistas.add(pos)
    resultados.sort(key=lambda x: x["posicion"])
    return resultados


def main() -> int:
    if len(sys.argv) != 2:
        print("Uso: python extraer_citas.py <fichero_texto>", file=sys.stderr)
        return 1
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        texto = f.read()
    citas = extraer(texto)
    print(json.dumps(citas, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
