# RPMZ - Zamboanga International Airport

<div class="metar-widget" data-icao="RPMZ">
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

<div class="metar-loading" id="metar-loading-RPMZ">Fetching METAR...</div>
<div class="metar-card" id="metar-card-RPMZ" style="display:none;"></div>
</div>

<script>
(function () {
  var ICAO = "RPMZ";
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
Zamboanga International Airport (RPMZ), also known as Zamboanga Airport, is a Class 1 principal airport located in Baliwasan, Zamboanga City, about 3 KM northwest of the city. It has a single runway (09/27) and serves domestic and international passenger and cargo flights, as well as general and military aviation.

- Main Terminal - Domestic and International Flights

The airport caters to passenger and cargo flights, as well as general and military aviation.

!!! note "Airspace"

    - **Zamboanga ATZ** — circle 5 NM radius centered on the ARP, surface up to but excluding 2000 FT (Class B). Aerodrome control is provided by **Zamboanga Tower (RPMZ_TWR)**.
    - **Zamboanga CTR** — circle 10 NM radius centered on the ZAM DVOR/DME, surface up to 1500 FT (Class D). Controlled by **Zamboanga Approach (RPMZ_APP)**.
    - **Zamboanga TMA** — circle 25 NM radius centered on the ZAM DVOR/DME, 1500 FT to FL200 (Class D below FL160, Class A on ATS routes at FL160 and above). Controlled by **Zamboanga Approach (RPMZ_APP)**.
    - **Transition altitude:** 11,000 FT.

## Charts
<div class="chart-picker" data-icao="RPMZ"></div>

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
      <td style="text-align:center"><strong>RPMZ_TWR</strong></td>
      <td style="text-align:center">Zamboanga Tower</td>
      <td style="text-align:center">123.500</td>
      <td style="text-align:center">ATZ SFC - 2000 ft</td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>RPMZ_APP</strong></td>
      <td style="text-align:center">Zamboanga Approach</td>
      <td style="text-align:center">122.700</td>
      <td style="text-align:center">Zamboanga TMA 1500 ft - FL200</td>
    </tr>
  </tbody>
</table>

## Runways

<div markdown="1">
Zamboanga currently has 1 runway (09/27), 2609 x 44 M, concrete and asphalt.

Both runway ends are served by a PAPI (3.0°) and runway threshold identification lights (RTIL, flashing white). Runway 27 also has Simple Approach Lighting (SALS, 420 M). The runway has a slight upslope (0.167%) towards the threshold of runway 27.

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
    <tr><td style="text-align:center"><strong>09</strong></td><td style="text-align:center">2609</td><td style="text-align:center">2690</td><td style="text-align:center">2609</td><td style="text-align:center">2609</td></tr>
    <tr><td style="text-align:center"><strong>27</strong></td><td style="text-align:center">2609</td><td style="text-align:center">2685</td><td style="text-align:center">2609</td><td style="text-align:center">2609</td></tr>
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
      <td style="text-align:center">ZAM</td>
      <td style="text-align:center">113.90 / CH86X</td>
      <td style="text-align:center">On the field; coverage 50 NM</td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>ILS/LOC RWY 09</strong></td>
      <td style="text-align:center">—</td>
      <td style="text-align:center">—</td>
      <td style="text-align:center">ILS or LOC approach to runway 09</td>
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

    **CEB123**: Zamboanga Tower, CEB123, Bay 1, A-3-2-0, request clearance Manila.

    **RPMZ_TWR**: CEB123, cleared Manila, [routing], [SID] RUNWAY 09, Climb [initial level], Squawk 4024.

    **CEB123**: Cleared Manila, [routing], [SID] RUNWAY 09, Climb [initial level], Squawk 4024, CEB123.

## Taxi

The apron connects to runway 09/27 via its taxiways. Follow the apron taxi guide lines and any instruction from the ground controller / marshaller.

!!! warning

    Never enter or backtrack the runway until you have been explicitly cleared to do so. Read back any hold short instruction with **"HOLDING SHORT"**.

??? phraseology "Phraseology"

    **CEB123**: Zamboanga Tower, CEB123, Bay 1, request taxi, runway 09.

    **RPMZ_TWR**: CEB123, taxi to holding point runway 09.

    **CEB123**: Taxi to holding point runway 09, CEB123.

## Departure

The departure procedure is decided by an online Approach (**APP**) or En-route Controller (**CTR**). When both are offline, Standard Instrument Departures (**SIDs**) are given by the aerodrome controller (**TWR**). When either **APP** or **CTR** is online, they decide if departures will be given radar vectors to the TMA exit points or will be following a **SID**.

When **APP** or **CTR** is online, after passing 2000 feet or leaving the control zone, report your passing altitude to **APP** or **CTR**. This is to help them identify you successfully in their radar screens.

??? phraseology "Phraseology"

    **CEB123**: Zamboanga Approach, CEB123, passing 2000, climbing [initial level].

    **RPMZ_APP**: CEB123, radar identified, continue climb FL150.

## Arrival

When arriving into Zamboanga, plan your descent to meet the level restrictions on your STAR. On initial contact with Zamboanga Approach (RPMZ_APP), report your current level.

??? phraseology "Phraseology"

    **CEB122**: Zamboanga Approach, CEB122, FL150.

APP will then issue your arrival clearance including the type of approach to expect to the active runway. APP either gives you radar vectors to final or gives you descent clearances via a STAR. Runway 09 is served by an ILS; DVOR/DME, VOR and RNP approaches are published for both runways.

??? phraseology "Phraseology"

    **RPMZ_APP**: CEB122, radar contact, cleared Zamboanga, expect ILS approach RWY 09.

    **CEB122**: Cleared Zamboanga, expect ILS approach RWY 09, CEB122.

    **RPMZ_APP**: CEB122, maintain present heading, descend 5,000, QNH 1012.

    **CEB122**: Maintain present heading, descend 5,000, QNH 1012, CEB122.

!!! warning

    If APP didn't give you any turns after you have passed the last waypoint on your routing, maintain your present heading.

*[ATZ]: Aerodrome Traffic Zone
*[CTR]: Control Zone
*[TMA]: Terminal Control Area
*[SID]: Standard Instrument Departure
*[STAR]: Standard Terminal Arrival Route
*[ILS]: Instrument Landing System
*[RNP]: Required Navigation Performance
*[RPMZ_TWR]: Zamboanga Tower
*[RPMZ_APP]: Zamboanga Approach
