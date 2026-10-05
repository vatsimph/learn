# RPVZ - Siquijor Airport

<div class="metar-widget" data-icao="RPVZ">
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

<div class="metar-loading" id="metar-loading-RPVZ">Fetching METAR...</div>
<div class="metar-card" id="metar-card-RPVZ" style="display:none;"></div>
</div>

<script>
(function () {
  var ICAO = "RPVZ";
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
Siquijor Airport (RPVZ) is a Community aerodrome in Siquijor. It has a single runway (04/22) and serves general aviation and light community air services.

The airport reference point (ARP) is 091242N 1232816E, aerodrome elevation 80 FT.

!!! airspace "Airspace"

    - Siquijor is an **uncontrolled** aerodrome. There is no control tower, advisory (FSS) service, control zone, terminal area, or radar service.
    - Operate under **UNICOM (122.800)** and self-announce your position and intentions on each leg. When **Manila Control (CTR)** is online, monitor it for traffic information.
    - **Transition altitude:** not published.

## Charts
<div class="chart-picker" data-icao="RPVZ"></div>

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
    <tr><td style="text-align:center"><strong>Unicom</strong></td><td style="text-align:center">—</td><td style="text-align:center">122.800</td><td style="text-align:center">Self-announce; no ATS at this aerodrome</td></tr>
  </tbody>
</table>

## Runways

<div markdown="1">
Siquijor has 1 runway (04/22), 1350 x 45 M, concrete, PCN 306/F/B/Y/U.

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
    <tr><td style="text-align:center"><strong>04</strong></td><td style="text-align:center">1350</td><td style="text-align:center">1500</td><td style="text-align:center">1350</td><td style="text-align:center">1350</td></tr>
    <tr><td style="text-align:center"><strong>22</strong></td><td style="text-align:center">1350</td><td style="text-align:center">1590</td><td style="text-align:center">1350</td><td style="text-align:center">1350</td></tr>
  </tbody>
</table>

## Operations

Siquijor operates VFR only and is uncontrolled. Broadcast your intentions on **UNICOM 122.800** — taxi, backtrack, line-up, take-off, circuit joining and final — and keep a good lookout for other traffic.

!!! tip "Who to monitor"

    Monitor the advisory frequency — **UNICOM (122.800)**. When no local controller is online, you are also advised to monitor **Manila Control (CTR)** when one is online for traffic information.

!!! warning

    With a single runway and no radar service, maintain a good lookout and self-announce on each leg of the circuit. Never enter or backtrack the runway until it is confirmed clear. Read back any hold short instruction with **"HOLDING SHORT"**.

*[ARP]: Aerodrome Reference Point
*[AAZ]: Aerodrome Advisory Zone
*[FSS]: Flight Service Station
*[CTR]: Control Zone
*[VFR]: Visual Flight Rules
*[PAPI]: Precision Approach Path Indicator
*[PCN]: Pavement Classification Number
