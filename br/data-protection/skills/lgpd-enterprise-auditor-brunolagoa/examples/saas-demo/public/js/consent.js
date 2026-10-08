// Banner de consentimento de cookies
(function () {
  const CHAVE = 'agendafacil_consentimento';
  const banner = document.getElementById('banner-cookies');

  function aplicar(escolha) {
    if (typeof fbq !== 'function') return;
    fbq('consent', escolha === 'aceito' ? 'grant' : 'revoke');
  }

  function salvar(escolha) {
    localStorage.setItem(CHAVE, JSON.stringify({ escolha, data: new Date().toISOString() }));
    aplicar(escolha);
    banner.hidden = true;
  }

  const salvo = localStorage.getItem(CHAVE);
  if (salvo) {
    aplicar(JSON.parse(salvo).escolha);
  } else {
    banner.hidden = false;
  }

  document.getElementById('cookies-aceitar').addEventListener('click', () => salvar('aceito'));
  document.getElementById('cookies-rejeitar').addEventListener('click', () => salvar('rejeitado'));
  document.getElementById('preferencias-cookies').addEventListener('click', (evento) => {
    evento.preventDefault();
    banner.hidden = false;
  });
})();
