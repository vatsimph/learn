# RPVB - Bacolod Principal Airport

<div class="metar-widget" data-icao="RPVB">
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

<div class="metar-loading" id="metar-loading-RPVB">Fetching METAR...</div>
<div class="metar-card" id="metar-card-RPVB" style="display:none;"></div>
</div>

<script>
(function () {
  var ICAO = "RPVB";
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
Bacolod Principal Airport (RPVB), also known as Bacolod-Silay Airport, is a Class 1 principal airport located in Silay City, Negros Occidental. It has a single runway (03/21) and serves domestic passenger and cargo flights, as well as general aviation.

- Main Terminal - Domestic Flights
- Cargo Terminal - Cargo Flights
- General Aviation Apron

The airport caters to passenger and cargo flights, as well as general aviation.

!!! note "Airspace"

    - **Bacolod ATZ** — surface up to but excluding 2000 FT (Class B). Aerodrome control is provided by **Bacolod Tower (RPVB_TWR)**.
    - **Bacolod CTR** — surface up to 1500 FT (Class D). Controlled by **Bacolod Approach (RPVB_APP)**.
    - **Bacolod/Iloilo TMA** — 1500 FT to FL200 (Class D below FL160, Class A on ATS routes at FL160 and above). Controlled by **Bacolod Approach (RPVB_APP)**.
    - **Transition altitude:** 11,000 FT.
    - **Transponder:** Mode C is required to operate within the Bacolod TMA, except for helicopters flying below 1000 FT AMSL.

## Charts
<div class="chart-picker" data-icao="RPVB"></div>

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
      <td style="text-align:center"><strong>RPVB_ATIS</strong></td>
      <td style="text-align:center">Bacolod ATIS</td>
      <td style="text-align:center">128.600</td>
      <td style="text-align:center"></td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>RPVB_TWR</strong></td>
      <td style="text-align:center">Bacolod Tower</td>
      <td style="text-align:center">118.800</td>
      <td style="text-align:center">ATZ SFC - 2000 ft</td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>RPVB_APP</strong></td>
      <td style="text-align:center">Bacolod Approach</td>
      <td style="text-align:center">121.000</td>
      <td style="text-align:center">Bacolod/Iloilo TMA 1500 ft - FL200</td>
    </tr>
  </tbody>
</table>

## Runways

<div markdown="1">
Bacolod currently has 1 runway (03/21), 2002 x 45 M, concrete.

Both runway ends are served by a PAPI (left, 3.0°). Runway 03 has Precision Approach Lighting (PALS, 900 M) with sequenced flashing lights and a wing-bar threshold; runway 21 has Simple Approach Lighting (SALS, 420 M).

Turning pads (60 M x 67 M) are provided at both runway ends.

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
      <td style="text-align:center"><strong>03</strong></td>
      <td style="text-align:center">2002</td>
      <td style="text-align:center">2642</td>
      <td style="text-align:center">2062</td>
      <td style="text-align:center">2002</td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>21</strong></td>
      <td style="text-align:center">2002</td>
      <td style="text-align:center">2282</td>
      <td style="text-align:center">2062</td>
      <td style="text-align:center">2002</td>
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
      <td style="text-align:center">BCD</td>
      <td style="text-align:center">115.30 / CH100X</td>
      <td style="text-align:center">On the field, east of the runway</td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>ILS RWY 03</strong></td>
      <td style="text-align:center">IBCD</td>
      <td style="text-align:center">109.70 / CH34X</td>
      <td style="text-align:center">Glide path 3.0°</td>
    </tr>
  </tbody>
</table>

## Clearance

On first contact with the controller that will issue your clearance, give
the following information:

- Your parking bay
- Your aircraft type
- The ATIS information letter

!!! warning

    Radio Checks on first contact are **discouraged** when building communication with the controller.
    It's best to greet or ask the controller, should you need any help before clearance issuance.

    Be straightforward and concise as possible when communicating within a controlled frequency.

Once you have requested for clearance, the controller will either tell you to standby, or give your clearance on the spot. Clearances include your routing, flight level restrictions, departure instructions and your squawk.

You must read back the clearance in full. Listen carefully to all details that the controller gives you, and if you are unsure about your clearance, **let the controller know.**

??? phraseology

    **CEB123**: Bacolod Tower, CEB123, Bay 3, A-3-2-0 with information A, request clearance Manila.

    **RPVB_TWR**: CEB123, cleared Manila, [routing], [SID] RUNWAY 03, Climb [initial level], Squawk 4024.

    **CEB123**: Cleared Manila, [routing], [SID] RUNWAY 03, Climb [initial level], Squawk 4024, CEB123.

## Taxi

The apron sits on the west side of the runway and connects to runway 03/21 via two taxiways, **A** and **B**. There is no parallel taxiway, so departing aircraft enter the runway and backtrack to the threshold, turning around on the turning pad at the runway end. Follow the apron taxi guide lines and any instruction from the tower controller / marshaller.

For arrivals, vacate via the taxiway given by ATC. If you roll past both taxiways, expect to turn around on the turning pad at the runway end and backtrack.

Tower clearance is required before moving off your parking bay, and pushback and engine start are only done on the designated positions **S1** and **S2**. Parking bays 1 to 5 are for A320 and smaller aircraft (bay 3 takes up to an A330); bays 6 and 7 are for turboprops with a wingspan of no more than 29 M and a length of no more than 33 M.

!!! warning

    Never enter or backtrack the runway until you have been explicitly cleared to do so. Read back any hold short instruction with **"HOLDING SHORT"**.

??? phraseology "Phraseology"

    **CEB123**: Bacolod Tower, CEB123, Bay 3, request taxi, runway 03.

    **RPVB_TWR**: CEB123, taxi to holding point runway 03 via A.

    **CEB123**: Holding point runway 03 via A, CEB123.

    **RPVB_TWR**: CEB123, backtrack and line up runway 03.

    **CEB123**: Backtrack and line up runway 03, CEB123.

## Departure

The departure procedure is decided by an online Approach (**APP**) or En-route Controller (**CTR**). When both are offline, Standard Instrument Departures (**SIDs**) are given by the aerodrome controller (**TWR**). When either **APP** or **CTR** is online, they decide if departures will be given radar vectors to the TMA exit points or will be following a **SID**.

When **APP** or **CTR** is online, after passing 2000 feet or leaving the control zone, report your passing altitude to **APP** or **CTR**. This is to help them identify you successfully in their radar screens.

??? phraseology "Phraseology"

    **CEB123**: Bacolod Approach, CEB123, passing 2000, climbing [initial level].

    **RPVB_APP**: CEB123, radar identified, continue climb FL150.

## Arrival

When arriving into Bacolod, plan your descent to meet the level restrictions on your STAR. On initial contact with Bacolod Approach (RPVB_APP), report your current level.

??? phraseology "Phraseology"

    **CEB122**: Bacolod Approach, CEB122, FL150.

APP will then issue your arrival clearance including the type of approach to expect to the active runway. APP either gives you radar vectors to final or gives you descent clearances via a STAR. Runway 03 is served by an ILS; RNP and VOR approaches are published for both runways.

??? phraseology "Phraseology"

    **RPVB_APP**: CEB122, radar contact, cleared Bacolod, expect ILS approach RWY 03.

    **CEB122**: Cleared Bacolod, expect ILS approach RWY 03, CEB122.

    **RPVB_APP**: CEB122, maintain present heading, descend 5,000, QNH 1012.

    **CEB122**: Maintain present heading, descend 5,000, QNH 1012, CEB122.

!!! warning

    If APP didn't give you any turns after you have passed the last waypoint on your routing, maintain your present heading.

*[GA]: General Aviation
*[ATZ]: Aerodrome Traffic Zone
*[CTR]: Control Zone
*[TMA]: Terminal Control Area
*[SID]: Standard Instrument Departure
*[STAR]: Standard Terminal Arrival Route
*[RPVB_TWR]: Bacolod Tower
*[RPVB_ATIS]: Bacolod ATIS
*[RPVB_APP]: Bacolod Approach
