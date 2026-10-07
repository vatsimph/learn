# RPUX - Plaridel Airport

<div class="metar-widget" data-icao="RPUX">
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

<div class="metar-loading" id="metar-loading-RPUX">Fetching METAR...</div>
<div class="metar-card" id="metar-card-RPUX" style="display:none;"></div>
</div>

<script>
(function () {
  var ICAO = "RPUX";
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
Plaridel Airport (RPUX) is a community airport in Barangay Lumang Bayan, Plaridel, Bulacan, in Central Luzon just north of Manila. It is one of the country's busiest **general-aviation and flight-training** fields, home to several flying schools, and has a single runway (17/35).

The airport reference point (ARP) is 145330N 1205111E, aerodrome elevation 20 FT (6 M).

!!! warning "Busy training circuit"

    Expect intense **VFR circuit traffic** — multiple light aircraft in the pattern practising take-offs and landings. Fly an accurate circuit, keep a constant lookout, and make concise, standard radio calls.

!!! airspace "Airspace"

    - **Plaridel ATZ** — circle 5 NM radius centered on the ARP, surface up to but excluding 2000 FT (Class B). Aerodrome control is provided by **Plaridel Tower (RPUX_TWR)**.
    - There is no approach-control or radar service; it is a tower-only aerodrome. Manila's airspace (RPLL TMA) lies immediately to the south, so remain clear unless coordinated.
    - **Overflying traffic** must fly at least **2500 FT** and remain **5 NM abeam** (east or west) of the ATZ.
    - **Transition altitude:** not published.

## Charts
<div class="chart-picker" data-icao="RPUX"></div>

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
      <td style="text-align:center"><strong>RPUX_TWR</strong></td>
      <td style="text-align:center">Plaridel Tower</td>
      <td style="text-align:center">122.400</td>
      <td style="text-align:center">ATZ SFC - 2000 ft</td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>Unicom</strong></td>
      <td style="text-align:center">—</td>
      <td style="text-align:center">122.800</td>
      <td style="text-align:center">When Plaridel Tower is offline</td>
    </tr>
  </tbody>
</table>

## Runways

<div markdown="1">
Plaridel has a single runway (17/35), 900 x 30 M, asphalt, PCN 8/F/C/Y/U. The runway slopes very slightly uphill to the south. There are no approach lights and no instrument approach; operations are **VFR by day** only. Due to the short runway and busy pattern, expect to backtrack to the threshold in use.

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
    <tr><td style="text-align:center"><strong>17</strong></td><td style="text-align:center">900</td><td style="text-align:center">930</td><td style="text-align:center">930</td><td style="text-align:center">900</td></tr>
    <tr><td style="text-align:center"><strong>35</strong></td><td style="text-align:center">900</td><td style="text-align:center">910</td><td style="text-align:center">910</td><td style="text-align:center">900</td></tr>
  </tbody>
</table>

## Clearance

Plaridel Tower provides aerodrome control only, and the aerodrome operates VFR. On first contact, give your parking position and aircraft type, and request your departure clearance.

!!! warning

    Radio Checks on first contact are **discouraged**. Be concise on a busy frequency, and read back your clearance in full.

??? phraseology

    **RP-C123**: Plaridel Tower, RP-C123, GA apron, request VFR departure to the north.

    **RPUX_TWR**: RP-C123, cleared VFR departure to the north not above [altitude], runway 35, squawk 12xx.

    **RP-C123**: Cleared VFR departure to the north not above [altitude], runway 35, squawk 12xx, RP-C123.

## Taxi

The apron connects to runway 17/35. Follow any instruction from Plaridel Tower and the apron guide lines. With a single short runway, expect to backtrack to the threshold in use.

!!! warning

    Never enter or backtrack the runway until you have been explicitly cleared to do so. Read back any hold short instruction with **"HOLDING SHORT"**.

??? phraseology "Phraseology"

    **RP-C123**: Plaridel Tower, RP-C123, request taxi, runway 35.

    **RPUX_TWR**: RP-C123, taxi to holding point runway 35.

    **RP-C123**: Taxi to holding point runway 35, RP-C123.

## Departure

Plaridel has no approach-control service. Departure instructions are given by **Plaridel Tower**. After departure, climb on your cleared routing and leave the ATZ as instructed. Departing VFR flights must maintain a continuous listening watch on **122.4 MHZ up to 10 NM**. After leaving the Tower's frequency it is highly suggested to **monitor Manila Control (CTR)** when one is online for traffic information, and remain clear of the Manila TMA to the south.

??? phraseology "Phraseology"

    **RP-C123**: Plaridel Tower, RP-C123, ready for departure runway 35.

    **RPUX_TWR**: RP-C123, runway 35, cleared for take-off, wind calm.

## Arrival

There is no radar approach service at Plaridel. Establish contact with **Plaridel Tower** on 122.4 MHZ **at least 15 NM inbound**, expect to join the traffic circuit, and expect a visual approach to the runway in use. Be prepared to sequence behind training traffic in the pattern.

??? phraseology "Phraseology"

    **RP-C122**: Plaridel Tower, RP-C122, 15 miles north, inbound landing.

    **RPUX_TWR**: RP-C122, join left downwind runway 35, report downwind, QNH 1012.

    **RP-C122**: Join left downwind runway 35, wilco, QNH 1012, RP-C122.

## VFR Area Chart

![RPUX VFR Area Chart](../../../assets/img/RPUX%20VFR/VFR%20Area%20Chart%20RPUX.png)

The chart shows the published VFR **arrival** (magenta), **departure** (blue) and **overflight** (dashed) routes and the visual reporting points within the 5 NM ATZ. (The AIP titles this the *Helicopter Route Chart*, but the routes and reporting points apply to VFR traffic generally.) All altitudes are in feet.

## Visual Landmarks and Reporting Points

<table>
  <thead>
    <tr>
      <th style="text-align:center">Reporting Point</th>
      <th style="text-align:center">Coordinates</th>
      <th style="text-align:center">Distance from ARP (NM)</th>
      <th style="text-align:center">Relative Position</th>
      <th style="text-align:center">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="text-align:center"><strong>APALIT</strong></td><td style="text-align:center">145707N 1204535E</td><td style="text-align:center">6.5</td><td style="text-align:center">NW</td><td style="text-align:center">Apalit Public Market</td></tr>
    <tr><td style="text-align:center"><strong>BALIUAG</strong></td><td style="text-align:center">145744N 1205350E</td><td style="text-align:center">4.9</td><td style="text-align:center">NE</td><td style="text-align:center">Puregold Baliuag</td></tr>
    <tr><td style="text-align:center"><strong>BALIUAG PURINA</strong></td><td style="text-align:center">145545N 1205224E</td><td style="text-align:center">2.5</td><td style="text-align:center">NE</td><td style="text-align:center">Cargill (formerly Purina), Baliuag</td></tr>
    <tr><td style="text-align:center"><strong>BOCAUE NLEX TOLL GATE</strong></td><td style="text-align:center">144809N 1205633E</td><td style="text-align:center">7.4</td><td style="text-align:center">SE</td><td style="text-align:center">Bocaue NLEX Toll Gate</td></tr>
    <tr><td style="text-align:center"><strong>MALOLOS FLYOVER</strong></td><td style="text-align:center">145109N 1204858E</td><td style="text-align:center">3.2</td><td style="text-align:center">SW</td><td style="text-align:center">Malolos Flyover</td></tr>
    <tr><td style="text-align:center"><strong>ROBINSON</strong></td><td style="text-align:center">145406N 1205157E</td><td style="text-align:center">1.0</td><td style="text-align:center">NW</td><td style="text-align:center">Robinsons Pulilan</td></tr>
    <tr><td style="text-align:center"><strong>SAN RAFAEL</strong></td><td style="text-align:center">145750N 1205547E</td><td style="text-align:center">6.2</td><td style="text-align:center">NE</td><td style="text-align:center">Angat Bridge, Plaridel Bypass Road</td></tr>
    <tr><td style="text-align:center"><strong>SAN SIMON TOLL GATE</strong></td><td style="text-align:center">145929N 1204456E</td><td style="text-align:center">8.5</td><td style="text-align:center">NW</td><td style="text-align:center">San Simon Toll Gate</td></tr>
    <tr><td style="text-align:center"><strong>SHELL STATION</strong></td><td style="text-align:center">144950N 1205433E</td><td style="text-align:center">4.9</td><td style="text-align:center">SE</td><td style="text-align:center">Shell Station along NLEX, Balagtas, Bulacan</td></tr>
    <tr><td style="text-align:center"><strong>STA RITA TOLL GATE</strong></td><td style="text-align:center">145142N 1205129E</td><td style="text-align:center">1.8</td><td style="text-align:center">S</td><td style="text-align:center">Sta Rita Toll Gate, NLEX</td></tr>
    <tr><td style="text-align:center"><strong>TABANG INTERCHANGE</strong></td><td style="text-align:center">145018N 1205145E</td><td style="text-align:center">3.2</td><td style="text-align:center">S</td><td style="text-align:center">Tabang Interchange, NLEX-SCTEX</td></tr>
    <tr><td style="text-align:center"><strong>TABANG TOLL GATE</strong></td><td style="text-align:center">145015N 1205205E</td><td style="text-align:center">3.4</td><td style="text-align:center">SE</td><td style="text-align:center">Tabang Toll Gate, NLEX-SCTEX</td></tr>
    <tr><td style="text-align:center"><strong>WALTER MART</strong></td><td style="text-align:center">145250N 1205159E</td><td style="text-align:center">1.0</td><td style="text-align:center">SE</td><td style="text-align:center">Walter Mart along Maharlika Highway</td></tr>
  </tbody>
</table>

*[ARP]: Aerodrome Reference Point
*[ATZ]: Aerodrome Traffic Zone
*[TMA]: Terminal Control Area
*[CTR]: Control Zone
*[VFR]: Visual Flight Rules
*[RPUX_TWR]: Plaridel Tower
