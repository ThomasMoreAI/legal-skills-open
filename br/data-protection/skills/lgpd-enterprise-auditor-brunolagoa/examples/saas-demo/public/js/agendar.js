// Envio do formulário de agendamento e exibição da confirmação
(function () {
  const clinica = new URLSearchParams(window.location.search).get('clinica');
  const form = document.getElementById('form-agendamento');
  const confirmacao = document.getElementById('confirmacao');

  form.addEventListener('submit', async (evento) => {
    evento.preventDefault();
    const dados = Object.fromEntries(new FormData(form).entries());
    dados.clinica = clinica;

    const resposta = await fetch('/api/agendamentos', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(dados),
    });
    const corpo = await resposta.json();
    if (!resposta.ok) {
      alert(corpo.erro);
      return;
    }

    if (typeof fbq === 'function') fbq('track', 'Schedule');

    const detalhe = await fetch(`/api/agendamentos/${corpo.codigo}`).then((r) => r.json());
    form.hidden = true;
    confirmacao.hidden = false;
    confirmacao.textContent =
      `Consulta confirmada para ${new Date(detalhe.data_hora).toLocaleString('pt-BR')}, ` +
      `${detalhe.nome}. Guarde o código ${corpo.codigo}.`;
  });
})();
