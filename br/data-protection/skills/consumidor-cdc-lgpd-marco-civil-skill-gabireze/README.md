# consumidor-cdc-br-skill

![status](https://img.shields.io/badge/status-pronto%20e%20otimizado-brightgreen)
![versao](https://img.shields.io/badge/versao-1.4.0-blue)
![idioma](https://img.shields.io/badge/idioma-pt--BR-yellow)
![dominio](https://img.shields.io/badge/dominio-CDC%20%7C%20LGPD%20%7C%20Marco%20Civil-purple)
![fontes](https://img.shields.io/badge/fontes-oficiais%20primeiro-success)
![validacao](https://img.shields.io/badge/validacao-Skill%20is%20valid-brightgreen)
![licenca](https://img.shields.io/badge/licenca-Apache--2.0%20%7C%20CC--BY--4.0-blue)

Skill/knowledge pack em portugues do Brasil para agentes de IA trabalharem com relacoes de consumo, produtos digitais, privacidade e uso da internet no Brasil, com foco em **CDC**, **LGPD**, **Marco Civil da Internet**, **ANPD**, **Senacon**, **Procon**, **Consumidor.gov.br**, plataformas digitais, marketplaces, assinaturas, comunicados, politicas, termos, cancelamento, cobrancas, garantias, SAC, logs, moderacao, incidentes e transferencia internacional de dados.

O pacote foi desenhado para Codex, mas os arquivos sao Markdown portateis e podem ser usados como base de conhecimento em Gemini, Claude, ChatGPT/GPTs, agentes internos, RAG e cursos.

> Esta skill e informativa. Ela nao substitui advogado, Defensoria, Procon, ANPD, agencia reguladora, autoridade policial ou revisao juridica humana.

## GitAds Sponsored
[![Sponsored by GitAds](https://gitads.dev/v1/ad-serve?source=gabireze/consumidor-cdc-lgpd-marco-civil-skill@github)](https://gitads.dev/v1/ad-track?source=gabireze/consumidor-cdc-lgpd-marco-civil-skill@github)

## Sumario

- [Status](#status)
- [O Que Esta Skill Faz](#o-que-esta-skill-faz)
- [Quando Usar](#quando-usar)
- [Quando Nao Usar Sozinha](#quando-nao-usar-sozinha)
- [Compatibilidade](#compatibilidade)
- [Instalacao e Uso](#instalacao-e-uso)
- [Estrutura do Pacote](#estrutura-do-pacote)
- [Mapa dos Arquivos](#mapa-dos-arquivos)
- [Fluxo de Trabalho do Agente](#fluxo-de-trabalho-do-agente)
- [Fontes Oficiais](#fontes-oficiais)
- [Exemplos de Prompt](#exemplos-de-prompt)
- [Validacao](#validacao)
- [Atualizacoes e Manutencao](#atualizacoes-e-manutencao)
- [Limites e Cuidados](#limites-e-cuidados)

## Status

| Campo | Valor |
|---|---|
| Nome da skill | `consumidor-cdc-br` |
| Versao | `1.4.0` |
| Ultima revisao manual | `2026-07-03` |
| Ultima validacao de prontidao | `2026-07-03` |
| Idioma | Portugues do Brasil |
| Escopo | Juridico-informativo, consumerista, privacidade e plataformas digitais |
| Validacao Codex | `quick_validate.py .` retornou `Skill is valid!` |
| Veredito para agentes | Pronto e otimizado (Padrão Gemini/Antigravity) |

## O Que Esta Skill Faz

Esta skill ajuda agentes de IA a:

- responder perguntas informativas sobre relacoes de consumo no Brasil;
- mapear base legal provavel com linguagem cautelosa;
- revisar comunicados, termos, politicas, checkouts, FAQs e fluxos de produto digital;
- estruturar reclamacoes para Consumidor.gov.br e Procon;
- revisar problemas de compra online, cancelamento, arrependimento, garantia, vicio, defeito, cobranca indevida e SAC;
- separar CDC, LGPD, Marco Civil, ANPD e regulacao setorial;
- orientar coleta de documentos e evidencias;
- reduzir risco de alucinacao juridica, promessa de resultado e citacao de fonte nao oficial;
- apoiar treinamento e avaliacao de agentes por meio de casos de teste.

## Quando Usar

Use quando o pedido envolver:

- CDC, relacao de consumo, fornecedor, consumidor, oferta, publicidade ou pratica abusiva;
- produto digital, app, SaaS, assinatura, marketplace, e-commerce, checkout ou pagina de preco;
- politica de privacidade, cookies, SDKs, analytics, cadastro, dados pessoais ou incidente de seguranca;
- LGPD, bases legais, direitos do titular, encarregado, ANPD, transferencia internacional ou RIPD;
- Marco Civil, aplicacao de internet, provedor, logs, IP, porta logica, neutralidade, conteudo de terceiro ou moderacao;
- SAC, atendimento, protocolo, cancelamento, suporte, Procon, Consumidor.gov.br ou Senacon;
- textos B2C: termos de uso, comunicado ao consumidor, regulamento comercial, FAQ, aviso de alteracao de termos ou resposta administrativa.

## Quando Nao Usar Sozinha

Use apenas como triagem e organizacao quando houver:

- processo judicial, prazo processual, peticao, recurso ou estrategia contenciosa;
- alto valor, risco coletivo, urgencia, saude, seguranca ou subsistencia;
- suspeita de crime, fraude, falsidade, ameaça, investigacao ou boletim de ocorrencia;
- setor regulado, como financeiro, seguros, saude, telecom, energia, educacao, transporte, apostas/jogos ou pagamentos;
- dados sensiveis, criancas/adolescentes, biometria, saude, incidente relevante ou transferencia internacional complexa;
- contrato, termo, politica ou comunicado que sera publicado sem revisao profissional.

## Compatibilidade

| Ambiente | Status | Forma recomendada de uso |
|---|---|---|
| Codex | Pronto | Instalar a pasta como skill. `SKILL.md` e `agents/openai.yaml` sao consumidos pelo ecossistema compatível. |
| OpenAI custom agents | Pronto com ajuste leve | Usar `SKILL.md` como instrucao principal e anexar `references/`, `assets/` e `evals/` como conhecimento. |
| ChatGPT/GPTs | Pronto como conhecimento | Colocar o conteudo de `SKILL.md` nas instrucoes e anexar as referencias principais. |
| Claude Projects/Skills | Pronto como conhecimento | Usar `SKILL.md` como roteador e anexar `references/` e `assets/`. |
| Gemini/Gems | Pronto e otimizado | Skill e diretórios estruturados nativamente (`references/`, `assets/`, `evals/`). |
| Agentes internos/RAG | Pronto | Indexar `references/` por arquivo e usar `SKILL.md` como policy/router. |
| Cursos e treinamentos | Pronto | Usar README, SKILL, checklists, assets e `evals/casos-teste.md`. |

Observacao: Codex consegue usar o formato de skill diretamente. Outras plataformas normalmente precisam receber os arquivos como conhecimento, contexto de projeto, prompt de sistema ou adapter proprio.

## Instalacao e Uso

### Codex

Coloque a pasta `consumidor-cdc-br-skill` no diretorio de skills do agente.

Exemplo de destino comum:

```text
%USERPROFILE%\.codex\skills\consumidor-cdc-br\
```

Depois, invoque pelo nome ou deixe o agente ativar por contexto:

```text
Use $consumidor-cdc-br para revisar esta politica de cancelamento de assinatura digital.
```

### Claude, Gemini, ChatGPT ou Agente Interno

Use este pacote como conhecimento:

1. Defina `SKILL.md` como instrucao principal.
2. Anexe os arquivos essenciais de `references/`.
3. Inclua `assets/` se o agente for redigir reclamacoes ou comunicados.
4. Inclua `evals/casos-teste.md` para validar comportamento.
5. Instrua o agente a consultar fontes oficiais atuais antes de citar norma, prazo, canal ou entendimento sensivel.

### Uso Minimo

Para ambientes com limite de contexto, priorize:

- `SKILL.md`
- `references/fontes-oficiais.md`
- `references/pesquisa-e-atualizacao.md`
- `references/matriz-temas-e-fontes.md`
- `references/politica-de-resposta.md`
- `references/lgpd-protecao-dados.md`
- `references/marco-civil-internet.md`
- `references/revisao-produtos-digitais.md`

## Estrutura do Pacote

```text
consumidor-cdc-br-skill/
  SKILL.md
  README.md
  VALIDATION_REPORT.md
  agents/
    openai.yaml
  references/
    agent-readiness-validation.md
    fontes-oficiais.md
    pesquisa-e-atualizacao.md
    artigos-chave-cdc.md
    lgpd-protecao-dados.md
    marco-civil-internet.md
    matriz-temas-e-fontes.md
    politica-de-resposta.md
    revisao-produtos-digitais.md
    checklists/
      cancelamento-assinaturas-digitais.md
      cobranca-indevida.md
      compra-online.md
      comunicados-consumidor.md
      garantia-vicio-defeito.md
      lgpd-produtos-digitais.md
      marco-civil-plataformas.md
      produtos-digitais-termos-politicas.md
      reclamacao-procon-consumidor-gov.md
      sac-e-atendimento.md
      superendividamento.md
  assets/
    comunicado-alteracao-termos.md
    notificacao-extrajudicial-fornecedor.md
    reclamacao-consumidor-gov.md
    reclamacao-procon.md
  evals/
    casos-teste.md
```

## Mapa dos Arquivos

| Arquivo | Funcao |
|---|---|
| `SKILL.md` | Entrada principal da skill. Define gatilhos, principios, fluxo e roteamento para referencias. |
| `agents/openai.yaml` | Metadados de interface para ambientes compatíveis com esse formato. |
| `references/fontes-oficiais.md` | Indice de fontes oficiais: Planalto, ANPD, Senacon, Consumidor.gov.br, STJ e normas correlatas. |
| `references/pesquisa-e-atualizacao.md` | Protocolo para verificar vigencia, citar normas e navegar na internet. |
| `references/matriz-temas-e-fontes.md` | Matriz para escolher base legal inicial por tema. |
| `references/politica-de-resposta.md` | Regras de cautela, formatos de resposta e frases proibidas. |
| `references/artigos-chave-cdc.md` | Resumo operacional de artigos recorrentes do CDC. |
| `references/lgpd-protecao-dados.md` | Guia LGPD: dados pessoais, bases legais, direitos, ANPD, incidentes e transferencia internacional. |
| `references/marco-civil-internet.md` | Guia Marco Civil: provedores, registros, logs, neutralidade, moderacao e conteudo de terceiro. |
| `references/revisao-produtos-digitais.md` | Guia para revisar apps, SaaS, marketplaces, termos, politicas e comunicados. |
| `references/checklists/` | Checklists especificos por tema. |
| `assets/` | Modelos adaptaveis de reclamacao, notificacao e comunicado (templates). |
| `evals/casos-teste.md` | Casos de validacao para testar agentes. |
| `references/agent-readiness-validation.md` | Relatorio de prontidao para uso por agentes. |
| `VALIDATION_REPORT.md` | Historico resumido da revisao da skill. |

## Fluxo de Trabalho do Agente

1. Classificar o pedido: consulta individual, revisao de texto, reclamacao, produto digital, privacidade, plataforma, incidente ou pesquisa normativa.
2. Carregar apenas a referencia necessaria.
3. Coletar fatos minimos: datas, fornecedor, canal, oferta, contrato, politica aceita, protocolos, prints, dados tratados e impacto.
4. Separar as bases: CDC, LGPD, Marco Civil, ANPD, contrato/termos e regulacao setorial.
5. Verificar fontes oficiais atuais antes de conclusao sensivel.
6. Responder com nivel de certeza: `base legal direta`, `tese plausivel`, `tema controvertido` ou `fora do escopo da skill`.
7. Entregar caminho pratico: documentos, pedido objetivo, canal adequado e ressalvas.

## Fontes Oficiais

A regra do pacote e **fonte oficial primeiro**.

Principais fontes mapeadas:

- Planalto: CDC, LGPD, Marco Civil, decretos e leis correlatas.
- ANPD: regulamentacoes, incidentes, RIPD, transferencia internacional, encarregado, sancoes e agentes de pequeno porte.
- Senacon/MJSP: defesa do consumidor e SNDC.
- Consumidor.gov.br: canal administrativo de reclamacao contra empresas participantes.
- STJ/STF: jurisprudencia qualificada, sumulas, repetitivos e precedentes oficiais quando necessario.

Antes de documento formal, termo, politica, comunicado ou resposta sensivel, registre:

```text
Fontes oficiais consultadas em DD/MM/AAAA
```

## Exemplos de Prompt

### Compra Online

```text
Use $consumidor-cdc-br para analisar uma compra online em que o consumidor quer desistir cinco dias apos o recebimento.
```

### Politica de Privacidade

```text
Use $consumidor-cdc-br para revisar esta politica de privacidade de app, separando LGPD, CDC e Marco Civil.
```

### Marketplace

```text
Use $consumidor-cdc-br para estruturar uma reclamacao contra marketplace em que o vendedor sumiu apos o pagamento.
```

### Incidente de Seguranca

```text
Use $consumidor-cdc-br para triagem de incidente com planilha de clientes exposta, indicando dados faltantes e cautelas de comunicacao ANPD/titulares.
```

### Plataforma e Moderacao

```text
Use $consumidor-cdc-br para avaliar banimento de conta paga em plataforma digital, considerando CDC, LGPD, Marco Civil e termos de uso.
```

## Validacao

### Validacao Automatizada

Executado em `2026-07-03`:

```powershell
python <caminho-para-skill-creator>/scripts/quick_validate.py .
```

Resultado:

```text
Skill is valid!
```

### Validacao de Prontidao

Relatorio completo:

- `references/agent-readiness-validation.md`

Veredito:

```text
PRONTO E OTIMIZADO (PADRÃO GEMINI/ANTIGRAVITY)
```

### Casos de Teste

Arquivo:

- `evals/casos-teste.md`

Cobertura atual:

- compra online e arrependimento;
- vicio/defeito;
- cobranca indevida;
- preco divergente;
- SAC e dano moral;
- superendividamento;
- assinatura digital e renovacao automatica;
- politica de privacidade;
- alteracao de termos;
- marketplace;
- suspensao de conta em plataforma;
- remocao de conteudo de terceiro;
- logs, IP e porta logica;
- cookies e analytics;
- incidente de seguranca;
- transferencia internacional.

## Atualizacoes e Manutencao

### Historico

| Versao | Data | Mudancas principais |
|---|---|---|
| `1.1.0` | 2026-07-03 | Escopo ampliado para produtos digitais, politicas e comunicados. |
| `1.2.0` | 2026-07-03 | Reorganizacao reutilizavel, fontes oficiais, Marco Civil, plataformas e validacao de readiness. |
| `1.3.0` | 2026-07-03 | Inclusao robusta de LGPD, ANPD, incidentes, transferencia internacional, cookies e dados pessoais. |
| `1.4.0` | 2026-07-03 | Reestruturação para o padrão Gemini/Antigravity (references, resources, examples) e links Markdown. |

### Rotina Recomendada

Revalidar quando houver:

- alteracao no CDC, LGPD, Marco Civil ou decretos correlatos;
- nova regulamentacao da ANPD;
- nova orientacao relevante da Senacon/MJSP;
- mudanca relevante em Consumidor.gov.br;
- jurisprudencia qualificada nova do STJ/STF;
- inclusao de novos templates ou checklists.

Checklist de manutencao:

1. Conferir `references/fontes-oficiais.md`.
2. Atualizar `references/pesquisa-e-atualizacao.md` se o procedimento mudar.
3. Atualizar matriz e checklists afetados.
4. Adicionar caso em `evals/casos-teste.md`.
5. Rodar `quick_validate.py .`.
6. Registrar a mudanca em `VALIDATION_REPORT.md`.

## Limites e Cuidados

O agente deve evitar:

- prometer resultado juridico;
- afirmar "causa ganha";
- inventar artigo, sumula, tema, prazo ou jurisprudencia;
- tratar fonte secundaria como lei vigente;
- afirmar dano moral automatico;
- afirmar inversao automatica do onus da prova;
- tratar politica de privacidade como documento resolvido apenas pelo CDC;
- dizer que termo, politica, contrato ou comunicado esta "100% conforme";
- orientar quebra de sigilo, invasao, coleta abusiva de logs ou exposicao de dados pessoais.

Encaminhe para advogado, Defensoria, Procon, ANPD, Anatel, Ministerio Publico, autoridade policial ou regulador setorial quando houver risco relevante.

## Licença

Este repositório utiliza um modelo de licenciamento duplo para separar o conteúdo explicativo e instruções de uso do material de templates reutilizável:

*   **Código, Configurações e Modelos (`assets/`, arquivos de configuração e scripts):** Licenciados sob a **Apache License 2.0**. Consulte o arquivo [LICENSE](file:///LICENSE) para os termos completos.
*   **Documentação e checklists (`references/`, `evals/` e guias gerais):** Licenciados sob a licença **Creative Commons Attribution 4.0 International (CC-BY-4.0)**. Consulte o arquivo [LICENSE-docs](file:///LICENSE-docs) para mais detalhes.

## Referencias de Formato Consultadas

Este README foi estruturado com base em padroes publicos de skills e documentacao para agentes, incluindo:

- [Anthropic Skills](https://github.com/anthropics/skills)
- [OpenAI Codex Agent Skills](https://developers.openai.com/codex/skills)
- [AGENTS.md](https://github.com/agentsmd/agents.md)
- [VoltAgent awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)
- [Composio awesome-codex-skills](https://github.com/composiohq/awesome-codex-skills)

Essas referencias foram usadas apenas para orientar estrutura documental: proposito, compatibilidade, instalacao, organizacao, validacao e limites.

<!-- GitAds-Verify: TF15EYG6NWID86UYPY9VR79V4SFUPJGD -->
