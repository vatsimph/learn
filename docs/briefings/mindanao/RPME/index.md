# RPME - Bancasi Airport

<div class="metar-widget" data-icao="RPME">
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

<div class="metar-loading" id="metar-loading-RPME">Fetching METAR...</div>
<div class="metar-card" id="metar-card-RPME" style="display:none;"></div>
</div>

<script>
(function () {
  var ICAO = "RPME";
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
Bancasi Airport (RPME), also known as Butuan Airport, is a Class 1 principal airport located in Bancasi, Butuan City, Agusan del Norte, about 5.35 KM from the city. It has a single runway (12/30) and serves domestic passenger and cargo flights, as well as general aviation.

- Main Terminal - Domestic Flights

The airport caters to passenger and cargo flights, as well as general aviation.

!!! warning "Bird activity"

    Exercise caution during landing and take-off on RWY 12/30 due to the presence of birds in the vicinity of the airport.

!!! note "Airspace"

    - **Butuan ATZ** — circle 5 NM radius centered on the ARP, surface up to but excluding 2000 FT (Class B). Aerodrome control is provided by **Butuan Tower (RPME_TWR)**.
    - **Butuan CTR** — circle 10 NM radius centered on the ARP, surface up to 1500 FT (Class D). Controlled by **Butuan Approach (RPME_APP)**.
    - **Butuan TMA** — 1500 FT to FL200 (Class D below FL160, Class A on ATS routes at FL160 and above). Controlled by **Butuan Approach (RPME_APP)**.
    - **Transition altitude:** 11,000 FT.

## Charts
<div class="chart-picker" data-icao="RPME"></div>

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
      <td style="text-align:center"><strong>RPME_TWR</strong></td>
      <td style="text-align:center">Butuan Tower</td>
      <td style="text-align:center">123.200</td>
      <td style="text-align:center">ATZ SFC - 2000 ft</td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>RPME_APP</strong></td>
      <td style="text-align:center">Butuan Approach</td>
      <td style="text-align:center">121.300</td>
      <td style="text-align:center">Butuan TMA 1500 ft - FL200</td>
    </tr>
  </tbody>
</table>

## Runways

<div markdown="1">
Butuan currently has 1 runway (12/30), 2096 x 45 M, concrete and asphalt.

Both runway ends are served by a PAPI (left, 3.0°) and Simple Approach Lighting (SALS): 300 M on runway 12, 360 M on runway 30. The runway has a slight upslope (0.25%) towards the threshold of runway 30.

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
    <tr>
      <td style="text-align:center"><strong>12</strong></td>
      <td style="text-align:center">2096</td>
      <td style="text-align:center">2256</td>
      <td style="text-align:center">2156</td>
      <td style="text-align:center">2096</td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>30</strong></td>
      <td style="text-align:center">2096</td>
      <td style="text-align:center">2236</td>
      <td style="text-align:center">2156</td>
      <td style="text-align:center">2096</td>
    </tr>
  </tbody>
</table>

## Navigation Aids
<table>
  <thead>
    <tr>
      <th style="text-align:center">Aid</th>
      <th style="text-align:center">Ident</th>
      <th style="text-align:center">Frequency</th>
      <th style="text-align:center">Remarks</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:center"><strong>DVOR/DME</strong></td>
      <td style="text-align:center">BN</td>
      <td style="text-align:center">112.50 / CH72X</td>
      <td style="text-align:center">On the field, 300 M left of centre line</td>
    </tr>
  </tbody>
</table>

## Clearance

On first contact with the controller that will issue your clearance, give
the following information:

- Your parking bay
- Your aircraft type

!!! warning

    Radio Checks on first contact are **discouraged** when building communication with the controller.
    It's best to greet or ask the controller, should you need any help before clearance issuance.

    Be straightforward and concise as possible when communicating within a controlled frequency.

Once you have requested for clearance, the controller will either tell you to standby, or give your clearance on the spot. Clearances include your routing, flight level restrictions, departure instructions and your squawk.

You must read back the clearance in full. Listen carefully to all details that the controller gives you, and if you are unsure about your clearance, **let the controller know.**

??? phraseology

    **CEB123**: Butuan Tower, CEB123, Bay 1, A-3-2-0, request clearance Manila.

    **RPME_TWR**: CEB123, cleared Manila, [routing], [SID] RUNWAY 12, Climb [initial level], Squawk 4024.

    **CEB123**: Cleared Manila, [routing], [SID] RUNWAY 12, Climb [initial level], Squawk 4024, CEB123.

## Taxi

The apron connects to runway 12/30 via two taxiways, **TWY East** and **TWY West**. Follow ATC taxi instructions and the apron guide lines. Turn-around pads are provided at both runway ends — avoid tight wheel turns on the runway itself, and use the turn pad to reverse direction.

!!! warning

    Never enter or backtrack the runway until you have been explicitly cleared to do so. Read back any hold short instruction with **"HOLDING SHORT"**.

??? phraseology "Phraseology"

    **CEB123**: Butuan Tower, CEB123, Bay 1, request taxi, runway 12.

    **RPME_TWR**: CEB123, taxi to holding point runway 12 via TWY East.

    **CEB123**: Holding point runway 12 via TWY East, CEB123.

## Departure

The departure procedure is decided by an online Approach (**APP**) or En-route Controller (**CTR**). When both are offline, Standard Instrument Departures (**SIDs**) are given by the aerodrome controller (**TWR**). When either **APP** or **CTR** is online, they decide if departures will be given radar vectors to the TMA exit points or will be following a **SID**.

When **APP** or **CTR** is online, after passing 2000 feet or leaving the control zone, report your passing altitude to **APP** or **CTR**. This is to help them identify you successfully in their radar screens.

??? phraseology "Phraseology"

    **CEB123**: Butuan Approach, CEB123, passing 2000, climbing [initial level].

    **RPME_APP**: CEB123, radar identified, continue climb FL150.

## Arrival

When arriving into Butuan, plan your descent to meet the level restrictions on your STAR. On initial contact with Butuan Approach (RPME_APP), report your current level.

??? phraseology "Phraseology"

    **CEB122**: Butuan Approach, CEB122, FL150.

APP will then issue your arrival clearance including the type of approach to expect to the active runway. APP either gives you radar vectors to final or gives you descent clearances via a STAR. Both runways are served by RNP approaches.

??? phraseology "Phraseology"

    **RPME_APP**: CEB122, radar contact, cleared Butuan, expect RNP approach RWY 12.

    **CEB122**: Cleared Butuan, expect RNP approach RWY 12, CEB122.

    **RPME_APP**: CEB122, maintain present heading, descend 5,000, QNH 1012.

    **CEB122**: Maintain present heading, descend 5,000, QNH 1012, CEB122.

!!! warning

    If APP didn't give you any turns after you have passed the last waypoint on your routing, maintain your present heading.

*[ATZ]: Aerodrome Traffic Zone
*[CTR]: Control Zone
*[TMA]: Terminal Control Area
*[SID]: Standard Instrument Departure
*[STAR]: Standard Terminal Arrival Route
*[RNP]: Required Navigation Performance
*[RPME_TWR]: Butuan Tower
*[RPME_APP]: Butuan Approach
