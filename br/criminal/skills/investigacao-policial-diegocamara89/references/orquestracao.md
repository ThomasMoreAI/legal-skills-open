# Guia de Orquestracao Multi-Agente para Investigacao

Referencia operacional para o agente principal decidir quando e como usar subagentes extratores e validador. Carregar este arquivo quando o volume de documentos justificar processamento multi-agente.

## Sumario

1. [Arvore de Decisao: Single vs Multi](#1-arvore-de-decisao)
2. [Como Dividir Documentos em Lotes](#2-divisao-em-lotes)
3. [Como Formular Prompts dos Extratores](#3-prompts-dos-extratores)
4. [Como Consolidar Retornos](#4-consolidacao)
5. [Como Acionar o Validador](#5-validacao)
6. [Como Interpretar Retornos do Validador](#6-interpretacao)
7. [Anti-Patterns](#7-anti-patterns)

---

## 1. Arvore de Decisao

```
Quantas paginas/documentos o caso tem?
|
|-- [< 50 paginas] --> AGENTE UNICO
|   Processar tudo diretamente.
|   Nao spawnar subagentes — o overhead nao compensa.
|   Seguir as Fases 1-5 da skill normalmente.
|
|-- [50-200 paginas] --> MODO MULTI (leve)
|   Spawnar 2-3 extratores em paralelo.
|   Cada extrator processa um lote tematico.
|   Apos consolidacao, spawnar 1 validador.
|
|-- [200+ paginas] --> MODO MULTI (completo)
|   Spawnar 4-6 extratores em paralelo.
|   Dividir por tipo de documento E por volume.
|   Apos consolidacao, spawnar 1 validador.
|   Considerar processar em 2 rodadas se > 500 paginas.
|
Outros criterios para ativar modo multi (independente de volume):
- Documentos em 3+ formatos diferentes (PDF + XLSX + DOCX)
- Fontes de dados claramente independentes (banco + operadora + TJ)
- Usuario pede explicitamente analise multi-agente
```

## 2. Divisao em Lotes

Dividir por **tipo de fonte**, nao por numero de paginas. Cada extrator deve processar documentos de uma mesma natureza para que seu "vocabulario" de extracao seja consistente.

### Lotes tipicos

| Lote | Extrator | Documentos tipicos |
|------|----------|--------------------|
| Bancario | `extrator_bancario` | Extratos, comprovantes Pix/TED, dados de abertura de conta, selfie biometrica |
| Provedores | `extrator_provedores` | Respostas da Meta/WhatsApp, Google, Microsoft (IPs, logs, dispositivos) |
| Operadoras | `extrator_telefonico` | Respostas de Claro/Vivo/Tim/Oi (IMEI, titular, linhas, ERBs) |
| Judicial | `extrator_judicial` | Logs de acesso ao PJe/TJ, certidoes, andamentos processuais |
| Documental | `extrator_documental` | BOs, depoimentos, oficios, laudos, portarias |
| Financeiro | `extrator_financeiro` | RIFs/COAF, BACENJUD, demonstrativos, planilhas de movimentacao |

### Regras de divisao

- Cada extrator recebe NO MAXIMO 100 paginas (se ultrapassar, dividir em sub-lotes)
- Se um documento aparece em mais de uma categoria (ex: extrato com IP), colocar no lote mais especifico (bancario, nao generico)
- Manter documentos relacionados no mesmo lote (ex: oficio de requisicao + resposta da operadora juntos)

## 3. Prompts dos Extratores

O prompt de cada extrator combina a base fixa (`agents/extrator.md`) com contexto do caso. O agente principal monta o prompt assim:

### Template de prompt

```
Voce e um extrator de dados investigativos.
Leia o arquivo agents/extrator.md para suas instrucoes completas e schema de saida.

CONTEXTO DO CASO:
- BO/IP: [numero]
- Crime: [tipo]
- Periodo de interesse: [data_inicio] a [data_fim]
- Suspeitos conhecidos (se houver): [nomes]

SEU LOTE:
Processar os seguintes arquivos:
1. [caminho/arquivo1.pdf] — [descricao breve, ex: "extrato Bradesco mar/2025"]
2. [caminho/arquivo2.xlsx] — [descricao breve]

PRIORIDADE DE EXTRACAO:
- [Adaptar ao lote: para bancario, priorizar IPs de transacao e valores]
- [Para provedores, priorizar IPs de acesso e timestamps]
- [Para operadoras, priorizar IMEIs e titulares]

Retorne a saida no schema "Lote de Extracao" definido em references/schemas_multiagente.md.
Seu extrator_id e: "[ex: extrator_bancario_01]"
```

### O que adaptar por lote

| Lote | Prioridade de extracao |
|------|------------------------|
| Bancario | IPs de transacao, valores, contas destino/origem, timestamps, dispositivos |
| Provedores | IPs de acesso com timestamp exato (h:m:s + fuso), tipo dispositivo, numeros vinculados |
| Operadoras | IMEI, titular da linha, tipo plano (pre/pos), data ativacao, todas linhas do IMEI |
| Judicial | IPs de acesso ao processo, usuario logado (OAB, nome), timestamps |
| Documental | Nomes, datas de eventos, enderecos, relatos de fatos, numeros de documentos |
| Financeiro | Contas, titulares, valores, datas, chaves Pix, tipologias suspeitas |

## 4. Consolidacao

Apos receber os retornos de todos os extratores:

### Passo 1 — Validacao estrutural dos extratores
Antes de consolidar, verificar CADA retorno de extrator:

- `status: "OK"`? Se "ERRO", verificar `alertas` e decidir se re-spawnar
- `total_dados` bate com `len(dados_extraidos)`?
- Alguma `paginas_com_falha`? Se sim, avaliar impacto

**Rejeitar automaticamente** dados que nao passem nestes criterios minimos:
- `pagina` deve ser coerente com o documento (nao maior que total de paginas)
- `linha_ou_celula` deve estar preenchido (nao vazio, nao generico como "documento inteiro")
- `texto_original` deve conter o valor do campo `dado` (se o dado e "187.34.56.78", o texto_original deve conter "187.34.56.78")
- Para XLSX: `linha_ou_celula` deve incluir referencia Excel real (ex: "linha 4 / Excel row 5 / colunas B-D") — nao apenas indice de dataframe

Dados rejeitados devem ser registrados em alerta para analise posterior, nao descartados silenciosamente.

### Passo 2 — Unificar dados
Juntar todos os `dados_extraidos` de todos os extratores em uma unica lista. Manter o `extrator_id` de cada dado para rastreabilidade.

### Passo 3 — Deduplicar
Se o mesmo dado aparece em mais de um extrator (ex: mesmo IP em fontes diferentes), NAO remover duplicatas — elas sao evidencia de convergencia. Apenas remover duplicatas exatas (mesmo arquivo, mesma pagina, mesmo dado, mesmo extrator).

### Passo 4 — Indexar por tipo
Organizar os dados unificados em tabelas por `tipo_dado`:
- Todos os IPs juntos (ordenados por timestamp)
- Todos os telefones juntos
- Todos os IMEIs juntos
- Todos os nomes juntos
- etc.

### Passo 5 — Cruzar
Agora que todos os dados estao estruturados e indexados, aplicar as Fases 3-4 da skill (Cruzamento de IPs, Expansao de Rede, Estabelecimento de Autoria) usando as tabelas indexadas em vez de documentos brutos.

### Passo 6 — Produzir conclusoes
Cada conclusao deve:
- Seguir o schema da secao 3 de `references/schemas_multiagente.md`
- Herdar as referencias exatas dos dados que a sustentam
- Incluir `extrator_id` em cada referencia para rastreabilidade

## 4B. Saneamento Tecnico de Referencias

Fase obrigatoria entre a producao de conclusoes (Passo 6) e a validacao (secao 5). O objetivo e garantir que as referencias estejam em formato que o validador consiga verificar deterministicamente, reduzindo falsos AMBIGUO.

### Por que esta fase existe

No beta com IP 11329/2025, o agente principal produziu conclusoes corretas em substancia, mas com referencias "humanamente boas, tecnicamente ruins" — citacoes multilinha como frase unica, linhas de planilha ambiguas, faixas imprecisas. O validador corretamente rejeitou como AMBIGUO, gerando 3 rodadas onde 1 bastaria.

### O que sanear

**1. Atomizar referencias multilinha**
Se o `dado_citado` de uma referencia contiver informacao que no documento bruto esta distribuida em multiplas linhas, quebrar em referencias unitarias:
- ANTES: `"dado_citado": "Lucimaria, CPF 123.456.789-00, IP 187.38.209.15, modem Huawei"`
- DEPOIS: 4 referencias separadas, cada uma com sua `linha_ou_celula` especifica

**2. Padronizar referencias de planilha**
Toda referencia a XLSX deve incluir:
- `aba_planilha`: nome da aba
- `linha_ou_celula`: formato "Excel row N / col A-D" (nao indice de dataframe)
- Se a linha Excel real nao puder ser determinada, marcar explicitamente: "indice dataframe 2, linha Excel indeterminada"

**3. Ajustar faixas de linha para TXT**
Toda referencia a TXT deve usar faixa de linhas especifica:
- ANTES: `"linha_ou_celula": "pagina 5"`
- DEPOIS: `"linha_ou_celula": "linhas 5205-5209"`

**4. Verificar coerencia dado vs texto_original**
Para cada referencia, confirmar que o `dado_citado` pode ser encontrado (literal ou normalizado) dentro do `texto_original` citado pelo extrator. Se nao, marcar para re-extracao antes de validar.

### Quando pular esta fase

Modo single (<50 paginas) com conclusoes que ja tenham referencias atomicas e especificas. Na duvida, executar — o custo e baixo e evita rodadas extras de validacao.

## 5. Validacao

Apos produzir TODAS as conclusoes e ANTES de relatar ao usuario:

### Quando validar
- **Sempre** no modo multi-agente (50+ paginas)
- **Opcional** no modo single (<50 paginas), mas recomendado para conclusoes criticas (indiciamento, convergencia de autoria)

### Como acionar

1. Gravar as conclusoes em arquivo JSON (formato secao 3 do schema)
2. Spawnar o subagente validador com:

```
Voce e o validador adversarial.
Leia o arquivo agents/validador.md para suas instrucoes completas.

ARQUIVO DE CONCLUSOES: [caminho/conclusoes.json]
DOCUMENTOS ORIGINAIS: [caminho/diretorio_documentos/]
SCRIPT DE EXTRACAO: scripts/extrator_verificacao.py

Valide CADA conclusao seguindo o processo descrito em agents/validador.md.
Retorne a saida no schema "Validacao" da secao 4 de references/schemas_multiagente.md.
Seu validador_id e: "validador_01"
```

## 6. Interpretacao

Apos receber o retorno do validador:

### Conclusoes VERIFICADO
- Incluir no relatorio/painel de status com confianca
- Manter as referencias e adicionar nota: "Verificado contra fonte bruta"

### Conclusoes CONTRADITO
- **Remover do relatorio** — nao relatar ao usuario como conclusao
- Investigar a causa: o extrator errou? O agente principal interpretou errado?
- Se possivel, buscar a informacao correta e formular nova conclusao
- Registrar a contradicao em log interno para auditoria

### Conclusoes AMBIGUO
- **Nao incluir como conclusao firme** — marcar como "pendente de verificacao manual"
- Apresentar ao usuario com transparencia: "Esta conclusao nao pode ser verificada automaticamente porque [motivo]"
- Sugerir acao: re-processar com OCR de melhor qualidade, verificar documento fisico, solicitar novo documento ao orgao

## 7. Guardrails Obrigatorios

### 7.1 Circuit Breakers (prevencao de cascata de erros)

Se um agente fabricar um dado e o proximo agente tratar como fato, o erro se amplifica exponencialmente (hallucination cascade). Para prevenir:

- **Limiar de confianca**: se mais de 30% dos dados de um extrator vierem de OCR com qualidade "media" ou "baixa", pausar e pedir verificacao humana antes de cruzar
- **Limiar de contradicoes**: se o validador retornar mais de 50% de conclusoes como CONTRADITO, algo esta fundamentalmente errado — nao corrigir individualmente, re-avaliar toda a analise
- **Preferir parar a propagar**: quando em duvida, marcar como AMBIGUO e escalar para o usuario. Uma conclusao ausente e melhor que uma conclusao errada no relatorio

### 7.2 Limites de Iteracao (prevencao de loops)

Pesquisas mostram que 15.7% das falhas em sistemas multi-agente sao repeticao de passos (step repetition). Para prevenir:

- **Extratores**: maximo 1 passagem por lote. Se falhar, reportar erro — nao re-tentar automaticamente
- **Validador**: maximo 1 rodada de validacao por conjunto de conclusoes. Se o agente principal corrigir conclusoes, pode spawnar nova validacao, mas maximo 2 rodadas totais
- **Agente principal**: se apos 2 rodadas de validacao ainda houver conclusoes CONTRADITO, escalar para o usuario com transparencia

### 7.3 Trilha de Auditoria (obrigatoria para contexto forense)

A legislacao brasileira exige que ferramentas de IA forense sejam **verificaveis, auditaveis e replicaveis**. Usar o script `scripts/auditoria.py` para registrar cada acao de agente automaticamente:

```bash
# Registrar acao
python scripts/auditoria.py --log auditoria_IP2025_00847.log \
  --acao "Extracao de dados bancarios" \
  --agente "extrator_bancario_01" \
  --entrada extrato_bradesco.pdf \
  --saida resultado_bancario.json \
  --modelo "claude-opus-4-6" \
  --documentos "extrato_bradesco.pdf,comprovantes_pix.pdf"

# Verificar integridade do log (cadeia de hashes)
python scripts/auditoria.py --log auditoria_IP2025_00847.log --verificar

# Resumo do log
python scripts/auditoria.py --log auditoria_IP2025_00847.log --resumo
```

O script gera log append-only onde cada registro inclui o hash SHA256 do registro anterior (cadeia de hashes). Se qualquer linha for alterada ou removida, `--verificar` detecta a adulteracao.

### 7.4 Escalacao Humana

O validador pode estar errado em ~9% dos casos (dado de pesquisa: MAST taxonomy, Berkeley/IBM, 2025). Para conclusoes de alto impacto, adicionar verificacao humana:

- **Sempre escalar para o usuario**: conclusoes de autoria (quem fez o crime), convergencias que sustentam indiciamento, identificacao de laranjas
- **Escalar quando ambiguo**: qualquer conclusao com veredicto AMBIGUO apos 2 rodadas
- **Formato de escalacao**: apresentar ao usuario a conclusao, as referencias, o texto bruto extraido pelo validador, e o veredicto — para que o usuario possa conferir visualmente

## 8. Anti-Patterns

### NAO faca

- **Spawnar mais de 6 extratores em paralelo** — o custo de tokens supera o beneficio e a consolidacao fica complexa demais. Se tem mais de 6 lotes, agrupe lotes menores.

- **Validar conclusoes triviais** — "O BO foi registrado na data X" nao precisa de validacao adversarial. Valide apenas conclusoes que envolvem cruzamento, convergencia ou atribuicao de autoria.

- **Re-spawnar o validador para as mesmas conclusoes** — se o validador disse CONTRADITO, nao rode de novo esperando resultado diferente. Corrija a conclusao e rode uma nova validacao.

- **Confiar no extrator cegamente** — o extrator pode ter omitido dados (OCR falhou, pagina pulada). Se uma convergencia esperada nao aparece, verificar se os documentos foram processados completamente.

- **Processar documentos duplicados** — antes de dividir em lotes, verificar se o mesmo arquivo aparece mais de uma vez. Hashes ajudam.

- **Misturar documentos de naturezas diferentes no mesmo extrator** — um extrator que recebe ao mesmo tempo um extrato bancario e um depoimento vai ter performance pior do que dois extratores especializados.

- **Spawnar subagentes para menos de 50 paginas** — o overhead de criar, consolidar e validar nao compensa. Use agente unico.
