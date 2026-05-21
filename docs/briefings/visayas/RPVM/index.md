# RPVM - Mactan - Cebu International Airport

<div class="metar-widget" data-icao="RPVM">
<style>
.metar-widget {
  margin: 1rem 0;
}
.metar-card {
  display: flex;
  flex-direction: column;
  gap: 0.45rem;
  padding: 0.75rem 1rem;
  border: 1px solid var(--md-default-fg-color--lightest);
  border-left: 4px solid var(--md-primary-fg-color, #4051b5);
  border-radius: 4px;
  background: var(--md-code-bg-color);
}
.metar-raw {
  font-family: var(--md-code-font, monospace);
  font-size: 0.75rem;
  line-height: 1.7;
  color: var(--md-default-fg-color);
  white-space: pre-wrap;
  letter-spacing: 0.02em;
}
.metar-loading {
  font-size: 0.75rem;
  color: var(--md-default-fg-color--light);
  letter-spacing: 0.04em;
  padding: 0.25rem 0;
}
</style>

<div class="metar-loading" id="metar-loading-RPVM">Fetching METAR...</div>
<div class="metar-card" id="metar-card-RPVM" style="display:none;"></div>
</div>

<script>
(function () {
  var ICAO = "RPVM";
  var loadingEl = document.getElementById("metar-loading-" + ICAO);
  var cardEl    = document.getElementById("metar-card-" + ICAO);

  function render(metar) {
    cardEl.innerHTML = '<div class="metar-raw">' + metar + '</div>';
    cardEl.style.display = "";
    loadingEl.style.display = "none";
  }

  function renderError(msg) {
    cardEl.innerHTML = '<div class="metar-raw" style="color:#b71c1c;">' + msg + '</div>';
    cardEl.style.display = "";
    loadingEl.style.display = "none";
  }

  function fetchMetar() {
    fetch("https://metar.vatsim.net/" + ICAO + "?format=json")
      .then(function(r) {
        if (!r.ok) throw new Error("HTTP " + r.status);
        return r.json();
      })
      .then(function(data) {
        if (!data || !data.length || !data[0].metar) {
          renderError("No METAR available for " + ICAO + ".");
          return;
        }
        render(data[0].metar);
      })
      .catch(function(e) {
        renderError(e.message || "Network error.");
      });
  }

  fetchMetar();
  setInterval(fetchMetar, 5000);
})();
</script>

## General
The Mactan - Cebu International Airport has 2 Runways, 2 passenger terminals, 1 general aviation areas, 1 military airbase, and 1 military maintenance hangar.

- Terminal 1 - Domestic Passenger and Cargo Flights 
- Terminal 2 - International Passenger and Cargo Flights

The airport caters passenger and cargo flights, as well as general and military aviation.

## Charts
[RPVM](https://vatphil.com/charts?icao=RPVM){ .md-button .md-button--primary }

## Frequency List
<table>
  <thead>
    <tr>
      <th style="text-align:center">Designator</th>
      <th style="text-align:center">Callsign</th>
      <th style="text-align:center">Frequency</th>
      <th style="text-align:center">Remarks</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:center"><strong>RPVM_ATIS</strong></td>
      <td style="text-align:center"></td>
      <td style="text-align:center">126.600</td>
      <td style="text-align:center">Every hour</td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>RPVM_DEL</strong></td>
      <td style="text-align:center">Clearance Delivery</td>
      <td style="text-align:center">126.600</td>
      <td style="text-align:center"></td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>RPVM_GND</strong></td>
      <td style="text-align:center">Mactan Ground</td>
      <td style="text-align:center">121.800</td>
      <td style="text-align:center"></td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>RPVM_TWR</strong></td>
      <td style="text-align:center">Mactan Tower</td>
      <td style="text-align:center">118.100</td>
      <td style="text-align:center"></td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>RPVM_APP</strong></td>
      <td rowspan="2" style="text-align:center">Mactan Approach[^2]</td>
      <td style="text-align:center">124.700</td>
      <td style="text-align:center">TMA 1500 ft - FL150[^1]</td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>RPVM_S_APP</strong></td>
      <td style="text-align:center">121.200</td>
      <td style="text-align:center">SUB TMA 1500 ft - FL150[^1]</td>
    </tr>
  </tbody>
</table>

[^1]: Vertical limit of FL150 can be increased to a maximum of FL200.
[^2]: Can control top-down Mactan TMA which includes RPVD and RPSP. But check the controller information if they do!


## Stand Assignments

Bay assignments, are strictly implemented virtually, and are based on the latest real-world operations. Virtual and other real-world airlines that are not listed will park at terminal 2.

<!DOCTYPE html>
<html>
<head>
    <title>Mactan-Cebu Stand Finder</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <style>
        #sf-root {
            all: initial;
            display: block;
            font-family: 'Mulish', system-ui, -apple-system, sans-serif;
            box-sizing: border-box;
            color: #e8e6dc;
            background: transparent;
            position: relative;
            --sf-gold: #8c7804;
            --sf-gold-light: #d9d61c;
            --sf-panel-bg: rgba(15, 17, 25, 0.94);
            --sf-text: #e8e6dc;
            --sf-text-muted: rgba(232, 230, 220, 0.55);
        }
        #sf-root *, #sf-root *::before, #sf-root *::after {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: inherit;
        }

        #sf-root #wrapper {
            position: relative;
            width: 100%;
            height: 600px;
            border-radius: 8px;
            overflow: hidden;
            z-index: 0;
            isolation: isolate;
            border: 1px solid rgba(140, 120, 4, 0.3);
            box-shadow: 0 2px 12px rgba(0, 0, 0, 0.15);
        }

        #sf-root #map {
            height: 100%;
            width: 100%;
        }

        #sf-root #panel {
            position: absolute;
            top: 12px;
            left: 12px;
            z-index: 10;
            background: var(--sf-panel-bg);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-left: 3px solid var(--sf-gold);
            border-radius: 6px;
            padding: 12px 14px;
            width: 280px;
            display: flex;
            flex-direction: column;
            gap: 10px;
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.35);
        }

        #sf-root .sf-title {
            font-size: 11px;
            font-weight: 700;
            color: var(--sf-text);
            letter-spacing: 0.1em;
            line-height: 1.45;
            text-transform: uppercase;
        }

        #sf-root .sf-row {
            display: flex;
            gap: 6px;
        }

        #sf-root #standInput {
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 4px;
            color: var(--sf-text);
            font-size: 13px;
            padding: 7px 10px;
            outline: none;
            flex: 1;
            line-height: normal;
            height: auto;
            width: auto;
            min-height: 0;
            box-shadow: none;
            -webkit-appearance: none;
            appearance: none;
            transition: border-color 0.15s, background 0.15s, box-shadow 0.15s;
        }

        #sf-root #standInput::placeholder {
            color: rgba(232, 230, 220, 0.4);
        }

        #sf-root #standInput:focus {
            border-color: var(--sf-gold-light);
            background: rgba(255, 255, 255, 0.07);
            box-shadow: 0 0 0 2px rgba(217, 214, 28, 0.18);
        }

        #sf-root #goBtn {
            background: var(--sf-gold);
            border: 1px solid var(--sf-gold);
            border-radius: 4px;
            color: #1a1a1a;
            cursor: pointer;
            font-size: 11px;
            font-weight: 700;
            padding: 7px 14px;
            line-height: normal;
            height: auto;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            box-shadow: none;
            transition: background 0.15s, border-color 0.15s;
            -webkit-appearance: none;
            appearance: none;
        }

        #sf-root #goBtn:hover {
            background: var(--sf-gold-light);
            border-color: var(--sf-gold-light);
        }

        #sf-root .sf-legend {
            display: flex;
            flex-direction: column;
            gap: 6px;
            border-top: 1px solid rgba(255, 255, 255, 0.08);
            padding-top: 10px;
            margin-top: 2px;
        }

        #sf-root .sf-leg-row {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 11px;
            color: rgba(232, 230, 220, 0.8);
            line-height: 1.4;
        }

        #sf-root .sf-dot {
            width: 9px;
            height: 9px;
            border-radius: 50%;
            flex-shrink: 0;
            display: inline-block;
            box-shadow: 0 0 0 2px rgba(255, 255, 255, 0.05);
        }

        #sf-root .leaflet-tooltip {
            background: rgba(15, 17, 25, 0.95);
            border: 1px solid rgba(140, 120, 4, 0.6);
            color: var(--sf-gold-light);
            font-size: 11px;
            font-weight: 700;
            padding: 3px 8px;
            border-radius: 3px;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.35);
            letter-spacing: 0.04em;
        }

        #sf-root .leaflet-tooltip-top::before,
        #sf-root .leaflet-tooltip-bottom::before,
        #sf-root .leaflet-tooltip-left::before,
        #sf-root .leaflet-tooltip-right::before {
            border: none !important;
            display: none !important;
        }

        #sf-root .leaflet-popup-content-wrapper {
            background: rgba(15, 17, 25, 0.97);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-top: 3px solid var(--pop-col, var(--sf-gold));
            color: var(--sf-text);
            border-radius: 6px;
            box-shadow: 0 6px 22px rgba(0, 0, 0, 0.55);
        }

        .sf-pop-t1  { --pop-col: #ff9900; --pop-col-bg: rgba(255,153,0,0.16);  --pop-col-bd: rgba(255,153,0,0.45); }
        .sf-pop-com { --pop-col: #8aa9ff; --pop-col-bg: rgba(138,169,255,0.16);--pop-col-bd: rgba(138,169,255,0.45); }
        .sf-pop-rpa { --pop-col: #00e096; --pop-col-bg: rgba(0,224,150,0.16);  --pop-col-bd: rgba(0,224,150,0.45); }
        .sf-pop-t2  { --pop-col: #00a8ff; --pop-col-bg: rgba(0,168,255,0.16);  --pop-col-bd: rgba(0,168,255,0.45); }

        #sf-root .leaflet-popup-tip {
            background: rgba(15, 17, 25, 0.97);
        }

        #sf-root .leaflet-popup-content {
            margin: 12px 16px;
            font-size: 12px;
            line-height: 1.6;
            color: var(--sf-text);
        }

        #sf-root .pop-stand {
            font-size: 18px;
            font-weight: 700;
            color: var(--pop-col, var(--sf-gold-light));
            letter-spacing: 0.02em;
        }

        #sf-root .pop-term {
            font-size: 10px;
            color: var(--sf-text-muted);
            margin-bottom: 8px;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            font-weight: 600;
        }

        #sf-root .pop-lbl {
            font-size: 9px;
            color: rgba(232, 230, 220, 0.5);
            text-transform: uppercase;
            letter-spacing: 0.1em;
            margin-top: 9px;
            font-weight: 700;
        }

        #sf-root .pop-val {
            color: var(--sf-text);
            font-size: 12px;
            margin-top: 2px;
        }

        #sf-root .atag {
            display: inline-block;
            background: var(--pop-col-bg, rgba(140, 120, 4, 0.18));
            border: 1px solid var(--pop-col-bd, rgba(140, 120, 4, 0.45));
            border-radius: 3px;
            color: var(--pop-col, var(--sf-gold-light));
            font-size: 10px;
            font-weight: 600;
            padding: 2px 6px;
            margin: 3px 3px 0 0;
            text-decoration: none;
            line-height: 1.4;
            letter-spacing: 0.03em;
        }

        @media (max-width: 520px) {
            #sf-root #panel {
                width: calc(100% - 24px);
                max-width: 280px;
            }
        }
    </style>
</head>
<body>

<div id="sf-root">
    <div id="panel">
        <div class="sf-title">Mactan-Cebu International Airport Stand Finder</div>
        <div class="sf-row">
            <input type="text" id="standInput" placeholder="Stand or airline (e.g. B1, PAL)" onkeypress="if(event.key==='Enter') searchStand()">
            <button id="goBtn" onclick="searchStand()">Go</button>
        </div>
        <div class="sf-legend">
            <div class="sf-leg-row"><span class="sf-dot" style="background:#ff9900"></span>Terminal 1 (Domestic)</div>
            <div class="sf-leg-row"><span class="sf-dot" style="background:#8aa9ff"></span>Northeast Apron</div>
            <div class="sf-leg-row"><span class="sf-dot" style="background:#00e096"></span>Remote Apron</div>
            <div class="sf-leg-row"><span class="sf-dot" style="background:#00a8ff"></span>Terminal 2 (International)</div>
        </div>
    </div>
    <div id="wrapper">
        <div id="map"></div>
    </div>
</div>

<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
var map = L.map('map', {zoomControl:false}).setView([10.3145, 123.9795], 16);
L.control.zoom({position:'bottomright'}).addTo(map);
L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {attribution:'© OpenStreetMap © CARTO'}).addTo(map);

map.on('popupopen', function(e){
    var btn = e.popup._container && e.popup._container.querySelector('.leaflet-popup-close-button');
    if(btn){
        btn.removeAttribute('href');
        btn.setAttribute('role','button');
        btn.style.cursor = 'pointer';
    }
});

function parseCoord(s) {
    var dir = s.slice(-1);
    var num = s.slice(0,-1);
    var isLng = (dir==='E'||dir==='W');
    var dLen = isLng ? 3 : 2;
    var d = parseFloat(num.slice(0,dLen));
    var m = parseFloat(num.slice(dLen,dLen+2));
    var sec = parseFloat(num.slice(dLen+2));
    var dec = d + m/60 + sec/3600;
    return (dir==='S'||dir==='W') ? -dec : dec;
}

// Airline groupings — _T1/_T2 suffixes denote domestic-only / international-only
// per the assignment table; normalizeAirline() strips them for search matching.
var T1  = ["PAL_T1","CEB_T1","SRQ","APG_T1","RLB"];
var RPA = ["PAL","CEB","SRQ","APG","RLB"];
var T2  = ["PAL_T2","CEB_T2","SRQ","APG_T2","RLB","ABL","JNA","JJA","AAR","HVN","UAL","CES","KAL","JST","SJX","CPA","UAE","QTR","TWB","TGW","EVA","SIA"];
var COM = [];

var T1_ACFT = "A300, A319, A320, A330, A340, B737, B747, B777, DC10, MD-11, MD-80, MD-82";
var RPA_ACFT_WB = "A300, A319, A320, A330, A340, B737, B747, B777, DC10, MD-11, MD-80, MD-82";
var T2_ACFT_E = "A330, A340, B747, B757, B767, B777";
var CODE_C = "A319, A320, A321, B737";

var stands = [
    // Terminal 1 (Northeast Apron contact bays)
    {id:"B1", lat:parseCoord("101851.28N"), lng:parseCoord("1235841.62E"), t:"T1",  acft:T1_ACFT, al:T1},
    {id:"B2", lat:parseCoord("101852.94N"), lng:parseCoord("1235843.31E"), t:"T1",  acft:T1_ACFT, al:T1},
    {id:"B3", lat:parseCoord("101854.63N"), lng:parseCoord("1235844.99E"), t:"T1",  acft:T1_ACFT, al:T1},
    {id:"B4", lat:parseCoord("101856.28N"), lng:parseCoord("1235846.65E"), t:"T1",  acft:T1_ACFT, al:T1},
    {id:"B5", lat:parseCoord("101857.97N"), lng:parseCoord("1235848.34E"), t:"T1",  acft:T1_ACFT, al:T1},
    {id:"B6", lat:parseCoord("101859.32N"), lng:parseCoord("1235849.95E"), t:"T1",  acft:"B737-800 and lower aircraft category", al:T1},

    // Commuter stands (Northeast Apron — C1-C5R, R50 cluster)
    {id:"C1",   lat:parseCoord("101904.77N"), lng:parseCoord("1235855.48E"), t:"COM", acft:"A319, A320, A321, B737-800", al:COM},
    {id:"C1L",  lat:parseCoord("101904.45N"), lng:parseCoord("1235854.45E"), t:"COM", acft:"Q400, ATR72 and lower category", al:COM},
    {id:"C1R",  lat:parseCoord("101905.27N"), lng:parseCoord("1235855.80E"), t:"COM", acft:"Q400, ATR72 and lower category", al:COM},
    {id:"C2",   lat:parseCoord("101903.74N"), lng:parseCoord("1235853.81E"), t:"COM", acft:"A319, A320, A321, B737-800", al:COM},
    {id:"C2L",  lat:parseCoord("101903.66N"), lng:parseCoord("1235853.66E"), t:"COM", acft:"Q400, ATR72 and lower category", al:COM},
    {id:"C3",   lat:parseCoord("101902.70N"), lng:parseCoord("1235852.76E"), t:"COM", acft:"A319, A320, A321, B737-800", al:COM},
    {id:"C3R",  lat:parseCoord("101902.88N"), lng:parseCoord("1235852.87E"), t:"COM", acft:"Q400, ATR72 and lower category", al:COM},
    {id:"C4",   lat:parseCoord("101901.67N"), lng:parseCoord("1235851.72E"), t:"COM", acft:"A319, A320, A321, B737-800", al:COM},
    {id:"C4R",  lat:parseCoord("101902.09N"), lng:parseCoord("1235852.08E"), t:"COM", acft:"ATR72, Q400", al:COM},
    {id:"C5R",  lat:parseCoord("101901.31N"), lng:parseCoord("1235851.29E"), t:"COM", acft:"ATR72, Q400", al:COM},
    {id:"R50",  lat:parseCoord("101903.79N"), lng:parseCoord("1235857.55E"), t:"COM", acft:"A319, A320, A321, B737-800", al:COM},
    {id:"R50L", lat:parseCoord("101904.59N"), lng:parseCoord("1235856.98E"), t:"COM", acft:"Q400, ATR72 and lower category", al:COM},
    {id:"R50R", lat:parseCoord("101903.66N"), lng:parseCoord("1235857.92E"), t:"COM", acft:"Q400, ATR72 and lower category", al:COM},

    // Remote Apron (bays 11-16)
    {id:"11",  lat:parseCoord("101848.35N"), lng:parseCoord("1235847.89E"), t:"RPA", acft:"B737, F50", al:RPA},
    {id:"11A", lat:parseCoord("101849.05N"), lng:parseCoord("1235848.13E"), t:"RPA", acft:RPA_ACFT_WB, al:RPA},
    {id:"12",  lat:parseCoord("101849.19N"), lng:parseCoord("1235848.73E"), t:"RPA", acft:"B737, F50", al:RPA},
    {id:"13",  lat:parseCoord("101850.28N"), lng:parseCoord("1235849.82E"), t:"RPA", acft:"B737, F50", al:RPA},
    {id:"13A", lat:parseCoord("101850.96N"), lng:parseCoord("1235850.06E"), t:"RPA", acft:RPA_ACFT_WB, al:RPA},
    {id:"14",  lat:parseCoord("101851.12N"), lng:parseCoord("1235850.67E"), t:"RPA", acft:"B737, F50", al:RPA},
    {id:"15",  lat:parseCoord("101852.21N"), lng:parseCoord("1235851.76E"), t:"RPA", acft:"B737, F50", al:RPA},
    {id:"15A", lat:parseCoord("101852.83N"), lng:parseCoord("1235852.00E"), t:"RPA", acft:RPA_ACFT_WB, al:RPA},
    {id:"16",  lat:parseCoord("101853.05N"), lng:parseCoord("1235852.60E"), t:"RPA", acft:"B737, F50", al:RPA},

    // Terminal 2 (Southwest Apron)
    {id:"C12C", lat:parseCoord("101849.48N"), lng:parseCoord("1235839.78E"), t:"T2", acft:T2_ACFT_E, al:T2},
    {id:"C12L", lat:parseCoord("101848.53N"), lng:parseCoord("1235839.56E"), t:"T2", acft:CODE_C, al:T2},
    {id:"C12R", lat:parseCoord("101849.83N"), lng:parseCoord("1235840.05E"), t:"T2", acft:CODE_C, al:T2},
    {id:"C13C", lat:parseCoord("101846.01N"), lng:parseCoord("1235838.41E"), t:"T2", acft:T2_ACFT_E, al:T2},
    {id:"C13L", lat:parseCoord("101845.25N"), lng:parseCoord("1235839.60E"), t:"T2", acft:CODE_C, al:T2},
    {id:"C13R", lat:parseCoord("101846.48N"), lng:parseCoord("1235838.57E"), t:"T2", acft:CODE_C, al:T2},
    {id:"C14",  lat:parseCoord("101843.71N"), lng:parseCoord("1235840.42E"), t:"T2", acft:CODE_C, al:T2},
    {id:"C15",  lat:parseCoord("101842.85N"), lng:parseCoord("1235841.43E"), t:"T2", acft:CODE_C, al:T2},
    {id:"C16",  lat:parseCoord("101842.74N"), lng:parseCoord("1235842.15E"), t:"T2", acft:T2_ACFT_E, al:T2},
    {id:"C17",  lat:parseCoord("101842.16N"), lng:parseCoord("1235842.60E"), t:"T2", acft:CODE_C, al:T2},
    {id:"C18",  lat:parseCoord("101839.88N"), lng:parseCoord("1235840.31E"), t:"T2", acft:CODE_C, al:T2},
    {id:"C19",  lat:parseCoord("101840.80N"), lng:parseCoord("1235839.37E"), t:"T2", acft:CODE_C, al:T2},
    {id:"C20",  lat:parseCoord("101841.72N"), lng:parseCoord("1235838.43E"), t:"T2", acft:CODE_C, al:T2},
    {id:"C21",  lat:parseCoord("101842.65N"), lng:parseCoord("1235837.49E"), t:"T2", acft:CODE_C, al:T2},
    {id:"C22",  lat:parseCoord("101843.70N"), lng:parseCoord("1235836.17E"), t:"T2", acft:CODE_C, al:T2},
    {id:"C23",  lat:parseCoord("101843.76N"), lng:parseCoord("1235834.44E"), t:"T2", acft:CODE_C, al:T2},
    {id:"R75",  lat:parseCoord("101842.92N"), lng:parseCoord("1235832.99E"), t:"T2", acft:CODE_C, al:T2}
];

var tCol = {"T1":"#ff9900","COM":"#8aa9ff","RPA":"#00e096","T2":"#00a8ff"};
var tLbl = {"T1":"Terminal 1 (Domestic)","COM":"Northeast Apron","RPA":"Remote Apron","T2":"Terminal 2 (International)"};
var standMarkers = {};

stands.forEach(function(s){
    var col = tCol[s.t]||"#8c7804";
    var m = L.circleMarker([s.lat,s.lng],{radius:5,fillColor:col,color:"#000",weight:1,fillOpacity:0.9}).addTo(map);
    var tags = s.al.length
        ? s.al.map(function(a){return '<span class="atag">'+a.replace(/_T[12]$|_CGO$/,'')+'</span>';}).join('')
        : '<span class="pop-val" style="opacity:0.6">No published airline assignment</span>';
    m.bindPopup(
        '<div class="pop-stand">Stand '+s.id+'</div><div class="pop-term">'+tLbl[s.t]+'</div><div class="pop-lbl">Aircraft Types</div><div class="pop-val">'+s.acft+'</div><div class="pop-lbl">Airlines</div><div>'+tags+'</div>',
        {
            maxWidth: 300,
            offset: [0, -8],
            autoPan: true,
            autoPanPaddingTopLeft: [320, 80],
            autoPanPaddingBottomRight: [40, 80],
            className: 'sf-pop-' + s.t.toLowerCase()
        }
    );
    m.bindTooltip('Stand '+s.id,{sticky:true,direction:'top',offset:[0,-6]});
    standMarkers[s.id.toUpperCase()] = {marker:m, stand:s, defCol:col};
});

function resetMarkerStyles(){
    Object.keys(standMarkers).forEach(function(k){
        var rec = standMarkers[k];
        rec.marker.setStyle({
            radius: 5,
            fillColor: rec.defCol,
            color: "#000",
            weight: 1,
            fillOpacity: 0.9,
            opacity: 1
        });
    });
}

function normalizeAirline(code){
    return code.replace(/_T[12]$|_CGO$/, '').toUpperCase();
}

function searchStand(){
    var v = document.getElementById('standInput').value.trim().toUpperCase();
    resetMarkerStyles();
    if(!v) return;

    if(standMarkers[v]){
        map.closePopup();
        map.setView(standMarkers[v].marker.getLatLng(), 18);
        standMarkers[v].marker.openPopup();
        return;
    }

    var matches = [];
    Object.keys(standMarkers).forEach(function(k){
        var rec = standMarkers[k];
        var airlines = rec.stand.al.map(normalizeAirline);
        if(airlines.indexOf(v) !== -1) matches.push(rec);
    });

    if(matches.length === 0){
        alert('No stand or airline matches "' + v + '".');
        return;
    }

    Object.keys(standMarkers).forEach(function(k){
        var rec = standMarkers[k];
        if(matches.indexOf(rec) === -1){
            rec.marker.setStyle({fillOpacity: 0.15, opacity: 0.25});
        }
    });

    matches.forEach(function(rec){
        rec.marker.setStyle({
            radius: 8,
            fillColor: '#d9d61c',
            color: '#8c7804',
            weight: 2,
            fillOpacity: 1,
            opacity: 1
        });
        rec.marker.bringToFront();
    });

    map.closePopup();
    var bounds = L.latLngBounds(matches.map(function(r){ return r.marker.getLatLng(); }));
    if(matches.length === 1){
        map.setView(matches[0].marker.getLatLng(), 18);
        matches[0].marker.openPopup();
    } else {
        map.fitBounds(bounds, {
            paddingTopLeft: [320, 60],
            paddingBottomRight: [40, 60],
            maxZoom: 17
        });
    }
}
</script>
</body>
</html>

<iframe src="../../../assets/pdfs/RPVMstands.pdf" width="70%" height="500px"></iframe>

## Runways

<div markdown="1">
Mactan currently has 2 runways .

Primary Runway (04R/22L) : **0930Z** - **1930Z**

Secondary (04L/22R) : **1930Z** - **0930Z** (+1 day) 
</div>

<div class="rwy-schedule">
<style>
.rwy-schedule {
  margin: 1rem 0 1.5rem;
  padding: 0.9rem 1rem 1rem;
  border: 1px solid var(--md-default-fg-color--lightest);
  border-left: 4px solid var(--md-primary-fg-color);
  border-radius: 4px;
  background: var(--md-code-bg-color);
  color: var(--md-default-fg-color);
  font-size: 0.8rem;
}
.rwy-schedule * { box-sizing: border-box; }

.rwy-schedule .rs-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  margin-bottom: 0.75rem;
  padding-bottom: 0.6rem;
  border-bottom: 1px solid var(--md-default-fg-color--lightest);
}
.rwy-schedule .rs-title {
  font-size: 0.7rem;
  font-weight: 700;
  color: var(--md-default-fg-color--light);
  letter-spacing: 0.08em;
  text-transform: uppercase;
}
.rwy-schedule .rs-clock {
  font-family: var(--md-code-font, monospace);
  font-size: 1.1rem;
  font-weight: 500;
  color: var(--md-default-fg-color);
  letter-spacing: 0.04em;
  text-align: right;
}
.rwy-schedule .rs-clock-label {
  font-size: 0.6rem;
  color: var(--md-default-fg-color--lighter);
  text-align: right;
  margin-top: 2px;
  letter-spacing: 0.06em;
}

.rwy-schedule .rs-legend {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  margin-bottom: 0.75rem;
}
.rwy-schedule .rs-legend-item {
  display: flex;
  align-items: center;
  gap: 0.35rem;
  font-size: 0.7rem;
  color: var(--md-default-fg-color--light);
}
.rwy-schedule .rs-legend-box {
  width: 12px;
  height: 12px;
  border-radius: 3px;
}
.rwy-schedule .rs-legend-line {
  width: 12px;
  height: 2px;
  background: #e53935;
  border-radius: 1px;
}

.rwy-schedule .rs-row {
  display: grid;
  grid-template-columns: 110px 1fr;
  gap: 0.75rem;
  align-items: center;
  margin-bottom: 0.6rem;
}
.rwy-schedule .rs-rwy-name {
  font-family: var(--md-code-font, monospace);
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--md-default-fg-color);
}
.rwy-schedule .rs-rwy-type {
  font-size: 0.65rem;
  color: var(--md-default-fg-color--lighter);
  margin-top: 2px;
}

.rwy-schedule .rs-bar-wrap {
  position: relative;
  height: 32px;
  border-radius: 4px;
}
.rwy-schedule .rs-bar-bg {
  position: absolute;
  inset: 0;
  background: var(--md-default-bg-color);
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 4px;
}
.rwy-schedule .rs-bar-active,
.rwy-schedule .rs-bar-active-2a,
.rwy-schedule .rs-bar-active-2b {
  position: absolute;
  top: 0;
  bottom: 0;
  background: var(--md-primary-fg-color);
  border-radius: 3px;
}
.rwy-schedule .rs-bar-active-2a { left: 0; }
.rwy-schedule .rs-bar-active-2b { right: 0; }

.rwy-schedule .rs-bar-label {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  font-family: var(--md-code-font, monospace);
  font-size: 0.62rem;
  font-weight: 600;
  color: #fff;
  white-space: nowrap;
  pointer-events: none;
  z-index: 5;
}

.rwy-schedule .rs-now-line {
  position: absolute;
  top: -5px;
  bottom: -5px;
  width: 2px;
  background: #e53935;
  border-radius: 2px;
  z-index: 10;
  transition: left 1s linear;
}
.rwy-schedule .rs-now-line::before {
  content: '';
  position: absolute;
  top: 5px;
  left: 50%;
  transform: translateX(-50%);
  width: 6px;
  height: 6px;
  background: #e53935;
  border-radius: 50%;
}

.rwy-schedule .rs-axis {
  display: grid;
  grid-template-columns: 110px 1fr;
  gap: 0.75rem;
  margin-top: 0.25rem;
  margin-bottom: 0.9rem;
}
.rwy-schedule .rs-axis-ticks {
  display: flex;
  justify-content: space-between;
  font-family: var(--md-code-font, monospace);
  font-size: 0.6rem;
  color: var(--md-default-fg-color--lighter);
}

.rwy-schedule .rs-status-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.6rem;
}
.rwy-schedule .rs-status-card {
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 4px;
  padding: 0.6rem 0.8rem;
  background: var(--md-default-bg-color);
}
.rwy-schedule .rs-status-card.active {
  border-left: 3px solid var(--md-primary-fg-color);
}
.rwy-schedule .rs-status-card.next {
  border-left: 3px solid var(--md-default-fg-color--lightest);
}
.md-typeset .rwy-schedule .rs-sc-label {
  font-size: 0.65rem;
  font-weight: 800 !important;
  color: var(--md-default-fg-color);
  margin-bottom: 0.25rem;
  text-transform: uppercase;
  letter-spacing: 0.06em;
}
.rwy-schedule .rs-sc-rwy {
  font-family: var(--md-code-font, monospace);
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--md-default-fg-color);
}
.rwy-schedule .rs-sc-sub {
  font-size: 0.7rem;
  color: var(--md-default-fg-color--light);
  margin-top: 3px;
}
.rwy-schedule .rs-sc-sub span {
  color: var(--md-primary-fg-color);
  font-weight: 600;
}

.rwy-schedule .rs-dot {
  display: inline-block;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--md-primary-fg-color);
  margin-right: 5px;
  animation: rs-pulse 2s infinite;
}
@keyframes rs-pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.3; }
}

@media (max-width: 480px) {
  .rwy-schedule .rs-row,
  .rwy-schedule .rs-axis { grid-template-columns: 80px 1fr; }
  .rwy-schedule .rs-status-grid { grid-template-columns: 1fr; }
  .rwy-schedule .rs-bar-label { font-size: 0.55rem; }
}
</style>

<div class="rs-header">
  <div>
    <div class="rs-clock" id="rs-clock">--:--:--Z</div>
  </div>
</div>

<div class="rs-legend">
  <div class="rs-legend-item"><div class="rs-legend-box" style="background:var(--md-primary-fg-color);"></div> Active</div>
  <div class="rs-legend-item"><div class="rs-legend-box" style="background:var(--md-default-bg-color); border:1px solid var(--md-default-fg-color--lightest);"></div> Inactive</div>
  <div class="rs-legend-item"><div class="rs-legend-line"></div> Now</div>
</div>

<div class="rs-row">
  <div>
    <div class="rs-rwy-name">04R/22L</div>
    <div class="rs-rwy-type">Primary</div>
  </div>
  <div class="rs-bar-wrap">
    <div class="rs-bar-bg"></div>
    <div class="rs-bar-active" style="left:39.58%; width:41.67%;"></div>
    <div class="rs-bar-label" style="left:60.21%; transform:translate(-50%, -50%);">0930Z – 1930Z</div>
    <div class="rs-now-line" id="rs-now1"></div>
  </div>
</div>

<div class="rs-row">
  <div>
    <div class="rs-rwy-name">04L/22R</div>
    <div class="rs-rwy-type">Secondary</div>
  </div>
  <div class="rs-bar-wrap">
    <div class="rs-bar-bg"></div>
    <div class="rs-bar-active-2a" id="rs-seg2a"></div>
    <div class="rs-bar-active-2b" id="rs-seg2b"></div>
    <div class="rs-bar-label" style="left:19.79%; transform:translate(-50%, -50%);">0000Z – 0930Z</div>
    <div class="rs-bar-label" style="right:2.5px;">1930Z – 2359Z</div>
    <div class="rs-now-line" id="rs-now2"></div>
  </div>
</div>

<div class="rs-axis">
  <div></div>
  <div class="rs-axis-ticks">
    <span>0000</span><span>0200</span><span>0400</span><span>0600</span>
    <span>0800</span><span>1000</span><span>1200</span><span>1400</span>
    <span>1600</span><span>1800</span><span>2000</span><span>2200</span><span>2400</span>
  </div>
</div>

<div class="rs-status-grid">
  <div class="rs-status-card active">
    <div class="rs-sc-label"></span>Currently active</div>
    <div class="rs-sc-rwy" id="rs-active-rwy">—</div>
    <div class="rs-sc-sub" id="rs-active-sub">—</div>
  </div>
  <div class="rs-status-card next">
    <div class="rs-sc-label">Next change</div>
    <div class="rs-sc-rwy" id="rs-next-rwy">—</div>
    <div class="rs-sc-sub" id="rs-next-sub">—</div>
  </div>
</div>

<script>
(function () {
  var PRIMARY_START = 9 * 60 + 30;
  var PRIMARY_END   = 19 * 60 + 30;

  function pct(m) { return (m / 1440) * 100; }

  document.getElementById('rs-seg2a').style.width = pct(PRIMARY_START) + '%';
  document.getElementById('rs-seg2b').style.left  = pct(PRIMARY_END) + '%';
  document.getElementById('rs-seg2b').style.width = (100 - pct(PRIMARY_END)) + '%';

  function update() {
    var now = new Date();
    var hh = String(now.getUTCHours()).padStart(2, '0');
    var mm = String(now.getUTCMinutes()).padStart(2, '0');
    var ss = String(now.getUTCSeconds()).padStart(2, '0');
    document.getElementById('rs-clock').textContent = hh + ':' + mm + ':' + ss + 'Z';

    var total = now.getUTCHours() * 60 + now.getUTCMinutes() + now.getUTCSeconds() / 60;
    var p = pct(total) + '%';
    document.getElementById('rs-now1').style.left = p;
    document.getElementById('rs-now2').style.left = p;

    var isPrimary = total >= PRIMARY_START && total < PRIMARY_END;

    if (isPrimary) {
      var left = PRIMARY_END - total;
      var h = Math.floor(left / 60), m = Math.floor(left % 60);
      document.getElementById('rs-active-rwy').textContent = '04R/22L';
      document.getElementById('rs-active-sub').innerHTML = 'Primary · until <span>1930Z</span>';
      document.getElementById('rs-next-rwy').textContent = '04L/22R';
      document.getElementById('rs-next-sub').innerHTML = 'Secondary · in <span>' + h + 'h ' + m + 'm</span>';
    } else {
      var left2 = total < PRIMARY_START ? PRIMARY_START - total : (1440 - total) + PRIMARY_START;
      var h2 = Math.floor(left2 / 60), m2 = Math.floor(left2 % 60);
      document.getElementById('rs-active-rwy').textContent = '04L/22R';
      document.getElementById('rs-active-sub').innerHTML = 'Secondary · until <span>0930Z</span>';
      document.getElementById('rs-next-rwy').textContent = '04R/22L';
      document.getElementById('rs-next-sub').innerHTML = 'Primary · in <span>' + h2 + 'h ' + m2 + 'm</span>';
    }
  }

  update();
  setInterval(update, 1000);
})();
</script>
</div>

Below is a table of the Take-Off Run available

**Take-off Run Available.**
<table>
  <thead>
    <tr>
      <th style="text-align:center">Runway</th>
      <th style="text-align:center">Intersection</th>
      <th style="text-align:center">TORA ft (m)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2" style="text-align:center"><strong>04R</strong></td>
      <td style="text-align:center">A4</td>
      <td style="text-align:center">5,561 (1695)</td>
    </tr>
    <tr>
      <td style="text-align:center">A5</td>
      <td style="text-align:center">8,301 (2530)</td>
    </tr>
    <tr>
      <td rowspan="2" style="text-align:center"><strong>22L</strong></td>
      <td style="text-align:center">A2</td>
      <td style="text-align:center">9,121 (2780)</td>
    </tr>
    <tr>
      <td style="text-align:center">A3</td>
      <td style="text-align:center">7,841 (2390)</td>
    </tr>
    <tr>
      <td rowspan="2" style="text-align:center"><strong>04L</strong></td>
      <td style="text-align:center">B5</td>
      <td style="text-align:center">5,233 (1595)</td>
    </tr>
    <tr>
      <td style="text-align:center">B6</td>
      <td style="text-align:center">6,939 (2115)</td>
    </tr>
    <tr>
      <td rowspan="2" style="text-align:center"><strong>22R</strong></td>
      <td style="text-align:center">B3</td>
      <td style="text-align:center">6,955 (2120)</td>
    </tr>
    <tr>
      <td style="text-align:center">B4</td>
      <td style="text-align:center">5,705 (1739)</td>
    </tr>
  </tbody>
</table>

!!! warning

    Take-off/landing on Rwy 04L/22R not allowed whenever Rwy 04R/22L is in use.

    Code C aircraft not allowed to enter Twy C whenever a Code D and above aircraft is taking-off and landing on Rwy 04L/22R.

    Code D and above aircraft not allowed to enter Twy C whenever a Code C and above taking-off or landing on Rwy 04L/22R.


??? info "Aircraft Codes"
    | Code letter | Wingspan | Typical aeroplane |
    |:-----------:|:---------|:------------------|
    | A | < 15 m | PIPER PA-31/CESSNA 404 Titan |
    | B | 15 m but < 24 m | BOMBARDIER Regional Jet CRJ-200/DE HAVILLAND CANADA DHC-6 |
    | C | 24 m but < 36 m | BOEING 737-700/AIRBUS A-320/EMBRAER ERJ 190-100 |
    | D | 36 m but < 52 m | B767 Series/AIRBUS A-310 |
    | E | 52 m but < 65 m | B777 Series/B787 Series/A330 Family |
    | F | 65 m but < 80 m | BOEING 747-8/AIRBUS A-380-800 |

## Routes

Local flights within RPHI and some international flights are to use routes given below. Simbrief also give a standard route which looks like this

![Simbrief Routes](../../../assets/img/simbrief_rpvm.png)

If your route is still invalid, a controller will send you a private message with your new route. Routes within RPHI are to follow the half-moon principle in both RVSM and non-RVSM conditions. During events you will have 5 minutes between the time you request clearance and the time you request pushback, or you will have to wait until a new slot is available.

!!! warning

    During events it is important that you put your EOBT in your flight plan as controllers will use that to determine your takeoff slot.

## Waypoint Restrictions

<h3 style="text-align:center"><strong>Waypoint Restrictions</strong></h3>

<table>
  <thead>
    <tr>
      <th style="text-align:center">FIR</th>
      <th style="text-align:center">Waypoint</th>
      <th style="text-align:center">Airway</th>
      <th style="text-align:center">Altitude (FL)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:center"><strong>HONG KONG</strong></td>
      <td style="text-align:center"><strong>NOMAN / SABNO</strong></td>
      <td style="text-align:center"><strong>A583 / A461 / M501</strong></td>
      <td style="text-align:center"><strong>300 / 340 / 380</strong></td>
    </tr>
    <tr>
      <td rowspan="4" style="text-align:center"><strong>SINGAPORE</strong></td>
      <td style="text-align:center"><strong>TEGID</strong></td>
      <td style="text-align:center"><strong>M767</strong></td>
      <td style="text-align:center"><strong>310 / 320 / 350 / 360 / 390 / 400</strong></td>
    </tr>
    <tr>
      <td rowspan="3" style="text-align:center"><strong>LAXOR</strong></td>
      <td style="text-align:center"><strong>L649</strong></td>
      <td style="text-align:center"><strong>300 / 380</strong></td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>M772</strong></td>
      <td style="text-align:center"><strong>300 / 380</strong></td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>N884</strong></td>
      <td style="text-align:center"><strong>320 / 360 / 400</strong></td>
    </tr>
    <tr>
      <td rowspan="3" style="text-align:center"><strong>HO CHI MINH</strong></td>
      <td rowspan="2" style="text-align:center"><strong>PANDI / ARESI</strong></td>
      <td style="text-align:center"><strong>M765 / L628</strong></td>
      <td style="text-align:center"><strong>280 / 340</strong></td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>N500</strong></td>
      <td style="text-align:center"><strong>300</strong></td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>MIGUG</strong></td>
      <td style="text-align:center"><strong>N892</strong></td>
      <td style="text-align:center"><strong>310 / 320 / 350 / 360 / 390 / 400</strong></td>
    </tr>
  </tbody>
</table>


## Clearance

On first contact with the controller that will issue your clearance, it is recommended for you to give
the following information:

- Your bay number
- Your aircraft type
- The ATIS information letter

!!! warning

    Radio Checks on first contact are **discouraged** when building communication with the controller. 
    It's best to greet or ask the controller, should you need any help before clearance issuance.

    Be straightforward and concise as possible when communicating within a controlled frequency. 

Once you have requested for clearance, the controller will either tell you to standby, or give your clearance on the spot. Clearances include your routing, flight level restrictions, departure instructions and your squawk.

You must read back the clearance in full. Listen carefully to all details that the controller gives you, and if you are unsure about your clearance, **let the controller know.**

??? phraseology

    **CEB586**: Clearance Delivery, CEB586, Stand B2, A-3-2-0 with information A, request clearance Manila, runway 04R.

    **RPVM_DEL**: CEB586, cleared Manila, W11 CONDE, RUNWAY 04R MULOP4P, Climb  FL150, Squawk 4024



## Pushback

Normally, a controller in Mactan will instruct you to push back to the nearest reference point.

!!! warning 

    1. **Do not preplan your pushback!**
    2. Connect the tug first!

??? phraseology "Phraseology"	

    **CEB586**: Mactan Ground, CEB586, Stand B2, request push and start, runway 04R.

    **RPVM_GND**: CEB586, push and start approved, abeam B3, face D2


## Departure

The departure procedure is decided by an online Approach (**APP**) or En-route Controller (**CTR**). When both are offline, Standard Instrument Departures (**SIDs**) are given by the aerodrome controllers (**TWR**, **GND** or **DEL**). When either **APP** or **CTR** is online, they decide if departures will be given radar vectors (climb and heading instructions) to the TMA exit points or will be following a **SID**.

When **APP** or **CTR** is online, after passing 2000 feet or 5 DME from RPVM, report your passing altitude to **APP**  or **CTR**. This is to help them identify you successfully in their radar screens.

??? phraseology "Phraseology"

    **CEB586**: Mactan Approach, CEB586, passing 2000, climbing FL150, MULOP4P

    **RPVM_APP**: CEB586, radar identified, continue climb FL150

## Arrival

When arriving in to Mactan, it is best for you to be in between FL160 and FL180 when reaching the border of the TMA or the start of the STAR. On initial contact with Mactan Approach (RPVM_APP), report your current level.

??? phraseology "Phraseology"

    **PAL301**: Mactan Approach, PAL301, FL180, inbound BATAY

APP will then issue your arrival clearance including the type of approach to expect to the active runway. APP either gives you radar vectors to final or gives you descent clearances via a STAR.

??? phraseology "Phraseology"

    **RPVM_APP**: PAL301, radar contact, cleared Mactan expect radar vectors ILS 22L

    **PAL301**: Cleared Mactan expect radar vectors ILS 22L, PAL301

    **RPVM_APP**: PAL301, Maintain present heading, descend 10,000, QNH 1011

    **PAL301**: Maintain present heading, descend 10,000, QNH 1011, PAL301

!!! warning

    If APP didn’t give you any turns after you have passed the last waypoint on your routing, maintain your present heading.


## Taxi Routing

=== "RWY 04R"

    **Departures:** D1/D2/D3 → C → B7 → A5 (intersection) or A6
    
    **Arrivals:** R1/A3 → B4 or A2 → B3 or A1 → B2 → C → D1
    
    **GA Departures:** G2
    
    **GA Arrivals:** G1

=== "RWY 22L"

    **Departures:** D1/D2/D3 → C → B3 → A2 (intersection) or B2 → A1
    
    **Arrivals:** R2 → B6 or A5 → B7 or A6 → C → D1/D2/D3
    
    **GA Departures:** G1 or G2
    
    **GA Arrivals:** G1 or G2

=== "RWY 04L"

    **Departures:** D1/D2/D3 → C → B7 or B6
    
    **Arrivals:** B2 or B3 → C → D1/D2/D3
    
    **GA Departures:** G1 or G2
    
    **GA Arrivals:** G1 or G2

=== "RWY 22R"

    **Departures:** D1/D2/D3 → C → B2
    
    **Arrivals:** B7 or B6 → C → D1/D2/D3
    
    **GA Departures:** G1 → A4
    
    **GA Arrivals:** A5 → G2

[^1]: Vertical limit of FL150 can be increased to a maximum of FL200.
[^2]: Can control top-down Mactan SUB-TMA which includes RPSP and RPVD. But check the controller information if they do!

*[GA]: General Aviation
*[EOBT]: Estimated off block time
*[TOBT]: Target off block time
*[TSAT]: Target start approval time
*[ASRT]: Actual start up time
*[TTOT]: Target takeoff time
*[CTOT]: Calculated takeoff time
*[RPVM_DEL]: Clearance Delivery
*[RPVM_GND]: Mactan Ground
*[RPVM_TWR]: Mactan Tower
*[RPVM_APP]: Mactan Approach
*[RPVM_S_APP]: Mactan Approach
