const KAPP_BRAND_HTML = 'ka<span class="wordmark-k">p</span>p';
document.querySelectorAll('[data-kapp-wordmark]').forEach((el) => {
  el.innerHTML = KAPP_BRAND_HTML;
});
