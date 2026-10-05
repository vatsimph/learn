# RPUS - San Fernando (Poro Point) Airport

<div class="metar-widget" data-icao="RPUS">
<style>
.metar-widget {
  margin: 1rem 0;
}
.metar-card {
  display: flex;
  flex-direction: column;
  gap: 0.45rem;
  padding: 0.75rem 1rem;
  border: 1px solid var(--md-default-fg-color--lightest);
  border-left: 4px solid var(--md-primary-fg-color, #4051b5);
  border-radius: 4px;
  background: var(--md-code-bg-color);
}
.metar-raw {
  font-family: var(--md-code-font, monospace);
  font-size: 0.75rem;
  line-height: 1.7;
  color: var(--md-default-fg-color);
  white-space: pre-wrap;
  letter-spacing: 0.02em;
}
.metar-loading {
  font-size: 0.75rem;
  color: var(--md-default-fg-color--light);
  letter-spacing: 0.04em;
  padding: 0.25rem 0;
}
</style>

<div class="metar-loading" id="metar-loading-RPUS">Fetching METAR...</div>
<div class="metar-card" id="metar-card-RPUS" style="display:none;"></div>
</div>

<script>
(function () {
  var ICAO = "RPUS";
  var loadingEl = document.getElementById("metar-loading-" + ICAO);
  var cardEl    = document.getElementById("metar-card-" + ICAO);

  function render(metar) {
    cardEl.innerHTML = '<div class="metar-raw">' + metar + '</div>';
    cardEl.style.display = "";
    loadingEl.style.display = "none";
  }

  function renderError(msg) {
    cardEl.innerHTML = '<div class="metar-raw" style="color:#b71c1c;">' + msg + '</div>';
    cardEl.style.display = "";
    loadingEl.style.display = "none";
  }

  function fetchMetar() {
    fetch("https://metar.vatsim.net/" + ICAO + "?format=json")
      .then(function(r) {
        if (!r.ok) throw new Error("HTTP " + r.status);
        return r.json();
      })
      .then(function(data) {
        if (!data || !data.length || !data[0].metar) {
          renderError("No METAR available for " + ICAO + ".");
          return;
        }
        render(data[0].metar);
      })
      .catch(function(e) {
        renderError(e.message || "Network error.");
      });
  }

  fetchMetar();
  setInterval(fetchMetar, 5000);
})();
</script>

## General
San Fernando Airport (RPUS), also known as Poro Point Airport, is a community airport located at Poro Point, San Fernando City, La Union. It has a single runway (01/19) and serves general aviation and occasional domestic flights.

- General aviation and light domestic traffic

!!! note "Airspace"

    - **San Fernando ATZ** — circle 5 NM radius centered on the ARP, surface up to but excluding 2000 FT (Class B). Aerodrome control is provided by **San Fernando Tower (RPUS_TWR)**.
    - There is no control zone, terminal area, or approach-control service at San Fernando; it is a tower-only aerodrome.
    - **Transition altitude:** not published.

## Charts
<div class="chart-picker" data-icao="RPUS"></div>

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
      <td style="text-align:center"><strong>RPUS_TWR</strong></td>
      <td style="text-align:center">San Fernando Tower</td>
      <td style="text-align:center">122.100</td>
      <td style="text-align:center">ATZ SFC - 2000 ft</td>
    </tr>
  </tbody>
</table>

## Runways

<div markdown="1">
San Fernando currently has 1 runway (01/19), 2120 x 45 M, concrete.

Runway 19 is served by a PAPI; runway 01 has no visual glide-slope guidance and a displaced threshold (landing distance available 1319 M on runway 01). There are no approach lights.

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
    <tr><td style="text-align:center"><strong>01</strong></td><td style="text-align:center">2120</td><td style="text-align:center">2180</td><td style="text-align:center">2120</td><td style="text-align:center">1319</td></tr>
    <tr><td style="text-align:center"><strong>19</strong></td><td style="text-align:center">2120</td><td style="text-align:center">2180</td><td style="text-align:center">2120</td><td style="text-align:center">2120</td></tr>
  </tbody>
</table>

## Clearance

San Fernando Tower provides aerodrome control only, and the aerodrome operates VFR. On first contact, give your parking position and aircraft type, and request your departure clearance.

!!! warning

    Radio Checks on first contact are **discouraged**. Be concise on a controlled frequency, and read back your clearance in full.

??? phraseology

    **RP-C123**: San Fernando Tower, RP-C123, GA apron, request VFR departure to the north.

    **RPUS_TWR**: RP-C123, cleared VFR departure to the north not above [altitude], runway 19, squawk 12xx.

    **RP-C123**: Cleared VFR departure to the north not above [altitude], runway 19, squawk 12xx, RP-C123.

## Taxi

The apron connects to runway 01/19. Follow any instruction from San Fernando Tower and the apron guide lines. With a single runway, expect to backtrack to the threshold in use.

!!! warning

    Never enter or backtrack the runway until you have been explicitly cleared to do so. Read back any hold short instruction with **"HOLDING SHORT"**.

??? phraseology "Phraseology"

    **RP-C123**: San Fernando Tower, RP-C123, request taxi, runway 19.

    **RPUS_TWR**: RP-C123, taxi to holding point runway 19.

    **RP-C123**: Taxi to holding point runway 19, RP-C123.

## Departure

San Fernando has no approach-control service. Departure instructions are given by **San Fernando Tower**. After departure, climb on your cleared routing and contact the en-route controller (**CTR**) when one is online, otherwise continue to your destination's controlling unit.

??? phraseology "Phraseology"

    **RP-C123**: San Fernando Tower, RP-C123, ready for departure runway 19.

    **RPUS_TWR**: RP-C123, runway 19, cleared for take-off, wind calm.

## Arrival

There is no radar approach service at San Fernando. Establish contact with **San Fernando Tower** on 122.1 MHZ before entering the ATZ, and expect a visual approach to the runway in use.

??? phraseology "Phraseology"

    **RP-C122**: San Fernando Tower, RP-C122, 10 miles north, inbound landing.

    **RPUS_TWR**: RP-C122, report 5 miles, runway 19, QNH 1012.

    **RP-C122**: Report 5 miles, runway 19, QNH 1012, RP-C122.

*[ATZ]: Aerodrome Traffic Zone
*[CTR]: Control Zone
*[RPUS_TWR]: San Fernando Tower
