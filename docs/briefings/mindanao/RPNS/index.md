# RPNS - Siargao Airport

<div class="metar-widget" data-icao="RPNS">
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

<div class="metar-loading" id="metar-loading-RPNS">Fetching METAR...</div>
<div class="metar-card" id="metar-card-RPNS" style="display:none;"></div>
</div>

<script>
(function () {
  var ICAO = "RPNS";
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
Siargao Airport (RPNS) is a Principal Class 2 airport serving Siargao Island in Surigao del Norte, a popular surfing and tourist destination in the Caraga region of Mindanao. It has a single runway (01/19) and handles domestic flights and general aviation.

The airport reference point (ARP) is 095131N 1260055E, aerodrome elevation 33 FT.

!!! note "Airspace"

    - **Siargao ATZ** — circle 5 NM radius centered on the ARP (095131N 1260055E), surface up to but excluding 2000 FT (Class B). Aerodrome control is provided by **Siargao Tower (RPNS_TWR)**.
    - There is no control zone, terminal area, or radar approach service; it is a tower-only aerodrome.
    - **Transition altitude:** not published.

## Charts
<div class="chart-picker" data-icao="RPNS"></div>

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
      <td style="text-align:center"><strong>RPNS_TWR</strong></td>
      <td style="text-align:center">Siargao Tower</td>
      <td style="text-align:center">127.100</td>
      <td style="text-align:center">ATZ, SFC up to excluding 2000 ft</td>
    </tr>
  </tbody>
</table>

!!! info "When no controller is online"

    When no Philippine controller is online, operate under **UNICOM (122.800)** and self-announce your intentions. When a Manila Radio / Center (**CTR/FSS**) controller is online, they provide a top-down service.

## Runways

<div markdown="1">
Siargao has 1 runway (01/19), 1347 x 30 M, concrete, PCN 488/R/B/W/U.

There are no approach lights. Below is a table of the declared distances.
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
    <tr><td style="text-align:center"><strong>01</strong></td><td style="text-align:center">1347</td><td style="text-align:center">1407</td><td style="text-align:center">1347</td><td style="text-align:center">1347</td></tr>
    <tr><td style="text-align:center"><strong>19</strong></td><td style="text-align:center">1347</td><td style="text-align:center">1407</td><td style="text-align:center">1347</td><td style="text-align:center">1347</td></tr>
  </tbody>
</table>

## Operations

Siargao Tower provides aerodrome control only, and the aerodrome operates VFR. On first contact, give your parking position and aircraft type, and request your departure clearance. There is no radar approach service; expect a visual approach to the runway in use.

!!! warning

    With a single runway and no radar service, maintain a good lookout and fly the circuit accurately. Never enter or backtrack the runway until you have been explicitly cleared to do so. Read back any hold short instruction with **"HOLDING SHORT"**.

??? phraseology "Phraseology"

    **RP-C123**: Siargao Tower, RP-C123, GA apron, request taxi, runway 01.

    **RPNS_TWR**: RP-C123, taxi to holding point runway 01.

    **RP-C123**: Taxi to holding point runway 01, RP-C123.

## VFR Area Chart

![RPNS VFR Area Chart](../../../assets/img/RPNS%20VFR/VFR%20Area%20Chart%20RPNS.png)

The chart shows the published VFR **arrival** (magenta) and **departure** (blue) routes and the visual reporting points around Siargao.

## Traffic Circuit

=== "RWY 01"

    ![RPNS Traffic Circuit RWY 01](../../../assets/img/RPNS%20VFR/Traffic%20Circuit%20RWY%2001.png)

    **Left-hand circuit.** Aircraft at **105 KT or less** fly the inner circuit (1.0 NM from the runway); aircraft at **106 KT or more** fly the outer circuit (2.0 NM).

=== "RWY 19"

    ![RPNS Traffic Circuit RWY 19](../../../assets/img/RPNS%20VFR/Traffic%20Circuit%20RWY%2019.png)

    **Right-hand circuit.** Aircraft at **105 KT or less** fly the inner circuit (1.0 NM from the runway); aircraft at **106 KT or more** fly the outer circuit (2.0 NM).

!!! info "Circuit entry and exit"

    - **Arriving aircraft** shall enter the traffic circuit on the **downwind leg at an angle of 45 degrees**.
    - **Departing aircraft** shall follow the traffic circuit and **leave the circuit at an angle of 45 degrees**.

*[ATZ]: Aerodrome Traffic Zone
*[CTR]: Control Zone
*[VFR]: Visual Flight Rules
*[PCN]: Pavement Classification Number
*[RPNS_TWR]: Siargao Tower
