---
name: oss-review-bossmann007
title: /oss-review
description: Verificação de conformidade de licença open source para lista de dependências, uma única biblioteca, ou código de saída. Use ao revisar um manifesto, SBOM, ou repositório em busca de obrigações de copyleft e compatibilidade de licença, quando perguntado se uma biblioteca pode ir a produção, ou ao preparar código para ser open-sourced.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/ip-legal/skills/oss-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: ip
language: pt
---

# /oss-review

Roda verificação de conformidade de licença open source contra o perfil de prática em `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`. Classifica dependências por família de licença, mapeia obrigações ao modelo de deployment, sinaliza pacotes de licença desconhecida e licenças não-OSI disfarçadas de open source, e recomenda ações — cumprir, substituir, remover, buscar revisão jurídica, buscar licença comercial.

## Instructions

1. **Carregue `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`.** Se houver placeholders, pare e pergunte: "Rode `/ip-legal:cold-start-interview` primeiro — preciso conhecer seu perfil de prática (e política de OSS, se houver) antes de revisar." Se o perfil de prática aponta para uma política de OSS carregada, leia também — é a fonte da verdade sobre licenças aceitas / em revisão / banidas nesse time.

2. **Estabeleça o escopo:** uma lista de dependências (package.json, requirements.txt, go.mod, Gemfile, Cargo.toml, pom.xml, SBOM), uma única biblioteca, ou código de saída que o time está preparando para abrir. Se o usuário passou um path, infira do arquivo; senão pergunte.

3. **Estabeleça o modelo de deployment** antes de classificar obrigações — SaaS, binário distribuído, apenas interno, ou embarcado. A mesma lista de dependências dispara obrigações diferentes dependendo disso.

4. **Siga o workflow abaixo.** Em particular:
   - Leia o texto real da licença, não apenas metadados — arquivos LICENSE podem estar errados, metadados de gerenciador de pacote podem estar desatualizados.
   - Classifique cada pacote em permissiva / copyleft fraco / copyleft forte / domínio público / não-OSI / desconhecida.
   - Sinalize licença desconhecida como "precisa revisão," não permissiva por padrão.
   - Sinalize licenças source-available não-OSI (SSPL, BUSL, Commons Clause, Elastic License, fair-source) — não são open source.
   - Para código de saída, verifique se a licença de saída escolhida é compatível com toda dependência embarcada.

5. **Produza o memorando** conforme template abaixo — cabeçalho de trabalho protegido primeiro, resumo executivo, flags de topo de memorando, blocos por pacote agrupados por severidade, nota de jurisdição, verificação de saída (se aplicável), roteamento de aprovação.

6. **Respeite a postura de decisão.** Quando uma análise de gatilho de copyleft depende de questão contestada ("interação em rede" da AGPL, "conveying" da GPL-3.0, escopo de linking da LGPL), sinalize para revisão de advogado e mostre os fatores que pesam em ambas direções. Qualquer coisa sinalizada como copyleft forte ou licença desconhecida vai a um advogado antes da dependência ir a produção ou o código ser liberado.

## Examples

```
/ip-legal:oss-review ~/code/meu-projeto/package.json
/ip-legal:oss-review ~/code/meu-projeto/requirements.txt
/ip-legal:oss-review redis
/ip-legal:oss-review ~/code/meu-projeto  # raiz do repositório — varre todos os manifestos
```

---

## Works better connected

Pedidos de liberação de OSS costumam entrar via sistema de tickets. Conectado a
Jira, Linear, ou Asana, este skill pode: monitorar pedidos de OSS recebidos,
responder com orientação diretamente no ticket (sinalizando informação
incompleta, pedindo o link do repositório, retornando a classificação de
família de licença), e rastrear status de liberação entre pedidos.

Sem conector, cole o ticket ou descreva o pedido e eu trato um de cada vez.
Ver `CONNECTORS.md` na raiz do repositório para como adicionar um conector de
ticketing.

## Matter context

**Contexto de matter.** Verifique `## Matter workspaces` no CLAUDE.md de nível de prática. Se `Enabled` é `✗` (padrão para usuários in-house), pule o resto deste parágrafo — skills usam contexto de nível de prática e a maquinaria de matter fica invisível. Se habilitado e não há matter ativo, pergunte: "Para qual matter é isso? Rode `/ip-legal:matter-workspace switch <slug>` ou diga `practice-level`." Carregue o `matter.md` do matter ativo para contexto e overrides específicos. Escreva outputs na pasta do matter em `~/.claude/plugins/config/claude-for-legal/ip-legal/matters/<matter-slug>/`. Nunca leia arquivos de outro matter a menos que `Cross-matter context` esteja `on`.

---

## Purpose

Diga ao usuário quais licenças estão na árvore de dependências, quais obrigações essas licenças disparam dado como o código será implantado, e o que fazer sobre cada uma. O output é um memorando que o advogado (ou o engenheiro com acesso a advogado) pode agir sobre — cumprir, substituir, remover, buscar revisão jurídica, buscar licença comercial.

**Isso é classificação de primeira passada.** Análise de copyleft depende do modelo de deployment, do grau de linking, da jurisdição, e às vezes de questões jurídicas não testadas em tribunal (notavelmente o "interage em rede" da AGPL, a cláusula de patente da GPL-3.0). Para qualquer coisa classificada como copyleft forte ou licença desconhecida, um advogado avalia antes da dependência ir a produção ou o código ser liberado. O skill reporta o que encontrou; o advogado decide o que fazer.

**No Brasil, software é protegido por regime sui generis.** A Lei 9.609/1998 (Lei do Software) rege a proteção jurídica do programa de computador; seu art. 2º determina que o regime de proteção à propriedade intelectual do software é o de direitos autorais (Lei 9.610/1998), aplicada subsidiariamente, mas com regras próprias — o prazo de proteção é de 50 anos (art. 2º §2º, contado de 1º de janeiro do ano subsequente à publicação ou criação), e os direitos morais do autor sobre o programa são limitados ao direito de reivindicar a paternidade e de opor-se a alterações não autorizadas que prejudiquem sua honra ou reputação (art. 2º §1º) — diferente do regime de direitos morais mais amplo aplicável a obras literárias sob a Lei 9.610/1998. Isso não muda a análise de compatibilidade de licenças open source em si (as licenças OSI — MIT, GPL, Apache etc. — são instrumentos contratuais internacionais que operam da mesma forma independente da jurisdição), mas importa para: (a) a lei aplicável a um contrato de licenciamento de saída que declare foro brasileiro, (b) a exigibilidade de cláusulas de garantia/isenção de responsabilidade sob o Código Civil e o CDC (Lei 8.078/1990, se o software for fornecido a consumidor), e (c) o registro opcional de programa de computador no INPI (Lei 9.609/1998 art. 3º) como prova de anterioridade — não constitutivo do direito, que nasce com a criação. [verified: https://www.planalto.gov.br/ccivil_03/leis/l9609.htm; https://www.planalto.gov.br/ccivil_03/leis/l9610.htm]

## Precondition: load the practice profile

**Antes de varrer dependências, leia `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`.** Se estiver ausente ou ainda contiver placeholders, pare e rode `/ip-legal:cold-start-interview`. O perfil de prática diz:

- Quem é dono da revisão de OSS nesse time (frequentemente engenharia com sign-off jurídico)
- Roteamento de escalonamento para obrigações de copyleft
- O cabeçalho de trabalho protegido a prefixar

Se o perfil de prática tem uma política de OSS carregada, leia também — é a fonte da verdade sobre quais licenças o time aceita, quais disparam revisão, e quais são banidas.

## Workflow

### Passo 1: Qual o escopo?

Pergunte (ou infira do que o usuário forneceu):

> O que estamos revisando?
>
> 1. **Uma lista de dependências** — `package.json`, `requirements.txt`, `go.mod`, `Gemfile`, `Cargo.toml`, `pom.xml`, um SBOM (SPDX / CycloneDX), um lockfile
> 2. **Uma única biblioteca** — um pacote específico que você está considerando adicionar
> 3. **Nosso próprio código** — planejamos abrir como open source e precisamos verificar o que está embarcado

O caminho de análise difere:

- Lista de dependências → classifica cada entrada, consolida obrigações
- Biblioteca única → classifica um pacote e percorre suas dependências transitivas se disponíveis
- Código de saída → verifica o que está embarcado (direto e transitivo), verifica se a licença de saída escolhida é compatível com todas as licenças embarcadas, verifica se os arquivos LICENSE / NOTICE estão corretos

### Passo 2: Qual o modelo de deployment?

Essa é a informação mais importante depois da lista de licenças — a mesma biblioteca carrega obrigações diferentes dependendo de como o software é entregue. Pergunte:

> Como isso será implantado?
>
> 1. **SaaS / serviço hospedado** — usuários acessam via rede; nada é enviado ao usuário
> 2. **Binário distribuído** — enviamos código compilado a usuários (app desktop, app mobile, servidor on-prem, ferramenta CLI)
> 3. **Apenas interno** — usado só dentro da empresa, não distribuído externamente
> 4. **Embarcado / firmware** — enviado em hardware ou como firmware de sistema fechado

| Deployment | Licenças que importam materialmente |
|---|---|
| SaaS | AGPL (gatilho de rede), atribuição permissiva em qualquer UI, SSPL/BUSL/Elastic se estivermos reaproveitando como serviço concorrente |
| Binário distribuído | GPL, LGPL, MPL, EPL (todas disparam na distribuição), atribuição permissiva |
| Apenas interno | A maioria do copyleft não dispara — sem distribuição. Atribuição permissiva ainda é boa prática. AGPL ainda dispara se usuários fora da empresa interagem via rede. |
| Embarcado / firmware | GPL é especialmente difícil de cumprir aqui (divulgação de código-fonte + build reproduzível + informação de instalação em alguns casos). Planeje isso antes do envio, não depois. |

Sinalize o modelo de deployment no memorando de output — a mesma lista de dependências revisada contra "SaaS" vs. "binário distribuído" gera obrigações diferentes.

### Passo 3: Classificar cada dependência

Para cada pacote, determine a licença. Leia o texto real da licença, não apenas metadados — arquivos LICENSE podem estar errados (o arquivo diz MIT mas os cabeçalhos dizem GPL; o README alega Apache mas não há arquivo de licença), e metadados de gerenciador de pacote podem estar desatualizados.

Classifique em:

| Categoria | Exemplos | Obrigações-chave |
|---|---|---|
| **Permissiva** | MIT, BSD-2-Clause, BSD-3-Clause, Apache-2.0, ISC, Zlib, Unlicense | Atribuição, preservar texto de licença, Apache-2.0 adiciona concessão de patente + requisito de NOTICE |
| **Copyleft fraco** | LGPL-2.1, LGPL-3.0, MPL-2.0, EPL-1.0, EPL-2.0, CDDL | Divulgação de fonte em nível de arquivo ou biblioteca; regras de linking variam |
| **Copyleft forte** | GPL-2.0, GPL-3.0, AGPL-3.0, OSL, EUPL (dependendo da versão) | Divulgação ampla de fonte; AGPL estende a uso em rede |
| **Domínio público / dedicação** | CC0, Unlicense, WTFPL | Tipicamente sem obrigações, mas algumas são contestadas em jurisdições que não reconhecem dedicação ao domínio público (no Brasil, a dedicação voluntária à obra em domínio público não é regime automático — a Lei 9.610/1998 art. 41 trata o domínio público como decorrência do decurso do prazo de proteção, não de renúncia; `[SME VERIFY]` a eficácia de uma licença CC0/Unlicense sob direito brasileiro) | [verified: https://www.planalto.gov.br/ccivil_03/leis/l9610.htm] [unverified: not found in primary source]
| **Source-available não-OSI** | SSPL, BUSL, Commons Clause, Elastic License, Confluent Community, família fair-source | Não é open source — restringe uso comercial, uso como serviço concorrente, ou ambos. Leia a licença específica. |
| **Outra / customizada / desconhecida** | específica de fornecedor, proprietária, sem arquivo de licença, conflito de licença entre arquivo e cabeçalhos | Pare — não trate como permissiva por padrão |

Sinalize:

- **Pacotes com dupla licença** — qual licença estamos usando? A escolha pode mudar obrigações.
- **Pacotes descontinuados** — o pacote não é mais mantido; há substituto suportado?
- **Pacotes com dependência copyleft na própria árvore** — a licença de topo é permissiva mas uma dependência transitiva é copyleft.
- **Pacotes que mudaram de licença recentemente** — Redis, MongoDB, Elastic, HashiCorp — confirme que a versão fixada está sob a licença que você pensa que está.

### Passo 4: Mapear obrigações ao modelo de deployment

Para cada dependência classificada, declare o que o modelo de deployment dispara:

```markdown
### [pacote@versão] — [Licença]

**Classificação:** [Permissiva / Copyleft fraco / Copyleft forte / Domínio público / Não-OSI / Desconhecida]

**Obrigações para nosso deployment ([SaaS / binário / interno / embarcado]):**

- [ ] [Obrigação específica — ex.: "Incluir atribuição em arquivo NOTICES enviado com o app"]
- [ ] [ex.: "Se modificarmos e distribuirmos, publicar código-fonte das modificações"]
- [ ] [ex.: "Gatilho de rede AGPL — se usuários acessam nossa versão modificada via rede, o código-fonte deve ser oferecido a eles"]

**Risco:** 🔴 Crítico | 🟠 Alto | 🟡 Médio | 🟢 Baixo

**Recomendação:** [Cumprir obrigações | Substituir por [alternativa] | Remover | Revisão de advogado antes de ir a produção | Buscar licença comercial de [fornecedor]]
```

> **Como a dependência copyleft é consumida?** A relação de linking determina se o copyleft de fato dispara. Pergunte ou determine:
> - **Linking estático / compilação junta:** As obras são combinadas em um binário. Sinal forte de que copyleft dispara (LGPL "obra baseada na Biblioteca," obra derivada GPL).
> - **Linking dinâmico / biblioteca compartilhada:** As obras permanecem separáveis em tempo de execução. LGPL permite explicitamente isso ("obra que usa a Biblioteca"). A posição da GPL é contestada (FSF diz que é derivada, outros discordam).
> - **Inclusão de header / funções inline:** Pode criar obra derivada dependendo de quanto é incluído.
> - **Subprocesso / IPC:** Processos separados comunicando via interfaces bem definidas. Geralmente não é derivada.
> - **Chamada de API via rede:** Para a maioria das licenças, não. Para **AGPL**, a cláusula de interação em rede significa que servir o software via rede É distribuição. Em arquitetura de microsserviços, um componente AGPL atrás de uma API ainda dispara.
> - **Copyleft em nível de arquivo (MPL):** Só os arquivos modificados carregam copyleft, não a obra inteira. Verifique se algum arquivo copyleft foi modificado.
>
> **A severidade depende disso.** "LGPL — copyleft fraco, regras de linking variam" sem a análise de linking é a resposta que faz um engenheiro ser processado. LGPL com linking estático em produto proprietário é 🔴 Crítico. LGPL com linking dinâmico é 🟢 Baixo. Mesma licença, classificação oposta.

**Calibração de severidade:**

| Nível | Significa |
|---|---|
| 🔴 Crítico | Copyleft forte em deployment que o dispara (ex.: GPL em binário distribuído, AGPL em SaaS). Licença não-OSI que conflita de fato com o modelo de negócio (ex.: SSPL enquanto construímos serviço gerenciado). Licença não pode ser determinada e o pacote é essencial. |
| 🟠 Alto | Copyleft fraco com obrigações para as quais o time não está preparado (divulgação em nível de arquivo, requisitos de NOTICE). Dupla licença onde a escolhida é ambígua. Arquivo de licença diz uma coisa, cabeçalhos dizem outra. |
| 🟡 Médio | Permissiva com requisitos de atribuição não incorporados ao build (arquivo NOTICES ausente, LICENSE ausente na distribuição). Copyleft transitivo em posição que pode ou não disparar, dependendo de como a biblioteca é consumida. |
| 🟢 Baixo | Permissiva com obrigações já satisfeitas. Copyleft em modelo de deployment que não o dispara (ex.: biblioteca GPL usada apenas internamente, sem redistribuição). |

### Passo 5: Sinalizar modos de falha

Aponte qualquer um dos seguintes em uma seção de topo de memorando:

- **Licença desconhecida** — classifique como "precisa revisão," não permissiva. Uma dependência não classificada deve parar uma decisão de ir a produção, não passar despercebida.
- **Arquivo de licença conflita com cabeçalhos de arquivo** — leia ambos e reporte o conflito.
- **Combinações incompatíveis** — GPL-2.0 only + Apache-2.0 historicamente uma incompatibilidade conhecida; verifique combinações MPL / EPL / GPL com cuidado.
- **Licenças não-OSI disfarçadas de open source** — SSPL, BUSL, Commons Clause, Elastic License, Confluent Community. Leia a licença; não confie no badge "open source" do GitHub.
- **Mudanças de licença** — se uma versão anterior era permissiva e a versão atual é source-available, a versão fixada importa.

### Passo 6: Verificação de saída (se revisando nosso próprio código antes de abrir)

Se o usuário está preparando código para abrir como open source:

- Confirme que a licença de saída escolhida é compatível com toda dependência embarcada (ex.: não é possível liberar sob MIT se código GPL foi embarcado — a obra combinada deve ser GPL)
- Confirme que o arquivo LICENSE está presente e correto
- Confirme que o arquivo NOTICE está presente e lista as atribuições exigidas (Apache-2.0 e outras)
- Confirme que textos de licença de terceiros estão empacotados onde exigido
- Confirme que não há código proprietário ou confidencial, dados de cliente, ou credenciais embarcadas no histórico do repositório
- Confirme política de marca e nome para qualquer nome de projeto (separado da licença de direito autoral)
- Se houver registro do programa no INPI (Lei 9.609/1998 art. 3º) ou depósito anterior, confirme que a liberação como open source não conflita com direitos de terceiros previamente cedidos ou licenciados sobre o mesmo código

### Passo 7: Montar o memorando

Prefixe o cabeçalho de trabalho protegido de `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` → `## Outputs` (difere por papel do usuário — ver `## Quem está usando isso`).

Este memorando e qualquer lista de dependências revisada podem ser sigilosos, confidenciais, ou ambos. O output herda esse status da fonte. Distribua apenas dentro do círculo de sigilo; remova o cabeçalho de trabalho protegido antes de qualquer entrega externa (inclusive antes de anexar o memorando a um ticket de engenharia fora do círculo de sigilo).

> **Sem suplemento silencioso.** Se uma consulta de pesquisa à ferramenta jurídica configurada retorna poucos ou nenhum resultado para uma regra que o memorando precisa (exigibilidade do gatilho de rede da AGPL em determinada jurisdição, escopo da concessão de patente da GPL-3.0, texto mais recente de licença de pacote recentemente relicenciado), reporte o que foi encontrado e pare. NÃO complete a lacuna com busca web ou conhecimento do modelo sem perguntar. Diga: "A busca retornou [N] resultados de [ferramenta]. A cobertura parece rasa para [regra / licença / jurisdição]. Opções: (1) ampliar a consulta, (2) tentar outra ferramenta de pesquisa, (3) buscar na web — resultados serão marcados `[busca web — verificar]` e devem ser checados contra fonte primária antes de confiar, ou (4) sinalizar como não verificado e parar. Qual você prefere?" Um advogado decide se aceita fontes de menor confiança.
>
> **Atribuição de fonte.** Onde o memorando cita texto de licença, decisão judicial interpretando uma licença, ou orientação de mantenedor (FSF, OSI, SPDX, SFLC), marque a citação: `[OSI]`, `[SPDX]`, `[FSF]`, `[SFC/SFLC]`, `[JusBrasil]`, ou o nome da ferramenta MCP para citações obtidas via conector; `[busca web — verificar]` para citações de busca web; `[conhecimento do modelo — verificar]` para citações lembradas de dados de treinamento; `[fornecido pelo usuário]` para texto de licença lido diretamente do repositório. Citações marcadas `verificar` carregam risco maior de fabricação. Nunca remova ou colapse as tags.

```markdown
[CABEÇALHO DE TRABALHO PROTEGIDO — conforme config do plugin ## Outputs]

# Revisão de OSS: [Projeto / Lista de Dependências / Pacote]

**Revisado em:** [data]
**Escopo:** [Lista de dependências / Biblioteca única / Código de saída]
**Modelo de deployment:** [SaaS / Binário / Interno / Embarcado]

---

## Resumo executivo

[Duas frases. Isso pode ir a produção? O que precisa acontecer antes?]

**Pacotes revisados:** [N]
**Por classificação:** [N permissiva, N copyleft fraco, N copyleft forte, N domínio público, N não-OSI, N desconhecida]
**Issues:** [N]🔴 [N]🟠 [N]🟡 [N]🟢

**Aprovação necessária de:** [nome, conforme perfil de prática]

---

## Flags de topo de memorando

[Lista de licença-desconhecida, lista de conflito-de-licença, lista de não-OSI-disfarçada-de-OSS, combinações incompatíveis]

---

## Por pacote

[Blocos do Passo 4, agrupados por severidade]

---

## Nota de jurisdição

Exigibilidade de licença open source varia — o gatilho de rede da AGPL não foi amplamente testado em tribunal brasileiro; a cláusula de patente da GPL-3.0 lê diferente sob direito de patentes brasileiro vs. americano/europeu; dedicações ao domínio público não são universalmente reconhecidas sob a Lei 9.610/1998 (que trata domínio público como decorrência do decurso de prazo, art. 41, não de renúncia voluntária — `[SME VERIFY]` a eficácia de CC0/Unlicense no Brasil). Declare a lei aplicável escolhida para qualquer distribuição a jusante (ex.: contratos com fornecedores que incorporem o código) e sinalize jurisdições que o perfil de prática marca como escalar.

---

## Verificação de saída (se aplicável)

[Do Passo 6]

---

## Roteamento de aprovação

[Do perfil de prática — quem aprova, o que dispara escalonamento automático]
```

## Decision posture

Quando uma licença não pode ser confidentemente classificada, sinalize como **"precisa revisão"** — não a chame de permissiva. Subclassificar risco de licença é porta de mão única: uma decisão de ir a produção tomada sob suposição de permissiva-por-padrão vira obrigação de divulgação de código ou tutela de urgência meses depois. Sobre-sinalizar é porta de duas mãos — o advogado reduz a lista na revisão.

Da mesma forma, quando a análise de gatilho de copyleft depende de questão contestada (o "interage em rede" da AGPL, o "conveying" da GPL-3.0, o escopo de linking da LGPL), sinalize para revisão de advogado e mostre os fatores que pesam em ambas direções.

## Quality checks before delivering

- [ ] Perfil de prática e qualquer política de OSS foram carregados
- [ ] Modelo de deployment foi estabelecido antes de classificar obrigações
- [ ] Toda dependência tem classificação, incluindo transitivas onde disponíveis
- [ ] Pacotes de licença desconhecida estão sinalizados, não default para permissiva
- [ ] Texto de licença foi lido (não só metadados) para qualquer achado de copyleft ou não-OSI
- [ ] Tags de fonte aplicadas às citações; nenhuma tag `verificar` removida
- [ ] Aprovador nomeado conforme perfil de prática
- [ ] Output marcado com o cabeçalho de trabalho protegido

## Close with the next-steps decision tree

Encerre com a árvore de decisão de próximos passos conforme CLAUDE.md `## Outputs`. Customize as opções ao que este skill acabou de produzir — os cinco ramos padrão (redigir o X, escalar, buscar mais fatos, observar e aguardar, algo mais) são ponto de partida, não travamento. A árvore é o output; o advogado escolhe.

Se a varredura revelou mais de ~10 pacotes, ou sempre que o usuário pedir: ofereça o dashboard (ver CLAUDE.md `## Outputs → Oferta de dashboard para outputs ricos em dados`). Molde a oferta ao que é útil aqui — contagens por família de licença (permissiva / copyleft fraco / copyleft forte / AGPL / proprietária / desconhecida), distribuição de risco, e tabela de achados com severidade e versão do pacote.
