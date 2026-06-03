# RPMY - Laguindingan Principal Airport

<div class="metar-widget" data-icao="RPMY">
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

<div class="metar-loading" id="metar-loading-RPMY">Fetching METAR...</div>
<div class="metar-card" id="metar-card-RPMY" style="display:none;"></div>
</div>

<script>
(function () {
  var ICAO = "RPMY";
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
Laguindingan Principal Airport (RPMY) is a Class 1 airport located in Laguindingan, Misamis Oriental, approximately 30 KM northwest of Cagayan de Oro City. It has a single runway (09/27) and serves domestic passenger and cargo flights, as well as general aviation.

- Main Terminal - Domestic and Cargo Flights

The airport caters to passenger and cargo flights, as well as general aviation.

!!! note "Airspace"

    - **Laguindingan ATZ** — circle 5 NM radius centered on the ARP, surface up to but excluding 2000 FT (Class B). Aerodrome control is provided by **Laguindingan Tower (RPMY_TWR)**.
    - **Laguindingan CTR** — circle 10 NM radius centered on the ARP, surface up to 1500 FT (Class D). Controlled by **Laguindingan Tower (RPMY_TWR)**.
    - **Laguindingan TMA** — 1500 FT to FL200 (Class D below FL160, Class A at FL160 and above). Controlled by **Laguindingan Approach**.
    - **Transition altitude:** 11,000 FT.

## Charts
<iframe
  src="https://vatphil.com/charts?icao=RPMY"
  title="RPMY Charts"
  loading="lazy"
  style="width:100%; height:750px; border:1px solid var(--md-default-fg-color--lightest); border-radius:8px;">
</iframe>

[Open charts in new tab](https://vatphil.com/charts?icao=RPMY){ .md-button .md-button--primary }

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
      <td style="text-align:center"><strong>RPMY_ATIS</strong></td>
      <td style="text-align:center">Laguindingan ATIS</td>
      <td style="text-align:center">127.600</td>
      <td style="text-align:center"></td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>RPMY_TWR</strong></td>
      <td style="text-align:center">Laguindingan Tower</td>
      <td style="text-align:center">122.600</td>
      <td style="text-align:center"></td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>RPMY_APP</strong></td>
      <td style="text-align:center">Laguindingan Approach</td>
      <td style="text-align:center">125.500</td>
      <td style="text-align:center">TMA 1500 ft - FL200</td>
    </tr>
  </tbody>
</table>

## Runways

<div markdown="1">
Laguindingan Principal Airport currently has 1 runway (09/27), 2100 x 45 M, concrete.

Both runway ends have a PAPI (3.0°). Runway 09 has Simple Approach Lighting (SALS, 420 M) with sequenced flashing lights and a Runway Threshold Identification Light (RTIL). Runway 27 has Precision Approach Lighting (PALS, 720 M) with sequenced flashing lights and an ILS.

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
      <td style="text-align:center">2100</td>
      <td style="text-align:center">2250</td>
      <td style="text-align:center">2100</td>
      <td style="text-align:center">2100</td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>27</strong></td>
      <td style="text-align:center">2100</td>
      <td style="text-align:center">2250</td>
      <td style="text-align:center">2100</td>
      <td style="text-align:center">2100</td>
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

    **CEB123**: Laguindingan Tower, CEB123, Bay 3, A-3-2-0 with information A, request clearance Manila.

    **RPMY_TWR**: CEB123, cleared Manila, [routing], [SID] RUNWAY 27, Climb FL150, Squawk 4024.

    **CEB123**: Cleared Manila, [routing], [SID] RUNWAY 27, Climb FL150, Squawk 4024, CEB123.

## Taxi

The apron connects to runway 09/27 via taxiways **Alpha** and **Bravo**. Follow the apron taxi guide lines and any instruction from ATC. Clearance from Laguindingan Tower must be obtained before pushback, tow or taxi.

!!! warning

    Never enter or backtrack the runway until you have been explicitly cleared to do so. Read back any hold short instruction with **"HOLDING SHORT"**.

??? phraseology "Phraseology"

    **CEB123**: Laguindingan Tower, CEB123, Bay 3, request taxi, runway 27.

    **RPMY_TWR**: CEB123, taxi to holding point runway 27 via Alpha.

    **CEB123**: Holding point runway 27 via Alpha, CEB123.

## Departure

The departure procedure is decided by an online Approach (**APP**) or En-route Controller (**CTR**). When both are offline, Standard Instrument Departures (**SIDs**) are given by the aerodrome controller (**TWR**).

When **APP** or **CTR** is online, after passing 2000 feet or leaving the control zone, report your passing altitude to **APP** or **CTR**.

??? phraseology "Phraseology"

    **CEB123**: Laguindingan Approach, CEB123, passing 2000, climbing FL150.

    **RPMY_APP**: CEB123, continue climb FL150.

## Arrival

When arriving into Laguindingan, it is best for you to be in between 10,000 FT and FL130 when reaching the border of the TMA or the start of the STAR. On initial contact with Laguindingan Approach (RPMY_APP), report your current level.

??? phraseology "Phraseology"

    **CEB122**: Laguindingan Approach, CEB122, FL130, inbound Laguindingan.

APP will then issue your arrival clearance including the type of approach to expect to the active runway. APP either gives you radar vectors to final or gives you descent clearances via a STAR.

??? phraseology "Phraseology"

    **RPMY_APP**: CEB122, radar contact, cleared Laguindingan, SAGOL4A expect ILS approach RWY 09.

    **CEB122**: Cleared Laguindingan, SAGOL4A ILS approach RWY 09, CEB122.

## Parking

Bays 1 to 5 are exclusively for aircraft **A320 and lower category**. Higher category aircraft may use a bay provided no other aircraft is parked or expected to park adjacent to it.


*[GA]: General Aviation
*[ATZ]: Aerodrome Traffic Zone
*[CTR]: Control Zone
*[TMA]: Terminal Control Area
*[SID]: Standard Instrument Departure
*[STAR]: Standard Terminal Arrival Route
*[RPMY_TWR]: Laguindingan Tower
*[RPMY_APP]: Laguindingan Approach
*[RPMY_ATIS]: Laguindingan ATIS
