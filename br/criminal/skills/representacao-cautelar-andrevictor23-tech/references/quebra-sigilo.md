# Quebras de Sigilo e Medidas sobre Dados

Mapa das medidas sobre dados: cada uma tem fundamento, requisitos e pedido próprios. Identificar exatamente o que a investigação precisa antes de escolher; pedir a medida errada (ou mais invasiva que o necessário) atrai indeferimento por falta de proporcionalidade.

## 0. O que NÃO precisa de representação (não gastar jurisdição)

- **Dados cadastrais** de linhas telefônicas e usuários (qualificação, filiação, endereço): requisição direta da autoridade policial às operadoras (art. 15 da Lei 12.850/13, aplicável às investigações de organização criminosa; art. 13-A do CPP para os crimes ali listados, como sequestro, redução a condição análoga, extorsão mediante sequestro, tráfico de pessoas). Fora dessas hipóteses, avaliar requisição fundamentada; se a operadora recusar, aí sim representar.
- **Sinal de localização em tráfico de pessoas e correlatos** (art. 13-B do CPP): requisição ao juiz, mas com regra especial de urgência (se não houver decisão em 12 horas, a requisição pode ir direto à operadora, com comunicação imediata ao juiz).
- **RIF do COAF**: o compartilhamento espontâneo ou por intercâmbio com a UIF dispensa autorização judicial (STF, Tema 990). O detalhamento adicional junto às instituições financeiras exige quebra judicial (item 3).

## 1. Registros telefônicos e dados telemáticos armazenados

**Objeto**: extratos de chamadas (HDC), registros de ERBs, registros de conexão e de acesso a aplicações de internet, dados de contas em provedores (Google, Meta), comunicações armazenadas.

**Fundamento**: reserva de jurisdição; Marco Civil da Internet, arts. 10, §1º, 22 e 23 (registros de conexão/acesso); art. 17 da Lei 12.850/13 (registros telefônicos); art. 3º, VI e VII, da Lei 12.965/2014.

**Requisitos do art. 22, parágrafo único, do Marco Civil** (usar como roteiro dos fundamentos mesmo fora de internet, pois o juiz os cobra por analogia):
1. fundados indícios da ocorrência do ilícito;
2. justificativa motivada da **utilidade** dos registros para a investigação;
3. **período** ao qual se referem os registros (delimitar: peça sem período definido é indeferida ou devolvida).

**Pedido deve individualizar**: linhas (com operadora), IMEIs, contas/perfis (URL, ID, e-mail), período exato, e a forma de entrega (mídia, e-mail funcional, sistema). Incluir pedido de **sigilo dos autos** (art. 20 do CPP) e de **ofício direto da autoridade policial** às operadoras/provedores para agilizar cumprimento.

## 2. Interceptação de comunicações telefônicas e telemáticas (Lei 9.296/96)

**Objeto**: comunicação **em fluxo** (voz e dados em tempo real, inclusive aplicativos, art. 1º, parágrafo único). Não confundir com dados armazenados (item 1) nem com conteúdo de celular apreendido (item 4).

**Requisitos cumulativos (art. 2º, a contrario sensu)**:
1. indícios razoáveis de autoria ou participação (descrever com clareza a situação objeto da investigação e qualificar os investigados, art. 2º, parágrafo único);
2. **imprescindibilidade**: a prova não pode ser feita por outros meios disponíveis (dizer quais meios já foram tentados ou por que são inviáveis; este é o parágrafo que os juízes mais escrutinam);
3. crime punido com **reclusão**.

**Prazo**: 15 dias, renováveis por igual período mediante demonstração da indispensabilidade (art. 5º). Pedir expressamente o prazo, os terminais alvo com operadora, e o encaminhamento do fluxo à unidade (sistema Guardião ou equivalente). Prorrogações exigem relatório do que a medida vem produzindo.

## 3. Sigilo bancário e fiscal (LC 105/2001, art. 1º, §4º)

**Objeto**: extratos, contratos, movimentação de contas, dados fiscais (DIRPF, notas), operações de câmbio e cartões.

**Fundamentos a demonstrar**: indícios do crime e **pertinência** entre as contas/período e o fato apurado (compatibilidade patrimonial, fluxo de valores ligado ao crime). Delimitar **titulares, instituições (ou SIMBA/CCS para localizar contas), período e tipo de dado**. Pedir transmissão via SIMBA quando disponível, e a extensão a contas localizadas via CCS em nome dos mesmos titulares no período.

**Fiscal**: requisitar à Receita Federal/SEFAZ os dados do período, com o mesmo lastro de pertinência.

## 4. Acesso a dados de dispositivos já apreendidos

Celular/computador apreendido em flagrante ou busca **não pode ter o conteúdo acessado sem autorização judicial específica** (jurisprudência consolidada do STJ). Representar pedindo: autorização de acesso, extração forense (Cellebrite/IPED ou equivalente) e análise integral dos dados (comunicações armazenadas, mídias, aplicativos, nuvem vinculada quando acessível a partir do aparelho), com observância da cadeia de custódia (arts. 158-A e seguintes do CPP). Individualizar os aparelhos (marca, modelo, IMEI, lacre, auto de apreensão e folhas).

Quando a busca e apreensão ainda vai ocorrer, incluir esse pedido desde logo na representação de busca (ver `busca-apreensao.md`).

## Proporcionalidade: escada de invasividade

Ordenar o pedido pela medida menos invasiva que resolve: cadastro (sem juiz) → registros/extratos com período delimitado → dados armazenados → interceptação em fluxo. Peça que pede interceptação quando bastariam extratos tende ao indeferimento; peça que escala fundamentadamente ("os extratos obtidos às fls. X revelaram contatos diários com o fornecedor, sendo agora imprescindível o conteúdo das comunicações") tende ao deferimento.

## Erros que derrubam a peça (checklist negativo)

- [ ] Período não delimitado ou desproporcional ao fato apurado
- [ ] Linhas/contas/aparelhos não individualizados (número, operadora, IMEI, ID)
- [ ] Interceptação sem o parágrafo de imprescindibilidade (outros meios)
- [ ] Pedido de medida mais invasiva sem escalar da menos invasiva
- [ ] Falta de pedido de sigilo dos autos quando a medida perde eficácia se conhecida
- [ ] Representar por dado cadastral que a autoridade policial pode requisitar diretamente
