---
name: cease-desist-bossmann007
title: /cease-desist
description: Draft uma notificação extrajudicial (modo envio) ou faça a triagem de uma recebida (modo recebimento). Use para fazer valer direitos contra um infrator com carta de cobrança calibrada à postura de enforcement, ou quando uma notificação recebida precisa virar memorando estruturado de opções com recomendação.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/ip-legal/skills/cease-desist
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: ip
language: pt
---

# /cease-desist

Dois modos. Escolha um:

- `/ip-legal:cease-desist --send` — redige notificação extrajudicial calibrada à postura de enforcement. Gate alto roda antes do envio.
- `/ip-legal:cease-desist --receive` — triagem de notificação recebida. Produz memorando de opções com recomendação.

## Instructions

1. **Leia o perfil de prática.** Carregue `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`. Se contiver marcadores `[PLACEHOLDER]` ou não existir, pare e diga: "Este plugin precisa de setup antes de gerar output útil. Rode `/ip-legal:cold-start-interview` — o skill de notificação depende da sua postura de enforcement, matriz de aprovação e mix de área de prática, nenhum configurado ainda."

2. **Verifique matter workspaces.** Conforme `## Matter workspaces`: se `Enabled` é `✗`, pule — skills usam contexto de nível de prática. Se habilitado e não há matter ativo, pergunte: "Para qual matter é isso? Rode `/ip-legal:matter-workspace switch <slug>` ou diga `practice-level`."

3. **Dispatch em `$ARGUMENTS`:**
   - Se `--send` presente: rode modo envio (abaixo). Percorra identificar-o-direito, identificar-a-conduta, identificar-a-relação, identificar-a-demanda, calibrar-à-postura, redigir, e o gate pré-envio.
   - Se `--receive` presente: rode modo recebimento (abaixo). Peça a carta recebida (path ou texto colado), depois avalie, identifique exposição, apresente opções, e escreva o memorando de triagem.
   - Se nenhuma flag presente: pergunte uma vez — "Estamos enviando uma notificação extrajudicial (nós afirmamos direito) ou fazendo triagem de uma recebida (nós nos defendemos)?" — e então faça dispatch.

4. **Respeite o gate.** No modo envio, o gate alto roda antes de qualquer draft final ser escrito em disco. Não pule.

5. **Respeite a matriz de aprovação.** Puxe o aprovador da linha de notificação de `## Postura de enforcement → Matriz de aprovação`. Puxe escalonamentos automáticos. Mostre ambos no gate; não os esconda.

6. **Faça handoff quando apropriado.** No modo recebimento, se a recomendação é responder firmemente, ofereça encadear em `/ip-legal:cease-desist --send` pré-populado com contexto de resposta. Se a recomendação é antecipar com ação declaratória negativa ou processo de nulidade no INPI, escale para escritório externo conforme a linha de contencioso de PI do perfil de prática — não redija.

## Examples

```
/ip-legal:cease-desist --send
/ip-legal:cease-desist --receive ~/Downloads/notificacao-recebida-acme.pdf
/ip-legal:cease-desist
```

## Notes

- A notificação de saída não carrega o cabeçalho de trabalho protegido por sigilo. O draft interno, o briefing pré-envio e o memorando de triagem carregam.
- Direito marcário é territorial; o draft assume as jurisdições declaradas no `Registrado em:` do perfil de prática (Brasil via INPI, mais qualquer registro estrangeiro/Protocolo de Madrid via Decreto 10.033/2019). Se a conduta ou contraparte estiver em outro país, sinalize antes de redigir.
- Todo `[CITE:___]` é não verificado até rodada em citador/pesquisa jurisprudencial. Tags de atribuição de fonte permanecem no draft.
- Usuários não-advogados recebem briefing de uma página para a conversa com o advogado antes do gate liberar.

---

## Purpose

Uma notificação extrajudicial afirma um direito legal e exige que alguém pare de fazer algo. É uma das cartas mais consequentes que uma prática de PI envia ou recebe. Enviar uma é um primeiro passo rumo a litígio — o destinatário pode ajuizar ação declaratória negativa em foro de sua escolha, e afirmações desproporcionais ou de má-fé podem ser usadas contra quem enviou (litigância de má-fé, CPC art. 80). Receber uma inicia um prazo e força uma decisão. Este skill trata os dois lados com as salvaguardas que a decisão exige.

Dois modos:

- `--send` — você está afirmando. Redija notificação calibrada à postura, gate antes da entrega.
- `--receive` — você está se defendendo. Triagem da carta recebida, produza memorando de opções, roteie para criação de matter se justificado.

Se o usuário não passar flag, pergunte uma vez: "Estamos enviando uma notificação extrajudicial (nós afirmamos direito) ou fazendo triagem de uma recebida (nós nos defendemos)?"

> **Entregável externo (modo envio):** a notificação redigida é enviada à contraparte. NÃO inclua o cabeçalho `SIGILOSO — TRABALHO PROTEGIDO POR SIGILO PROFISSIONAL` na carta de saída. Drafts internos, briefings pré-envio e memorandos de triagem mantêm o cabeçalho conforme config do plugin `## Outputs`.

## Premissa de jurisdição

Direito marcário é territorial — um registro no INPI não viaja automaticamente para outro país (ressalvada a marca notoriamente conhecida, art. 126, Lei 9.279/1996, e a Convenção da União de Paris art. 6º bis). Direito autoral é regido pela Convenção de Berna (proteção automática multilateral), mas a execução é específica de cada jurisdição. Este skill assume a jurisdição declarada no matter ou no `Registrado em:` do perfil de prática. Se a conduta infratora, a contraparte, ou o foro estiver em outro lugar, sinalize — o draft pode não se aplicar como redigido.

## Load context

- `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` → `## Postura de enforcement` (postura, gatilhos de notificação, critérios de carta branda, matriz de aprovação, escalonamentos automáticos), `## Perfil de prática (PI)` (mix de área de prática, jurisdições registradas, roster de escritórios externos), `## Outputs` (cabeçalho de trabalho protegido, papel), `## Quem está usando isso` (papel — advogado vs. não-advogado)
- Qualquer template de notificação ou playbook de enforcement referenciado nos documentos-semente do perfil de prática — leia e siga a estrutura
- **Contexto de matter.** Verifique `## Matter workspaces` no CLAUDE.md de nível de prática. Se `Enabled` é `✗` (padrão para usuários in-house), pule a maquinaria de matter — skills usam contexto de nível de prática. Se habilitado e não há matter ativo, pergunte: "Para qual matter é isso? Rode `/ip-legal:matter-workspace switch <slug>` ou diga `practice-level`." Carregue o `matter.md` do matter ativo para overrides específicos (ex.: override de postura, override de aprovador). Escreva outputs na pasta do matter em `~/.claude/plugins/config/claude-for-legal/ip-legal/matters/<matter-slug>/`. Nunca leia arquivos de outro matter a menos que `Cross-matter context` esteja `on`.

## Modo envio — redigindo a notificação

### Passo 1: Identificar o direito

Pergunte, em um bloco:

> Qual direito de PI estamos afirmando?
>
> - **Marca** — está registrada? Onde (INPI, e/ou estrangeiro — USPTO, EUIPO, etc.)? Número de registro e classe(s) NCL? Ou apenas uso de fato (data do primeiro uso, escopo geográfico — sem proteção de marca de alto renome nem notoriamente conhecida)?
> - **Direito autoral** — obra registrada na Biblioteca Nacional / Escola de Belas Artes (opcional no Brasil, proteção é automática pela Lei 9.610/1998 art. 18) ou não registrada? Título, data de criação, evidência de autoria?
> - **Ambos** — identifique cada um.

Registre cada direito. Direitos registrados são citados pelo número no INPI. Direitos de uso de fato recebem o parágrafo de evidência de primeiro uso. Direito autoral não registrado no Brasil ainda tem proteção plena (Lei 9.610/1998 art. 18, "a proteção aos direitos... independe de registro") — diferente do regime americano, não há flag de "precisa registrar antes de processar". [verified: https://www.planalto.gov.br/ccivil_03/leis/l9610.htm]

### Passo 2: Identificar a conduta

> Descreva a conduta infratora com especificidade, não adjetivos:
>
> - **Quem** está fazendo — nome da entidade, indivíduo, handle de plataforma?
> - **O quê** — a marca acusada, a cópia acusada, o produto acusado? Anexe ou descreva amostras.
> - **Onde** — URL do site, anúncio em marketplace, varejo físico, rede social?
> - **Desde quando** — data da primeira observação, data do uso mais antigo documentável?
> - **Evidência** — screenshots, recibos, monitoramento de mercado, denúncias de confusão de consumidor?

Fatos entram específicos. "Você vendeu o produto X em [URL] com a marca [Y] em [data]" é melhor que "você vem infringindo nossos direitos." Adjetivos denunciam registro factual fraco.

### Passo 3: Identificar a relação

> Qual a relação entre nós e o destinatário?
>
> - **Concorrente** (direto ou adjacente) — postura padrão se aplica
> - **Revendedor / parceiro de canal** — tom se ajusta; considere o caminho de carta branda
> - **Ex-licenciado / ex-funcionário / ex-parceiro** — cláusulas contratuais provavelmente se aplicam; cite-as
> - **Estranho / infrator aleatório** — padrão
> - **Cliente atual / parceiro** — escalonamento automático conforme perfil de prática; sinalize antes de redigir

Isso muda o tom, o aprovador, e se redigir sem escalonamento é sequer apropriado.

### Passo 4: Identificar a demanda

> O que o cliente realmente quer?
>
> - **Parar** — cessar o uso infrator
> - **Prestar contas** — reportar vendas, lucros, volumes (para base de indenização)
> - **Destruir** — destruir ou recolher estoque infrator
> - **Indenização** — acordo pecuniário (Lei 9.279/1996 art. 208-210 para danos materiais/morais em PI)
> - **Transferir / ceder** — transferir domínio, entregar a conta, ceder a marca ou obra acusada
> - **Correção pública** — remoção de conteúdo, declaração pública
> - **Confirmação por escrito** — compromisso de conformidade até data

Escolha os remédios reais. A demanda deve ser proporcional ao dano — demanda desproporcional é evidência de má-fé se o caso for litigado (litigância de má-fé, CPC art. 80; abuso de direito, Código Civil art. 187). [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm; https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm]

**Caminho paralelo de takedown de canal (infração em marketplace).** Se a conduta acusada está em marketplace (Mercado Livre, Amazon, Shopee, Etsy, eBay, Alibaba, TikTok Shop, AliExpress), sinalize o canal de denúncia de PI da plataforma como caminho paralelo mais rápido e barato que não exige notificação nem litígio:

- **Mercado Livre — Denúncia de Propriedade Intelectual** (programa de proteção à marca)
- **Amazon Brand Registry** (takedown de marca e direito autoral, remoção de falsificação)
- **Shopee — canal de denúncia de PI**
- **Etsy IP Infringement reporting** (formulários de marca / direito autoral / patente)
- **eBay VeRO** (Verified Rights Owner program)
- **Alibaba IPP** (IP Protection Platform)
- **TikTok Shop IP Protection**

Um takedown de marketplace muitas vezes resolve em dias; uma notificação extrajudicial dá tempo ao infrator para vender o estoque enquanto negocia. Os dois caminhos não são mutuamente exclusivos — recomende registrar ambos quando a conduta é baseada em marketplace, com a notificação cobrindo conduta fora da plataforma (site próprio, atacado, redes sociais, varejo físico) que a denúncia da plataforma não alcança. Anote no briefing pré-envio se o caminho paralelo foi registrado, está em fila, ou foi recusado (e por quê).

### Passo 5: Calibrar à postura

Leia `## Postura de enforcement` → `Postura padrão:` e aplique:

- **Agressiva** — carta firme, prazo curto (frequentemente 7–14 dias), linguagem explícita de consequência (ação judicial, indenização, honorários, tutela de urgência), sem suavização de acordo
- **Moderada** — firme mas profissional, prazo padrão (14–30 dias), consequências citadas sem teatralidade, abertura a diálogo se responderem
- **Conservadora** — enquadramento de carta branda, prazo mais longo ou sem prazo rígido, abertura de "gostaríamos de discutir", linguagem de consequência atenuada ou ausente

Leia também `Quando enviamos notificação`, `Quando enviamos carta branda primeiro`, e `Quando apenas ajuizamos`. Se os fatos sugerirem que deveria ser carta branda ou ajuizamento direto conforme o perfil de prática, sinalize antes de redigir: "Conforme sua postura de enforcement, este padrão combina com [carta branda / ajuizamento]. Ainda quer uma notificação, ou prefere [alternativa]?"

Overrides em nível de matter no `matter.md` prevalecem sobre o padrão de prática.

### Passo 5.5: Diligência da contraparte — PRÉ-REQUISITO OBRIGATÓRIO

**Antes de redigir, rode diligência da contraparte e apresente os resultados ao usuário.** Isso não é condicional a "se a contraparte parecer grande." Toda afirmação em notificação extrajudicial carrega exposição a ação declaratória negativa / inversão de ônus / má-fé calibrada a *quem* é o destinatário. O skill não redige notificação até o usuário ver a diligência e confirmar que ainda quer comprar essa briga.

Colete e apresente — em um bloco, para aprovação do usuário — o seguinte:

- **Entidade legal** — razão social exata, CNPJ, UF de constituição, nome fantasia se houver. Registro de marca no INPI; busca na Junta Comercial (Lei 8.934/1994); documentos públicos se sociedade anônima (Lei 6.404/1976). Sinalize `[SME VERIFY]` se a fonte não for confirmada.
- **Porte e recursos** — headcount aproximado, faixa de faturamento se público, financiamento se startup, controladora se subsidiária. Fontes públicas (LinkedIn, imprensa, Receita Federal/CNPJ público). Sinalize honestamente se o porte não puder ser determinado.
- **Portfólio de PI** — eles têm marcas, patentes, ou direitos autorais registrados em classes adjacentes? Uma contraparte com portfólio próprio é mais provável de (a) entender a postura, (b) contra-afirmar, e (c) ajuizar ação declaratória negativa. Busca rápida na base do INPI sobre a entidade acusada e afiliadas.
- **Histórico de litígio** — busca rápida em JusBrasil / consulta processual (TJs, TRFs) para litígio de PI anterior como autor ou réu. Litigante contumaz ou propenso a ação declaratória negativa muda o cálculo. Sinalize campanhas de notificação anteriores no setor.
- **Advogado** — têm advogado externo de PI conhecido? Escritório, sócio responsável se identificável de processos anteriores. "Sem advogado no registro" já é um dado.
- **Risco de autor em ação declaratória negativa** — dado porte, portfólio de PI, histórico de litígio, e advogado: essa é uma contraparte propensa a receber uma notificação como convite para ajuizar ação declaratória negativa em foro de sua escolha? Sinalize alto / médio / baixo com uma frase de razão.
- **Risco de relacionamento** — somos clientes deles, compartilhamos investidores, são potencial adquirente ou parceiro? "Não é cliente" confirmado pelo perfil de prática; qualquer outra coisa sinalizada.

Apresente como memorando curto no chat ANTES do draft:

```
## Diligência de contraparte — [Nome da Entidade]

- **Entidade:** [razão social, UF de constituição, controladora se houver]
- **Porte:** [faixa de headcount, faixa de faturamento, estágio de financiamento] — [fonte, `[SME VERIFY]` onde aplicável]
- **Portfólio de PI:** [marcas / patentes / direitos autorais registrados em classes adjacentes — ou "nenhum encontrado"]
- **Histórico de litígio:** [casos de PI anteriores como autor ou réu — ou "nenhum encontrado em busca rápida"]
- **Advogado:** [advogado externo de PI conhecido — ou "nenhum identificado"]
- **Risco de autor em ação declaratória:** [alto / médio / baixo — razão]
- **Risco de relacionamento:** [qualquer sobreposição de cliente / investidor / parceiro / adquirente — ou "nenhum identificado"]

**Escalonamentos automáticos que isso dispara** (conforme perfil de prática `## Postura de enforcement` → Escalonamentos automáticos):
- [liste cada gatilho que essa diligência revela]

**Confirme antes de eu redigir:**
- Quer prosseguir com uma notificação contra essa contraparte, dada a diligência acima?
- Algum dos escalonamentos automáticos se aplica? Se sim, o aprovador nomeado no perfil confirma antes de redigir, não depois.
```

**Não avance para o Passo 6 (Draft) até o usuário se engajar com o bloco de diligência.** Um "ok" em branco é pior que nenhuma confirmação — insista: "Antes de eu redigir — algo na diligência muda o cálculo? Porte, litígio anterior, o advogado deles, relacionamento?"

Se a diligência revelar algo na lista de escalonamento automático do perfil de prática (cliente, contraparte maior, matter de patente, atrai imprensa, etc.), roteie ao aprovador nomeado conforme o perfil — não redija em nome do revisor até o aprovador confirmar prosseguimento.

Se itens críticos de diligência não puderem ser respondidos (ex.: entidade não pode ser confirmada, porte desconhecido e a contraparte não está em nenhum registro público), diga isso e sinalize: "Não consigo confirmar [entidade / porte / advogado] com as fontes disponíveis. Você tem isso, ou devemos pausar até um paralegal ou escritório externo confirmar?"

### Passo 6: Draft

Estrutura do draft:

1. **Remetente / papel timbrado e data**
2. **Bloco do destinatário**
3. **Linha de referência** — concisa, não revela estratégia sigilosa. `Ref.: Uso não autorizado de [MARCA] (Registro INPI nº [•])`
4. **Abertura** — identifica o remetente, o direito, o registro (se houver), e o fato da carta
5. **O direito** — marca: nº de registro, classe NCL, data de primeiro uso, status do registro; direito autoral: data de criação, registro se houver, descrição da obra; uso de fato: data de primeiro uso, escopo geográfico, evidência de distintividade adquirida
6. **A conduta infratora** — específico: quem, o quê, onde, quando, evidência
7. **O fundamento legal** — `[CITE: Lei 9.279/1996 art. 129 / art. 189 e ss. / Lei 9.610/1998 art. 102 e ss. / Código Civil art. 187]` conforme aplicável
8. **A demanda** — numerada, específica, proporcional
9. **O prazo** — data-calendário, método de confirmação
10. **Consequências do descumprimento** — calibradas à postura
11. **Demanda de preservação** — documentos, comunicações, metadados relacionados à conduta acusada
12. **Reserva de direitos** — "sem renúncia a quaisquer direitos ou ações, judiciais ou extrajudiciais"
13. **Bloco de assinatura** — aprovador conforme perfil de prática

**Regras de redação:**

- **Especificidade sobre adjetivos.** Datas, URLs, números de registro, amostras. Adjetivos são sinal de que os fatos são fracos.
- **Sem afirmações desproporcionais.** Se a marca está registrada em uma classe e o uso acusado é em classe diferente, diga isso — não finja que o registro cobre ambas (regra da especialidade, salvo alto renome ou notoriamente conhecida). Notificações desproporcionais são evidência de má-fé e podem sustentar litigância de má-fé (CPC art. 80) ou abuso de direito (Código Civil art. 187). [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm; https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm] [unverified: not found in primary source]
- **Citações como placeholders até verificadas.** `[CITE: Lei 9.279/1996 art. 129]` permanece como placeholder a menos que o usuário forneça a citação ou uma ferramenta de pesquisa retorne. Marque toda citação com fonte — `[JusBrasil]`, `[fornecido pelo usuário]`, `[conhecimento do modelo — verificar]`, `[busca web — verificar]`. Nunca remova as tags.
- **Linguagem de consequência combina com postura.** Agressiva → relief específico ameaçado (tutela de urgência, indenização por danos materiais e morais nos termos da Lei 9.279/1996 arts. 208-210 / Lei 9.610/1998 art. 102 e ss., honorários sucumbenciais). Moderada → "reservamo-nos todos os direitos." Conservadora → "gostaríamos de discutir antes de considerar outras medidas."
- **Ganchos específicos de jurisdição** — se Brasil, atente para disputa de domínio via SACI-Adm (registro.br) para casos de cybersquatting, crimes contra a propriedade industrial (Lei 9.279/1996 arts. 189-195) para uso indevido de marca, ação de abstenção de uso c/c perdas e danos (arts. 207-210). Fora do Brasil: sinalize o foro e anote que o draft pode precisar de revisão por correspondente estrangeiro.

### Passo 7: O gate alto antes da entrega

Antes de apresentar o draft no chat ou escrever o .docx, exiba este gate verbatim. **O usuário deve se engajar com ele** — reconhecimento em branco é pior que nenhum gate.

```
┌─────────────────────────────────────────────────────────────┐
│  ANTES DESSE DRAFT IR PARA QUALQUER LUGAR                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Isto é um draft para revisão de advogado — não uma carta   │
│  pronta para envio. Enviar uma notificação extrajudicial é  │
│  afirmação de direitos legais com consequências reais:      │
│                                                             │
│  • Pode disparar ação declaratória negativa em foro de      │
│    escolha do destinatário. Uma contraparte bem financiada  │
│    pode usar a notificação como convite para escolher um    │
│    foro hostil.                                              │
│                                                             │
│  • Afirmações desproporcionais ou de má-fé podem ser usadas │
│    contra quem envia — litigância de má-fé (CPC art. 80),   │
│    abuso de direito (Código Civil art. 187), honorários     │
│    sucumbenciais.                                            │
│                                                             │
│  • Inicia uma disputa que pode não se resolver barato.      │
│                                                             │
│  Confirme antes da carta sair:                               │
│                                                             │
│    1. Os direitos afirmados são válidos — registrados       │
│       (extraídos do INPI, não presumidos) ou sólidos em     │
│       uso de fato com evidência de distintividade adquirida.│
│    2. A alegação é plausível — um profissional razoável a   │
│       faria com base nesses fatos.                          │
│    3. A demanda é proporcional — pedimos o relief que a     │
│       conduta justifica, não tudo.                          │
│    4. Quem tem autoridade para iniciar uma disputa aprovou. │
│    5. A diligência de contraparte (Passo 5.5) foi           │
│       apresentada e confirmada — entidade, porte,           │
│       portfólio de PI, litígio anterior, advogado, risco de │
│       ação declaratória negativa, e risco de relacionamento.│
│       Não condicional. Obrigatório.                          │
│                                                             │
│  Aprovador conforme seu perfil de prática: [nome/papel do   │
│  aprovador da Postura de enforcement → Matriz de aprovação  │
│  → linha de notificação]                                    │
│                                                             │
│  Escalonamentos automáticos aplicáveis aqui: [liste         │
│  qualquer um do perfil de prática que este matter dispara — │
│  cliente, contraparte maior, patente, atrai imprensa, etc. — │
│  revelados na diligência do Passo 5.5]                       │
│                                                             │
│  Status do caminho paralelo (conduta em marketplace):        │
│  [registrado / em fila / recusado — do Passo 4. "Não         │
│  aplicável" se a conduta não é em marketplace.]              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

Se o usuário é não-advogado (conforme `## Quem está usando isso`), adicione:

> Enviar uma notificação extrajudicial tem consequências legais além da resposta do destinatário — é afirmação positiva de direitos que pode ser usada contra você. Você revisou isso com um advogado? Se não, aqui vai um briefing para levar a ele: [gere resumo de 1 página: partes, direitos afirmados, conduta infratora, demanda, postura, riscos sinalizados acima, o que pode dar errado, perguntas específicas para o advogado].
>
> Se precisar encontrar um advogado licenciado na sua jurisdição: o serviço de referência da OAB seccional do seu estado é o ponto de partida mais rápido. A ABPI (Associação Brasileira da Propriedade Intelectual) mantém diretório de associados especializados em marca e direito autoral.

Não escreva o .docx nem marque o draft como pronto sem engajamento explícito com o gate.

### Passo 8: Output

**Primário:** `<pasta-matter>/cease-desist/<slug>/draft-v<N>.docx` (ou `cease-desist/<slug>/draft-v<N>.docx` em nível de prática). Use o skill `docx`. Formatado como carta conforme a estrutura acima. Remova o cabeçalho de trabalho protegido da carta de saída.

**No chat:** mostre o draft como texto simples para revisão antes de escrever o .docx. Itere antes de comprometer em disco.

**Nota de encerramento para o revisor** (anexada apenas ao preview no chat, removida do .docx):

> Este é um draft de notificação extrajudicial para revisão de advogado, não uma carta pronta para envio. Enviá-la é afirmação de direitos legais com as consequências descritas no gate pré-entrega. Um advogado licenciado revisa, edita, e assume responsabilidade profissional antes do envio. Não envie este draft sem revisão.

**Verificação de citações.** Todo `[CITE:___]` e toda citação trazida de template ou autoridade fornecida é não verificada até rodada em fonte de pesquisa jurisprudencial. Antes de enviar, verifique cada citação em plataforma de pesquisa jurídica (JusBrasil, base do INPI, sites dos tribunais). Preserve as tags de atribuição de fonte — `[JusBrasil]`, `[INPI]`, `[fornecido pelo usuário]`, `[conhecimento do modelo — verificar]`, `[busca web — verificar]` — tags marcadas `verificar` são checadas primeiro.

**Sem suplemento silencioso.** Se uma ferramenta de pesquisa configurada retorna poucos ou nenhum resultado para uma autoridade que o draft precisa, reporte o que foi encontrado e pare. NÃO complete com busca web ou conhecimento do modelo sem perguntar. Apresente opções — ampliar a busca, tentar outra ferramenta, aceitar busca web com tags, deixar o placeholder — e deixe o usuário decidir.

**Checklist pós-envio.** Após o draft ser aprovado, escreva `<pasta-matter>/cease-desist/<slug>/checklist.md` com: leitura final pelo aprovador, todos `[VERIFY]` resolvidos, todos `[CITE]` preenchidos e verificados, marcações de sigilo removidas da carta de saída, aprovador assinou, método de entrega executado, prova de entrega retida, prazo de conformidade no calendário, plano de escalonamento se não houver resposta, matter criado em `matters/` se ainda não criado.

## Modo recebimento — triagem da notificação recebida

### Passo 1: Ler a carta

Extraia:

- **Remetente** — entidade, signatário, escritório externo se houver
- **Destinatário** — qual das nossas entidades/pessoas
- **Método e data de entrega**
- **Direito afirmado** — marca (nº de registro? jurisdição?), direito autoral (registrado? título?), ambos, algo mais
- **Conduta alegada** — a versão deles do que estamos fazendo
- **Fundamento legal** — estatutos, cláusulas contratuais, teorias citadas
- **Demanda** — o que querem; prazo declarado?
- **Ameaças** — o que dizem que farão
- **Tom** — firme / brando / terra arrasada; assinatura de advogado geralmente sinaliza seriedade

### Passo 2: Avaliar a afirmação

Não é parecer jurídico — uma leitura estruturada:

- **Validade dos direitos.** Os registros afirmados são reais e ativos? (Verificar base do INPI, registros da Biblioteca Nacional — sinalizar qualquer um que pareça caduco ou não vigente.) Para alegações de uso de fato, que evidência eles realmente citam?
- **Plausibilidade de confusão / semelhança / infração.** Nos fatos alegados, essa é uma alegação plausível ou está forçando? Para marca: risco de confusão pela regra da especialidade (art. 124 XIX, Lei 9.279/1996), salvo alto renome (art. 125) ou notoriamente conhecida (art. 126) — `[SME VERIFY]` a jurisprudência do TRF-2/STJ aplicável. Para direito autoral: acesso + semelhança substancial. Sinalize onde a alegação parece mais fraca.
- **Desproporcionalidade.** Estão demandando mais do que a conduta justifica? (Querem a marca transferida quando o registro cobriria no máximo re-rotulagem? Querem todas as vendas quando só um canal tocou o direito?) Demandas desproporcionais enfraquecem a posição de negociação e reforçam contra-alegação de abuso de direito.
- **Prazos.** Decadência, prescrição (Lei 9.279/1996 art. 225 — prescrição em 5 anos para ação de reparação), timing de registro — sinalize qualquer questão de data na face da carta.
- **Foro.** Onde processariam? O foro está fixado contratualmente (improvável em disputa de PI entre estranhos)? Há oportunidade de ação declaratória negativa para nós?

### Passo 3: Avaliar nossa exposição

- **Estamos de fato infringindo?** Olhar honesto. O que o registro mostra?
- **Poderíamos parar facilmente?** Custo de conformidade vs. custo da briga.
- **O remetente é troll ou reclamante real?** Litigante contumaz? Conhecido por lutar? Campanha recente de notificação em uso comparável? Verificar processos públicos se houver tempo.
- **O que está em jogo além dessa disputa?** Valor de marca, relacionamentos com clientes, precedente para notificações inbound semelhantes.

### Passo 4: Opções

Apresente 4-5 opções com tradeoffs:

**A — Cumprir rapidamente**
- Quando: a alegação é plausível, conformidade é barata, e a briga não vale a pena
- Tradeoff: estabelece concessão que podem apontar depois; pode encorajar futuras afirmações
- Próximo passo: confirmar conformidade por escrito (estrita), não conceder teoria mais ampla

**B — Negociar**
- Quando: há acordo de meio-termo (licença, coexistência, cronograma de rebranding) que resolve
- Tradeoff: consome tempo; exige cuidado na postura de comunicação de acordo (confidencialidade de negociação/mediação, Lei 13.140/2015 art. 30 — proteção decorre da substância e contexto, não apenas do rótulo)
- Próximo passo: carta de espera + abertura de trilha de negociação

**C — Responder firmemente (rejeitar)**
- Quando: a alegação deles é fraca, desproporcional, ou factualmente errada; queremos encerrar sem litigar
- Tradeoff: trava uma posição; se a alegação for de fato plausível, nossa resposta vira prova documental
- Próximo passo: redigir carta de resposta — considerar rodar via `/ip-legal:cease-desist --send` reenquadrada como resposta

**D — Ignorar (e preservar)**
- Quando: a alegação é frívola, o remetente não parece ter capacidade de processar, o prazo não tem consequência legal
- Tradeoff: silêncio pode ser usado como não-negação em alguns contextos; hold legal obrigatório de qualquer forma; risco de ajuizamento seguir
- Próximo passo: emitir hold legal via processo em nível de matter; registrar a demanda; seguir em frente

**E — Antecipar com ação declaratória negativa ou processo de nulidade**
- Quando: enfrentamos incerteza real de negócio, a alegação é fraca, e nos beneficiamos do nosso próprio foro
- Tradeoff: vamos à ofensiva; orçamento e aprovação de liderança necessários; agora há um processo
- Próximo passo: escalar para escritório externo conforme perfil de prática, não redigir

**F — Processo administrativo de nulidade no INPI ou ação de nulidade de registro**
- Quando: os próprios direitos deles são vulneráveis e queremos tirar o instrumento de jogo
- Tradeoff: lento, caro, público; separado da disputa em si (Lei 9.279/1996 art. 168-175 para processo administrativo; art. 173-175 para ação judicial de nulidade)
- Próximo passo: escalar para escritório externo

Recomende uma com duas frases de justificativa. Seja específico sobre o porquê.

### Passo 5: Triagem de prazos

- Prazo declarado por eles — anote, mas não nos vincula legalmente (a menos que estatuto específico dê força).
- Nosso prazo interno de decisão — tipicamente prazo declarado menos tempo suficiente para redigir, revisar, e aprovar resposta. Sinalize no calendário.
- Prazos legais — prescrição de qualquer alegação subjacente (Lei 9.279/1996 art. 225 — 5 anos), períodos contratuais de cura, prazos específicos de foro.

Ignorar um prazo declarado inteiramente é uma escolha, não um padrão. Note que ajuizamento geralmente segue o silêncio, não a data do prazo.

### Passo 6: Escrever o memorando de triagem

Output: `<pasta-matter>/cease-desist/inbound/<slug>/triage.md` (ou em nível de prática se matter workspaces estiver desligado).

```markdown
[CABEÇALHO DE TRABALHO PROTEGIDO — conforme config do plugin ## Outputs — difere por papel; ver `## Quem está usando isso`]

[BLOCO DE HERANÇA DE SIGILO — escolha por papel e tipo de matter; ver orientação abaixo do template]

# Notificação Recebida — Triagem

> **LEITURA PARA TRIAGEM, NÃO PARECER.** Este é um scan de intake e análise de opções — não um parecer jurídico de mérito. A avaliação abaixo é leitura estruturada para apoiar a decisão do advogado sobre roteamento e resposta. Toda lei, regra, ou caso citado está sinalizado para verificação de especialista; toda avaliação de mérito é do advogado, não deste skill.

**Slug:** [slug]
**Recebida:** [AAAA-MM-DD]
**Recebida por:** [entidade / pessoa]
**Arquivo recebido:** [path]

## A afirmação

**Remetente:** [entidade, signatário, advogado]
**Direito afirmado:** [marca / direito autoral / ambos — com especificidades, números de registro, jurisdições]
**Conduta alegada:** [versão deles, um parágrafo]
**Demanda:** [lista — pedidos específicos]
**Prazo declarado por eles:** [data]
**Tom:** [firme / brando / terra arrasada]

## Validade dos direitos

[Registros conforme afirmados — `[SME VERIFY]` contra o INPI/Biblioteca Nacional; alegações de uso de fato avaliadas contra a evidência citada]

## Fundamento legal citado

[Cada citação com tag inline `[SME VERIFY: aplicabilidade / vigência / jurisdição]` e fonte `[JusBrasil / fornecido pelo usuário / conhecimento do modelo — verificar / busca web — verificar]`. Não confie em nenhuma citação aqui sem checagem independente.]

## Avaliação de plausibilidade

- **Confusão / semelhança / infração nos fatos:** [leitura]
- **Desproporcionalidade:** [leitura]
- **Questões de prazo (decadência, prescrição, timing de registro):** [leitura]
- **Foro:** [foro provável deles; oportunidade de ação declaratória negativa]

## Nossa exposição

- **De fato infringindo?** [olhar honesto]
- **Custo de conformidade vs. custo da briga:** [leitura]
- **Credibilidade do remetente:** [troll / reclamante real / litigante contumaz — com evidência pública se houver]
- **Riscos colaterais:** [marca, clientes, precedente]

**Classificação de triagem:** [substancial / discutível / fraca / frívola] — *leitura estruturada para roteamento, não parecer de mérito; `[SME VERIFY]`*

## Opções

### A. Cumprir rapidamente
[Justificativa, tradeoffs, próximo passo]

### B. Negociar
[Justificativa, tradeoffs, próximo passo]

### C. Responder firmemente
[Justificativa, tradeoffs, próximo passo]

### D. Ignorar + preservar
[Justificativa, tradeoffs, próximo passo]

### E. Antecipar (ação declaratória negativa)
[Justificativa, tradeoffs, próximo passo]

### F. Processo de nulidade
[Justificativa, tradeoffs, próximo passo]

**Recomendação:** [A/B/C/D/E/F] — [duas frases do porquê] — `[SME VERIFY: advogado confirma antes de executar]`

## Prazos

- **Prazo declarado por eles:** [data]
- **Nosso prazo interno de decisão:** [data]
- **Prazos legais de qualquer alegação subjacente:** [prescrição, cura, processual — com datas]

## Ações imediatas

- [ ] Hold legal emitido — [sim/não]
- [ ] Matter criado no log — [sim/não/a definir]
- [ ] Advogado designado — [quem]
- [ ] Seguro acionado — [sim/não/N-A]
- [ ] Escalonamento interno — [quem/quando]
```

**Bloco de herança de sigilo — escolha por papel e tipo de matter.** Leia `## Quem está usando isso` (Papel) na config do plugin e o tipo de matter (marca / direito autoral / patente / OSS / outro). Esta triagem registra uma leitura de mérito de primeira passada sobre uma afirmação adversa; se de fato é sigilosa depende de quem a preparou e do que trata. Errar em qualquer direção é prejudicial — uma marcação falsa de "sigiloso" cria admissão descobrível que soa como concessão; sub-marcar um memorando genuinamente sigiloso pode renunciar à proteção. Insira exatamente um dos seguintes:

- **Papel = Advogado(a) / profissional jurídico:**
  > **Herança de sigilo.** Esta triagem registra nossa leitura de mérito de primeira passada e postura de resposta sobre afirmação adversa. É material protegido pelo sigilo profissional advogado-cliente (Estatuto OAB, Lei 8.906/1994, art. 7º II e XIX, art. 34 VII). Não encaminhe, não anexe a acionamento de seguro sem expurgo, não compartilhe com a contraparte. Armazene com material sigiloso do matter e marque conforme convenção interna de sigilo. [verified: https://www.planalto.gov.br/ccivil_03/leis/l8906.htm]

- **Papel = Agente da Propriedade Industrial registrado, matter é processo de PI perante o INPI:**
  > **Sigilo (agente-cliente).** Esta triagem é tratada com sigilo na representação estrita perante o INPI (Lei 9.279/1996, art. 216), por se relacionar a matéria razoavelmente necessária e incidente à prosecução de pedidos de registro perante o INPI. Esse sigilo é estreito: não se estende a matérias fora da representação no INPI e não equivale ao sigilo profissional do advogado (Estatuto OAB). Não encaminhe, não anexe a acionamento de seguro sem expurgo, não compartilhe com a contraparte. Leve a advogado(a) supervisor(a) para decisões de sigilo específicas do matter. [unverified: LPI Art. 216 estabelece que os atos são praticados por partes ou procuradores qualificados perante o INPI; não confirma sigilo agente-cliente — https://www.planalto.gov.br/ccivil_03/leis/l9279.htm]

- **Papel = Agente da Propriedade Industrial registrado, matter NÃO é processo de PI perante o INPI** (marca em disputa judicial, direito autoral, OSS, segredo industrial, contrato, ou qualquer coisa fora da representação estrita perante o INPI):
  > **CONFIDENCIAL — NÃO SIGILOSO.** Esta triagem não é sigilosa porque a representação do Agente da Propriedade Industrial se limita à prosecução perante o INPI (Lei 9.279/1996, art. 216). Uma disputa marcária judicializada, direito autoral, OSS, ou outra matéria fora da representação no INPI cai fora dessa proteção estreita. Trate este documento como confidencial, armazene com cuidado, leve a advogado(a), e deixe o advogado marcá-lo. Não encaminhe como sigiloso. [unverified: LPI Art. 216 estabelece que os atos são praticados por partes ou procuradores qualificados perante o INPI; não confirma sigilo agente-cliente — https://www.planalto.gov.br/ccivil_03/leis/l9279.htm]

- **Papel = Não-advogado e não Agente da Propriedade Industrial:**
  > **CONFIDENCIAL — NÃO SIGILOSO.** Este documento não é protegido por sigilo profissional a menos que e até que seja revisado por advogado(a) licenciado(a) (Estatuto OAB). Trate como confidencial; não encaminhe a ninguém fora da cadeia de revisão jurídica; leve a advogado(a) e deixe o advogado marcá-lo. Encaminhar este documento como "sigiloso" antes de revisão de advogado não o torna sigiloso e pode prejudicá-lo se o matter se tornar contencioso.

Encerre a apresentação no chat com esta salvaguarda verbatim:

> Este é um memorando de triagem, não um parecer. A avaliação de força acima é uma primeira leitura baseada apenas na carta — não considera fatos que você não me contou, registros que não posso verificar, ou questões jurisdicionais. Um advogado avalia antes de você responder, decidir ignorar, ou se comprometer com um caminho.

Se o usuário é não-advogado, adicione o parágrafo de roteamento "encontre um advogado" do modo envio.

### Passo 7: Handoff

Baseado na recomendação e confirmação do usuário:

- Responder firmemente → handoff para `/ip-legal:cease-desist --send` com contexto pré-populado como carta de resposta (isso dispara o gate de modo envio novamente).
- Negociar → iniciar carta de espera / trilha de negociação no matter.
- Antecipar ou processo de nulidade → escalar para escritório externo conforme a linha de contencioso de PI do perfil de prática; não redigir.
- Criação de matter → se não houver um e o matter for material, oferecer `/ip-legal:matter-workspace new <slug>` pré-populado.
- Cumprir / ignorar → registrar a decisão no histórico do matter; emitir ou confirmar o hold legal; fechar o registro de triagem.

## Decision posture

Conforme `## Postura de decisão em questões jurídicas subjetivas` no perfil de prática: quando incerto se há infração, se uma marca é confusamente semelhante, se uma obra é substancialmente semelhante, se uma alegação é plausível, ou se enviar é seguro — não decida silenciosamente que está tudo bem. Sinalize para revisão de advogado, mostre os fatores que pesam em ambas direções, anote a incerteza. Enviar notificação com base em suposição é porta de mão única; expor a dúvida é porta de duas mãos.

## Consequential-action gate (modo envio — antes de enviar notificação extrajudicial)

**Antes de enviar a notificação redigida à contraparte — e sempre antes de executar uma demanda ou pressão formal:** Leia `## Quem está usando isso` em ~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md. Se o Role é **Não-advogado** (seja com ou sem acesso a advogado):

> Enviar uma notificação extrajudicial afirmando direito é um ato jurídico com consequências. É uma afirmação formal do seu direito, fica registrado em processo futuro contra você, e posições tomadas aqui prendem a empresa e podem ser usadas contra ela em procedimentos posteriores. Você conversou com um advogado? Se sim, prossiga. Se não, aqui está um briefing para levar a ele/ela:
>
> - O direito afirmado (marca no INPI, direito autoral, segredo industrial, etc.) — está registrado/protegido nas jurisdições onde a contraparte atua?
> - A conduta infratora — é claro o bastante para uma notificação, ou há ambiguidade sobre intenção/infração?
> - A contraparte — é uma pessoa física, empresa, concorrente, cliente, aliado, ou desconhecida? Essa relação muda o tom e a estratégia.
> - Desproporcionalidade — o benefício de enviar notificação agora supera o risco de transformar uma situação cinzenta em contencioso agressivo?
> - Prazos — há prazo para agir (decadência de marca, prescrição, caducidade), ou podemos esperar para avaliar?
> - Risco colateral — a empresa pode ser processada com ação declaratória negativa em foro da contraparte? Pode sofrer represálias comerciais? Pode prejudicar relação com cliente/parceiro?
> - O que pode dar errado (litigância de má-fé — CPC art. 80 — se a alegação for infundada, abuso de direito, ação declaratória negativa em foro desfavorável)
> - O que perguntar ao advogado (devemos enviar? Devemos suavizar o tom? Devemos enviar em conjunto via associação profissional? Há posições que NÃO devemos tomar?)
>
> Se precisa encontrar um advogado: a OAB (Ordem dos Advogados do Brasil) seccional do seu estado é o ponto de partida — sua Comissão de sociedade/serviço de referência ou a subsecção local pode encaminhá-lo(a). (Para matéria de PI estrangeira: entre em contato com correspondente local ou escritório com experiência naquela jurisdição.)

Não redija nem envie notificação definitiva após este gate sem um sim explícito do usuário. Um rascunho marcado PARA REVISÃO DE ADVOGADO é aceitável.

---

## What this skill does not do

- **Enviar a carta.** Apenas redação. O usuário envia, após aprovação.
- **Pesquisar citações.** Placeholders permanecem placeholders a menos que o usuário forneça autoridades ou ferramenta de pesquisa conectada retorne. Inventar citações é exposição de responsabilidade profissional.
- **Pular o gate.** O gate de modo envio roda toda vez. Mesmo com flag `--skip-gate` (nenhuma é fornecida), o skill registraria a omissão no arquivo de draft.
- **Decidir mérito definitivamente no lado recebimento.** A classificação é leitura estruturada para roteamento; parecer formal de mérito fica com o advogado.
- **Validar a lei citada pelo remetente.** Sinaliza para o usuário; não declara autonomamente uma alegação válida ou inválida.
- **Fazer a chamada de criação de matter.** Mostra a recomendação; o usuário decide.
