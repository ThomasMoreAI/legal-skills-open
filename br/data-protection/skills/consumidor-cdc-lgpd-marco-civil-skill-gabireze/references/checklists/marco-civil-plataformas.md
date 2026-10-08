# Checklist: Marco Civil, plataformas e aplicacoes de internet

Use para casos de conta online, plataforma, moderacao, remocao de conteudo, logs, neutralidade, termos digitais e responsabilidade de provedor.

## Classificacao inicial

- [ ] O servico e provedor de conexao, provedor de aplicacao, marketplace, rede social, app, SaaS, hospedagem, mensageria, e-mail ou videoconferencia?
- [ ] O problema e conteudo de terceiro, conta do usuario, cobranca, privacidade, seguranca, suporte, neutralidade ou investigacao?
- [ ] Ha relacao de consumo B2C?
- [ ] Ha dados pessoais, crianca/adolescente, conteudo intimo, crime, fraude ou setor regulado?
- [ ] Ha pedido judicial, notificacao extrajudicial, protocolo ou ordem administrativa?

## Evidencias minimas

- [ ] URL, ID do conteudo, ID da conta, print e data/hora com fuso.
- [ ] Termos de uso e politica vigentes na data do fato.
- [ ] Comunicacao da plataforma: aviso, e-mail, push, ticket, protocolo.
- [ ] Historico de recurso, contestacao ou atendimento.
- [ ] Comprovante de assinatura, plano, pagamento ou impacto economico, se houver.
- [ ] Logs ou dados tecnicos disponiveis licitamente.

## Base por tema

| Tema | Fonte inicial | Perguntas |
|---|---|---|
| Remocao de conteudo de terceiro | Marco Civil arts. 19 e 21 | Ha URL especifica? Houve ordem judicial? E conteudo intimo privado? |
| Suspensao de conta | Marco Civil, CDC, termos e LGPD | Houve aviso, regra violada, canal de recurso e impacto ao consumidor? |
| Logs/IP/porta logica | Marco Civil arts. 10, 13, 15 e 22; Decreto 8.771/2016; Decreto 12.975/2026 conforme vigencia | Qual dado e necessario? Ha ordem judicial ou base legal? |
| Neutralidade de rede | Marco Civil art. 9º; Decreto 8.771/2016 | Ha degradacao/discriminacao? Existe justificativa tecnica, seguranca ou emergencia? |
| Termos e moderacao | CDC, Marco Civil, Decreto 12.975/2026 conforme vigencia | As regras sao claras, publicas, revisadas e aplicadas de modo consistente? |
| Dados pessoais | LGPD como base primaria | O tratamento real bate com politica, termos, logs e retencao? |
| Crianca/adolescente | ECA, Lei 15.211/2025, Decreto 12.880/2026, LGPD | O produto e direcionado ou de acesso provavel por menores? |

## Red flags

- Plataforma nao informa regra violada nem canal de contestacao.
- Termos permitem suspensao ou remocao "por qualquer motivo" sem criterio minimo.
- Pedido de logs sem ordem judicial ou base legal especifica.
- Politica promete excluir dados, mas logs sao retidos sem criterio claro.
- Conteudo intimo privado e tratado como reclamacao comum.
- Caso de crianca/adolescente sem avaliacao de prioridade e autoridade competente.
- Neutralidade de rede alegada sem evidencia tecnica minima.

## Saida sugerida

```md
Nivel de certeza: [base legal direta | tese plausivel | tema controvertido | fora do escopo da skill]

Enquadramento:
- Marco Civil: [por que se aplica].
- CDC: [se houver relacao de consumo].
- LGPD: [se houver dados pessoais].
- Norma especial: [se houver crianca/adolescente, telecom, penal, eleitoral, autoral ou setor regulado].

Fatos que faltam:
1. [evidencia]
2. [evidencia]

Caminho pratico:
1. preservar URL/prints/data/hora;
2. acionar canal formal da plataforma;
3. avaliar Procon/Consumidor.gov.br/ANPD/Anatel/advogado/Defensoria/autoridade policial conforme o risco.
```
