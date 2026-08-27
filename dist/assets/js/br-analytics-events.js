/**
 * Billed Right — GTM event tracking.
 * Pushes structured dataLayer events for conversion-relevant interactions
 * so GTM/GA4 can measure CTA clicks, phone clicks, and form submissions
 * without relying on brittle click-text matching inside GTM itself.
 */
(function () {
  'use strict';
  window.dataLayer = window.dataLayer || [];

  function push(event, data) {
    window.dataLayer.push(Object.assign({ event: event }, data));
  }

  document.addEventListener(
    'click',
    function (e) {
      var telLink = e.target.closest('a[href^="tel:"]');
      if (telLink) {
        push('phone_click', {
          phone_number: telLink.getAttribute('href').replace('tel:', ''),
          link_text: telLink.textContent.trim(),
          page_path: window.location.pathname,
        });
        return;
      }

      var ctaLink = e.target.closest(
        '.br-btn-red, .br-btn-outline, .br-btn-outline-dark'
      );
      if (ctaLink && ctaLink.tagName === 'A') {
        var style = ctaLink.classList.contains('br-btn-red')
          ? 'primary'
          : 'secondary';
        push('cta_click', {
          cta_text: ctaLink.textContent.trim(),
          cta_href: ctaLink.getAttribute('href'),
          cta_style: style,
          page_path: window.location.pathname,
        });
        return;
      }

      var subscribeBtn = e.target.closest('.br-footer-subscribe-form button');
      if (subscribeBtn) {
        push('newsletter_signup_click', { page_path: window.location.pathname });
      }
    },
    true
  );

  document.addEventListener(
    'submit',
    function (e) {
      var form = e.target;
      if (form && form.tagName === 'FORM') {
        push('form_submit', {
          form_name: form.getAttribute('name') || form.getAttribute('id') || 'unnamed_form',
          page_path: window.location.pathname,
        });
      }
    },
    true
  );
})();
