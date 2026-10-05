# RPVJ - Masbate Airport

<div class="metar-widget" data-icao="RPVJ">
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

<div class="metar-loading" id="metar-loading-RPVJ">Fetching METAR...</div>
<div class="metar-card" id="metar-card-RPVJ" style="display:none;"></div>
</div>

<script>
(function () {
  var ICAO = "RPVJ";
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
Masbate Airport (RPVJ) is a Principal Class 2 airport in Masbate City, Masbate. It has a single runway (04/22) and serves domestic flights and general aviation.

The airport reference point (ARP) is 122210N 1233747E, aerodrome elevation 50 FT.

!!! airspace "Airspace"

    - **Masbate Aerodrome Advisory Zone (AAZ)** — circle 5 NM radius centered on the ARP, surface up to but excluding 2000 FT (Class G). Flight information and advisory service is provided by **Masbate Radio (RPVJ_R_TWR)** on **122.000**, an FSS.
    - There is no control zone, terminal area, or radar approach service. When Masbate Radio is offline, operate on **UNICOM (122.800)**.
    - **Transition altitude:** not published.

## Charts
<div class="chart-picker" data-icao="RPVJ"></div>

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
    <tr><td style="text-align:center"><strong>RPVJ_R_TWR</strong></td><td style="text-align:center">Masbate Radio</td><td style="text-align:center">122.000</td><td style="text-align:center">FSS, advisory within the AAZ</td></tr>
    <tr><td style="text-align:center"><strong>Unicom</strong></td><td style="text-align:center">—</td><td style="text-align:center">122.800</td><td style="text-align:center">When Masbate Radio is offline</td></tr>
  </tbody>
</table>

## Runways

<div markdown="1">
Masbate has 1 runway (04/22), 1280 x 30 M, concrete and asphalt, PCN 103/F/B/Y/U.

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
    <tr><td style="text-align:center"><strong>04</strong></td><td style="text-align:center">1280</td><td style="text-align:center">1340</td><td style="text-align:center">1340</td><td style="text-align:center">NU</td></tr>
    <tr><td style="text-align:center"><strong>22</strong></td><td style="text-align:center">NU</td><td style="text-align:center">NU</td><td style="text-align:center">NU</td><td style="text-align:center">1280</td></tr>
  </tbody>
</table>

*NU = not usable for that operation.*

## Operations

!!! warning

    **Single-direction operations.** The declared distances allow **take-off on runway 04 only** and **landing on runway 22 only** (the opposite directions are not usable). Plan to depart on 04 and arrive on 22.

!!! note "Flight Service Station"

    Masbate Radio is a **Flight Service Station (FSS)**. It provides **traffic and flight information advisories only** and **cannot issue ATC clearances**. Pilots remain responsible for their own separation and self-announce their intentions.

Masbate operates VFR. On first contact with Masbate Radio (or on UNICOM when it is offline), give your position, aircraft type and intentions, and listen out for other traffic.

!!! tip "Who to monitor"

    Monitor the advisory frequency — Masbate Radio on **122.000** (or **UNICOM 122.800** when it is offline). When no local controller is online, you are also advised to monitor **Manila Control (CTR)** when one is online for traffic information.

!!! warning

    With a single runway and no radar service, maintain a good lookout and self-announce on each leg of the circuit. Never enter or backtrack the runway until it is confirmed clear. Read back any hold short instruction with **"HOLDING SHORT"**.

*[ARP]: Aerodrome Reference Point
*[AAZ]: Aerodrome Advisory Zone
*[FSS]: Flight Service Station
*[CTR]: Control Zone
*[VFR]: Visual Flight Rules
*[PAPI]: Precision Approach Path Indicator
*[PCN]: Pavement Classification Number
*[RPVJ_R_TWR]: Masbate Radio
