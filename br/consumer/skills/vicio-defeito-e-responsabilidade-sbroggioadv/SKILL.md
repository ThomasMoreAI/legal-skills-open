---
name: vicio-defeito-e-responsabilidade-sbroggioadv
title: Vício, Defeito e Responsabilidade
description: 'Distingue vício (arts. 18-20, 23, CDC) de defeito/fato do produto e serviço (arts. 12-14, CDC), aplica a responsabilidade objetiva e suas excludentes (art. 12 §3º e art. 14 §3º), delimita a responsabilidade do comerciante (art. 13) e do profissional liberal (art. 14 §4º, subjetiva), e lista as três alternativas do consumidor após 30 dias sem solução. Aciona: quando é preciso qualificar um problema em produto/serviço como vício ou defeito, escolher o réu correto na cadeia de fornecimento, avaliar uma excludente de responsabilidade alegada pelo fornecedor, ou decidir se o dano decorre de fortuito interno (não exclui) ou externo (exclui).'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/consumidor-adv-os-marketplace/tree/main/consumidor-adv-os/skills/vicio-defeito-e-responsabilidade
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: consumer
language: pt
---

# Vício, Defeito e Responsabilidade

## Quando esta skill entra
Depois de confirmada a relação de consumo (`relacao-de-consumo-e-partes`), esta skill decide
**qual regime de responsabilidade** incide: vício (o produto/serviço não presta para o fim a que
se destina, ou tem menos do que devia) ou defeito/fato (o produto/serviço causa um acidente de
consumo, um dano à segurança que vai além do próprio bem). São regimes diferentes, com prazos
diferentes (ver `prazos-decadencia-prescricao-consumo`) e réus potencialmente diferentes.

## Base normativa
**Vício (Seção III — Da Responsabilidade por Vício do Produto e do Serviço):**
- **Art. 18** — fornecedores respondem **solidariamente** por vícios de qualidade ou quantidade
  que tornem o produto impróprio/inadequado ou diminuam seu valor. §1º: não sanado em **30 dias**,
  o consumidor pode exigir, alternativa e à sua escolha: (I) substituição por outro da mesma
  espécie; (II) restituição imediata da quantia paga, atualizada, sem prejuízo de perdas e danos;
  (III) abatimento proporcional do preço. §2º: as partes podem convencionar prazo entre 7 e 180
  dias. §3º: as alternativas do §1º ficam disponíveis de imediato quando a substituição
  comprometer a qualidade, diminuir o valor, ou se tratar de produto essencial.
- **Art. 19** — vício de **quantidade** (conteúdo líquido inferior ao indicado): abatimento,
  complementação, substituição ou restituição, à escolha do consumidor.
- **Art. 20** — vício de qualidade em **serviços**: reexecução sem custo, restituição imediata
  atualizada, ou abatimento proporcional.
- **Art. 23** — a ignorância do fornecedor sobre o vício **não o exime** de responsabilidade.

**Defeito / fato do produto e do serviço (Seção II — responsabilidade objetiva):**
- **Art. 12** — fabricante, produtor, construtor e importador respondem, **independentemente de
  culpa**, por danos causados por defeitos de projeto, fabricação, construção, montagem, fórmulas,
  manipulação, apresentação ou acondicionamento, e por informação insuficiente/inadequada. §3º —
  só não responde quem provar: (I) que não colocou o produto no mercado; (II) que o defeito
  inexiste; (III) culpa exclusiva do consumidor ou de terceiro.
- **Art. 13** — o **comerciante** responde nos mesmos termos quando: (I) fabricante/construtor/
  produtor/importador não puderem ser identificados; (II) o produto for fornecido sem
  identificação clara de quem o fabricou; (III) não conservar adequadamente produto perecível.
  Parágrafo único: quem pagar tem direito de regresso contra os demais responsáveis.
- **Art. 14** — o fornecedor de **serviços** responde, independentemente de culpa, por defeitos
  relativos à prestação. §3º — só não responde provando (I) que, tendo prestado o serviço, o
  defeito inexiste; (II) culpa exclusiva do consumidor ou de terceiro. **§4º** — a responsabilidade
  **pessoal do profissional liberal** é apurada **mediante verificação de culpa** (única exceção
  subjetiva do sistema — não é responsabilidade objetiva).
(fonte: `context/cdc-lei-8078.md`)

## O teste / o passo a passo
1. O problema torna o bem inadequado ao uso, ou apenas causa dano além do próprio bem?
   Inadequado → **vício** (arts. 18-20). Causa acidente/dano à segurança → **defeito/fato**
   (arts. 12-14).
2. Se é vício: o fornecedor teve 30 dias (ou o prazo convencionado, 7-180) para sanar? Não sanou →
   as três alternativas do §1º ficam disponíveis.
3. Se é defeito/fato: quem é o réu correto? Fabricante/produtor/importador via art. 12;
   comerciante só nas três hipóteses do art. 13; serviço via art. 14.
4. O réu é profissional liberal (médico, advogado, contador)? Responsabilidade **subjetiva** —
   apurar culpa, não basta o dano objetivo (art. 14, §4º). Cross-link: mérito clínico é
   `direito-medico-adv-os`.
5. Há excludente provada (não colocou no mercado, defeito inexiste, culpa exclusiva de
   terceiro/consumidor)? Checar a doutrina do fortuito interno × externo abaixo antes de aceitar.

## Fortuito interno × externo — o critério que decide a excludente na prática
Jurisprudência do STJ (matéria especial, 5 precedentes reais confirmados em fonte oficial):
**fortuito interno** = risco inerente à própria atividade do fornecedor → **não exclui**
responsabilidade (assalto em drive-thru — REsp 1.450.434; tiroteio entre seguranças do
estabelecimento — REsp 1.732.398; furto em loja de shopping — REsp 1.487.443; desabamento por
chuva previsível — REsp 1.764.439). **Fortuito externo** = fato estranho à atividade, sem relação
com o risco que o fornecedor criou → **exclui** (roubo em estacionamento aberto, gratuito, de
livre acesso — EREsp 1.431.606). Critério decisivo: **teoria do risco-proveito** — se o fornecedor
se beneficia, ainda que indiretamente, da situação que favoreceu o dano, a responsabilidade se
mantém. (fonte: `context/fornecedor-e-administrativo.md`, §1.3)

## Tese do consumidor × Tese do fornecedor
- **Tese do consumidor:** enquadrar o dano como fortuito **interno** sempre que houver qualquer
  conexão com o risco da atividade (segurança, acesso, atendimento); exigir as três alternativas
  do art. 18 quando o prazo de 30 dias for ultrapassado sem solução; buscar todos os elos
  solidários da cadeia em vez de processar só o comerciante.
- **Tese do fornecedor:** provar as excludentes do art. 12 §3º / 14 §3º com prova concreta
  (perícia, laudo, prova de terceiro estranho); reduzir o polo passivo ao elo correto (comerciante
  só responde nas três hipóteses taxativas do art. 13); se profissional liberal, deslocar o debate
  para a ausência de culpa (art. 14, §4º), não para o resultado.

## Armadilhas
- Confundir vício (regime dos arts. 18-20, prazo decadencial) com defeito/fato (regime dos arts.
  12-14, prazo prescricional) muda o prazo aplicável — ver `prazos-decadencia-prescricao-consumo`.
- **T13** — normalizar espaço em branco ao conferir citação literal contra os anexos.
- Citar REsp de fortuito interno/externo fora dos cinco confirmados nesta skill sem nova
  verificação em fonte oficial.

## Fronteira
Mérito clínico de responsabilidade médica (erro de procedimento, negligência clínica):
`direito-medico-adv-os`. Liquidação/cálculo de indenização: `calculosjudiciais-adv-os`. Execução
do título já reconhecido: `execucao-adv-os`.
