const BRAND_WORDMARK_HTML = 'm<span class="wordmark-accent">o</span>ov';
document.querySelectorAll('[data-brand-wordmark]').forEach((el) => {
  el.innerHTML = BRAND_WORDMARK_HTML;
});
