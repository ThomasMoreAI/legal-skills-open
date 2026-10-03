---
name: termination-review-bossmann007
title: /termination-review
description: Revisão de rescisão — detecção de flags de alto risco (estabilidades), verbas rescisórias + homologação, e prazo de pagamento conforme CLT art. 477. Regras específicas de base territorial/CCT e requisitos de assistência sindical são pesquisados por revisão, não armazenados. Use quando o usuário disser "revisando uma rescisão", "podemos dispensar essa pessoa", "revisão de rescisão", ou descrever um cenário de dispensa.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/employment-legal/skills/termination-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: employment
language: en
---

# /termination-review

1. Carregar `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → gatilhos de revisão de rescisão, flags de alto risco, prática de verbas rescisórias, regras de base territorial.
2. Usar o workflow abaixo.
3. Percorrer o checklist. Verificar toda flag de alto risco.
4. Prazo de pagamento das verbas conforme CLT art. 477 (10 dias corridos). Verbas rescisórias + homologação/assistência sindical se aplicável. [verified: https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452compilado.htm]
5. Se qualquer flag de alto risco disparar: escalar conforme tabela, não prosseguir sem aprovação.

---

## Matter context

**Matter context.** Verificar `## Matter workspaces` no CLAUDE.md de nível prática. Se `Enabled` for `✗` (padrão para in-house), pular o resto deste parágrafo — os skills usam contexto de nível prática e a mecânica de matéria fica invisível. Se habilitado e não houver matéria ativa, perguntar: "Para qual matéria é isso? Rode `/employment-legal:matter-workspace switch <slug>` ou diga `practice-level`." Carregar o `matter.md` da matéria ativa para contexto e overrides específicos. Gravar outputs na pasta da matéria em `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/<matter-slug>/`. Nunca ler arquivos de outra matéria a menos que `Cross-matter context` esteja `on`.

---

## Purpose

A maioria das rescisões corre bem. Algumas são reclamação trabalhista
esperando para acontecer. Este skill roda o checklist que pega o segundo tipo
antes que a decisão seja definitiva. O skill não afirma a lei — toda regra
específica de base territorial/CCT e requisito de assistência sindical é
pesquisada e citada no momento da revisão.

## Load context

`~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → gatilhos de revisão de rescisão, flags de alto risco, verbas rescisórias padrão, tabela de base territorial/CCT.

## Output header

Antepor o cabeçalho de sigilo profissional de `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → `## Outputs` (difere por papel do usuário — ver `## Who's using this`). Seguir o formato de memorando dos memorandos-semente de rescisão referenciados nessa config, se existir. O cabeçalho de sigilo profissional vem sempre primeiro.

## Workflow

### Step 1: Os fatos básicos

- Nome do empregado (ou função, se mantendo abstrato)
- Base territorial/categoria (onde trabalha, qual CCT se aplica)
- Motivo da dispensa (desempenho, justa causa, dispensa sem justa causa,
  extinção de posto, PDV/dispensa coletiva)
- Tempo de casa (relevante para aviso prévio proporcional, Lei 12.506/2011, e
  multa FGTS)
- Situação de saúde/afastamento (relevante para estabilidade acidentária)
- Se outros empregados estão sendo dispensados no mesmo contexto (relevante
  para regras de dispensa coletiva — negociação coletiva prévia)
- Data planejada da rescisão

### Step 2: Varredura de flags de alto risco

Este é o passo mais importante. Verificar toda flag de
`~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md`. Conjunto padrão:

| Flag | Por que é alto risco | Verificar |
|---|---|---|
| **Estabilidade gestante** | Nulidade da dispensa + reintegração ou indenização do período (CF art. 10, II, "b", ADCT; Súmula 244 TST) | A empregada está grávida (mesmo que a empresa não soubesse no momento da dispensa)? Estabilidade vai da confirmação da gravidez até 5 meses após o parto. |
| **Estabilidade acidentária** | Nulidade da dispensa + reintegração (Lei 8.213/1991 art. 118) | Empregado afastado por acidente de trabalho ou doença ocupacional nos últimos 12 meses após retorno/alta do INSS (auxílio-doença acidentário, código B91)? |
| **Estabilidade de dirigente sindical/CIPA** | Nulidade da dispensa (CF art. 8º, VIII; CLT art. 165 e art. 10, II, "a" ADCT) | Empregado é membro eleito da CIPA (titular ou suplente) ou dirigente/representante sindical com mandato vigente ou até 1 ano após? |
| **Denúncia recente (assédio, irregularidade, CAT)** | Indício de dispensa retaliatória, agravado por normas de combate ao assédio (Lei 14.457/2022) | Esse empregado registrou denúncia de assédio, reclamação interna, ou abriu CAT (Comunicação de Acidente de Trabalho) recentemente? |
| **Proximidade de aposentadoria/estabilidade pré-aposentadoria contratual** | Se prevista em CCT/acordo, pode gerar nulidade | Alguma CCT/ACT aplicável prevê estabilidade pré-aposentadoria? Empregado está no período coberto? |
| **Documentação rasa** | Problema de "por que agora" | Para dispensa por desempenho: há advertências, PDI, feedback documentado? Ou surgiu do nada? |
| **Comparador** | Tratamento discriminatório/isonomia | Outro empregado faz a mesma coisa e não está sendo dispensado? |
| **Promessa em contrato/regulamento** | Descumprimento gerando indenização | A carta-proposta, o regulamento interno, ou algo por escrito promete um processo que não está sendo seguido? |
| **Enquadramento art. 62 CLT questionável** | Passivo de horas extras retroativo | Ver a checagem de enquadramento abaixo. |

**Flag de enquadramento art. 62 CLT.** Disparar esta flag quando TODAS as
condições a seguir forem verdadeiras:

1. O empregado está classificado como enquadrado no art. 62 CLT (sem controle
   de jornada, sem direito a horas extras) — **E**
2. A função tem "supervisor", "coordenador", "analista", "administrador," ou
   "especialista" no título (case-insensitive, e qualquer título de escopo
   equivalente que o perfil da prática sinalize como arriscado) — **E**
3. A gratificação de função paga é inferior a ~40% do salário-base (parâmetro
   de referência do entendimento consolidado sobre cargo de confiança) ou não
   há evidência de poder de gestão real.

Quando as três disparam, emitir:

> 🔴 **Possível enquadramento indevido (art. 62 CLT)** — [título] recebendo
> [gratificação] em [base territorial]. O entendimento consolidado exige poder
> de gestão real e gratificação compatível para sustentar a exceção de
> controle de jornada `[conhecimento do modelo — verificar]`. Antes da
> dispensa, encaminhar para `/employment-legal:wage-hour-qa` para checagem de
> enquadramento — um empregado mal enquadrado que é dispensado tem uma
> reclamação trabalhista pronta por horas extras retroativas com reflexos
> (FGTS, 13º, férias, INSS), sujeita a prescrição de até 5 anos (CF art. 7º,
> XXIX), o que o acordo de rescisão pode não conseguir quitar de forma limpa.

Não suprima esta flag porque o título "parece gerencial" — a premissa da
reclamação de enquadramento indevido é justamente que títulos enganam.
Encaminhar para `/employment-legal:wage-hour-qa` para o teste real de poder de
gestão e gratificação.

**Se um valor de passivo está sendo calculado como parte desta revisão
(modelagem de acordo, exposição estimada), NÃO calcule nesse skill.**
Encaminhar para `wage-hour-qa` → checagem de horas extras e usar seu roteiro
de base de cálculo: integração de comissões/prêmios/adicionais na
remuneração-base, adicional mínimo de 50% (CF art. 7º, XVI) ou 100% se
previsto em CCT, reflexos em DSR/13º/férias/FGTS, e prescrição
quinquenal/bienal (CF art. 7º, XXIX). Todo número de passivo carrega
`[verificar — consultar especialista em jornada/remuneração antes de afirmar
ou pagar]`. Um número que parece limpo mas está errado aqui é o modo de falha
específico que este roteiro previne.

**Qualquer flag disparada → escalar conforme
`~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` antes
de a rescisão prosseguir.** Não depois. Antes.

### Step 3: Exigências específicas de base territorial/CCT

> **Pesquisar as regras aplicáveis à base territorial do empregado antes de
> finalizar o plano.** Especificamente:
>
> - Prazo de pagamento das verbas rescisórias — CLT art. 477, §6º: 10 dias [verified: https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452compilado.htm]
>   corridos a contar do término do contrato, para qualquer modalidade de
>   rescisão. Atraso gera multa de 1 salário do empregado (art. 477, §8º).
>   Pesquisar se há regra adicional na CCT aplicável.
> - Assistência sindical/homologação — pesquisar se a CCT da categoria exige
>   assistência do sindicato para validade da rescisão (não é mais exigência
>   legal geral desde a Reforma Trabalhista, mas pode ser cláusula
>   convencional).
> - Quitação anual (CLT art. 507-B) — há termo de quitação anual firmado
>   perante o sindicato? Isso limita o que pode ser discutido depois.
> - Avisos obrigatórios — comunicação de dispensa ao eSocial, guia de
>   seguro-desemprego (se aplicável), chave de conectividade social/FGTS para
>   saque.
> - Dispensa coletiva/PDV — pesquisar o entendimento do STF (Tema 638, RE
>   999435) sobre a exigência de negociação coletiva prévia com o sindicato
>   para dispensa em massa, e qualquer previsão de PDV na CCT aplicável
>   (adesão a PDV, quando prevista em norma coletiva, pode gerar quitação
>   ampla e irrestrita, Súmula/entendimento do STF sobre o tema).
>
> Citar fontes primárias. Verificar atualidade.
>
> **Sem suplemento silencioso.** Se uma pesquisa na ferramenta de pesquisa
> jurídica configurada retornar poucos ou nenhum resultado para a regra de
> prazo, assistência sindical, ou aviso da base territorial, reportar o que
> foi encontrado e parar. NÃO preencher a lacuna com busca web ou conhecimento
> do modelo sem perguntar. Dizer: "A busca retornou [N] resultados de
> [ferramenta]. Cobertura parece rasa para [base/regra]. Opções: (1) ampliar a
> busca, (2) tentar outra ferramenta de pesquisa, (3) buscar na web —
> resultados marcados `[busca web — verificar]` e devem ser checados contra
> fonte primária antes de confiar, ou (4) parar aqui e sinalizar para
> verificação do advogado. Qual você prefere?" O advogado decide se aceita
> fontes de confiança menor.
>
> **Atribuição de fonte.** Marcar cada citação no plano — regra de prazo,
> assistência sindical, avisos, dispensa coletiva, restrições de quitação —
> com sua origem: `[JusBrasil]`, `[TST]`, `[STF]`, ou o nome da ferramenta MCP
> para citações obtidas de conector de pesquisa jurídica; `[busca web —
> verificar]` para citações de busca web; `[conhecimento do modelo —
> verificar]` para citações lembradas do treinamento; `[fornecido pelo
> usuário]` para citações que o usuário forneceu. Citações marcadas
> `verificar` carregam maior risco de fabricação e devem ser checadas
> primeiro. Nunca remova ou colapse as tags.

### Step 4: Verbas rescisórias e quitação

Conforme `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → verbas rescisórias padrão:

- Verbas devidas: saldo de salário, aviso prévio (trabalhado ou indenizado,
  proporcional conforme Lei 12.506/2011), 13º proporcional, férias vencidas e
  proporcionais + 1/3, multa FGTS 40% (dispensa sem justa causa) ou 20%
  (rescisão por acordo, CLT art. 484-A).
- Rescisão por acordo (CLT art. 484-A) sendo usada? Ela reduz o aviso prévio
  pela metade, a multa FGTS para 20%, e libera só 80% do saldo do FGTS —
  confirmar que o empregado entende a diferença frente à dispensa sem justa
  causa integral.

> **Pesquisar as regras de quitação aplicáveis.** Se há termo de quitação
> anual (art. 507-B) ou termo de rescisão homologado com assistência
> sindical, isso amplia o efeito de quitação. Pesquisar o entendimento
> corrente do TST sobre o alcance da quitação em cada modalidade — não afirme
> o alcance de memória. Citar fontes primárias. Verificar atualidade.

Separadamente, considerar se algum dos seguintes se aplica ao termo de
rescisão:
- Cláusula de confidencialidade sobre o valor do acordo e sobre o motivo da
  saída.
- Restrições da CCT aplicável sobre o que pode ser quitado ou exigência de
  cláusula específica.
- Regras sobre não-divulgação relacionadas a denúncia de assédio ou
  discriminação — cuidado ao redigir cláusula de confidencialidade que possa
  ser lida como abafamento de denúncia (Lei 14.457/2022).

### Step 5: Checagem de documentação

Especialmente para dispensas por desempenho:

- Há histórico documentado? Advertências, PDI (Plano de Desenvolvimento
  Individual), registros de feedback?
- O histórico conta uma história consistente?
- Há algo por escrito que contradiga o motivo (avaliação positiva recente,
  bônus, promoção)?

A pergunta "por que agora": se essa pessoa está com baixo desempenho há um
ano, o que mudou? A resposta deveria estar documentada.

## Output

> **Pré-flight de conector de pesquisa.** Antes de emitir o memorando,
> verificar se um conector de pesquisa jurídica está acessível nesta sessão —
> JusBrasil, TST, ou qualquer MCP de pesquisa configurado pela firma.
> Consolidar isso na nota do revisor conforme CLAUDE.md `## Outputs`: se
> nenhum conector retornar resultados no Step 3 (ou nenhum estiver
> configurado), registrar na linha **Sources:** da nota do revisor — ex.:
> `não conectado — citações de conhecimento de treinamento; os tópicos de
> maior risco de fabricação em memorandos de rescisão são prazo de pagamento
> (art. 477), alcance da quitação anual (art. 507-B), e exigência de
> negociação coletiva prévia para dispensa em massa (Tema 638 STF) —
> checar esses primeiro`. Tags `[conhecimento do modelo — verificar]` por
> citação permanecem inline. Não emitir um banner separado acima do
> memorando.

> **Premissa de base territorial.** Esta revisão assume a base
> territorial/categoria do empregado conforme declarado no Step 1 e quaisquer
> padrões de `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → Abrangência territorial. Regras trabalhistas, prazo de
> pagamento, exigência de quitação e obrigações de aviso variam materialmente
> por base/CCT. Se o empregado trabalha em base diferente, ou se a CCT
> aplicável é disputada, esta análise pode não valer como redigida.

Seguir o formato de memorando dos memorandos-semente de rescisão referenciados
em `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md`. Se
não houver:

```markdown
[CABEÇALHO DE SIGILO PROFISSIONAL — conforme config do plugin ## Outputs — difere por papel; ver `## Who's using this`]

## Revisão de Rescisão: [Função/Nome] — [Data]

**Base territorial/CCT:** [Estado/Categoria]
**Motivo:** [Desempenho / Justa causa / Sem justa causa / Extinção de posto / PDV]
**Data planejada:** [Data]

---

### Conclusão

[Pode prosseguir / Precisa corrigir X primeiro / Parar — motivo em uma frase]

---

### Flags de alto risco

[Toda flag do Step 2. ✅ Sem flag ou 🔴 FLAG com detalhe.]

**Escalonamento:** [Não necessário | Escalar para [nome] antes de prosseguir — [qual flag]]

---

### Exigências de base territorial/CCT ([Estado/Categoria])

- Prazo de pagamento: [regra pesquisada e citada — CLT art. 477, §6º, 10 dias corridos]
- Avisos obrigatórios: [lista, cada um pesquisado e citado]
- Dispensa coletiva (se aplicável): [regra pesquisada e citada — Tema 638 STF]

---

### Verbas rescisórias e quitação

- Verbas: [valores por fórmula / conforme calculado]
- Modalidade: [sem justa causa / por acordo art. 484-A / justa causa]
- Quitação: [termo de quitação anual aplicável / termo de rescisão homologado
  — pesquisar e aplicar o alcance de quitação corrente do TST; citar fontes
  primárias e verificar atualidade]
- [Quaisquer restrições de CCT ou cláusulas de confidencialidade/não-divulgação aplicáveis]

---

### Documentação

[Avaliação do histórico documentado. Lacunas sinalizadas.]

---

### Ir / Não ir

[Liberado para prosseguir | Prosseguir com as mudanças abaixo | Aguardar — escalonamento pendente]

### Checklist do dia da rescisão

- [ ] Verbas rescisórias prontas, valor correto, pagamento dentro do prazo do art. 477
- [ ] Comunicação ao eSocial preparada
- [ ] Guia de seguro-desemprego preparada (se aplicável)
- [ ] Termo de rescisão (TRCT) com a modalidade correta e, se exigido pela CCT, assistência sindical agendada
- [ ] Devolução de bens/corte de acesso coordenado
- [ ] [etc.]
```

## Consequential-action gate (dispensar um empregado)

**Antes de produzir uma recomendação "Ir" ou um checklist do dia da rescisão
marcado como pronto:** ler `## Who's using this` em
`~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md`. Se o Papel for **Não-advogado**:

> Dispensar um empregado tem consequências jurídicas — reintegração por
> estabilidade, dispensa discriminatória/retaliatória, e reclamação de horas
> extras retroativas todas remontam a como essa decisão é estruturada. Você
> revisou essa rescisão com um advogado? Se sim, prossiga. Se não, aqui está
> um resumo para levar a ele:
>
> - Empregado, base territorial, motivo, data planejada
> - Toda flag de alto risco que a revisão levantou (estabilidade gestante,
>   acidentária, CIPA/sindical, denúncia recente, documentação rasa,
>   comparador, promessa em contrato) — com detalhe
> - Achados de base territorial/CCT (prazo, avisos, regras de dispensa
>   coletiva) e de onde foram citados
> - Análise de verbas rescisórias/quitação, incluindo eventuais ângulos de
>   estabilidade
> - Perguntas em aberto e o que está sem resolver
> - O que pode dar errado (a tese de ação que esse padrão de fatos sustenta)
> - O que perguntar ao advogado (essa é uma dispensa limpa; precisamos de mais
>   documentação primeiro; o termo de quitação precisa de linguagem
>   específica; precisamos escalonar as dispensas coletivas)
>
> Se precisar encontrar um advogado: use o serviço de indicação da OAB da sua
> seccional. Trabalhista é uma área em que uma consulta curta antes da reunião
> de dispensa consistentemente supera em valor uma defesa de reclamação
> depois da dispensa.

Não produza um output "Liberado para prosseguir" além deste gate sem um "sim"
explícito. Um rascunho marcado como DRAFT sinalizado para revisão do advogado
está ok.

---

## Close with the next-steps decision tree

Encerrar com a árvore de decisão de próximos passos conforme CLAUDE.md
`## Outputs`. Customizar as opções para o que este skill acabou de produzir —
os cinco ramos padrão (rascunhar X, escalar, buscar mais fatos, aguardar e
observar, outra coisa) são um ponto de partida, não uma obrigação. A árvore é
o output; o advogado escolhe.

## What this skill does not do

- Tomar a decisão de dispensar. Verifica a decisão.
- Ter a conversa. O gestor faz isso.
- Afirmar regras de quitação ou de base territorial de memória — toda regra é
  pesquisada e citada no momento da revisão.
- Garantir ausência de reclamação trabalhista. Reduz o risco pegando os
  problemas óbvios.
