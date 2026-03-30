const BRAND_WORDMARK_HTML = 's<span class="wordmark-accent">i</span>mpl';
document.querySelectorAll('[data-brand-wordmark]').forEach((el) => {
  el.innerHTML = BRAND_WORDMARK_HTML;
});
