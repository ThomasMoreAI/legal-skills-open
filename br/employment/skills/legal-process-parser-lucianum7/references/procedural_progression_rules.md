# Regras para andamento processual e peças de trabalho

## Princípio de proveniência

Todo evento, prazo, documento, prova ou sugestão deve apontar para pdf_page,
court_page quando disponível, piece, document_id e uma âncora legível.
Quando a fonte não for suficiente, use needs_review, unknown ou not_assessed;
nunca complete o valor por plausibilidade.

## Peças geradas

O pipeline gera os seguintes artefatos derivados:

- andamento_processual.json: contrato estruturado de eventos, prazos, evidências,
  pendências e tarefas;
- relatorio_andamento.md: estado atual e fila de próximas conferências;
- pendencias_e_prazos.md: marcos encontrados sem calcular vencimento;
- matriz_documental.md: segmentos, páginas e status técnico;
- mapa_provas.md: menções documentais, sem conclusão de suficiência;
- checklist_manifestacao.md: itens a revisar antes de uma manifestação;
- minuta_peca.md: esqueleto de trabalho com fatos e pedidos em aberto;
- relatorio_conformidade.md: controles de cobertura e limitações.

## Limites jurídicos

Datas são apenas ocorrências textuais até que o profissional confirme seu
significado. O parser não aplica feriados, suspensões, intimações presumidas ou
regras de contagem sem parâmetros fornecidos. Uma menção a “prova” não confirma
autenticidade, admissibilidade, pertinência ou suficiência. Uma minuta nunca é
pronta para protocolo e não deve inserir fundamentos ou pedidos ausentes dos autos.

## Revisão recomendada

1. resolver páginas PARTIAL e descrições visuais pendentes;
2. conferir número do processo, partes, peça, data e folha;
3. validar cada evento e distinguir data do documento de data do fato;
4. calcular prazos somente com marco, calendário e regra aplicável;
5. aprovar fatos, provas, pedidos e responsáveis;
6. só então adaptar a minuta para o formato exigido pelo órgão competente.
