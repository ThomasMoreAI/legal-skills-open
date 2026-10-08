document.addEventListener('DOMContentLoaded', () => {
  const input = document.querySelector('#cardFilter');
  const items = Array.from(document.querySelectorAll('.filter-item'));
  const emptyState = document.querySelector('#noResults');
  const status = document.querySelector('#filterStatus');

  if (!input || !items.length || !emptyState || !status) {
    return;
  }

  const applyFilter = () => {
    const term = input.value.trim().toLowerCase();
    let visible = 0;

    items.forEach((item) => {
      const haystack = (item.dataset.search || '').toLowerCase();
      const match = !term || haystack.includes(term);
      item.classList.toggle('is-hidden', !match);
      if (match) visible += 1;
    });

    emptyState.classList.toggle('d-none', visible !== 0);
    status.textContent = term
      ? `${visible} tarjeta${visible === 1 ? '' : 's'} visible${visible === 1 ? '' : 's'} para “${input.value.trim()}”.`
      : `${visible} tarjeta${visible === 1 ? '' : 's'} visible${visible === 1 ? '' : 's'} en el panel.`;
  };

  input.addEventListener('input', applyFilter);
  applyFilter();
});
