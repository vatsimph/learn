# Collaborative Decision Making (CDM)

On VATSIM, CDM is a tool that encourages virtual pilots & controllers to coordinate more effectively - much like in the real world, but adapted for an online flight simulation environment. By sharing essential departure data, planning collaborative push-back times, and adhering to consistent procedures, CDM helps to reduce airfield congestion and improve overall traffic flow. The result is a more immersive, realistic, and seamless experience for everyone involved in the virtual aviation community.

| Time | Description |
| :--- | :--- |
| EOBT | The departure time entered by the pilot on the flightplan, not useful for VATSIM as this is normally inaccurate. |
| TOBT | When the aircraft aims to push back. |
| TSAT  | When ATC plans to approve start, considering flow restrictions, taxi times, capacity etc. |
| ASRT  | The time at which the pilot requests start. |
| TTOT  | When the A-CDM system estimates the aircraft will be airborne. |
| CTOT | Also known as a "slot". The aircraft must depart -5/+10 minutes of this time. |


Below is an example of how it is setup in VATPHIL
![CDM](https://lh3.googleusercontent.com/keep-bbsk/AFgXFlKlF39IG2qT6JaBc6IimZjLIG7miSdc5tIpKIOYL5VbIr6t0_Uf7pF5Hbftbspg2uvUOZM7o5xXYKlIvegMgspANzkvfLGjIoVqGRh9FGyYCKj84KE9=s512)

Pilots can change their TOBT at https://cdm.vatsimspain.es/vdgs/index.php
To enable it, simply press on the aerodrome you are controlling. Note that only one (1) controller can be the “Master” at one time. If RPLL_P_GND is online then they take master followed by RPLL_DEL.


Red: No master set.
Purple: Master set by another ATC.
Yellow: Enabling/Disabling Master.
Green: Master Airport set by me.
![CDMLogin](https://lh3.googleusercontent.com/keep-bbsk/AFgXFlIPhto0RKvk6niFv27tZQaW147lc0Fh0axscoYtje8KxKhVEHW-6ThWb537_DuxfN01v4fwMk2UAWRu4aitG338v2wUVwOlmiyrlqayCL9Yo4IM-dTy=s586){ align=left }










*[EOBT]: Estimated off block time
*[TOBT]: Target off block time
*[TSAT]: Target start approval time
*[ASRT]: Actual start up time
*[TTOT]: Target takeoff time
*[CTOT]: Calculated takeoff time
*[RPLL_P_GND]: Manila Planner
