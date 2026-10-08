# RELATÓRIO DE MISSÃO POLICIAL — TEMPLATE

## Estrutura do Documento .docx

Este template define a estrutura e conteúdo obrigatório do Relatório de Missão Policial.
Destinado ao Ministério Público e ao Judiciário como subsídio ao Relatório Final do Delegado.
Produzido pelo Agente/Investigador de Polícia Civil responsável pela missão investigativa.

**Diferença fundamental em relação ao Relatório Final**: este documento NÃO tipifica penalmente,
NÃO conclui sobre indiciamento e NÃO faz análise jurídica. Foca em materialidade, autoria e
sugestão de diligências. A tipificação e a conclusão jurídica pertencem ao Relatório Final.

Gerar com o script compartilhado:

```bash
python scripts/gerar_docx_relatorio.py \
  --input relatorio_missao.md \
  --output relatorio_missao_IP<numero>.docx \
  --template assets/template_pcrn_drcc.docx \
  --ip-numero "<numero do IP>" \
  --footer-text "Rel. Missão — IP n. <numero>"
```

---

### Configurações do Documento

```
Página: A4
Margens: Superior 3cm, Inferior 2cm, Esquerda 3cm, Direita 2cm (padrão ABNT)
Fonte: Times New Roman 12pt
Espaçamento: 1,5 entrelinhas
Alinhamento: Justificado
Recuo primeira linha: parágrafos corridos
```

---

### Cabeçalho Institucional

```
POLÍCIA CIVIL DO ESTADO DO RIO GRANDE DO NORTE
DIRETORIA DE POLÍCIA DA GRANDE NATAL — DPGRAN
DELEGACIA ESPECIALIZADA EM REPRESSÃO A CRIMES CIBERNÉTICOS — DRCC
```

---

### Endereçamento

```
EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) DELEGADO(A) DE POLÍCIA CIVIL
[titular da unidade responsável pelo IP]

ou, conforme determinação:

EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) PROMOTOR(A) DE JUSTIÇA
[da Xª Promotoria de Justiça de ____]
```

---

### Dados do Procedimento (em negrito)

```
Inquérito Policial nº: ___
Investigado(s): ___
Missão: ___
Agente Responsável: ___ | Matrícula: ___
Data de início da missão: ___
Data do relatório: ___
```

---

### Preâmbulo

```
O AGENTE DE POLÍCIA CIVIL [nome], matrícula nº [nº], lotado(a) na
[unidade], no exercício de suas atribuições legais, vem, respeitosamente,
apresentar o RELATÓRIO DE MISSÃO POLICIAL referente ao Inquérito Policial
em epígrafe, com o objetivo de registrar as diligências realizadas,
os elementos probatórios colhidos, e subsidiar o Relatório Final
a cargo do Delegado(a) de Polícia responsável, nos termos que seguem:
```

---

### Seções Obrigatórias

#### I — ORIGEM DA INVESTIGAÇÃO

- Boletim de Ocorrência, número, data, delegacia de registro
- Instauração do IP: número, data, portaria
- Natureza da missão atribuída ao agente
- Resumo da notícia-crime

#### II — QUALIFICAÇÃO DO(S) INVESTIGADO(S)

Para cada investigado:
- Nome completo e alcunha (se houver)
- Filiação, data de nascimento, idade
- CPF, RG (órgão expedidor)
- Naturalidade, nacionalidade, estado civil, profissão
- Endereço completo, telefone(s) de contato
- Antecedentes criminais (SINESP/INFOSEG)
- Situação processual atual

#### III — QUALIFICAÇÃO DA(S) VÍTIMA(S)

Para cada vítima:
- Nome completo
- CPF, data de nascimento, profissão
- Endereço, telefone
- Valor do prejuízo sofrido
- Resumo do relato (com referência à folha dos autos)

#### IV — DESCRIÇÃO DOS FATOS

- Narrativa cronológica e detalhada dos fatos apurados
- Datas, horários e locais precisos
- Modus operandi identificado
- Fluxo do dinheiro (origem → destino)
- Consequências e prejuízos totais

#### V — DILIGÊNCIAS REALIZADAS

**A) Oitivas e Depoimentos**
- Data | Ouvido | Qualificação | Síntese | Folha(s) dos autos

**B) Requisições e Respostas Obtidas**
- Órgão requisitado | Data ofício | Data resposta | Dados obtidos | Folha(s)

**C) Quebras de Sigilo Autorizadas**
- Tipo (telemático/bancário) | Autorização judicial | Data | Dados obtidos

**D) Buscas e Apreensões**
- Data | Local | O que foi apreendido | Auto de apreensão (folha)

**E) Análises e Cruzamentos Realizados**
- Metodologia de cruzamento de IPs (com referência a `references/metodologia_ip.md`)
- Expansão de rede realizada (com referência a `references/expansao_rede.md`)
- Fontes cruzadas: lista de fontes com resultado do cruzamento

**F) Outras Diligências**
- Demais atos investigativos com data, descrição e resultado

#### VI — MATERIALIDADE DELITIVA

Elementos probatórios que comprovam a ocorrência do fato delituoso:

| Nº | Elemento de Prova | Descrição | Localização nos Autos |
|----|-------------------|-----------|----------------------|
| 1  | [tipo de prova] | [descrição] | [folha(s)] |

Para cada elemento: indicar se VERIFICADO pelo validador adversarial (se processado em modo multi-agente).

#### VII — AUTORIA

**A) Indícios de Autoria**

Enumerar cada indício com:
- Descrição do indício
- Fonte (documento + folha)
- Status de verificação adversarial (VERIFICADO / PENDENTE)

**B) Análise de Convergência**

Baseada em `references/estabelecimento_autoria.md`:

| Fonte | Dado | Converge em | Status |
|-------|------|-------------|--------|
| [origem] | [IP/IMEI/nome] | [suspeito] | VERIFICADO/AMBÍGUO |

Grau de robustez da convergência: [1 fonte insuficiente / 2 fontes fraco / 3+ fontes robusto]

**C) Hipóteses Investigativas Avaliadas**

| Hipótese | Evidências a favor | Evidências contra | Status |
|----------|-------------------|-------------------|--------|
| H1: [suspeito X como operador direto] | [...] | [...] | [confirmada/refutada/aberta] |
| H2: [laranja/intermediário] | [...] | [...] | [confirmada/refutada/aberta] |

**D) Laranjas Identificados**

Para cada laranja: qualificação, papel na cadeia, grau de conivência apurado.

#### VIII — ANÁLISE DAS PROVAS

**A) Provas Testemunhais**
- Avaliação de credibilidade e consistência entre depoimentos
- Contradições identificadas e análise

**B) Provas Documentais**
- Análise dos documentos obtidos e seu valor probatório

**C) Provas Digitais**
- Metodologia de coleta e cadeia de custódia (refs. `references/cadeia_custodia.md`)
- Hash SHA256 dos arquivos digitais (quando aplicável)
- Resultado das verificações adversariais (se modo multi-agente)

**D) Provas Periciais**
- Laudos existentes, referência e conclusões relevantes

**E) Limitações Probatórias**
- Provas que não puderam ser obtidas e motivo
- Provas com valor probatório reduzido e justificativa

#### IX — CONTRADIÇÕES E PONTOS DE ATENÇÃO

- Contradições entre versões (investigados, vítimas, documentos)
- Hipóteses concorrentes ainda em aberto
- Elementos que podem ser explorados pela defesa
- Análise crítica dos pontos frágeis da investigação

*Não omitir fragilidades — o relatório deve ser uma análise honesta, não advocacy.*

#### X — DILIGÊNCIAS PENDENTES

Diligências já requisitadas mas sem retorno:

| Diligência | Ofício nº | Data | Status | Urgência |
|------------|-----------|------|--------|----------|
| [o que] | [nº] | [data envio] | aguardando | IMEDIATA/CURTO/ESTRATÉGICO |

#### XI — SUGESTÃO DE NOVAS DILIGÊNCIAS

Diligências ainda não realizadas que se mostram necessárias para:
- Confirmar autoria (indicar qual hipótese cada diligência testa)
- Fortalecer materialidade
- Esclarecer contradições identificadas
- Expandir a rede de investigados

| Nº | Diligência sugerida | Fundamento | Objetivo | Urgência |
|----|---------------------|------------|----------|----------|
| 1  | [ex: requisitar ERB da operadora X] | [dados de IP sugerem uso de celular na região] | [confirmar presença física no local] | CURTA PRAZO |

*Esta seção é de natureza sugestiva. A decisão sobre quais diligências autorizar pertence ao Delegado de Polícia.*

#### XII — SÍNTESE INVESTIGATIVA

**Status da materialidade**: [COMPROVADA / PARCIALMENTE COMPROVADA / NÃO COMPROVADA]
- Síntese dos elementos que sustentam essa conclusão

**Status da autoria**: [ESTABELECIDA / PARCIALMENTE ESTABELECIDA / NÃO ESTABELECIDA]
- Em relação a cada investigado: grau de convergência probatória
- Fontes que convergem: [lista]
- Lacunas probatórias remanescentes: [lista]

**Estado geral da investigação**: [CONCLUÍDA PARA RELATÓRIO FINAL / EM ANDAMENTO / BLOQUEADA POR ___]

*Esta síntese não constitui conclusão jurídica. Não há tipificação, não há juízo de indiciamento.
A conclusão jurídica pertence ao Relatório Final, de responsabilidade exclusiva do Delegado de Polícia.*

#### XIII — DISPOSIÇÕES FINAIS

```
O presente Relatório de Missão Policial foi elaborado com observância
aos princípios da legalidade, imparcialidade e completude investigativa.

Todas as conclusões relativas à autoria estão baseadas em convergência
de fontes independentes, verificadas contra documentos brutos.
As limitações probatórias foram expressamente indicadas.

Os elementos de prova encontram-se devidamente documentados nos autos,
com indicação precisa de sua localização e cadeia de custódia preservada.

Coloco-me à disposição para prestar quaisquer esclarecimentos.
```

---

### Fechamento

```
É o relatório.

[Cidade], [data por extenso].

[Nome do Agente de Polícia Civil]
Agente de Polícia Civil | Matrícula nº [nº]
[Unidade Policial]
```

---

## Regras de Formatação e Entrega

1. **Formato**: sempre `.docx` — jamais entregar Markdown como documento final
2. **Emojis e ícones**: PROIBIDOS no corpo do documento — este é documento judicial
3. **Painéis de status** (✅/❌/🔄): restritos ao uso operacional interno, NUNCA no documento formal
4. **Referência de folhas**: sempre que possível, indicar folha(s) dos autos
5. **Campos em branco**: marcar como "Não informado" ou "Não apurado" — nunca deixar vazio
6. **Diagramas**: quando fluxos de dinheiro ou vínculos ganham clareza com visualização, gerar
   em Mermaid e inserir como imagem no `.docx` — nunca deixar código Mermaid cru no documento
7. **Completude antes da entrega**: se faltarem dados institucionais obrigatórios (nº IP, agente
   responsável, matrícula, unidade), perguntar antes de gerar — não preencher com placeholder
8. **Bullet points — quando usar (obrigatório)**:
   - Endereços para cumprimento de mandado de busca e apreensão
   - Terminais telefônicos e e-mails alvos de interceptação ou quebra telemática
   - CPFs, CNPJs e contas bancárias alvos de quebra de sigilo
   - Período e escopo delimitado de cada medida cautelar
9. **Bullet points — quando NÃO usar**:
   - Narrativa factual corrida (fatos, modus operandi, cronologia)
   - Fundamentação jurídica e motivação das medidas
   - Seções de conclusão e síntese investigativa
   - Qualquer parágrafo que flua naturalmente em prosa
10. **Mermaid — quebra de linha em labels**: usar SEMPRE `<br/>` — NUNCA `\n` (o `\n` literal
    é renderizado como "n/n/" nas imagens PNG geradas para inserção no `.docx`)

## Checklist de Qualidade Antes de Entregar

**Forma:**
- [ ] Cabeçalho institucional correto (PCRN/DPGRAN/DRCC)
- [ ] Endereçamento adequado ao destinatário
- [ ] Dados do IP e agente preenchidos
- [ ] Todas as seções presentes (I a XIII)
- [ ] Nenhum emoji ou ícone de status no corpo
- [ ] Fechamento com assinatura e data

**Conteúdo:**
- [ ] Narrativa cronológica coerente (seção IV)
- [ ] Materialidade sustentada por provas concretas com referência de folha
- [ ] Autoria analisada com grau de convergência explícito
- [ ] Hipóteses concorrentes avaliadas (seção VII-C)
- [ ] Limitações probatórias declaradas (seção VIII-E)
- [ ] Contradições apontadas (seção IX)
- [ ] Sugestões de diligências fundamentadas (seção XI)
- [ ] Síntese sem tipificação ou juízo de indiciamento (seção XII)

**Proibições:**
- [ ] ZERO tipificação penal
- [ ] ZERO conclusão sobre indiciamento ou não indiciamento
- [ ] ZERO análise de prescrição
- [ ] ZERO análise de excludentes de ilicitude
- [ ] ZERO referência a "art." de lei penal em seção de conclusão
- [ ] ZERO menção a IA, sistema multi-agente, validação adversarial, trilha de auditoria ou qualquer ferramenta computacional de análise — **este documento é peça judicial assinada por agente humano; mencionar IA contamina a cadeia de custódia, expõe a defesa a questionar toda a prova e pode anular o ato**
