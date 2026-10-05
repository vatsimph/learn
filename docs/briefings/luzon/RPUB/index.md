# RPUB - Loakan (Baguio) Airport

<div class="metar-widget" data-icao="RPUB">
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

<div class="metar-loading" id="metar-loading-RPUB">Fetching METAR...</div>
<div class="metar-card" id="metar-card-RPUB" style="display:none;"></div>
</div>

<script>
(function () {
  var ICAO = "RPUB";
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
Loakan Airport (RPUB), also known as Baguio Airport, is a Class 2 principal airport located in Loakan, Baguio City, Benguet. It has a single runway (09/27) and serves domestic passenger flights and general aviation.

- Main Terminal - Domestic Flights

The airport caters to passenger flights and general aviation.

!!! warning "High-elevation mountain airport"

    Baguio sits at **4251 FT** in mountainous terrain, with a short 1566 M runway. Expect reduced aircraft performance (density altitude), terrain on all approaches, and often marginal mountain weather. Plan carefully.

!!! note "Airspace"

    - **Baguio ATZ** — 5 NM arc centered on the ARP, surface up to but excluding 2000 FT AGL (Class B). Aerodrome control is provided by **Baguio Tower (RPUB_TWR)**.
    - There is no control zone, terminal area, or approach-control service at Baguio; it is a tower-only aerodrome.
    - **Transition altitude:** not published.

## Charts
<div class="chart-picker" data-icao="RPUB"></div>

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
      <td style="text-align:center"><strong>RPUB_TWR</strong></td>
      <td style="text-align:center">Baguio Tower</td>
      <td style="text-align:center">123.500</td>
      <td style="text-align:center">ATZ SFC - 2000 ft AGL</td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>Unicom</strong></td>
      <td style="text-align:center">—</td>
      <td style="text-align:center">121.900</td>
      <td style="text-align:center">When Baguio Tower is offline</td>
    </tr>
  </tbody>
</table>

## Runways

<div markdown="1">
Baguio currently has 1 runway (09/27), 1566 x 36 M, concrete.

Runway 27 is served by a PAPI; runway 09 has no visual glide-slope guidance. There are no approach lights. The runway slopes uphill towards the threshold of runway 27 (THR 09 elevation 4198 FT, THR 27 elevation 4247 FT).

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
    <tr><td style="text-align:center"><strong>09</strong></td><td style="text-align:center">1566</td><td style="text-align:center">1626</td><td style="text-align:center">1566</td><td style="text-align:center">1566</td></tr>
    <tr><td style="text-align:center"><strong>27</strong></td><td style="text-align:center">1566</td><td style="text-align:center">1686</td><td style="text-align:center">1566</td><td style="text-align:center">1566</td></tr>
  </tbody>
</table>

## Clearance

Baguio Tower provides aerodrome control only, and the aerodrome operates VFR. On first contact, give your parking position and aircraft type, and request your departure clearance.

!!! warning

    Radio Checks on first contact are **discouraged**. Be concise on a controlled frequency, and read back your clearance in full.

??? phraseology

    **RP-C123**: Baguio Tower, RP-C123, GA apron, request VFR departure to the west.

    **RPUB_TWR**: RP-C123, cleared VFR departure to the west not above [altitude], runway 27, squawk 12xx.

    **RP-C123**: Cleared VFR departure to the west not above [altitude], runway 27, squawk 12xx, RP-C123.

## Taxi

The apron connects to runway 09/27. Follow any instruction from Baguio Tower and the apron guide lines. With a single short runway, expect to backtrack to the threshold in use.

!!! warning

    Never enter or backtrack the runway until you have been explicitly cleared to do so. Read back any hold short instruction with **"HOLDING SHORT"**.

??? phraseology "Phraseology"

    **CEB123**: Baguio Tower, CEB123, request taxi, runway 27.

    **RPUB_TWR**: CEB123, taxi to holding point runway 27.

    **CEB123**: Taxi to holding point runway 27, CEB123.

## Departure

Baguio has no approach-control service, so Standard Instrument Departures (**SIDs**) or departure instructions are given by **Baguio Tower**. After departure, remain clear of terrain and climb on your cleared routing; contact the en-route controller (**CTR**) when one is online, otherwise continue to your destination's controlling unit.

??? phraseology "Phraseology"

    **CEB123**: Baguio Tower, CEB123, ready for departure runway 27.

    **RPUB_TWR**: CEB123, runway 27, cleared for take-off, wind calm.

## Arrival

There is no radar approach service at Baguio. Establish contact with **Baguio Tower** on 123.5 MHZ approaching 15 NM inbound, and establish two-way radio contact by 5 NM. Expect a visual approach.

??? phraseology "Phraseology"

    **CEB122**: Baguio Tower, CEB122, 15 miles east, inbound landing.

    **RPUB_TWR**: CEB122, report 5 miles, runway 27, QNH 1012.

    **CEB122**: Report 5 miles, runway 27, QNH 1012, CEB122.

## VFR Area Chart

![RPUB VFR Area Chart](../../../assets/img/RPUB%20VFR/VFR%20Area%20Chart%20RPUB.png)

The chart shows the published VFR **arrival** (magenta) and **departure** (blue) routes and the visual reporting points around Baguio.

## Traffic Circuit

!!! warning "High-altitude aerodrome and terrain"

    Baguio (Loakan) sits at **4,251 FT** elevation, ringed by terrain above 5,000 FT. True airspeeds and groundspeeds are high for a given indicated speed — fly the circuit accurately and remain within the published pattern.

=== "RWY 09"

    ![RPUB Traffic Circuit RWY 09](../../../assets/img/RPUB%20VFR/Traffic%20Circuit%20RWY%2009.png)

    **Left-hand circuit.** Aircraft at **105 KT or less** fly the inner circuit (0.5 NM from the runway); aircraft at **106 KT or more** fly the outer circuit (2.0 NM). A separate helicopter traffic circuit is published.

=== "RWY 27"

    ![RPUB Traffic Circuit RWY 27](../../../assets/img/RPUB%20VFR/Traffic%20Circuit%20RWY%2027.png)

    **Right-hand circuit.** Aircraft at **105 KT or less** fly the inner circuit (0.5 NM from the runway); aircraft at **106 KT or more** fly the outer circuit (2.0 NM). A separate helicopter traffic circuit is published.

!!! info "Circuit entry and exit"

    - **Arriving aircraft** shall enter the traffic circuit on the **downwind leg at an angle of 45 degrees**.
    - **Departing aircraft** shall follow the traffic circuit and **leave the circuit at an angle of 45 degrees**.

*[ATZ]: Aerodrome Traffic Zone
*[AGL]: Above Ground Level
*[SID]: Standard Instrument Departure
*[CTR]: Control Zone
*[RPUB_TWR]: Baguio Tower
