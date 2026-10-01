# RPVA - Daniel Z. Romualdez Airport

<div class="metar-widget" data-icao="RPVA">
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

<div class="metar-loading" id="metar-loading-RPVA">Fetching METAR...</div>
<div class="metar-card" id="metar-card-RPVA" style="display:none;"></div>
</div>

<script>
(function () {
  var ICAO = "RPVA";
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
Daniel Z. Romualdez Airport (RPVA), also known as Tacloban Airport, is a Class 1 principal airport located in San Jose, Tacloban City, Leyte, about 3.5 KM southeast of the city center. It has a single runway (18/36) and serves domestic passenger and cargo flights, as well as general aviation.

- Main Terminal - Domestic Flights

The airport caters to passenger and cargo flights, as well as general and military aviation.

!!! warning "Bird activity"

    Exercise extreme caution during landing and take-off on RWY 18/36 due to concentration of birds at the aerodrome.

!!! note "Airspace"

    - **Tacloban ATZ** — circle 5 NM radius centered on the ARP, surface up to but excluding 2000 FT (Class B). Aerodrome control is provided by **Tacloban Tower (RPVA_TWR)**.
    - **Tacloban CTR** — circle 10 NM radius centered on the TAC DVOR/DME, surface up to 1500 FT (Class D). Controlled by **Tacloban Approach (RPVA_APP)**.
    - **Tacloban TMA** — 1500 FT to FL200 (Class D below FL160, Class A on ATS routes at FL160 and above). Controlled by **Tacloban Approach (RPVA_APP)**.
    - **Transition altitude:** 11,000 FT.

## Charts
<div class="chart-picker" data-icao="RPVA"></div>

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
      <td style="text-align:center"><strong>RPVA_TWR</strong></td>
      <td style="text-align:center">Tacloban Tower</td>
      <td style="text-align:center">124.300</td>
      <td style="text-align:center">ATZ SFC - 2000 ft</td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>RPVA_APP</strong></td>
      <td style="text-align:center">Tacloban Approach</td>
      <td style="text-align:center">120.800</td>
      <td style="text-align:center">Tacloban TMA 1500 ft - FL200</td>
    </tr>
  </tbody>
</table>

## Runways

<div markdown="1">
Tacloban currently has 1 runway (18/36), 2142 x 45 M, asphalt.

Both runway ends are served by a PAPI (left, 3.0°) and runway threshold identification lights (RTIL, flashing white). There are no approach lights or runway centre line lights.

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
      <td style="text-align:center"><strong>18</strong></td>
      <td style="text-align:center">2142</td>
      <td style="text-align:center">2262</td>
      <td style="text-align:center">2142</td>
      <td style="text-align:center">2142</td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>36</strong></td>
      <td style="text-align:center">2142</td>
      <td style="text-align:center">2217</td>
      <td style="text-align:center">2142</td>
      <td style="text-align:center">2142</td>
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
      <td style="text-align:center">TAC</td>
      <td style="text-align:center">115.50 / CH102X</td>
      <td style="text-align:center">VOR 60 NM, DME 40 NM</td>
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

    **CEB123**: Tacloban Tower, CEB123, Bay 1, A-3-2-0, request clearance Manila.

    **RPVA_TWR**: CEB123, cleared Manila, [routing], [SID] RUNWAY 18, Climb [initial level], Squawk 4024.

    **CEB123**: Cleared Manila, [routing], [SID] RUNWAY 18, Climb [initial level], Squawk 4024, CEB123.

## Taxi

The main apron connects to runway 18/36 via the **North Taxiway** and the **South Taxiway**. Follow ATC taxi instructions and the apron guide lines. Turn-around pads are provided at both runway ends — avoid tight wheel turns on the runway itself, and use the turn pad to reverse direction.

!!! warning

    Never enter or backtrack the runway until you have been explicitly cleared to do so. Read back any hold short instruction with **"HOLDING SHORT"**.

??? phraseology "Phraseology"

    **CEB123**: Tacloban Tower, CEB123, Bay 1, request taxi, runway 18.

    **RPVA_TWR**: CEB123, taxi to holding point runway 18 via North Taxiway.

    **CEB123**: Holding point runway 18 via North Taxiway, CEB123.

## Departure

The departure procedure is decided by an online Approach (**APP**) or En-route Controller (**CTR**). When both are offline, Standard Instrument Departures (**SIDs**) are given by the aerodrome controller (**TWR**). When either **APP** or **CTR** is online, they decide if departures will be given radar vectors to the TMA exit points or will be following a **SID**.

When **APP** or **CTR** is online, after passing 2000 feet or leaving the control zone, report your passing altitude to **APP** or **CTR**. This is to help them identify you successfully in their radar screens.

??? phraseology "Phraseology"

    **CEB123**: Tacloban Approach, CEB123, passing 2000, climbing [initial level].

    **RPVA_APP**: CEB123, radar identified, continue climb FL150.

## Arrival

When arriving into Tacloban, plan your descent to meet the level restrictions on your STAR. On initial contact with Tacloban Approach (RPVA_APP), report your current level.

??? phraseology "Phraseology"

    **CEB122**: Tacloban Approach, CEB122, FL150.

APP will then issue your arrival clearance including the type of approach to expect to the active runway. APP either gives you radar vectors to final or gives you descent clearances via a STAR. Runway 36 is served by VOR and RNP approaches; runway 18 has an RNP approach.

??? phraseology "Phraseology"

    **RPVA_APP**: CEB122, radar contact, cleared Tacloban, expect RNP approach RWY 36.

    **CEB122**: Cleared Tacloban, expect RNP approach RWY 36, CEB122.

    **RPVA_APP**: CEB122, maintain present heading, descend 5,000, QNH 1012.

    **CEB122**: Maintain present heading, descend 5,000, QNH 1012, CEB122.

!!! warning

    If APP didn't give you any turns after you have passed the last waypoint on your routing, maintain your present heading.

*[ATZ]: Aerodrome Traffic Zone
*[CTR]: Control Zone
*[TMA]: Terminal Control Area
*[SID]: Standard Instrument Departure
*[STAR]: Standard Terminal Arrival Route
*[RNP]: Required Navigation Performance
*[RPVA_TWR]: Tacloban Tower
*[RPVA_APP]: Tacloban Approach
