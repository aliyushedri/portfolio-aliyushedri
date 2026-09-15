// Keep old index.html links usable while showing the directory URL.
if (location.pathname.endsWith('/index.html')) {
  const cleanUrl = new URL(location.href);
  cleanUrl.pathname = cleanUrl.pathname.slice(0, -'index.html'.length);
  history.replaceState(history.state, '', cleanUrl);
}

const isIndonesian = document.documentElement.lang === 'id';
const toggle = document.querySelector('.nav-toggle');
const navigation = document.querySelector('.desktop-nav');
const menuLabel = open => isIndonesian ? (open ? 'Tutup menu navigasi' : 'Buka menu navigasi') : (open ? 'Close navigation menu' : 'Open navigation menu');
function closeMenu() {
  navigation?.classList.remove('is-open');
  toggle?.setAttribute('aria-expanded', 'false');
  toggle?.setAttribute('aria-label', menuLabel(false));
}
toggle?.addEventListener('click', () => {
  const open = toggle.getAttribute('aria-expanded') !== 'true';
  toggle.setAttribute('aria-expanded', String(open));
  toggle.setAttribute('aria-label', menuLabel(open));
  navigation.classList.toggle('is-open', open);
});
navigation?.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
window.matchMedia('(min-width: 761px)').addEventListener('change', closeMenu);
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && toggle?.getAttribute('aria-expanded') === 'true') { closeMenu(); toggle.focus(); }
});
document.querySelector('.language-switch')?.addEventListener('click', event => {
  const destination = new URL(event.currentTarget.dataset.languageTarget, location.href);
  destination.hash = location.hash;
  destination.search = location.search;
  location.assign(destination.href);
});
const filters = [...document.querySelectorAll('.filter-button')];
const cards = [...document.querySelectorAll('.project-card')];
function selectFilter(value, updateUrl = false) {
  const selected = filters.find(button => button.dataset.filter === value) || filters[0];
  if (!selected) return;
  filters.forEach(button => button.setAttribute('aria-pressed', String(button === selected)));
  let count = 0;
  cards.forEach(card => {
    card.hidden = selected.dataset.filter !== 'all' && !card.dataset.category.split(' ').includes(selected.dataset.filter);
    if (!card.hidden) count++;
  });
  const status = document.querySelector('#filter-status');
  if (status) status.textContent = isIndonesian ? `${count} proyek ditampilkan` : `${count} projects shown`;
  if (updateUrl) {
    const url = new URL(location.href);
    if (selected.dataset.filter === 'all') url.searchParams.delete('filter'); else url.searchParams.set('filter', selected.dataset.filter);
    history.replaceState(null, '', url);
  }
}
filters.forEach(button => button.addEventListener('click', () => selectFilter(button.dataset.filter, true)));
selectFilter(new URL(location.href).searchParams.get('filter'));
window.addEventListener('popstate', () => selectFilter(new URL(location.href).searchParams.get('filter')));
const dialog = document.querySelector('#certificate-dialog');
let certificateOpener;
document.querySelectorAll('[data-certificate]').forEach(button => button.addEventListener('click', () => {
  if (!dialog) return;
  certificateOpener = button;
  const title = button.dataset.certificateTitle;
  dialog.querySelector('#certificate-title').textContent = title;
  const image = dialog.querySelector('#certificate-image');
  image.src = button.dataset.certificate; image.alt = title;
  dialog.showModal(); dialog.querySelector('.dialog-close').focus();
}));
dialog?.querySelector('.dialog-close')?.addEventListener('click', () => dialog.close());
dialog?.addEventListener('click', event => {
  const rect = dialog.getBoundingClientRect();
  if (event.target === dialog && (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom)) dialog.close();
});
dialog?.addEventListener('close', () => certificateOpener?.focus());
