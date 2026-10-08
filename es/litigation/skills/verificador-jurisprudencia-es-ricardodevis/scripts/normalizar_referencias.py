"""
Normaliza una cita extraída a la estructura que espera cada sub-agente.
"""
from __future__ import annotations
import re
from typing import Dict, Optional


MESES = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4,
    "mayo": 5, "junio": 6, "julio": 7, "agosto": 8,
    "septiembre": 9, "setiembre": 9, "octubre": 10,
    "noviembre": 11, "diciembre": 12,
}


def parsear_fecha_es(texto: str) -> Optional[str]:
    """Convierte '15 de marzo de 2024' a '2024-03-15'.

    Si el día es imposible (e.g. 31 de febrero), devuelve None
    para que el llamante marque la cita como sospechosa.
    """
    if not texto:
        return None
    m = re.match(r"(\d{1,2})\s+de\s+(\w+)\s+de\s+(\d{4})", texto.strip(), re.IGNORECASE)
    if not m:
        return None
    dia_s, mes_nombre, anio_s = m.groups()
    mes = MESES.get(mes_nombre.lower())
    if not mes:
        return None
    try:
        from datetime import date
        date(int(anio_s), mes, int(dia_s))
    except ValueError:
        # Fecha imposible (e.g. 31 de febrero)
        return None
    return f"{anio_s}-{mes:02d}-{int(dia_s):02d}"


def normalizar_para_cendoj(cita: Dict) -> Dict:
    datos = cita.get("datos", {})
    salida: Dict = {
        "tipo": cita["tipo"],
        "texto_original": cita["texto_original"],
    }
    if "numero" in datos:
        salida["numero_recurso"] = datos["numero"]
    if "fecha" in datos:
        fecha_iso = parsear_fecha_es(datos["fecha"])
        if fecha_iso:
            salida["fecha"] = fecha_iso
        else:
            salida["fecha_imposible"] = datos["fecha"]
    return salida


def normalizar_para_tc(cita: Dict) -> Dict:
    datos = cita.get("datos", {})
    numero = datos.get("numero", "")
    salida = {"tipo": cita["tipo"], "texto_original": cita["texto_original"]}
    if "/" in numero:
        num, anio = numero.split("/")
        salida["numero"] = num
        salida["anio"] = anio
    return salida


def normalizar_para_eurlex(cita: Dict) -> Dict:
    datos = cita.get("datos", {})
    salida = {"tipo": cita["tipo"], "texto_original": cita["texto_original"]}
    if "asunto" in datos:
        salida["asunto"] = datos["asunto"]
    if "numero" in datos:
        salida["numero"] = datos["numero"]
    return salida


def normalizar_para_boe(cita: Dict, fecha_escrito: Optional[str] = None) -> Dict:
    datos = cita.get("datos", {})
    return {
        "tipo": cita["tipo"],
        "texto_original": cita["texto_original"],
        "numero": datos.get("numero"),
        "articulo": datos.get("articulo"),
        "norma": datos.get("norma"),
        "fecha_referencia_escrito": fecha_escrito,
    }


def normalizar_para_doctrina(cita: Dict) -> Dict:
    datos = cita.get("datos", {})
    return {
        "tipo": cita["tipo"],
        "texto_original": cita["texto_original"],
        "autor": datos.get("autor"),
        "obra": datos.get("obra"),
        "editorial": datos.get("editorial"),
        "anio": datos.get("anio"),
    }


def enrutar(cita: Dict) -> str:
    """Decide qué sub-agente debe atender una cita.

    Devuelve el nombre del sub-agente ('cendoj', 'tc', 'eurlex',
    'boe', 'doctrina') o 'no_estructurada' si no encaja.
    """
    tipo = cita.get("tipo", "")
    if tipo in ("STS", "ATS", "STSJ", "SAP", "SAN", "AAN"):
        return "cendoj"
    if tipo in ("STC", "ATC"):
        return "tc"
    if tipo in ("STJUE", "REGLAMENTO_UE", "DIRECTIVA"):
        return "eurlex"
    if tipo in ("LEY", "RD", "ARTICULO"):
        return "boe"
    if tipo == "DOCTRINA":
        return "doctrina"
    return "no_estructurada"
