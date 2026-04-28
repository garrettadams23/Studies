
// ─────────────────────────────────────────────────────────────────────────────
// 7. URL ENCODER / DECODER TOOL
// Powers the interactive codec widget in the URL Encoding topic.
// Wraps native encodeURIComponent / decodeURIComponent with error handling.
// ─────────────────────────────────────────────────────────────────────────────

/** Get input textarea value, trimmed. */
function _urlInput()  { return (document.getElementById("url-codec-input")  || {}).value || ""; }
/** Set output textarea value. */
function _urlOutput(v){ var el = document.getElementById("url-codec-output"); if(el) el.value = v; }
/** Show a brief status message. */
function _urlMsg(txt, color) {
  var el = document.getElementById("url-codec-msg");
  if(!el) return;
  el.textContent = txt;
  el.style.color = color || "var(--muted)";
  clearTimeout(el._t);
  el._t = setTimeout(function(){ el.textContent = ""; }, 2500);
}

/** Percent-encode the input using encodeURIComponent. */
function urlToolEncode() {
  var raw = _urlInput();
  if(!raw) { _urlMsg("⚠ Nothing to encode.", "var(--amber)"); return; }
  try {
    _urlOutput(encodeURIComponent(raw));
    _urlMsg("✓ Encoded.", "var(--green)");
  } catch(e) {
    _urlMsg("✗ Encode error: " + e.message, "var(--red)");
  }
}

/** Decode percent-encoded input using decodeURIComponent. */
function urlToolDecode() {
  var raw = _urlInput();
  if(!raw) { _urlMsg("⚠ Nothing to decode.", "var(--amber)"); return; }
  try {
    _urlOutput(decodeURIComponent(raw));
    _urlMsg("✓ Decoded.", "var(--cyan)");
  } catch(e) {
    // Fallback: try replacing + with space first (form-encoded input)
    try {
      _urlOutput(decodeURIComponent(raw.replace(/\+/g, " ")));
      _urlMsg("✓ Decoded (form-encoded +→space).", "var(--cyan)");
    } catch(e2) {
      _urlMsg("✗ Malformed encoding: " + e2.message, "var(--red)");
    }
  }
}

/** Copy output to clipboard. */
function urlToolCopy() {
  var el = document.getElementById("url-codec-output");
  if(!el || !el.value) { _urlMsg("⚠ Nothing to copy.", "var(--amber)"); return; }
  navigator.clipboard.writeText(el.value)
    .then(function(){ _urlMsg("✓ Copied to clipboard.", "var(--green)"); })
    .catch(function(){
      // Fallback for older browsers
      el.select();
      document.execCommand("copy");
      _urlMsg("✓ Copied (fallback).", "var(--green)");
    });
}

/** Clear both textareas and message. */
function urlToolClear() {
  var i = document.getElementById("url-codec-input");
  var o = document.getElementById("url-codec-output");
  if(i) i.value = "";
  if(o) o.value = "";
  _urlMsg("");
}
