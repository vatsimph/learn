# RPLB - Subic Bay Principal Airport

<div class="metar-widget" data-icao="RPLB">
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

<div class="metar-loading" id="metar-loading-RPLB">Fetching METAR...</div>
<div class="metar-card" id="metar-card-RPLB" style="display:none;"></div>
</div>

<script>
(function () {
  var ICAO = "RPLB";
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

Subic Bay Principal Airport has 1 Runway and 1 passenger terminal.

- Main Terminal - Domestic, International and Cargo Flights

The airport caters passenger and cargo flights, as well as general and military aviation.

## Charts

[RPLB](https://vatphil.com/charts?icao=RPLB){ .md-button .md-button--primary }

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
      <td style="text-align:center"><strong>RPLB_DEL</strong></td>
      <td style="text-align:center">Subic Clearance Delivery</td>
      <td style="text-align:center">121.300</td>
      <td style="text-align:center"></td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>RPLB_GND</strong></td>
      <td style="text-align:center">Ground Control</td>
      <td style="text-align:center">121.800</td>
      <td style="text-align:center"></td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>RPLB_TWR</strong></td>
      <td style="text-align:center">Subic Tower</td>
      <td style="text-align:center">118.200</td>
      <td style="text-align:center"></td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>RPLC_APP</strong></td>
      <td style="text-align:center">Clark Approach</td>
      <td style="text-align:center">119.200</td>
      <td style="text-align:center">CTR SFC - 1500 FT / TMA 1500 FT - FL150</td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>RPLB_ATIS</strong></td>
      <td style="text-align:center">Subic ATIS</td>
      <td style="text-align:center">134.400</td>
      <td style="text-align:center"></td>
    </tr>
  </tbody>
</table>

## Runways

<div markdown="1">
Subic Bay currently has 1 runway.
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
      <td style="text-align:center"><strong>07</strong></td>
      <td style="text-align:center">9,006 (2745)</td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>25</strong></td>
      <td style="text-align:center">9,006 (2745)</td>
    </tr>
  </tbody>
</table>

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

    **RPC123**: Subic Clearance Delivery, RPC123, Stand [X], [AIRCRAFT TYPE], request clearance [DEST], FL[XXX].

    **RPLB_DEL**: RPC123, cleared [DEST], [ROUTE], RUNWAY 07 EISMA1H, EXOLO TRANSITION, Climb 7000, Squawk [XXXX]

!!! info "Did you know?"

    Subic is the only aerodrome in the Philippines to have transitions on its STAR.

## Pushback

Normally, a controller in Subic Bay will instruct you to push back to the nearest start-up point.

For RWY 07 departures, expect to face West

For RWY 25 departures, expect to face East

!!! warning

    1. **Do not preplan your pushback!**
    2. Connect the tug first!

??? phraseology "Phraseology"

    **RPC123**: Subic Ground, RPC123, Stand [X], request push and start, runway 07.

    **RPLB_GND**: RPC123, push and start approved, face West

## Taxi

!!! warning

    The Southeast Apron and Passenger Terminal are **not visible from the Control Tower**. All aircraft movements onto and off stands shall be supervised by a ground marshall.

??? phraseology "Phraseology"

    **RPC123**: Subic Ground, RPC123, Stand [X], request taxi runway 07

    **RPLB_GND**: RPC123, taxi via [TWY], hold short runway 07

    **RPC123**: Taxi via [TWY], hold short runway 07, RPC123

## Departure

The departure procedure is decided by an online Approach (**APP**) or En-route Controller (**CTR**). When both are offline, Standard Instrument Departures (**SIDs**) are given by the aerodrome controllers (**TWR**). When either **APP** or **CTR** is online, they decide if departures will be following a **SID**.

When **APP** or **CTR** is online, after becoming airborne report your passing altitude to **APP** or **CTR**.

!!! warning

    All turbo-jet/turbo-fan aircraft departing RWY 25 must attain **1000 FT** and pass the runway end before commencing any turn. Avoid overflying Olongapo City.

??? phraseology "Phraseology"

    **RPC123**: Clark Approach, RPC123, passing 2000, climbing FL[XXX], [SID]

    **RPLC_APP**: RPC123, identified, continue climb FL[XXX]

## Arrival

When arriving into Subic, on initial contact with Clark Approach (**RPLC_APP**), report your current level.

Available approaches include **RNP Y RWY 07** and **RNP Z RWY 07**.

??? phraseology "Phraseology"

    **RPC122**: Clark Approach, RPC122, FL[XXX], inbound [FIX]

APP will then issue your arrival clearance including the type of approach to expect to the active runway. APP will issue descent clearances via a STAR, or assign radar vectors.

??? phraseology "Phraseology"

    **RPLC_APP**: RPC122, cleared Subic Bay [STAR], expect RNP [Y/Z] RWY 07

    **RPC122**: Cleared Subic Bay [STAR], expect RNP [Y/Z] RWY 07, RPC122

    **RPLC_APP**: RPC122, descend via STAR [ALT], QNH [XXXX]

    **RPC122**: Descend via STAR [ALT], QNH [XXXX], RPC122

## Parking Bays

### Southeast Apron

|  Bay  | Aircraft Type                      |
| :---: | :--------------------------------- |
|   1   | B737-8 and lower category aircraft |
|   2   | A330 and lower category aircraft   |
|   3   | A321 and lower category aircraft   |
|  4L   | A320 and lower category aircraft   |
|  4R   | B737-8 and lower category aircraft |
|   5   | B777 and lower category aircraft   |
|  6L   | A319 and lower category aircraft   |
|  6R   | A319 and lower category aircraft   |
|   7   | A319 and lower category aircraft   |

### Southwest Apron A

|       Bay        | Aircraft Type                           |
| :--------------: | :-------------------------------------- |
| 1–6, 8–14, 16–18 | A320-200 and lower category aircraft    |
|      7, 15       | A330 / B777 and lower category aircraft |

### Southwest Apron B

|    Bay     | Aircraft Type                    |
| :--------: | :------------------------------- |
| A, B, C, D | C208 and lower category aircraft |

### Midway Apron

|  Bay  | Aircraft Type                    |
| :---: | :------------------------------- |
| 1, 2  | B747 and lower category aircraft |

*[GA]: General Aviation
*[EOBT]: Estimated off block time
*[TOBT]: Target off block time
*[TSAT]: Target start approval time
*[ASRT]: Actual start up time
*[TTOT]: Target takeoff time
*[CTOT]: Calculated takeoff time
*[RPLB_DEL]: Clearance Delivery
*[RPLB_GND]: Subic Ground
*[RPLB_TWR]: Subic Tower
*[RPLC_APP]: Clark Approach