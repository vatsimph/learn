# RPLI - Laoag International Airport

<div class="metar-widget" data-icao="RPLI">
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

<div class="metar-loading" id="metar-loading-RPLI">Fetching METAR...</div>
<div class="metar-card" id="metar-card-RPLI" style="display:none;"></div>
</div>

<script>
(function () {
  var ICAO = "RPLI";
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
Laoag International Airport (RPLI) is located in Laoag City, Ilocos Norte, in the far north of Luzon. It serves the Ilocos Region with domestic flights and occasional international charters, and has a single runway (01/19).

The airport reference point (ARP) is 181034N 1203152E, aerodrome elevation 24 FT.

!!! airspace "Airspace"

    - **Laoag ATZ** — circle 5 NM radius centered on the ARP (181034N 1203152E), surface up to but excluding 2000 FT (Class B).
    - **Laoag CTR** — circle 10 NM radius centered on the LAO DVOR/DME (181044N 1203145E), surface up to 1500 FT (Class D).
    - **Laoag TMA** — 1500 FT to FL200, excluding the ATZ and ATS routes at FL160 and above (Class D below FL160, Class A at FL160 and above). Approach control is provided by **Laoag Approach (RPLI_APP)**.
    - **Transition altitude:** 11,000 FT.

## Charts
<div class="chart-picker" data-icao="RPLI"></div>

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
      <td style="text-align:center"><strong>RPLI_TWR</strong></td>
      <td style="text-align:center">Laoag Tower</td>
      <td style="text-align:center">118.100</td>
      <td style="text-align:center">ATZ, SFC up to excluding 2000 ft</td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>RPLI_APP</strong></td>
      <td style="text-align:center">Laoag Approach</td>
      <td style="text-align:center">122.300</td>
      <td style="text-align:center">CTR / TMA, 1500 ft - FL200</td>
    </tr>
  </tbody>
</table>

## Runways

<div markdown="1">
Laoag International Airport has 1 runway (01/19), 2784 x 45 M, concrete and asphalt (PCN 608/R/B/W/U).

Runway 01 is served by SALS and a PAPI (left/right, 3.0°). Runway 19 is served by MSALS and a PAPI (left/right, 3.0°).

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
      <td style="text-align:center"><strong>01</strong></td>
      <td style="text-align:center">2784</td>
      <td style="text-align:center">2984</td>
      <td style="text-align:center">2784</td>
      <td style="text-align:center">2784</td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>19</strong></td>
      <td style="text-align:center">2784</td>
      <td style="text-align:center">2934</td>
      <td style="text-align:center">2784</td>
      <td style="text-align:center">2784</td>
    </tr>
  </tbody>
</table>

## Clearance

On first contact with the controller that will issue your clearance, give the following information:

- Your parking bay
- Your aircraft type
- The ATIS information letter

!!! warning

    Radio Checks on first contact are **discouraged** when building communication with the controller.
    It's best to greet or ask the controller, should you need any help before clearance issuance.

    Be straightforward and concise as possible when communicating within a controlled frequency.

Once you have requested for clearance, the controller will either tell you to standby, or give your clearance on the spot. Clearances include your routing, flight level restrictions, departure instructions and your squawk. You must read back the clearance in full.

??? phraseology "Phraseology"

    **PAL123**: Laoag Tower, PAL123, Bay 1, A-3-2-0 with information A, request clearance Manila.

    **RPLI_TWR**: PAL123, cleared Manila, [routing], [SID] RUNWAY 01, Climb FL150, Squawk 4024.

    **PAL123**: Cleared Manila, [routing], [SID] RUNWAY 01, Climb FL150, Squawk 4024, PAL123.

## Taxi

Avoid tight turning on the runway; use the turn-around pad at the end of either runway. Expect to backtrack depending on your parking bay and the active runway.

!!! warning

    Never enter or backtrack the runway until you have been explicitly cleared to do so. Read back any hold short instruction with **"HOLDING SHORT"**.

??? phraseology "Phraseology"

    **PAL123**: Laoag Tower, PAL123, Bay 1, request taxi, runway 01.

    **RPLI_TWR**: PAL123, backtrack runway 01 report ready for departure.

    **PAL123**: Backtrack runway 01, wilco, PAL123.

## Departure

The departure procedure is decided by an online Approach (**APP**) or En-route Controller (**CTR**). When both are offline, Standard Instrument Departures (**SIDs**) are given by the aerodrome controller (**TWR**). When either **APP** or **CTR** is online, they decide if departures will be given radar vectors to the TMA exit points or will be following a **SID**.

When **APP** or **CTR** is online, after passing 1500 feet or leaving the ATZ, report your passing altitude to **APP** or **CTR**. This is to help them identify you successfully in their radar screens.

??? phraseology "Phraseology"

    **PAL123**: Laoag Approach, PAL123, passing 2000, climbing FL150.

    **RPLI_APP**: PAL123, radar identified, continue climb FL150.

## Arrival

When arriving into Laoag, it is best for you to be between 8,000 FT and FL130 when reaching the border of the TMA or the start of the STAR. On initial contact with Laoag Approach (RPLI_APP), report your current level.

??? phraseology "Phraseology"

    **PAL122**: Laoag Approach, PAL122, FL130.

APP will then issue your arrival clearance including the type of approach to expect to the active runway. APP either gives you radar vectors to final or gives you descent clearances via a STAR.

??? phraseology "Phraseology"

    **RPLI_APP**: PAL122, radar identified, cleared Laoag, expect RNP approach RWY 01.

    **PAL122**: Cleared Laoag, expect RNP approach RWY 01, PAL122.

!!! warning

    If APP didn't give you any turns after you have passed the last waypoint on your routing, maintain your present heading.

*[ATIS]: Automatic Terminal Information Service
*[ATZ]: Aerodrome Traffic Zone
*[CTR]: Control Zone
*[TMA]: Terminal Control Area
*[SID]: Standard Instrument Departure
*[STAR]: Standard Terminal Arrival Route
*[APP]: Approach
*[TWR]: Tower
*[CTR]: Control Zone
*[PCN]: Pavement Classification Number
*[RPLI_TWR]: Laoag Tower
*[RPLI_APP]: Laoag Approach
