# RPUO - Basco Airport

<div class="metar-widget" data-icao="RPUO">
<style>
.metar-widget { margin: 1rem 0; }
.metar-card {
  display: flex; flex-direction: column; gap: 0.45rem; padding: 0.75rem 1rem;
  border: 1px solid var(--md-default-fg-color--lightest);
  border-left: 4px solid var(--md-primary-fg-color, #4051b5);
  border-radius: 4px; background: var(--md-code-bg-color);
}
.metar-raw {
  font-family: var(--md-code-font, monospace); font-size: 0.75rem; line-height: 1.7;
  color: var(--md-default-fg-color); white-space: pre-wrap; letter-spacing: 0.02em;
}
.metar-loading {
  font-size: 0.75rem; color: var(--md-default-fg-color--light);
  letter-spacing: 0.04em; padding: 0.25rem 0;
}
</style>

<div class="metar-loading" id="metar-loading-RPUO">Fetching METAR...</div>
<div class="metar-card" id="metar-card-RPUO" style="display:none;"></div>
</div>

<script>
(function () {
  var ICAO = "RPUO";
  var loadingEl = document.getElementById("metar-loading-" + ICAO);
  var cardEl    = document.getElementById("metar-card-" + ICAO);
  function render(metar) { cardEl.innerHTML = '<div class="metar-raw">' + metar + '</div>'; cardEl.style.display = ""; loadingEl.style.display = "none"; }
  function renderError(msg) { cardEl.innerHTML = '<div class="metar-raw" style="color:#b71c1c;">' + msg + '</div>'; cardEl.style.display = ""; loadingEl.style.display = "none"; }
  function fetchMetar() {
    fetch("https://metar.vatsim.net/" + ICAO + "?format=json")
      .then(function(r) { if (!r.ok) throw new Error("HTTP " + r.status); return r.json(); })
      .then(function(data) { if (!data || !data.length || !data[0].metar) { renderError("No METAR available for " + ICAO + "."); return; } render(data[0].metar); })
      .catch(function(e) { renderError(e.message || "Network error."); });
  }
  fetchMetar();
  setInterval(fetchMetar, 5000);
})();
</script>

## General
Basco Airport (RPUO) is a Principal Class 2 airport in Basco, Batanes. It has a single runway (06/24) and serves domestic flights and general aviation.

The airport reference point (ARP) is 202705N 1215849E, aerodrome elevation 309 FT.

Runway 06 is served by a PAPI (3.0°); runway 24 has no visual glide-slope guidance. The runway slopes up towards the threshold of runway 24.

!!! airspace "Airspace"

    - **Basco Aerodrome Advisory Zone (AAZ)** — circle 5 NM radius centered on the ARP, surface up to but excluding 2000 FT (Class G). Flight information and advisory service is provided by **Basco Radio (RPUO_R_TWR)** on **122.000**, an FSS.
    - There is no control zone, terminal area, or radar approach service. When Basco Radio is offline, operate on **UNICOM (122.800)**.
    - **Transition altitude:** not published.

## Charts
<div class="chart-picker" data-icao="RPUO"></div>

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
    <tr><td style="text-align:center"><strong>RPUO_R_TWR</strong></td><td style="text-align:center">Basco Radio</td><td style="text-align:center">122.000</td><td style="text-align:center">FSS, advisory within the AAZ</td></tr>
    <tr><td style="text-align:center"><strong>Unicom</strong></td><td style="text-align:center">—</td><td style="text-align:center">122.800</td><td style="text-align:center">When Basco Radio is offline</td></tr>
  </tbody>
</table>

## Runways

<div markdown="1">
Basco has 1 runway (06/24), 1244 x 30 M, asphalt, PCN 380/F/B/X/T.

Below is a table of the declared distances.
</div>

**Declared Distances (metres).**
<table>
  <thead>
    <tr>
      <th style="text-align:center">Runway</th>
      <th style="text-align:center">TORA (m)</th>
      <th style="text-align:center">TODA (m)</th>
      <th style="text-align:center">ASDA (m)</th>
      <th style="text-align:center">LDA (m)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="text-align:center"><strong>06</strong></td><td style="text-align:center">1244</td><td style="text-align:center">1364</td><td style="text-align:center">1244</td><td style="text-align:center">1244</td></tr>
    <tr><td style="text-align:center"><strong>24</strong></td><td style="text-align:center">1244</td><td style="text-align:center">1379</td><td style="text-align:center">1341</td><td style="text-align:center">1244</td></tr>
  </tbody>
</table>

## Operations

!!! warning

    **Terrain.** Mount Iraya (3306 FT) lies about 2.4 KM from the ARP. For fixed-wing aircraft there is **no landing on runway 24 and no take-off on runway 06**. No more than two aircraft in the traffic pattern at any time.

!!! note "Flight Service Station"

    Basco Radio is a **Flight Service Station (FSS)**. It provides **traffic and flight information advisories only** and **cannot issue ATC clearances**. Pilots remain responsible for their own separation and self-announce their intentions.

Basco operates VFR. On first contact with Basco Radio (or on UNICOM when it is offline), give your position, aircraft type and intentions, and listen out for other traffic.

!!! tip "Who to monitor"

    Monitor the advisory frequency — Basco Radio on **122.000** (or **UNICOM 122.800** when it is offline). When no local controller is online, you are also advised to monitor **Manila Control (CTR)** when one is online for traffic information.

!!! warning

    With a single runway and no radar service, maintain a good lookout and self-announce on each leg of the circuit. Never enter or backtrack the runway until it is confirmed clear. Read back any hold short instruction with **"HOLDING SHORT"**.

*[ARP]: Aerodrome Reference Point
*[AAZ]: Aerodrome Advisory Zone
*[FSS]: Flight Service Station
*[CTR]: Control Zone
*[VFR]: Visual Flight Rules
*[PAPI]: Precision Approach Path Indicator
*[PCN]: Pavement Classification Number
*[RPUO_R_TWR]: Basco Radio
