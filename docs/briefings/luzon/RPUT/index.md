# RPUT - Tuguegarao Airport

<div class="metar-widget" data-icao="RPUT">
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

<div class="metar-loading" id="metar-loading-RPUT">Fetching METAR...</div>
<div class="metar-card" id="metar-card-RPUT" style="display:none;"></div>
</div>

<script>
(function () {
  var ICAO = "RPUT";
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
Tuguegarao Airport (RPUT) is a Principal Class 1 airport serving Tuguegarao City, the capital of Cagayan, in the Cagayan Valley region of northern Luzon. It has a single runway (17/35) and handles domestic passenger flights and general aviation.

The airport reference point (ARP) is 173837N 1214359E, aerodrome elevation 75 FT.

!!! note "Airspace"

    - **Tuguegarao Aerodrome Advisory Zone (AAZ)** — circle 5 NM radius centered on the ARP (173837N 1214359E), surface up to but excluding 2000 FT (Class G). Flight information and advisory service is provided by **Tuguegarao Radio (RPUT_R_TWR)**.
    - There is no control zone, terminal area, or radar approach service.
    - **Transition altitude:** not published.

## Charts
<div class="chart-picker" data-icao="RPUT"></div>

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
      <td style="text-align:center"><strong>RPUT_R_TWR</strong></td>
      <td style="text-align:center">Tuguegarao Radio</td>
      <td style="text-align:center">122.850</td>
      <td style="text-align:center">FSS, advisory within the AAZ</td>
    </tr>
  </tbody>
</table>

!!! info "When a controller is online"

    Tuguegarao is an advisory aerodrome, controllers do not give you clearance, rather they give advisory information.

## Runways

<div markdown="1">
Tuguegarao has 1 runway (17/35), 1965 x 45 M, concrete (stopway macadam), PCN 470/R/B/X/U.

Both thresholds have green threshold lights, a Runway Threshold Identification Light (RTIL, flashing white) and a PAPI (left, 3.0°). There are no approach lights.

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
    <tr><td style="text-align:center"><strong>17</strong></td><td style="text-align:center">1965</td><td style="text-align:center">2100</td><td style="text-align:center">2100</td><td style="text-align:center">1965</td></tr>
    <tr><td style="text-align:center"><strong>35</strong></td><td style="text-align:center">1965</td><td style="text-align:center">2100</td><td style="text-align:center">2100</td><td style="text-align:center">1965</td></tr>
  </tbody>
</table>

## Operations

!!! note "Flight Service Station"

    Tuguegarao Radio is a **Flight Service Station (FSS)**. It provides **traffic and flight information advisories only** and **cannot issue ATC clearances**. Pilots remain responsible for their own separation and self-announce their intentions.

Tuguegarao operates VFR within the advisory zone, with a maximum of **two (2) aircraft in the traffic pattern at any given time**. On first contact with Tuguegarao Radio (or on UNICOM when uncontrolled), give your position, aircraft type and intentions, and listen out for other traffic.

!!! warning

    With a single runway and no radar service, maintain a good lookout and self-announce on each leg of the circuit. Never enter or backtrack the runway until it is confirmed clear. Read back any hold short instruction with **"HOLDING SHORT"**.

See the [Visual Flight Rules](vfr.md) page for the published traffic circuit.

??? phraseology "Phraseology (advisory)"

    **RP-C123**: Tuguegarao Radio, RP-C123, GA apron, request airport advisory, VFR departure to the south.

    **RPUT_R_TWR**: RP-C123, Tuguegarao Radio, runway 35 in use, wind calm, QNH 1012, no reported traffic.

    **RP-C123**: Runway 35, QNH 1012, RP-C123.

*[ATIS]: Automatic Terminal Information Service
*[AAZ]: Aerodrome Advisory Zone
*[FSS]: Flight Service Station
*[CTR]: Control Zone
*[VFR]: Visual Flight Rules
*[PCN]: Pavement Classification Number
*[RTIL]: Runway Threshold Identification Light
*[RPUT_R_TWR]: Tuguegarao Radio
