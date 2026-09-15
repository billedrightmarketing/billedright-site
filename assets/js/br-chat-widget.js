/* =============================================================
   Billed Right Live Chat Widget v3
   Uses Supabase JS client for reliable realtime
   Project: itgrapibtnuaoagtsiwh.supabase.co

   v3 adds a "Talk To Us" launcher teaser and a 3-option FAB menu
   (Live Chat / Call Us / Email Us) that expands from the launcher,
   plus an Email Us popup mirroring the /contact/ page's Netlify form.
   ============================================================= */
(function(){
  // ── Live Chat kill switch ────────────────────────────────────
  // Set to false to hide just the "Live Chat" option while we fix
  // issues with it — the launcher bubble, "Talk To Us" teaser, and
  // the Call Us / Email Us FAB options all stay fully visible and
  // functional. When false: the "Live Chat" FAB item isn't rendered,
  // its click handler isn't wired, and the Supabase chat backend
  // isn't initialized (so no stray unread badge from an old
  // conversation with no way to open it). Nothing else changes.
  // Flip back to true to bring Live Chat back.
  const LIVE_CHAT_ENABLED = false;

  const SUPA_URL = 'https://itgrapibtnuaoagtsiwh.supabase.co';
  const SUPA_KEY = 'sb_publishable_fuKICh99F0hIucOEjb-dqQ_tVrocUmC';
  const PHONE_DISPLAY = '407-217-9281';
  const PHONE_TEL = '+14072179281';

  // ── Load Supabase JS client then init ──────────────────────
  function loadSupabase(cb){
    if(window.supabase){ cb(window.supabase.createClient(SUPA_URL, SUPA_KEY)); return; }
    const s = document.createElement('script');
    s.src = 'https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2';
    s.onload = () => cb(window.supabase.createClient(SUPA_URL, SUPA_KEY));
    document.head.appendChild(s);
  }

  // ── State ──────────────────────────────────────────────────
  let db = null;
  let convId = null;
  let visitorName = '';
  let isOpen = false;
  let fabOpen = false;
  let contactOpen = false;
  let unread = 0;
  let realtimeChannel = null;

  // ── Styles ─────────────────────────────────────────────────
  const styles = `
  /* Widget elements are appended directly to <body>, outside the page's
     own .br-reset scope, so they don't inherit its box-sizing:border-box
     reset. Force it here so width:100% + padding behaves the same way
     for every element in the widget (inputs and buttons previously drifted
     out of alignment because of this). */
  #br-chat-window *, #br-contact-modal *, #br-fab-menu *, #br-chat-launcher *, #br-chat-teaser {
    box-sizing: border-box;
  }
  #br-chat-launcher {
    position: fixed; bottom: 24px; right: 24px; z-index: 99999;
    width: 56px; height: 56px; border-radius: 50%;
    background: #BA2025; border: none; cursor: pointer;
    display: flex; align-items: center; justify-content: center;
    box-shadow: 0 4px 20px rgba(186,32,37,0.45);
    transition: transform 0.2s, box-shadow 0.2s;
  }
  #br-chat-launcher:hover { transform: scale(1.08); box-shadow: 0 6px 28px rgba(186,32,37,0.55); }
  #br-chat-launcher svg { width: 26px; height: 26px; fill: #fff; }
  #br-chat-badge {
    position: absolute; top: -2px; right: -2px;
    background: #31425E; color: #fff; font-size: 10px; font-weight: 700;
    width: 18px; height: 18px; border-radius: 50%;
    display: none; align-items: center; justify-content: center;
    font-family: system-ui, sans-serif;
  }

  /* ── Talk To Us teaser bubble — sits up and to the left of the
     launcher, its curved corner tail pointing at the 10:30 position
     on the circle (diagonally up-left, not straight left). ── */
  #br-chat-teaser {
    position: fixed; bottom: 82px; right: 78px; z-index: 99999;
    background: #fff; color: #31425E; font-family: 'Inter', system-ui, sans-serif;
    font-size: 13px; font-weight: 600; padding: 11px 18px; border-radius: 20px 20px 6px 20px;
    box-shadow: 0 4px 18px rgba(0,0,0,0.14); cursor: pointer;
    white-space: nowrap; border: none;
    transform: scale(0.85) translateY(6px); opacity: 0; pointer-events: none;
    transition: transform 0.28s cubic-bezier(0.34,1.56,0.64,1), opacity 0.22s ease;
  }
  #br-chat-teaser.show { transform: scale(1) translateY(0); opacity: 1; pointer-events: all; }
  #br-chat-teaser .br-teaser-tail {
    position: absolute; right: -1px; bottom: -1px; width: 16px; height: 16px;
    transform: scaleX(-1);
  }

  /* ── FAB option menu ──
     One clean set of rules: fixed stack positioned 92px above the
     viewport bottom (clears the 56px launcher + its 24px offset + a
     little breathing room), 28px from the right edge, even 14px gaps
     between items via flex gap (no per-item margin hacks). */
  #br-fab-menu {
    position: fixed; right: 28px; bottom: 92px; z-index: 99997;
    display: flex; flex-direction: column-reverse; align-items: flex-end; gap: 14px;
    pointer-events: none;
  }
  .br-fab-item {
    display: flex; align-items: center; gap: 10px;
    transform: scale(0.4) translateY(10px); opacity: 0;
    transition: transform 0.24s cubic-bezier(0.34,1.56,0.64,1), opacity 0.18s ease;
    pointer-events: none;
  }
  .br-fab-item[data-fab="email"] { order: 1; }
  .br-fab-item[data-fab="call"]  { order: 2; }
  .br-fab-item[data-fab="chat"]  { order: 3; }
  #br-fab-menu.open .br-fab-item { transform: scale(1) translateY(0); opacity: 1; pointer-events: all; }
  #br-fab-menu.open .br-fab-item[data-fab="chat"] { transition-delay: 0.02s; }
  #br-fab-menu.open .br-fab-item[data-fab="call"] { transition-delay: 0.07s; }
  #br-fab-menu.open .br-fab-item[data-fab="email"] { transition-delay: 0.12s; }
  .br-fab-label {
    background: #31425E; color: #fff; font-family: 'Inter', system-ui, sans-serif;
    font-size: 12.5px; font-weight: 600; padding: 8px 14px; border-radius: 16px;
    white-space: nowrap; box-shadow: 0 3px 12px rgba(0,0,0,0.18);
  }
  .br-fab-circle {
    width: 48px; height: 48px; border-radius: 50%; background: #fff;
    display: flex; align-items: center; justify-content: center; flex-shrink: 0;
    box-shadow: 0 3px 14px rgba(0,0,0,0.2); text-decoration: none;
    transition: transform 0.15s;
  }
  .br-fab-circle:hover { transform: scale(1.08); }
  .br-fab-circle svg { width: 21px; height: 21px; stroke: #BA2025; fill: none; stroke-width: 2; }

  #br-chat-window, #br-contact-modal {
    position: fixed; bottom: 92px; right: 24px; z-index: 99998;
    width: min(360px, calc(100vw - 48px)); max-height: 560px; border-radius: 16px;
    background: #fff; box-shadow: 0 8px 40px rgba(0,0,0,0.18);
    display: flex; flex-direction: column; overflow: hidden;
    font-family: 'Inter', system-ui, sans-serif;
    transform: scale(0.92) translateY(12px); opacity: 0;
    pointer-events: none;
    transition: all 0.22s cubic-bezier(0.34,1.56,0.64,1);
  }
  #br-chat-window.open, #br-contact-modal.open { transform: scale(1) translateY(0); opacity: 1; pointer-events: all; }
  .br-chat-header {
    background: #31425E; padding: 16px 18px;
    display: flex; align-items: center; gap: 12px; flex-shrink: 0;
    box-sizing: border-box; width: 100%; border-radius: 16px 16px 0 0;
  }
  .br-chat-header-avatar {
    width: 40px; height: 40px; border-radius: 50%; background: #BA2025;
    display: flex; align-items: center; justify-content: center; font-size: 18px; flex-shrink: 0;
  }
  .br-chat-header-info { flex: 1; }
  .br-chat-header-name { color: #fff; font-weight: 700; font-size: 14px; line-height: 1.2; }
  .br-chat-header-status { display: flex; align-items: center; gap: 5px; margin-top: 2px; }
  .br-status-dot { width: 7px; height: 7px; border-radius: 50%; background: #4ade80; }
  .br-status-dot.offline { background: #94a3b8; }
  .br-chat-header-status span { font-size: 11px; color: rgba(255,255,255,0.7); }
  .br-chat-close {
    background: none; border: none; cursor: pointer;
    color: rgba(255,255,255,0.6); font-size: 20px; padding: 0; line-height: 1; transition: color 0.15s;
  }
  .br-chat-close:hover { color: #fff; }
  #br-chat-intro {
    padding: 6px 18px 20px; background: #f8fafc;
    border-bottom: 1px solid #e2e8f0; flex-shrink: 0;
  }
  #br-chat-intro p { font-size: 13px; color: #475569; margin-bottom: 12px; line-height: 1.5; }
  #br-chat-intro input {
    width: 100%; box-sizing: border-box; border: 1px solid #cbd5e1; border-radius: 8px;
    padding: 9px 12px; font-size: 13px; outline: none; margin-bottom: 8px;
    font-family: inherit; color: #1e293b; transition: border-color 0.15s; display: block;
  }
  #br-chat-intro input:focus { border-color: #BA2025; }
  #br-chat-start-btn {
    width: 100%; box-sizing: border-box; background: #BA2025; color: #fff; border: none;
    border-radius: 8px; padding: 10px; font-size: 13px; font-weight: 600;
    cursor: pointer; font-family: inherit; transition: background 0.15s;
  }
  #br-chat-start-btn:hover { background: #9b1a1e; }
  #br-chat-start-btn:disabled { background: #94a3b8; cursor: not-allowed; }
  #br-chat-messages {
    flex: 1; overflow-y: auto; padding: 14px 14px 10px;
    display: none; flex-direction: column; gap: 10px;
    min-height: 180px; background: #f8fafc;
  }
  .br-msg {
    max-width: 80%; padding: 9px 13px; border-radius: 14px;
    font-size: 13px; line-height: 1.5; word-break: break-word;
  }
  .br-msg.visitor {
    background: #31425E; color: #fff;
    align-self: flex-end; border-bottom-right-radius: 4px;
  }
  .br-msg.rep {
    background: #fff; color: #1e293b;
    align-self: flex-start; border-bottom-left-radius: 4px; border: 1px solid #e2e8f0;
  }
  .br-msg.system {
    background: transparent; color: #94a3b8; font-size: 11px;
    align-self: center; text-align: center; font-style: italic;
  }
  #br-chat-input-row {
    display: none; padding: 10px 12px; background: #fff;
    border-top: 1px solid #e2e8f0; gap: 8px; align-items: flex-end; flex-shrink: 0;
  }
  #br-chat-input {
    flex: 1; box-sizing: border-box; border: 1px solid #cbd5e1; border-radius: 10px;
    padding: 9px 12px; font-size: 13px; outline: none; resize: none;
    font-family: inherit; max-height: 90px; min-height: 36px;
    line-height: 1.4; color: #1e293b; transition: border-color 0.15s;
  }
  #br-chat-input:focus { border-color: #BA2025; }
  #br-chat-send {
    width: 36px; height: 36px; box-sizing: border-box; border-radius: 50%; background: #BA2025;
    border: none; cursor: pointer; display: flex; align-items: center;
    justify-content: center; flex-shrink: 0; transition: background 0.15s;
  }
  #br-chat-send:hover { background: #9b1a1e; }
  #br-chat-send svg { width: 16px; height: 16px; fill: #fff; }

  /* ── Contact popup form ── */
  #br-contact-modal { max-height: 78vh; }
  #br-contact-body { padding: 16px 18px 18px; overflow-y: auto; background: #fff; }
  #br-contact-body p.br-cf-sub { font-size: 12.5px; color: #64748b; margin-bottom: 14px; line-height: 1.5; }
  .br-cf-field { margin-bottom: 10px; }
  .br-cf-field label { display: block; font-size: 11.5px; font-weight: 600; color: #31425E; margin-bottom: 4px; }
  .br-cf-field input, .br-cf-field select, .br-cf-field textarea {
    width: 100%; border: 1px solid #cbd5e1; border-radius: 8px;
    padding: 9px 11px; font-size: 13px; outline: none; font-family: inherit;
    color: #1e293b; transition: border-color 0.15s; box-sizing: border-box;
  }
  .br-cf-field input:focus, .br-cf-field select:focus, .br-cf-field textarea:focus { border-color: #BA2025; }
  .br-cf-field textarea { resize: vertical; min-height: 54px; }
  #br-contact-body button[type="submit"] {
    width: 100%; box-sizing: border-box; background: #BA2025; color: #fff; border: none;
    border-radius: 8px; padding: 11px; font-size: 13px; font-weight: 700;
    cursor: pointer; font-family: inherit; transition: background 0.15s;
    display: flex; align-items: center; justify-content: center; gap: 6px; margin-top: 4px;
  }
  #br-contact-body button[type="submit"]:hover { background: #9b1a1e; }
  #br-contact-body button[type="submit"] svg { width: 15px; height: 15px; fill: #fff; }
  .br-cf-fine { font-size: 10.5px; color: #94a3b8; margin-top: 8px; line-height: 1.4; text-align: center; }

  @media(max-width: 400px){
    #br-chat-window, #br-contact-modal { width: calc(100vw - 24px); right: 12px; bottom: 80px; }
    #br-chat-teaser { font-size: 12px; padding: 9px 15px; }
  }
  `;

  const styleEl = document.createElement('style');
  styleEl.textContent = styles;
  document.head.appendChild(styleEl);

  // ── Build DOM: launcher ──────────────────────────────────────
  const launcher = document.createElement('button');
  launcher.id = 'br-chat-launcher';
  launcher.setAttribute('aria-label', 'Talk to Billed Right');
  launcher.innerHTML = `
    <svg viewBox="0 0 24 24"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm0 14H6l-2 2V4h16v12z"/></svg>
    <span id="br-chat-badge"></span>
  `;
  document.body.appendChild(launcher);

  // ── Build DOM: "Talk To Us" teaser bubble ─────────────────────
  const teaser = document.createElement('button');
  teaser.id = 'br-chat-teaser';
  teaser.type = 'button';
  teaser.innerHTML = `Talk To Us<svg class="br-teaser-tail" viewBox="0 0 30 30" aria-hidden="true"><path d="M30 30C13 30 0 17 0 0v30h30z" fill="#fff"/></svg>`;
  document.body.appendChild(teaser);

  // ── Build DOM: FAB option menu ────────────────────────────────
  const fabMenu = document.createElement('div');
  fabMenu.id = 'br-fab-menu';
  fabMenu.innerHTML = `
    ${LIVE_CHAT_ENABLED ? `
    <div class="br-fab-item" data-fab="chat">
      <span class="br-fab-label">Live Chat</span>
      <button class="br-fab-circle" id="br-fab-chat" aria-label="Start live chat" type="button">
        <svg viewBox="0 0 24 24"><path d="M21 11.5a8.38 8.38 0 01-.9 3.8 8.5 8.5 0 01-7.6 4.7 8.38 8.38 0 01-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 01-.9-3.8 8.5 8.5 0 014.7-7.6 8.38 8.38 0 013.8-.9h.5a8.48 8.48 0 018 8v.5z"/></svg>
      </button>
    </div>` : ''}
    <div class="br-fab-item" data-fab="call">
      <span class="br-fab-label">Call Us</span>
      <a class="br-fab-circle" id="br-fab-call" href="tel:${PHONE_TEL}" aria-label="Call ${PHONE_DISPLAY}">
        <svg viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6A19.79 19.79 0 01.01 4.18 2 2 0 012 2h3a2 2 0 012 1.72c.13.96.36 1.9.7 2.81a2 2 0 01-.45 2.11L6.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0122 16.92z"/></svg>
      </a>
    </div>
    <div class="br-fab-item" data-fab="email">
      <span class="br-fab-label">Email Us</span>
      <button class="br-fab-circle" id="br-fab-email" aria-label="Open contact form" type="button">
        <svg viewBox="0 0 24 24"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22 6 12 13 2 6"/></svg>
      </button>
    </div>
  `;
  document.body.appendChild(fabMenu);

  // ── Build DOM: chat window ─────────────────────────────────
  const win = document.createElement('div');
  win.id = 'br-chat-window';
  win.innerHTML = `
    <div class="br-chat-header">
      <div class="br-chat-header-avatar">💬</div>
      <div class="br-chat-header-info">
        <div class="br-chat-header-name">Billed Right Sales</div>
        <div class="br-chat-header-status">
          <div class="br-status-dot" id="br-online-dot"></div>
          <span id="br-online-label">Available now</span>
        </div>
      </div>
      <button class="br-chat-close" id="br-close-btn" aria-label="Close chat">&times;</button>
    </div>
    <div id="br-chat-intro">
      <p>Hi there! Have a question about medical billing or our services? Our team is here to help.</p>
      <input type="text" id="br-visitor-name" placeholder="Your name (required)" maxlength="60"/>
      <input type="email" id="br-visitor-email" placeholder="Your email (optional)" maxlength="100"/>
      <button id="br-chat-start-btn">Start Conversation</button>
    </div>
    <div id="br-chat-messages"></div>
    <div id="br-chat-input-row">
      <textarea id="br-chat-input" placeholder="Type a message..." rows="1"></textarea>
      <button id="br-chat-send" aria-label="Send">
        <svg viewBox="0 0 24 24"><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/></svg>
      </button>
    </div>
  `;
  document.body.appendChild(win);

  // ── Build DOM: contact popup (mirrors /contact/'s Netlify form) ──
  const contactModal = document.createElement('div');
  contactModal.id = 'br-contact-modal';
  contactModal.innerHTML = `
    <div class="br-chat-header">
      <div class="br-chat-header-avatar">✉️</div>
      <div class="br-chat-header-info">
        <div class="br-chat-header-name">Talk to a Solution Specialist</div>
        <div class="br-chat-header-status"><span>A solution specialist responds within one business day.</span></div>
      </div>
      <button class="br-chat-close" id="br-contact-close-btn" aria-label="Close contact form">&times;</button>
    </div>
    <div id="br-contact-body">
      <form name="contact-billing-review-request" method="POST" data-netlify="true" action="/thank-you/contact/">
        <input type="hidden" name="form-name" value="contact-billing-review-request">
        <input type="hidden" name="bot-field" />
        <input type="hidden" name="page_url" value="">
        <div class="br-cf-field"><label for="br-w-name">Name</label><input type="text" id="br-w-name" name="name" required autocomplete="name"></div>
        <div class="br-cf-field"><label for="br-w-phone">Phone Number</label><input type="tel" id="br-w-phone" name="phone" placeholder="(407) 000-0000" autocomplete="tel"></div>
        <div class="br-cf-field"><label for="br-w-email">Work Email</label><input type="email" id="br-w-email" name="email" placeholder="you@yourpractice.com" autocomplete="email"></div>
        <div class="br-cf-field"><label for="br-w-practice">Practice Name</label><input type="text" id="br-w-practice" name="practice" placeholder="Your practice name" required autocomplete="organization"></div>
        <div class="br-cf-field"><label for="br-w-message">What's your biggest billing challenge?</label><textarea id="br-w-message" name="message" placeholder="Tell us where you're losing revenue..."></textarea></div>
        <button type="submit" aria-label="Submit contact request">
          Talk to a Solution Specialist
          <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
        </button>
        <p class="br-cf-fine">Your information is HIPAA-protected. No contracts required.</p>
      </form>
    </div>
  `;
  document.body.appendChild(contactModal);

  // Well-known medicine/science names (real historical figures + TV
  // doctors) — same fixed list used on /contact/'s form. Randomized
  // independently of that page's own pick.
  const BR_NAME_EXAMPLES = ['Albert Einstein', 'Marie Curie', 'Jonas Salk', 'Louis Pasteur', 'Florence Nightingale', 'Alexander Fleming', 'Elizabeth Blackwell', 'Meredith Grey', 'Gregory House', 'Derek Shepherd', 'Shaun Murphy', 'Doogie Howser', 'John Watson', 'Cristina Yang'];
  const contactNameInput = document.getElementById('br-w-name');
  if (contactNameInput) {
    contactNameInput.placeholder = 'e.g. ' + BR_NAME_EXAMPLES[Math.floor(Math.random() * BR_NAME_EXAMPLES.length)];
  }

  const contactFormEl = contactModal.querySelector('form');
  const contactEmailEl = document.getElementById('br-w-email');
  const contactPhoneEl = document.getElementById('br-w-phone');
  // Email and phone are each optional individually, but at least one is
  // required so a solution specialist has a way to respond. Native
  // `required` can't express "one of two fields", so this listener
  // (registered before brWireLeadForm's own submit handler) checks it
  // and, on failure, stops that handler from also running via
  // stopImmediatePropagation.
  contactFormEl.addEventListener('submit', function(e) {
    if (!contactEmailEl.value.trim() && !contactPhoneEl.value.trim()) {
      e.preventDefault();
      e.stopImmediatePropagation();
      let msg = contactFormEl.querySelector('.br-contact-validation-error');
      if (!msg) {
        msg = document.createElement('div');
        msg.className = 'br-contact-validation-error br-lead-form-error';
        contactFormEl.appendChild(msg);
      }
      msg.textContent = 'Please provide an email address or phone number.';
      (contactEmailEl || contactPhoneEl).focus();
    }
  });

  if (window.brWireLeadForm) {
    window.brWireLeadForm(contactFormEl, { formSource: 'chat-widget' });
  }

  // ── Teaser visibility ──────────────────────────────────────
  function showTeaser(){ if(!isOpen && !fabOpen && !contactOpen) teaser.classList.add('show'); }
  function hideTeaser(){ teaser.classList.remove('show'); }
  setTimeout(showTeaser, 900);

  // ── FAB menu open/close ─────────────────────────────────────
  function openFab(){
    fabOpen = true;
    fabMenu.classList.add('open');
    hideTeaser();
  }
  function closeFab(){
    fabOpen = false;
    fabMenu.classList.remove('open');
    showTeaser();
  }
  function toggleFab(){ fabOpen ? closeFab() : openFab(); }

  // ── Chat open/close ─────────────────────────────────────────
  function openChat(){
    closeFab();
    closeContactModal();
    isOpen = true;
    win.classList.add('open');
    hideTeaser();
    unread = 0;
    updateBadge();
    setTimeout(() => {
      const el = convId
        ? document.getElementById('br-chat-input')
        : document.getElementById('br-visitor-name');
      if(el) el.focus();
    }, 100);
  }
  function closeChat(){ isOpen = false; win.classList.remove('open'); showTeaser(); }
  function updateBadge(){
    const badge = document.getElementById('br-chat-badge');
    if(unread > 0){ badge.style.display = 'flex'; badge.textContent = unread > 9 ? '9+' : unread; }
    else { badge.style.display = 'none'; }
  }

  // ── Contact popup open/close ─────────────────────────────────
  function openContactModal(){
    closeFab();
    closeChat();
    contactOpen = true;
    contactModal.classList.add('open');
    hideTeaser();
    setTimeout(() => {
      const el = document.getElementById('br-w-name');
      if(el) el.focus();
    }, 100);
  }
  function closeContactModal(){
    contactOpen = false;
    contactModal.classList.remove('open');
    showTeaser();
  }

  // ── Wire up launcher / teaser / FAB items ───────────────────
  launcher.addEventListener('click', () => {
    if(isOpen){ closeChat(); return; }
    if(contactOpen){ closeContactModal(); return; }
    toggleFab();
  });
  teaser.addEventListener('click', toggleFab);
  document.getElementById('br-close-btn').addEventListener('click', closeChat);
  document.getElementById('br-contact-close-btn').addEventListener('click', closeContactModal);
  if (LIVE_CHAT_ENABLED) {
    document.getElementById('br-fab-chat').addEventListener('click', openChat);
  }
  document.getElementById('br-fab-call').addEventListener('click', closeFab);
  document.getElementById('br-fab-email').addEventListener('click', openContactModal);

  document.addEventListener('click', (e) => {
    if(!fabOpen) return;
    if(fabMenu.contains(e.target) || launcher.contains(e.target) || teaser.contains(e.target)) return;
    closeFab();
  });

  // ── Start conversation ─────────────────────────────────────
  document.getElementById('br-chat-start-btn').addEventListener('click', async () => {
    const nameEl = document.getElementById('br-visitor-name');
    const emailEl = document.getElementById('br-visitor-email');
    visitorName = nameEl.value.trim();
    if(!visitorName){ nameEl.focus(); nameEl.style.borderColor = '#BA2025'; return; }
    nameEl.style.borderColor = '';

    const btn = document.getElementById('br-chat-start-btn');
    btn.textContent = 'Connecting...';
    btn.disabled = true;

    try {
      const { data, error } = await db
        .from('chat_conversations')
        .insert({ visitor_name: visitorName, visitor_email: emailEl.value.trim() || null, status: 'open' })
        .select()
        .single();

      if(error) throw error;

      convId = data.id;
      document.getElementById('br-chat-intro').style.display = 'none';
      document.getElementById('br-chat-messages').style.display = 'flex';
      document.getElementById('br-chat-input-row').style.display = 'flex';

      try {
        localStorage.setItem('br_conv_id', convId);
        localStorage.setItem('br_visitor_name', visitorName);
      } catch(storageErr){ /* localStorage unavailable — conversation just won't persist across reloads */ }

      appendMessage('Hi ' + visitorName + '! A member of our team will be with you shortly. How can we help?', 'rep');
      subscribeToReplies();
      document.getElementById('br-chat-input').focus();

    } catch(err){
      console.error('Chat error:', err);
      btn.textContent = 'Start Conversation';
      btn.disabled = false;
      appendMessage('Connection issue. Please try again.', 'system');
    }
  });

  // ── Realtime subscription using Supabase JS client ─────────
  function subscribeToReplies(){
    if(!convId || !db) return;

    realtimeChannel = db
      .channel('chat-replies-' + convId)
      .on(
        'postgres_changes',
        {
          event: 'INSERT',
          schema: 'public',
          table: 'chat_messages',
          filter: 'conversation_id=eq.' + convId
        },
        (payload) => {
          const msg = payload.new;
          if(msg.sender === 'rep'){
            appendMessage(msg.content, 'rep');
            if(!isOpen){ unread++; updateBadge(); }
          }
        }
      )
      .subscribe((status) => {
        console.log('Billed Right chat realtime status:', status);
      });
  }

  // ── Send message ───────────────────────────────────────────
  async function sendMessage(){
    if(!convId || !db) return;
    const input = document.getElementById('br-chat-input');
    const content = input.value.trim();
    if(!content) return;
    input.value = '';
    input.style.height = '';
    appendMessage(content, 'visitor');
    try {
      const { error } = await db.from('chat_messages').insert({
        conversation_id: convId,
        sender: 'visitor',
        content: content
      });
      if(error) throw error;
    } catch(err){
      appendMessage('Message could not be sent. Please check your connection.', 'system');
    }
  }

  document.getElementById('br-chat-send').addEventListener('click', sendMessage);
  document.getElementById('br-chat-input').addEventListener('keydown', (e) => {
    if(e.key === 'Enter' && !e.shiftKey){ e.preventDefault(); sendMessage(); }
  });
  document.getElementById('br-chat-input').addEventListener('input', function(){
    this.style.height = 'auto';
    this.style.height = Math.min(this.scrollHeight, 90) + 'px';
  });

  // ── Append message ─────────────────────────────────────────
  function appendMessage(content, sender){
    const msgs = document.getElementById('br-chat-messages');
    const div = document.createElement('div');
    div.className = 'br-msg ' + sender;
    div.textContent = content;
    msgs.appendChild(div);
    msgs.scrollTop = msgs.scrollHeight;
  }

  // ── Restore an existing conversation from localStorage ──────
  async function restoreConversation(savedConvId, savedName){
    convId = savedConvId;
    visitorName = savedName;

    document.getElementById('br-chat-intro').style.display = 'none';
    document.getElementById('br-chat-messages').style.display = 'flex';
    document.getElementById('br-chat-input-row').style.display = 'flex';

    try {
      const { data, error } = await db
        .from('chat_messages')
        .select('*')
        .eq('conversation_id', savedConvId)
        .order('created_at', { ascending: true });

      if(error) throw error;

      (data || []).forEach((msg) => appendMessage(msg.content, msg.sender));
    } catch(err){
      console.error('Chat restore error:', err);
    }

    appendMessage('Welcome back, ' + visitorName + '. Continuing your conversation.', 'system');
    subscribeToReplies();
  }

  // ── Init ───────────────────────────────────────────────────
  // Skipped while Live Chat is disabled — no backend to connect to,
  // no reason to load the Supabase SDK or restore an old conversation
  // into a chat window nothing links to anymore.
  if (LIVE_CHAT_ENABLED) {
    loadSupabase(async (client) => {
      db = client;
      console.log('Billed Right chat widget ready');

      let savedConvId = null;
      let savedName = null;
      try {
        savedConvId = localStorage.getItem('br_conv_id');
        savedName = localStorage.getItem('br_visitor_name');
      } catch(storageErr){ /* localStorage unavailable — fall back to the intro form */ }

      if(savedConvId && savedName){
        await restoreConversation(savedConvId, savedName);
      }
    });
  }

})();
