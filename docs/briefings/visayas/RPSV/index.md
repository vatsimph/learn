# RPSV - San Vicente Airport

<div class="metar-widget" data-icao="RPSV">
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

<div class="metar-loading" id="metar-loading-RPSV">Fetching METAR...</div>
<div class="metar-card" id="metar-card-RPSV" style="display:none;"></div>
</div>

<script>
(function () {
  var ICAO = "RPSV";
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
San Vicente Airport (RPSV) is a Principal Class 2 airport in San Vicente, northern Palawan, serving the Long Beach / Port Barton tourism area. It has a single runway (04/22) and handles domestic flights and general aviation.

The airport reference point (ARP) is approximately 103130N 1191625E, aerodrome elevation 24 FT.

!!! warning "Terrain"

    High terrain lies to the south-east of the aerodrome, with peaks above 2,000 FT. Note the obstacles on the Runway 22 approach and fly the published circuit accurately.

!!! note "Airspace"

    - San Vicente is an **advisory** aerodrome. Flight information and advisory service within the aerodrome advisory zone is provided by **San Vicente Radio (RPSV_R_TWR)**, an FSS, during published hours (2300 - 0900).
    - There is no control zone, terminal area, or radar approach service. Outside the advisory hours the aerodrome is uncontrolled.
    - **Transition altitude:** not published.

## Charts
<div class="chart-picker" data-icao="RPSV"></div>

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
      <td style="text-align:center"><strong>RPSV_R_TWR</strong></td>
      <td style="text-align:center">San Vicente Radio</td>
      <td style="text-align:center">123.300</td>
      <td style="text-align:center">FSS, advisory service</td>
    </tr>
  </tbody>
</table>

!!! info "When no controller is online"

    San Vicente is an advisory aerodrome and is rarely staffed on the network. When no Philippine controller is online, operate under **UNICOM (122.800)** and self-announce your intentions. When a Manila Radio / Center (**CTR/FSS**) controller is online, they provide a top-down service.

## Runways

<div markdown="1">
San Vicente has 1 runway (04/22), 1825 x 45 M, concrete, PCN 470/R/B/X/U.

Both runways have a displaced threshold (04 by 133 M, LDA 1692 M; 22 by 76 M, LDA 1749 M). There are no approach lights. **Runway 04 is the preferred runway-in-use whenever the wind is calm (5 KT or less).**

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
    <tr><td style="text-align:center"><strong>04</strong></td><td style="text-align:center">1825</td><td style="text-align:center">1885</td><td style="text-align:center">1825</td><td style="text-align:center">1692</td></tr>
    <tr><td style="text-align:center"><strong>22</strong></td><td style="text-align:center">1825</td><td style="text-align:center">1975</td><td style="text-align:center">1825</td><td style="text-align:center">1749</td></tr>
  </tbody>
</table>

## Operations

!!! note "Flight Service Station"

    San Vicente Radio is a **Flight Service Station (FSS)**. It provides **traffic and flight information advisories only** and **cannot issue ATC clearances**. Pilots remain responsible for their own separation and self-announce their intentions.

San Vicente operates VFR within the advisory zone. On first contact with San Vicente Radio (or on UNICOM when uncontrolled), give your position, aircraft type and intentions, and listen out for other traffic.

!!! warning

    With a single runway, terrain to the south-east and no radar service, maintain a good lookout and self-announce on each leg of the circuit. Never enter or backtrack the runway until it is confirmed clear. Read back any hold short instruction with **"HOLDING SHORT"**.

## Traffic Circuit

!!! warning "Terrain"

    High terrain lies to the south-east, with peaks above 2,000 FT. Fly the circuit accurately and remain clear of the high ground.

=== "RWY 04"

    ![RPSV Traffic Circuit RWY 04](../../../assets/img/RPSV%20VFR/Traffic%20Circuit%20RWY%2004.png)

    **Left-hand circuit.** Aircraft at **105 KT or less** fly the inner circuit (1.0 NM from the runway); aircraft at **106 KT or more** fly the outer circuit (2.0 NM). **Runway 04 is the preferred runway-in-use when the wind is calm (5 KT or less).**

=== "RWY 22"

    ![RPSV Traffic Circuit RWY 22](../../../assets/img/RPSV%20VFR/Traffic%20Circuit%20RWY%2022.png)

    **Right-hand circuit.** Aircraft at **105 KT or less** fly the inner circuit (1.0 NM from the runway); aircraft at **106 KT or more** fly the outer circuit (2.0 NM).

!!! info "Circuit entry and exit"

    - **Arriving aircraft** shall enter the traffic circuit on the **downwind leg at an angle of 45 degrees**.
    - **Departing aircraft** shall follow the traffic circuit and **leave the circuit at an angle of 45 degrees**.

*[AAZ]: Aerodrome Advisory Zone
*[FSS]: Flight Service Station
*[CTR]: Control Zone
*[VFR]: Visual Flight Rules
*[PCN]: Pavement Classification Number
*[RPSV_R_TWR]: San Vicente Radio
