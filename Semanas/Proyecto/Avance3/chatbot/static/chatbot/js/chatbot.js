// Chatbot UI: consume the decision tree API and render options/buttons.

document.addEventListener('DOMContentLoaded', () => {
  const API_URL = '/chatbot/query'; // Django view que entrega los nodos

  const widget = document.getElementById('chatbot-widget');
  const toggle = document.getElementById('chatbot-toggle');
  const panel = document.getElementById('chatbot-panel');
  const closeBtn = document.getElementById('chatbot-close');
  const messagesEl = document.getElementById('chatbot-messages');
  const typing = document.getElementById('chatbot-typing');

  let currentOptions = {};
  let optionContainer = null;
  let currentNodeId = 'root';
  let bootstrapped = false;

  function getCsrfToken() {
    const match = document.cookie.match(/csrftoken=([^;]+)/);
    return match ? match[1] : '';
  }

  function openWidget() {
    widget.classList.add('open');
    panel.setAttribute('aria-hidden', 'false');
    widget.setAttribute('aria-hidden', 'false');
    ensureRootLoaded();
  }
  function closeWidget() {
    widget.classList.remove('open');
    panel.setAttribute('aria-hidden', 'true');
    widget.setAttribute('aria-hidden', 'true');
    toggle.focus();
  }

  toggle.addEventListener('click', () => {
    if (widget.classList.contains('open')) closeWidget(); else openWidget();
  });
  closeBtn.addEventListener('click', closeWidget);

  function ensureRootLoaded() {
    if (bootstrapped) return;
    bootstrapped = true;
    loadNode('root');
  }

  function scrollToBottom() {
    messagesEl.scrollTop = messagesEl.scrollHeight;
  }

  function clearOptionButtons() {
    if (optionContainer?.parentNode) optionContainer.parentNode.removeChild(optionContainer);
    optionContainer = null;
  }

  function appendMessage(text, cls) {
    const li = document.createElement('li');
    li.className = cls;
    li.textContent = text;
    messagesEl.appendChild(li);
    scrollToBottom();
  }

  function appendList(items) {
    const li = document.createElement('li');
    li.className = 'msg-bot';
    const ul = document.createElement('ul');
    ul.className = 'bot-list';
    items.forEach(item => {
      const it = document.createElement('li');
      if (typeof item === 'string') {
        it.textContent = item;
      } else {
        it.textContent = item.titulo || item.descripcion || JSON.stringify(item);
      }
      ul.appendChild(it);
    });
    li.appendChild(ul);
    messagesEl.appendChild(li);
    scrollToBottom();
  }

  function appendDocument(link) {
    const li = document.createElement('li');
    li.className = 'msg-bot';
    const anchor = document.createElement('a');
    anchor.href = link;
    anchor.target = '_blank';
    anchor.rel = 'noopener noreferrer';
    anchor.textContent = 'Abrir documento';
    li.appendChild(anchor);
    messagesEl.appendChild(li);
    scrollToBottom();
  }

  function renderOptions(options = {}) {
    currentOptions = options;
    clearOptionButtons();
    const keys = Object.keys(options || {});
    if (!keys.length) return;

    optionContainer = document.createElement('li');
    optionContainer.className = 'msg-options';
    const wrap = document.createElement('div');
    wrap.className = 'option-group';

    keys.forEach(key => {
      const opt = options[key] || {};
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'option-btn';
      btn.textContent = opt.text || key;
      btn.addEventListener('click', () => handleOptionSelection(key, opt));
      wrap.appendChild(btn);
    });

    optionContainer.appendChild(wrap);
    messagesEl.appendChild(optionContainer);
    scrollToBottom();
  }

  function handleOptionSelection(optionKey, optionData) {
    appendMessage(optionData.text || optionKey, 'msg-user');
    clearOptionButtons();
    const next = optionData.next_node || optionKey || 'root';
    loadNode(next);
  }

  async function loadNode(nodeId = 'root') {
    typing.hidden = false;
    try {
      const res = await fetch(API_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCsrfToken(),
        },
        body: JSON.stringify({ node: nodeId, from: currentNodeId }),
      });
      const data = await res.json();
      typing.hidden = true;

      if (!res.ok || data?.error) {
        appendMessage('Ocurrió un error al cargar la información. Intenta de nuevo.', 'msg-bot');
        renderOptions({ root: { text: 'Volver al inicio', next_node: 'root' } });
        return;
      }

      currentNodeId = data.node_id || nodeId;

      appendMessage(data.text || '', 'msg-bot');

      if ((data.type === 'list' || data.type === 'dynamic') && Array.isArray(data.items) && data.items.length) {
        appendList(data.items);
      }

      if (data.type === 'document' && data.document) {
        appendDocument(data.document);
      }

      renderOptions(data.options || {});
    } catch (err) {
      typing.hidden = true;
      appendMessage('No se pudo contactar al asistente en este momento.', 'msg-bot');
      renderOptions({ root: { text: 'Intentar nuevamente', next_node: 'root' } });
    }
  }

  // Close when clicking outside panel
  document.addEventListener('click', (e) => {
    if (!widget.contains(e.target) && widget.classList.contains('open')) {
      closeWidget();
    }
  });

  // Preload the first node so the main menu is ready immediately
  ensureRootLoaded();
});
