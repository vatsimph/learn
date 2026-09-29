---
hide:
  - toc
---

# NOTAMs

Current Philippine (RPHI) NOTAMs from the CAAP AIS. Use the filters or click an aerodrome on the map.

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
#nt-ap {
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
#nt-reset { color:var(--nt-gold); cursor:pointer; font-weight:600; display:none; }
#nt-reset.show { display:inline; }
#nt-areas-l { display:inline-flex; align-items:center; gap:5px; font-size:0.76rem; color:var(--md-default-fg-color--light); cursor:pointer; user-select:none; }
.nt-icao { cursor:pointer; }
#nt-areas-l input[type=checkbox] { accent-color:var(--nt-gold); cursor:pointer; }
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
  <input id="nt-search" type="text" placeholder="Search ICAO, number or text…" autocomplete="off" />
  <div id="nt-seg">
    <button data-s="active" class="on">Active</button>
    <button data-s="upcoming">Upcoming</button>
    <button data-s="expired">Expired</button>
    <button data-s="all">All</button>
  </div>
  <select id="nt-ap"><option value="">All aerodromes</option></select>
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

    var MON = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
    var SCOPE = { A:'Aerodrome', E:'En-route', W:'Nav warning', AE:'Aerodrome + En-route', AW:'Aerodrome + Warning', K:'Checklist' };
    var TRAFFIC = { I:'IFR', V:'VFR', IV:'IFR & VFR', K:'Checklist' };
    var PURPOSE = { N:'Immediate attention', B:'Optionally significant', O:'Flight operations',
                    M:'Miscellaneous', K:'Checklist', BO:'Branch office', NBO:'National branch office' };
    function subItems(n){
      var a = [];
      if (n.alt)     a.push(['Alt', n.alt]);
      if (n.code)    a.push(['Q', n.code]);
      if (n.scope)   a.push(['Scope', SCOPE[n.scope] || n.scope]);
      if (n.traffic) a.push(['Traffic', TRAFFIC[n.traffic] || n.traffic]);
      if (n.purpose) a.push(['Purpose', PURPOSE[n.purpose] || n.purpose]);
      if (n.est)     a.push([n.est, '']);
      return a;
    }
    function subHtml(n){
      return subItems(n).map(function(kv){
        return '<span><span class="k">'+kv[0]+'</span>'+(kv[1]?' '+kv[1]:'')+'</span>';
      }).join('');
    }
    function pad(n){ return (n<10?'0':'')+n; }
    function fmt(iso){
      if (!iso) return null; var d=new Date(iso); if (isNaN(d)) return null;
      return pad(d.getUTCDate())+' '+MON[d.getUTCMonth()]+' '+pad(d.getUTCHours())+':'+pad(d.getUTCMinutes())+'Z';
    }
    var NOW = Date.now();
    function statusOf(n){
      var f = n.from ? Date.parse(n.from) : null;
      var t = n.to   ? Date.parse(n.to)   : null;
      if (f && f > NOW) return 'upcoming';
      if (t && t < NOW) return 'expired';
      return 'active';
    }
    function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
    function fmtWindow(n){
      var toTxt = n.to ? fmt(n.to) : (n.est==='PERM' ? 'PERM' : 'UFN');
      return (fmt(n.from)||'—') + '  →  ' + toTxt;
    }
    function notamPopup(n){
      var st = n._st, sh = subHtml(n);
      return '<div class="nt-pop">'
        + '<div class="nt-pop-h"><b>'+n.num+'</b>'
        +   '<span class="nt-pill '+st+'">'+st+'</span>'
        +   (n.type==='R'?'<span class="nt-rtag">REPLACES</span>':'')+'</div>'
        + '<div class="nt-pop-m">'+n.icao+'  ·  '+fmtWindow(n)+'</div>'
        + (n.sched?'<div class="nt-pop-sched">◷ '+esc(n.sched)+'</div>':'')
        + '<div class="nt-pop-b">'+esc(n.text||'')+'</div>'
        + (sh?'<div class="nt-pop-s nt-sub">'+sh+'</div>':'')
        + '</div>';
    }

    var map = L.map('nt-map', { zoomControl:true, attributionControl:true, scrollWheelZoom:true })
      .setView([12.6, 122.6], 5);
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
    var byId = {}, shapeLayers = {};
    var state = { s:'active', q:'', ap:'', areas:true, flMin:null, flMax:null };
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
      if (state.ap && n.icao !== state.ap) return false;
      if (state.q){
        var hay = (n.num+' '+n.icao+' '+(n.text||'')+' '+(n.code||'')).toLowerCase();
        if (hay.indexOf(state.q) === -1) return false;
      }
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
          if (g.t==='poly')      lyr = L.polygon(g.c, { color:col, weight:2, opacity:.9, fillColor:col, fillOpacity:.12 });
          else if (g.t==='line') lyr = L.polyline(g.c, { color:col, weight:3, opacity:.9 });
          else if (g.t==='circ') lyr = L.circle(g.c[0], { radius:(g.r||1)*1852, color:col, weight:2, opacity:.9, fillColor:col, fillOpacity:.1 });
          else if (g.t==='pts')  lyr = L.featureGroup(g.c.map(function(p){ return L.circleMarker(p, { radius:4, color:col, weight:1.5, fillColor:col, fillOpacity:.7 }); }));
          if (lyr){ lyr.addTo(geoLayer).bindPopup(notamPopup(n), { maxWidth:340, minWidth:240, className:'nt-pop-wrap' }); shapeLayers[n.id] = lyr; }
        });
      }
      var by = {};
      list.forEach(function(n){ if (DATA.airports[n.icao]){ (by[n.icao]=by[n.icao]||[]).push(n); } });
      var pts = [];
      Object.keys(by).forEach(function(icao){
        var ap = DATA.airports[icao], grp = by[icao], c = grp.length;
        var col = bubbleColor(grp);
        var r = Math.min(15, 9 + Math.round(Math.log(c+1)*4));
        pts.push([ap[0], ap[1]]);
        L.marker([ap[0], ap[1]], { icon: L.divIcon({ className:'', iconSize:[r*2,r*2], iconAnchor:[r,r],
            html:'<div class="nt-mk" style="width:'+(r*2)+'px;height:'+(r*2)+'px;font-size:'+(r>11?11:9)+'px;background:'+col+';box-shadow:0 0 0 2px '+col+'66,0 2px 6px rgba(0,0,0,.5)">'+c+'</div>' }) })
          .addTo(mkLayer)
          .bindPopup('<div class="nt-pop"><b>'+icao+'</b> — '+ap[2]+'<br>'+c+' NOTAM'+(c>1?'s':'')+' shown</div>')
          .on('click', function(){ setAp(icao); });
      });
      if (pts.length && state.ap && by[state.ap]) map.setView([DATA.airports[state.ap][0], DATA.airports[state.ap][1]], 8);
    }

    function renderList(list){
      var box = document.getElementById('nt-list');
      if (!list.length){ box.innerHTML = '<p class="nt-empty">No NOTAMs match these filters.</p>'; return; }
      var html = list.map(function(n){
        var st = n._st;
        var toTxt = n.to ? fmt(n.to) : (n.est==='PERM' ? 'PERM' : 'UFN');
        var when = (fmt(n.from)||'—') + '  →  ' + toTxt;
        var rtag = n.type==='R' ? '<span class="nt-rtag">REPLACES</span>' : (n.type==='C' ? '<span class="nt-rtag">CANCEL</span>' : '');
        var sched = n.sched ? '<div class="nt-sched">'+esc(n.sched)+'</div>' : '';
        var mapbtn = (n.geo || DATA.airports[n.icao]) ? '<button class="nt-mapbtn" data-id="'+n.id+'">Show on map ›</button>' : '';
        return '<div class="nt-card '+st+'" data-id="'+n.id+'">'
          + '<div class="nt-top">'
          +   '<span class="nt-num">'+n.num+'</span>'
          +   '<span class="nt-icao" data-icao="'+n.icao+'">'+n.icao+'</span>'
          +   '<span class="nt-pill '+st+'">'+st+'</span>'
          +   rtag
          +   '<span class="nt-when">'+when+'</span>'
          +   '<span class="nt-expand">▾</span>'
          + '</div>'
          + '<div class="nt-body">'+esc(n.text||'')+'</div>'
          + '<div class="nt-detail">'
          +   sched
          +   '<div class="nt-sub">'+subHtml(n)+'</div>'
          +   mapbtn
          + '</div>'
          + '</div>';
      }).join('');
      box.innerHTML = html;
      // whole card toggles open/closed
      box.querySelectorAll('.nt-card').forEach(function(card){
        card.addEventListener('click', function(){ card.classList.toggle('open'); });
      });
      // ICAO chip filters by aerodrome (don't toggle the card)
      box.querySelectorAll('.nt-icao').forEach(function(el){
        el.addEventListener('click', function(ev){ ev.stopPropagation(); setAp(el.getAttribute('data-icao')); });
      });
      // "Show on map" flies to it (don't toggle the card)
      box.querySelectorAll('.nt-mapbtn').forEach(function(el){
        el.addEventListener('click', function(ev){ ev.stopPropagation(); focusNotam(byId[el.getAttribute('data-id')]); });
      });
    }

    function focusNotam(n){
      if (!n) return;
      mapEl.scrollIntoView({ behavior:'smooth', block:'center' });
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
      map.flyToBounds(b.pad(0.35), { maxZoom:12, duration:0.6 });
      var lyr = shapeLayers[n.id];                   // its drawn shape, if areas are on
      if (lyr && lyr.openPopup){ lyr.openPopup(); }
      else { L.popup({ maxWidth:340, minWidth:240, className:'nt-pop-wrap', autoPan:false })
               .setLatLng(center).setContent(notamPopup(n)).openOn(map); }
    }

    function render(){
      var list = DATA.notams.filter(matches);
      renderMap(list);
      renderList(list);
      document.getElementById('nt-showing').textContent =
        list.length + ' NOTAM' + (list.length===1?'':'s') + ' shown' + (state.ap?(' · '+state.ap):'');
      document.getElementById('nt-reset').classList.toggle('show', !!state.ap);
    }

    function setAp(icao){
      state.ap = (state.ap===icao ? '' : icao);
      document.getElementById('nt-ap').value = state.ap;
      render();
    }

    // controls
    document.getElementById('nt-search').addEventListener('input', function(e){ state.q = e.target.value.trim().toLowerCase(); render(); });
    document.getElementById('nt-ap').addEventListener('change', function(e){ state.ap = e.target.value; render(); });
    document.getElementById('nt-reset').addEventListener('click', function(){ state.ap=''; document.getElementById('nt-ap').value=''; render(); });
    document.querySelectorAll('#nt-seg button').forEach(function(b){
      b.addEventListener('click', function(){
        document.querySelectorAll('#nt-seg button').forEach(function(x){ x.classList.remove('on'); });
        b.classList.add('on'); state.s = b.getAttribute('data-s'); render();
      });
    });
    document.getElementById('nt-areas').addEventListener('change', function(e){ state.areas = e.target.checked; render(); });
    function flVal(id){ var v = document.getElementById(id).value.trim(); return v==='' ? null : Math.max(0, Math.min(999, parseInt(v,10)||0)); }
    document.getElementById('nt-flmin').addEventListener('input', function(){ state.flMin = flVal('nt-flmin'); render(); });
    document.getElementById('nt-flmax').addEventListener('input', function(){ state.flMax = flVal('nt-flmax'); render(); });

    fetch('../../assets/data/notams.json').then(function(r){ return r.json(); }).then(function(j){
      DATA = j;
      DATA.notams.forEach(function(n){ n._st = statusOf(n); byId[n.id] = n; });
      // aerodrome dropdown — only ICAOs that actually appear, with counts
      var counts = {};
      DATA.notams.forEach(function(n){ counts[n.icao] = (counts[n.icao]||0)+1; });
      var sel = document.getElementById('nt-ap');
      Object.keys(counts).sort().forEach(function(icao){
        var o = document.createElement('option'); o.value = icao;
        o.textContent = icao + ' (' + counts[icao] + ')'; sel.appendChild(o);
      });
      var g = j.generated ? new Date(j.generated) : null;
      document.getElementById('nt-updated').textContent = g ?
        ('updated ' + fmt(j.generated).replace('Z',' UTC') ) : '';
      render();
    }).catch(function(e){
      document.getElementById('nt-list').innerHTML = '<p class="nt-empty">Could not load NOTAM data.</p>';
    });
  }
  if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', init); } else { init(); }
})();
</script>
