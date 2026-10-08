# Diario — 2026-08-22: XSD en CI y ampliación de cobertura Akoma Ntoso (TAREA-089 y TAREA-090)

## Qué se ha hecho

- **TAREA-089**: vendorizados `akomantoso30.xsd` (OASIS LegalDocML 1.0) y
  `xml.xsd` en `11_calidad/xsd/`; nuevo script
  `11_calidad/validar_akoma_ntoso.py`; paso de validación en
  `.github/workflows/validar-corpus.yml`. Los 60 XML publicados pasan.
- **TAREA-090**, cinco líneas:
  1. Artículo 3 de las ocho normas ya cubiertas (RD 217/2022, Ley 6/2014,
     Decreto 30/2023, RD 243/2022, Decretos 211/2022 y 196/2022,
     RD 157/2022 y RD 659/2023).
  2. Artículos 1 y 2 de `NOR-009` (ROC; pertenecen al anexo, documentado)
     y `NOR-024` (atención a la diversidad).
  3. Soporte del generador para disposiciones adicionales/finales
     (`tipo:`, `ordinal:`, `hcontainer`) y apartados multipárrafo.
  4. Artículo 2 de la LOFP con las 24 definiciones (la definición 6 lleva
     su segundo párrafo sin numeración propia).
  5. Disposiciones breves de RD 217/2022 (6), RD 243/2022 (8) y
     RD 659/2023 (14).
- Total: de 17 a 60 porciones publicadas, todas conformes al XSD.
- README de pilotos, `interoperabilidad-juridica.md`, comprobaciones de
  `pages.yml`, inventario y catálogo actualizados.

## IDs consumidos

- TAREA-089, TAREA-090.

## Hallazgos y dudas

- La extracción confirmó lo ya registrado en `PREG-011`: la `url_oficial`
  de `NOR-018` apunta a un documento del BOC sin relación con la orden de
  IES descrita. No se generó ningún piloto para `NOR-018`.
- Referencias oficiales verificadas hoy: NOR-043 → BOC núm. 231/2022,
  NOR-047 → BOC núm. 212/2022, NOR-006 → BOE-A-2022-5521,
  NOR-080 → BOE-A-2023-16889, LOFP → BOE-A-2022-5139.
- Erratas detectadas en el texto oficial del RD 659/2023 (DA 19 sin la
  palabra «adicional») se transcriben literalmente.

## Validación

- `generar_interoperabilidad.py --check`: OK.
- `validar_akoma_ntoso.py`: 60/60 conformes.
- `validar_corpus.py`: 0 errores (3 avisos preexistentes de TEXTOS).
