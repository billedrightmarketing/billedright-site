/* =============================================================
   Billed Right Live Chat Widget
   Connects to Supabase: epvensmhlhkhlvmmejob.supabase.co
   Tables: chat_conversations, chat_messages
   ============================================================= */
(function(){
  const SUPA_URL = 'https://epvensmhlhkhlvmmejob.supabase.co';
  const SUPA_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVwdmVuc21obGhraGx2bW1lam9iIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDU3MDU1NzcsImV4cCI6MjA2MTI4MTU3N30.lkKMb0JMGhpHzNvlOHPZTc0P2P5TyTTdvdHa0N2SbSs';

  // ── State ──────────────────────────────────────────────────
  let convId = null;
  let visitorName = '';
  let channel = null;
  let isOpen = false;
  let isOnline = true; // toggled by rep presence (future) — default true for now
  let unread = 0;

  // ── Supabase REST helpers ──────────────────────────────────
  async function sbPost(path, body){
    const r = await fetch(SUPA_URL + '/rest/v1/' + path, {
      method:'POST',
      headers:{
        'apikey': SUPA_KEY,
        'Authorization': 'Bearer ' + SUPA_KEY,
        'Content-Type': 'application/json',
        'Prefer': 'return=representation'
      },
      body: JSON.stringify(body)
    });
    return r.json();
  }

  async function sbGet(path){
    const r = await fetch(SUPA_URL + '/rest/v1/' + path, {
      headers:{
        'apikey': SUPA_KEY,
        'Authorization': 'Bearer ' + SUPA_KEY
      }
    });
    return r.json();
  }

  // ── Subscribe to new messages via Supabase realtime ────────
  function subscribeToMessages(){
    if(!convId) return;
    const wsUrl = SUPA_URL.replace('https','wss') + '/realtime/v1/websocket?apikey=' + SUPA_KEY + '&vsn=1.0.0';
    const ws = new WebSocket(wsUrl);

    ws.onopen = () => {
      ws.send(JSON.stringify({
        topic: 'realtime:public:chat_messages:conversation_id=eq.' + convId,
        event: 'phx_join',
        payload: {},
        ref: '1'
      }));
    };

    ws.onmessage = (e) => {
      const msg = JSON.parse(e.data);
      if(msg.event === 'INSERT' && msg.payload && msg.payload.record){
        const rec = msg.payload.record;
        if(rec.sender === 'rep'){
          appendMessage(rec.content, 'rep');
          if(!isOpen){
            unread++;
            updateBadge();
          }
        }
      }
    };

    channel = ws;
  }

  // ── DOM build ──────────────────────────────────────────────
  const styles = `
  #br-chat-launcher {
    position: fixed;
    bottom: 24px;
    right: 24px;
    z-index: 99999;
    width: 56px;
    height: 56px;
    border-radius: 50%;
    background: #BA2025;
    border: none;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 20px rgba(186,32,37,0.45);
    transition: transform 0.2s, box-shadow 0.2s;
  }
  #br-chat-launcher:hover {
    transform: scale(1.08);
    box-shadow: 0 6px 28px rgba(186,32,37,0.55);
  }
  #br-chat-launcher svg { width: 26px; height: 26px; fill: #fff; }
  #br-chat-badge {
    position: absolute;
    top: -2px;
    right: -2px;
    background: #31425E;
    color: #fff;
    font-size: 10px;
    font-weight: 700;
    width: 18px;
    height: 18px;
    border-radius: 50%;
    display: none;
    align-items: center;
    justify-content: center;
    font-family: system-ui, sans-serif;
  }
  #br-chat-window {
    position: fixed;
    bottom: 92px;
    right: 24px;
    z-index: 99998;
    width: 360px;
    max-height: 520px;
    border-radius: 16px;
    background: #fff;
    box-shadow: 0 8px 40px rgba(0,0,0,0.18);
    display: flex;
    flex-direction: column;
    overflow: hidden;
    font-family: 'Inter', system-ui, sans-serif;
    transform: scale(0.92) translateY(12px);
    opacity: 0;
    pointer-events: none;
    transition: all 0.22s cubic-bezier(0.34,1.56,0.64,1);
  }
  #br-chat-window.open {
    transform: scale(1) translateY(0);
    opacity: 1;
    pointer-events: all;
  }
  .br-chat-header {
    background: #31425E;
    padding: 16px 18px;
    display: flex;
    align-items: center;
    gap: 12px;
    flex-shrink: 0;
  }
  .br-chat-header-avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: #BA2025;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    flex-shrink: 0;
  }
  .br-chat-header-info { flex: 1; }
  .br-chat-header-name {
    color: #fff;
    font-weight: 700;
    font-size: 14px;
    line-height: 1.2;
  }
  .br-chat-header-status {
    display: flex;
    align-items: center;
    gap: 5px;
    margin-top: 2px;
  }
  .br-status-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #4ade80;
  }
  .br-status-dot.offline { background: #94a3b8; }
  .br-chat-header-status span {
    font-size: 11px;
    color: rgba(255,255,255,0.7);
  }
  .br-chat-close {
    background: none;
    border: none;
    cursor: pointer;
    color: rgba(255,255,255,0.6);
    font-size: 20px;
    padding: 0;
    line-height: 1;
    transition: color 0.15s;
  }
  .br-chat-close:hover { color: #fff; }
  #br-chat-intro {
    padding: 20px 18px;
    background: #f8fafc;
    border-bottom: 1px solid #e2e8f0;
    flex-shrink: 0;
  }
  #br-chat-intro p {
    font-size: 13px;
    color: #475569;
    margin-bottom: 12px;
    line-height: 1.5;
  }
  #br-chat-intro input {
    width: 100%;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    padding: 9px 12px;
    font-size: 13px;
    outline: none;
    margin-bottom: 8px;
    font-family: inherit;
    color: #1e293b;
    transition: border-color 0.15s;
  }
  #br-chat-intro input:focus { border-color: #BA2025; }
  #br-chat-start-btn {
    width: 100%;
    background: #BA2025;
    color: #fff;
    border: none;
    border-radius: 8px;
    padding: 10px;
    font-size: 13px;
    font-weight: 600;
    cursor: pointer;
    font-family: inherit;
    transition: background 0.15s;
  }
  #br-chat-start-btn:hover { background: #9b1a1e; }
  #br-chat-messages {
    flex: 1;
    overflow-y: auto;
    padding: 14px 14px 10px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    min-height: 180px;
    background: #f8fafc;
    display: none;
  }
  .br-msg {
    max-width: 80%;
    padding: 9px 13px;
    border-radius: 14px;
    font-size: 13px;
    line-height: 1.5;
    word-break: break-word;
  }
  .br-msg.visitor {
    background: #31425E;
    color: #fff;
    align-self: flex-end;
    border-bottom-right-radius: 4px;
  }
  .br-msg.rep {
    background: #fff;
    color: #1e293b;
    align-self: flex-start;
    border-bottom-left-radius: 4px;
    border: 1px solid #e2e8f0;
  }
  .br-msg.system {
    background: transparent;
    color: #94a3b8;
    font-size: 11px;
    align-self: center;
    text-align: center;
    font-style: italic;
  }
  #br-chat-input-row {
    display: none;
    padding: 10px 12px;
    background: #fff;
    border-top: 1px solid #e2e8f0;
    gap: 8px;
    align-items: flex-end;
    flex-shrink: 0;
  }
  #br-chat-input {
    flex: 1;
    border: 1px solid #cbd5e1;
    border-radius: 10px;
    padding: 9px 12px;
    font-size: 13px;
    outline: none;
    resize: none;
    font-family: inherit;
    max-height: 90px;
    min-height: 36px;
    line-height: 1.4;
    color: #1e293b;
    transition: border-color 0.15s;
  }
  #br-chat-input:focus { border-color: #BA2025; }
  #br-chat-send {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background: #BA2025;
    border: none;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    transition: background 0.15s;
  }
  #br-chat-send:hover { background: #9b1a1e; }
  #br-chat-send svg { width: 16px; height: 16px; fill: #fff; }
  #br-offline-msg {
    padding: 16px 18px;
    background: #f1f5f9;
    border-top: 1px solid #e2e8f0;
    font-size: 12px;
    color: #64748b;
    line-height: 1.5;
    text-align: center;
    display: none;
    flex-shrink: 0;
  }
  @media(max-width: 400px){
    #br-chat-window { width: calc(100vw - 24px); right: 12px; bottom: 80px; }
  }
  `;

  const styleEl = document.createElement('style');
  styleEl.textContent = styles;
  document.head.appendChild(styleEl);

  // Launcher button
  const launcher = document.createElement('button');
  launcher.id = 'br-chat-launcher';
  launcher.setAttribute('aria-label', 'Chat with Billed Right');
  launcher.innerHTML = `
    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
      <path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm0 14H6l-2 2V4h16v12z"/>
    </svg>
    <span id="br-chat-badge"></span>
  `;
  document.body.appendChild(launcher);

  // Chat window
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
      <p>Hi there! Have questions about medical billing or our services? Our team is here to help.</p>
      <input type="text" id="br-visitor-name" placeholder="Your name (required)" maxlength="60"/>
      <input type="email" id="br-visitor-email" placeholder="Your email (optional)" maxlength="100"/>
      <button id="br-chat-start-btn">Start Conversation</button>
    </div>

    <div id="br-chat-messages"></div>

    <div id="br-offline-msg">
      Our team is currently offline. Leave your message above and we will follow up by email as soon as possible.
    </div>

    <div id="br-chat-input-row">
      <textarea id="br-chat-input" placeholder="Type a message..." rows="1"></textarea>
      <button id="br-chat-send" aria-label="Send">
        <svg viewBox="0 0 24 24"><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/></svg>
      </button>
    </div>
  `;
  document.body.appendChild(win);

  // ── Toggle open/close ──────────────────────────────────────
  function openChat(){
    isOpen = true;
    win.classList.add('open');
    unread = 0;
    updateBadge();
    if(!convId){
      document.getElementById('br-visitor-name').focus();
    } else {
      document.getElementById('br-chat-input').focus();
    }
  }

  function closeChat(){
    isOpen = false;
    win.classList.remove('open');
  }

  function updateBadge(){
    const badge = document.getElementById('br-chat-badge');
    if(unread > 0){
      badge.style.display = 'flex';
      badge.textContent = unread > 9 ? '9+' : unread;
    } else {
      badge.style.display = 'none';
    }
  }

  launcher.addEventListener('click', () => isOpen ? closeChat() : openChat());
  document.getElementById('br-close-btn').addEventListener('click', closeChat);

  // ── Start conversation ─────────────────────────────────────
  document.getElementById('br-chat-start-btn').addEventListener('click', async () => {
    const nameEl = document.getElementById('br-visitor-name');
    const emailEl = document.getElementById('br-visitor-email');
    visitorName = nameEl.value.trim();
    if(!visitorName){ nameEl.focus(); nameEl.style.borderColor='#BA2025'; return; }
    nameEl.style.borderColor='';

    const btn = document.getElementById('br-chat-start-btn');
    btn.textContent = 'Connecting...';
    btn.disabled = true;

    try {
      const res = await sbPost('chat_conversations', {
        visitor_name: visitorName,
        visitor_email: emailEl.value.trim() || null,
        status: 'open'
      });

      if(res && res[0]){
        convId = res[0].id;
        document.getElementById('br-chat-intro').style.display = 'none';
        document.getElementById('br-chat-messages').style.display = 'flex';
        document.getElementById('br-chat-input-row').style.display = 'flex';

        appendMessage('Hi ' + visitorName + '! A member of our team will be with you shortly. How can we help?', 'rep');
        subscribeToMessages();
        document.getElementById('br-chat-input').focus();
      } else {
        throw new Error('No conversation ID returned');
      }
    } catch(err){
      btn.textContent = 'Start Conversation';
      btn.disabled = false;
      appendMessage('Sorry, there was a connection issue. Please try again.', 'system');
    }
  });

  // ── Send message ───────────────────────────────────────────
  async function sendMessage(){
    if(!convId) return;
    const input = document.getElementById('br-chat-input');
    const content = input.value.trim();
    if(!content) return;

    input.value = '';
    input.style.height = '';
    appendMessage(content, 'visitor');

    try {
      await sbPost('chat_messages', {
        conversation_id: convId,
        sender: 'visitor',
        content: content
      });
    } catch(err){
      appendMessage('Message could not be sent. Please check your connection.', 'system');
    }
  }

  document.getElementById('br-chat-send').addEventListener('click', sendMessage);

  document.getElementById('br-chat-input').addEventListener('keydown', (e) => {
    if(e.key === 'Enter' && !e.shiftKey){
      e.preventDefault();
      sendMessage();
    }
  });

  // Auto-resize textarea
  document.getElementById('br-chat-input').addEventListener('input', function(){
    this.style.height = 'auto';
    this.style.height = Math.min(this.scrollHeight, 90) + 'px';
  });

  // ── Append message to UI ───────────────────────────────────
  function appendMessage(content, sender){
    const msgs = document.getElementById('br-chat-messages');
    const div = document.createElement('div');
    div.className = 'br-msg ' + sender;
    div.textContent = content;
    msgs.appendChild(div);
    msgs.scrollTop = msgs.scrollHeight;
  }

})();
