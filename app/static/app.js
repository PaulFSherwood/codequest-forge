(function () {
  const palette = document.getElementById('command-palette');
  const input = document.getElementById('command-input');
  const close = document.getElementById('close-command');

  function openPalette() {
    palette.classList.remove('hidden');
    setTimeout(() => input && input.focus(), 30);
  }
  function closePalette() {
    palette.classList.add('hidden');
    if (input) input.value = '';
  }

  document.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      openPalette();
    }
    if (e.key === 'Escape') closePalette();
  });
  if (close) close.addEventListener('click', closePalette);
  if (palette) palette.addEventListener('click', (e) => {
    if (e.target === palette) closePalette();
  });
})();
