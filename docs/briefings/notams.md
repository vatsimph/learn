---
hide:
  - toc
---

# NOTAMs

Current Philippine (RPHI) NOTAMs from the CAAP AIS. Use the filters or click an aerodrome on the map. Hover (or tap) a dotted abbreviation for its meaning, and link straight to an aerodrome or NOTAM with `#RPLL` or `#B5069/26` on the end of this page's address.

<div id="nt-root">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css" />
<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js"></script>

<style>
#nt-root { --nt-gold:#8c7804; --nt-active:#00c774; --nt-soon:#ff9d3c; --nt-exp:#ff5a5a; }

#nt-bar { display:flex; flex-wrap:wrap; gap:10px; align-items:center; margin:1rem 0 0.6rem; }
#nt-search {
  flex:1 1 220px; min-width:180px; background:var(--md-code-bg-color); color:var(--md-default-fg-color);
  border:1px solid var(--md-default-fg-color--lightest); border-radius:8px; padding:9px 12px; font-size:0.82rem; font-family:inherit;
}
#nt-search:focus { outline:none; border-color:var(--nt-gold); }
#nt-ap, #nt-cat {
  max-width:min(100%, 300px);   /* airport names make the widest option long */
  background:var(--md-code-bg-color); color:var(--md-default-fg-color);
  border:1px solid var(--md-default-fg-color--lightest); border-radius:8px; padding:9px 10px; font-size:0.8rem; font-family:inherit;
}
#nt-seg { display:inline-flex; border:1px solid var(--md-default-fg-color--lightest); border-radius:8px; overflow:hidden; }
#nt-seg button {
  background:transparent; color:var(--md-default-fg-color--light); border:0; border-right:1px solid var(--md-default-fg-color--lightest);
  padding:9px 13px; font-size:0.75rem; font-weight:600; cursor:pointer; font-family:inherit; letter-spacing:.02em;
}
#nt-seg button:last-child { border-right:0; }
#nt-seg button.on { background:var(--nt-gold); color:#1a1a1a; }
#nt-seg button[data-s="active"].on   { background:var(--nt-active); }
#nt-seg button[data-s="upcoming"].on { background:var(--nt-soon); }
#nt-seg button[data-s="expired"].on  { background:var(--nt-exp); }
#nt-seg button:not(.on):hover { background:var(--md-default-fg-color--lightest); }

#nt-meta { display:flex; flex-wrap:wrap; gap:6px 14px; align-items:center; font-size:0.72rem; color:var(--md-default-fg-color--light); margin-bottom:0.6rem; }
#nt-meta .nt-updated { font-family:var(--md-code-font,monospace); }
#nt-meta .nt-updated.stale { color:var(--nt-soon); }
.nt-note { margin-top:0.45rem; font-size:0.72rem; color:var(--nt-soon); }
#nt-root .nt-pop .nt-note { margin:0 0 7px; font-size:0.7rem; color:#ffb870; }
#nt-reset { color:var(--nt-gold); cursor:pointer; font-weight:600; display:none; }
#nt-reset.show { display:inline; }
#nt-areas-l, #nt-now-l { display:inline-flex; align-items:center; gap:5px; font-size:0.76rem; color:var(--md-default-fg-color--light); cursor:pointer; user-select:none; white-space:nowrap; }
.nt-icao { cursor:pointer; }
#nt-areas-l input[type=checkbox], #nt-now-l input[type=checkbox] { accent-color:var(--nt-gold); cursor:pointer; }
.nt-now { font-size:0.62rem; font-weight:800; letter-spacing:.04em; padding:2px 7px; border-radius:999px; font-family:var(--md-code-font,monospace); white-space:nowrap; }
.nt-now.on  { background:rgba(0,199,116,.16); color:var(--nt-active); }
.nt-now.off { background:var(--md-default-fg-color--lightest); color:var(--md-default-fg-color--light); }
.nt-sched .nt-sched-st { color:var(--md-default-fg-color--light); }
.nt-note.info { color:var(--md-default-fg-color--light); }
#nt-root .nt-pop .nt-note.info { color:#9aa4b2; }
.nt-body abbr, .nt-pop-b abbr { text-decoration:underline dotted; text-decoration-color:rgba(140,120,4,.7); text-underline-offset:2px; cursor:help; }
#nt-tip {
  position:fixed; z-index:1000; max-width:280px; padding:5px 9px; border-radius:6px; pointer-events:none;
  background:#12151c; color:#e8ecf2; border:1px solid rgba(140,120,4,.5); box-shadow:0 4px 14px rgba(0,0,0,.45);
  font:600 0.72rem/1.35 var(--md-text-font,sans-serif); opacity:0; visibility:hidden; transition:opacity .08s;
}
#nt-tip.show { opacity:1; visibility:visible; }
#nt-tip b { font-family:var(--md-code-font,monospace); color:#e6c34a; margin-right:6px; }
.nt-actions { display:flex; flex-wrap:wrap; gap:8px; align-items:center; }
.nt-linkbtn {
  margin-top:0.6rem; background:transparent; color:var(--md-default-fg-color--light); border:1px solid var(--md-default-fg-color--lightest);
  font-weight:600; font-size:0.72rem; padding:6px 13px; border-radius:999px; cursor:pointer; font-family:inherit;
}
.nt-linkbtn:hover { border-color:var(--nt-gold); color:var(--md-default-fg-color); }
@keyframes nt-flash { from { box-shadow:0 0 0 3px rgba(140,120,4,.7); } to { box-shadow:0 0 0 3px rgba(140,120,4,0); } }
.nt-card.flash { animation:nt-flash 2.4s ease-out; }
.nt-num { cursor:default; }
#nt-alt-f { display:inline-flex; align-items:center; gap:7px; font-size:0.76rem; color:var(--md-default-fg-color--light); border:1px solid var(--md-default-fg-color--lightest); border-radius:8px; padding:5px 11px; white-space:nowrap; flex:0 0 auto; }
#nt-alt-f input { width:58px; background:var(--md-code-bg-color); color:var(--md-default-fg-color); border:1px solid var(--md-default-fg-color--lightest); border-radius:6px; padding:6px 8px; font-size:0.78rem; font-family:var(--md-code-font,monospace); text-align:center; -moz-appearance:textfield; }
#nt-alt-f input::-webkit-outer-spin-button, #nt-alt-f input::-webkit-inner-spin-button { -webkit-appearance:none; margin:0; }
#nt-alt-f input:focus { outline:none; border-color:var(--nt-gold); }
.nt-sched { margin-top:0.45rem; font-size:0.74rem; color:#e6c34a; font-family:var(--md-code-font,monospace); display:flex; align-items:center; gap:6px; }
.nt-sched::before { content:"◷"; font-size:0.9rem; }
#nt-root .nt-pop-sched { margin:0 0 7px; font-size:0.73rem; color:#e6c34a; font-family:var(--md-code-font,monospace); }

#nt-map { width:100%; height:600px; border-radius:8px; border:1px solid rgba(140,120,4,.3); box-shadow:0 2px 12px rgba(0,0,0,.15); position:relative; z-index:0; }

/* full-NOTAM popup (dark, matches theme) */
#nt-root .leaflet-popup.nt-pop-wrap .leaflet-popup-content-wrapper {
  background:#12151c; color:#e8ecf2; border:1px solid rgba(140,120,4,.5); border-radius:8px; box-shadow:0 6px 22px rgba(0,0,0,.55);
}
#nt-root .leaflet-popup.nt-pop-wrap .leaflet-popup-content { margin:11px 13px; }
#nt-root .leaflet-popup.nt-pop-wrap .leaflet-popup-tip { background:#12151c; border:1px solid rgba(140,120,4,.5); }
#nt-root .leaflet-popup.nt-pop-wrap a.leaflet-popup-close-button { color:#9aa4b2; }
#nt-root .nt-pop-h { display:flex; align-items:center; gap:8px; flex-wrap:wrap; }
#nt-root .nt-pop-h b { font-family:var(--md-code-font,monospace); font-size:0.95rem; color:#f2f5f9; }
#nt-root .nt-pop-m { font-family:var(--md-code-font,monospace); font-size:0.72rem; color:#9aa4b2; margin:4px 0 7px; }
#nt-root .nt-pop-b { font-family:var(--md-code-font,monospace); font-size:0.77rem; line-height:1.5; white-space:pre-wrap; word-break:break-word; max-height:230px; overflow:auto; color:#dbe1ea; }
#nt-root .nt-pop-s { margin-top:7px; padding-top:6px; border-top:1px solid rgba(255,255,255,.09); font-size:0.66rem; color:#9aa4b2; }
#nt-root .nt-mk {
  display:flex; align-items:center; justify-content:center; border-radius:50%;
  background:rgba(0,199,116,.9); color:#04120a; font-weight:800; font-family:var(--md-code-font,monospace);
  border:2px solid #04120a; box-shadow:0 0 0 2px rgba(0,199,116,.4), 0 2px 6px rgba(0,0,0,.5);
}
#nt-root .nt-pop { font-family:var(--md-text-font,sans-serif); }
#nt-root .nt-pop b { font-family:var(--md-code-font,monospace); }

#nt-list { margin-top:1rem; display:grid; gap:10px; }
.nt-card {
  border:1px solid var(--md-default-fg-color--lightest); border-left:4px solid var(--nt-exp);
  border-radius:8px; background:var(--md-code-bg-color); padding:0.7rem 0.9rem;
  cursor:pointer; transition:border-color .12s, background .12s;
}
.nt-card:hover { border-color:rgba(140,120,4,.45); }
.nt-card.open { background:var(--md-default-bg-color); }
.nt-card.active   { border-left-color:var(--nt-active); }
.nt-card.upcoming { border-left-color:var(--nt-soon); }
/* collapsed: clamp the body to a short preview; expanded: show all + detail */
.nt-card .nt-body { display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden; }
.nt-card.open .nt-body { display:block; overflow:visible; }
.nt-detail { display:none; margin-top:0.5rem; }
.nt-card.open .nt-detail { display:block; }
.nt-mapbtn {
  margin-top:0.6rem; background:var(--nt-gold); color:#1a1a1a; border:1px solid var(--nt-gold);
  font-weight:700; font-size:0.72rem; letter-spacing:.03em; padding:6px 13px; border-radius:999px; cursor:pointer;
}
.nt-mapbtn:hover { filter:brightness(1.12); }
.nt-expand { margin-left:auto; font-size:0.7rem; color:var(--md-default-fg-color--light); }
.nt-top { display:flex; flex-wrap:wrap; align-items:center; gap:8px; }
.nt-num { font-family:var(--md-code-font,monospace); font-weight:800; font-size:0.92rem; color:var(--md-default-fg-color); }
.nt-icao {
  font-family:var(--md-code-font,monospace); font-weight:700; font-size:0.74rem; color:var(--nt-gold);
  border:1px solid rgba(140,120,4,.4); border-radius:5px; padding:1px 6px; cursor:pointer;
}
.nt-pill { font-size:0.63rem; font-weight:800; letter-spacing:.06em; text-transform:uppercase; padding:2px 8px; border-radius:999px; }
.nt-pill.active   { background:rgba(0,199,116,.16); color:var(--nt-active); }
.nt-pill.upcoming { background:rgba(255,157,60,.16); color:var(--nt-soon); }
.nt-pill.expired  { background:rgba(255,90,90,.16); color:var(--nt-exp); }
.nt-rtag { font-size:0.6rem; font-weight:700; color:#e6c34a; border:1px solid rgba(230,195,74,.5); background:rgba(230,195,74,.14); border-radius:4px; padding:1px 5px; letter-spacing:.04em; }
.nt-when { margin-left:auto; font-family:var(--md-code-font,monospace); font-size:0.72rem; color:var(--md-default-fg-color--light); white-space:nowrap; }
.nt-body { margin-top:0.5rem; font-family:var(--md-code-font,monospace); font-size:0.8rem; line-height:1.5; white-space:pre-wrap; word-break:break-word; color:var(--md-default-fg-color); }
.nt-sub { margin-top:0.45rem; display:flex; flex-wrap:wrap; gap:4px 12px; font-size:0.66rem; color:var(--md-default-fg-color--light); }
.nt-sub .k { text-transform:uppercase; letter-spacing:.05em; }
.nt-empty, .nt-loading { font-size:0.85rem; color:var(--md-default-fg-color--light); font-style:italic; padding:1.4rem 0; text-align:center; }
</style>

<div id="nt-bar">
  <input id="nt-search" type="text" placeholder="Search ICAO, airport, number or text…" autocomplete="off" />
  <div id="nt-seg">
    <button data-s="active" class="on">Active</button>
    <button data-s="upcoming">Upcoming</button>
    <button data-s="expired">Expired</button>
    <button data-s="all">All</button>
  </div>
  <select id="nt-ap"><option value="">All aerodromes</option></select>
  <select id="nt-cat"><option value="">All categories</option></select>
  <label id="nt-now-l" title="Only NOTAMs in force right now, including their daily D) schedule"><input type="checkbox" id="nt-now"> In effect now</label>
  <span id="nt-alt-f" title="Show NOTAMs whose vertical extent overlaps this flight-level range">FL <input id="nt-flmin" type="number" min="0" max="999" placeholder="min"> – <input id="nt-flmax" type="number" min="0" max="999" placeholder="max"></span>
  <label id="nt-areas-l"><input type="checkbox" id="nt-areas" checked> Areas</label>
</div>

<div id="nt-meta">
  <span id="nt-showing"></span>
  <span class="nt-updated" id="nt-updated"></span>
  <span id="nt-reset">✕ clear aerodrome</span>
</div>

<div id="nt-map"></div>

<div id="nt-list"><p class="nt-loading">Loading NOTAMs…</p></div>
</div>

<script>
(function () {
  function init() {
    if (!window.L) { setTimeout(init, 100); return; }
    var mapEl = document.getElementById('nt-map');
    if (!mapEl || mapEl._leaflet_id) return;
    // Leaflet is loaded twice (in this page and site-wide), and when Material
    // re-runs the page (instant navigation, or a #hash change) a fresh copy can
    // replace window.L after the map already exists. Layers from one copy
    // crash on a map from the other, so pin the copy the map is built with.
    var L = window.L;

    var MON = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
    var SCOPE = { A:'Aerodrome', E:'En-route', W:'Nav warning', AE:'Aerodrome + En-route', AW:'Aerodrome + Warning', K:'Checklist' };
    var TRAFFIC = { I:'IFR', V:'VFR', IV:'IFR & VFR', K:'Checklist' };
    var PURPOSE = { N:'Immediate attention', B:'Optionally significant', O:'Flight operations',
                    M:'Miscellaneous', K:'Checklist', BO:'Branch office', NBO:'National branch office' };
    // category filter, keyed off the Q-code subject (2nd–3rd letters of the Q-code)
    var CATS = [
      ['rwy',  'Runway / taxiway / apron'],
      ['lgt',  'Lighting'],
      ['fac',  'Aerodrome facilities'],
      ['nav',  'Navaids & comms'],
      ['atm',  'Airspace, ATS & procedures'],
      ['warn', 'Military, UAS & warnings'],
      ['obst', 'Obstacles'],
      ['oth',  'Other / AIP triggers']
    ];
    var CAT_NAME = {}; CATS.forEach(function(c){ CAT_NAME[c[0]] = c[1]; });
    function catOf(n){
      var s = (n.code || '').slice(0, 2), c = s.charAt(0);
      if (s === 'OB' || s === 'OL') return 'obst';
      if (!c) return 'oth';
      if (c === 'M') return 'rwy';
      if (c === 'L') return 'lgt';
      if (c === 'F') return 'fac';
      if ('INGC'.indexOf(c) !== -1) return 'nav';
      if ('ASP'.indexOf(c) !== -1) return 'atm';
      if (c === 'R' || c === 'W') return 'warn';
      return 'oth';
    }
    // abbreviations + Q-code meanings (docs/assets/data/notam_glossary.json)
    var GLOSS = { abbr:{}, qsubj:{}, qcond:{} };
    function qText(n){
      if (!n.code) return '';
      var subj = GLOSS.qsubj[n.code.slice(0, 2)], cond = n.code.slice(2, 4);
      var ctext = cond !== 'XX' && GLOSS.qcond[cond];
      return n.code + (subj ? ' · ' + subj + (ctext ? ' — ' + ctext : '') : '');
    }
    function subItems(n){
      var a = [];
      if (n.alt)     a.push(['Alt', n.alt]);
      if (n.code)    a.push(['Q', qText(n)]);
      if (n.scope)   a.push(['Scope', SCOPE[n.scope] || n.scope]);
      if (n.traffic) a.push(['Traffic', TRAFFIC[n.traffic] || n.traffic]);
      if (n.purpose) a.push(['Purpose', PURPOSE[n.purpose] || n.purpose]);
      if (n.est)     a.push([n.est, '']);
      return a;
    }
    function subHtml(n){
      return subItems(n).map(function(kv){
        return '<span><span class="k">'+esc(kv[0])+'</span>'+(kv[1]?' '+esc(kv[1]):'')+'</span>';
      }).join('');
    }
    function pad(n){ return (n<10?'0':'')+n; }
    function fmt(iso){
      if (!iso) return null; var d=new Date(iso); if (isNaN(d)) return null;
      var y = d.getUTCFullYear();   // only spell out the year when it isn't this one
      return pad(d.getUTCDate())+' '+MON[d.getUTCMonth()]+(y!==new Date().getUTCFullYear()?' '+y:'')
        +' '+pad(d.getUTCHours())+':'+pad(d.getUTCMinutes())+'Z';
    }
    function fmtShort(ms){         // "14:00Z" today, "02 Oct 14:00Z" otherwise
      var d = new Date(ms), n = new Date(NOW), hm = pad(d.getUTCHours())+':'+pad(d.getUTCMinutes())+'Z';
      return d.toISOString().slice(0,10) === n.toISOString().slice(0,10) ? hm : pad(d.getUTCDate())+' '+MON[d.getUTCMonth()]+' '+hm;
    }
    var NOW = Date.now();
    function statusOf(n){
      var f = n._badFrom ? null : (n.from ? Date.parse(n.from) : null);
      var t = n.to ? Date.parse(n.to) : null;
      n._estPast = false;
      if (f && f > NOW) return 'upcoming';
      if (t && t < NOW){
        // an EST end is only an estimate: the NOTAM stays in force until CAAP
        // cancels or replaces it (their AIS still lists these as Active)
        if (n.est === 'EST'){ n._estPast = true; return 'active'; }
        return 'expired';
      }
      return 'active';
    }
    function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;'); }
    // NOTAM text with ICAO abbreviations / aerodrome codes explained on hover
    // (data-t feeds the page's own tooltip — see showTip below)
    function annotate(text){
      return esc(text || '').replace(/\b(U\/S|A\/G|[A-Z][A-Z0-9]+)\b/g, function(w){
        var t = GLOSS.abbr[w] || (DATA.airports[w] && DATA.airports[w][2]);
        return t ? '<abbr data-t="'+esc(t)+'">'+w+'</abbr>' : w;
      });
    }

    // ---- D) schedule: "2200-1000", "SUN-FRI 2130-2230 0830-0930",
    // "SEP 26-OCT 10 0000-2359, OCT 14-22 0000-2359", "0000-2359 EXC JUL 04 06".
    // Times are UTC; a window whose end is before its start runs past midnight
    // and belongs to the day it starts on. Returns null for anything not
    // understood (SR-SS, HJ, …) so the raw text is shown without a verdict.
    var WDAY = { SUN:0, MON:1, TUE:2, WED:3, THU:4, FRI:5, SAT:6 };
    var MONS = { JAN:0, FEB:1, MAR:2, APR:3, MAY:4, JUN:5, JUL:6, AUG:7, SEP:8, OCT:9, NOV:10, DEC:11 };
    function parseSched(txt){
      var toks = String(txt).toUpperCase().replace(/\s*-\s*/g, '-').replace(/,/g, ' , ').split(/\s+/).filter(Boolean);
      var segs = [], exc = { wd:null, dates:[] }, cur = null, inExc = false, mon = null, m;
      function days(){ return inExc ? exc : (cur && !cur.win.length ? cur : (cur = { wd:null, dates:[], win:[] }, segs.push(cur), cur)); }
      function addWd(a, b){
        var d = days(); d.wd = d.wd || {};
        for (var i = a; ; i = (i + 1) % 7){ d.wd[i] = true; if (i === b) break; }
      }
      for (var i = 0; i < toks.length; i++){
        var t = toks[i];
        if (t === ','){ inExc = false; cur = null; continue; }
        if (t === 'EXC'){ inExc = true; continue; }
        if (t === 'DAILY'){ days(); continue; }
        if ((m = /^(\d{2})(\d{2})-(\d{2})(\d{2})$/.exec(t)) || t === 'H24'){
          if (inExc) return null;
          if (!cur){ cur = { wd:null, dates:[], win:[] }; segs.push(cur); }
          var a = m ? +m[1]*60 + +m[2] : 0, b = m ? +m[3]*60 + +m[4] : 1440;
          if (b === 23*60+59) b = 1440;              // "…-2359" means to the end of the day
          cur.win.push([a, b > a ? b : b + 1440]);
          continue;
        }
        if (t in WDAY){ addWd(WDAY[t], WDAY[t]); continue; }
        if ((m = /^([A-Z]{3})-([A-Z]{3})$/.exec(t)) && m[1] in WDAY && m[2] in WDAY){ addWd(WDAY[m[1]], WDAY[m[2]]); continue; }
        if (t in MONS){ mon = MONS[t]; days(); continue; }
        if (mon === null) return null;
        if ((m = /^(\d{1,2})$/.exec(t))){ days().dates.push([mon*100 + +m[1]]); continue; }
        if ((m = /^(\d{1,2})-(\d{1,2})$/.exec(t))){ days().dates.push([mon*100 + +m[1], mon*100 + +m[2]]); continue; }
        // "SEP 26-OCT 10": range start here, end month now, end day is the next token
        if ((m = /^(\d{1,2})-([A-Z]{3})$/.exec(t)) && m[2] in MONS && /^\d{1,2}$/.test(toks[i+1] || '')){
          var start = mon*100 + +m[1]; mon = MONS[m[2]];
          days().dates.push([start, mon*100 + +toks[++i]]);
          continue;
        }
        return null;
      }
      segs.forEach(function(s){ if (!s.win.length) s.win.push([0, 1440]); });
      return segs.length ? { segs:segs, exc:exc } : null;
    }
    function dayMatch(spec, d){                       // d: Date at 00:00Z
      if (spec.wd && !spec.wd[d.getUTCDay()]) return false;
      if (!spec.dates.length) return true;
      var md = d.getUTCMonth()*100 + d.getUTCDate();
      return spec.dates.some(function(r){
        if (r.length === 1) return md === r[0];
        return r[0] <= r[1] ? (md >= r[0] && md <= r[1]) : (md >= r[0] || md <= r[1]);   // wraps the new year
      });
    }
    // -> { on:bool, until:ms|null, next:ms|null } relative to `now`; `until`
    // runs through back-to-back windows (e.g. daily 0000-2359) and is null
    // when that chain reaches past the 3-week look-ahead
    function schedState(sp, now){
      var d0 = new Date(now), iv = [], H = 22;
      d0 = Date.UTC(d0.getUTCFullYear(), d0.getUTCMonth(), d0.getUTCDate());
      for (var off = -1; off <= H; off++){
        var day = d0 + off*864e5, dd = new Date(day);
        if ((sp.exc.wd || sp.exc.dates.length) && dayMatch(sp.exc, dd)) continue;
        sp.segs.forEach(function(s){
          if (dayMatch(s, dd)) s.win.forEach(function(w){ iv.push([day + w[0]*6e4, day + w[1]*6e4]); });
        });
      }
      iv.sort(function(a, b){ return a[0] - b[0]; });
      var res = { on:false, until:null, next:null };
      iv.forEach(function(w){
        if (w[0] <= now && now < w[1]){ res.on = true; res.until = Math.max(res.until || 0, w[1]); }
        else if (w[0] > now && res.next === null) res.next = w[0];
      });
      if (res.on){
        iv.forEach(function(w){ if (w[0] <= res.until && w[1] > res.until) res.until = w[1]; });
        if (res.until >= d0 + H*864e5) res.until = null;
        res.next = null;
      }
      return res;
    }
    // schedule verdict for an active NOTAM, clipped to its own C) end
    function schedNow(n){
      if (!n._sp || n._st !== 'active') return null;
      var r = schedState(n._sp, NOW), to = (n.to && !n._estPast) ? Date.parse(n.to) : null;
      if (r.on && to) r.until = r.until ? Math.min(r.until, to) : to;
      if (!r.on && r.next && to && r.next >= to) r.next = null;
      return r;
    }
    function nowBadge(n){
      var r = n._sn;
      if (!r) return '';
      return r.on ? '<span class="nt-now on" data-t="Inside its scheduled hours right now">◷ NOW</span>'
                  : '<span class="nt-now off" data-t="Outside its scheduled hours">◷ '+(r.next ? 'from '+fmtShort(r.next) : 'not now')+'</span>';
    }
    function schedLine(n){
      var r = n._sn, st = '';
      if (r) st = r.on ? 'in effect now' + (r.until ? ' until ' + fmtShort(r.until) : '')
                       : (r.next ? 'next ' + fmtShort(r.next) : 'no further window');
      return esc(n.sched) + (st ? ' <span class="nt-sched-st">· ' + st + '</span>' : '');
    }

    function fmtWindow(n){
      var toTxt = n.to ? fmt(n.to) + (n.est==='EST' ? ' EST' : '') : (n.est==='PERM' ? 'PERM' : 'UFN');
      return (fmt(n.from)||'—') + '  →  ' + toTxt;
    }
    function tagHtml(n){
      var w = n.type==='R' ? 'REPLACES' : (n.type==='C' ? 'CANCELS' : '');
      return w ? '<span class="nt-rtag">'+w+(n.ref?' '+esc(n.ref):'')+'</span>' : '';
    }
    function notesHtml(n){
      var a = [];
      if (n._badFrom) a.push(['warn', 'Start time is after the end time in the source NOTAM — treat the start as unknown.']);
      if (n._estPast) a.push(['warn', 'Estimated end has passed — remains in force until cancelled or replaced.']);
      if (n.geo && n.geo.q) a.push(['info', 'Map position is approximate — the NOTAM\'s Q-line centre and radius, not its text.']);
      return a.map(function(x){
        return '<div class="nt-note'+(x[0]==='info'?' info':'')+'">'+(x[0]==='info'?'ⓘ ':'⚠ ')+x[1]+'</div>';
      }).join('');
    }
    function apShort(icao){
      var a = DATA.airports[icao]; if (!a) return '';
      var s = a[2].replace(/ \/.*$/, '').replace(/\bInternational\b/, 'Intl').replace(/ Airport$/, '');
      return s.length > 28 ? s.slice(0, 27) + '…' : s;
    }
    function notamPopup(n){
      var st = n._st, sh = subHtml(n);
      return '<div class="nt-pop">'
        + '<div class="nt-pop-h"><b>'+esc(n.num)+'</b>'
        +   '<span class="nt-pill '+st+'">'+st+'</span>'
        +   nowBadge(n) + tagHtml(n)+'</div>'
        + '<div class="nt-pop-m">'+esc(n.icao)+'  ·  '+fmtWindow(n)+'</div>'
        + (n.sched?'<div class="nt-pop-sched">◷ '+schedLine(n)+'</div>':'')
        + notesHtml(n)
        + '<div class="nt-pop-b">'+annotate(n.text)+'</div>'
        + (sh?'<div class="nt-pop-s nt-sub">'+sh+'</div>':'')
        + '</div>';
    }

    var HOME = [12.6, 122.6], HOME_Z = 5;
    // The wheel zooms as soon as the pointer moves over the map. While the page
    // itself is scrolling and the map slides under a still pointer, the wheel
    // keeps scrolling the page instead of getting stuck zooming the map.
    var map = L.map('nt-map', { zoomControl:true, attributionControl:true, scrollWheelZoom:false })
      .setView(HOME, HOME_Z);
    // (browsers fire a zero-movement mousemove after a page scroll; ignore it)
    mapEl.addEventListener('mousemove', function(e){ if (e.movementX || e.movementY) map.scrollWheelZoom.enable(); });
    window.addEventListener('scroll', function(){
      if (document.body.contains(mapEl)) map.scrollWheelZoom.disable();
    }, { passive:true });
    L.tileLayer('https://services.arcgisonline.com/arcgis/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{z}/{y}/{x}',
      { attribution:'Tiles &copy; Esri', maxZoom:16 }).addTo(map);
    L.tileLayer('https://services.arcgisonline.com/arcgis/rest/services/Canvas/World_Dark_Gray_Reference/MapServer/tile/{z}/{y}/{x}',
      { maxZoom:16, opacity:0.85 }).addTo(map);
    // RPHI (Manila) FIR boundary — outline only, no fill, sits at the back
    fetch('../../assets/data/mnl_boundary.json').then(function(r){ return r.json(); }).then(function(geo){
      L.geoJSON(geo, { interactive:false, style:{ color:'#4a9eff', weight:1.5, opacity:0.45, fill:false, dashArray:'5,6' } }).addTo(map).bringToBack();
    }).catch(function(){});
    var geoLayer = L.layerGroup().addTo(map);   // NOTAM areas (drawn first = under)
    var mkLayer = L.layerGroup().addTo(map);     // aerodrome count bubbles (on top)

    var DATA = { notams:[], airports:{} };
    var byId = {}, byNum = {}, counts = {}, shapeLayers = {}, openIds = {};
    var state = { s:'active', q:'', ap:'', cat:'', now:false, areas:true, flMin:null, flMax:null };
    var SCOL = { active:'#00c774', upcoming:'#ff9d3c', expired:'#ff5a5a' };

    // Leaflet's close button is <a href="#close">. Under Material's instant
    // navigation that stray hash re-runs the page (looks like a crash), so
    // strip the href and close the popup ourselves.
    map.on('popupopen', function(e){
      var c = e.popup && e.popup._container;
      var btn = c && c.querySelector('.leaflet-popup-close-button');
      if (!btn) return;
      btn.removeAttribute('href');
      btn.style.cursor = 'pointer';
      if (!btn._ntfix){
        btn._ntfix = true;
        btn.addEventListener('click', function(ev){ ev.preventDefault(); ev.stopPropagation(); map.closePopup(); });
      }
    });

    function bubbleColor(grp){   // most relevant status among an aerodrome's NOTAMs
      if (grp.some(function(n){ return n._st==='active'; }))   return SCOL.active;
      if (grp.some(function(n){ return n._st==='upcoming'; })) return SCOL.upcoming;
      return SCOL.expired;
    }
    function passStatus(st){ return state.s==='all' ? true : st===state.s; }
    function matches(n){
      var st = n._st;
      if (!passStatus(st)) return false;
      if (state.now && (st !== 'active' || (n._sn && !n._sn.on))) return false;
      if (state.ap && n.icao !== state.ap) return false;
      if (state.cat && n._cat !== state.cat) return false;
      if (state.q && n._hay.indexOf(state.q) === -1) return false;
      if (state.flMin != null || state.flMax != null){
        // keep NOTAMs whose [low,high] FL band overlaps the query range;
        // NOTAMs with no stated limits are always shown (unknown vertical extent)
        if (n.low != null){
          var qlo = state.flMin != null ? state.flMin : 0;
          var qhi = state.flMax != null ? state.flMax : 999;
          if (n.high < qlo || n.low > qhi) return false;
        }
      }
      return true;
    }

    function renderMap(list){
      mkLayer.clearLayers();
      geoLayer.clearLayers();
      shapeLayers = {};
      if (state.areas){
        list.forEach(function(n){
          if (!n.geo) return;
          var col = SCOL[n._st] || '#8892a0', g = n.geo, lyr = null;
          // Q-line positions are approximate: dashed and fainter
          var dash = g.q ? '6,6' : null, fo = g.q ? .05 : .1;
          if (g.t==='poly')      lyr = L.polygon(g.c, { color:col, weight:2, opacity:.9, fillColor:col, fillOpacity:.12 });
          else if (g.t==='line') lyr = L.polyline(g.c, { color:col, weight:3, opacity:.9 });
          else if (g.t==='circ') lyr = L.circle(g.c[0], { radius:(g.r||1)*1852, color:col, weight:2, opacity:.9, fillColor:col, fillOpacity:fo, dashArray:dash });
          else if (g.t==='pts')  lyr = L.featureGroup(g.c.map(function(p){ return L.circleMarker(p, { radius:4, color:col, weight:1.5, fillColor:col, fillOpacity:.7 }); }));
          if (lyr){ lyr.addTo(geoLayer).bindPopup(notamPopup(n), { maxWidth:340, minWidth:240, className:'nt-pop-wrap' }); shapeLayers[n.id] = lyr; }
        });
      }
      var by = {};
      list.forEach(function(n){ if (DATA.airports[n.icao]){ (by[n.icao]=by[n.icao]||[]).push(n); } });
      Object.keys(by).forEach(function(icao){
        var ap = DATA.airports[icao], grp = by[icao], c = grp.length;
        var col = bubbleColor(grp);
        var r = Math.min(15, 9 + Math.round(Math.log(c+1)*4));
        // hover tooltip, not a popup: the click re-renders the layer, which
        // would close a popup the instant it opened
        L.marker([ap[0], ap[1]], { icon: L.divIcon({ className:'', iconSize:[r*2,r*2], iconAnchor:[r,r],
            html:'<div class="nt-mk" style="width:'+(r*2)+'px;height:'+(r*2)+'px;font-size:'+(r>11?11:9)+'px;background:'+col+';box-shadow:0 0 0 2px '+col+'66,0 2px 6px rgba(0,0,0,.5)">'+c+'</div>' }) })
          .addTo(mkLayer)
          .bindTooltip('<b>'+esc(icao)+'</b> — '+esc(ap[2])+'<br>'+c+' NOTAM'+(c>1?'s':'')+' shown · click to '+(state.ap===icao?'clear':'filter'),
                       { direction:'top', offset:[0,-r] })
          .on('click', function(){ setAp(icao, true); });
      });
    }

    function renderList(list){
      var box = document.getElementById('nt-list');
      if (!list.length){ box.innerHTML = '<p class="nt-empty">No NOTAMs match these filters.</p>'; return; }
      var html = list.map(function(n){
        var st = n._st;
        var sched = n.sched ? '<div class="nt-sched">'+schedLine(n)+'</div>' : '';
        var mapbtn = (n.geo || DATA.airports[n.icao]) ? '<button class="nt-mapbtn" data-id="'+n.id+'">Show on map ›</button>' : '';
        var apName = DATA.airports[n.icao] ? ' data-t="'+esc(DATA.airports[n.icao][2])+' — click to filter"' : '';
        return '<div class="nt-card '+st+(openIds[n.id]?' open':'')+'" data-id="'+n.id+'">'
          + '<div class="nt-top">'
          +   '<span class="nt-num">'+esc(n.num)+'</span>'
          +   '<span class="nt-icao" data-icao="'+esc(n.icao)+'"'+apName+'>'+esc(n.icao)+'</span>'
          +   '<span class="nt-pill '+st+'">'+st+'</span>'
          +   nowBadge(n)
          +   tagHtml(n)
          +   '<span class="nt-when">'+fmtWindow(n)+'</span>'
          +   '<span class="nt-expand">▾</span>'
          + '</div>'
          + '<div class="nt-body">'+annotate(n.text)+'</div>'
          + '<div class="nt-detail">'
          +   sched
          +   notesHtml(n)
          +   '<div class="nt-sub">'+subHtml(n)+'</div>'
          +   '<div class="nt-actions">'+mapbtn
          +     '<button class="nt-linkbtn" data-num="'+esc(n.num)+'">Copy link</button></div>'
          + '</div>'
          + '</div>';
      }).join('');
      box.innerHTML = html;
      // whole card toggles open/closed — but not when the click ends a text
      // selection (copying NOTAM text shouldn't collapse the card)
      box.querySelectorAll('.nt-card').forEach(function(card){
        card.addEventListener('click', function(){
          var sel = window.getSelection && window.getSelection();
          if (sel && !sel.isCollapsed && card.contains(sel.anchorNode)) return;
          var id = card.getAttribute('data-id');
          if (card.classList.toggle('open')) openIds[id] = true; else delete openIds[id];
        });
      });
      // ICAO chip filters by aerodrome (don't toggle the card)
      box.querySelectorAll('.nt-icao').forEach(function(el){
        el.addEventListener('click', function(ev){ ev.stopPropagation(); setAp(el.getAttribute('data-icao'), true); });
      });
      // "Show on map" flies to it (don't toggle the card)
      box.querySelectorAll('.nt-mapbtn').forEach(function(el){
        el.addEventListener('click', function(ev){ ev.stopPropagation(); focusNotam(byId[el.getAttribute('data-id')]); });
      });
      box.querySelectorAll('.nt-linkbtn').forEach(function(el){
        el.addEventListener('click', function(ev){ ev.stopPropagation(); copyLink(el); });
      });
    }

    function focusNotam(n, noScroll){
      if (!n) return;
      if (!noScroll) mapEl.scrollIntoView({ behavior:'smooth', block:'center' });
      var b = null, center = null;
      if (n.geo && n.geo.c && n.geo.c.length){
        b = L.latLngBounds(n.geo.c.map(function(p){ return L.latLng(p[0], p[1]); }));
        if (n.geo.t==='circ'){ b = b.getCenter().toBounds((n.geo.r||1)*1852*2.4); }
        center = b.getCenter();
      } else if (DATA.airports[n.icao]){
        center = L.latLng(DATA.airports[n.icao][0], DATA.airports[n.icao][1]);
        b = center.toBounds(30000);
      }
      if (!center){ return; }                       // no coords at all -> nothing to show
      var lyr = shapeLayers[n.id];                   // its drawn shape, if areas are on
      // open once the fly-to lands: opening mid-flight lets the popup's
      // autoPan cancel the animation and leave the map off-target
      map.once('moveend', function(){
        if (lyr && lyr.openPopup && lyr._map){ lyr.openPopup(); }
        else { L.popup({ maxWidth:340, minWidth:240, className:'nt-pop-wrap', autoPan:false })
                 .setLatLng(center).setContent(notamPopup(n)).openOn(map); }
      });
      map.flyToBounds(b.pad(0.35), { maxZoom:12, duration:0.6 });
    }

    // re-evaluate status (and schedule windows) against the current time — the
    // page may have been open for hours. Returns a signature so the minute
    // ticker below can tell whether anything visible changed.
    function refreshStatus(){
      NOW = Date.now();
      var sig = '';
      DATA.notams.forEach(function(n){
        n._st = statusOf(n);
        n._sn = schedNow(n);
        sig += n._st.charAt(0) + (n._sn ? (n._sn.on ? '1' : '0') + (n._sn.until || n._sn.next || '') : '');
      });
      return sig;
    }
    var lastSig = '';
    function render(){
      lastSig = refreshStatus();
      var list = DATA.notams.filter(matches);
      renderMap(list);
      renderList(list);
      document.getElementById('nt-showing').textContent =
        list.length + ' NOTAM' + (list.length===1?'':'s') + ' shown' + (state.ap?(' · '+state.ap):'');
      document.getElementById('nt-reset').classList.toggle('show', !!state.ap);
    }
    var ticker = setInterval(function(){
      if (document.getElementById('nt-map') !== mapEl){ clearInterval(ticker); return; }   // navigated away
      if (DATA.notams.length && refreshStatus() !== lastSig) render();
    }, 60000);

    // ---- shareable links: #RPLL (aerodrome) or #B5069/26 (one NOTAM), read
    // once the data loads and again if the hash is edited in place. The page
    // updates the hash with replaceState, not location.hash, so its own
    // changes don't loop back through hashchange.
    function setHash(h){
      try { history.replaceState(history.state, '', h ? '#' + h : location.pathname + location.search); } catch (e) {}
    }
    function linkFor(num){ return location.origin + location.pathname + '#' + num; }
    function copyLink(btn){
      var url = linkFor(btn.getAttribute('data-num'));
      function done(){ btn.textContent = 'Link copied ✓'; setTimeout(function(){ btn.textContent = 'Copy link'; }, 1800); }
      if (navigator.clipboard && navigator.clipboard.writeText){
        navigator.clipboard.writeText(url).then(done, function(){ window.prompt('Copy this link:', url); });
      } else { window.prompt('Copy this link:', url); }
    }
    function setSeg(s){
      state.s = s;
      document.querySelectorAll('#nt-seg button').forEach(function(x){ x.classList.toggle('on', x.getAttribute('data-s') === s); });
    }
    function clearFilters(){
      state.q = ''; state.cat = ''; state.now = false; state.flMin = state.flMax = null; state.ap = '';
      document.getElementById('nt-search').value = '';
      document.getElementById('nt-cat').value = '';
      document.getElementById('nt-now').checked = false;
      document.getElementById('nt-flmin').value = document.getElementById('nt-flmax').value = '';
      document.getElementById('nt-ap').value = '';
    }
    function applyHash(){
      var h = decodeURIComponent((location.hash || '').slice(1)).trim().toUpperCase();
      var n = byNum[h];
      if (n){
        clearFilters();
        refreshStatus();
        setSeg(n._st);
        openIds[n.id] = true;
        render();
        var card = document.querySelector('.nt-card[data-id="'+n.id+'"]');
        if (card){ card.scrollIntoView({ block:'center' }); card.classList.add('flash'); }
        focusNotam(n, true);
        return true;
      }
      if (/^[A-Z]{4}$/.test(h) && counts[h]){ setAp(h); return true; }
      return false;
    }
    window.addEventListener('hashchange', function(){
      // listeners from earlier visits stay registered under instant navigation
      if (document.getElementById('nt-map') === mapEl && DATA.notams.length) applyHash();
    });

    // move the map only when the aerodrome selection itself changes (not on
    // every search keystroke / status toggle, which used to snap it back)
    function setAp(icao, toggle){
      state.ap = (toggle && state.ap===icao) ? '' : icao;
      document.getElementById('nt-ap').value = state.ap;
      setHash(state.ap);
      render();
      var ap = DATA.airports[state.ap];
      if (ap) map.flyTo([ap[0], ap[1]], 9, { duration:0.6 });
      else if (!state.ap) map.flyTo(HOME, HOME_Z, { duration:0.6 });
    }

    // ---- tooltip for abbreviations, ICAO chips and ◷ badges (anything with
    // data-t). Our own rather than title=: native title tooltips appear late,
    // not at all in some embedded browsers, and never on touch screens.
    var root = document.getElementById('nt-root');
    var tip = document.createElement('div'), tipFor = null;
    tip.id = 'nt-tip'; tip.setAttribute('role', 'tooltip');
    root.appendChild(tip);                       // inside the page, so it leaves with it
    function showTip(el){
      tipFor = el;
      tip.innerHTML = (el.tagName === 'ABBR' ? '<b>'+esc(el.textContent)+'</b>' : '') + esc(el.getAttribute('data-t'));
      tip.classList.add('show');
      var r = el.getBoundingClientRect(), w = tip.offsetWidth, h = tip.offsetHeight;
      var y = r.top - h - 6;
      tip.style.left = Math.max(8, Math.min(r.left + r.width/2 - w/2, window.innerWidth - w - 8)) + 'px';
      tip.style.top = (y < 8 ? r.bottom + 6 : y) + 'px';
    }
    function hideTip(){ if (tipFor){ tipFor = null; tip.classList.remove('show'); } }
    root.addEventListener('mouseover', function(e){
      var el = e.target.closest && e.target.closest('[data-t]');
      if (el){ if (el !== tipFor) showTip(el); } else hideTip();
    });
    root.addEventListener('mouseleave', hideTip);
    root.addEventListener('scroll', hideTip, true);     // popup bodies scroll too
    window.addEventListener('scroll', function(){ if (document.body.contains(root)) hideTip(); }, { passive:true });
    // touch screens: tap an abbreviation to see it, without toggling the card
    var touchOnly = window.matchMedia && window.matchMedia('(hover: none)').matches;
    root.addEventListener('click', function(e){
      if (!touchOnly) return;
      var el = e.target.closest && e.target.closest('abbr[data-t]');
      if (!el){ hideTip(); return; }
      e.stopPropagation();
      if (tipFor === el) hideTip(); else showTip(el);
    }, true);

    // controls
    var qTimer = null;
    document.getElementById('nt-search').addEventListener('input', function(e){
      var v = e.target.value.trim().toLowerCase();
      clearTimeout(qTimer);
      qTimer = setTimeout(function(){ state.q = v; render(); }, 150);
    });
    document.getElementById('nt-ap').addEventListener('change', function(e){ setAp(e.target.value); });
    document.getElementById('nt-cat').addEventListener('change', function(e){ state.cat = e.target.value; render(); });
    document.getElementById('nt-now').addEventListener('change', function(e){ state.now = e.target.checked; render(); });
    document.getElementById('nt-reset').addEventListener('click', function(){ setAp(''); });
    document.querySelectorAll('#nt-seg button').forEach(function(b){
      b.addEventListener('click', function(){ setSeg(b.getAttribute('data-s')); render(); });
    });
    document.getElementById('nt-areas').addEventListener('change', function(e){ state.areas = e.target.checked; render(); });
    function flVal(id){ var v = document.getElementById(id).value.trim(); return v==='' ? null : Math.max(0, Math.min(999, parseInt(v,10)||0)); }
    document.getElementById('nt-flmin').addEventListener('input', function(){ state.flMin = flVal('nt-flmin'); render(); });
    document.getElementById('nt-flmax').addEventListener('input', function(){ state.flMax = flVal('nt-flmax'); render(); });

    var glossary = fetch('../../assets/data/notam_glossary.json').then(function(r){ return r.json(); })
      .then(function(g){ GLOSS = g; }).catch(function(){});   // optional: page works without it
    Promise.all([fetch('../../assets/data/notams.json').then(function(r){ return r.json(); }), glossary]).then(function(res){
      var j = res[0];
      DATA = j;
      DATA.notams.forEach(function(n){
        // B) after C) is a typo in the source (e.g. B5069/26 starts "2029"):
        // ignore the start for status/sorting rather than calling it upcoming
        n._badFrom = !!(n.from && n.to && Date.parse(n.from) > Date.parse(n.to));
        n._sp = n.sched ? parseSched(n.sched) : null;
        n._cat = catOf(n);
        var ap = DATA.airports[n.icao];
        n._hay = [n.num, n.icao, ap ? ap[2] : '', n.text || '', n.code || '', qText(n), CAT_NAME[n._cat]].join(' ').toLowerCase();
        byId[n.id] = n; byNum[String(n.num).toUpperCase()] = n;
        counts[n.icao] = (counts[n.icao]||0)+1;
      });
      DATA.notams.sort(function(a, b){
        var fa = a._badFrom ? 0 : (Date.parse(a.from) || 0), fb = b._badFrom ? 0 : (Date.parse(b.from) || 0);
        return fb - fa;
      });
      // aerodrome dropdown — only ICAOs that actually appear, with name + count
      var sel = document.getElementById('nt-ap');
      Object.keys(counts).sort().forEach(function(icao){
        var o = document.createElement('option'), nm = apShort(icao); o.value = icao;
        o.textContent = icao + (nm ? ' — ' + nm : '') + ' (' + counts[icao] + ')'; sel.appendChild(o);
      });
      var ccount = {};
      DATA.notams.forEach(function(n){ ccount[n._cat] = (ccount[n._cat]||0)+1; });
      var csel = document.getElementById('nt-cat');
      CATS.forEach(function(c){
        if (!ccount[c[0]]) return;
        var o = document.createElement('option'); o.value = c[0];
        o.textContent = c[1] + ' (' + ccount[c[0]] + ')'; csel.appendChild(o);
      });
      // the data is a build-time snapshot: new NOTAMs and cancellations since
      // then are missing. CI refreshes it hourly, so a few hours old already
      // means the refresh is failing — say so.
      var upd = document.getElementById('nt-updated');
      var gen = j.generated ? Date.parse(j.generated) : NaN;
      if (!isNaN(gen)){
        var ageH = (Date.now() - gen) / 36e5, stale = ageH >= 3;
        upd.textContent = 'updated ' + fmt(j.generated).replace('Z',' UTC')
          + (stale ? ' · ' + (ageH < 48 ? Math.floor(ageH) + ' hours' : Math.floor(ageH/24) + ' days')
                   + ' old — may be missing new NOTAMs' : '');
        upd.classList.toggle('stale', stale);
      }
      if (!applyHash()) render();
    }).catch(function(e){
      console.error(e);
      document.getElementById('nt-list').innerHTML = '<p class="nt-empty">Could not load NOTAM data.</p>';
    });
  }
  if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', init); } else { init(); }
})();
</script>
