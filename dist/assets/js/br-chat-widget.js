/* =============================================================
   Billed Right Live Chat Widget v2
   Uses Supabase JS client for reliable realtime
   Project: itgrapibtnuaoagtsiwh.supabase.co
   ============================================================= */
(function(){
  const SUPA_URL = 'https://itgrapibtnuaoagtsiwh.supabase.co';
  const SUPA_KEY = 'sb_publishable_fuKICh99F0hIucOEjb-dqQ_tVrocUmC';

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
  let unread = 0;
  let realtimeChannel = null;

  // ── Styles ─────────────────────────────────────────────────
  const styles = `
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
  #br-chat-window {
    position: fixed; bottom: 92px; right: 24px; z-index: 99998;
    width: 360px; max-height: 520px; border-radius: 16px;
    background: #fff; box-shadow: 0 8px 40px rgba(0,0,0,0.18);
    display: flex; flex-direction: column; overflow: hidden;
    font-family: 'Inter', system-ui, sans-serif;
    transform: scale(0.92) translateY(12px); opacity: 0;
    pointer-events: none;
    transition: all 0.22s cubic-bezier(0.34,1.56,0.64,1);
  }
  #br-chat-window.open { transform: scale(1) translateY(0); opacity: 1; pointer-events: all; }
  .br-chat-header {
    background: #31425E; padding: 16px 18px;
    display: flex; align-items: center; gap: 12px; flex-shrink: 0;
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
    padding: 20px 18px; background: #f8fafc;
    border-bottom: 1px solid #e2e8f0; flex-shrink: 0;
  }
  #br-chat-intro p { font-size: 13px; color: #475569; margin-bottom: 12px; line-height: 1.5; }
  #br-chat-intro input {
    width: 100%; border: 1px solid #cbd5e1; border-radius: 8px;
    padding: 9px 12px; font-size: 13px; outline: none; margin-bottom: 8px;
    font-family: inherit; color: #1e293b; transition: border-color 0.15s; display: block;
  }
  #br-chat-intro input:focus { border-color: #BA2025; }
  #br-chat-start-btn {
    width: 100%; background: #BA2025; color: #fff; border: none;
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
    flex: 1; border: 1px solid #cbd5e1; border-radius: 10px;
    padding: 9px 12px; font-size: 13px; outline: none; resize: none;
    font-family: inherit; max-height: 90px; min-height: 36px;
    line-height: 1.4; color: #1e293b; transition: border-color 0.15s;
  }
  #br-chat-input:focus { border-color: #BA2025; }
  #br-chat-send {
    width: 36px; height: 36px; border-radius: 50%; background: #BA2025;
    border: none; cursor: pointer; display: flex; align-items: center;
    justify-content: center; flex-shrink: 0; transition: background 0.15s;
  }
  #br-chat-send:hover { background: #9b1a1e; }
  #br-chat-send svg { width: 16px; height: 16px; fill: #fff; }
  @media(max-width: 400px){
    #br-chat-window { width: calc(100vw - 24px); right: 12px; bottom: 80px; }
  }
  `;

  const styleEl = document.createElement('style');
  styleEl.textContent = styles;
  document.head.appendChild(styleEl);

  // ── Build DOM ──────────────────────────────────────────────
  const launcher = document.createElement('button');
  launcher.id = 'br-chat-launcher';
  launcher.setAttribute('aria-label', 'Chat with Billed Right');
  launcher.innerHTML = `
    <svg viewBox="0 0 24 24"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm0 14H6l-2 2V4h16v12z"/></svg>
    <span id="br-chat-badge"></span>
  `;
  document.body.appendChild(launcher);

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

  // ── Open/close ─────────────────────────────────────────────
  function openChat(){
    isOpen = true;
    win.classList.add('open');
    unread = 0;
    updateBadge();
    setTimeout(() => {
      const el = convId
        ? document.getElementById('br-chat-input')
        : document.getElementById('br-visitor-name');
      if(el) el.focus();
    }, 100);
  }
  function closeChat(){ isOpen = false; win.classList.remove('open'); }
  function updateBadge(){
    const badge = document.getElementById('br-chat-badge');
    if(unread > 0){ badge.style.display = 'flex'; badge.textContent = unread > 9 ? '9+' : unread; }
    else { badge.style.display = 'none'; }
  }

  launcher.addEventListener('click', () => isOpen ? closeChat() : openChat());
  document.getElementById('br-close-btn').addEventListener('click', closeChat);

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

  // ── Init ───────────────────────────────────────────────────
  loadSupabase((client) => {
    db = client;
    console.log('Billed Right chat widget ready');
  });

})();
