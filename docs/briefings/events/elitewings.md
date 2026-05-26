# RPVP - Puerto Princesa International Airport - Elite Wings

Think you’ve got what it takes to handle complex airspace and high-traffic operations? Elite Wings is here to put your skills to the test!

This event is designed for experienced pilots who want a real challenge. We’re talking busy frequencies, complex procedures, and ATC coverage from gate to gate. If you’re used to flying in quieter airspace, get ready—this will be a whole different level.

On the 6th of June, starting at 1200 UTC, you’ll depart from VVTS - Tan Son Nhat and head to RPVP - Puerto Princesa, with a Circle to Land approach in a non-radar environment. This isn’t just a flight—it’s an experience.

To maintain a structured and realistic flow of traffic, slot booking is mandatory. Make sure to reserve your departure time [here](https://booking.vatsim.net) in advance so you can participate.

Bring your A-game, because controllers will expect you to be sharp with procedures and quick with readbacks. If you're ready for a realistic, high-traffic challenge, this is the event for you. The skies are waiting—are you up for it?


<div class="metar-widget" data-icao="RPVP">
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

<div class="metar-loading" id="metar-loading-RPVP">Fetching METAR...</div>
<div class="metar-card" id="metar-card-RPVP" style="display:none;"></div>
</div>

<script>
(function () {
  var ICAO = "RPVP";
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

Puerto Princesa International Airport has 1 Runway and 1 passenger terminal.

- Main Terminal - Domestic, International and Cargo Flights

The airport caters passenger and cargo flights, as well as general and military aviation.

## Charts

[RPVP](https://vatphil.com/charts?icao=RPVP){ .md-button .md-button--primary }

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
      <td style="text-align:center"><strong>RPVP_TWR</strong></td>
      <td style="text-align:center">Puerto Princesa Tower</td>
      <td style="text-align:center">118.100</td>
      <td style="text-align:center"></td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>RPVP_APP</strong></td>
      <td style="text-align:center">Puerto Princesa Approach</td>
      <td style="text-align:center">122.000</td>
      <td style="text-align:center">CTR SFC - 1500 FT / TMA 1500 FT - FL200</td>
    </tr>
  </tbody>
</table>

## Runways

<div markdown="1">
Puerto Princesa currently has 1 runway.
Below is a table of the Take-Off Run Available.

**Take-off Run Available.**
</div>
<table>
  <thead>
    <tr>
      <th style="text-align:center">Runway</th>
      <th style="text-align:center">TORA ft (m)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:center"><strong>09</strong></td>
      <td style="text-align:center">8,533 (2601)</td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>27</strong></td>
      <td style="text-align:center">8,533 (2601)</td>
    </tr>
  </tbody>
</table>

## Routes

Local flights within RPHI and some international flights are to use routes given below. Simbrief also gives a standard route which looks like this:

![Simbrief Routes](../../../assets/img/simbrief_rpmd.png)

If your route is still invalid, a controller will send you a private message with your new route. Routes within RPHI are to follow the half-moon principle in both RVSM and non-RVSM conditions. During events you will have 5 minutes between the time you request clearance and the time you request pushback, or you will have to wait until a new slot is available.

!!! warning

    During events it is important that you put your EOBT in your flight plan as controllers will use that to determine your takeoff slot.

## Clearance

On first contact with the controller that will issue your clearance, it is recommended for you to give the following information:

- Your bay number
- Your aircraft type

!!! warning

    Radio Checks on first contact are **discouraged** when building communication with the controller.
    It's best to greet or ask the controller, should you need any help before clearance issuance.

    Be straightforward and concise as possible when communicating within a controlled frequency.

Once you have requested for clearance, the controller will either tell you to standby, or give your clearance on the spot. Clearances include your routing, flight level restrictions, departure instructions and your squawk.

You must read back the clearance in full. Listen carefully to all details that the controller gives you, and if you are unsure about your clearance, **let the controller know.**

??? phraseology

    **PAL123**: Puerto Princesa Tower, PAL123, Stand 2, A-3-2-0, request clearance Manila, FL[XXX].

    **RPVP_TWR**: PAL123, cleared Manila, [ROUTE], RUNWAY 09 [SID], Climb FL150, Squawk [XXXX]

## Pushback

Normally, a controller in Puerto Princesa will instruct you to push back facing a direction.

For RWY 09 departures, expect to face West

For RWY 27 departures, expect to face East

!!! warning

    1. **Do not preplan your pushback!**
    2. Connect the tug first!

??? phraseology "Phraseology"

    **PAL123**: Puerto Princesa Tower, PAL123, Stand 2, request push and start, runway 27.

    **RPVP_TWR**: PAL123, push and start approved, abeam stand 3, face East

## Taxi

In Puerto Princesa, large category aircraft (B737, A320 and bigger) must use **TWY A** for taxiing out. Arriving aircraft may use either TWY A or TWY B towards their assigned parking bay.

!!! warning

    All departing large category aircraft such as B737, A320 and bigger shall take **TWY A** for taxiing out.

??? phraseology "Phraseology"

    **PAL123**: Puerto Princesa Tower, PAL123, Stand 2, request taxi runway 27

    **RPVP_TWR**: PAL123, taxi via TWY A, hold short runway 27

    **PAL123**: Taxi via TWY A, hold short runway 27, PAL123

## Departure

The departure procedure is decided by an online Approach (**APP**) or En-route Controller (**CTR**). When both are offline, Standard Instrument Departures (**SIDs**) are given by the aerodrome controllers (**TWR**). When either **APP** or **CTR** is online, they decide if departures will be following a **SID**.

Available SIDs include **DABOY**, **SAIRA**, **MARIN** and **NOMYO** departures for both RWY 09 and RWY 27, as well as RNP SIDs.

When **APP** or **CTR** is online, after becoming airborne report your passing altitude to **APP** or **CTR**.

??? phraseology "Phraseology"

    **PAL123**: Puerto Princesa Approach, PAL123, passing 2000, climbing FL150, [SID]

    **RPVP_APP**: PAL123, identified, continue climb FL150

## Arrival

When arriving into Puerto Princesa, on initial contact with Puerto Princesa Approach (**RPVP_APP**), report your current level.

Available approaches include **ILS or LOC RWY 27**, **VOR RWY 27**, **RNP RWY 27**, and **VPT[^2] RWY 09**.

??? phraseology "Phraseology"

    **PAL122**: Puerto Princesa Approach, PAL122, FL140, inbound [FIX]

APP will then issue your arrival clearance including the type of approach to expect to the active runway. APP will issue descent clearances via a STAR.

??? phraseology "Phraseology"

    **RPVP_APP**: PAL122, cleared Puerto Princesa [STAR] expect ILS RWY 27

    **PAL122**: Cleared Puerto Princesa [STAR] expect ILS RWY 27, PAL122

    **RPVP_APP**: PAL122, descend via STAR 8,000, QNH 1011

    **PAL122**: Descend via STAR 8,000, QNH 1011, PAL122

## Parking Bays

| Bay | Aircraft Type |
|:---:|:---|
| 1 | A321, A320, and lower category aircraft |
| 2 | A321, A320, and lower category aircraft |
| 3 | A321, A320, and lower category aircraft |
| 4 | A330, A321, A320, and lower category aircraft |
| 5 | A321, A320, and lower category aircraft |
| 6 | A321, A320, and lower category aircraft |

## Visual Approach Chart

<iframe src="../../../assets/pdfs/RPVP%20VPT.pdf" width="100%" height="600px" style="border:none;"></iframe>

[^1]: Vertical limit of FL150 can be increased to a maximum of FL200.
[^2]: Visual Manoeuvring with Prescribed Tracks

*[GA]: General Aviation
*[EOBT]: Estimated off block time
*[TOBT]: Target off block time
*[TSAT]: Target start approval time
*[ASRT]: Actual start up time
*[TTOT]: Target takeoff time
*[CTOT]: Calculated takeoff time
*[RPVP_TWR]: Puerto Princesa Tower
*[RPVP_APP]: Puerto Princesa Approach

# RPVP Sceneries

| Simulator | Provider                                                                                      | Price    |
| --------- | --------------------------------------------------------------------------------------------- | -------- |
| MSFS 2020 | [TurtleTank1997](https://flightsim.to/addon/14259/puerto-princesa-international-airport-rpvp) | Freeware |