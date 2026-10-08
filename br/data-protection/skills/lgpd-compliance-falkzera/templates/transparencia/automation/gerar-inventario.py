#!/usr/bin/env python3
"""
scripts/gerar-inventario.py
============================
Skill: lgpd-compliance (Parte 3)

Gera transparencia/inventario.yaml automaticamente a partir de:
  1. COMMENT ON COLUMN no Postgres (via introspecção SQL)
  2. Anotações @pii em código Python (decorator)
  3. JSDoc/comments em TS (regex)
  4. transparencia/terceiros.yaml e finalidades.yaml (validação cruzada)

Uso:
    python scripts/gerar-inventario.py                 # gera inventario.yaml
    python scripts/gerar-inventario.py --check         # falha se há drift
    python scripts/gerar-inventario.py --diff          # mostra diff
    python scripts/gerar-inventario.py --json          # emite JSON canônico em stdout

Dependências:
    pip install psycopg2-binary pyyaml typer rich
"""

from __future__ import annotations

import json
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

try:
    import psycopg2
    import yaml
    import typer
    from rich.console import Console
except ImportError as e:
    print(f"Dependência faltando: {e}. Rode: pip install psycopg2-binary pyyaml typer rich")
    sys.exit(1)


app = typer.Typer(add_completion=False, no_args_is_help=False)
console = Console()


# === Configuração ===========================================================

ROOT = Path(__file__).resolve().parent.parent
INVENTARIO_PATH = ROOT / "transparencia" / "inventario.yaml"
TERCEIROS_PATH = ROOT / "transparencia" / "terceiros.yaml"
FINALIDADES_PATH = ROOT / "transparencia" / "finalidades.yaml"

DB_URL = os.environ.get("DATABASE_URL", "postgresql://localhost/postgres")

# === Estruturas =============================================================

@dataclass
class Campo:
    tabela: str
    coluna: str
    tipo: str
    finalidade: list[str] = field(default_factory=list)
    base_legal: str = ""
    retencao: str = ""
    sensibilidade: str = ""
    compartilha_com: list[str] = field(default_factory=list)
    observacao: str | None = None
    no_pii: bool = False


# === 1. Extração via COMMENT ON COLUMN do Postgres =========================

def extrair_de_postgres() -> list[Campo]:
    """Conecta no banco e lê COMMENT ON COLUMN de cada tabela @contains_pii."""
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()

    cur.execute(
        """
        SELECT
            c.table_name,
            c.column_name,
            c.data_type,
            pgd.description
        FROM information_schema.columns c
        LEFT JOIN pg_catalog.pg_statio_all_tables st
            ON st.relname = c.table_name AND st.schemaname = c.table_schema
        LEFT JOIN pg_catalog.pg_description pgd
            ON pgd.objoid = st.relid
            AND pgd.objsubid = c.ordinal_position
        WHERE c.table_schema = 'public'
        ORDER BY c.table_name, c.ordinal_position;
        """
    )

    campos: list[Campo] = []
    for tabela, coluna, tipo, desc in cur.fetchall():
        if not desc:
            continue
        campo = _parse_comment(tabela, coluna, tipo, desc)
        if campo:
            campos.append(campo)

    cur.close()
    conn.close()
    return campos


def _parse_comment(tabela: str, coluna: str, tipo: str, comment: str) -> Campo | None:
    """Faz parse de '@pii @finalidade=X,Y @base=Z @retencao=W ...'"""
    if "@no_pii" in comment:
        return Campo(tabela=tabela, coluna=coluna, tipo=tipo, no_pii=True)

    if "@pii" not in comment:
        return None

    campo = Campo(tabela=tabela, coluna=coluna, tipo=tipo)

    for match in re.finditer(r"@(\w+)=([^\s@]+)", comment):
        chave, valor = match.group(1), match.group(2)
        if chave == "finalidade":
            campo.finalidade = valor.split(",")
        elif chave == "base":
            campo.base_legal = valor
        elif chave == "retencao":
            campo.retencao = valor
        elif chave == "sensibilidade":
            campo.sensibilidade = valor
        elif chave == "compartilha":
            campo.compartilha_com = valor.split(",")
        elif chave == "observacao":
            campo.observacao = valor

    return campo


# === 2. Extração de código Python (decorators @pii) ========================

def extrair_de_codigo_python(diretorio: Path) -> list[Campo]:
    """
    TODO: Implementar parser via AST que detecta @pii em decorators e
    Annotated[..., PII(...)] em type hints. Por ora, esqueleto.
    """
    campos: list[Campo] = []
    # Esqueleto: percorrer .py, ast.parse, achar decorators @pii(...)
    return campos


# === 3. Extração de TS (regex em JSDoc) ====================================

PII_TS_REGEX = re.compile(
    r"@pii\(([^)]+)\)\s*\n?\s*\w+\s+(\w+)",
    re.MULTILINE,
)


def extrair_de_codigo_ts(diretorio: Path) -> list[Campo]:
    campos: list[Campo] = []
    for arquivo in diretorio.rglob("*.ts"):
        if "node_modules" in str(arquivo):
            continue
        conteudo = arquivo.read_text(encoding="utf-8", errors="ignore")
        for match in PII_TS_REGEX.finditer(conteudo):
            atribs_str, nome_campo = match.group(1), match.group(2)
            campo = Campo(
                tabela=arquivo.stem,
                coluna=nome_campo,
                tipo="unknown",
            )
            for sub in re.finditer(r"(\w+)=(\[[^\]]+\]|[\w_]+)", atribs_str):
                chave, valor = sub.group(1), sub.group(2)
                if valor.startswith("["):
                    valor_list = [v.strip() for v in valor.strip("[]").split(",")]
                else:
                    valor_list = [valor]
                _aplicar(campo, chave, valor_list, valor)
            campos.append(campo)
    return campos


def _aplicar(campo: Campo, chave: str, valor_list: list[str], valor_raw: str) -> None:
    if chave == "finalidade":
        campo.finalidade = valor_list
    elif chave == "base":
        campo.base_legal = valor_raw
    elif chave == "retencao":
        campo.retencao = valor_raw
    elif chave == "sensibilidade":
        campo.sensibilidade = valor_raw
    elif chave == "compartilha":
        campo.compartilha_com = valor_list


# === Validação cruzada =====================================================

def carregar_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        console.print(f"[red]Arquivo não encontrado:[/red] {path}")
        sys.exit(1)
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def validar(campos: list[Campo]) -> list[str]:
    """Retorna lista de erros encontrados."""
    erros: list[str] = []

    terceiros = carregar_yaml(TERCEIROS_PATH)
    finalidades = carregar_yaml(FINALIDADES_PATH)

    terceiros_ids = {t["id"] for t in terceiros.get("processadores", [])}
    finalidades_ids = {f["id"] for f in finalidades.get("finalidades", [])}

    for c in campos:
        if c.no_pii:
            continue
        if not c.finalidade:
            erros.append(f"{c.tabela}.{c.coluna}: @finalidade faltando")
        for f in c.finalidade:
            if f not in finalidades_ids:
                erros.append(
                    f"{c.tabela}.{c.coluna}: finalidade '{f}' não está em "
                    f"transparencia/finalidades.yaml"
                )
        if not c.base_legal:
            erros.append(f"{c.tabela}.{c.coluna}: @base faltando")
        if not c.sensibilidade:
            erros.append(f"{c.tabela}.{c.coluna}: @sensibilidade faltando")
        for t in c.compartilha_com:
            if t not in terceiros_ids:
                erros.append(
                    f"{c.tabela}.{c.coluna}: compartilha com '{t}' não está em "
                    f"transparencia/terceiros.yaml"
                )

    return erros


# === Serialização =========================================================

def montar_inventario(campos: list[Campo]) -> dict[str, Any]:
    """Agrupa campos por categoria (heurística por nome) e monta estrutura."""
    inventario = carregar_yaml(INVENTARIO_PATH) if INVENTARIO_PATH.exists() else {}
    # Mantém meta + categorias existentes; substitui só os itens.
    # Implementação completa exige merge cuidadoso.
    # Por simplicidade aqui, geramos uma seção 'gerado_automaticamente':
    inventario.setdefault("meta", {})
    inventario["gerado_automaticamente"] = [
        {
            "tabela": c.tabela,
            "coluna": c.coluna,
            "finalidade": c.finalidade,
            "base_legal_lgpd": c.base_legal,
            "retencao": c.retencao,
            "sensibilidade": c.sensibilidade,
            "compartilhado_com": c.compartilha_com,
        }
        for c in campos
        if not c.no_pii
    ]
    return inventario


# === CLI ===================================================================

@app.command()
def gerar(
    check: bool = typer.Option(False, "--check", help="Falha se houver drift (uso em CI)"),
    diff: bool = typer.Option(False, "--diff", help="Mostra diff vs inventário atual"),
    json_out: bool = typer.Option(False, "--json", help="Emite JSON canônico em stdout"),
) -> None:
    console.print("[bold]Extraindo anotações PII...[/bold]")

    campos: list[Campo] = []
    campos.extend(extrair_de_postgres())
    campos.extend(extrair_de_codigo_ts(ROOT / "app"))
    # campos.extend(extrair_de_codigo_python(ROOT / "app"))

    console.print(f"  {len(campos)} campos identificados.")

    erros = validar(campos)
    if erros:
        console.print("[red bold]Erros de validação:[/red bold]")
        for e in erros:
            console.print(f"  ✗ {e}")
        if check:
            sys.exit(1)

    inventario = montar_inventario(campos)

    if json_out:
        print(json.dumps(inventario, indent=2, ensure_ascii=False))
        return

    if check:
        # Compara com arquivo atual
        atual = carregar_yaml(INVENTARIO_PATH)
        if atual.get("gerado_automaticamente") != inventario.get("gerado_automaticamente"):
            console.print(
                "[red bold]DRIFT detectado:[/red bold] inventario.yaml não reflete o código."
            )
            console.print("Rode `python scripts/gerar-inventario.py` e commite as mudanças.")
            sys.exit(1)
        console.print("[green]Inventário em dia.[/green]")
        return

    INVENTARIO_PATH.write_text(
        yaml.safe_dump(inventario, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )
    console.print(f"[green]Gerado:[/green] {INVENTARIO_PATH}")


if __name__ == "__main__":
    app()
