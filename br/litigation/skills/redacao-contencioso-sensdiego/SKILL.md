---
name: redacao-contencioso-sensdiego
title: Redação contenciosa
description: Redigir peças, recursos, execuções, procedimentos especiais e manifestações para processo civil usando somente fatos, provas, normas e escolhas já interpretados e confirmados. Use quando o usuário quiser minuta protocolável após análise confirmada.
author: sensdiego
author_url: https://github.com/sensdiego/codigo-aberto/tree/main/skills/redacao-contencioso
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: litigation
language: pt
sources:
- title: Indice Modulos
  path: references/indice-modulos.md
- title: Acao Monitoria
  path: references/modulos/acao-monitoria.md
- title: Acao Rescisoria
  path: references/modulos/acao-rescisoria.md
- title: Acoes Familia
  path: references/modulos/acoes-familia.md
- title: Acoes Possessorias
  path: references/modulos/acoes-possessorias.md
- title: Acordo Homologacao
  path: references/modulos/acordo-homologacao.md
- title: Agravo Instrumento
  path: references/modulos/agravo-instrumento.md
- title: Agravo Interno
  path: references/modulos/agravo-interno.md
- title: Alegacoes Finais
  path: references/modulos/alegacoes-finais.md
- title: Apelacao
  path: references/modulos/apelacao.md
- title: Consignacao Pagamento
  path: references/modulos/consignacao-pagamento.md
- title: Contestacao
  path: references/modulos/contestacao.md
- title: Cumprimento Sentenca
  path: references/modulos/cumprimento-sentenca.md
- title: Demarcacao Divisao
  path: references/modulos/demarcacao-divisao.md
- title: Dissolucao Parcial Sociedade
  path: references/modulos/dissolucao-parcial-sociedade.md
- title: Embargos Declaracao
  path: references/modulos/embargos-declaracao.md
- title: Embargos Terceiro
  path: references/modulos/embargos-terceiro.md
- title: Especificacao Provas
  path: references/modulos/especificacao-provas.md
- title: Excecao Pre Executividade
  path: references/modulos/excecao-pre-executividade.md
- title: Execucao Titulo Extrajudicial
  path: references/modulos/execucao-titulo-extrajudicial.md
- title: Exibicao Documento Coisa
  path: references/modulos/exibicao-documento-coisa.md
- title: Exigir Contas
  path: references/modulos/exigir-contas.md
- title: Habilitacao Impugnacao Credito
  path: references/modulos/habilitacao-impugnacao-credito.md
- title: Homologacao Penhor Legal
  path: references/modulos/homologacao-penhor-legal.md
- title: Incidente Desconsideracao Personalidade Juridica
  path: references/modulos/incidente-desconsideracao-personalidade-juridica.md
- title: Inventario Partilha
  path: references/modulos/inventario-partilha.md
- title: Jurisdicao Voluntaria
  path: references/modulos/jurisdicao-voluntaria.md
- title: Liquidacao Sentenca
  path: references/modulos/liquidacao-sentenca.md
- title: Manifestacao Generica
  path: references/modulos/manifestacao-generica.md
- title: Oposicao
  path: references/modulos/oposicao.md
- title: Peticao Inicial
  path: references/modulos/peticao-inicial.md
- title: Producao Antecipada Prova
  path: references/modulos/producao-antecipada-prova.md
- title: Prova Pericial
  path: references/modulos/prova-pericial.md
- title: Recurso Especial Extraordinario
  path: references/modulos/recurso-especial-extraordinario.md
- title: Regulacao Avaria Grossa
  path: references/modulos/regulacao-avaria-grossa.md
- title: Replica
  path: references/modulos/replica.md
- title: Restauracao Autos
  path: references/modulos/restauracao-autos.md
- title: Tutela Urgencia Evidencia
  path: references/modulos/tutela-urgencia-evidencia.md
---

# Redação contenciosa

Redija somente depois da análise. Observe a
[disciplina compartilhada](../../references/disciplina.md), o
[contrato de handoff](../../references/handoff.md) e a
[biblioteca do CPC](../../references/legislacao/cpc/README.md).

## Pré-requisitos

Verifique os handoffs de análise documental e jurídica. Eles devem corresponder
ao mesmo caso e à mesma lente, declarar fontes e escopo e identificar conteúdo
confirmado. Documento bruto, narrativa solta ou pesquisa não verificada não
servem como insumo de minuta.

Se a entrada declarar `case-adaptation-v1`, valide recibo, identidade, lente e
elegibilidade; selecione a frente material e confira evento controlador,
cobertura, conflitos e `scope_status`. Não selecione módulo quando a frente ou o
ato estiver `indeterminado`, a cobertura estiver `bloqueada`, o conflito bloquear
o efeito necessário ou o escopo estiver `nao_suportado`. Em
`suportado_condicionado`, só avance depois de satisfazer a condição nomeada.

Módulo indicado pelo pacote é candidato, não ordem. Refaça o mapeamento pelo
índice depois do mapa jurídico. Ato `decidido` exige recibo de decisão humana e
ainda passa pelo briefing próprio; `candidato` exige análise ou deliberação.
Ao expor ato ainda candidato, preserve a hierarquia declarada no pacote entre
módulo-base e complementos como pista não autoritativa; nunca apresente
complemento como ato-base autônomo.
Sem recibo de adaptação, aplique os pré-requisitos comuns sem exigir conversão.

Uma manifestação simples com resultado da análise e escolha do advogado
expressamente confirmados no contexto atual não exige reabrir análise nem
deliberação. Prepare o briefing proporcional e preserve como `[verificar]`
qualquer fonte ou localizador que o usuário não tenha fornecido.

Infira o ato provável, mas não escolha silenciosamente. Consulte o
[índice de módulos](references/indice-modulos.md) e carregue depois da
confirmação somente o módulo-base correspondente. Quando o módulo oferecer
modos, confirme um modo e carregue apenas o trecho aplicável. Se o briefing
também confirmar tutela provisória, acrescente apenas o módulo complementar de
tutela.

Se o ato e a posição central já estiverem registrados e a escolha restante
couber como item explícito do briefing, apresente-o como `BLOQUEADA — item
aberto`; não exija deliberação anterior. Se a escolha estratégica impedir um
briefing coerente (ato entre alternativas, posição, pedido ou concessão
material), ou se o ato inferido não estiver entre as opções do mapa jurídico,
o handoff de tipo `decisão` é pré-requisito. Se ele estiver ausente, exponha as
opções registradas e suas consequências sem escolher, encaminhe para
`deliberacao-juridica` e não leia módulo de redação.

## Briefing obrigatório

Antes de redigir, apresente:

- ato e destinatário;
- módulo-base e modo, quando houver;
- objetivo processual;
- parte e posição representada;
- fatos, provas, normas e teses que serão usados;
- pedidos, conclusões ou resultado pretendido;
- profundidade e tom;
- prazo e cabimento conforme o mapa jurídico;
- lacunas e campos que permanecerão marcados.

Pare e espere confirmação humana explícita. Termine o briefing com a pergunta
fechada da disciplina compartilhada. Resposta a item aberto não autoriza
redação — nem quando a mesma mensagem diz "pode redigir": nesse caso,
reapresente o consolidado (o que mudou + a pergunta fechada) e aguarde a
confirmação distinta. "Analise", "prepare" ou "prossiga" em etapa anterior
não confirma o briefing desta minuta.

Mostre o estado da redação definido na disciplina. Só leia o módulo quando o
turno anterior do assistente já tiver declarado `AGUARDANDO CONFIRMAÇÃO DO
BRIEFING CONSOLIDADO` e a mensagem atual responder afirmativamente à pergunta
fechada sem trazer mudança material. Resolver item aberto e dizer "pode
redigir" na mesma mensagem apenas muda o estado para `AGUARDANDO`.

## Redação e auditoria

Depois da confirmação:

1. recupere somente elementos interpretados e confirmados;
2. leia o módulo-base, o complemento de tutela quando confirmado e os artigos
   integrais referenciados por eles;
3. produza estrutura proporcional ao ato;
4. ligue afirmações materiais às fontes e localizadores;
5. preserve `[verificar]`, lacunas e decisões do advogado;
6. rode o checklist específico;
7. declare expressamente que nada foi protocolado.

Pesquisa jurisprudencial é opcional. Se não tiver sido realizada, não atribua
entendimento a tribunal. Se usada, aceite somente precedente no estado de
verificação compatível com redação.

## O que esta skill não faz

- Não redige diretamente de documentos brutos.
- Não escolhe recurso, tese, pedido ou concessão sem confirmação.
- Não inventa fato, prova, dispositivo, precedente ou localizador.
- Não infla manifestação simples.
- Não protocola, envia, assina ou pratica ato externo.

> Documento gerado com suporte de inteligência artificial. Conteúdo sujeito à
> revisão e validação obrigatória pelo advogado responsável antes de qualquer
> uso profissional ou processual.
