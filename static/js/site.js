document.querySelector('.menu')?.addEventListener('click', () => {
  document.querySelector('.nav nav')?.classList.toggle('open');
});

window.setTimeout(() => document.querySelector('.messages')?.remove(), 5000);
