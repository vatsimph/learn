# RPVS - Antique Airport

<div class="metar-widget" data-icao="RPVS">
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

<div class="metar-loading" id="metar-loading-RPVS">Fetching METAR...</div>
<div class="metar-card" id="metar-card-RPVS" style="display:none;"></div>
</div>

<script>
(function () {
  var ICAO = "RPVS";
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
Antique Airport (RPVS), also known as Evelio Javier Airport, is a Principal Class 2 airport in San Jose de Buenavista, the capital of Antique province on the island of Panay, Western Visayas. It has a single runway (18/36) and serves domestic flights and general aviation.

The airport reference point (ARP) is 104605N 1215556E, aerodrome elevation 33 FT.

!!! note "Airspace"

    - **Antique Aerodrome Advisory Zone (AAZ)** — circle 5 NM radius centered on the ARP (104605N 1215556E), surface up to but excluding 2000 FT (Class G). Flight information and advisory service is provided by **Antique Radio (RPVS_R_TWR)**, an FSS, during published hours (2200 - 0900).
    - There is no control zone, terminal area, or radar approach service. Outside the advisory hours the aerodrome is uncontrolled.
    - **Transition altitude:** not published.

## Charts
<div class="chart-picker" data-icao="RPVS"></div>

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
      <td style="text-align:center"><strong>RPVS_R_TWR</strong></td>
      <td style="text-align:center">Antique Radio</td>
      <td style="text-align:center">127.100</td>
      <td style="text-align:center">FSS, advisory within the AAZ</td>
    </tr>
  </tbody>
</table>

!!! info "When no controller is online"

    Antique is an advisory aerodrome and is rarely staffed on the network. When no Philippine controller is online, operate under **UNICOM (122.800)** and self-announce your intentions. When a Manila Radio / Center (**CTR/FSS**) controller is online, they provide a top-down service.

## Runways

<div markdown="1">
Antique has 1 runway (18/36), 1631 x 30 M, concrete and asphalt, PCN 306/R/B/X/U.

Runway 18 has a displaced threshold (131 M; landing distance available 1500 M). There are no approach lights.

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
    <tr><td style="text-align:center"><strong>18</strong></td><td style="text-align:center">1631</td><td style="text-align:center">1691</td><td style="text-align:center">1631</td><td style="text-align:center">1500</td></tr>
    <tr><td style="text-align:center"><strong>36</strong></td><td style="text-align:center">1631</td><td style="text-align:center">1691</td><td style="text-align:center">1631</td><td style="text-align:center">1631</td></tr>
  </tbody>
</table>

## Operations

!!! note "Flight Service Station"

    Antique Radio is a **Flight Service Station (FSS)**. It provides **traffic and flight information advisories only** and **cannot issue ATC clearances**. Pilots remain responsible for their own separation and self-announce their intentions.

Antique operates VFR within the advisory zone. On first contact with Antique Radio (or on UNICOM when uncontrolled), give your position, aircraft type and intentions, and listen out for other traffic.

!!! warning

    With a single runway and no radar service, maintain a good lookout and self-announce on each leg of the circuit. Never enter or backtrack the runway until it is confirmed clear. Read back any hold short instruction with **"HOLDING SHORT"**.

## VFR Area Chart

![RPVS VFR Area Chart](../../../assets/img/RPVS%20VFR/VFR%20Area%20Chart%20RPVS.png)

The chart shows the published VFR **arrival** (magenta) and **departure** (blue) routes and the visual reporting points around Antique.

## Traffic Circuit

=== "RWY 18"

    ![RPVS Traffic Circuit RWY 18](../../../assets/img/RPVS%20VFR/Traffic%20Circuit%20RWY%2018.png)

    **Right-hand circuit.** Aircraft at **105 KT or less** fly the inner circuit (1.0 NM from the runway); aircraft at **106 KT or more** fly the outer circuit (2.0 NM).

=== "RWY 36"

    ![RPVS Traffic Circuit RWY 36](../../../assets/img/RPVS%20VFR/Traffic%20Circuit%20RWY%2036.png)

    **Left-hand circuit.** Aircraft at **105 KT or less** fly the inner circuit (1.0 NM from the runway); aircraft at **106 KT or more** fly the outer circuit (2.0 NM).

!!! info "Circuit entry and exit"

    - **Arriving aircraft** shall enter the traffic circuit on the **downwind leg at an angle of 45 degrees**.
    - **Departing aircraft** shall follow the traffic circuit and **leave the circuit at an angle of 45 degrees**.

*[AAZ]: Aerodrome Advisory Zone
*[FSS]: Flight Service Station
*[CTR]: Control Zone
*[VFR]: Visual Flight Rules
*[PCN]: Pavement Classification Number
*[RPVS_R_TWR]: Antique Radio
