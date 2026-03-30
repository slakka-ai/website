const BRAND_WORDMARK_HTML = 'k<span class="wordmark-accent">a</span>sk';
document.querySelectorAll('[data-brand-wordmark]').forEach((el) => {
  el.innerHTML = BRAND_WORDMARK_HTML;
});
