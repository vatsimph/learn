# RPVI - Iloilo International Airport

<div class="metar-widget" data-icao="RPVI">
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

<div class="metar-loading" id="metar-loading-RPVI">Fetching METAR...</div>
<div class="metar-card" id="metar-card-RPVI" style="display:none;"></div>
</div>

<script>
(function () {
  var ICAO = "RPVI";
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
Iloilo International Airport (RPVI) is an international airport located in Barangay Gaub, Cabatuan, Iloilo. It has a single runway (02/20) and serves domestic and international passenger and cargo flights, as well as general aviation.

- Main Terminal - Domestic and International Flights
- Cargo Terminal - Cargo Flights

The airport caters to passenger and cargo flights, as well as general aviation.

!!! note "Airspace"

    - **Iloilo ATZ** — surface up to but excluding 2000 FT (Class B). Aerodrome control is provided by **Iloilo Tower (RPVI_TWR)**.
    - **Iloilo CTR** — surface up to 1500 FT (Class D). Controlled by **Bacolod Approach (RPVB_APP)**.
    - **Bacolod/Iloilo TMA** — 1500 FT to FL200 (Class D below FL160, Class A on ATS routes at FL160 and above). Controlled by **Bacolod Approach (RPVB_APP)**.
    - **Transition altitude:** 11,000 FT.

## Charts
<div class="chart-picker" data-icao="RPVI"></div>

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
      <td style="text-align:center"><strong>RPVI_ATIS</strong></td>
      <td style="text-align:center">Iloilo ATIS</td>
      <td style="text-align:center">126.450</td>
      <td style="text-align:center"></td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>RPVI_GND</strong></td>
      <td style="text-align:center">Iloilo Ground</td>
      <td style="text-align:center">121.800</td>
      <td style="text-align:center"></td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>RPVI_TWR</strong></td>
      <td style="text-align:center">Iloilo Tower</td>
      <td style="text-align:center">123.400</td>
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
Iloilo currently has 1 runway (02/20), 2500 x 45 M, asphalt.

Both runway ends are served by a PAPI (left, 3.0°). Runway 02 has Simple Approach Lighting (SALS, 420 M); runway 20 has Precision Approach Lighting (PALS, 900 M) with sequenced flashing lights and a wing-bar threshold. The runway slopes uphill towards the threshold of runway 20 (THR 02 elevation 132 FT, THR 20 elevation 153 FT).

Turning pads (65 M x 65 M) are provided at both runway ends.

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
      <td style="text-align:center"><strong>02</strong></td>
      <td style="text-align:center">2500</td>
      <td style="text-align:center">2620</td>
      <td style="text-align:center">2560</td>
      <td style="text-align:center">2500</td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>20</strong></td>
      <td style="text-align:center">2500</td>
      <td style="text-align:center">2500</td>
      <td style="text-align:center">2560</td>
      <td style="text-align:center">2500</td>
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
      <td style="text-align:center">IOO</td>
      <td style="text-align:center">116.30 / CH110X</td>
      <td style="text-align:center">On the field, west of the runway</td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>ILS CAT I RWY 20</strong></td>
      <td style="text-align:center">IIO</td>
      <td style="text-align:center">111.50 / CH52X</td>
      <td style="text-align:center">Glide path 2.94°</td>
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

    **CEB123**: Iloilo Ground, CEB123, Bay 4, A-3-2-0 with information A, request clearance Manila.

    **RPVI_GND**: CEB123, cleared Manila, [routing], [SID] RUNWAY 20, Climb [initial level], Squawk 4024.

    **CEB123**: Cleared Manila, [routing], [SID] RUNWAY 20, Climb [initial level], Squawk 4024, CEB123.

## Taxi

The apron sits on the east side of the runway and connects to runway 02/20 via two taxiways, **E1** (north) and **E2** (south). There is no parallel taxiway, so departing aircraft enter the runway and backtrack to the threshold, turning around on the turning pad at the runway end. Follow the apron taxi guide lines and any instruction from the ground controller / marshaller.

For arrivals, vacate via the taxiway given by ATC. If you roll past both taxiways, expect to turn around on the turning pad at the runway end and backtrack.

!!! warning

    Never enter or backtrack the runway until you have been explicitly cleared to do so. Read back any hold short instruction with **"HOLDING SHORT"**.

??? phraseology "Phraseology"

    **CEB123**: Iloilo Ground, CEB123, Bay 4, request taxi, runway 20.

    **RPVI_GND**: CEB123, taxi to holding point runway 20 via E1.

    **CEB123**: Holding point runway 20 via E1, CEB123.

    **RPVI_TWR**: CEB123, backtrack and line up runway 20.

    **CEB123**: Backtrack and line up runway 20, CEB123.

## Departure

The departure procedure is decided by an online Approach (**APP**) or En-route Controller (**CTR**). When both are offline, Standard Instrument Departures (**SIDs**) are given by the aerodrome controller (**TWR**). When either **APP** or **CTR** is online, they decide if departures will be given radar vectors to the TMA exit points or will be following a **SID**.

When **APP** or **CTR** is online, after passing 2000 feet or leaving the control zone, report your passing altitude to **APP** or **CTR**. This is to help them identify you successfully in their radar screens.

??? phraseology "Phraseology"

    **CEB123**: Bacolod Approach, CEB123, passing 2000, climbing [initial level].

    **RPVB_APP**: CEB123, radar identified, continue climb FL150.

## Arrival

When arriving into Iloilo, plan your descent to meet the level restrictions on your STAR. On initial contact with Bacolod Approach (RPVB_APP), report your current level.

??? phraseology "Phraseology"

    **CEB122**: Bacolod Approach, CEB122, FL150.

APP will then issue your arrival clearance including the type of approach to expect to the active runway. APP either gives you radar vectors to final or gives you descent clearances via a STAR. Runway 20 is served by an ILS; RNP and VOR approaches are published for both runways.

??? phraseology "Phraseology"

    **RPVB_APP**: CEB122, radar contact, cleared Iloilo, expect ILS approach RWY 20.

    **CEB122**: Cleared Iloilo, expect ILS approach RWY 20, CEB122.

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
*[RPVI_TWR]: Iloilo Tower
*[RPVI_GND]: Iloilo Ground
*[RPVI_ATIS]: Iloilo ATIS
*[RPVB_APP]: Bacolod Approach
