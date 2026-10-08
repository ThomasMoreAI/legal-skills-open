#!/usr/bin/env python3
"""
juris.py — cliente de linha de comando para a jurisprudencia do TJRO (sistema JURIS).

Usa o endpoint REAL de busca (Elasticsearch por tras de DRF):
    POST https://juris-back.tjro.jus.br/search/varios_parametros/

NAO usa GET /search/documentos/ : naquele endpoint os parametros de busca sao
IGNORADOS pelo servidor (retorna o corpus inteiro). Ver SKILL.md.

Sem dependencias externas (apenas stdlib).

Modos:
    buscar   <termo> [filtros]   busca documentos; saida compacta
    processo <nr_processo>        todos os documentos de um processo (CNJ)
    texto    <id>                 texto limpo COMPLETO de um documento
    facetas  [termo]             agregacoes (classes, orgaos, relatores, tipos)

Rode `python juris.py -h` ou `python juris.py <modo> -h` para detalhes.
"""

import argparse
import html as htmllib
import json
import re
import sys
import urllib.request
import urllib.parse

BASE = "https://juris-back.tjro.jus.br"
PORTAL = "https://juris.tjro.jus.br"
UA = "Mozilla/5.0 (juris-tjro skill)"

TIPOS_VALIDOS = [
    "ACÓRDÃO",
    "DECISÃO",
    "DECISÃO DA PRESIDÊNCIA",
    "SENTENÇA",
    "VOTO",
    "EMENTA",
    "RELATÓRIO",
]


# ----------------------------------------------------------------------------
# HTTP
# ----------------------------------------------------------------------------
def _post(path, body, timeout=60):
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(  # noqa: S310
        BASE + path,
        data=data,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": UA,
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as r:  # noqa: S310
        return json.loads(r.read().decode("utf-8"))


def _get(path, params=None, timeout=60):
    url = BASE + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": UA})  # noqa: S310
    with urllib.request.urlopen(req, timeout=timeout) as r:  # noqa: S310
        return json.loads(r.read().decode("utf-8"))


def buscar_raw(fields, size=20, frm=0, sort=None):
    """Chamada bruta ao endpoint de busca. `sort` None => relevancia."""
    body = {"from": frm, "size": size, "fields": fields, "sort": sort or [], "token": ""}
    d = _post("/search/varios_parametros/", body)
    return d


# ----------------------------------------------------------------------------
# Utilidades
# ----------------------------------------------------------------------------
def clean_html(h):
    """Remove imagens base64, estilos e tags; devolve texto corrido."""
    if not h:
        return ""
    h = re.sub(r"<img[^>]*>", " ", h, flags=re.I)
    h = re.sub(r"<style[\s\S]*?</style[^>]*>", " ", h, flags=re.I)
    h = re.sub(r"<script[\s\S]*?</script[^>]*>", " ", h, flags=re.I)
    h = re.sub(r"<[^>]+>", " ", h)
    h = htmllib.unescape(h)
    h = re.sub(r"\s+", " ", h).strip()
    return h


def cnj(n):
    """Formata 20 digitos -> NNNNNNN-DD.AAAA.J.TR.OOOO."""
    d = re.sub(r"\D", "", n or "")
    if len(d) == 20:
        return f"{d[0:7]}-{d[7:9]}.{d[9:13]}.{d[13:14]}.{d[14:16]}.{d[16:20]}"
    return n


def so_digitos(n):
    return re.sub(r"\D", "", n or "")


def portal_url(src):
    p = {
        "id": src.get("id_processo_documento"),
        "sistema_origem": src.get("sistema_origem"),
        "tipo": src.get("tipo"),
        "id_documento_principal": src.get("id_documento_principal"),
    }
    p = {k: v for k, v in p.items() if v not in (None, "")}
    return f"{PORTAL}/jurisprudencia/?{urllib.parse.urlencode(p)}"


def relator(src):
    return (
        src.get("nome_relator_acordao")
        or src.get("nome_relator_processo")
        or src.get("ds_nome")
        or "—"
    )


def orgao(src):
    return src.get("ds_orgao_julgador_colegiado") or src.get("ds_orgao_julgador") or "—"


def trecho_em_torno(txt, termo, raio=200):
    if not txt:
        return ""
    pos = -1
    if termo:
        m = re.search(re.escape(termo), txt, re.I)
        if m:
            pos = m.start()
    if pos < 0:
        return txt[: raio * 2].strip()
    ini = max(0, pos - raio)
    fim = min(len(txt), pos + len(termo) + raio)
    return ("..." if ini > 0 else "") + txt[ini:fim].strip() + ("..." if fim < len(txt) else "")


def _data_iso(s):
    """Aceita DD/MM/AAAA ou AAAA-MM-DD -> AAAA-MM-DD (string comparavel)."""
    s = (s or "").strip()
    m = re.match(r"(\d{2})/(\d{2})/(\d{4})", s)
    if m:
        return f"{m.group(3)}-{m.group(2)}-{m.group(1)}"
    return s  # assume ja AAAA-MM-DD


# ----------------------------------------------------------------------------
# Modo: buscar
# ----------------------------------------------------------------------------
def montar_fields(args):
    fields = {}
    if args.termo:
        fields["ds_modelo_documento"] = args.termo
    if args.tipo:
        # tipo TEM que ser array (string crua -> erro 500 no servidor)
        fields["tipo"] = list(args.tipo)
    if args.classe:
        fields["ds_classe_judicial"] = args.classe
    if args.orgao:
        fields["ds_orgao_julgador"] = args.orgao
    if args.relator:
        fields["nome_relator_acordao"] = args.relator
    if getattr(args, "processo", None):
        fields["nr_processo"] = so_digitos(args.processo)
    return fields


def cmd_buscar(args):
    fields = montar_fields(args)
    if not fields:
        print("Informe ao menos um criterio (termo ou filtro).", file=sys.stderr)
        return 2

    sort = [{"dtjulgamento": "desc"}] if args.recentes else []

    # Se ha pos-filtros client-side (--contendo, --de, --ate), buscamos um pool maior.
    pos_filtro = bool(args.contendo or args.de or args.ate)
    pool = max(args.tamanho * 6, 120) if pos_filtro else args.tamanho
    pool = min(pool, 400)

    d = buscar_raw(fields, size=pool, sort=sort)
    total = d.get("hits", {}).get("total", {}).get("value", 0)
    hits = d.get("hits", {}).get("hits", [])

    de = _data_iso(args.de) if args.de else None
    ate = _data_iso(args.ate) if args.ate else None
    contendo = [c.lower() for c in (args.contendo or [])]

    resultados = []
    vistos = set()
    for h in hits:
        src = h.get("_source", {})
        nr = src.get("nr_processo", "")
        if not args.repetidos and nr in vistos:
            continue
        txt = clean_html(src.get("ds_modelo_documento", ""))
        # filtro AND client-side (a busca textual do servidor e OR)
        if contendo and not all(c in txt.lower() for c in contendo):
            continue
        dj = src.get("dtjulgamento") or ""
        if de and dj and dj < de:
            continue
        if ate and dj and dj > ate:
            continue
        vistos.add(nr)
        resultados.append((src, txt))
        if len(resultados) >= args.tamanho:
            break

    if args.json:
        out = []
        for src, txt in resultados:
            out.append(
                {
                    "nr_processo": cnj(src.get("nr_processo", "")),
                    "tipo": src.get("tipo"),
                    "data_julgamento": src.get("dtjulgamento_str"),
                    "classe": src.get("ds_classe_judicial"),
                    "orgao": orgao(src),
                    "relator": relator(src),
                    "id_documento": src.get("id_processo_documento"),
                    "sistema_origem": src.get("sistema_origem"),
                    "url": portal_url(src),
                    "trecho": trecho_em_torno(txt, args.trecho_perto or args.termo, 200),
                }
            )
        print(
            json.dumps(
                {"total_no_acervo": total, "retornados": len(out), "resultados": out},
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0

    # saida texto
    cab = f"{total} documento(s) no acervo para o criterio"
    if pos_filtro:
        cab += f" | exibindo {len(resultados)} apos filtro client-side (pool de {len(hits)})"
    else:
        cab += f" | exibindo {len(resultados)}"
    print(cab)
    print("=" * 92)
    for i, (src, txt) in enumerate(resultados, 1):
        print(
            f"\n[{i}] {cnj(src.get('nr_processo', ''))} | {src.get('tipo')} | "
            f"{src.get('dtjulgamento_str')} | {src.get('ds_classe_judicial')}"
        )
        print(f"    relator/magistrado: {relator(src)}")
        print(f"    orgao: {orgao(src)}")
        tr = trecho_em_torno(txt, args.trecho_perto or args.termo, 180)
        if tr:
            print(f"    trecho: {tr}")
        print(f"    {portal_url(src)}")
    if not resultados:
        print("\n(nenhum resultado apos os filtros)")
    return 0


# ----------------------------------------------------------------------------
# Modo: processo
# ----------------------------------------------------------------------------
def cmd_processo(args):
    nr = so_digitos(args.numero)
    d = buscar_raw({"nr_processo": nr}, size=100, sort=[{"dtjulgamento": "desc"}])
    hits = d.get("hits", {}).get("hits", [])
    total = d.get("hits", {}).get("total", {}).get("value", 0)
    if args.json:
        out = [
            {
                "tipo": h["_source"].get("tipo"),
                "data_julgamento": h["_source"].get("dtjulgamento_str"),
                "classe": h["_source"].get("ds_classe_judicial"),
                "orgao": orgao(h["_source"]),
                "relator": relator(h["_source"]),
                "id_documento": h["_source"].get("id_processo_documento"),
                "sistema_origem": h["_source"].get("sistema_origem"),
                "url": portal_url(h["_source"]),
            }
            for h in hits
        ]
        print(
            json.dumps(
                {"processo": cnj(nr), "documentos": len(out), "itens": out},
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0
    print(f"Processo {cnj(nr)} — {total} documento(s)")
    print("=" * 92)
    for h in hits:
        src = h["_source"]
        print(
            f"\n  {src.get('tipo')} | {src.get('dtjulgamento_str')} | {src.get('ds_classe_judicial')}"
        )
        print(f"    relator/magistrado: {relator(src)}  | orgao: {orgao(src)}")
        print(f"    id={src.get('id_processo_documento')}  {portal_url(src)}")
    return 0


# ----------------------------------------------------------------------------
# Modo: texto (integra limpa de UM documento)
# ----------------------------------------------------------------------------
def cmd_texto(args):
    d = buscar_raw({"id_processo_documento": int(args.id)}, size=1)
    hits = d.get("hits", {}).get("hits", [])
    if not hits:
        print(f"Documento id={args.id} nao encontrado.", file=sys.stderr)
        return 1
    src = hits[0]["_source"]
    txt = clean_html(src.get("ds_modelo_documento", ""))
    if args.max and args.max > 0:
        txt = txt[: args.max]
    print(f"# {src.get('tipo')} — Processo {cnj(src.get('nr_processo', ''))}")
    print(
        f"# {src.get('ds_classe_judicial')} | {src.get('dtjulgamento_str')} | "
        f"{orgao(src)} | relator: {relator(src)}"
    )
    print(f"# {portal_url(src)}")
    print()
    print(txt)
    return 0


# ----------------------------------------------------------------------------
# Modo: facetas (agregacoes)
# ----------------------------------------------------------------------------
def cmd_facetas(args):
    params = {"paginaAtual": 1, "quantidadePorPagina": 1}
    if args.termo:
        # o endpoint de agregacoes aceita os mesmos params; texto livre via 'texto'
        params["texto"] = args.termo
    d = _get("/search/agregacoes", params)
    aggs = d.get("aggregations", {})
    if args.json:
        print(json.dumps(aggs, ensure_ascii=False, indent=2))
        return 0
    rotulos = {
        "tipos_documentos": "Tipos de documento",
        "classes_judiciais": "Classes judiciais",
        "orgaos_julgadores": "Orgaos julgadores",
        "orgaos_julgadores_colegiados": "Orgaos colegiados",
        "juizes": "Magistrados / relatores",
    }
    for key, titulo in rotulos.items():
        buckets = aggs.get(key, {}).get("buckets", [])
        if not buckets:
            continue
        print(f"\n## {titulo}")
        for b in buckets[: args.limite]:
            print(f"  {b.get('doc_count'):>9}  {b.get('key')}")
    return 0


# ----------------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------------
def build_parser():
    p = argparse.ArgumentParser(description="Consulta a jurisprudencia do TJRO (sistema JURIS).")
    sub = p.add_subparsers(dest="modo", required=True)

    b = sub.add_parser("buscar", help="busca documentos por texto e/ou filtros")
    b.add_argument(
        "termo",
        nargs="?",
        default="",
        help="texto livre (busca no inteiro teor). DICA: a busca do "
        "servidor e OR (mais palavras = MAIS resultados); para "
        "precisao use o termo mais distintivo aqui e --contendo "
        "para as demais palavras obrigatorias.",
    )
    b.add_argument(
        "--tipo",
        nargs="+",
        choices=TIPOS_VALIDOS,
        metavar="TIPO",
        help="um ou mais tipos: " + ", ".join(TIPOS_VALIDOS),
    )
    b.add_argument("--classe", help="match na classe judicial (ex: 'APELAÇÃO CÍVEL')")
    b.add_argument("--orgao", help="match no orgao julgador")
    b.add_argument("--relator", help="match no nome do relator do acordao")
    b.add_argument(
        "--contendo",
        nargs="+",
        metavar="PALAVRA",
        help="filtro AND client-side: so resultados cujo inteiro teor "
        "contenha TODAS estas palavras",
    )
    b.add_argument("--de", help="data inicial (DD/MM/AAAA) — filtro client-side")
    b.add_argument("--ate", help="data final (DD/MM/AAAA) — filtro client-side")
    b.add_argument(
        "--recentes",
        action="store_true",
        help="ordena por data de julgamento decrescente (padrao: relevancia)",
    )
    b.add_argument("--tamanho", type=int, default=20, help="numero de resultados (padrao 20)")
    b.add_argument("--repetidos", action="store_true", help="nao deduplicar por numero de processo")
    b.add_argument(
        "--trecho-perto",
        metavar="TERMO",
        help="extrai o trecho ao redor deste termo (padrao: o termo de busca)",
    )
    b.add_argument("--json", action="store_true", help="saida em JSON")
    b.set_defaults(func=cmd_buscar)

    pr = sub.add_parser("processo", help="lista os documentos de um processo (CNJ)")
    pr.add_argument("numero", help="numero do processo (com ou sem mascara CNJ)")
    pr.add_argument("--json", action="store_true")
    pr.set_defaults(func=cmd_processo)

    t = sub.add_parser("texto", help="texto limpo COMPLETO de um documento")
    t.add_argument("id", help="id_processo_documento (campo 'id_documento' dos resultados)")
    t.add_argument("--max", type=int, default=0, help="trunca em N caracteres (0 = sem limite)")
    t.set_defaults(func=cmd_texto)

    f = sub.add_parser("facetas", help="agregacoes (classes, orgaos, relatores, tipos)")
    f.add_argument("termo", nargs="?", default="")
    f.add_argument("--limite", type=int, default=15, help="itens por faceta (padrao 15)")
    f.add_argument("--json", action="store_true")
    f.set_defaults(func=cmd_facetas)

    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        return args.func(args)
    except urllib.error.HTTPError as e:
        body = ""
        try:
            body = e.read().decode("utf-8", "replace")[:300]
        except OSError:
            pass
        print(f"Erro HTTP {e.code} ao consultar a API. {body}", file=sys.stderr)
        return 1
    except urllib.error.URLError as e:
        print(f"Erro de rede: {e.reason}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
