"""Ingestao de modelos de representacao (.docx) para templates de texto.

Resolve dois problemas dos arquivos brutos do usuario:
1. Muitos .docx vieram de conversao de PDF e PERDERAM os espacos entre palavras
   ("REPRESENTOaVossaExcelencia"). Reconstrui os espacos por segmentacao de
   programacao dinamica, usando um lexico montado a partir dos proprios arquivos
   que vieram bem formatados (o vocabulario juridico se repete entre eles).
2. Dados sensiveis (nomes, e-mails, CPFs, telefones, numeros de processo) sao
   substituidos por placeholders.

Uso:
    python scripts/ingest_modelos.py <pasta_brutos> <pasta_saida_txt>

O resultado e texto limpo; a curadoria final (nomear, classificar, escrever o
cabecalho do template e indexar no catalogo) e feita pelo Claude.
"""

import math
import os
import re
import sys
import unicodedata
from collections import Counter

try:
    from docx import Document
    from docx.table import Table
    from docx.text.paragraph import Paragraph
    from docx.oxml.table import CT_Tbl
    from docx.oxml.text.paragraph import CT_P
except ImportError:
    sys.exit("Instale python-docx: pip install python-docx")

# Vocabulario semente. Fica num arquivo externo, e nao no codigo, porque a lista
# reflete o vocabulario operacional das pecas do usuario (material sigiloso, ver
# references/catalogo-modelos.LEIA-ME.md). O script funciona sem ele: apenas
# reconstroi menos espacos, deixando mais palavras coladas para a curadoria.
SEED_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lexico-semente.txt")

_FALLBACK_SEED = """
ante exposto objetivando possibilitar localizacao colheita elementos venham auxiliar
investigacoes visto impossibilidade producao provas outros meios represento vossa
excelencia afastamento sigilo dados eletronicos telematicos bancario fiscal expedicao
mandados judiciais contendo expressamente mandado seguintes determinacoes contas periodo
envio cadastrais nome enderecos atividades respectivas conexao portas logicas data hora
acessos marcas modelos aparelhos telefonicos vinculados referencia numeros dispositivos
fornecimento conteudo armazenado servico imagens fotografias videos respectivos metadados
aplicacao historico pesquisa pontos interesse deslocamento registrado sistema integral
usuarios documentos incluindo arquivos enviados anexos formato preservando estrutura
informar quais vinculadas localizacoes dispositivo geograficas especificas meio agenda
contatos moveis sobre cartoes debito credito caso investigados mencionados utilizem
transacoes financeiras relacionadas aplicativos baixados natureza financeira determinar
notifique quebra trata investigacao tramita segredo justica descumprimento estabeleca
multa cem mil reais diaria valor limite determinacao judicial cumprimento parcial termos
artigo razao necessaria celeridade exigida informo encaminhado utilizado empresa receber
solicitacoes legais respectiva resposta direcionada constando como referencia processo
indicado interceptacao fluxo comunicacoes informatica telematica prazo dias policia civil
estado delegado subscritor uso atribuicoes legais regulamentares conferidas constituicao
federal codigo processo penal lei demais dispositivos correlatos representa motivos fato
direito seguir apresentados inviolabilidade telefonicas criminal instrucao processual
ordem juiz competente acao principal jurisprudencia pacifica sentido permitir esclarecer
fatos habeas corpus indicios crime legalidade privacidade ressalva admitir persecucao
mediante autorizacao acesso documentos informacoes bem relator ministro orgao julgador
turma julgamento publicacao ementa representacao gravidade demonstram veracidade alegado
suporte probatorio autorizar marco internet principios garantias direitos deveres brasil
coleta armazenamento guarda tratamento registros pessoais provedores aplicacoes territorio
nacional legislacao brasileira sequestro indisponibilidade bens valores busca apreensao
extracao analise investigados instaurou inquerito policial fortes suspeitos condutas
tipos penais medidas necessarias urgentes apuracao verdade real ressarcimento vitimas
danos patrimoniais decretacao assecuratorias patrimonial produto delito reparacao dano
infracoes praticadas pagamento custas processuais assegurar atividade criminosa vantagem
operadoras telefonia movel chamadas efetuadas recebidas conexoes registradas cobertura
enderecos datas periodos especificados prazo maximo horas antenas apresentar planilha
terminal extrato tempo interlocutores relatorio retroativos durante recebimento oficio
agentes autorizados investigacao concessionaria forneca mensagens texto compreendido
vara criminal comarca juizo representar linhas vinculada relacionadas razoes momento
fundamentos posto fundamento republica garantia publica regulamenta preve resolucao
deferimento conste desvio plataforma digital diretoria inteligencia responsavel indicacao
usuario senha endereco porta utilizadas providenciado segundo audio solicitado autoridade
requisitante telefones policiais indicados necessidade original serial forma execucao
medida provedores estiverem trafego voz instantaneas multimidia paginas acessadas
recebidos extensao transferencias protocolos remoto conversacao instantanea chamadas
video utilizar softwares sites relacionamentos reproducao nominalmente independentemente
tecnologia geografica antena precisao possivel identificacao assinante alteracoes
contratuais monitoramento correspondentes qualificativos telefone inicio termino bytes
referentes trafegada ponto emissao originadas expressamente quaisquer vinculado
temporario terminais internet autorizado definidos implementado questionamento parte
manter respondendo tecnico portabilidade comunicar administracao efetivada continuidade
condicoes pedido eventual transicao desativacao ativacao servico telecomunicacoes
concluida cumprir iniciando referida encerramento inicialmente fixado suspensao entrega
conexao gerencia apoio tecnologico existentes pais podem evitando perda possibilitando
investigacoes rastreamento senha feito eletronicos analistas acompanhamento diligencias
responsabilidade subscritora matricula preservando constitucional solicitar diretamente
operadora comunicando imediatamente cancelamento autorizada unidade empresas requisitado
constar valores pagamento estabelecimento vinculado indicada autorizadas pesquisas
demais checagens disponiveis vierem investigativo aguarda oficios elaborados
individualmente limites definidos judiciaria reproduzindo constantes listados usados
disponibilizar captacao proprio eventos navegados troca concessionarias curso suspenso
total somente determinados criterio solicitante informado respondendo concedida imediato
notebooks objetos apreendidos posse investigado angariados compartilhada procedimentos
policiais delegacia unidades civis possibilidade obter ligados crimes titulares acerca
requisicao procedimento sigiloso encaminhados responsaveis expediente indicar completo
institucional agente membro ministerio publico autoridades juizo emissor alienacao
antecipada destinacao fundo especial prisao preventiva imoveis deferido cautelar operacao
veiculos sequestrados bloqueadas bancarias denunciados especies relacao segue permanecem
constritos lastro procedencia licita indicios trazidos autos relacionados ilicita
indiciados encontram atualmente sofrendo manutencao exigem cuidados complexidade custos
administracao preconizado lavagem preservar valor qualidade hipotese sentenca obtidos
devolvidos instituido receitas ativos financeiros provenientes apurados conduzida
perdimento decretado poder judiciario favor arrecadados ambito propriedade identificada
regulamentando publicado decreto recursos decorrentes transito julgado divisao podendo
utilizados conselho gestor tribunal dispondo materiais gestao parceria orgaos
administrativos respeitados aplicavel garantir preservacao adequada consonancia
constricao processos avaliar deliberar restituicao utilizacao descarte destruicao normas
aplicaveis requerimento estadual podera realizar leiloes publicos preferencialmente
ampla divulgacao participacao interessados obtencao propostas arrecadado destinado
vigente observado depositado disposicao bloqueados ordens destinados agencia corrente
secretaria carater provisorio secretarias prestado contas tramites hasta publica ficando
condicionada necessario registrar alienados tema pacificado veiculo passivel penhora
pertence credor possibilitar restituicao instituicao financeira intimada depositar pagos
devedor oriundos ilicitas pena consequente mediante cautela reversao prolacao
condenatoria interesse termos pede espera identificativas perfis representacao
cautelares preventiva temporaria flagrante autuado conduzido vitima testemunha
protetiva domestica familiar mulher genero vulneravel enfermo idoso deficiencia
reiteracao pregressa aplicacao contemporaneidade subsidiariedade proporcionalidade
individualizacao fundadas razoes domiciliar diurno noturno cadeia custodia forense
denuncia anonima corroborada movimentacao entorpecente entorpecentes trafico
municoes arma armas fogo receptacao estelionato furto roubo extorsao ameaca lesao
homicidio sequestro carcere privado estupro epidemia genocidio associacao hediondos
"""


def _load_seed():
    """Le o lexico externo; se ausente, usa o fallback generico embutido."""
    if os.path.exists(SEED_FILE):
        with open(SEED_FILE, encoding="utf-8") as f:
            lines = [l for l in f if not l.lstrip().startswith("#")]
        return " ".join(lines)
    return _FALLBACK_SEED


SEED = _load_seed()


def strip_accents(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def iter_blocks(doc):
    for child in doc.element.body.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, doc)
        elif isinstance(child, CT_Tbl):
            yield Table(child, doc)


def raw_text(path):
    doc = Document(path)
    out = []
    for b in iter_blocks(doc):
        if isinstance(b, Paragraph):
            if b.text.strip():
                out.append(b.text.rstrip())
        else:
            for row in b.rows:
                cells, seen = [], None
                for c in row.cells:
                    t = c.text.strip().replace("\n", " ")
                    if t != seen:
                        cells.append(t)
                        seen = t
                if any(cells):
                    out.append("| " + " | ".join(cells) + " |")
    return "\n".join(out)


GLUE_RE = re.compile(r"[A-Za-zÀ-ÿ]{6,}")


def build_lexicon(texts):
    """Palavras que aparecem ja separadas em qualquer arquivo do lote.

    Os proprios tokens colados tambem casam com o regex, entao exigimos
    frequencia >= 2 para palavras nao-semente: artefatos de colagem tendem a ser
    unicos, palavras reais se repetem. Tokens longos (>=12) so entram via semente.
    """
    seed = {strip_accents(w).lower() for w in SEED.split()}
    raw = Counter()
    for t in texts:
        for w in re.findall(r"[A-Za-zÀ-ÿ]+", t):
            raw[strip_accents(w).lower()] += 1

    freq = Counter()
    for w, c in raw.items():
        if w in seed or len(w) > 15:
            continue
        if c >= 2 and len(w) <= 11:
            freq[w] = c
    for w in seed:
        freq[w] += 20
    return freq


# Monossilabos/preposicoes que podem faltar no corpus mas sao validos isolados.
SHORT_OK = set("a e o as os da de do das dos na no nas nos em um uma ao aos com por "
               "que se sua seu suas seus la lo ha ja ou nem ate sob ser sao pelo pela "
               "ip ips id ids cpf erb erbs sms mms gps url urls".split())

WORD_PENALTY = 4.0  # penaliza particoes com muitas pecas (evita estilhacar palavras)


def segment(token, freq, total):
    """Melhor particao do token em palavras do lexico.

    Regras de seguranca, nesta ordem de importancia:
    1. Se o token inteiro ja e palavra conhecida, nao mexe (protege "quebra",
       "sobrepor" e afins de serem partidos indevidamente).
    2. TODA peca precisa estar no lexico (ou ser monossilabo/sigla conhecida).
       Tentamos tolerar pecas desconhecidas com custo alto e o resultado foi pior:
       o algoritmo passa a cortar em qualquer ponto ("SECRETARIADEJUSTIÇ A").
       Sem lexico completo do portugues, exigir palavras conhecidas e a unica
       regra que nunca corrompe o texto.
    Se nao houver particao valida, devolve None e o token fica colado: erro
    visivel e corrigivel na curadoria, em vez de corrupcao silenciosa do texto.
    Trecho colado o Claude ainda le corretamente; palavra partida errado, nao.
    """
    low = strip_accents(token).lower()
    if low in freq:
        return None
    n = len(low)
    NEG = -1e18
    best = [(0.0, 0)] + [(NEG, 0)] * n
    for i in range(1, n + 1):
        for j in range(max(0, i - 18), i):
            if best[j][0] == NEG:
                continue
            w = low[j:i]
            c = freq.get(w, 0)
            if c and len(w) >= 3:
                score = math.log(c / total)
            elif w in SHORT_OK:
                score = math.log(max(freq.get(w, 1), 1) / total) - 1.0
            else:
                continue
            cand = best[j][0] + score - WORD_PENALTY
            if cand > best[i][0]:
                best[i] = (cand, j)
    if best[n][0] == NEG:
        return None
    cuts, i = [], n
    while i > 0:
        j = best[i][1]
        cuts.append((j, i))
        i = j
    cuts.reverse()
    if len(cuts) == 1:
        return None
    return " ".join(token[a:b] for a, b in cuts)


def deglue(text, freq, total, flagged):
    def repl(m):
        tok = m.group(0)
        # siglas curtas em caixa alta (NCPC, CPP, ERB) ficam intactas
        if tok.isupper() and len(tok) <= 5:
            return tok
        seg = segment(tok, freq, total)
        if not seg or seg == tok:
            if len(tok) >= 12:  # so vale a pena revisar os visivelmente colados
                flagged.append(tok)
            return tok
        return seg

    return GLUE_RE.sub(repl, text)


# \b nao funciona aqui: nos arquivos colados o numero costuma vir grudado em "nº",
# e "º" conta como caractere de palavra em Unicode. Usamos lookarounds de digito.
NB = r"(?<![\d])"
NA = r"(?![\d])"

SANITIZE = [
    (re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+"), "[EMAIL]"),
    (re.compile(NB + r"\d{3}\.\d{3}\.\d{3}-\d{2}" + NA), "[CPF]"),
    (re.compile(NB + r"\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}" + NA), "[CNPJ]"),
    (re.compile(NB + r"\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4}" + NA), "[Nº AUTOS]"),
    (re.compile(r"\+?55\s?\(?\d{2}\)?\s?9?\d{4}[-\s]?\d{3,4}"), "[TELEFONE]"),
    (re.compile(NB + r"\d{15}" + NA), "[IMEI]"),
]


def sanitize(text):
    for rx, rep in SANITIZE:
        text = rx.sub(rep, text)
    return text


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else "assets/modelos-brutos"
    dst = sys.argv[2] if len(sys.argv) > 2 else "assets/modelos-txt"
    os.makedirs(dst, exist_ok=True)

    files = [f for f in sorted(os.listdir(src)) if f.lower().endswith(".docx")]
    raws = {f: raw_text(os.path.join(src, f)) for f in files}

    freq = build_lexicon(raws.values())
    total = sum(freq.values())

    for f, text in raws.items():
        flagged = []
        clean = sanitize(deglue(text, freq, total, flagged))
        out = os.path.join(dst, os.path.splitext(f)[0] + ".txt")
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(clean)
        msg = f"{f}: ok"
        if flagged:
            msg += f" | nao segmentados: {len(flagged)}"
        print(msg)


if __name__ == "__main__":
    main()
