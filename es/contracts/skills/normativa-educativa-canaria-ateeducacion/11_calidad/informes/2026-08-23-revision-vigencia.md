# Informe de revisión de vigencia — 2026-08-23

TAREA: TAREA-097 · Método: `python3 11_calidad/reexportar_texto_oficial.py --auditar`
(contraste de cada copia local contra el sumario oficial del boletín que declara su
cabecera, según el procedimiento de DEC-0011).

## Resultado

- **68 fichas NOR contrastadas** contra fuente oficial.
- **Hallazgo inicial**: 2 fichas con título no literal respecto al boletín
  (`NOR-114`, coincidencia 44 %; `NOR-115`, 52 %). Los títulos habían sido
  registrados parafraseados al catalogar las órdenes del programa piloto.
- **Corrección**: ambos títulos sustituidos por la redacción literal oficial,
  extraída directamente de los anuncios del BOC (2023/064/007 y 2023/101/024),
  en ficha e índice. Los títulos literales completos también revelaron matices:
  la Orden de 24/03/2023 «autoriza la implantación… dando continuidad a la
  experiencia piloto iniciada» y no «desarrolla la implantación y ampliación».

## Estado tras la corrección

Re-ejecución del auditor: **68 fichas contrastadas · 0 a revisar**.

## Notas

- El auditor cubre las fichas NOR con copia local registrada; las normas sin
  copia local (p. ej., las fichas mínimas NOR-117 a NOR-124) se contrastan
  cuando se les exporte texto local.
- La comprobación contra boletines es manual y periódica (DEC-0011): esta
  revisión queda como punto de referencia y debe repetirse tras cada tanda de
  altas.
