# RPMR - Tambler Principal Airport

<div class="metar-widget" data-icao="RPMR">
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

<div class="metar-loading" id="metar-loading-RPMR">Fetching METAR...</div>
<div class="metar-card" id="metar-card-RPMR" style="display:none;"></div>
</div>

<script>
(function () {
  var ICAO = "RPMR";
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
Tambler Principal Airport (RPMR), also known as General Santos International Airport, is a Class 1 airport located approximately 18 KM southwest of General Santos City, South Cotabato. It has a single runway (17/35) and serves domestic passenger and cargo flights, as well as general and military aviation.

- Main Terminal - Domestic and Cargo Flights

The airport caters to passenger and cargo flights, as well as general and military aviation.

!!! note "Airspace"

    - **Tambler ATZ** — circle 5 NM radius centered on the ARP, surface up to but excluding 2000 FT (Class B). Aerodrome control is provided by **Tambler Tower (RPMR_TWR)**.
    - **Tambler CTR** — circle 10 NM radius centered on the ARP, surface up to 1500 FT (Class D). Controlled by **Tambler Tower (RPMR_TWR)**.
    - **Tambler TMA** — 1500 FT to FL200 (Class D below FL160, Class A at FL160 and above). Controlled by **Tambler Approach**.
    - **Transition altitude:** 11,000 FT.

## Airport Regulations

### General

No wide body aircraft (A330 and above category) shall taxi behind a parked B777-300ER. Narrow body aircraft (A321 and below category) are allowed to taxi behind a B777-300ER.

## Charts
<iframe
  data-chart-src="https://vatphil.com/charts?icao=RPMR"
  title="RPMR Charts"
  loading="lazy"
  style="width:100%; height:750px; border:1px solid var(--md-default-fg-color--lightest); border-radius:8px;">
</iframe>

[Open charts in new tab](https://vatphil.com/charts?icao=RPMR){ .md-button .md-button--primary }

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
      <td style="text-align:center"><strong>RPMR_TWR</strong></td>
      <td style="text-align:center">Tambler Tower</td>
      <td style="text-align:center">118.400</td>
      <td style="text-align:center"></td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>RPMR_APP</strong></td>
      <td style="text-align:center">Tambler Approach</td>
      <td style="text-align:center">119.100</td>
      <td style="text-align:center">TMA 1500 ft - FL200</td>
    </tr>
  </tbody>
</table>

## Runways

<div markdown="1">
Tambler Principal Airport currently has 1 runway (17/35), 3227 x 45 M, concrete.

Runway 17 is served by Precision Approach Lighting (PALS, 900 M) and an ILS, with PAPI (3.0°). Runway 35 has a PAPI (3.0°) and a Runway Threshold Identification Light (RTIL).

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
      <td style="text-align:center"><strong>17</strong></td>
      <td style="text-align:center">3227</td>
      <td style="text-align:center">3527</td>
      <td style="text-align:center">3344</td>
      <td style="text-align:center">3227</td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>35</strong></td>
      <td style="text-align:center">3227</td>
      <td style="text-align:center">3527</td>
      <td style="text-align:center">3343</td>
      <td style="text-align:center">3227</td>
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

    **CEB123**: Tambler Tower, CEB123, Bay 3, A-3-2-0 with information A, request clearance Manila.

    **RPMR_TWR**: CEB123, cleared Manila, [routing], [SID] RUNWAY 17, Climb FL150, Squawk 4024.

    **CEB123**: Cleared Manila, [routing], [SID] RUNWAY 17, Climb FL150, Squawk 4024, CEB123.

## Pushback

Clearance from Tambler Tower must be obtained prior to commencing pushback or taxi. The required facing depends on the departure runway:

- **RWY 17 departure** — push back at the designated start-up point parallel with the runway, facing **North** (or as instructed by ATC).
- **RWY 35 departure** — push back at the designated start-up point parallel with the runway, facing **South** (or as instructed by ATC).

??? phraseology "Phraseology"

    **CEB123**: Tambler Tower, CEB123, Bay 3, request push and start, runway 17.

    **RPMR_TWR**: CEB123, push and start approved, face North.

    **CEB123**: Push and start approved, face North, CEB123.

## Taxi

The apron connects to runway 17/35 via taxiways **C** and **D**.

For arrivals, unless otherwise instructed, vacate and taxi in via **TWY C** when landing runway 17, and via **TWY D** when landing runway 35.

!!! info
    Bays 1 and 7 are for A321 and lower category aircraft; bays 2 to 6 are for B747, B777 and lower category aircraft.

!!! warning

    Never enter or backtrack the runway until you have been explicitly cleared to do so. Read back any hold short instruction with **"HOLDING SHORT"**.

??? phraseology "Phraseology"

    **CEB123**: Tambler Tower, CEB123, Bay 3, request taxi, runway 17.

    **RPMR_TWR**: CEB123, taxi to holding point runway 17 via D.

    **CEB123**: Holding point runway 17 via D, CEB123.

## Departure

The departure procedure is decided by an online Approach (**APP**) or En-route Controller (**CTR**). When both are offline, Standard Instrument Departures (**SIDs**) are given by the aerodrome controller (**TWR**).

When **APP** or **CTR** is online, after passing 2000 feet or leaving the control zone, report your passing altitude to **APP** or **CTR**.

??? phraseology "Phraseology"

    **CEB123**: Tambler Approach, CEB123, passing 2000, climbing FL150.

    **RPMR_APP**: CEB123, continue climb FL150.

## Arrival

When arriving into General Santos, it is best for you to be in between 10,000 FT and FL130 when reaching the border of the TMA or the start of the STAR. On initial contact with Tambler Approach (RPMR_APP), report your current level.

??? phraseology "Phraseology"

    **CEB122**: Tambler Approach, CEB122, FL130, inbound General Santos.

APP will then issue your arrival clearance including the type of approach to expect to the active runway.

??? phraseology "Phraseology"

    **RPMR_APP**: CEB122, cleared General Santos, MELBY3R expect RNP approach RWY 17.

    **CEB122**: Cleared General Santos, MELBY3R, RNP approach RWY 17, CEB122.

!!! warning

    If APP didn't give you any turns after you have passed the last waypoint on your routing, maintain your present heading.

*[GA]: General Aviation
*[ATZ]: Aerodrome Traffic Zone
*[CTR]: Control Zone
*[TMA]: Terminal Control Area
*[SID]: Standard Instrument Departure
*[STAR]: Standard Terminal Arrival Route
*[RPMR_TWR]: Tambler Tower
*[RPMR_APP]: Tambler Approach
