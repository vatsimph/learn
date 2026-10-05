# RPLK - Bicol International Airport

<div class="metar-widget" data-icao="RPLK">
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

<div class="metar-loading" id="metar-loading-RPLK">Fetching METAR...</div>
<div class="metar-card" id="metar-card-RPLK" style="display:none;"></div>
</div>

<script>
(function () {
  var ICAO = "RPLK";
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
Bicol International Airport (RPLK), also known as Bicol Airport, is a Class 1 principal airport located in Barangay Alobo, Daraga, Albay, about 5.5 KM south-southwest of Daraga. It has a single runway (05/23) and serves domestic passenger and cargo flights, as well as general aviation. It replaced the former Legazpi Airport.

- Main Terminal - Domestic Flights
- Cargo Terminal - Cargo Flights

The airport caters to passenger and cargo flights, as well as general aviation.

!!! airspace "Airspace"

    - **Bicol ATZ** — circle 5 NM radius centered on the ARP, surface up to but excluding 2000 FT (Class B). Aerodrome control is provided by **Bicol Tower (RPLK_TWR)**.
    - **Bicol CTR** — circle 10 NM radius centered on the ARP, surface up to 1500 FT (Class D). Controlled by **Bicol Approach (RPLK_APP)**.
    - **Legazpi TMA** — 1500 FT to FL200 (Class D below FL130, Class A on ATS routes at FL130 and above). Controlled by **Bicol Approach (RPLK_APP)**.
    - **Transition altitude:** 11,000 FT.

## Charts
<div class="chart-picker" data-icao="RPLK"></div>

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
      <td style="text-align:center"><strong>RPLK_TWR</strong></td>
      <td style="text-align:center">Bicol Tower</td>
      <td style="text-align:center">118.700</td>
      <td style="text-align:center">ATZ SFC - 2000 ft</td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>RPLK_APP</strong></td>
      <td style="text-align:center">Bicol Approach</td>
      <td style="text-align:center">120.200</td>
      <td style="text-align:center">Legazpi TMA 1500 ft - FL200 (Legazpi Approach in the AIP)</td>
    </tr>
  </tbody>
</table>

## Runways

<div markdown="1">
Bicol currently has 1 runway (05/23), 2500 x 45 M, concrete.

Both runway ends are served by a PAPI and runway threshold identification lights (RTIL, flashing white). Runway 05 has a PAPI on the left at 3.0°; runway 23 has a PAPI at 3.5°. There are no approach lights or runway centre line lights. Both thresholds are displaced (RWY 05 by 450 M, RWY 23 by 600 M), which reduces the landing distance available.

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
      <td style="text-align:center"><strong>05</strong></td>
      <td style="text-align:center">2500</td>
      <td style="text-align:center">2500</td>
      <td style="text-align:center">2560</td>
      <td style="text-align:center">2050</td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>23</strong></td>
      <td style="text-align:center">2500</td>
      <td style="text-align:center">2500</td>
      <td style="text-align:center">2560</td>
      <td style="text-align:center">1900</td>
    </tr>
  </tbody>
</table>

!!! note "Navigation"

    Bicol has no ground-based navaids. All instrument procedures are RNP (GNSS): RNP approaches are published for both runways, along with RNP SIDs and STARs.

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

    **CEB123**: Bicol Tower, CEB123, Bay 2, A-3-2-0, request clearance Manila.

    **RPLK_TWR**: CEB123, cleared Manila, [routing], [SID] RUNWAY 05, Climb [initial level], Squawk 4024.

    **CEB123**: Cleared Manila, [routing], [SID] RUNWAY 05, Climb [initial level], Squawk 4024, CEB123.

## Taxi

Bicol has a single runway (05/23) served by connector taxiways (B and C) with no full-length parallel taxiway. Depending on your parking position and the runway in use, expect to enter the runway and backtrack to the threshold. Follow the apron taxi guide lines and any instruction from the tower controller / marshaller.

!!! warning

    Never enter or backtrack the runway until you have been explicitly cleared to do so. Read back any hold short instruction with **"HOLDING SHORT"**.

??? phraseology "Phraseology"

    **CEB123**: Bicol Tower, CEB123, Bay 2, request taxi, runway 05.

    **RPLK_TWR**: CEB123, taxi to holding point runway 05 via B.

    **CEB123**: Holding point runway 05 via B, CEB123.

    **RPLK_TWR**: CEB123, backtrack and line up runway 05.

    **CEB123**: Backtrack and line up runway 05, CEB123.

## Departure

The departure procedure is decided by an online Approach (**APP**) or En-route Controller (**CTR**). When both are offline, Standard Instrument Departures (**SIDs**) are given by the aerodrome controller (**TWR**). When either **APP** or **CTR** is online, they decide if departures will be given radar vectors to the TMA exit points or will be following a **SID**.

When **APP** or **CTR** is online, after passing 2000 feet or leaving the control zone, report your passing altitude to **APP** or **CTR**. This is to help them identify you successfully in their radar screens.

??? phraseology "Phraseology"

    **CEB123**: Bicol Approach, CEB123, passing 2000, climbing [initial level].

    **RPLK_APP**: CEB123, radar identified, continue climb FL150.

## Arrival

When arriving into Bicol, plan your descent to meet the level restrictions on your STAR. On initial contact with Bicol Approach (RPLK_APP), report your current level.

??? phraseology "Phraseology"

    **CEB122**: Bicol Approach, CEB122, FL150.

APP will then issue your arrival clearance including the type of approach to expect to the active runway. APP either gives you radar vectors to final or gives you descent clearances via a STAR. Both runways are served by RNP approaches.

??? phraseology "Phraseology"

    **RPLK_APP**: CEB122, radar contact, cleared Bicol, expect RNP approach RWY 05.

    **CEB122**: Cleared Bicol, expect RNP approach RWY 05, CEB122.

    **RPLK_APP**: CEB122, maintain present heading, descend 5,000, QNH 1012.

    **CEB122**: Maintain present heading, descend 5,000, QNH 1012, CEB122.

!!! warning

    If APP didn't give you any turns after you have passed the last waypoint on your routing, maintain your present heading.

*[GA]: General Aviation
*[ATZ]: Aerodrome Traffic Zone
*[CTR]: Control Zone
*[TMA]: Terminal Control Area
*[SID]: Standard Instrument Departure
*[STAR]: Standard Terminal Arrival Route
*[RNP]: Required Navigation Performance
*[RPLK_TWR]: Bicol Tower
*[RPLK_APP]: Bicol Approach
