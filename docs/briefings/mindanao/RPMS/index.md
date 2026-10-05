# RPMS - Surigao Airport

<div class="metar-widget" data-icao="RPMS">
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

<div class="metar-loading" id="metar-loading-RPMS">Fetching METAR...</div>
<div class="metar-card" id="metar-card-RPMS" style="display:none;"></div>
</div>

<script>
(function () {
  var ICAO = "RPMS";
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
Surigao Airport (RPMS) is a Principal Class 2 airport in Surigao City, Surigao del Norte. It has a single runway (18/36) and serves domestic flights and general aviation.

The airport reference point (ARP) is 094528N 1252852E, aerodrome elevation 20 FT.

!!! airspace "Airspace"

    - **Surigao Aerodrome Advisory Zone (AAZ)** — circle 5 NM radius centered on the ARP, surface up to but excluding 2000 FT (Class G). Flight information and advisory service is provided by **Surigao Radio (RPMS_R_TWR)** on **122.000**, an FSS.
    - There is no control zone, terminal area, or radar approach service. When Surigao Radio is offline, operate on **UNICOM (122.800)**.
    - **Transition altitude:** not published.

## Charts
<div class="chart-picker" data-icao="RPMS"></div>

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
    <tr><td style="text-align:center"><strong>RPMS_R_TWR</strong></td><td style="text-align:center">Surigao Radio</td><td style="text-align:center">122.000</td><td style="text-align:center">FSS, advisory within the AAZ</td></tr>
    <tr><td style="text-align:center"><strong>Unicom</strong></td><td style="text-align:center">—</td><td style="text-align:center">122.800</td><td style="text-align:center">When Surigao Radio is offline</td></tr>
  </tbody>
</table>

## Runways

<div markdown="1">
Surigao has 1 runway (18/36), 1619 x 45 M, concrete and asphalt, PCN 620/R/B/W/T.

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
    <tr><td style="text-align:center"><strong>18</strong></td><td style="text-align:center">1619</td><td style="text-align:center">1679</td><td style="text-align:center">1619</td><td style="text-align:center">1619</td></tr>
    <tr><td style="text-align:center"><strong>36</strong></td><td style="text-align:center">1619</td><td style="text-align:center">1679</td><td style="text-align:center">1619</td><td style="text-align:center">1619</td></tr>
  </tbody>
</table>

## Operations

!!! note "Flight Service Station"

    Surigao Radio is a **Flight Service Station (FSS)**. It provides **traffic and flight information advisories only** and **cannot issue ATC clearances**. Pilots remain responsible for their own separation and self-announce their intentions.

Surigao operates VFR. On first contact with Surigao Radio (or on UNICOM when it is offline), give your position, aircraft type and intentions, and listen out for other traffic.

!!! tip "Who to monitor"

    Monitor the advisory frequency — Surigao Radio on **122.000** (or **UNICOM 122.800** when it is offline). When no local controller is online, you are also advised to monitor **Butuan Approach (RPME_APP)** or **Manila Control (CTR)** when one is online for traffic information.

!!! warning

    With a single runway and no radar service, maintain a good lookout and self-announce on each leg of the circuit. Never enter or backtrack the runway until it is confirmed clear. Read back any hold short instruction with **"HOLDING SHORT"**.

*[ARP]: Aerodrome Reference Point
*[AAZ]: Aerodrome Advisory Zone
*[FSS]: Flight Service Station
*[CTR]: Control Zone
*[VFR]: Visual Flight Rules
*[PAPI]: Precision Approach Path Indicator
*[PCN]: Pavement Classification Number
*[RPMS_R_TWR]: Surigao Radio
*[RPME_APP]: Butuan Approach
