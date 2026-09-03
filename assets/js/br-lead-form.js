/**
 * Billed Right — shared lead-capture form submit handler.
 *
 * Wires a <form> to POST its fields as JSON to the zoho-lead Netlify
 * Function instead of doing a normal browser form submission. Shared by
 * all 33 lead-capture forms on the site (contact form, chat widget,
 * service-page "consultation request" forms, specialty-page "brochure
 * request" forms, case-study forms) so the fetch/success/error logic
 * lives in exactly one place.
 *
 * Only calls preventDefault(), never stopPropagation() /
 * stopImmediatePropagation() — the existing GA4 form_submit hook in
 * br-analytics-events.js (a separate, capture-phase listener on
 * `document`) keeps firing on every submit completely independently of
 * this handler; the two don't interact.
 *
 * Usage (one line per form, right after the form in the page's HTML):
 *   <script>window.brWireLeadForm(document.currentScript.previousElementSibling, { formSource: "contact-page" });</script>
 */
(function () {
  'use strict';

  // This site has no shared stylesheet — every page carries its own
  // inline <style> block — so the success/error states this script adds
  // are styled here once, injected into <head>, rather than needing to
  // touch 32 separate pages' CSS.
  //
  // The submitting-button feedback reuses the site's existing button
  // transition timing (.br-btn's `transition: transform .15s ease` —
  // see pages/home.html's .br-btn rule) for the click bounce, rather
  // than inventing a new duration/easing. There's no existing spinner
  // anywhere on the site to reuse, so that part is necessarily new —
  // it borrows the button's own red/white color scheme instead of
  // introducing a new palette.
  var styleTag = document.createElement('style');
  styleTag.textContent =
    '.br-lead-form-error{margin-top:12px;padding:10px 14px;border-radius:8px;' +
    'background:rgba(186,32,37,.08);border:1px solid rgba(186,32,37,.25);' +
    'color:#941a1e;font-size:13px;line-height:1.5}' +
    '.br-lead-form-success{padding:24px;text-align:center;font-size:15px;' +
    'color:#31425E;line-height:1.6}' +
    '.br-lead-form-success strong{display:block;font-size:18px;margin-bottom:6px;color:#1a2535}' +
    '.br-lead-form-submitting{position:relative;color:transparent!important;' +
    'animation:br-lead-form-pulse .15s ease}' +
    '.br-lead-form-submitting::after{content:"";position:absolute;width:16px;height:16px;' +
    'top:50%;left:50%;margin:-8px 0 0 -8px;border:2px solid rgba(255,255,255,.4);' +
    'border-top-color:#fff;border-radius:50%;animation:br-lead-form-spin .6s linear infinite}' +
    '@keyframes br-lead-form-pulse{0%{transform:scale(1)}50%{transform:scale(.96)}100%{transform:scale(1)}}' +
    '@keyframes br-lead-form-spin{to{transform:rotate(360deg)}}';
  document.head.appendChild(styleTag);

  function formToPayload(form) {
    var data = {};
    var formData = new FormData(form);
    formData.forEach(function (value, key) {
      // Netlify Forms' own bookkeeping fields — not real lead data, and
      // zoho-lead.js doesn't read them.
      if (key === 'form-name' || key === 'bot-field') return;
      data[key] = value;
    });
    return data;
  }

  function setBusy(form, busy) {
    var submitBtn = form.querySelector('button[type="submit"]');
    if (!submitBtn) return;
    submitBtn.disabled = busy;
    if (busy) {
      // Restart the pulse/spinner animation even on a rapid re-click by
      // forcing a reflow between removing and re-adding the class.
      submitBtn.classList.remove('br-lead-form-submitting');
      void submitBtn.offsetWidth;
      submitBtn.classList.add('br-lead-form-submitting');
    } else {
      submitBtn.classList.remove('br-lead-form-submitting');
    }
  }

  var EMAIL_PATTERN = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  function showError(form, text) {
    var msg = form.querySelector('.br-lead-form-error');
    if (!msg) {
      msg = document.createElement('div');
      msg.className = 'br-lead-form-error';
      form.appendChild(msg);
    }
    msg.textContent = text;
  }

  function clearError(form) {
    var msg = form.querySelector('.br-lead-form-error');
    if (msg) msg.remove();
  }

  function showInlineSuccess(form) {
    Array.prototype.forEach.call(form.children, function (el) {
      el.style.display = 'none';
    });
    var success = document.createElement('div');
    success.className = 'br-lead-form-success';
    success.innerHTML =
      '<strong>Thank you.</strong> We’ve received your submission and will be in touch within one business day.';
    form.appendChild(success);
  }

  /**
   * @param {HTMLFormElement} form
   * @param {{formSource: string}} options
   */
  window.brWireLeadForm = function (form, options) {
    if (!form || form.tagName !== 'FORM') {
      console.error('br-lead-form: brWireLeadForm() was not given a <form> element');
      return;
    }
    options = options || {};
    var formSource = options.formSource || document.title || window.location.pathname;

    // A real thank-you confirmation page redirect is kept as-is (after a
    // successful submission, not before). Anything else — including
    // pages/case-studies/credentialing/index.html's form, whose action
    // is "/contact/" (another lead form, not a confirmation page) — gets
    // the inline success state instead of bouncing the visitor
    // somewhere that isn't actually a "thank you" experience.
    var action = form.getAttribute('action') || '';
    var thankYouRedirect = action.indexOf('/thank-you/') === 0 ? action : null;

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      clearError(form);

      // Client-side format check, before any network activity: a
      // malformed email (e.g. "test@example" — no "." after the @) is
      // something the visitor can fix immediately, so tell them
      // specifically rather than sending it to zoho-lead.js and getting
      // back a generic failure. Native browser type="email" validation
      // doesn't actually require a "." in the domain, so this catches
      // cases the browser itself lets through.
      var emailInput = form.querySelector('[name="email"]');
      if (emailInput && emailInput.value.trim() && !EMAIL_PATTERN.test(emailInput.value.trim())) {
        showError(form, 'Please check the email address you entered and try again');
        return;
      }

      var payload = formToPayload(form);
      payload.form_source = formSource;

      setBusy(form, true);

      fetch('/.netlify/functions/zoho-lead', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      })
        .then(function (res) {
          return res
            .json()
            .catch(function () {
              return {};
            })
            .then(function (body) {
              return { ok: res.ok, body: body };
            });
        })
        .then(function (result) {
          if (!result.ok || !result.body || result.body.success !== true) {
            throw new Error((result.body && result.body.error) || 'Submission failed');
          }
          if (thankYouRedirect) {
            window.location.href = thankYouRedirect;
            return; // navigating away — no need to re-enable the button
          }
          showInlineSuccess(form);
        })
        .catch(function (err) {
          console.error('br-lead-form: submission failed:', err);
          showError(
            form,
            'Something went wrong submitting the form. Please try again, or call us directly at 407-217-9281.'
          );
          setBusy(form, false);
        });
    });
  };
})();
