const BRAND_WORDMARK_HTML = 'p<span class="wordmark-accent">a</span>i';
document.querySelectorAll('[data-brand-wordmark]').forEach((el) => {
  el.innerHTML = BRAND_WORDMARK_HTML;
});
