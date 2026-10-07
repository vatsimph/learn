# Airspace Explorer

An interactive map of the airspace in the Manila FIR — the **ACC sector splits**, the **approach / terminal areas (TMA)**, and each aerodrome's **control zone (CTR)**, **aerodrome traffic zone (ATZ)** and **advisory zone (AAZ)**. Toggle the layers with the control at the top-right, and **click any area** for its class, vertical limits and controlling unit/frequency.

<div id="airspace-map" class="as-map"></div>

<div class="as-legend" id="as-legend"></div>

<style>
.as-map {
  height: 640px; border-radius: 10px; margin: 1rem 0 0.7rem;
  border: 1px solid var(--md-default-fg-color--lightest); z-index: 1;
  box-shadow: 0 2px 14px rgba(0,0,0,0.12);
}
/* legend as pills */
.as-legend {
  display: flex; flex-wrap: wrap; gap: 8px 10px; margin-bottom: 1rem;
}
.as-legend span {
  display: inline-flex; align-items: center; gap: 7px; font-size: 0.73rem; font-weight: 600;
  padding: 4px 10px 4px 8px; border-radius: 999px;
  border: 1px solid var(--md-default-fg-color--lightest); background: var(--md-code-bg-color);
  color: var(--md-default-fg-color--light);
}
.as-legend i { width: 13px; height: 13px; border-radius: 50%; display: inline-block; border: 2px solid; }
.as-lcls { display: inline-block; color: #fff; font-weight: 800; font-size: 0.62rem; line-height: 1.5; padding: 0 5px; border-radius: 4px; margin-left: 6px; }
/* aerodrome labels on the map */
.as-lbl {
  font-size: 0.64rem; font-weight: 800; color: #eef3f8; letter-spacing: 0.04em; white-space: nowrap;
  text-shadow: 0 0 3px #000, 0 0 3px #000, 0 0 3px #000; width: auto !important; height: auto !important;
  margin-left: 7px; margin-top: -7px; pointer-events: none;
}
/* popup */
.as-pop { font-size: 0.8rem; line-height: 1.5; color: #e9edf2; min-width: 170px; }
.as-pop b { font-size: 0.9rem; color: #fff; }
.as-pop .as-cls { display: inline-block; font-weight: 700; padding: 1px 6px; border-radius: 4px; margin-left: 6px; color: #fff; font-size: 0.68rem; vertical-align: middle; }
/* override Material's global table chrome inside the dark popup */
.leaflet-popup-content .as-pop table {
  display: table !important; width: 100%; margin: 6px 0 0 !important;
  background: transparent !important; border: 0 !important; box-shadow: none !important;
}
.leaflet-popup-content .as-pop tr { background: transparent !important; border: 0 !important; }
.leaflet-popup-content .as-pop td {
  background: transparent !important; border: 0 !important; padding: 2px 10px 2px 0 !important;
  font-size: 0.78rem; color: #e9edf2;
}
.leaflet-popup-content .as-pop td:first-child { color: #9fb0c0; white-space: nowrap; }
.leaflet-popup-content-wrapper { background: #1c2430; color: #e9edf2; border-radius: 10px; box-shadow: 0 6px 22px rgba(0,0,0,0.45); }
.leaflet-popup-tip { background: #1c2430; }
.leaflet-popup-content { margin: 12px 14px; }
.leaflet-popup-close-button { color: #9fb0c0 !important; }
/* hover tooltip */
.as-tip {
  background: rgba(20,26,35,0.92); border: 1px solid rgba(255,255,255,0.12); color: #eef2f6;
  font-size: 0.7rem; font-weight: 600; letter-spacing: 0.02em; padding: 2px 7px; border-radius: 5px; box-shadow: none;
}
.as-tip::before { display: none; }
/* themed layer control */
.as-map .leaflet-control-layers {
  background: rgba(22,28,38,0.94); color: #dfe6ee; border: 1px solid rgba(255,255,255,0.12);
  border-radius: 9px; box-shadow: 0 4px 16px rgba(0,0,0,0.4); padding: 4px 6px;
}
.as-map .leaflet-control-layers-list { font-size: 0.78rem; }
.as-map .leaflet-control-layers label { margin: 3px 0; display: flex; align-items: center; gap: 7px; cursor: pointer; }
.as-map .leaflet-control-layers-selector { margin: 0; accent-color: #e0b84d; }
.as-map .leaflet-bar a { background: #1c2430; color: #dfe6ee; border-color: rgba(255,255,255,0.12); }
.as-map .leaflet-bar a:hover { background: #26303f; }
</style>

<script>
(function () {
  var MNL_FREQ = {
    MNL_CTR:"119.300", MNL_C_CTR:"132.075", MNL_N_CTR:"126.575", MNL_S_CTR:"133.500",
    MNL_2_CTR:"124.950", MNL_CN_CTR:"120.500", MNL_CE_CTR:"128.750", MNL_CS_CTR:"125.700",
    MNL_CW_CTR:"132.700", MNL_NE_RDO:"132.500", MNL_NW_CTR:"128.700", MNL_SE_CTR:"125.750",
    MNL_SW_CTR:"124.900", MNL_W_CTR:"118.900", MNL_N1_CTR:"129.000", MNL_S1_CTR:"131.500"
  };
  var TMA_FREQ = {
    RPLL:"124.800", RPLI:"122.300", RPLC:"119.200", RPLK:"120.200", RPMD:"122.400",
    RPME:"121.300", RPMR:"119.100", RPMY:"125.500", RPVA:"120.800", RPVB:"121.000",
    RPVK:"120.400", RPVM:"124.700", RPVP:"122.000"
  };
  // colour per layer  [stroke, fill]
  var COL = {
    fir: ["#c3ccd6", "transparent"],
    sector: ["#e6c25a", "#e6c25a"],
    tma: ["#a883ff", "#a883ff"],
    CTR: ["#f0953e", "#f0953e"],
    ATZ: ["#5a9bed", "#5a9bed"],
    AAZ: ["#44c07d", "#44c07d"]
  };
  function hover(layer, w, fo) {
    layer.on("mouseover", function () { this.setStyle({ weight: w + 1.6, fillOpacity: Math.min(fo + 0.16, 0.4) }); });
    layer.on("mouseout",  function () { this.setStyle({ weight: w, fillOpacity: fo }); });
  }
  var CLSCOL = { A:"#b03a3a", B:"#2f6fb0", C:"#2f8f8f", D:"#6a4ea8", E:"#888", F:"#999", G:"#3f8f55" };

  function clsBadge(c) { return '<span class="as-cls" style="background:' + (CLSCOL[c]||"#777") + '">Class ' + c + '</span>'; }
  function freqRow(unit, freq) {
    if (!freq) return "";
    return '<tr><td>' + (unit || "Controlled by") + '</td><td><b>' + freq + '</b> MHz</td></tr>';
  }

  function run() {
    var L = window.L;
    var el = document.getElementById("airspace-map");
    if (!L || !el || el._leaflet_id) return;

    var map = L.map(el, { center: [12.6, 122.9], zoom: 6, zoomControl: true, attributionControl: true });
    // clean label-free dark base (Esri dark gray, no reference labels) — we add our own aerodrome labels below
    L.tileLayer("https://services.arcgisonline.com/arcgis/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{z}/{y}/{x}",
      { attribution: 'Tiles &copy; <a href="https://www.esri.com/">Esri</a>', maxZoom: 16 }).addTo(map);

    function j(name) { return fetch("../../assets/data/" + name).then(function (r) { return r.ok ? r.json() : null; }).catch(function () { return null; }); }
    function tip() { return { permanent: false, direction: "top", className: "as-tip", opacity: 1, sticky: false, offset: [0, -2] }; }

    var layers = {
      fir: L.layerGroup(), sector: L.layerGroup(), tma: L.layerGroup(),
      CTR: L.layerGroup(), ATZ: L.layerGroup(), AAZ: L.layerGroup()
    };
    var labels = L.layerGroup();          // aerodrome ICAO labels (zoom-gated)
    var labelPts = {};                    // icao -> [lat,lon]

    Promise.all([j("mnl_boundary.json"), j("acc_sectors.json"), j("tmas.json"), j("airspace_zones.json")])
      .then(function (res) {
        var fir = res[0], acc = res[1], tmas = res[2], az = res[3];

        // --- FIR boundary ---
        if (fir) L.geoJSON(fir, { style: { color: COL.fir[0], weight: 1.5, dashArray: "6 5", fill: false } })
          .bindPopup('<div class="as-pop"><b>Manila FIR</b><br>Flight information region boundary</div>')
          .addTo(layers.fir);

        // --- ACC sectors (overlapping; draw larger first so small ones sit on top) ---
        if (acc && acc.sectors) {
          var secs = acc.sectors.slice().sort(function (a, b) { return (b.ring ? b.ring.length : 0) - (a.ring ? a.ring.length : 0); });
          secs.forEach(function (s) {
            if (!s.ring || !s.ring.length) return;
            var abbr = (s.owners && s.owners[0]) || "";
            var cs = acc.posmap ? acc.posmap[abbr] : null;
            var freq = cs ? MNL_FREQ[cs] : null;
            var pg = L.polygon(s.ring, { color: COL.sector[0], weight: 1, fillColor: COL.sector[1], fillOpacity: 0.05 })
              .bindPopup('<div class="as-pop"><b>' + s.name + '</b>' + clsBadge("A") +
                '<table><tr><td>Unit</td><td>Manila Control</td></tr>' + freqRow("Primary", freq) +
                '<tr><td>Levels</td><td>upper control area</td></tr></table></div>')
              .bindTooltip(s.name, tip());
            hover(pg, 1, 0.05);
            pg.addTo(layers.sector);
          });
        }

        // --- TMAs ---
        if (tmas && tmas.features) {
          tmas.features.forEach(function (ft) {
            var id = ft.properties.id, nm = ft.properties.name;
            var g = L.geoJSON(ft, { style: { color: COL.tma[0], weight: 1.4, fillColor: COL.tma[1], fillOpacity: 0.09 } })
              .bindPopup('<div class="as-pop"><b>' + nm + '</b>' + clsBadge("D") +
                '<table><tr><td>Type</td><td>Terminal control area</td></tr>' +
                '<tr><td>Levels</td><td>1500 FT – FL200</td></tr>' +
                freqRow(nm, TMA_FREQ[id]) + '</table></div>')
              .bindTooltip(nm + " · Class D", tip());
            hover(g, 1.4, 0.09);
            g.addTo(layers.tma);
          });
        }

        // --- aerodrome CTR / ATZ / AAZ circles ---
        if (az && az.zones) {
          az.zones.forEach(function (z) {
            var c = COL[z.type] || ["#999", "#999"];
            var fo = z.type === "CTR" ? 0.08 : 0.13;
            var sh;
            if (z.geom === "polygon") {
              sh = L.polygon(z.coords, { color: c[0], weight: 1.4, fillColor: c[1], fillOpacity: fo });
            } else {
              sh = L.circle(z.center, { radius: z.radiusNm * 1852, color: c[0], weight: 1.4, fillColor: c[1], fillOpacity: fo });
              if (!labelPts[z.icao]) labelPts[z.icao] = z.center;   // one label per aerodrome
            }
            sh.bindPopup('<div class="as-pop"><b>' + z.icao + " — " + z.name + '</b>' + clsBadge(z["class"]) +
                '<table><tr><td>Type</td><td>' + z.typeName + ' (' + z.type + ')</td></tr>' +
                '<tr><td>Levels</td><td>' + z.lower + ' – ' + z.upper + '</td></tr>' +
                (z.geom === "circle" ? '<tr><td>Radius</td><td>' + z.radiusNm + ' NM</td></tr>' : '') +
                freqRow(z.unit, z.freq) + '</table></div>')
              .bindTooltip(z.icao + " " + z.type, tip());
            hover(sh, 1.4, fo);
            sh.addTo(layers[z.type]);
          });
        }

        // aerodrome ICAO labels (one per field, shown when zoomed in)
        Object.keys(labelPts).forEach(function (ic) {
          L.marker(labelPts[ic], {
            icon: L.divIcon({ className: "as-lbl", html: ic, iconSize: null }),
            interactive: false, keyboard: false
          }).addTo(labels);
        });
        function syncLabels() {
          if (map.getZoom() >= 7) { if (!map.hasLayer(labels)) labels.addTo(map); }
          else if (map.hasLayer(labels)) map.removeLayer(labels);
        }
        map.on("zoomend", syncLabels); syncLabels();

        // add overlays + control (ACC sectors off by default to reduce clutter)
        layers.fir.addTo(map); layers.tma.addTo(map);
        layers.CTR.addTo(map); layers.ATZ.addTo(map); layers.AAZ.addTo(map);
        L.control.layers(null, {
          "Manila FIR": layers.fir,
          "ACC sectors": layers.sector,
          "TMA (Approach)": layers.tma,
          "Control zones (CTR)": layers.CTR,
          "Traffic zones (ATZ)": layers.ATZ,
          "Advisory zones (AAZ)": layers.AAZ
        }, { collapsed: false, position: "topright" }).addTo(map);

        // legend — colour swatch · what it is · class chip
        var LEG = [
          ["CTR", "Control zone", "D"], ["ATZ", "Traffic zone", "B"], ["AAZ", "Advisory zone", "G"],
          ["tma", "Terminal area", "D"], ["sector", "ACC sector", "A"]
        ];
        var leg = document.getElementById("as-legend");
        if (leg) leg.innerHTML = LEG.map(function (p) {
          return '<span><i style="border-color:' + COL[p[0]][0] + ';background:' + COL[p[0]][1] + '33"></i>' +
                 p[1] + '<b class="as-lcls" style="background:' + (CLSCOL[p[2]] || "#777") + '">' + p[2] + '</b></span>';
        }).join("");
      });

    setTimeout(function () { map.invalidateSize(); }, 200);
  }

  if (window.document$ && typeof window.document$.subscribe === "function") window.document$.subscribe(run);
  else if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run);
  else run();
})();
</script>

*[FIR]: Flight Information Region
*[TMA]: Terminal Control Area
*[CTR]: Control Zone
*[ATZ]: Aerodrome Traffic Zone
*[AAZ]: Aerodrome Advisory Zone
*[ACC]: Area Control Centre
