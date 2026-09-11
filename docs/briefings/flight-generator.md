---
hide:
  - toc
---

# Random Flight Generator

Press **Generate** for a random flight that either starts or ends within the RPHI FIR.

<div id="rg-root">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css" />
<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js"></script>

<style>
#rg-root { --rg-gold:#8c7804; --rg-gold-light:#d9d61c; }
#rg-controls {
  display:flex; flex-wrap:wrap; align-items:center; gap:10px; margin:1rem 0 0.75rem;
}
#rg-controls select {
  background: var(--md-code-bg-color); color: var(--md-default-fg-color);
  border:1px solid var(--md-default-fg-color--lightest); border-radius:6px;
  padding:8px 10px; font-size:0.8rem; font-family:inherit;
}
#rg-generate {
  background: var(--rg-gold); border:1px solid var(--rg-gold); color:#1a1a1a;
  font-weight:800; letter-spacing:0.06em; text-transform:uppercase; font-size:0.78rem;
  padding:9px 20px; border-radius:999px; cursor:pointer;
  transition: background .15s, transform .1s, box-shadow .2s;
  box-shadow:0 4px 12px rgba(0,0,0,.18);
}
#rg-generate:hover { background: var(--rg-gold-light); transform:translateY(-1px); }
#rg-generate:active { transform:translateY(0); }
#rg-count { font-size:0.72rem; color: var(--md-default-fg-color--light); }

#rg-map {
  width:100%; height:520px; border-radius:8px; margin-top:0.5rem;
  border:1px solid rgba(140,120,4,.3); box-shadow:0 2px 12px rgba(0,0,0,.15);
  position:relative; z-index:0;
}

#rg-card {
  margin-top:0.9rem; border:1px solid var(--md-default-fg-color--lightest);
  border-left:4px solid var(--rg-gold); border-radius:8px;
  background: var(--md-code-bg-color); padding:0.9rem 1.1rem; display:none;
}
#rg-card.show { display:block; }
.rg-pair {
  display:flex; align-items:center; gap:10px; font-family:var(--md-code-font,monospace);
  font-size:1.25rem; font-weight:700; color: var(--md-default-fg-color); flex-wrap:wrap;
}
.rg-arrow { color: var(--rg-gold); }
.rg-names { font-size:0.72rem; color: var(--md-default-fg-color--light); margin-top:2px; font-family:inherit; }
.rg-route {
  margin-top:0.7rem; font-family:var(--md-code-font,monospace); font-size:0.9rem;
  line-height:1.7; color: var(--md-default-fg-color); word-break:break-word;
  background: var(--md-default-bg-color); border:1px solid var(--md-default-fg-color--lightest);
  border-radius:6px; padding:0.5rem 0.7rem;
}
.rg-meta { display:flex; flex-wrap:wrap; gap:0.5rem 1.25rem; margin-top:0.7rem; font-size:0.75rem; }
.rg-meta .rg-k { color: var(--md-default-fg-color--light); text-transform:uppercase; letter-spacing:0.05em; font-size:0.65rem; }
.rg-meta .rg-v { color: var(--md-default-fg-color); font-weight:600; }
.rg-note { margin-top:0.6rem; font-size:0.75rem; color: var(--rg-gold); }
.rg-loading { font-size:0.8rem; color: var(--md-default-fg-color--light); font-style:italic; }

/* Leaflet marker labels */
#rg-root .rg-wp-label {
  background:rgba(15,17,25,.9); border:1px solid rgba(140,120,4,.6); color:#f0ede0;
  font-family:var(--md-code-font,monospace); font-size:10px; font-weight:700;
  padding:1px 5px; border-radius:3px; white-space:nowrap;
}
#rg-root .rg-wp-label::before { display:none !important; }
#rg-root .leaflet-tooltip { box-shadow:none; }
/* airway bend waypoints — smaller and fainter than route fixes */
#rg-root .rg-awy-wp {
  font-size:8px; font-weight:600; padding:0 3px; color:#aebdd6;
  background:rgba(15,17,25,.68); border-color:rgba(120,140,180,.35);
}
/* airway name label, rotated to run along the line */
#rg-root .rg-awy-name { background:transparent; border:0; }
#rg-root .rg-awy-name span {
  display:block; width:64px; text-align:center; line-height:14px;
  color:#ffe14d; font-family:var(--md-code-font,monospace); font-size:10px;
  font-weight:800; letter-spacing:0.08em;
  text-shadow:0 0 3px #000, 0 0 3px #000, 0 1px 2px #000;
}
</style>

<div id="rg-controls">
  <button id="rg-generate" type="button">✈ Generate Flight</button>
  <select id="rg-filter"><option value="">Any departure</option></select>
  <span id="rg-count"></span>
</div>

<div id="rg-map"></div>

<div id="rg-card">
  <div class="rg-pair"><span id="rg-dep"></span><span class="rg-arrow">→</span><span id="rg-dest"></span></div>
  <div class="rg-names" id="rg-names"></div>
  <div class="rg-route" id="rg-route"></div>
  <div class="rg-meta">
    <div><div class="rg-k">Aircraft</div><div class="rg-v" id="rg-acft"></div></div>
    <div><div class="rg-k">Distance</div><div class="rg-v" id="rg-dist"></div></div>
    <div><div class="rg-k">Direction</div><div class="rg-v" id="rg-dir"></div></div>
    <div><div class="rg-k">Cruise levels</div><div class="rg-v" id="rg-levels"></div></div>
  </div>
  <div class="rg-note" id="rg-note"></div>
</div>

<p class="rg-loading" id="rg-status">Loading routes…</p>
</div>

<script>
(function () {
  function init() {
    if (!window.L) { setTimeout(init, 100); return; }
    var mapEl = document.getElementById('rg-map');
    if (!mapEl || mapEl._leaflet_id) return; // already initialised

    var status = document.getElementById('rg-status');
    var map = L.map('rg-map', { zoomControl: true, attributionControl: true, scrollWheelZoom: false })
      .setView([12.0, 122.5], 5);
    L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png',
      { attribution: '&copy; OpenStreetMap &copy; CARTO', subdomains: 'abcd', maxZoom: 19 }).addTo(map);
    map.on('focus', function () { map.scrollWheelZoom.enable(); });
    map.on('blur',  function () { map.scrollWheelZoom.disable(); });

    // Permanent overlays — non-interactive and always on (no toggle).
    // Manila ACC outer boundary (blue), drawn first so it sits at the back.
    fetch('../../assets/data/mnl_boundary.json').then(function(r){ return r.json(); })
      .then(function(geo){
        L.geoJSON(geo, {
          interactive: false,
          style: { color:'#4a9eff', weight:2, opacity:0.6, fillColor:'#4a9eff', fillOpacity:0.03, dashArray:'6, 6' }
        }).addTo(map).bringToBack();
      }).catch(function(){});
    // TMA boundaries (yellow).
    fetch('../../assets/data/tmas.json').then(function(r){ return r.json(); })
      .then(function(geo){
        L.geoJSON(geo, {
          interactive: false,
          style: { color:'#ffdd00', weight:1.5, opacity:0.65, fillColor:'#ffdd00', fillOpacity:0.04, dashArray:'4, 5' }
        }).addTo(map).bringToBack();
      }).catch(function(){});

    var layer = L.layerGroup().addTo(map);
    var ROUTES = [];

    function toRad(d){ return d*Math.PI/180; }
    function nm(a, b){
      var R=3440.065, dLat=toRad(b[0]-a[0]), dLon=toRad(b[1]-a[1]);
      var s=Math.sin(dLat/2)**2 + Math.cos(toRad(a[0]))*Math.cos(toRad(b[0]))*Math.sin(dLon/2)**2;
      return 2*R*Math.asin(Math.min(1,Math.sqrt(s)));
    }
    function bearing(a, b){
      var y=Math.sin(toRad(b[1]-a[1]))*Math.cos(toRad(b[0]));
      var x=Math.cos(toRad(a[0]))*Math.sin(toRad(b[0])) - Math.sin(toRad(a[0]))*Math.cos(toRad(b[0]))*Math.cos(toRad(b[1]-a[1]));
      return (Math.atan2(y,x)*180/Math.PI + 360) % 360;
    }

    function dot(color){
      return L.divIcon({ className:'', iconSize:[10,10], iconAnchor:[5,5],
        html:'<div style="width:10px;height:10px;border-radius:50%;background:'+color+';border:1.5px solid #0b0d13;box-shadow:0 0 0 1.5px '+color+'55"></div>' });
    }
    function smallDot(color){
      return L.divIcon({ className:'', iconSize:[6,6], iconAnchor:[3,3],
        html:'<div style="width:6px;height:6px;border-radius:50%;background:'+color+';border:1px solid #0b0d13"></div>' });
    }
    function endIcon(letter, color){
      return L.divIcon({ className:'', iconSize:[22,22], iconAnchor:[11,11],
        html:'<div style="width:22px;height:22px;border-radius:50%;background:'+color+';border:2px solid #0b0d13;'
           + 'display:flex;align-items:center;justify-content:center;color:#0b0d13;font-weight:800;font-size:11px;'
           + 'font-family:monospace;box-shadow:0 0 0 2px '+color+'55">'+letter+'</div>' });
    }

    function draw(r){
      layer.clearLayers();
      var line = r.line || [];        // full polyline incl. airway bends
      var pts  = r.pts  || [];        // labelled points: [id, lat, lon, kind]
      var awys = r.awy  || [];        // airway labels: [name, aLat,aLon, bLat,bLon]
      if (line.length < 2) return null;

      // glow under, bright line over
      L.polyline(line, { color:'#8c7804', weight:7, opacity:0.12 }).addTo(layer);
      L.polyline(line, { color:'#d9d61c', weight:2.5, opacity:0.9 }).addTo(layer);

      var dist = 0; for (var i=1;i<line.length;i++) dist += nm(line[i-1], line[i]);
      map.fitBounds(L.latLngBounds(line).pad(0.18));  // set view before projecting labels

      // airway name labels — rotated to run along the line
      awys.forEach(function(a){
        var pa = map.latLngToLayerPoint(L.latLng(a[1], a[2]));
        var pb = map.latLngToLayerPoint(L.latLng(a[3], a[4]));
        var ang = Math.atan2(pb.y - pa.y, pb.x - pa.x) * 180 / Math.PI;
        if (ang > 90) ang -= 180; else if (ang < -90) ang += 180;  // keep upright
        var mid = [(a[1] + a[3]) / 2, (a[2] + a[4]) / 2];
        L.marker(mid, { interactive:false, zIndexOffset:500, icon: L.divIcon({
          className:'rg-awy-name', iconSize:[64,14], iconAnchor:[32,7],
          html:'<span style="transform:rotate(' + ang.toFixed(1) + 'deg)">' + a[0] + '</span>'
        }) }).addTo(layer);
      });

      // waypoints
      pts.forEach(function(p, i){
        var id = p[0], ll = [p[1], p[2]], kind = p[3];
        if (i === 0 || i === pts.length-1) {              // A = departure, B = destination
          var isDep = (i === 0);
          L.marker(ll, { icon: endIcon(isDep?'A':'B', isDep?'#00e096':'#ff5a5a'), zIndexOffset:1000 })
            .addTo(layer).bindTooltip(id, { permanent:true, direction:'top', className:'rg-wp-label', offset:[0,-12] });
        } else if (kind === 'awy') {                      // airway bend fix — small & faint
          L.marker(ll, { icon: smallDot('#6f86b8'), zIndexOffset:200 }).addTo(layer)
            .bindTooltip(id, { permanent:true, direction:'top', className:'rg-wp-label rg-awy-wp', offset:[0,-4] });
        } else {                                          // fix written in the route
          L.marker(ll, { icon: dot('#8ab4ff'), zIndexOffset:300 }).addTo(layer)
            .bindTooltip(id, { permanent:true, direction:'top', className:'rg-wp-label', offset:[0,-6] });
        }
      });

      return { dist: dist, brg: bearing(line[0], line[line.length-1]) };
    }

    function show(r){
      var info = draw(r);
      document.getElementById('rg-dep').textContent = r.dept;
      document.getElementById('rg-dest').textContent = r.dest;
      document.getElementById('rg-route').textContent = r.route || 'DCT';
      document.getElementById('rg-acft').textContent = r.acft || 'Any';
      document.getElementById('rg-dist').textContent = info ? Math.round(info.dist) + ' NM' : '—';
      var eastbound = info ? (info.brg < 180) : null;
      document.getElementById('rg-dir').textContent = info ? (eastbound ? 'Eastbound' : 'Westbound') : '—';
      document.getElementById('rg-levels').textContent = info ? (eastbound ? 'Odd (FL250, 270…)' : 'Even (FL240, 260…)') : '—';
      var note = document.getElementById('rg-note');
      note.textContent = r.notes ? ('⚠ ' + r.notes) : '';
      note.style.display = r.notes ? 'block' : 'none';
      document.getElementById('rg-card').classList.add('show');
    }

    function currentPool(){
      var f = document.getElementById('rg-filter').value;
      return f ? ROUTES.filter(function(r){ return r.dept === f; }) : ROUTES;
    }
    function generate(){
      var pool = currentPool();
      if (!pool.length) return;
      show(pool[Math.floor(Math.random()*pool.length)]);
    }

    document.getElementById('rg-generate').addEventListener('click', generate);
    document.getElementById('rg-filter').addEventListener('change', generate);

    fetch('../../assets/data/routes.json').then(function(r){ return r.json(); })
      .then(function(rj){
        ROUTES = rj.data || [];
        var depts = Array.from(new Set(ROUTES.map(function(r){ return r.dept; }))).sort();
        var sel = document.getElementById('rg-filter');
        depts.forEach(function(d){ var o=document.createElement('option'); o.value=d; o.textContent=d; sel.appendChild(o); });
        document.getElementById('rg-count').textContent = ROUTES.length + ' routes available';
        status.style.display = 'none';
        generate();
      })
      .catch(function(e){
        status.textContent = 'Could not load routes: ' + (e.message || e);
      });
  }
  // Run immediately (the script sits after its markup). Material re-executes
  // inline scripts on instant navigation, so this also fires when navigating in.
  if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', init); }
  else { init(); }
})();
</script>
