# RPSP - Bohol-Panglao International Airport

<div class="metar-widget" data-icao="RPSP">
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

<div class="metar-loading" id="metar-loading-RPSP">Fetching METAR...</div>
<div class="metar-card" id="metar-card-RPSP" style="display:none;"></div>
</div>

<script>
(function () {
  var ICAO = "RPSP";
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
Bohol-Panglao International Airport (RPSP) is an international airport located in Tawala, Panglao, Bohol, approximately 12 KM southwest of Tagbilaran City. It has a single runway (03/21) and serves domestic and international passenger and cargo flights, as well as general aviation.

- Main Terminal - Domestic and International Flights

The airport caters to passenger and cargo flights, as well as general aviation.

!!! note "Airspace"

    - **Panglao ATZ** — circle 5 NM radius centered on the ARP, surface up to but excluding 2000 FT (Class B). Aerodrome control is provided by **Panglao Tower (RPSP_TWR)**.
    - **Panglao CTR** — circle 10 NM radius centered on the ARP, surface up to 1500 FT (Class D). Controlled by **Panglao Tower (RPSP_TWR)**.
    - **Mactan Sub-TMA** — 1500 FT to FL200 (Class D below FL160, Class A at FL160 and above). Controlled by **Mactan Approach**.
    - **Transition altitude:** 11,000 FT.

## Airport Regulations

### 1.1 General

1.1.1 All aircraft from **A319 and above** shall not make a 180-degree turn on any part of the runway except at the turn pad areas at the end of the runway, and must strictly follow the nose wheel guide line.

1.1.2 The aerodrome is closed to aircraft without a functioning two-way radio.

### 1.2 Taxiing

1.2.1 Panglao Tower will include the parking bay assignment with the taxi instruction.

1.2.2 Unless otherwise instructed by ATC, aircraft landing **RWY 03 taxi in via TWY E2**; aircraft landing **RWY 21 taxi in via TWY E1**.

1.2.3 Bays 3 to 9 may be used by A321 or lower category aircraft (wingspan less than 36 M).

## Charts
<iframe
  data-chart-src="https://vatphil.com/charts?icao=RPSP"
  title="RPSP Charts"
  loading="lazy"
  style="width:100%; height:750px; border:1px solid var(--md-default-fg-color--lightest); border-radius:8px;">
</iframe>

[Open charts in new tab](https://vatphil.com/charts?icao=RPSP){ .md-button .md-button--primary }

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
      <td style="text-align:center"><strong>RPSP_ATIS</strong></td>
      <td style="text-align:center">Panglao ATIS</td>
      <td style="text-align:center">126.500</td>
      <td style="text-align:center">Hourly</td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>RPSP_GND</strong></td>
      <td style="text-align:center">Panglao Ground</td>
      <td style="text-align:center">121.600</td>
      <td style="text-align:center"></td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>RPSP_TWR</strong></td>
      <td style="text-align:center">Panglao Tower</td>
      <td style="text-align:center">124.500</td>
      <td style="text-align:center"></td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>RPVM_APP</strong></td>
      <td rowspan="2" style="text-align:center">Mactan Approach</td>
      <td style="text-align:center">124.700</td>
      <td style="text-align:center">TMA 1500 ft - FL200</td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>RPVM_S_APP</strong></td>
      <td style="text-align:center">121.200</td>
      <td style="text-align:center">SUB TMA 1500 ft - FL200</td>
    </tr>
  </tbody>
</table>

## Runways

<div markdown="1">
Bohol-Panglao currently has 1 runway (03/21), 2500 x 45 M, asphalt.

Both runway ends are served by a PAPI (left, 3.0°). Runway 03 has Simple Approach Lighting (SALS, 427 M); runway 21 has Precision Approach Lighting (PALS, 900 M) with a wing-bar threshold. The runway has a slight upslope (0.099%) towards the threshold of runway 21.

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
      <td style="text-align:center">2500</td>
      <td style="text-align:center">2650</td>
      <td style="text-align:center">2500</td>
      <td style="text-align:center">2500</td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>21</strong></td>
      <td style="text-align:center">2500</td>
      <td style="text-align:center">2650</td>
      <td style="text-align:center">2500</td>
      <td style="text-align:center">2500</td>
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

    **CEB123**: Panglao Tower, CEB123, Bay 4, A-3-2-0 with information A, request clearance Manila.

    **RPSP_TWR**: CEB123, cleared Manila, [routing], [SID] RUNWAY 21, Climb FL150, Squawk 4024.

    **CEB123**: Cleared Manila, [routing], [SID] RUNWAY 21, Climb FL150, Squawk 4024, CEB123.

## Taxi

The main apron connects to runway 03/21 via taxiways **E1** and **E2**. Follow the apron taxi guide lines and any instruction from the ground controller / marshaller.

For arrivals, unless otherwise instructed, vacate and taxi in via **TWY E2** when landing runway 03, and via **TWY E1** when landing runway 21.

!!! warning

    Never enter or backtrack the runway until you have been explicitly cleared to do so. Read back any hold short instruction with **"HOLDING SHORT"**.

    Aircraft A319 and above may only make a 180-degree turn at the runway turn pads — not on the runway body.

??? phraseology "Phraseology"

    **CEB123**: Panglao Ground, CEB123, Bay 4, request taxi, runway 21.

    **RPSP_GND**: CEB123, taxi to holding point runway 21 via E1.

    **CEB123**: Holding point runway 21 via E1, CEB123.

## Departure

The departure procedure is decided by an online Approach (**APP**) or En-route Controller (**CTR**). When both are offline, Standard Instrument Departures (**SIDs**) are given by the aerodrome controller (**TWR**). When either **APP** or **CTR** is online, they decide if departures will be given radar vectors to the TMA exit points or will be following a **SID**.

When **APP** or **CTR** is online, after passing 2000 feet or leaving the control zone, report your passing altitude to **APP** or **CTR**. This is to help them identify you successfully in their radar screens.

??? phraseology "Phraseology"

    **CEB123**: Mactan Approach, CEB123, passing 2000, climbing FL150.

    **RPVM_APP**: CEB123, radar identified, continue climb FL150.

## Arrival

When arriving into Bohol-Panglao, it is best for you to be in between 10,000 FT and FL130 when reaching the border of the TMA or the start of the STAR. On initial contact with Mactan Approach (RPVM_APP), report your current level.

??? phraseology "Phraseology"

    **CEB122**: Mactan Approach, CEB122, FL150.

APP will then issue your arrival clearance including the type of approach to expect to the active runway. APP either gives you radar vectors to final or gives you descent clearances via a STAR.

??? phraseology "Phraseology"

    **RPVM_APP**: CEB122, radar contact, cleared Bohol, expect ILS approach RWY 21.

    **CEB122**: Cleared Bohol, expect ILS approach RWY 21, CEB122.

    **RPVM_APP**: CEB122, maintain present heading, descend 5,000, QNH 1012.

    **CEB122**: Maintain present heading, descend 5,000, QNH 1012, CEB122.

!!! warning

    If APP didn't give you any turns after you have passed the last waypoint on your routing, maintain your present heading.

*[GA]: General Aviation
*[ATZ]: Aerodrome Traffic Zone
*[CTR]: Control Zone
*[TMA]: Terminal Control Area
*[SID]: Standard Instrument Departure
*[STAR]: Standard Terminal Arrival Route
*[RPSP_TWR]: Panglao Tower
*[RPSP_GND]: Panglao Ground
*[RPSP_ATIS]: Panglao ATIS
*[RPVM_APP]: Mactan Approach
*[RPVM_S_APP]: Mactan Approach
