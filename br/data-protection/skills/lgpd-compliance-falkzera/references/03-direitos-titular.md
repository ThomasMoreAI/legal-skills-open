# 03: Direitos do Titular (Art. 18), o que CONSTRUIR no app

> Self-service no app cobre ~80% dos pedidos. Canal do DPO cobre os 20% complexos (reclamações, contestações de decisão automatizada, casos com terceiros). Os 9 direitos são **gratuitos** e atendidos **a qualquer momento mediante requisição** (art. 18 caput + §5º).

## Os 9 direitos (art. 18 LGPD)

### I: Confirmação da existência de tratamento

**Lei:** "confirmação da existência de tratamento"

**O que construir:**
- Tela autenticada `/privacidade` que responde sim/não: "Sim, tratamos dados sobre você."
- Resposta em **formato simplificado, IMEDIATA** (art. 19 I).
- Pra pedido externo (e-mail), fluxo de verificação de identidade (token por e-mail/SMS) antes de confirmar.

### II: Acesso aos dados

**Lei:** "acesso aos dados"

**O que construir:**
- Tela "Meus dados" listando perfil + transações + logs.
- Combinado com art. 19 II: declaração completa contendo **origem dos dados, critérios usados, finalidade do tratamento**, em até **15 dias** (regime geral) ou **30 dias** (pequeno porte).
- Não basta exibir o registro, precisa explicar de onde veio cada campo (cadastro próprio? integração? cookie?).

### III: Correção de dados incompletos, inexatos ou desatualizados

**O que construir:**
- Edição de perfil (cobre 80%).
- Pra campos não-editáveis (CPF, e-mail verificado): solicitar via canal do DPO + audit log (quem, quando, valor antigo → novo).
- Se o dado errado foi compartilhado com terceiros, **comunicar a correção** a esses terceiros (art. 18 §6º).

### IV: Anonimização, bloqueio ou eliminação de dados desnecessários, excessivos ou tratados em desconformidade

**Diferente do VI:** o gatilho aqui é **excesso/desnecessidade**, não revogação de consentimento.

**O que construir:**
- Endpoint admin pra mascarar campos específicos por requisição.
- Anonimização **verdadeira**: hash irreversível + remoção de identificadores diretos e indiretos.
- Bloqueio temporário: flag `is_blocked` que impede leitura sem deletar.

### V: Portabilidade dos dados

**Lei:** "portabilidade dos dados a outro fornecedor de serviço ou produto, mediante requisição expressa, de acordo com a regulamentação da autoridade nacional, observados os segredos comercial e industrial"

**O que construir:**
- Endpoint **`GET /api/legal/export`** retornando JSON estruturado e legível por máquina.
- **NÃO exportar dados inferidos pelo seu algoritmo** (segredo industrial). Exportar o que o usuário forneceu + dados objetivamente coletados.
- Schema documentado (template em `templates/endpoints-direitos/`).

### VI: Eliminação dos dados tratados com consentimento

**Lei:** "eliminação dos dados pessoais tratados com o consentimento do titular, exceto nas hipóteses previstas no art. 16"

**O que construir:**
- Botão **"Excluir minha conta"** no mesmo nível visual do "Criar conta". Não escondido.
- Fluxo de hard-delete ou pseudonimização irreversível.
- Backups: política de purga (não basta deletar do banco principal, agendar purga do backup respeitando retenção mínima).
- **Diferenciar visualmente** o que será apagado x o que será **retido por obrigação legal** (cruzar com `04-matriz-retencao.md`).

### VII: Informação sobre compartilhamento

**O que construir:**
- Política de privacidade lista os processadores (genérico), mínimo viável.
- Ideal: log por usuário ("seu CEP foi enviado pra Correios em 2026-04-12 às 14:32").
- Lista nominal de terceiros sempre atualizada.

### VIII: Informação sobre possibilidade de não fornecer consentimento e consequências

**O que construir:**
- No momento do consentimento: **explicar o que acontece se recusar**.
  - Ex: "Sem consentimento de geolocalização, você não verá restaurantes próximos, mas o app continua funcional."
- Vedados dark patterns ("Aceitar e continuar" / "Cancelar e sair" sem alternativa).
- Tem que existir caminho de uso sem consentimento opcional.

### IX: Revogação do consentimento

**Lei:** "revogação do consentimento, nos termos do § 5º do art. 8º"

**O que construir:**
- Tela **"Preferências de Privacidade"** com toggle individual por consentimento.
- Revogação tão fácil quanto consentir (art. 8º §5º). Se foi 1 clique, revogar é 1 clique.
- **Consent log** com timestamp e estado de cada consentimento (prova pra ANPD).

## Prazos de resposta (art. 19 + Res. 2/2022)

| Requisição | Regime geral | Pequeno porte |
|---|---|---|
| Confirmação simplificada (art. 19 I) | **Imediata** | até 15 dias |
| Declaração completa (art. 19 II) | até **15 dias** | até **30 dias** |
| Demais requisições (correção, eliminação, portabilidade) | **Razoável** (sem prazo fechado) | em dobro |

**Sempre gratuita** (art. 18 §5º). Proibido cobrar taxa, **mesmo em casos repetidos**.

## Dados de crianças e adolescentes (art. 14)

**Texto:** *"O tratamento de dados pessoais de crianças deverá ser realizado com o consentimento específico e em destaque dado por pelo menos um dos pais ou pelo responsável legal."* (§1º)

**Enunciado ANPD 24/05/2023:** ampliou a interpretação, dados de crianças/adolescentes podem usar **qualquer base do art. 7º ou 11**, desde que respeitado o **melhor interesse**. Consentimento parental segue como via padrão quando o serviço é oferecido diretamente à criança.

### O que construir

- **Verificação de idade no onboarding**, perguntar **data de nascimento completa**, não "tem mais de 18?".
- Se `< 12` (criança) ou `< 18` (adolescente): trigger fluxo diferente.
- **Consentimento parental verificável** pra crianças: link por e-mail ao responsável, com algum grau de prova (cartão tokenizado R$0,01, upload de documento, verificação por chamada).
- Art. 14 §5º: *"esforços razoáveis considerando as tecnologias disponíveis"*, proporcional ao risco do serviço.
- Art. 14 §3º: **proibido condicionar** participação a fornecer dados além do necessário.
- Art. 14 §6º: linguagem **acessível à criança** (audiovisual quando adequado).

## Decisões automatizadas (art. 20)

### Quando se aplica
- Score de crédito (clássico).
- Aprovação/recusa automática (cadastro, financiamento, seguro).
- Perfilamento publicitário (categoria de consumo).
- Algoritmo de recomendação que decide o que o titular vê.
- Anti-fraude que bloqueia contas sem revisão humana.
- Precificação dinâmica baseada em perfil.

### O que construir

- **Disclosure no momento da decisão**: "Esta decisão foi tomada automaticamente com base em [critérios resumidos]."
- **Endpoint de explicação**: clicar "por que essa decisão?" → explicação em linguagem natural dos principais fatores (sem revelar pesos exatos do modelo, se for segredo).
- **Fluxo de contestação**: botão "Contestar" → ticket pra revisão (preferencialmente humana), com SLA explícito.
- **Log da decisão**: input, output, versão do modelo, timestamp, pra auditoria.

> **Nota:** a versão original do art. 20 exigia revisão **por pessoa natural**; uma MP removeu essa exigência. Hoje o texto não obriga revisão humana, mas a melhor prática (e o que a ANPD está direcionando) aponta pra revisão por humano qualificado.

## Canal de atendimento ao titular

### Exigências (art. 41)
- **Obrigatório pra todos**, incluindo MEs/EPPs que não precisam designar DPO formal mas precisam de canal (Res. 2/2022 art. 11).
- **Encarregado é o ponto focal** (art. 41 §2º I): aceitar reclamações dos titulares.
- **Identidade e contato em destaque no site** (art. 41 §1º).

### Forma: boa prática combinada

1. **E-mail dedicado** (`dpo@empresa.com.br` ou `privacidade@empresa.com.br`), baixo atrito, trilha escrita.
2. **Formulário web** com campos estruturados (tipo de pedido do art. 18, identificação, comprovação). Bom pra triagem.
3. **Tela "Privacidade" autenticada no app** pra usuários logados: **self-service** cobre 80%.

**Combinação ideal:** self-service no app (acesso, portabilidade, exclusão, revogação) + e-mail do DPO (reclamações, casos complexos, contestação de decisão automatizada).

### O que precisa estar na Política de Privacidade

- Nome e contato do encarregado (ou canal genérico se pequeno porte).
- Lista dos 9 direitos do art. 18 (literal).
- Como exercer cada direito (URL do self-service ou e-mail).
- Prazo de resposta esperado.
- **Direito de reclamar à ANPD** ([canal de petição em gov.br/anpd](https://www.gov.br/anpd/pt-br/canais_atendimento/cidadao/peticao-de-titular)).

## Checklist mínimo de implementação

- [ ] Tela autenticada `/privacidade` com confirmação imediata + lista de dados
- [ ] Endpoint `GET /api/legal/export` retornando JSON estruturado
- [ ] Botão "Excluir minha conta" no mesmo nível do botão de cadastro
- [ ] Painel de consentimentos granular com toggle de revogação
- [ ] Checkbox de consentimento vazio por padrão, com log do aceite (consent_log)
- [ ] Verificação de idade no onboarding + fluxo parental se `< 18`
- [ ] Matriz de retenção codificada (dado × base × prazo), ver `04-matriz-retencao.md`
- [ ] Disclosure de decisões automatizadas + fluxo de contestação
- [ ] E-mail `dpo@` ou `privacidade@` publicado no site (footer)
- [ ] Audit log de: consentimentos, correções, exportações, exclusões, contestações
- [ ] SLA interno documentado: simplificado imediato, completo em 15/30 dias

## Referências externas

- [LGPD Art. 18 (Planalto)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm#art18)
- [LGPD Art. 19 (Planalto)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm#art19)
- [LGPD Art. 14 (crianças e adolescentes) (Planalto)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm#art14)
- [LGPD Art. 20 (decisões automatizadas) (Planalto)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm#art20)
- [Enunciado ANPD 24/05/2023 (Dados de Crianças e Adolescentes)](https://www.gov.br/anpd/pt-br/assuntos/noticias/anpd-divulga-enunciado-sobre-o-tratamento-de-dados-pessoais-de-criancas-e-adolescentes)
- [Resolução CD/ANPD nº 18/2024 (Encarregado de Dados)](https://www.gov.br/anpd/pt-br/canais_atendimento/encarregado-de-dados-na-anpd)
- [Petição de Titular (ANPD)](https://www.gov.br/anpd/pt-br/canais_atendimento/cidadao/peticao-de-titular)
