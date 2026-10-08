# representacao-cautelar

> Redige representações da Autoridade Policial dirigidas ao Juízo (preventiva, temporária, busca e apreensão, quebras de sigilo, interceptação), no padrão real da Delegacia de Alta Floresta/MT e do NEAMV.

**English summary:** Drafts the police authority's motions to the criminal court — pretrial detention, temporary arrest, search and seizure, telecom/telematic data disclosure, wiretaps, bank and tax records, access to seized devices — following the real structure and phrasing of the unit. Grounded in a private bank of the author's real motions, which is deliberately kept out of this public repository. Always a draft for human review and signature.

## O que faz

A skill produz o rascunho das **representações cautelares que o Delegado assinaria**: prisão preventiva, prisão temporária, busca e apreensão domiciliar, afastamento de sigilo de dados telefônicos e telemáticos, interceptação de comunicações, sigilo bancário e fiscal, acesso a dados de dispositivos apreendidos, medidas assecuratórias e destinação de bens. Fecha o ciclo com as skills irmãs: `despacho-plantao` decide o plantão, esta materializa a medida, e `relatorio-final-ip` encerra o inquérito.

O princípio de redação é a reserva de jurisdição: cada requisito legal recebe um parágrafo próprio, amarrado a fato concreto dos autos com indicação de folhas. Antes de escrever, a skill verifica o **cabimento** da medida (art. 313 do CPP, rol taxativo da Lei 7.960/89, corroboração prévia para busca, requisição direta de dados cadastrais) e, se não couber, propõe a alternativa cabível em vez de redigir peça natimorta. Também trata cumulações e pedidos acessórios (acesso aos dados dos dispositivos apreendidos, cautelares subsidiárias do art. 319, período delimitado nas quebras).

A skill se apoia em um **banco de modelos reais do próprio Delegado**, indexado em `references/catalogo-modelos.md`: havendo modelo compatível, a fraseologia real do usuário prevalece sobre os blocos genéricos das referências. Quando o usuário entrega autos sem nomear a medida ("vê o que cabe"), a skill lista todas as medidas cabíveis e pede confirmação antes de redigir.

## Quando usar

- "Representa pela preventiva" / "monta a representação" / "faz o pedido de busca";
- "Quebra o sigilo do alvo" / "pede a interceptação" / "representa pelo acesso ao celular apreendido";
- Pedidos com alvo em provedores de aplicação, redes sociais, aplicativos de mensagens/transporte/entrega ou operadoras, inclusive os ofícios judiciais a essas empresas;
- Quando o despacho de plantão já sinalizou "é caso para REPRESENTAÇÃO PELA PRISÃO PREVENTIVA" e o usuário quer a peça completa;
- "Olha esses autos e vê o que cabe" (avaliação de medidas cabíveis);
- Adicionar/ingerir modelos novos na base de conhecimento da skill.

Não use para despacho de plantão (`despacho-plantao`) nem para relatório final de IP (`relatorio-final-ip`).

## Como usar

> "Representa pela prisão preventiva do investigado do IP 55.4.2026.123, com base no APF e na vida pregressa anexos."

> "Monta a representação de busca e apreensão domiciliar no endereço do alvo, com pedido de acesso aos dados dos celulares que forem apreendidos."

> "Quebra o sigilo telemático do alvo: dados de conta do WhatsApp e da Meta, período de janeiro a junho, com os ofícios às empresas."

> "Olha esses autos e vê o que cabe de medida cautelar nesse caso de tráfico."

> "Ingere esses novos modelos de representação na base da skill."

## O que a skill entrega

- **Padrão: peça formatada direto no chat**, pronta para revisar e colar, com a estrutura fixa da unidade (endereçamento, preâmbulo, I. Dos Fatos, II. Do Direito, III. Do Pedido, fecho e assinatura);
- Seção separada de **Notas ao Delegado**: premissas assumidas, pontos de atenção jurídica, campos `[VERIFICAR: ...]` a completar antes do protocolo e diligências recomendadas;
- Arquivo **.docx** apenas se solicitado, com as configurações jurídicas da unidade (A4, Arial 12, entrelinha 1,5, cabeçalho e rodapé de `templates/modelo_base.md`).

## Estrutura da pasta

| Item | Papel |
|---|---|
| `SKILL.md` | Instruções completas: fluxo em 6 passos, cabimento, redação, cumulações e notas |
| `references/preventiva-temporaria.md` | Requisitos legais e fraseologia de preventiva (arts. 311-316 CPP) e temporária (Lei 7.960/89) |
| `references/busca-apreensao.md` | Requisitos e armadilhas da busca e apreensão (arts. 240-250 CPP) |
| `references/quebra-sigilo.md` | Quebras de sigilo, interceptação, bancário/fiscal e dispositivos apreendidos |
| `references/catalogo-modelos.LEIA-ME.md` | Explica onde está o catálogo real e como restaurá-lo |
| `templates/modelo_base.md` | Template estrutural comum (endereçamento, cabeçalho, fecho) |
| `scripts/ingest_modelos.py` | Ingestão de modelos .docx: reconstrói espaços perdidos e sanitiza dados sensíveis com placeholders |
| `assets/modelos/`, `assets/modelos-brutos/` | Destinos locais do acervo de modelos (aqui, só os LEIA-ME) |
| `evals/evals.json` | Casos de avaliação da skill (testes de qualidade das peças) |

## Requisitos

- **O acervo de modelos reais e o catálogo (`references/catalogo-modelos.md`) são material sigiloso e NÃO estão versionados neste repositório público** — as pastas `assets/modelos*` contêm apenas os LEIA-ME. A fonte de verdade fica no repositório privado `delegacia-claude-workspace`; o LEIA-ME traz o procedimento de restauração. Sem o catálogo a skill funciona com as referências genéricas, apenas sem a fraseologia real do usuário.
- **Python 3** para `scripts/ingest_modelos.py` (ingestão de modelos novos);
- Extrator local (Docling + EasyOCR) em `~/.claude/tools/` para autos em PDF — não ler PDFs direto no contexto;
- Entrada esperada: fatos ou autos (BO, APF, despacho de plantão, termos), qualificação do investigado e o dado específico da medida (endereço da busca, linha e período do sigilo, IMEI etc.).

## Avisos

- **A minuta exige revisão da Autoridade Policial**: quem decide é o juiz e quem assina é o Delegado; a skill entrega rascunho fundamentado para revisão humana.
- **Dados sigilosos** (investigados, vítimas, modelos operacionais da unidade) não devem ser colados em ambientes não autorizados; por isso o acervo real fica fora do repositório público.
- Tratamento de dados pessoais sujeito à **LGPD** (Lei 13.709/2018) e ao sigilo funcional: a peça compila apenas o que a medida exige.
- A skill segue as convenções da **Delegacia de Alta Floresta/MT e do NEAMV** (endereçamento à Comarca de Alta Floresta, fraseologia e assinatura); precisa de adaptação para outras unidades.
