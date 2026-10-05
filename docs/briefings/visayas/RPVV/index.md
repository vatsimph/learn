# RPVV - Busuanga (Francisco B. Reyes) Airport

<div class="metar-widget" data-icao="RPVV">
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

<div class="metar-loading" id="metar-loading-RPVV">Fetching METAR...</div>
<div class="metar-card" id="metar-card-RPVV" style="display:none;"></div>
</div>

<script>
(function () {
  var ICAO = "RPVV";
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
Busuanga Airport (RPVV), officially Francisco B. Reyes Airport, is a Principal Class 2 airport serving the Coron / Busuanga area in northern Palawan. It has a single runway (08/26) and serves domestic flights and general aviation to one of the country's busiest island destinations.

The airport reference point (ARP) is 120719N 1200603E, aerodrome elevation 148 FT.

!!! warning "Terrain"

    Busuanga is surrounded by high terrain, with hills rising above 1,000 FT close to the aerodrome. Fly the published traffic circuit accurately and remain within the ATZ lateral and vertical limits.

!!! airspace "Airspace"

    - **Busuanga ATZ** — circle 5 NM radius centered on the ARP (120719N 1200603E), surface up to but excluding 3000 FT (Class B). Aerodrome control is provided by **Busuanga Tower (RPVV_TWR)**.
    - There is no control zone, terminal area, or radar approach service; it is a tower-only aerodrome.
    - **Transition altitude:** not published.

## Charts
<div class="chart-picker" data-icao="RPVV"></div>

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
      <td style="text-align:center"><strong>RPVV_TWR</strong></td>
      <td style="text-align:center">Busuanga Tower</td>
      <td style="text-align:center">126.700</td>
      <td style="text-align:center">ATZ, SFC up to excluding 3000 ft</td>
    </tr>
  </tbody>
</table>

!!! info "When no controller is online"

    When no Philippine controller is online, operate under **UNICOM (122.800)** and self-announce your intentions. When **Manila Control (CTR)** is online, monitor it for traffic information.

## Runways

<div markdown="1">
Busuanga has 1 runway (08/26), 1225 x 30 M.

Runway 26 is served by a PAPI (left, 3.0°). Runway 08 has no visual glide-slope guidance, and there are no approach lights on either runway.

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
    <tr><td style="text-align:center"><strong>08</strong></td><td style="text-align:center">1225</td><td style="text-align:center">1325</td><td style="text-align:center">1265</td><td style="text-align:center">1225</td></tr>
    <tr><td style="text-align:center"><strong>26</strong></td><td style="text-align:center">1225</td><td style="text-align:center">1325</td><td style="text-align:center">1325</td><td style="text-align:center">1225</td></tr>
  </tbody>
</table>

## Operations

Busuanga Tower provides aerodrome control only, and the aerodrome operates VFR. On first contact, give your parking position and aircraft type, and request your departure clearance. There is no radar approach service; expect a visual approach to the runway in use.

!!! warning

    With a single runway, terrain all around and no radar service, fly the circuit accurately and maintain a good lookout. Never enter or backtrack the runway until you have been explicitly cleared to do so. Read back any hold short instruction with **"HOLDING SHORT"**.

??? phraseology "Phraseology"

    **RP-C123**: Busuanga Tower, RP-C123, GA apron, request taxi, runway 26.

    **RPVV_TWR**: RP-C123, taxi to holding point runway 26.

    **RP-C123**: Taxi to holding point runway 26, RP-C123.

## VFR Area Chart

![RPVV VFR Area Chart](../../../assets/img/RPVV%20VFR/VFR%20Area%20Chart%20RPVV.png)

The chart shows the published VFR **arrival** (magenta) and **departure** (blue) routes and the visual reporting points around Busuanga.

## Traffic Circuit

!!! warning "Terrain"

    Busuanga is surrounded by high terrain. Fly the circuit accurately and do not exceed the ATZ vertical limit (below 3000 FT).

=== "RWY 08"

    ![RPVV Traffic Circuit RWY 08](../../../assets/img/RPVV%20VFR/Traffic%20Circuit%20RWY%2008.png)

    **Left-hand circuit.** Aircraft at **105 KT or less** fly the inner circuit (1.0 NM from the runway); aircraft at **106 KT or more** fly the outer circuit (2.0 NM).

=== "RWY 26"

    ![RPVV Traffic Circuit RWY 26](../../../assets/img/RPVV%20VFR/Traffic%20Circuit%20RWY%2026.png)

    **Right-hand circuit.** Aircraft at **105 KT or less** fly the inner circuit (1.0 NM from the runway); aircraft at **106 KT or more** fly the outer circuit (2.0 NM).

!!! info "Circuit entry and exit"

    - **Arriving aircraft** shall enter the traffic circuit on the **downwind leg at an angle of 45 degrees**.
    - **Departing aircraft** shall follow the traffic circuit and **leave the circuit at an angle of 45 degrees**.

*[ATZ]: Aerodrome Traffic Zone
*[CTR]: Control Zone
*[VFR]: Visual Flight Rules
*[RPVV_TWR]: Busuanga Tower
