---
hide:
  - toc
---

# Live Traffic

Click an aircraft for its route and details.

<div id="lt-root">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css" />
<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js"></script>

<style>
#lt-root { --lt-gold:#8c7804; }
#lt-bar {
  display:flex; flex-wrap:wrap; gap:8px 16px; align-items:center; margin:0.8rem 0 0.55rem; font-size:0.76rem;
}
#lt-bar .lt-stat b { font-family:var(--md-code-font,monospace); font-size:0.95rem; }
#lt-bar label { display:inline-flex; align-items:center; gap:5px; cursor:pointer; user-select:none; }
#lt-bar input { accent-color:var(--lt-gold); cursor:pointer; }
#lt-legend { display:flex; flex-wrap:wrap; gap:4px 12px; align-items:center; font-size:0.7rem; color:var(--md-default-fg-color--light); }
#lt-legend .k { display:inline-flex; align-items:center; gap:5px; }
#lt-legend .sw { width:12px; height:12px; border-radius:3px; display:inline-block; }
#lt-updated { font-size:0.7rem; color:var(--md-default-fg-color--light); font-family:var(--md-code-font,monospace); margin-left:auto; }

#lt-map { width:100%; height:580px; border-radius:8px; border:1px solid rgba(140,120,4,.3); box-shadow:0 2px 12px rgba(0,0,0,.15); position:relative; z-index:0; }

/* aircraft: heading arrow + label */
#lt-root .lt-ac { position:relative; }
#lt-root .lt-arrow {
  position:absolute; left:-6px; top:-5px; width:0; height:0;
  border-left:5px solid transparent; border-right:5px solid transparent; border-bottom:10px solid #cfd8e0;
  transform-origin:50% 62%; filter:drop-shadow(0 0 1px #000);
}
#lt-root .lt-lbl {
  position:absolute; left:9px; top:-8px; white-space:nowrap;
  font:700 11px/1.12 var(--md-code-font,monospace); color:#10141a;
  padding:2px 5px; border-radius:3px; box-shadow:0 1px 3px rgba(0,0,0,.45);
}
#lt-root .lt-lbl .s { display:block; font-weight:400; font-size:9px; color:#2b3138; }
#lt-root .lt-arr .lt-lbl, .lt-arr-bg,
#lt-root .lt-dep .lt-lbl, .lt-dep-bg { background:#7db3ff; }   /* arrival + departure (RP) */
#lt-root .lt-oth .lt-lbl, .lt-oth-bg { background:#d5dbe1; }   /* other / overflight */
#lt-root .lt-arr .lt-arrow,
#lt-root .lt-dep .lt-arrow { border-bottom-color:#7db3ff; }
#lt-root .lt-oth .lt-arrow { border-bottom-color:#cfd8e0; }

#lt-root .lt-atc-lbl {
  position:absolute; left:8px; top:-9px; display:inline-flex; align-items:baseline; gap:6px;
  font:600 10.5px/1.3 var(--md-text-font,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif);
  white-space:nowrap; color:#eaeef4;
  background:rgba(17,20,27,.82); -webkit-backdrop-filter:blur(4px); backdrop-filter:blur(4px);
  border:1px solid rgba(255,255,255,.09); border-left:3px solid var(--c,#4a9eff);
  border-radius:6px; padding:3px 9px 3px 7px;
  box-shadow:0 3px 10px rgba(0,0,0,.4);
}
#lt-root .lt-atc-lbl .cs { font-weight:600; letter-spacing:.01em; }
#lt-root .lt-atc-lbl .fr {
  font-family:var(--md-code-font,monospace); font-size:9.5px; font-weight:600;
  color:var(--c,#4a9eff); opacity:.92;
}

#lt-root .lt-pop-cs { font-family:var(--md-code-font,monospace); font-weight:700; font-size:14px; }
#lt-root .lt-pop-rt { font-family:var(--md-code-font,monospace); font-size:12px; margin-top:2px; }
#lt-root .lt-pop-k  { font-size:11px; opacity:.7; margin-top:2px; }

#lt-atc-title { margin-top:1.4rem; font-size:0.78rem; font-weight:700; letter-spacing:0.08em; text-transform:uppercase; color:var(--md-default-fg-color--light); }
#lt-atc { display:grid; grid-template-columns:repeat(auto-fill,minmax(210px,1fr)); gap:10px; margin-top:0.55rem; }
.lt-atc-card { border:1px solid var(--md-default-fg-color--lightest); border-left:3px solid var(--lt-gold); border-radius:6px; background:var(--md-code-bg-color); padding:0.55rem 0.7rem; }
.lt-atc-cs { font-family:var(--md-code-font,monospace); font-weight:700; font-size:0.88rem; }
.lt-atc-nm { font-size:0.7rem; color:var(--md-default-fg-color--light); margin:2px 0 5px; }
.lt-atc-fq { font-family:var(--md-code-font,monospace); font-size:0.8rem; color:#4a9eff; font-weight:600; }
.lt-empty { font-size:0.78rem; color:var(--md-default-fg-color--light); font-style:italic; }
</style>

<div id="lt-bar">
  <span class="lt-stat"><b id="lt-air">–</b> airborne</span>
  <span class="lt-stat"><b id="lt-gnd">–</b> ground</span>
  <span class="lt-stat"><b id="lt-ctr">–</b> ATC</span>
  <label><input type="checkbox" id="lt-t-traffic" checked> Traffic</label>
  <label><input type="checkbox" id="lt-t-atc" checked> ATC</label>
  <span id="lt-legend">
    <span class="k"><span class="sw lt-dep-bg"></span>Arrival / Departure</span>
    <span class="k"><span class="sw lt-oth-bg"></span>Transit</span>
  </span>
  <span id="lt-updated"></span>
</div>

<div id="lt-map"></div>

<div id="lt-atc-title">Online ATC</div>
<div id="lt-atc"><span class="lt-empty">Loading…</span></div>
</div>

<script>
(function () {
  var FEED = 'https://data.vatsim.net/v3/vatsim-data.json';
  var AP = {
    RPLL:[14.5086,121.0197],RPLC:[15.1860,120.5600],RPLB:[14.7944,120.2714],
    RPVM:[10.3075,123.9794],RPVP:[9.7419,118.7597],RPVK:[11.6795,122.3760],
    RPVR:[11.5977,122.7517],RPVE:[11.9246,121.9530],RPVD:[9.3342,123.3019],
    RPSP:[9.5739,123.7706],RPMD:[7.1255,125.6458],RPMR:[6.0581,125.0961],RPMY:[8.6122,124.4564],
    RPVI:[10.8331,122.4933],RPVB:[10.7767,123.0192],
    RPLK:[13.1128,123.6778],RPVA:[11.2275,125.0278],RPME:[8.9519,125.4781],
    RPMZ:[6.9225,122.0597],RPUN:[13.5850,123.2708],RPUB:[16.3750,120.6189],RPUS:[16.5956,120.3033],
    RPLI:[18.1761,120.5311],RPUT:[17.6436,121.7331],RPVS:[10.7681,121.9322],RPVV:[12.1219,120.1008],RPSV:[10.5250,119.2740],RPNS:[9.8586,126.0153],
    RPUO:[20.4514,121.9803],RPUV:[13.5769,124.2050],RPUW:[13.3611,121.8256],RPVF:[12.5022,124.6358],RPVJ:[12.3694,123.6297],
    RPVW:[11.6744,125.4794],RPVZ:[9.2117,123.4711],RPSB:[11.1622,123.7847],RPMH:[9.2542,124.7092],RPMS:[9.7578,125.4811]
  };

  function init() {
    if (!window.L) { setTimeout(init, 100); return; }
    var el = document.getElementById('lt-map');
    if (!el || el._leaflet_id) return;
    // Leaflet loads twice (page + site-wide); pin the copy the map is built
    // with so a later reload of window.L can't mix instances.
    var L = window.L;

    // The wheel zooms as soon as the pointer moves over the map. While the page
    // itself is scrolling and the map slides under a still pointer, the wheel
    // keeps scrolling the page instead of getting stuck zooming the map.
    var map = L.map('lt-map', { zoomControl:true, attributionControl:true, scrollWheelZoom:false })
      .setView([12.2, 122.5], 5);
    // (browsers fire a zero-movement mousemove after a page scroll; ignore it)
    el.addEventListener('mousemove', function(e){ if (e.movementX || e.movementY) map.scrollWheelZoom.enable(); });
    window.addEventListener('scroll', function(){
      if (document.body.contains(el)) map.scrollWheelZoom.disable();
    }, { passive:true });
    // Esri Dark Gray Canvas — keyless dark basemap (CARTO's keyless tiles now
    // rate-limit / require a key in some regions).
    L.tileLayer('https://services.arcgisonline.com/arcgis/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{z}/{y}/{x}',
      { attribution:'Tiles &copy; Esri', maxZoom:16 }).addTo(map);
    L.tileLayer('https://services.arcgisonline.com/arcgis/rest/services/Canvas/World_Dark_Gray_Reference/MapServer/tile/{z}/{y}/{x}',
      { maxZoom:16, opacity:0.85 }).addTo(map);

    var acLayer = L.layerGroup().addTo(map);
    var atcLayer = L.layerGroup().addTo(map);
    var rings = [], boundaryLayer = null, tmaFeat = {};
    var ACC = null, id2cs = {};   // Manila ACC sub-sector polygons + owner priority

    function getJSON(url){
      var ac = ('AbortController' in window) ? new AbortController() : null;
      var to = ac ? setTimeout(function(){ ac.abort(); }, 25000) : null;
      return fetch(url, ac ? { signal:ac.signal } : undefined).then(function(r){
        if (to) clearTimeout(to);
        if (!r.ok) throw new Error('HTTP ' + r.status);
        return r.json();
      });
    }

    getJSON('../../assets/data/mnl_boundary.json').then(function(geo){
      boundaryLayer = L.geoJSON(geo, { interactive:false, style:{ color:'#4a9eff', weight:2, opacity:0.5, fillColor:'#4a9eff', fillOpacity:0.02, dashArray:'6,6' } }).addTo(map);
      boundaryLayer.bringToBack();
      (geo.features||[]).forEach(function(f){ var c=f.geometry.coordinates,t=f.geometry.type; (t==='Polygon'?[c]:c).forEach(function(p){ rings.push(p[0]); }); });
    }).catch(function(){});
    getJSON('../../assets/data/tmas.json').then(function(geo){
      L.geoJSON(geo, { interactive:false, style:{ color:'#ffdd00', weight:1, opacity:0.32, fillColor:'#ffdd00', fillOpacity:0.02, dashArray:'4,5' } }).addTo(map).bringToBack();
      (geo.features||[]).forEach(function(f){ if (f.properties && f.properties.id) tmaFeat[f.properties.id]=f; });
    }).catch(function(){});
    getJSON('../../assets/data/acc_sectors.json').then(function(j){ ACC=j; id2cs=j.posmap||{}; }).catch(function(){});

    function centroid(ring){ var x=0,y=0,n=ring.length; for(var i=0;i<n;i++){ x+=ring[i][0]; y+=ring[i][1]; } return [x/n, y/n]; }
    function featCentroid(f){
      var g=f.geometry, cs=g.coordinates, ring;
      if (g.type==='Polygon') ring=cs[0];
      else { ring=cs[0][0]; cs.forEach(function(poly){ if(poly[0].length>ring.length) ring=poly[0]; }); }
      var c=centroid(ring); return [c[1], c[0]];
    }

    function inPH(lat, lon){
      if (!rings.length) return (lat>3&&lat<22&&lon>113&&lon<131);
      for (var r=0;r<rings.length;r++){ var ring=rings[r],ins=false;
        for (var i=0,j=ring.length-1;i<ring.length;j=i++){ var xi=ring[i][0],yi=ring[i][1],xj=ring[j][0],yj=ring[j][1];
          if (((yi>lat)!==(yj>lat)) && (lon<(xj-xi)*(lat-yi)/(yj-yi)+xi)) ins=!ins; }
        if (ins) return true; }
      return false;
    }
    function isRP(s){ return /^RP[A-Z]{2}$/i.test(s||''); }
    function fmtAlt(a){ return a>=18000 ? 'FL'+Math.round(a/100) : (Math.round(a/100)*100)+'ft'; }

    function acIcon(hdg, role, cs, sub){
      return L.divIcon({ className:'', iconSize:[0,0], iconAnchor:[0,0],
        html:'<div class="lt-ac lt-'+role+'">'
          + '<span class="lt-arrow" style="transform:rotate('+(hdg||0)+'deg)"></span>'
          + '<span class="lt-lbl">'+cs+'<span class="s">'+sub+'</span></span></div>' });
    }

    var markers = {};
    function refresh(){
      getJSON(FEED).then(function(d){
        var pilots=d.pilots||[], controllers=d.controllers||[], air=0, gnd=0, seen={};
        pilots.forEach(function(p){
          if (!inPH(p.latitude,p.longitude)) return;
          var ground=(p.groundspeed||0)<50; if(ground)gnd++; else air++;
          seen[p.callsign]=1;
          var fp=p.flight_plan||{}, dep=(fp.departure||'').toUpperCase(), arr=(fp.arrival||'').toUpperCase();
          var role, apt;
          if (isRP(arr) && !isRP(dep)) { role='arr'; apt=dep||'????'; }
          else if (isRP(dep))         { role='dep'; apt=arr||'????'; }
          else                        { role='oth'; apt=arr||dep||'????'; }
          var type=fp.aircraft_short||fp.aircraft_faa||fp.aircraft||'';
          var sub=(type?type+' ':'')+apt;
          var pop='<div class="lt-pop-cs">'+p.callsign+'</div><div class="lt-pop-rt">'+(dep||'????')+' → '+(arr||'????')+'</div>'
                + '<div class="lt-pop-k">'+(type||'?')+' &middot; '+fmtAlt(p.altitude||0)+' &middot; '+(p.groundspeed||0)+' kt &middot; hdg '+(p.heading||0)+'</div>';
          var rec=markers[p.callsign];
          if (rec){ rec.setLatLng([p.latitude,p.longitude]).setIcon(acIcon(p.heading,role,p.callsign,sub)); rec.getPopup().setContent(pop); }
          else { markers[p.callsign]=L.marker([p.latitude,p.longitude],{icon:acIcon(p.heading,role,p.callsign,sub)}).addTo(acLayer).bindPopup(pop); }
        });
        Object.keys(markers).forEach(function(cs){ if(!seen[cs]){ acLayer.removeLayer(markers[cs]); delete markers[cs]; } });

        // ---- ATC ----
        atcLayer.clearLayers();
        var atc = controllers.filter(function(c){ return /^(RP[A-Z]{2}|MNL)_/i.test(c.callsign) && !/_ATIS$/i.test(c.callsign) && c.frequency && c.frequency!=='199.998'; });
        atc.sort(function(a,b){ return a.callsign<b.callsign?-1:1; });
        var COL={APP:'#4a9eff',DEP:'#4a9eff',TWR:'#00c774',GND:'#c9a2ff',DEL:'#c9a2ff',CTR:'#ffd24a',FSS:'#ffd24a'};
        function atcLabel(ll,col,cs,freq){
          L.marker(ll,{interactive:false,zIndexOffset:800,icon:L.divIcon({className:'',iconSize:[0,0],
            html:'<span class="lt-atc-lbl" style="--c:'+col+'"><span class="cs">'+cs+'</span>'
              +(freq?'<span class="fr">'+freq+'</span>':'')+'</span>'})}).addTo(atcLayer);
        }
        var centres=[];
        atc.forEach(function(c){
          var parts=c.callsign.toUpperCase().split('_'), type=parts[parts.length-1];
          var col=COL[type]||'#4a9eff';
          if (type==='CTR'||type==='FSS'){ centres.push(c); return; }
          var station=parts[0]==='MNL'?'RPLL':parts[0];
          if ((type==='APP'||type==='DEP') && tmaFeat[station]){   // light up the actual TMA sector
            L.geoJSON(tmaFeat[station], { interactive:false, style:{ color:col, weight:2.5, opacity:.95, fillColor:col, fillOpacity:.16 } }).addTo(atcLayer);
            atcLabel(featCentroid(tmaFeat[station]), col, c.callsign, c.frequency);
            return;
          }
          var ll=AP[station]; if(!ll) return;
          var rad={APP:65000,DEP:65000,TWR:9000,GND:4500,DEL:4500}[type]||9000;
          L.circle(ll,{radius:rad,color:col,weight:2,opacity:.95,fillColor:col,fillOpacity:.18,interactive:false}).addTo(atcLayer);
          atcLabel(ll,col,c.callsign,c.frequency);
        });

        // ---- Centre coverage: light only the ACC sub-sectors each CTR actually owns ----
        var CENTRE_COLS=['#ffd24a','#ff9d3c','#ffcf7a','#d9b84a','#ffb861','#e6c34a'];
        var assignedAny=false;
        if (centres.length){
          var onlineCS={}; centres.forEach(function(c){ onlineCS[c.callsign.toUpperCase()]=c; });
          var owned={};   // callsign -> [ring,...]
          if (ACC && ACC.sectors){
            ACC.sectors.forEach(function(sec){
              for (var i=0;i<sec.owners.length;i++){
                var cs=(id2cs[sec.owners[i]]||'').toUpperCase();
                if (cs && onlineCS[cs]){ (owned[cs]=owned[cs]||[]).push(sec.ring); assignedAny=true; break; }
              }
            });
          }
          var ci=0;
          centres.forEach(function(c){
            var cs=c.callsign.toUpperCase(), col=CENTRE_COLS[ci%CENTRE_COLS.length]; ci++;
            var mine=owned[cs];
            if (mine && mine.length){
              var big=null;
              mine.forEach(function(ring){
                L.polygon(ring,{interactive:false,color:col,weight:2,opacity:.9,fillColor:col,fillOpacity:.14}).addTo(atcLayer);
                if(!big||ring.length>big.length) big=ring;
              });
              atcLabel(centroid(big), col, c.callsign, c.frequency);
            } else if (rings.length){   // unknown centre id -> fall back to whole FIR
              L.polygon(rings[0].map(function(p){return [p[1],p[0]];}),{interactive:false,color:col,weight:2,opacity:.85,fillColor:col,fillOpacity:.06}).addTo(atcLayer);
              var ct=centroid(rings[0]); atcLabel([ct[1],ct[0]], col, c.callsign, c.frequency);
            }
          });
        }
        if (boundaryLayer){
          if (centres.length) boundaryLayer.setStyle({ color:'#ffd24a', opacity:.5, weight:1.5, fillColor:'#ffd24a', fillOpacity:0, dashArray:null });
          else boundaryLayer.setStyle({ color:'#4a9eff', opacity:.5, weight:2, fillColor:'#4a9eff', fillOpacity:.02, dashArray:'6,6' });
        }

        var box=document.getElementById('lt-atc');
        box.innerHTML = atc.length ? atc.map(function(c){ return '<div class="lt-atc-card"><div class="lt-atc-cs">'+c.callsign+'</div><div class="lt-atc-nm">'+(c.name||'')+'</div><div class="lt-atc-fq">'+c.frequency+'</div></div>'; }).join('') : '<span class="lt-empty">No Philippine ATC online right now.</span>';
        document.getElementById('lt-air').textContent=air;
        document.getElementById('lt-gnd').textContent=gnd;
        document.getElementById('lt-ctr').textContent=atc.length;
        document.getElementById('lt-updated').textContent='updated '+new Date().toISOString().substr(11,8)+'Z';
      }).catch(function(){
        // keep the last-known aircraft/ATC on screen; just note we're retrying
        var u=document.getElementById('lt-updated'); if(u) u.textContent='reconnecting…';
      });
    }

    document.getElementById('lt-t-traffic').addEventListener('change',function(e){ e.target.checked?map.addLayer(acLayer):map.removeLayer(acLayer); });
    document.getElementById('lt-t-atc').addEventListener('change',function(e){ e.target.checked?map.addLayer(atcLayer):map.removeLayer(atcLayer); });

    refresh();
    var iv=setInterval(refresh,30000);
    var obs=new MutationObserver(function(){ if(!document.body.contains(el)){ clearInterval(iv); obs.disconnect(); } });
    obs.observe(document.body,{ childList:true, subtree:true });
  }
  if (document.readyState==='loading'){ document.addEventListener('DOMContentLoaded',init); } else { init(); }
})();
</script>
