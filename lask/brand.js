const BRAND_WORDMARK_HTML = 'la<span class="wordmark-accent">s</span>k';
document.querySelectorAll('[data-brand-wordmark]').forEach((el) => {
  el.innerHTML = BRAND_WORDMARK_HTML;
});
