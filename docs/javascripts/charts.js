/*
 * Native chart picker for briefings:
 *
 *   <div class="chart-picker" data-icao="RPLL"></div>
 *
 * Chart lists come from docs/assets/data/charts.json, which tools/build_charts.py
 * reads from vatphil.com/charts at build time (that page has no CORS header, so
 * the browser can't read it directly). The PDFs open straight from vatphil.com
 * in a viewer overlay — or a new tab on phones, whose browsers can't show a PDF
 * inside a page.
 */
(function () {
  var script = document.currentScript;
  // site root, including any mike version prefix (/latest/…)
  var BASE = script ? script.src.replace(/javascripts\/charts\.js.*$/, "") : "/";
  var VIEW = "https://vatphil.com/viewchart.php?id=";
  var PAGE = "https://vatphil.com/charts?icao=";
  // vatphil.com category -> label, in the order pilots and controllers reach for them
  var CATS = [
    ["Airport Chart", "Aerodrome"],
    ["Departure Chart", "SID"],
    ["Arrival Chart", "STAR"],
    ["Approach Chart", "Approach"],
    ["Traffic Circuit Chart", "Circuit"],
    ["Area Chart", "General"]
  ];
  var MON = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
  var PHONE = window.matchMedia ? window.matchMedia("(max-width: 44.9375em), (hover: none) and (pointer: coarse)") : null;
  // phones, and browsers that say they can't show PDFs inline, get a new tab instead of the viewer
  function newTabOnly() { return (PHONE && PHONE.matches) || navigator.pdfViewerEnabled === false; }

  var dataP = null;
  function load() {
    if (!dataP) {
      dataP = fetch(BASE + "assets/data/charts.json").then(function (r) {
        if (!r.ok) throw new Error("charts.json " + r.status);
        return r.json();
      }).catch(function (e) { dataP = null; throw e; });   // retry on the next page
    }
    return dataP;
  }

  function esc(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }
  function pad(n) { return (n < 10 ? "0" : "") + n; }
  function fmt(iso) {
    var d = new Date(iso);
    return isNaN(d) ? "" : pad(d.getUTCDate()) + " " + MON[d.getUTCMonth()] + " " + pad(d.getUTCHours()) + ":" + pad(d.getUTCMinutes()) + "Z";
  }

  // [{key, label, items:[{id, name, key, label}]}] in CATS order; unknown categories last
  function groups(raw) {
    var byKey = {}, out = [];
    (raw || []).forEach(function (c) { byKey[c[0]] = c[1]; });
    var order = CATS.map(function (c) { return c[0]; });
    Object.keys(byKey).forEach(function (k) { if (order.indexOf(k) === -1) order.push(k); });
    order.forEach(function (k) {
      if (!byKey[k] || !byKey[k].length) return;
      var known = CATS.filter(function (c) { return c[0] === k; })[0];
      var label = known ? known[1] : k.replace(/ Chart$/, "");
      out.push({ key: k, label: label, items: byKey[k].map(function (it) {
        return { id: it[0], name: it[1], key: k, label: label };
      }) });
    });
    return out;
  }

  // ---- viewer overlay (one per page, created on first use) ----
  var modal = null, mList = [], mIdx = 0, mReturn = null;
  function buildModal() {
    modal = document.createElement("div");
    modal.className = "cp-modal";
    modal.setAttribute("role", "dialog");
    modal.setAttribute("aria-modal", "true");
    modal.setAttribute("aria-label", "Chart viewer");
    modal.innerHTML =
      '<div class="cp-mbar">' +
        '<span class="cp-mcat"></span><span class="cp-mtitle"></span>' +
        '<span class="cp-mnav"><button type="button" class="cp-prev" aria-label="Previous chart">‹</button>' +
          '<span class="cp-mpos"></span><button type="button" class="cp-next" aria-label="Next chart">›</button></span>' +
        '<a class="cp-mopen" target="_blank" rel="noopener">Open in new tab ↗</a>' +
        '<button type="button" class="cp-mclose" aria-label="Close chart">✕</button>' +
      '</div>' +
      // the hint sits behind the PDF: a working PDF viewer paints over it, a
      // browser that can't show PDFs inline leaves it visible
      '<div class="cp-mbody"><div class="cp-mhint"><span class="cp-mloading">Loading chart…</span>' +
        '<span class="cp-mfail">Chart not showing? This browser may not display PDFs inside a page — use “Open in new tab ↗” above.</span></div>' +
        '<iframe class="cp-mframe" title="Chart"></iframe></div>';
    modal.addEventListener("click", function (e) {
      if (e.target === modal) closeModal();
      else if (e.target.closest(".cp-mclose")) closeModal();
      else if (e.target.closest(".cp-prev")) step(-1);
      else if (e.target.closest(".cp-next")) step(1);
    });
    modal.querySelector(".cp-mframe").addEventListener("load", function () { modal.classList.remove("loading"); });
    document.body.appendChild(modal);
  }
  function show(i) {
    mIdx = (i + mList.length) % mList.length;
    var it = mList[mIdx];
    modal.querySelector(".cp-mcat").textContent = it.label;
    modal.querySelector(".cp-mtitle").textContent = it.name;
    modal.querySelector(".cp-mpos").textContent = (mIdx + 1) + " / " + mList.length;
    modal.querySelector(".cp-mnav").style.display = mList.length > 1 ? "" : "none";
    modal.querySelector(".cp-mopen").href = VIEW + it.id;
    modal.classList.add("loading");
    modal.querySelector(".cp-mframe").src = VIEW + it.id;
  }
  function step(d) { if (mList.length > 1) show(mIdx + d); }
  function openChart(list, i, from) {
    if (newTabOnly()) { window.open(VIEW + list[i].id, "_blank", "noopener"); return; }
    if (!modal) buildModal();
    mList = list; mReturn = from || null;
    show(i);
    modal.classList.add("open");
    document.documentElement.classList.add("cp-lock");
    modal.querySelector(".cp-mclose").focus();
  }
  function closeModal() {
    if (!modal || !modal.classList.contains("open")) return;
    modal.classList.remove("open");
    document.documentElement.classList.remove("cp-lock");
    modal.querySelector(".cp-mframe").removeAttribute("src");   // stop a big PDF still downloading
    if (mReturn && document.body.contains(mReturn)) mReturn.focus();
  }
  document.addEventListener("keydown", function (e) {
    if (!modal || !modal.classList.contains("open")) return;
    if (e.key === "Escape") { closeModal(); e.preventDefault(); }
    else if (e.key === "ArrowLeft") { step(-1); e.preventDefault(); }
    else if (e.key === "ArrowRight") { step(1); e.preventDefault(); }
  });
  // a plain click opens the viewer; ctrl/cmd/shift/middle-click keep their usual new-tab meaning
  function plainClick(e) { return e.button === 0 && !e.ctrlKey && !e.metaKey && !e.shiftKey && !e.altKey; }

  // ---- picker ----
  function renderPicker(el, gs, data) {
    var icao = el.getAttribute("data-icao");
    var st = { k: "", q: "" }, visible = [];
    var total = gs.reduce(function (n, g) { return n + g.items.length; }, 0);
    el.innerHTML =
      '<div class="cp">' +
        '<div class="cp-bar">' +
          '<div class="cp-chips" role="group" aria-label="Chart category">' +
            '<button type="button" class="cp-chip on" data-k="">All <span>' + total + '</span></button>' +
            gs.map(function (g) {
              return '<button type="button" class="cp-chip" data-k="' + esc(g.key) + '">' + esc(g.label) + ' <span>' + g.items.length + '</span></button>';
            }).join("") +
          '</div>' +
          '<input class="cp-filter" type="search" placeholder="Filter, e.g. RWY 24 or BETEL" aria-label="Filter ' + esc(icao) + ' charts" autocomplete="off">' +
        '</div>' +
        '<div class="cp-groups"></div>' +
        '<div class="cp-foot">Charts from <a href="' + PAGE + esc(icao) + '" target="_blank" rel="noopener">vatphil.com/charts ↗</a>' +
          (data.generated ? ' · list updated ' + fmt(data.generated) : '') + '</div>' +
      '</div>';
    var box = el.querySelector(".cp-groups");

    function draw() {
      var words = st.q.toLowerCase().split(/\s+/).filter(Boolean);
      visible = [];
      var shown = 0;
      var html = gs.filter(function (g) { return !st.k || g.key === st.k; }).map(function (g) {
        var items = g.items.filter(function (it) {
          var hay = (it.name + " " + g.label).toLowerCase().replace(/\s+/g, " ");
          var squashed = hay.replace(/\s/g, "");       // "RWY06" matches "RWY 06" and vice versa
          return words.every(function (w) { return hay.indexOf(w) !== -1 || squashed.indexOf(w) !== -1; });
        });
        if (!items.length) return "";
        shown++;
        return '<div class="cp-group"><div class="cp-gh">' + esc(g.label) + ' <span>' + items.length + '</span></div>' +
          items.map(function (it) {
            visible.push(it);
            return '<a class="cp-item" href="' + VIEW + it.id + '" target="_blank" rel="noopener" data-i="' + (visible.length - 1) + '">' + esc(it.name) + '</a>';
          }).join("") + '</div>';
      }).join("");
      box.innerHTML = html || '<div class="cp-empty">No charts match “' + esc(st.q) + '”.</div>';
      box.classList.toggle("single", shown === 1);   // one group: let it use the full width
    }
    function setCat(k) {
      st.k = k;
      el.querySelectorAll(".cp-chip").forEach(function (c) { c.classList.toggle("on", c.getAttribute("data-k") === k); });
      draw();
    }

    el.querySelector(".cp-chips").addEventListener("click", function (e) {
      var c = e.target.closest(".cp-chip");
      if (c) setCat(c.getAttribute("data-k"));
    });
    el.querySelector(".cp-filter").addEventListener("input", function (e) { st.q = e.target.value.trim(); draw(); });
    box.addEventListener("click", function (e) {
      var a = e.target.closest(".cp-item");
      if (!a || !plainClick(e) || newTabOnly()) return;   // let the link open the PDF in a new tab
      e.preventDefault();
      openChart(visible.slice(), +a.getAttribute("data-i"), a);
    });
    draw();
  }

  function init() {
    closeModal();                                 // instant navigation: don't carry a viewer across pages
    var els = document.querySelectorAll(".chart-picker[data-icao]");
    if (!els.length) return;
    load().then(function (data) {
      els.forEach(function (el) {
        if (el._cpDone || !document.body.contains(el)) return;
        el._cpDone = true;
        var icao = el.getAttribute("data-icao").toUpperCase();
        var gs = groups((data.airports || {})[icao]);
        var fallback = '<a href="' + PAGE + esc(icao) + '" target="_blank" rel="noopener">' + esc(icao) + ' charts on vatphil.com ↗</a>';
        if (!gs.length) { el.innerHTML = '<div class="cp-empty">No chart list available here yet — ' + fallback + '</div>'; return; }
        renderPicker(el, gs, data);
      });
    }).catch(function () {
      els.forEach(function (el) {
        var icao = esc(el.getAttribute("data-icao"));
        el.innerHTML = '<div class="cp-empty">Couldn\'t load the chart list — <a href="' + PAGE + icao + '" target="_blank" rel="noopener">' + icao + ' charts on vatphil.com ↗</a></div>';
      });
    });
  }

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(init);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
