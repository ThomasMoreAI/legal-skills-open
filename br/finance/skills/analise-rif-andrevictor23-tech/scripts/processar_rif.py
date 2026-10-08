#!/usr/bin/env python3
"""Processador de dados RIF/COAF.

Carrega, valida, limpa, deduplica e resume os 3 CSVs do RIF (Envolvidos,
Comunicacoes, Ocorrencias) e monta as tabelas relacionais das FASES 4 e 5
(cruzamento por Indexador, titulares, correlacoes, verificacao de alvos).
Substitui os blocos de codigo que antes viviam colados no SKILL.md: aqui e um
arquivo executavel e testavel, nao um exemplo para reproduzir a mao.

Uso:
    python processar_rif.py --entrada DIR_COM_OS_CSVS
    python processar_rif.py --entrada . --saida resumo.json
    python processar_rif.py --entrada . --exportar-limpos ./limpos
    python processar_rif.py --entrada . --alvos alvos.csv --saida resumo.json

alvos.csv: colunas `nome` e `cpf_cnpj` (separador ; ou ,), uma linha por alvo.
Tambem aceita .json com uma lista de objetos com as mesmas chaves.

Requisito: pandas.
"""

import argparse
import json
import os
import re
import sys
import unicodedata

import pandas as pd

CAMPOS_VALOR = ["CampoA", "CampoB", "CampoC", "CampoD", "CampoE"]
NATUREZA_CORRELACAO = "correlacao de registros no RIF; nao prova vinculo"


def so_digitos(s):
    if s is None or pd.isna(s):
        return ""
    return re.sub(r"\D", "", str(s))


def normalizar_nome(s):
    """Maiusculas, sem acento e com espacos colapsados, para comparar nome completo."""
    if s is None or pd.isna(s):
        return ""
    s = unicodedata.normalize("NFKD", str(s))
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", s).strip().upper()


def formatar_valor_br(valor):
    return "R$ " + f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def carregar_alvos(caminho):
    if caminho.lower().endswith(".json"):
        with open(caminho, encoding="utf-8") as fh:
            return json.load(fh)
    for sep in (";", ","):
        df = pd.read_csv(caminho, sep=sep, dtype=str, encoding="utf-8-sig").fillna("")
        if {"nome", "cpf_cnpj"} <= set(df.columns):
            return df.to_dict("records")
    raise ValueError(f"{caminho}: esperado CSV com colunas nome e cpf_cnpj, ou JSON")


class ProcessadorRIF:
    def __init__(self, dir_entrada="."):
        self.dir = dir_entrada
        self.df_env = None
        self.df_com = None
        self.df_oco = None
        self.legendas_campos = {}
        self.log_processamento = []
        self.metricas = {}

    def log(self, msg):
        self.log_processamento.append(msg)
        print(msg)

    def carregar_csv(self, filepath):
        """Carrega CSV do COAF com deteccao automatica de encoding e separador."""
        for enc in ["latin-1", "utf-8", "cp1252"]:
            for sep in [";", ","]:
                try:
                    df = pd.read_csv(filepath, encoding=enc, sep=sep, dtype=str)
                except Exception:
                    continue
                if len(df.columns) > 1 and "Indexador" in df.columns:
                    self.log(
                        f"OK  Carregado: {os.path.basename(filepath)} "
                        f"({enc}, sep='{sep}', {len(df)} linhas)"
                    )
                    return df
        raise ValueError(f"Falha ao ler: {filepath}")

    def encontrar_arquivos(self):
        """Encontra os 3 CSVs do RIF no diretorio de entrada."""
        arquivos = os.listdir(self.dir)
        csv_files = [f for f in arquivos if f.lower().endswith(".csv") and "RIF" in f.upper()]

        env = [f for f in csv_files if "envolvido" in f.lower()]
        com = [f for f in csv_files if "comunicac" in f.lower()]
        oco = [f for f in csv_files if "ocorrencia" in f.lower()]

        return env, com, oco

    def extrair_legendas(self, df_com_raw):
        """Extrai legendas dos campos de valores das linhas nao-indexadoras.

        A legenda do proprio arquivo prevalece sobre references/legenda_campos_segmento.md.
        """
        legendas = {}
        for _, row in df_com_raw.iterrows():
            idx = str(row.get("Indexador", "")).strip()
            if not idx.isdigit() and idx and re.match(r"^\d+\s*-", idx):
                # Linha de legenda: "42 - SFN - Especie: CampoA = Total..."
                match = re.match(r"^(\d+)\s*-\s*(.+)", idx)
                if match:
                    legendas[match.group(1)] = match.group(2)
        self.legendas_campos = legendas
        return legendas

    def filtrar_indexadores(self, df):
        """Mantem apenas as linhas com indexador numerico valido."""
        df_clean = df.copy()
        df_clean["Indexador"] = df_clean["Indexador"].astype(str).str.strip()
        mask = df_clean["Indexador"].str.match(r"^\d+$", na=False)
        removidos = int((~mask).sum())
        df_clean = df_clean[mask].copy()
        df_clean["Indexador"] = df_clean["Indexador"].astype(int)
        return df_clean, removidos

    def deduplicar(self, df_com):
        """Deduplica por idComunicacao (nivel-caso; ids vazios sao unicos — ver FASE 3).

        Entre duplicatas, mantem a linha com informacoesAdicionais mais longa.
        """
        if "idComunicacao" not in df_com.columns:
            return df_com, 0

        antes = len(df_com)
        ids = df_com["idComunicacao"].fillna("").astype(str).str.strip()
        sem_id = df_com[ids == ""]
        com_id = df_com[ids != ""].copy()
        com_id["_info_len"] = (
            com_id.get("informacoesAdicionais", pd.Series(dtype=str)).fillna("").str.len()
        )
        com_id = (
            com_id.sort_values("_info_len", ascending=False)
            .drop_duplicates(subset=["idComunicacao"], keep="first")
            .drop(columns=["_info_len"])
        )
        df_dedup = pd.concat([com_id, sem_id]).sort_index()
        return df_dedup, antes - len(df_dedup)

    def converter_valor(self, val):
        """Converte valor monetario (padrao brasileiro ou americano) para float.

        Vazio, "0" e "-" valem 0.0 (ausencia de valor). Texto que nao e numero
        devolve NaN: fica fora das somas e sai no resumo como [VERIFICAR].
        """
        if pd.isna(val) or str(val).strip() in ["", "0", "-"]:
            return 0.0
        s = re.sub(r"\s|R\$", "", str(val), flags=re.IGNORECASE)
        if not s:
            return 0.0
        tem_ponto, tem_virgula = "." in s, "," in s
        if tem_ponto and tem_virgula:
            s = s.replace(".", "").replace(",", ".")
        elif tem_virgula:
            s = s.replace(",", ".")
        elif tem_ponto and re.fullmatch(r"-?\d{1,3}(\.\d{3})+", s):
            s = s.replace(".", "")
        try:
            return float(s)
        except ValueError:
            return float("nan")

    def processar(self):
        """Pipeline completo. Devolve True se processou os 3 arquivos."""
        env_files, com_files, oco_files = self.encontrar_arquivos()

        faltando = [
            nome
            for nome, lista in (("Envolvidos", env_files), ("Comunicacoes", com_files), ("Ocorrencias", oco_files))
            if not lista
        ]
        if faltando:
            self.log(f"ERRO  CSV do RIF nao encontrado: {', '.join(faltando)} (em {self.dir})")
            return False

        self.df_env = self.carregar_csv(os.path.join(self.dir, env_files[0]))
        self.df_com = self.carregar_csv(os.path.join(self.dir, com_files[0]))
        self.df_oco = self.carregar_csv(os.path.join(self.dir, oco_files[0]))

        # Legendas saem das linhas nao-indexadoras — extrair ANTES de filtrar.
        self.extrair_legendas(self.df_com)

        self.df_env, rem_env = self.filtrar_indexadores(self.df_env)
        self.df_com, rem_com = self.filtrar_indexadores(self.df_com)
        self.df_oco, rem_oco = self.filtrar_indexadores(self.df_oco)
        self.log(
            f"Indexadores filtrados - Env: {rem_env} removidos, "
            f"Com: {rem_com} removidos, Oco: {rem_oco} removidos"
        )

        self.df_com, dedup = self.deduplicar(self.df_com)
        self.log(f"Deduplicacao: {dedup} comunicacoes duplicadas eliminadas")

        invalidos = {}
        for campo in CAMPOS_VALOR:
            if campo in self.df_com.columns:
                col = self.df_com[campo].apply(self.converter_valor)
                self.df_com[f"{campo}_float"] = col
                ruins = self.df_com[col.isna()]
                if len(ruins):
                    invalidos[campo] = [
                        {
                            "Indexador": int(r["Indexador"]),
                            "idComunicacao": str(r.get("idComunicacao", "")),
                            "valor_bruto": str(r[campo]),
                        }
                        for _, r in ruins.iterrows()
                    ]

        # Periodo sobre datas convertidas: ordenacao textual de dd/mm/aaaa erra.
        inicio, fim, datas_ruins = "N/I", "N/I", 0
        if "Data_da_operacao" in self.df_com.columns:
            datas = pd.to_datetime(
                self.df_com["Data_da_operacao"].str.strip(), format="%d/%m/%Y", errors="coerce"
            )
            datas_ruins = int(datas.isna().sum())
            if datas.notna().any():
                inicio = datas.min().strftime("%d/%m/%Y")
                fim = datas.max().strftime("%d/%m/%Y")

        self.metricas = {
            "comunicacoes_validas": len(self.df_com),
            "comunicacoes_removidas_dedup": dedup,
            "indexadores_unicos": int(self.df_com["Indexador"].nunique()),
            "titulares": int(self.titulares()["cpfCnpjEnvolvido"].nunique()),
            "envolvidos": int(self.df_env["cpfCnpjEnvolvido"].nunique()),
            "ocorrencias": len(self.df_oco),
            "valor_total_campoA": float(self.df_com["CampoA_float"].sum())
            if "CampoA_float" in self.df_com.columns
            else 0.0,
            "valores_invalidos": invalidos,
            "periodo_inicio": inicio,
            "periodo_fim": fim,
            "datas_ausentes_ou_invalidas": datas_ruins,
            "correlacoes_por_indexador": len(self.correlacoes_por_indexador()),
            "legendas_do_arquivo": self.legendas_campos,
        }

        m = self.metricas
        self.log("")
        self.log("RESUMO DO RIF:")
        self.log(f"   Comunicacoes validas: {m['comunicacoes_validas']}")
        self.log(f"   Indexadores unicos:   {m['indexadores_unicos']}")
        self.log(f"   Titulares:            {m['titulares']}")
        self.log(f"   Total de envolvidos:  {m['envolvidos']}")
        self.log(f"   Valor total (CampoA): {formatar_valor_br(m['valor_total_campoA'])}")
        self.log(f"   Periodo:              {m['periodo_inicio']} a {m['periodo_fim']}")
        if datas_ruins:
            self.log(f"   [VERIFICAR] {datas_ruins} comunicacao(oes) sem data valida, fora do periodo")
        for campo, itens in invalidos.items():
            self.log(f"   [VERIFICAR] {campo}: {len(itens)} valor(es) invalido(s), fora das somas")

        return True

    def titulares(self):
        """FASE 4.2: titulares de conta (tipoEnvolvido = Titular)."""
        cols = [
            c
            for c in ("Indexador", "cpfCnpjEnvolvido", "nomeEnvolvido", "agenciaEnvolvido", "contaEnvolvido", "DataAberturaConta")
            if c in self.df_env.columns
        ]
        t = self.df_env[self.df_env["tipoEnvolvido"].str.strip().str.lower() == "titular"]
        return t[cols].drop_duplicates()

    def cruzar(self):
        """FASE 4.1: cruza os tres arquivos pelo Indexador (uma linha por combinacao)."""
        df = pd.merge(self.df_env, self.df_com, on="Indexador", how="outer", suffixes=("_env", "_com"))
        return pd.merge(df, self.df_oco, on="Indexador", how="outer", suffixes=("", "_oco"))

    def correlacoes_por_indexador(self):
        """FASE 5.3: pares de envolvidos que aparecem no mesmo Indexador.

        O mesmo Indexador so indica correlacao de registros no RIF; nao prova,
        por si, vinculo financeiro, societario, familiar ou criminoso.
        """
        cols = ["cpfCnpjEnvolvido", "nomeEnvolvido", "tipoEnvolvido"]
        pares = []
        for idx, grupo in self.df_env.groupby("Indexador"):
            pessoas = grupo[cols].drop_duplicates().values.tolist()
            for i in range(len(pessoas)):
                for j in range(i + 1, len(pessoas)):
                    pares.append({
                        "indexador": int(idx),
                        "pessoa_1": pessoas[i][1], "cpf_cnpj_1": pessoas[i][0], "tipo_1": pessoas[i][2],
                        "pessoa_2": pessoas[j][1], "cpf_cnpj_2": pessoas[j][0], "tipo_2": pessoas[j][2],
                        "natureza": NATUREZA_CORRELACAO,
                    })
        colunas = ["indexador", "pessoa_1", "cpf_cnpj_1", "tipo_1", "pessoa_2", "cpf_cnpj_2", "tipo_2", "natureza"]
        return pd.DataFrame(pares, columns=colunas)

    def verificar_alvos(self, alvos):
        """FASE 4.5: localiza os alvos da investigacao no RIF.

        Correspondencia so vale por CPF/CNPJ. Nome completo identico sem o mesmo
        documento gera apenas candidato [VERIFICAR] (homonimo e comum). Nome
        parcial nunca casa.
        """
        env = self.df_env.assign(
            _doc=self.df_env["cpfCnpjEnvolvido"].map(so_digitos),
            _nome=self.df_env["nomeEnvolvido"].map(normalizar_nome),
        )
        vazio = env.iloc[0:0]
        resultados = []
        for alvo in alvos:
            doc = so_digitos(alvo.get("cpf_cnpj", ""))
            nome = normalizar_nome(alvo.get("nome", ""))
            achados = env[env["_doc"] == doc] if doc else vazio
            status = "encontrado_por_documento"
            if achados.empty:
                achados = env[env["_nome"] == nome] if nome else vazio
                if achados.empty:
                    status = "nao_encontrado"
                elif doc:
                    status = "[VERIFICAR] nome identico, documento divergente"
                else:
                    status = "[VERIFICAR] nome identico, alvo sem documento"
            resultados.append({
                "alvo_nome": alvo.get("nome", ""),
                "alvo_cpf_cnpj": alvo.get("cpf_cnpj", ""),
                "status": status,
                "no_rif": [
                    {
                        "nome": n,
                        "cpf_cnpj": c,
                        "tipos": sorted(g["tipoEnvolvido"].str.strip().unique().tolist()),
                        "indexadores": sorted(int(i) for i in g["Indexador"].unique()),
                    }
                    for (c, n), g in achados.groupby(["cpfCnpjEnvolvido", "nomeEnvolvido"])
                ],
            })
        return resultados

    def exportar_limpos(self, destino):
        """Grava os CSVs limpos e as tabelas relacionais, base das FASES 4 a 6."""
        os.makedirs(destino, exist_ok=True)
        tabelas = (
            ("limpo_envolvidos", self.df_env),
            ("limpo_comunicacoes", self.df_com),
            ("limpo_ocorrencias", self.df_oco),
            ("cruzado_por_indexador", self.cruzar()),
            ("titulares", self.titulares()),
            ("correlacoes_por_indexador", self.correlacoes_por_indexador()),
        )
        for nome, df in tabelas:
            caminho = os.path.join(destino, f"{nome}.csv")
            df.to_csv(caminho, index=False, encoding="utf-8", sep=";")
            self.log(f"Gravado: {caminho}")


def main():
    ap = argparse.ArgumentParser(
        description="Processa os CSVs do RIF/COAF (validacao, limpeza, deduplicacao, resumo e tabelas relacionais)."
    )
    ap.add_argument("--entrada", default=".", help="diretorio com os 3 CSVs do RIF (padrao: diretorio atual)")
    ap.add_argument("--saida", help="grava o resumo em JSON neste arquivo")
    ap.add_argument("--exportar-limpos", metavar="DIR", help="grava os CSVs limpos e as tabelas das FASES 4 e 5 neste diretorio")
    ap.add_argument("--alvos", metavar="ARQ", help="CSV (nome;cpf_cnpj) ou JSON com os alvos a localizar no RIF")
    args = ap.parse_args()

    proc = ProcessadorRIF(args.entrada)
    if not proc.processar():
        return 1

    if args.alvos:
        proc.metricas["alvos"] = proc.verificar_alvos(carregar_alvos(args.alvos))
        proc.log("")
        proc.log("ALVOS:")
        for r in proc.metricas["alvos"]:
            proc.log(f"   {r['alvo_nome'] or r['alvo_cpf_cnpj']}: {r['status']}")

    if args.exportar_limpos:
        proc.exportar_limpos(args.exportar_limpos)

    if args.saida:
        with open(args.saida, "w", encoding="utf-8") as fh:
            json.dump(proc.metricas, fh, ensure_ascii=False, indent=2)
        print(f"\nResumo gravado em {args.saida}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
