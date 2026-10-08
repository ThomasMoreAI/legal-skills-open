#!/usr/bin/env python3
"""Repara el doble encodeo UTF-8 -> latin-1 de las copias locales de texto oficial.

Los ficheros son mixtos: la cabecera que añade el proceso de exportación está bien
codificada y el cuerpo llegó doble-encodeado, así que revertir el fichero entero
falla. Se reparan solo los tramos que contienen `Ã` o `Â`, que son la firma del
daño, y cada tramo se acepta únicamente si decodifica limpio como UTF-8. El texto
sano no se toca.

Uso:
    python3 reparar_mojibake.py <directorio> [--aplicar]

Sin `--aplicar` solo informa.
"""
import pathlib
import re
import sys

# Tramos de caracteres latin-1 contiguos: es donde puede estar el daño.
TRAMO = re.compile("[-ÿ]+")


def reparar(texto: str) -> tuple[str, int]:
    arreglos = 0

    def sub(m: re.Match) -> str:
        nonlocal arreglos
        s = m.group(0)
        if "Ã" not in s and "Â" not in s:
            return s
        try:
            r = s.encode("latin-1").decode("utf-8")
        except (UnicodeEncodeError, UnicodeDecodeError):
            return s
        if r != s:
            arreglos += 1
        return r

    reparado = TRAMO.sub(sub, texto)

    # Resto: el espacio duro (U+00A0) doble-encodeado deja «Â» seguido del
    # espacio, y al normalizarse este a espacio normal la «Â» queda huérfana
    # fuera de cualquier tramo latin-1. No aparece nunca sola en texto legal.
    reparado, n = re.subn("Â(?=[  ])", "", reparado)
    arreglos += n

    # Indicadores ordinales: «nÂº» por «nº». La «Â» sobrante queda pegada a un
    # carácter ASCII, que corta el tramo latin-1 y la deja fuera del paso anterior.
    for malo, bueno in (("Âº", "º"), ("Âª", "ª")):
        reparado, n = re.subn(re.escape(malo), bueno, reparado)
        arreglos += n
    return reparado, arreglos


def main() -> int:
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    raiz = pathlib.Path(sys.argv[1])
    aplicar = "--aplicar" in sys.argv

    tocados = 0
    for fichero in sorted(raiz.glob("*.txt")):
        texto = fichero.read_text(encoding="utf-8")
        reparado, n = reparar(texto)
        if n == 0:
            continue
        restante = reparado.count("Ã") + reparado.count("Â")
        tocados += 1
        print(f"  {fichero.name}: {n} tramos, mojibake restante {restante}")
        if aplicar:
            fichero.write_text(reparado, encoding="utf-8")

    print(f"\n{tocados} ficheros con daño{' — reparados' if aplicar else ' (simulación)'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
