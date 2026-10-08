# Fuentes oficiales (corpus primario)

Objetivo: que la auditoría sea **reproducible y contrastada contra la ley vigente, nada inventado**.
Toda afirmación legal de la skill debe poder rastrearse a uno de estos archivos + el artículo.
Si algo no se puede verificar contra estos textos, se marca `[verificar contra fuente oficial]`.

> Descargado: **2026-06-23** desde IMPO (Información Oficial — texto consolidado vigente). Los `.txt` se
> extrajeron del HTML oficial de IMPO (decodificado cp1252 → UTF-8). Re-descargables con los comandos de abajo.

| Archivo | Norma | Tipo | SHA-256 (trunc.) | Fuente oficial |
|---|---|---|---|---|
| `ley-18331.txt` | Ley N° 18.331 — Protección de Datos Personales y Acción de Habeas Data (2008) | texto consolidado | `0eb9c075…` | IMPO |
| `decreto-414-009.txt` | Decreto N° 414/009 — reglamentario de la Ley 18.331 | texto consolidado | `a5b85a3c…` | IMPO |
| `ley-19670.txt` | Ley N° 19.670 (Rendición de Cuentas 2017), **arts. 37–40** (datos personales) | texto consolidado | `6104cd55…` | IMPO |
| `decreto-64-020.txt` | Decreto N° 64/020 — reglamenta arts. 37–40 Ley 19.670 + art. 12 Ley 18.331 | texto consolidado | `0b52e82d…` | IMPO |
| `ley-19574.txt` | Ley N° 19.574 — Ley Integral contra el Lavado de Activos (2017) | texto consolidado | `61c2328c…` | IMPO |
| `decreto-379-018.txt` | Decreto N° 379/018 — reglamentario, sujetos obligados **no financieros** (PLA/FT) | texto consolidado | `72a81e90…` | IMPO |

## Notas de validez (IMPORTANTE)
- **La Ley 18.331 ya rige desde 2008**; la reglamenta el **Decreto 414/009**. La parte "moderna"
  (responsabilidad proactiva, brechas, DPIA, DPO, privacidad por diseño/defecto) entra por la **Ley 19.670
  arts. 37–40 (2018)** y su reglamento **Decreto 64/020 (2020)**. El art. 39 de la Ley 19.670 **da nueva
  redacción al art. 12 de la Ley 18.331** (principio de responsabilidad).
- **Uruguay tiene adecuación UE**: Decisión de Ejecución **2012/484/UE** (21-ago-2012, DO L 227/11). Permite
  transferencias UE→Uruguay sin salvaguardas adicionales. Además Uruguay ratificó el **Convenio 108** del
  Consejo de Europa (vigente desde 1-ago-2013) y su **Protocolo modernizador 108+** (ratificado 5-ago-2021).
  Estas dos referencias se citan por su fuente externa (EUR-Lex / Council of Europe), no se incluyen como `.txt`.
- **PLA/FT (Ley 19.574):** la **UIAF** del **BCU** recibe los reportes de operaciones sospechosas (ROS); la
  **SENACLAFT** supervisa a los sujetos obligados no financieros. Aplica solo a **sujetos obligados** (no a
  toda empresa) — ver `packs/ley-19574/pack.md`.

## Cómo re-descargar (reproducibilidad)
```bash
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"
# IMPO sirve el texto consolidado completo en la URL base de cada norma:
curl -fsSL -A "$UA" "https://www.impo.com.uy/bases/leyes/18331-2008"   -o ley-18331.html
curl -fsSL -A "$UA" "https://www.impo.com.uy/bases/decretos/414-2009"  -o decreto-414-009.html
curl -fsSL -A "$UA" "https://www.impo.com.uy/bases/leyes/19670-2018"   -o ley-19670.html
curl -fsSL -A "$UA" "https://www.impo.com.uy/bases/decretos/64-2020"   -o decreto-64-020.html
curl -fsSL -A "$UA" "https://www.impo.com.uy/bases/leyes/19574-2017"   -o ley-19574.html
curl -fsSL -A "$UA" "https://www.impo.com.uy/bases/decretos/379-2018"  -o decreto-379-018.html
# Extraer texto (IMPO viene en cp1252):
python3 -c "import re,html,sys;raw=open(sys.argv[1],'rb').read();t=raw.decode('cp1252');\
t=re.sub(r'(?is)<(script|style).*?</\1>',' ',t);t=re.sub(r'(?s)<[^>]+>',' ',t);t=html.unescape(t);\
open(sys.argv[2],'w').write(re.sub(r'[ \t]+',' ',t))" ley-18331.html ley-18331.txt
sha256sum *.txt
```

## Regla de uso para la skill
1. Antes de afirmar algo legal, búscalo en estos archivos.
2. Cita siempre **ley/decreto + artículo + archivo fuente**.
3. Si no está en el corpus o no es verificable, dilo: `[verificar contra fuente oficial / abogado]`.
4. Nunca uses un blog/fuente secundaria como base de una afirmación normativa en el output final.
