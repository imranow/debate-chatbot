const threadEl = document.getElementById("thread");
const formEl = document.getElementById("composer");
const questionEl = document.getElementById("question");
const askEl = document.getElementById("ask");
const topkEl = document.getElementById("topk");

let msgSeq = 0;

const EXAMPLE_QUESTIONS = [
  "What did candidates say about healthcare?",
  "How did candidates differ on immigration?",
  "What was said about climate change policy?",
  "How did candidates address income inequality?",
];

function clampInt(value, min, max, fallback) {
  const n = Number.parseInt(String(value || ""), 10);
  if (Number.isNaN(n)) return fallback;
  return Math.max(min, Math.min(max, n));
}

function el(tag, className) {
  const n = document.createElement(tag);
  if (className) n.className = className;
  return n;
}

function scrollThread() {
  threadEl.scrollTop = threadEl.scrollHeight;
}

function renderTyping() {
  const wrap = el("span", "typing");
  for (let i = 0; i < 3; i++) wrap.appendChild(el("span", "dot"));
  return wrap;
}

function renderInline(text) {
  const frag = document.createDocumentFragment();
  const re = /(\[\d+\])|(`[^`]+`)/g;
  let last = 0;
  let m;
  while ((m = re.exec(text)) !== null) {
    if (m.index > last) frag.appendChild(document.createTextNode(text.slice(last, m.index)));
    const tok = m[0];
    if (tok[0] === "[") {
      const n = tok.slice(1, -1);
      const btn = el("button", "cite-ref");
      btn.type = "button";
      btn.dataset.cite = n;
      btn.textContent = tok;
      frag.appendChild(btn);
    } else if (tok[0] === "`") {
      const code = el("code", "inline-code");
      code.textContent = tok.slice(1, -1);
      frag.appendChild(code);
    }
    last = m.index + tok.length;
  }
  if (last < text.length) frag.appendChild(document.createTextNode(text.slice(last)));
  return frag;
}

function renderMarkdownish(text) {
  const frag = document.createDocumentFragment();
  const lines = String(text || "").replace(/\r\n/g, "\n").split("\n");

  let i = 0;
  while (i < lines.length) {
    const line = lines[i] || "";

    // Code fences: ```lang ... ```
    if (line.trim().startsWith("```")) {
      const fence = line.trim();
      const lang = fence.slice(3).trim();
      i += 1;
      const codeLines = [];
      while (i < lines.length && !(lines[i] || "").trim().startsWith("```")) {
        codeLines.push(lines[i]);
        i += 1;
      }
      if (i < lines.length && (lines[i] || "").trim().startsWith("```")) i += 1;

      const pre = el("pre", "md-code");
      const code = el("code");
      code.textContent = codeLines.join("\n");
      pre.appendChild(code);
      if (lang) pre.dataset.lang = lang;
      frag.appendChild(pre);
      continue;
    }

    // Blank line: paragraph boundary.
    if (!line.trim()) {
      i += 1;
      continue;
    }

    // Headings: #, ##, ###
    const hm = line.match(/^(#{1,3})\s+(.*)$/);
    if (hm) {
      const level = hm[1].length;
      const tag = level === 1 ? "h3" : level === 2 ? "h4" : "h5";
      const h = el(tag, "md-head");
      h.appendChild(renderInline(hm[2]));
      frag.appendChild(h);
      i += 1;
      continue;
    }

    // Lists: - item
    if (/^\s*[-*]\s+/.test(line)) {
      const ul = el("ul", "md-list");
      while (i < lines.length && /^\s*[-*]\s+/.test(lines[i] || "")) {
        const item = (lines[i] || "").replace(/^\s*[-*]\s+/, "");
        const li = el("li");
        li.appendChild(renderInline(item));
        ul.appendChild(li);
        i += 1;
      }
      frag.appendChild(ul);
      continue;
    }

    // Paragraph: collect until blank line or another block construct.
    const paraLines = [line];
    i += 1;
    while (i < lines.length) {
      const l = lines[i] || "";
      if (!l.trim()) break;
      if (l.trim().startsWith("```")) break;
      if (/^\s*[-*]\s+/.test(l)) break;
      if (/^(#{1,3})\s+/.test(l)) break;
      paraLines.push(l);
      i += 1;
    }

    const p = el("p", "md-p");
    paraLines.forEach((pl, idx) => {
      p.appendChild(renderInline(pl));
      if (idx < paraLines.length - 1) p.appendChild(document.createElement("br"));
    });
    frag.appendChild(p);
  }

  return frag;
}

function isTruncated(text) {
  if (!text) return false;
  if (text.endsWith("\u2026")) return true;
  // Check if text ends mid-sentence (no sentence-ending punctuation)
  const trimmed = text.trimEnd();
  if (!trimmed) return false;
  const lastChar = trimmed[trimmed.length - 1];
  return !/[.!?"'\u201d\u2019]/.test(lastChar);
}

function normalizeScore(score, allScores) {
  if (!allScores || allScores.length === 0) return 0;
  const max = Math.max(...allScores);
  const min = Math.min(...allScores);
  if (max === min) return 100;
  return Math.round(((score - min) / (max - min)) * 100);
}

function addMessage({ role, text, citations, status, elapsed }) {
  const msgId = `m${++msgSeq}`;
  const msg = el("div", `msg ${role}`);
  msg.dataset.mid = msgId;
  const who = el("div", "who");
  const badge = el("div", `badge ${role === "assistant" ? "assistant" : ""}`);
  badge.textContent = role === "assistant" ? "BOT" : "YOU";
  who.appendChild(badge);

  const content = el("div", "content");
  const bubble = el("div", `bubble ${role}`);
  const body = el("div", `text ${role === "user" ? "raw" : "rich"}`);

  if (status === "typing") {
    body.appendChild(renderTyping());
  } else {
    body.appendChild(renderMarkdownish(text || ""));
  }
  bubble.appendChild(body);

  // Meta row: citations toggle for assistant messages.
  if (role === "assistant") {
    const meta = el("div", "meta");
    const left = el("div", "pill");
    const k = clampInt(topkEl.value, 1, 50, 8);
    left.innerHTML = `<strong>RAG</strong> top_k=${k}`;

    const toggle = el("button", "cite-toggle");
    toggle.type = "button";
    const citeCount = Array.isArray(citations) ? citations.length : 0;
    toggle.textContent = citeCount ? `Sources (${citeCount})` : "Sources (0)";

    const cites = el("div", "citations");
    if (Array.isArray(citations)) {
      const allScores = citations.map((c) => c.score).filter((s) => typeof s === "number");
      citations.forEach((c, idx) => {
        const cite = el("div", "cite");
        cite.dataset.cite = String(idx + 1);
        const head = el("div", "cite-head");
        const num = el("span", "cite-num");
        num.textContent = String(idx + 1);
        head.appendChild(num);

        // Relevance score badge
        if (typeof c.score === "number") {
          const scoreBadge = el("span", "cite-score");
          const pct = normalizeScore(c.score, allScores);
          scoreBadge.textContent = `${pct}%`;
          if (pct >= 80) scoreBadge.classList.add("high");
          else if (pct >= 50) scoreBadge.classList.add("mid");
          else scoreBadge.classList.add("low");
          head.appendChild(scoreBadge);
        }

        const parts = [];
        if (c.date) parts.push(c.date);
        if (c.debate_name) parts.push(c.debate_name);
        if (c.debate_section) parts.push(c.debate_section);
        if (c.speaker) parts.push(c.speaker);
        const metaText = el("span");
        metaText.textContent = parts.join(" | ");
        head.appendChild(metaText);

        const excerpt = el("div", "cite-excerpt");
        excerpt.textContent = c.text || "";

        // Truncation indicator
        if (isTruncated(c.text)) {
          const trunc = el("div", "cite-truncated");
          trunc.textContent = "Excerpt truncated";
          cite.appendChild(head);
          cite.appendChild(excerpt);
          cite.appendChild(trunc);
        } else {
          cite.appendChild(head);
          cite.appendChild(excerpt);
        }

        cites.appendChild(cite);
      });
    }

    toggle.addEventListener("click", () => {
      cites.classList.toggle("open");
    });

    bubble.addEventListener("click", (ev) => {
      const t = ev.target;
      if (!t || !(t instanceof HTMLElement)) return;
      if (!t.classList.contains("cite-ref")) return;
      const n = t.dataset.cite;
      if (!n) return;
      if (!cites.classList.contains("open")) cites.classList.add("open");
      const target = cites.querySelector(`.cite[data-cite="${n}"]`);
      if (target instanceof HTMLElement) {
        target.scrollIntoView({ behavior: "smooth", block: "nearest" });
        target.classList.remove("flash");
        // Force restart animation.
        void target.offsetWidth;
        target.classList.add("flash");
      }
    });

    if (elapsed) {
      const timePill = el("span", "elapsed-pill");
      timePill.textContent = `${elapsed}s`;
      left.appendChild(document.createTextNode(" "));
      left.appendChild(timePill);
    }

    meta.appendChild(left);
    meta.appendChild(toggle);
    bubble.appendChild(meta);
    bubble.appendChild(cites);
  }

  content.appendChild(bubble);
  if (role === "user") {
    msg.appendChild(content);
    msg.appendChild(who);
  } else {
    msg.appendChild(who);
    msg.appendChild(content);
  }
  threadEl.appendChild(msg);
  scrollThread();
  return { msg, body };
}

function renderStatusIndicator() {
  const wrap = el("div", "status-indicator");
  const text = el("span", "status-text");
  text.textContent = "Searching debate transcripts...";
  const timer = el("span", "status-timer");
  timer.textContent = "";
  wrap.appendChild(text);
  wrap.appendChild(timer);
  return { wrap, text, timer };
}

function setBusy(busy) {
  askEl.disabled = !!busy;
  questionEl.disabled = !!busy;
  topkEl.disabled = !!busy;
}

async function ask(question) {
  const top_k = clampInt(topkEl.value, 1, 50, 8);

  addMessage({ role: "user", text: question });
  const pending = addMessage({ role: "assistant", status: "typing", citations: [] });

  // Add status indicator below the typing dots
  const status = renderStatusIndicator();
  pending.body.appendChild(status.wrap);

  const startTime = performance.now();
  let timerInterval = setInterval(() => {
    const elapsed = ((performance.now() - startTime) / 1000).toFixed(1);
    status.timer.textContent = `${elapsed}s`;
  }, 100);

  setBusy(true);
  try {
    // Phase 1: searching
    status.text.textContent = "Searching debate transcripts\u2026";

    const resp = await fetch("/chat", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ question, top_k }),
    });

    // Phase 2: generating (response started coming back)
    status.text.textContent = "Generating answer\u2026";

    if (!resp.ok) {
      const err = await resp.text();
      throw new Error(err || `HTTP ${resp.status}`);
    }
    const data = await resp.json();

    clearInterval(timerInterval);
    const elapsed = ((performance.now() - startTime) / 1000).toFixed(1);

    // Re-render citations by replacing the assistant message element.
    pending.msg.remove();
    addMessage({
      role: "assistant",
      text: data.answer || "",
      citations: data.citations || [],
      elapsed: elapsed,
    });
  } catch (e) {
    clearInterval(timerInterval);
    pending.body.innerHTML = "";
    const errorText = el("span", "error-message");
    errorText.textContent = "Service temporarily unavailable. Please try again.";
    pending.body.appendChild(errorText);
  } finally {
    setBusy(false);
    questionEl.focus();
  }
}

formEl.addEventListener("submit", (ev) => {
  ev.preventDefault();
  const q = (questionEl.value || "").trim();
  if (!q) return;
  questionEl.value = "";
  ask(q);
});

questionEl.addEventListener("keydown", (ev) => {
  if (ev.key === "Enter" && !ev.shiftKey) {
    ev.preventDefault();
    formEl.requestSubmit();
  }
});

// Seed with welcome message and example questions.
addMessage({
  role: "assistant",
  text: "Ask a question about the 2019-2020 Democratic primary debates. I will answer using retrieved transcript sources.\n\nTry one of these to get started:",
  citations: [],
});

// Add clickable example questions
const examplesWrap = el("div", "example-questions");
EXAMPLE_QUESTIONS.forEach((q) => {
  const btn = el("button", "example-q");
  btn.type = "button";
  btn.textContent = q;
  btn.addEventListener("click", () => {
    questionEl.value = q;
    formEl.requestSubmit();
  });
  examplesWrap.appendChild(btn);
});
threadEl.lastElementChild.querySelector(".bubble").appendChild(examplesWrap);
