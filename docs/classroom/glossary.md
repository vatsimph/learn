# Glossary

Aviation and air-traffic-control abbreviations you will meet across these briefings, on charts, and in NOTAMs. The base list follows **ICAO Doc 8400** (the official abbreviation set), with a few VATSIM and flow-management terms added.

Start typing an abbreviation or a word from its meaning to filter the list.

<div class="gl-wrap">
  <input id="gl-search" class="gl-search" type="search" placeholder="Search, e.g. RVSM, threshold, QNH…" aria-label="Search the glossary" autocomplete="off">
  <div id="gl-count" class="gl-count"></div>
  <div id="gl-list" class="gl-list"><div class="gl-loading">Loading glossary…</div></div>
</div>

<style>
.gl-wrap { margin: 1rem 0 1.5rem; }
.gl-search {
  width: 100%; max-width: 460px; box-sizing: border-box; font: inherit; font-size: 0.9rem;
  padding: 10px 13px; border-radius: 8px; border: 1px solid var(--md-default-fg-color--lightest);
  background: var(--md-code-bg-color); color: var(--md-default-fg-color);
}
.gl-search:focus { outline: none; border-color: #8c7804; }
.gl-count { font-size: 0.72rem; color: var(--md-default-fg-color--light); margin: 0.4rem 0 0.2rem; letter-spacing: 0.03em; }
.gl-group { margin-top: 0.6rem; }
.gl-letter {
  font-size: 0.72rem; font-weight: 800; letter-spacing: 0.08em; color: #8c7804;
  border-bottom: 1px solid var(--md-default-fg-color--lightest); padding: 0.3rem 0 0.2rem; margin-bottom: 0.2rem;
}
.gl-row { display: grid; grid-template-columns: 7.5rem 1fr; gap: 0.5rem 1rem; padding: 0.3rem 0.2rem; align-items: baseline; }
.gl-row:nth-child(even) { background: var(--md-code-bg-color); border-radius: 5px; }
.gl-term { font-weight: 700; font-size: 0.82rem; font-family: var(--md-code-font, monospace); color: var(--md-default-fg-color); }
.gl-def { font-size: 0.82rem; color: var(--md-default-fg-color); line-height: 1.5; }
.gl-loading, .gl-empty { font-size: 0.82rem; color: var(--md-default-fg-color--light); font-style: italic; padding: 0.7rem 0; }
@media (max-width: 30em) {
  .gl-row { grid-template-columns: 5.5rem 1fr; }
}
</style>

<script>
(function () {
  var listEl   = document.getElementById("gl-list");
  var countEl  = document.getElementById("gl-count");
  var searchEl = document.getElementById("gl-search");
  if (!listEl) return;

  // page is served at /classroom/glossary/ -> two levels up to the site root
  var URL_JSON = "../../assets/data/glossary.json";
  var terms = [];

  function esc(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }

  function render(filter) {
    var q  = (filter || "").trim().toLowerCase();
    var qs = q.replace(/\s+/g, "");
    var shown = 0, html = "", letter = "";
    terms.forEach(function (t) {
      var ab = t[0], def = t[1];
      if (q) {
        var hay = (ab + " " + def).toLowerCase();
        if (hay.indexOf(q) === -1 && hay.replace(/\s+/g, "").indexOf(qs) === -1) return;
      }
      var first = ab[0].toUpperCase();
      if (!/[A-Z]/.test(first)) first = "#";
      if (first !== letter) {
        if (letter) html += "</div>";
        letter = first;
        html += '<div class="gl-group"><div class="gl-letter">' + letter + '</div>';
      }
      html += '<div class="gl-row"><span class="gl-term">' + esc(ab) + '</span><span class="gl-def">' + esc(def) + '</span></div>';
      shown++;
    });
    if (letter) html += "</div>";
    listEl.innerHTML = shown ? html : '<div class="gl-empty">No entry matches “' + esc(q) + '”.</div>';
    countEl.textContent = q ? (shown + " of " + terms.length + " terms") : (terms.length + " terms");
  }

  fetch(URL_JSON)
    .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(function (data) {
      terms = (data.terms || []).slice().sort(function (a, b) { return a[0].toUpperCase().localeCompare(b[0].toUpperCase()); });
      render("");
      searchEl.addEventListener("input", function () { render(searchEl.value); });
    })
    .catch(function () {
      listEl.innerHTML = '<div class="gl-empty">Couldn’t load the glossary. Please try again later.</div>';
    });
})();
</script>

*[ICAO]: International Civil Aviation Organization
*[NOTAM]: Notice to Airmen
*[VATSIM]: Virtual Air Traffic Simulation Network
