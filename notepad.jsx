
// ── CSS vars matching garrettstudies site ────────────────────────────────────
const css = `
  @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Outfit:wght@300;400;500;600&display=swap');

  * { box-sizing: border-box; margin: 0; padding: 0; }

  :root {
    --bg:      #07090f;
    --bg2:     #0d1117;
    --bg3:     #111620;
    --border:  #1e2535;
    --text:    #c9d1d9;
    --muted:   #556070;
    --cyan:    #00d4ff;
    --green:   #00ff99;
    --amber:   #ffb020;
    --red:     #ff4d6d;
    --purple:  #a855f7;
    --mono:    'Share Tech Mono', monospace;
    --sans:    'Outfit', sans-serif;
  }

  body { background: var(--bg); color: var(--text); font-family: var(--sans); }

  .wrap {
    max-width: 860px; margin: 0 auto; padding: 32px 20px 60px;
    min-height: 100vh;
  }

  /* Header */
  .hdr {
    display: flex; align-items: center; gap: 14px;
    margin-bottom: 28px; padding-bottom: 18px;
    border-bottom: 1px solid var(--border);
  }
  .hdr-icon { font-size: 26px; }
  .hdr-title {
    font-family: var(--mono); font-size: 15px; color: var(--cyan);
    letter-spacing: 2px; text-transform: uppercase;
  }
  .hdr-sub { font-size: 12px; color: var(--muted); margin-top: 2px; }
  .hdr-live {
    margin-left: auto; display: flex; align-items: center; gap: 6px;
    font-family: var(--mono); font-size: 10px; color: var(--green);
    letter-spacing: 1px;
  }
  .live-dot {
    width: 7px; height: 7px; border-radius: 50%;
    background: var(--green);
    animation: pulse 2s infinite;
  }
  @keyframes pulse {
    0%,100% { opacity: 1; transform: scale(1); }
    50%      { opacity: 0.4; transform: scale(0.8); }
  }

  /* Compose box */
  .compose {
    background: var(--bg2); border: 1px solid var(--border);
    border-radius: 6px; padding: 16px; margin-bottom: 24px;
    transition: border-color 0.2s;
  }
  .compose:focus-within { border-color: var(--cyan); }

  .compose-top {
    display: flex; gap: 10px; margin-bottom: 10px; align-items: center;
  }
  .name-input {
    background: var(--bg3); border: 1px solid var(--border);
    border-radius: 4px; padding: 6px 10px;
    font-family: var(--mono); font-size: 12px; color: var(--cyan);
    width: 160px; outline: none; transition: border-color 0.2s;
  }
  .name-input:focus { border-color: var(--cyan); }
  .name-input::placeholder { color: var(--muted); }

  .char-count {
    font-family: var(--mono); font-size: 10px; color: var(--muted);
    margin-left: auto;
  }
  .char-count.warn { color: var(--amber); }
  .char-count.over { color: var(--red); }

  .note-input {
    width: 100%; background: transparent; border: none; outline: none;
    font-family: var(--sans); font-size: 14px; color: var(--text);
    resize: none; line-height: 1.6; min-height: 80px;
  }
  .note-input::placeholder { color: var(--muted); }

  .compose-footer {
    display: flex; align-items: center; justify-content: space-between;
    margin-top: 12px; padding-top: 10px; border-top: 1px solid var(--border);
  }
  .compose-hint { font-size: 11px; color: var(--muted); }
  .compose-hint kbd {
    background: var(--bg3); border: 1px solid var(--border);
    border-radius: 3px; padding: 1px 5px;
    font-family: var(--mono); font-size: 10px; color: var(--text);
  }

  .post-btn {
    background: transparent; border: 1px solid var(--cyan);
    color: var(--cyan); font-family: var(--mono); font-size: 11px;
    letter-spacing: 1px; padding: 7px 18px; border-radius: 3px;
    cursor: pointer; transition: all 0.2s;
  }
  .post-btn:hover:not(:disabled) { background: rgba(0,212,255,0.1); }
  .post-btn:disabled { opacity: 0.35; cursor: not-allowed; }

  /* Filter / sort bar */
  .toolbar {
    display: flex; align-items: center; gap: 10px;
    margin-bottom: 16px; flex-wrap: wrap;
  }
  .note-count {
    font-family: var(--mono); font-size: 11px; color: var(--muted);
    margin-right: auto;
  }
  .sort-btn {
    background: transparent; border: 1px solid var(--border);
    color: var(--muted); font-family: var(--mono); font-size: 10px;
    letter-spacing: 1px; padding: 4px 12px; border-radius: 2px;
    cursor: pointer; transition: all 0.15s;
  }
  .sort-btn.active { border-color: var(--amber); color: var(--amber); }
  .sort-btn:hover:not(.active) { border-color: var(--text); color: var(--text); }

  .search-box {
    background: var(--bg2); border: 1px solid var(--border);
    border-radius: 3px; padding: 4px 10px;
    font-family: var(--mono); font-size: 11px; color: var(--text);
    outline: none; width: 160px; transition: border-color 0.2s;
  }
  .search-box:focus { border-color: var(--cyan); }
  .search-box::placeholder { color: var(--muted); }

  /* Notes list */
  .notes-list { display: flex; flex-direction: column; gap: 10px; }

  .note-card {
    background: var(--bg2); border: 1px solid var(--border);
    border-radius: 6px; padding: 14px 16px;
    border-left: 3px solid transparent;
    animation: fadeIn 0.25s ease;
    position: relative;
  }
  .note-card.own { border-left-color: var(--cyan); }
  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(-6px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  .note-meta {
    display: flex; align-items: center; gap: 10px;
    margin-bottom: 8px;
  }
  .note-author {
    font-family: var(--mono); font-size: 11px; color: var(--cyan);
    font-weight: 600;
  }
  .note-time {
    font-family: var(--mono); font-size: 10px; color: var(--muted);
  }
  .note-own-badge {
    font-family: var(--mono); font-size: 9px; color: var(--green);
    border: 1px solid rgba(0,255,153,0.3); padding: 1px 6px;
    border-radius: 2px; letter-spacing: 1px;
  }
  .note-del {
    margin-left: auto; background: transparent; border: none;
    color: var(--muted); font-size: 13px; cursor: pointer;
    opacity: 0; transition: opacity 0.15s, color 0.15s;
    padding: 2px 4px;
  }
  .note-card:hover .note-del { opacity: 1; }
  .note-del:hover { color: var(--red); }

  .note-body {
    font-size: 14px; line-height: 1.65; color: var(--text);
    white-space: pre-wrap; word-break: break-word;
  }

  /* Empty / loading states */
  .empty {
    text-align: center; padding: 60px 20px;
    font-family: var(--mono); font-size: 12px; color: var(--muted);
    letter-spacing: 1px;
  }
  .empty-icon { font-size: 32px; margin-bottom: 12px; }

  .loading-bar {
    height: 2px; background: var(--border); border-radius: 1px;
    margin-bottom: 24px; overflow: hidden;
  }
  .loading-fill {
    height: 100%; width: 40%; background: var(--cyan);
    border-radius: 1px;
    animation: loading 1.2s ease-in-out infinite;
  }
  @keyframes loading {
    0%   { transform: translateX(-100%); }
    100% { transform: translateX(350%); }
  }

  /* Toast */
  .toast {
    position: fixed; bottom: 24px; left: 50%; transform: translateX(-50%);
    background: var(--bg2); border: 1px solid var(--border);
    font-family: var(--mono); font-size: 11px; color: var(--text);
    padding: 8px 18px; border-radius: 4px; letter-spacing: 1px;
    pointer-events: none; transition: opacity 0.3s;
    box-shadow: 0 4px 20px rgba(0,0,0,0.5);
  }
  .toast.show { opacity: 1; }
  .toast.hide { opacity: 0; }

  @media (max-width: 600px) {
    .wrap { padding: 20px 14px 40px; }
    .compose-top { flex-wrap: wrap; }
    .name-input { width: 100%; }
  }
`;

// ── Helpers ──────────────────────────────────────────────────────────────────
const MAX_CHARS = 500;
const STORAGE_KEY = "shared-notepad-notes";
const SESSION_KEY = "notepad-session-id";

function getSessionId() {
  let id = sessionStorage.getItem(SESSION_KEY);
  if (!id) {
    id = Math.random().toString(36).slice(2, 10);
    sessionStorage.setItem(SESSION_KEY, id);
  }
  return id;
}

function relativeTime(ts) {
  const diff = Math.floor((Date.now() - ts) / 1000);
  if (diff < 5)  return "just now";
  if (diff < 60) return `${diff}s ago`;
  if (diff < 3600) return `${Math.floor(diff/60)}m ago`;
  if (diff < 86400) return `${Math.floor(diff/3600)}h ago`;
  return new Date(ts).toLocaleDateString();
}

// ── Component ────────────────────────────────────────────────────────────────
function SharedNotepad() {
  const sessionId = getSessionId();

  const [notes,     setNotes]     = useState([]);
  const [loading,   setLoading]   = useState(true);
  const [author,    setAuthor]    = useState(() => localStorage.getItem("notepad-author") || "");
  const [body,      setBody]      = useState("");
  const [posting,   setPosting]   = useState(false);
  const [sort,      setSort]      = useState("newest");
  const [filter,    setFilter]    = useState("");
  const [toast,     setToast]     = useState({ msg: "", show: false });
  const [tick,      setTick]      = useState(0);       // forces relativeTime refresh
  const pollRef = useRef(null);

  // ── Storage helpers ──────────────────────────────────────────────────────
  async function loadNotes() {
    try {
      const res = await window.storage.get(STORAGE_KEY, true);
      setNotes(res ? JSON.parse(res.value) : []);
    } catch { setNotes([]); }
    setLoading(false);
  }

  async function saveNotes(updated) {
    try {
      await window.storage.set(STORAGE_KEY, JSON.stringify(updated), true);
    } catch (e) { console.error("Storage write failed", e); }
  }

  // ── Poll every 8s for new notes from others ──────────────────────────────
  useEffect(() => {
    loadNotes();
    pollRef.current = setInterval(loadNotes, 8000);
    const tickTimer = setInterval(() => setTick(t => t + 1), 30000);
    return () => { clearInterval(pollRef.current); clearInterval(tickTimer); };
  }, []);

  // ── Persist author name ──────────────────────────────────────────────────
  useEffect(() => {
    if (author) localStorage.setItem("notepad-author", author);
  }, [author]);

  // ── Toast helper ─────────────────────────────────────────────────────────
  function showToast(msg) {
    setToast({ msg, show: true });
    setTimeout(() => setToast(t => ({ ...t, show: false })), 2200);
  }

  // ── Post note ────────────────────────────────────────────────────────────
  async function postNote() {
    const trimBody   = body.trim();
    const trimAuthor = author.trim() || "Anonymous";
    if (!trimBody || trimBody.length > MAX_CHARS) return;

    setPosting(true);
    const newNote = {
      id:        Math.random().toString(36).slice(2),
      author:    trimAuthor,
      body:      trimBody,
      ts:        Date.now(),
      sessionId,
    };
    // Reload fresh before writing to avoid overwriting concurrent posts
    let latest = [];
    try {
      const res = await window.storage.get(STORAGE_KEY, true);
      latest = res ? JSON.parse(res.value) : [];
    } catch { latest = [...notes]; }

    const updated = [newNote, ...latest];
    await saveNotes(updated);
    setNotes(updated);
    setBody("");
    setPosting(false);
    showToast("✓ note posted");
  }

  // ── Delete note ──────────────────────────────────────────────────────────
  async function deleteNote(id) {
    const updated = notes.filter(n => n.id !== id);
    await saveNotes(updated);
    setNotes(updated);
    showToast("note removed");
  }

  // ── Keyboard shortcut: Ctrl+Enter / Cmd+Enter to post ────────────────────
  function onKeyDown(e) {
    if ((e.ctrlKey || e.metaKey) && e.key === "Enter") postNote();
  }

  // ── Derive display list ──────────────────────────────────────────────────
  const displayed = notes
    .filter(n => {
      if (!filter) return true;
      const q = filter.toLowerCase();
      return n.body.toLowerCase().includes(q) || n.author.toLowerCase().includes(q);
    })
    .sort((a, b) => sort === "newest" ? b.ts - a.ts : a.ts - b.ts);

  const chars = body.length;
  const charClass = chars > MAX_CHARS ? "over" : chars > MAX_CHARS * 0.85 ? "warn" : "";
  const canPost = body.trim().length > 0 && chars <= MAX_CHARS && !posting;

  return (
    <>
      <style>{css}</style>
      <div className="wrap">

        {/* Header */}
        <div className="hdr">
          <span className="hdr-icon">📋</span>
          <div>
            <div className="hdr-title">Shared Notepad</div>
            <div className="hdr-sub">Notes are public — visible to all visitors</div>
          </div>
          <div className="hdr-live">
            <span className="live-dot" />
            LIVE
          </div>
        </div>

        {/* Loading bar */}
        {loading && (
          <div className="loading-bar"><div className="loading-fill" /></div>
        )}

        {/* Compose */}
        <div className="compose">
          <div className="compose-top">
            <input
              className="name-input"
              placeholder="Your name (optional)"
              value={author}
              onChange={e => setAuthor(e.target.value.slice(0, 30))}
              maxLength={30}
            />
            <span className={`char-count ${charClass}`}>
              {chars}/{MAX_CHARS}
            </span>
          </div>

          <textarea
            className="note-input"
            placeholder="Leave a note for anyone visiting…"
            value={body}
            onChange={e => setBody(e.target.value)}
            onKeyDown={onKeyDown}
            rows={3}
          />

          <div className="compose-footer">
            <span className="compose-hint">
              <kbd>Ctrl</kbd>+<kbd>Enter</kbd> to post
            </span>
            <button className="post-btn" onClick={postNote} disabled={!canPost}>
              POST NOTE ▶
            </button>
          </div>
        </div>

        {/* Toolbar */}
        {!loading && (
          <div className="toolbar">
            <span className="note-count">{notes.length} note{notes.length !== 1 ? "s" : ""}</span>
            <input
              className="search-box"
              placeholder="⌕ filter notes…"
              value={filter}
              onChange={e => setFilter(e.target.value)}
            />
            <button className={`sort-btn ${sort === "newest" ? "active" : ""}`} onClick={() => setSort("newest")}>NEWEST</button>
            <button className={`sort-btn ${sort === "oldest" ? "active" : ""}`} onClick={() => setSort("oldest")}>OLDEST</button>
          </div>
        )}

        {/* Notes */}
        {!loading && (
          displayed.length === 0 ? (
            <div className="empty">
              <div className="empty-icon">{filter ? "🔍" : "📝"}</div>
              {filter ? "No notes match that filter." : "No notes yet — be the first to leave one."}
            </div>
          ) : (
            <div className="notes-list">
              {displayed.map(n => (
                <div key={n.id} className={`note-card ${n.sessionId === sessionId ? "own" : ""}`}>
                  <div className="note-meta">
                    <span className="note-author">
                      {n.author || "Anonymous"}
                    </span>
                    <span className="note-time">{relativeTime(n.ts)}</span>
                    {n.sessionId === sessionId && (
                      <span className="note-own-badge">YOU</span>
                    )}
                    {n.sessionId === sessionId && (
                      <button className="note-del" onClick={() => deleteNote(n.id)} title="Delete">✕</button>
                    )}
                  </div>
                  <div className="note-body">{n.body}</div>
                </div>
              ))}
            </div>
          )
        )}

        {/* Toast */}
        <div className={`toast ${toast.show ? "show" : "hide"}`}>{toast.msg}</div>

      </div>
    </>
  );
}
// Mount bridge for Babel standalone loader
window.__mountNotepad = function() {
  const root = ReactDOM.createRoot(document.getElementById('notepad-root'));
  root.render(React.createElement(SharedNotepad));
};
// Auto-mount if panel already open
window.__mountNotepad();
