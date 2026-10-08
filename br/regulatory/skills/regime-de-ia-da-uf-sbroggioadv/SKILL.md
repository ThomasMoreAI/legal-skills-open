---
name: regime-de-ia-da-uf-sbroggioadv
title: Regime de IA da UF
description: 'Classifica o uso de IA na serventia segundo cinco posturas estaduais: PI facultativa com rol aberto, MT proibitiva, MA permissiva com rol fechado, AM permissiva sob homologação prévia hoje inexistente e as outras 23 UFs sem norma estadual localizada. Esta skill deve ser usada quando o pedido mencionar usar IA no cartório, ferramenta de IA, minuta automática, análise documental, qualificação, chatbot, fornecedor, homologação, treinamento com acervo ou autorização estadual.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/tabelionato-os-marketplace/tree/main/tabelionato-os/skills/regime-de-ia-da-uf
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: regulatory
language: pt
---

# Regime de IA da UF

> Camada C2. Separar cinco posturas incompatíveis. Nunca transportar regime de IA entre UFs.

## Anexos obrigatórios

- `context/ia-por-uf.md` — endereços, usos, vedações e contradições materiais;
- `context/uf-matriz-27.md` — confirmação da UF e do documento-mãe;
- `context/estado-da-norma.md` — data de corte e vigência;
- `context/prov-cnj-213-2026-e-anexos.md` — piso federal de segurança e acervo;
- `context/res-cnj-615-2025-recorte-dados.md` — régua de governança, sem convertê-la em vínculo extrajudicial;
- `context/travas-defasagem.md` — remissões mortas e gates estaduais.

## Entradas bloqueantes

Fixar:

1. UF da serventia;
2. função pretendida — redação, análise, qualificação, interpretação, atendimento, transcrição, indexação, sumarização, decisão ou outra;
3. classe de dado e fluxo — local/externo, retenção, treinamento e acesso do fornecedor;
4. condição da delegação quando a norma a distinguir;
5. ferramenta e fornecedor, sem inserir dado real de parte ou acervo.

Sem UF, fornecer somente o piso federal de segurança e declarar que ele não autoriza uma função estadual. Não presumir permissão pelo silêncio.

## As cinco posturas

### 1. PI — facultativa, rol aberto

Aplicar o Provimento CFE 62/2024, arts. 102-108. Reconhecer uso facultativo, suporte ao julgamento humano e rol aberto por cláusula de eficiência e qualidade. Admitir somente os usos cobertos e sujeitá-los a governança, capacitação, verificação e comunicação anual.

Não transformar faculdade em dever. Não afirmar que o PI foi o primeiro do Brasil; afirmar apenas que sua norma antecede a do MT entre as quatro normas comparadas.

### 2. MT — proibitiva, com exceções fechadas

Aplicar o Provimento 1/2026-GAB-CGJ como ato autônomo. Bloquear qualificação, interpretação, enquadramento ou sugestão de decisão jurídica, **ainda que sob revisão humana**. Admitir somente as exceções auxiliares taxativas de baixo risco.

Não usar revisão humana como cura para função proibida. Reconduzir a remissão morta ao Provimento CNJ 74/2018 para o Provimento CN 213/2026 e alterações, declarando a desatualização material.

### 3. MA — permissiva condicionada, rol fechado

Aplicar o Provimento COGEX 28/2026, arts. 167-179. Limitar o uso aos cinco incisos do art. 171 e exigir cumulativamente as travas de contratação, inclusive desenvolvimento ou armazenamento no Brasil, banco no servidor da serventia, segurança e auditoria.

Não abrir o rol por analogia com o PI. Escalonar atendimento para pessoa humana e preservar a decisão jurídica humana.

### 4. AM — permissiva sob homologação prévia inexistente

Aplicar o Provimento 531/2026-CGJ/AM, arts. 164-170 e art. 663. Reconhecer a permissão em tese e a autorização específica do art. 663 para auxílio à **qualificação registral**, sem ampliá-la automaticamente ao tabelionato de notas.

Tratar o art. 168, IV, “a” como gate operante: modelo não homologado previamente pela Corregedoria não pode ser usado. Na data de corte de 25/08/2026, o procedimento de homologação prévia é **inexistente na base oficial varrida**; não há via pública de cumprimento nem modelo comprovadamente homologado. Classificar a adoção hoje como **NÃO ENDEREÇÁVEL / BLOQUEADA**, orientar consulta à CGJ/AM e não ligar, recomendar ou declarar regular qualquer função de IA.

Não escolher entre proibição autoaplicável e eficácia dependente de regulamentação. Identificar essa controvérsia como questão jurídica local. Não afirmar que fornecedor específico está homologado.

### 5. Outras 23 UFs — sem norma estadual localizada

Aplicar apenas o piso federal de segurança, acervo e proteção de dados. Declarar que a ausência de norma estadual localizada na data de corte não equivale a autorização, proibição ou dispensa de atualização. Tratar a Resolução CNJ 615/2025 como régua de governança, não como norma vinculante da serventia extrajudicial.

## Teste de contradição obrigatório

Antes da conclusão, comparar a função pretendida com as oposições:

- **MT × PI/MA:** MT proíbe funções de qualificação, interpretação e decisão que PI ou MA podem admitir nos limites locais;
- **PI × MA:** PI possui rol aberto; MA possui rol fechado e contratação cumulativamente condicionada;
- **MT × AM:** MT proíbe qualificação registral por IA; AM a admite em tese, mas o gate de homologação hoje não pode ser cumprido;
- **quatro UFs × demais:** norma judicial, notícia institucional ou prática de tribunal não cria norma para delegatário.

Se a resposta permanecer idêntica após trocar MT por PI ou MA, reprovar o roteamento.

## Cartão de saída

| Campo | Resultado |
|---|---|
| UF, norma e data de corte | |
| postura | uma das cinco |
| função pretendida | |
| permitido | uso e condições exatas |
| proibido | função e fundamento |
| não resolvido | lacuna ou controvérsia |
| gates | homologação, autorização, contrato, capacitação, reporte |
| dados e acervo | fluxo admissível ou bloqueio |
| decisão | permitida, proibida, bloqueada ou não concluída |

## Reprovação automática

- citar provimento estadual de IA fora de PI, MT, MA ou AM;
- tratar o padrão mais permissivo como média nacional;
- autorizar no MT o que a revisão humana não cura;
- abrir o rol fechado do MA;
- autorizar IA no AM sem homologação prévia comprovada;
- transpor o art. 663 do AM de registro para Notas;
- usar acervo, entrada ou saída para treinamento;
- inserir conteúdo confidencial em sistema externo;
- delegar decisão final, manifestação de vontade ou validação jurídica à IA.
