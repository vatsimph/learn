# RPVD - Dumaguete Principal Airport

<div class="metar-widget" data-icao="RPVD">
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

<div class="metar-loading" id="metar-loading-RPVD">Fetching METAR...</div>
<div class="metar-card" id="metar-card-RPVD" style="display:none;"></div>
</div>

<script>
(function () {
  var ICAO = "RPVD";
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
Dumaguete Principal Airport (RPVD) is a Class 1 airport located approximately 1.3 NM west of Dumaguete City, in Agan-an, Sibulan, Negros Oriental. It has a single runway (09/27) and serves domestic passenger and cargo flights, as well as general aviation.

- Main Terminal - Domestic and Cargo Flights

The airport caters to passenger and cargo flights, as well as general aviation.

!!! note "Airspace"

    - **Dumaguete ATZ** — circle 5 NM radius centered on the ARP, up to but excluding 2000 FT (Class B). Do not enter the ATZ on an IAS exceeding **200 KT** unless authorized by ATC.
    - **Dumaguete CTR** — circle 10 NM radius centered on the ARP, surface up to 1500 FT (Class D).
    - **Mactan TMA** — 1500 FT to FL200 (Class D below FL160, Class A at FL160 and above). Approach control is provided by **Mactan Approach (RPVM_APP)**.
    - **Transition altitude:** 11,000 FT.

## Charts
<iframe
  src="https://vatphil.com/charts?icao=RPVD"
  title="RPVD Charts"
  loading="lazy"
  style="width:100%; height:750px; border:1px solid var(--md-default-fg-color--lightest); border-radius:8px;">
</iframe>

[Open charts in new tab](https://vatphil.com/charts?icao=RPVD){ .md-button .md-button--primary }

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
      <td style="text-align:center"><strong>RPVD_TWR</strong></td>
      <td style="text-align:center">Dumaguete Tower</td>
      <td style="text-align:center">129.700</td>
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
Dumaguete Principal Airport currently has 1 runway (09/27), 1845 x 45 M, concrete and asphalt.

Runway 27 is served by a PAPI (right, 3.0°) and a Runway Threshold Identification Light (RTIL). Runway 09 has no visual approach slope guidance.

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
      <td style="text-align:center"><strong>09</strong></td>
      <td style="text-align:center">1845</td>
      <td style="text-align:center">1845</td>
      <td style="text-align:center">1845</td>
      <td style="text-align:center">1845</td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>27</strong></td>
      <td style="text-align:center">1845</td>
      <td style="text-align:center">1895</td>
      <td style="text-align:center">1895</td>
      <td style="text-align:center">1845</td>
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

    **CEB123**: Dumaguete Tower, CEB123, Bay 1, A-3-2-0 with information A, request clearance Manila.

    **RPVD_TWR**: CEB123, cleared Cebu, [routing], [SID] RUNWAY 09, Climb FL150, Squawk 4024.

    **CEB123**: Cleared Cebu, [routing], [SID] RUNWAY 09, Climb FL150, Squawk 4024, CEB123.

## Taxi

Dumaguete has limited taxiway infrastructure, so expect to backtrack the runway and make a 180-degree turn to line up.

!!! warning

    Never enter or backtrack the runway until you have been explicitly cleared to do so. Read back any hold short instruction with **"HOLDING SHORT"**.

??? phraseology "Phraseology"

    **CEB123**: Dumaguete Tower, CEB123, Bay 1, request taxi, runway 27.

    **RPVD_TWR**: CEB123, backtrack runway 27 report ready for departure.

    **CEB123**: Backtrack runway 27, wilco, CEB123.

## Departure

The departure procedure is decided by an online Approach (**APP**) or En-route Controller (**CTR**). When both are offline, Standard Instrument Departures (**SIDs**) are given by the aerodrome controller (**TWR**). When either **APP** or **CTR** is online, they decide if departures will be given radar vectors to the TMA exit points or will be following a **SID**.

When **APP** or **CTR** is online, after passing 1500 feet or leaving the ATZ, report your passing altitude to **APP** or **CTR**. This is to help them identify you successfully in their radar screens.

??? phraseology "Phraseology"

    **CEB123**: Mactan Approach, CEB123, passing 2000, climbing FL150.

    **RPVM_APP**: CEB123, radar identified, continue climb FL150.

!!! info "Runway 09"

    Departing RWY 09 allowed during IMC.

## Arrival

When arriving into Dumaguete, it is best for you to be in between 8,000 FT and FL130 when reaching the border of the TMA or the start of the STAR. On initial contact with Mactan Approach (RPVM_APP), report your current level.

??? phraseology "Phraseology"

    **CEB122**: Mactan Approach, CEB122, FL130.

APP will then issue your arrival clearance including the type of approach to expect to the active runway. APP either gives you radar vectors to final or gives you descent clearances via a STAR.

??? phraseology "Phraseology"

    **RPVM_APP**: CEB122, radar identified, cleared Dumaguete, expect RNP approach RWY 27.

    **CEB122**: Cleared Dumaguete, expect RNP approach RWY 27, CEB122.

    **RPVM_APP**: CEB122, maintain present heading, descend 5,000, QNH 1012.

    **CEB122**: Maintain present heading, descend 5,000, QNH 1012, CEB122.

!!! warning

    If APP didn't give you any turns after you have passed the last waypoint on your routing, maintain your present heading.

!!! info "Runway 09"

    Landing RWY 09 allowed during day VMC except for A319 and higher category aircraft.

*[GA]: General Aviation
*[ATZ]: Aerodrome Traffic Zone
*[CTR]: Control Zone
*[TMA]: Terminal Control Area
*[EOBT]: Estimated off block time
*[TOBT]: Target off block time
*[TSAT]: Target start approval time
*[ASRT]: Actual start up time
*[TTOT]: Target takeoff time
*[CTOT]: Calculated takeoff time
*[RPVD_TWR]: Dumaguete Tower
*[RPVM_APP]: Mactan Approach
*[RPVM_S_APP]: Mactan Approach
