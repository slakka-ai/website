const BRAND_WORDMARK_HTML = 'ko<span class="wordmark-accent">r</span>r';
document.querySelectorAll('[data-brand-wordmark]').forEach((el) => {
  el.innerHTML = BRAND_WORDMARK_HTML;
});
