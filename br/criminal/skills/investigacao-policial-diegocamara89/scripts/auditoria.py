#!/usr/bin/env python3
"""
auditoria.py - Trilha de auditoria forense com hashes encadeados

Gera e mantem um log append-only onde cada registro inclui o hash SHA256
do registro anterior, formando uma cadeia verificavel (tamper-evident).
Atende aos requisitos da Lei 13.964/2019 (arts. 158-A a 158-F do CPP):
verificavel, auditavel e replicavel.

Uso:
    # Registrar acao de agente
    python auditoria.py --log caso_001.log --acao "Extracao de dados" \
        --agente "extrator_bancario_01" --entrada dados.pdf --saida resultado.json

    # Verificar integridade do log
    python auditoria.py --log caso_001.log --verificar

    # Exibir resumo do log
    python auditoria.py --log caso_001.log --resumo
"""

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path


def _resolver_caminho(filepath, log_path=None):
    """Normaliza e tenta resolver um caminho de arquivo.

    Tenta, em ordem:
    1. Caminho como fornecido (absoluto ou relativo ao cwd)
    2. Relativo ao diretorio do log (se log_path fornecido)
    3. Normalizacao de separadores Windows/Unix

    Retorna (path_resolvido, motivo_falha_ou_None).
    """
    if not filepath:
        return None, "caminho vazio"

    # Normalizar separadores
    normalizado = str(Path(filepath))

    # Tentativa 1: caminho como fornecido (ja normalizado)
    if os.path.exists(normalizado):
        return normalizado, None

    # Tentativa 2: relativo ao cwd
    cwd_path = os.path.join(os.getcwd(), normalizado)
    if os.path.exists(cwd_path):
        return cwd_path, None

    # Tentativa 3: relativo ao diretorio do log
    if log_path:
        log_dir = os.path.dirname(os.path.abspath(log_path))
        log_rel = os.path.join(log_dir, normalizado)
        if os.path.exists(log_rel):
            return log_rel, None

    return None, f"arquivo nao encontrado: '{filepath}' (tentado como absoluto, relativo ao cwd e relativo ao log)"


def calcular_hash_arquivo(filepath):
    """Calcula SHA256 de um arquivo."""
    if not filepath or not os.path.exists(filepath):
        return None
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for bloco in iter(lambda: f.read(8192), b""):
            sha256.update(bloco)
    return sha256.hexdigest()


def calcular_hash_texto(texto):
    """Calcula SHA256 de uma string."""
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


def obter_ultimo_hash(log_path):
    """Le o ultimo registro do log e retorna seu hash.

    Retorna '0' * 64 se o log nao existe ou esta vazio (genesis block).
    """
    if not os.path.exists(log_path) or os.path.getsize(log_path) == 0:
        return "0" * 64

    ultimo_registro = None
    with open(log_path, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if linha:
                ultimo_registro = linha

    if not ultimo_registro:
        return "0" * 64

    return calcular_hash_texto(ultimo_registro)


def registrar(log_path, acao, agente, entrada=None, saida=None, modelo=None,
              documentos=None):
    """Adiciona um registro ao log com hash encadeado."""
    hash_anterior = obter_ultimo_hash(log_path)

    registro = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "acao": acao,
        "agente": agente,
        "hash_anterior": hash_anterior,
    }

    if modelo:
        registro["modelo"] = modelo

    if entrada:
        path_resolvido, motivo = _resolver_caminho(entrada, log_path)
        if path_resolvido:
            registro["entrada"] = path_resolvido
            registro["hash_entrada"] = calcular_hash_arquivo(path_resolvido)
        else:
            registro["entrada"] = entrada
            registro["hash_entrada"] = calcular_hash_texto(entrada)
            registro["entrada_aviso"] = motivo

    if saida:
        path_resolvido, motivo = _resolver_caminho(saida, log_path)
        if path_resolvido:
            registro["saida"] = path_resolvido
            registro["hash_saida"] = calcular_hash_arquivo(path_resolvido)
        else:
            registro["saida"] = saida
            registro["hash_saida"] = calcular_hash_texto(saida)
            registro["saida_aviso"] = motivo

    if documentos:
        docs = []
        for doc in documentos.split(","):
            doc = doc.strip()
            path_resolvido, motivo = _resolver_caminho(doc, log_path)
            if path_resolvido:
                h = calcular_hash_arquivo(path_resolvido)
                docs.append({"arquivo": path_resolvido, "hash": h})
            else:
                docs.append({"arquivo": doc, "hash": "arquivo_nao_encontrado",
                             "aviso": motivo})
        registro["documentos"] = docs

    linha_json = json.dumps(registro, ensure_ascii=False, separators=(",", ":"))

    with open(log_path, "a", encoding="utf-8") as f:
        f.write(linha_json + "\n")

    hash_registro = calcular_hash_texto(linha_json)
    return {"status": "OK", "registro": registro, "hash_registro": hash_registro}


def verificar_integridade(log_path):
    """Verifica a cadeia de hashes do log.

    Cada registro deve ter hash_anterior == SHA256 do registro anterior.
    Se algum registro foi alterado ou removido, a cadeia quebra.
    """
    if not os.path.exists(log_path):
        return {"status": "ERRO", "erro": f"Log nao encontrado: {log_path}"}

    with open(log_path, "r", encoding="utf-8") as f:
        linhas = [l.strip() for l in f if l.strip()]

    if not linhas:
        return {"status": "OK", "registros": 0, "mensagem": "Log vazio"}

    hash_esperado = "0" * 64
    erros = []

    for i, linha in enumerate(linhas):
        try:
            reg = json.loads(linha)
        except json.JSONDecodeError:
            erros.append({
                "registro": i + 1,
                "erro": "JSON invalido",
                "linha": linha[:100],
            })
            continue

        hash_anterior = reg.get("hash_anterior", "")
        if hash_anterior != hash_esperado:
            erros.append({
                "registro": i + 1,
                "erro": "Hash encadeado nao confere",
                "esperado": hash_esperado,
                "encontrado": hash_anterior,
                "acao": reg.get("acao", "?"),
            })

        hash_esperado = calcular_hash_texto(linha)

    if erros:
        return {
            "status": "COMPROMETIDO",
            "registros": len(linhas),
            "erros": erros,
            "mensagem": f"Cadeia de hashes quebrada em {len(erros)} ponto(s). "
                        "O log pode ter sido adulterado.",
        }

    return {
        "status": "INTEGRO",
        "registros": len(linhas),
        "hash_final": hash_esperado,
        "mensagem": "Cadeia de hashes verificada com sucesso. Nenhuma adulteracao detectada.",
    }


def resumo(log_path):
    """Exibe resumo do log: total de registros, agentes, periodo."""
    if not os.path.exists(log_path):
        return {"status": "ERRO", "erro": f"Log nao encontrado: {log_path}"}

    with open(log_path, "r", encoding="utf-8") as f:
        linhas = [l.strip() for l in f if l.strip()]

    if not linhas:
        return {"status": "OK", "registros": 0}

    agentes = set()
    acoes = []
    primeiro_ts = None
    ultimo_ts = None

    for linha in linhas:
        try:
            reg = json.loads(linha)
            agentes.add(reg.get("agente", "?"))
            acoes.append(reg.get("acao", "?"))
            ts = reg.get("timestamp")
            if ts:
                if not primeiro_ts:
                    primeiro_ts = ts
                ultimo_ts = ts
        except json.JSONDecodeError:
            continue

    return {
        "status": "OK",
        "registros": len(linhas),
        "agentes": sorted(agentes),
        "periodo": {"inicio": primeiro_ts, "fim": ultimo_ts},
        "acoes": acoes,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Trilha de auditoria forense com hashes encadeados"
    )
    parser.add_argument("--log", required=True, help="Caminho do arquivo de log")

    grupo = parser.add_mutually_exclusive_group(required=True)
    grupo.add_argument("--verificar", action="store_true",
                       help="Verificar integridade do log")
    grupo.add_argument("--resumo", action="store_true",
                       help="Exibir resumo do log")
    grupo.add_argument("--acao", help="Descricao da acao a registrar")

    parser.add_argument("--agente", help="ID do agente (ex: extrator_bancario_01)")
    parser.add_argument("--entrada", help="Arquivo ou dado de entrada")
    parser.add_argument("--saida", help="Arquivo ou dado de saida")
    parser.add_argument("--modelo", help="ID do modelo IA usado")
    parser.add_argument("--documentos",
                        help="Lista de documentos processados (separados por virgula)")
    parser.add_argument(
        "--formato", default="json", choices=["json", "texto"],
        help="Formato de saida"
    )

    args = parser.parse_args()

    if args.verificar:
        resultado = verificar_integridade(args.log)
    elif args.resumo:
        resultado = resumo(args.log)
    else:
        if not args.agente:
            parser.error("--agente e obrigatorio ao registrar uma acao")
        resultado = registrar(
            args.log, args.acao, args.agente,
            entrada=args.entrada, saida=args.saida,
            modelo=args.modelo, documentos=args.documentos,
        )

    if args.formato == "json":
        print(json.dumps(resultado, ensure_ascii=False, indent=2))
    else:
        if resultado.get("status") == "INTEGRO":
            print(f"OK: {resultado['registros']} registros, cadeia integra.")
        elif resultado.get("status") == "COMPROMETIDO":
            print(f"ALERTA: Cadeia comprometida em {len(resultado['erros'])} ponto(s)!")
        elif resultado.get("status") == "OK":
            print(f"Registrado: {resultado.get('registro', {}).get('acao', '?')}")
        else:
            print(f"ERRO: {resultado.get('erro', 'Falha desconhecida')}")
            sys.exit(1)


if __name__ == "__main__":
    main()
