# Training Areas

Flight Training Areas (FTAs) within the Manila FIR (RPHI) are designated blocks of airspace reserved for military and civil flight training operations. Within RPHI, these areas are identified using the **RP-T#** designation (e.g., RP-T1, RP-T6, RP-T10).

Below is a chart of all currently published Flight Training Areas within RPHI.

<iframe src="assets/pdfs/trainingareas.pdf" width="70%" height="700px"></iframe>

---

## Area Vertical Limits

The following table summarises the upper and lower vertical limits for each RP-T area:

| Area    | Upper   | Lower   |
| ------- | ------- | ------- |
| RP-T1   | 3000 FT | SFC     |
| RP-T2   | 3000 FT | SFC     |
| RP-T4   | 2500 FT | SFC     |
| RP-T5   | 2500 FT | SFC     |
| RP-T6   | 3000 FT | SFC     |
| RP-T10  | FL300   | FL210   |
| RP-T15  | 5000 FT | SFC     |
| RP-T15A | 8000 FT | SFC     |
| RP-T16  | FL240   | 6000 FT |
| RP-T17  | FL150   | SFC     |
| RP-T18  | FL200   | SFC     |
| RP-T19  | 3000 FT | SFC     |
| RP-T20  | 5000 FT | SFC     |
| RP-T21  | 3000 FT | SFC     |
| RP-T22  | 3000 FT | SFC     |
| RP-T23  | 3000 FT | SFC     |
| RP-T24  | 3000 FT | SFC     |
| RP-T25  | 3000 FT | SFC     |
| RP-T26  | 3000 FT | SFC     |
| RP-T27  | 3000 FT | SFC     |
| RP-T28  | 3000 FT | SFC     |

!!! note
    Always verify vertical limits against the current AIP Philippines ENR 5.2 before flight. Controllers may adjust approved levels based on traffic.

---

## Making a Reservation

Training area reservations within RPHI are managed through **V-LARA**, the VATSIM airspace reservation web client. Reservations are visible to ATC in real time, only make a reservation if you genuinely intend to use the airspace.

### V-Lara

=== "1. Review the Area"

    Familiarise yourself with the RP-T area you intend to use. Check the chart above and confirm the vertical limits apply to your planned activity.

=== "2. Add Your Reservation"

    Log in to V-LARA using your VATSIM account. Navigate to **Add Reservation** and fill in the following:

    - **Callsign(s)** — enter all callsigns that will be operating in the area
    - **Area** — select the applicable RP-T area from the dropdown
    - **Lower / Upper limits** — enter as Flight Levels. Use `0` for SFC and `999` for UNL
    - **Start / End time** — in UTC. Minimum duration is 30 minutes; maximum is 3 hours
    - **Remarks** — optional, but useful for coordination with ATC

    !!! warning "Advance notice required"
        Reservations must be submitted **at least 30 minutes** before the intended start time. Reservations cannot be made more than **7 days** in advance.

=== "3. File a Flight Plan"

    File a valid ICAO flight plan. For local FTA flights, insert the area identifier in the route field where applicable, and ensure your flight plan accurately reflects intended activity.

=== "4. Edit or Cancel"

    You may edit your reservation up until **30 minutes before** the start time. After that, only ATC can make modifications.

    **Please cancel your reservation** if you no longer intend to use the airspace. ATC will normally cancel the reservation once activity in the area has ended.

---

## Reservation Status Reference

| Status        | Meaning                                   |
| ------------- | ----------------------------------------- |
| **RESERVED**  | Active reservation; pilot can still edit  |
| **PENDING**   | Within 30 min of start; only ATC can edit |
| **ACTIVE**    | Area is currently in use                  |
| **CANCELLED** | Reservation has been cancelled            |

!!! tip
    If your **ACTIVE** reservation is ending within 10 minutes and activity is still ongoing, contact ATC immediately to request an extension. The reservation will be automatically cancelled when the end time is reached.

---

## Quick Rules Summary

- Reservations must be made at least **30 minutes** in advance
- Minimum reservation duration: **30 minutes**
- Maximum reservation duration: **3 hours**
- Maximum advance booking: **7 days**
- Pilots may edit reservations up to **30 minutes** before start time
- Only **one reservation** may be active per airspace block at a time