#!/usr/bin/env python3
"""
legal-pyme-mx · validate_curp.py
Valida estructura y dígito verificador de CURP mexicana según reglas RENAPO.

Uso:
  validate_curp.py <CURP>
  echo "CURP" | validate_curp.py --stdin

Devuelve JSON. NO consulta el servicio online del gob.mx (no hay API pública abierta).
"""
import argparse
import json
import re
import sys

# Estructura CURP (18 caracteres):
#   AAAA      = 4 letras: 1 letra del primer apellido + 1 vocal interna del primer apellido + 1 letra primer apellido del segundo + 1 letra del nombre
#   AAMMDD    = fecha de nacimiento
#   S         = sexo (H/M)
#   EE        = entidad de nacimiento (2 letras)
#   CCC       = 3 consonantes (1 de cada apellido y del nombre)
#   X         = carácter alfanumérico que distingue homonimias
#   D         = dígito verificador (calculable)
RE_CURP = re.compile(r"^([A-Z]{4})(\d{2})(\d{2})(\d{2})([HM])([A-Z]{2})([B-DF-HJ-NP-TV-Z]{3})([A-Z0-9])(\d)$")

ENTIDADES_VALIDAS = {
    "AS": "Aguascalientes", "BC": "Baja California", "BS": "Baja California Sur",
    "CC": "Campeche", "CL": "Coahuila", "CM": "Colima", "CS": "Chiapas",
    "CH": "Chihuahua", "DF": "Ciudad de México", "DG": "Durango",
    "GT": "Guanajuato", "GR": "Guerrero", "HG": "Hidalgo", "JC": "Jalisco",
    "MC": "Estado de México", "MN": "Michoacán", "MS": "Morelos",
    "NT": "Nayarit", "NL": "Nuevo León", "OC": "Oaxaca", "PL": "Puebla",
    "QT": "Querétaro", "QR": "Quintana Roo", "SP": "San Luis Potosí",
    "SL": "Sinaloa", "SR": "Sonora", "TC": "Tabasco", "TS": "Tamaulipas",
    "TL": "Tlaxcala", "VZ": "Veracruz", "YN": "Yucatán", "ZS": "Zacatecas",
    "NE": "Nacido en el Extranjero",
}

PALABRAS_INCONVENIENTES = {
    # RENAPO sustituye estas iniciales por "X" para evitar palabras altisonantes/inconvenientes
    "BACA", "BAKA", "BUEI", "BUEY", "CACA", "CACO", "CAGA", "CAGO", "CAKA",
    "CAKO", "COGE", "COGI", "COJA", "COJE", "COJI", "COJO", "COLA", "CULO",
    "FALO", "FETO", "GETA", "GUEI", "GUEY", "JETA", "JOTO", "KACA", "KACO",
    "KAGA", "KAGO", "KAKA", "KAKO", "KOGE", "KOGI", "KOJA", "KOJE", "KOJI",
    "KOJO", "KOLA", "KULO", "LILO", "LOCA", "LOCO", "LOKA", "LOKO", "MAME",
    "MAMO", "MEAR", "MEAS", "MEON", "MIAR", "MION", "MOCO", "MOKO", "MULA",
    "MULO", "NACA", "NACO", "PEDA", "PEDO", "PENE", "PIPI", "PITO", "POPO",
    "PUTA", "PUTO", "QULO", "RATA", "ROBA", "ROBE", "ROBO", "RUIN", "SENO",
    "TETA", "VACA", "VAGA", "VAGO", "VAKA", "VUEI", "VUEY", "WUEI", "WUEY",
}


def calcular_digito_verificador(curp17: str) -> int:
    """
    Calcula el último dígito verificador siguiendo el algoritmo RENAPO:
    1. Asignar valor por carácter (0='0', 9='9', A=10, B=11, ..., Ñ=24, ..., Z=36)
    2. Multiplicar cada valor por (18 - posición)
    3. Sumar todos
    4. Mod 10
    5. (10 - resultado) mod 10 = dígito verificador
    """
    valores = "0123456789ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    suma = 0
    for i, ch in enumerate(curp17):
        if ch in valores:
            v = valores.index(ch)
        else:
            return -1  # carácter inválido
        suma += v * (18 - i)
    return (10 - (suma % 10)) % 10


def validar_estructura(curp: str):
    curp = curp.strip().upper()
    if not curp:
        return {"valido": False, "razon": "CURP vacía"}
    if len(curp) != 18:
        return {"valido": False, "razon": f"longitud incorrecta: {len(curp)} (debe ser 18)"}

    m = RE_CURP.match(curp)
    if not m:
        return {"valido": False, "razon": "estructura no_match contra patrón RENAPO"}

    iniciales, aa, mm, dd, sexo, entidad, consonantes, homonimia, digito = m.groups()

    # validar fecha
    try:
        mm_i, dd_i = int(mm), int(dd)
        if not (1 <= mm_i <= 12) or not (1 <= dd_i <= 31):
            return {"valido": False, "razon": "fecha inválida"}
    except ValueError:
        return {"valido": False, "razon": "fecha no numérica"}

    # validar entidad
    entidad_nombre = ENTIDADES_VALIDAS.get(entidad)
    if entidad_nombre is None:
        return {"valido": False, "razon": f"código entidad inválido: {entidad}"}

    # advertir si iniciales son palabra inconveniente sin X sustituida (RENAPO debería haber puesto X)
    iniciales_warning = None
    if iniciales in PALABRAS_INCONVENIENTES:
        iniciales_warning = f"iniciales '{iniciales}' son palabra inconveniente; RENAPO normalmente sustituye 2ª letra por X"

    # validar dígito verificador
    curp17 = curp[:17]
    digito_calculado = calcular_digito_verificador(curp17)
    digito_real = int(digito)
    digito_ok = digito_calculado == digito_real

    return {
        "valido": digito_ok,
        "iniciales": iniciales,
        "iniciales_warning": iniciales_warning,
        "fecha_nacimiento": f"19{aa}-{mm}-{dd}" if int(aa) > 25 else f"20{aa}-{mm}-{dd}",
        "sexo": "Hombre" if sexo == "H" else "Mujer",
        "entidad_codigo": entidad,
        "entidad_nombre": entidad_nombre,
        "homonimia": homonimia,
        "digito_verificador_provisto": digito_real,
        "digito_verificador_calculado": digito_calculado,
        "digito_verificador_ok": digito_ok,
        "razon_invalida": None if digito_ok else f"dígito verificador esperado {digito_calculado}, llegó {digito_real}",
    }


def main():
    ap = argparse.ArgumentParser(description="Valida CURP mexicana (estructura + dígito verificador)")
    ap.add_argument("curp", nargs="?", help="CURP a validar")
    ap.add_argument("--stdin", action="store_true", help="Lee CURP de stdin")
    args = ap.parse_args()

    if args.stdin:
        curp = sys.stdin.read().strip()
    elif args.curp:
        curp = args.curp
    else:
        ap.error("CURP requerida (positional o --stdin)")

    resultado = {"curp_input": curp, "validacion": validar_estructura(curp)}
    resultado["nota_oficial"] = (
        "Validación local del algoritmo RENAPO. Para confirmar existencia real, "
        "consulta https://www.gob.mx/curp/ (no hay API pública abierta)."
    )
    print(json.dumps(resultado, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
