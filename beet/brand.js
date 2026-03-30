const BRAND_WORDMARK_HTML = 'b<span class="wordmark-accent">e</span>et';
document.querySelectorAll('[data-brand-wordmark]').forEach((el) => {
  el.innerHTML = BRAND_WORDMARK_HTML;
});
