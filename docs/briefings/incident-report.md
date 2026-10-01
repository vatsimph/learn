---
hide:
  - toc
---

# Air Traffic Incident Report

Fill out the form below to generate an **ICAO model Air Traffic Incident Report** (Doc 4444, Appendix).

!!! warning

    This form is for **flight simulation purposes only** on the VATSIM network. It is not a real aviation incident report and must not be used for real-world reporting.

!!! note "When to use this form"

    File an air traffic incident report only when your aircraft was **receiving an air traffic control service** (under ATC). It does **not** apply to flights operating under **advisory** only.

??? info "Instructions for completion (ICAO Doc 4444)"

    | Item | Guidance |
    |------|----------|
    | **A** | Aircraft identification of the aircraft filing the report. |
    | **B** | An AIRPROX report should be filed immediately by radio. |
    | **C 1** | Date/time UTC and position in bearing and distance from a navigation aid, or in LAT/LONG. |
    | **C 2** | Information regarding the aircraft filing the report; tick as necessary. |
    | **C 2 c)** | Level and altimeter setting — e.g. FL 350 / 1013 hPa, or 2 500 ft / QNH 1007 hPa, or 1 200 ft / QFE 998 hPa. |
    | **C 3** | Information regarding the other aircraft involved. |
    | **C 4** | Passing distance — state the units used. |
    | **C 6** | Attach additional papers as required. The diagrams may be used to show the aircraft's positions. |
    | **D 1 f)** | State the name of the ATS unit and date/time in UTC. |
    | **D 1 g)** | Date and time in UTC and place of completion of the form. |
    | **E 2** | Include details of the ATS unit such as service provided, radiotelephony frequency, SSR codes assigned and altimeter setting. Use the diagram to show the aircraft's position and attach additional papers as required. |

<div id="ir-root">

<style>
#ir-root { --ir-gold:#8c7804; }
#ir-form fieldset {
  border:1px solid var(--md-default-fg-color--lightest); border-radius:8px; margin:0 0 1rem; padding:0.6rem 0.9rem 0.9rem;
}
#ir-form legend {
  font-weight:800; font-size:0.8rem; letter-spacing:0.03em; padding:0 0.4rem; color:var(--ir-gold); text-transform:uppercase;
}
#ir-form .ir-sub { font-weight:700; font-size:0.82rem; margin:0.7rem 0 0.3rem; color:var(--md-default-fg-color); }
#ir-form label.ir-q { display:block; font-size:0.8rem; font-weight:600; margin:0.55rem 0 0.2rem; }
#ir-form .ir-hint { font-weight:400; color:var(--md-default-fg-color--light); font-size:0.74rem; }
#ir-form input[type=text], #ir-form input[type=datetime-local], #ir-form textarea, #ir-form select {
  width:100%; box-sizing:border-box; background:var(--md-code-bg-color); color:var(--md-default-fg-color);
  border:1px solid var(--md-default-fg-color--lightest); border-radius:6px; padding:7px 9px; font-size:0.82rem; font-family:inherit;
}
#ir-form textarea { min-height:64px; resize:vertical; line-height:1.5; }
#ir-form input:focus, #ir-form textarea:focus, #ir-form select:focus { outline:none; border-color:var(--ir-gold); }
#ir-form .ir-opts { display:grid; grid-template-columns:repeat(auto-fit, minmax(180px, 1fr)); gap:2px 14px; margin:0.15rem 0 0.2rem; }
#ir-form .ir-opts.ir-narrow { grid-template-columns:repeat(auto-fit, minmax(140px, 1fr)); }
#ir-form .ir-opts label { display:flex; align-items:flex-start; gap:6px; font-size:0.8rem; padding:2px 0; cursor:pointer; }
#ir-form .ir-opts input { accent-color:var(--ir-gold); margin-top:2px; cursor:pointer; flex:0 0 auto; }
#ir-form .ir-inline { display:flex; flex-wrap:wrap; gap:8px 14px; align-items:center; }
#ir-form .ir-inline > div { flex:1 1 200px; }
#ir-form .ir-grid2 { display:grid; grid-template-columns:1fr 1fr; gap:10px 14px; }
@media (max-width:44em){ #ir-form .ir-grid2 { grid-template-columns:1fr; } }
#ir-actions { display:flex; flex-wrap:wrap; gap:10px; align-items:center; margin:0.4rem 0 0.5rem; }
#ir-actions button {
  font-family:inherit; font-size:0.82rem; font-weight:700; padding:10px 18px; border-radius:8px; cursor:pointer; border:1px solid var(--ir-gold);
}
#ir-gen { background:var(--ir-gold); color:#1a1a1a; }
#ir-gen:hover { filter:brightness(1.1); }
#ir-send { background:transparent; color:var(--md-default-fg-color); }
#ir-send:hover { border-color:var(--ir-gold); }
#ir-reset { background:transparent; color:var(--md-default-fg-color--light); border-color:var(--md-default-fg-color--lightest); font-weight:600; }
#ir-status { font-size:0.78rem; color:var(--md-default-fg-color--light); }
#ir-status.err { color:#d34; }
#ir-status.ok { color:#2a9d5c; }
.ir-note { font-size:0.74rem; color:var(--md-default-fg-color--light); margin:0.2rem 0 0.6rem; }
.ir-diagrams { display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-top:0.3rem; }
@media (max-width:44em){ .ir-diagrams { grid-template-columns:1fr; } }
.ir-diag-h { font-size:0.76rem; font-weight:700; margin-bottom:4px; }
#ir-form canvas { width:100%; max-width:360px; height:auto; aspect-ratio:28/20; display:block;
  border:1px solid var(--md-default-fg-color--lightest); border-radius:6px; background:#fff; cursor:crosshair; touch-action:none; }
.ir-diag-btns { display:flex; gap:8px; margin-top:5px; }
.ir-diag-btns button { font-family:inherit; font-size:0.72rem; font-weight:600; padding:4px 11px; border-radius:6px;
  border:1px solid var(--md-default-fg-color--lightest); background:transparent; color:var(--md-default-fg-color--light); cursor:pointer; }
.ir-diag-btns button:hover { border-color:var(--ir-gold); color:var(--md-default-fg-color); }
</style>

<form id="ir-form" autocomplete="off" onsubmit="return false;">

  <div class="ir-grid2">
    <fieldset>
      <legend>A — Aircraft identification</legend>
      <label class="ir-q" for="ir-acid">Your aircraft identification (callsign)</label>
      <input type="text" id="ir-acid" placeholder="e.g. PAL431">
    </fieldset>
    <fieldset>
      <legend>B — Type of incident</legend>
      <label class="ir-q">Select one</label>
      <div class="ir-opts" data-radio="inctype" style="grid-template-columns:1fr;">
        <label><input type="radio" name="inctype" value="AIRPROX"> <span><strong>AIRPROX</strong> <span class="ir-hint">— proximity to another aircraft compromised safety (near-miss / loss of separation)</span></span></label>
        <label><input type="radio" name="inctype" value="PROCEDURE"> <span><strong>PROCEDURE</strong> <span class="ir-hint">— caused by applying, or failing to apply, ATS procedures</span></span></label>
        <label><input type="radio" name="inctype" value="FACILITY"> <span><strong>FACILITY</strong> <span class="ir-hint">— caused by a failure or malfunction of a facility (comms, navaid, radar, lighting)</span></span></label>
      </div>
      <p class="ir-note" style="margin-top:6px;">An AIRPROX report should be filed immediately by radio.</p>
    </fieldset>
  </div>

  <fieldset>
    <legend>C — The incident</legend>

    <div class="ir-sub">1. General</div>
    <div class="ir-grid2">
      <div><label class="ir-q" for="ir-datetime">a) Date / time of incident (UTC)</label><input type="text" id="ir-datetime" placeholder="e.g. 12 OCT 2026 / 0430Z"></div>
      <div><label class="ir-q" for="ir-position">b) Position <span class="ir-hint">(bearing/distance from a navaid, or LAT/LONG)</span></label><input type="text" id="ir-position" placeholder="e.g. 15 NM SE of MIA VOR, FL350"></div>
    </div>

    <div class="ir-sub">2. Own aircraft</div>
    <label class="ir-q" for="ir-o-headroute">a) Heading and route</label>
    <input type="text" id="ir-o-headroute">
    <label class="ir-q">b) True airspeed</label>
    <div class="ir-inline">
      <div><input type="text" id="ir-o-tas" placeholder="measured value"></div>
      <div class="ir-opts ir-narrow" data-radio="o-tasunit" style="flex:0 0 auto;">
        <label><input type="radio" name="o-tasunit" value="kt"> kt</label>
        <label><input type="radio" name="o-tasunit" value="km/h"> km/h</label>
      </div>
    </div>
    <label class="ir-q" for="ir-o-level">c) Level and altimeter setting</label>
    <input type="text" id="ir-o-level" placeholder="e.g. FL350 / 1013 hPa, or 2500 ft / QNH 1007">
    <label class="ir-q">d) Aircraft climbing or descending</label>
    <div class="ir-opts" data-radio="o-vs">
      <label><input type="radio" name="o-vs" value="Level flight"> Level flight</label>
      <label><input type="radio" name="o-vs" value="Climbing"> Climbing</label>
      <label><input type="radio" name="o-vs" value="Descending"> Descending</label>
    </div>
    <label class="ir-q">e) Aircraft bank angle</label>
    <div class="ir-opts" data-radio="o-bank">
      <label><input type="radio" name="o-bank" value="Wings level"> Wings level</label>
      <label><input type="radio" name="o-bank" value="Slight bank"> Slight bank</label>
      <label><input type="radio" name="o-bank" value="Moderate bank"> Moderate bank</label>
      <label><input type="radio" name="o-bank" value="Steep bank"> Steep bank</label>
      <label><input type="radio" name="o-bank" value="Inverted"> Inverted</label>
      <label><input type="radio" name="o-bank" value="Unknown"> Unknown</label>
    </div>
    <label class="ir-q">f) Aircraft direction of bank</label>
    <div class="ir-opts" data-radio="o-bankdir">
      <label><input type="radio" name="o-bankdir" value="Left"> Left</label>
      <label><input type="radio" name="o-bankdir" value="Right"> Right</label>
      <label><input type="radio" name="o-bankdir" value="Unknown"> Unknown</label>
    </div>
    <label class="ir-q">g) Restrictions to visibility <span class="ir-hint">(select as many as required)</span></label>
    <div class="ir-opts" data-checks="o-vis">
      <label><input type="checkbox" name="o-vis" value="Sunglare"> Sunglare</label>
      <label><input type="checkbox" name="o-vis" value="Windscreen pillar"> Windscreen pillar</label>
      <label><input type="checkbox" name="o-vis" value="Dirty windscreen"> Dirty windscreen</label>
      <label><input type="checkbox" name="o-vis" value="Other cockpit structure"> Other cockpit structure</label>
      <label><input type="checkbox" name="o-vis" value="None"> None</label>
    </div>
    <label class="ir-q">h) Use of aircraft lighting <span class="ir-hint">(select as many as required)</span></label>
    <div class="ir-opts" data-checks="o-lights">
      <label><input type="checkbox" name="o-lights" value="Navigation lights"> Navigation lights</label>
      <label><input type="checkbox" name="o-lights" value="Strobe lights"> Strobe lights</label>
      <label><input type="checkbox" name="o-lights" value="Cabin lights"> Cabin lights</label>
      <label><input type="checkbox" name="o-lights" value="Red anti-collision lights"> Red anti-collision lights</label>
      <label><input type="checkbox" name="o-lights" value="Landing / taxi lights"> Landing / taxi lights</label>
      <label><input type="checkbox" name="o-lights" value="Logo (tail fin) lights"> Logo (tail fin) lights</label>
      <label><input type="checkbox" name="o-lights" value="Other"> Other</label>
      <label><input type="checkbox" name="o-lights" value="None"> None</label>
    </div>
    <label class="ir-q">i) Traffic avoidance advice issued by ATS</label>
    <div class="ir-opts" data-radio="o-taa">
      <label><input type="radio" name="o-taa" value="Yes, based on radar"> Yes, based on radar</label>
      <label><input type="radio" name="o-taa" value="Yes, based on visual sighting"> Yes, based on visual sighting</label>
      <label><input type="radio" name="o-taa" value="Yes, based on other information"> Yes, based on other information</label>
      <label><input type="radio" name="o-taa" value="No"> No</label>
    </div>
    <label class="ir-q">j) Traffic information issued</label>
    <div class="ir-opts" data-radio="o-ti">
      <label><input type="radio" name="o-ti" value="Yes, based on radar"> Yes, based on radar</label>
      <label><input type="radio" name="o-ti" value="Yes, based on visual sighting"> Yes, based on visual sighting</label>
      <label><input type="radio" name="o-ti" value="Yes, based on other information"> Yes, based on other information</label>
      <label><input type="radio" name="o-ti" value="No"> No</label>
    </div>
    <label class="ir-q">k) Airborne collision avoidance system — ACAS</label>
    <div class="ir-opts" data-radio="o-acas">
      <label><input type="radio" name="o-acas" value="Not carried"> Not carried</label>
      <label><input type="radio" name="o-acas" value="Traffic advisory issued"> Traffic advisory issued</label>
      <label><input type="radio" name="o-acas" value="Resolution advisory issued"> Resolution advisory issued</label>
      <label><input type="radio" name="o-acas" value="Traffic advisory or resolution advisory not issued"> TA/RA not issued</label>
    </div>
    <label class="ir-q" for="ir-o-acastype">ACAS type <span class="ir-hint">(if carried)</span></label>
    <input type="text" id="ir-o-acastype" placeholder="e.g. TCAS II 7.1">
    <label class="ir-q">l) Radar identification</label>
    <div class="ir-opts" data-radio="o-radar">
      <label><input type="radio" name="o-radar" value="No radar available"> No radar available</label>
      <label><input type="radio" name="o-radar" value="Radar identification"> Radar identification</label>
      <label><input type="radio" name="o-radar" value="No radar identification"> No radar identification</label>
    </div>
    <label class="ir-q">m) Other aircraft sighted</label>
    <div class="ir-opts" data-radio="o-sighted">
      <label><input type="radio" name="o-sighted" value="Yes"> Yes</label>
      <label><input type="radio" name="o-sighted" value="No"> No</label>
      <label><input type="radio" name="o-sighted" value="Wrong aircraft sighted"> Wrong aircraft sighted</label>
    </div>
    <label class="ir-q">n) Avoiding action taken</label>
    <div class="ir-opts" data-radio="o-avoid">
      <label><input type="radio" name="o-avoid" value="Yes"> Yes</label>
      <label><input type="radio" name="o-avoid" value="No"> No</label>
    </div>
    <label class="ir-q">o) Type of flight plan</label>
    <div class="ir-opts" data-radio="o-fpl">
      <label><input type="radio" name="o-fpl" value="IFR"> IFR</label>
      <label><input type="radio" name="o-fpl" value="VFR"> VFR</label>
      <label><input type="radio" name="o-fpl" value="none"> none</label>
    </div>

    <div class="ir-sub">3. Other aircraft</div>
    <label class="ir-q" for="ir-x-typecs">a) Type and call sign / registration <span class="ir-hint">(if known)</span></label>
    <input type="text" id="ir-x-typecs">
    <label class="ir-q">b) If a) above not known, describe below</label>
    <div class="ir-opts" data-checks="x-wing">
      <label><input type="checkbox" name="x-wing" value="High wing"> High wing</label>
      <label><input type="checkbox" name="x-wing" value="Mid wing"> Mid wing</label>
      <label><input type="checkbox" name="x-wing" value="Low wing"> Low wing</label>
      <label><input type="checkbox" name="x-wing" value="Rotorcraft"> Rotorcraft</label>
    </div>
    <div class="ir-opts" data-checks="x-eng">
      <label><input type="checkbox" name="x-eng" value="1 engine"> 1 engine</label>
      <label><input type="checkbox" name="x-eng" value="2 engines"> 2 engines</label>
      <label><input type="checkbox" name="x-eng" value="3 engines"> 3 engines</label>
      <label><input type="checkbox" name="x-eng" value="4 engines"> 4 engines</label>
      <label><input type="checkbox" name="x-eng" value="More than 4 engines"> More than 4 engines</label>
    </div>
    <label class="ir-q" for="ir-x-marking">Marking, colour or other available details</label>
    <textarea id="ir-x-marking"></textarea>
    <label class="ir-q">c) Aircraft climbing or descending</label>
    <div class="ir-opts" data-radio="x-vs">
      <label><input type="radio" name="x-vs" value="Level flight"> Level flight</label>
      <label><input type="radio" name="x-vs" value="Climbing"> Climbing</label>
      <label><input type="radio" name="x-vs" value="Descending"> Descending</label>
      <label><input type="radio" name="x-vs" value="Unknown"> Unknown</label>
    </div>
    <label class="ir-q">d) Aircraft bank angle</label>
    <div class="ir-opts" data-radio="x-bank">
      <label><input type="radio" name="x-bank" value="Wings level"> Wings level</label>
      <label><input type="radio" name="x-bank" value="Slight bank"> Slight bank</label>
      <label><input type="radio" name="x-bank" value="Moderate bank"> Moderate bank</label>
      <label><input type="radio" name="x-bank" value="Steep bank"> Steep bank</label>
      <label><input type="radio" name="x-bank" value="Inverted"> Inverted</label>
      <label><input type="radio" name="x-bank" value="Unknown"> Unknown</label>
    </div>
    <label class="ir-q">e) Aircraft direction of bank</label>
    <div class="ir-opts" data-radio="x-bankdir">
      <label><input type="radio" name="x-bankdir" value="Left"> Left</label>
      <label><input type="radio" name="x-bankdir" value="Right"> Right</label>
      <label><input type="radio" name="x-bankdir" value="Unknown"> Unknown</label>
    </div>
    <label class="ir-q">f) Lights displayed</label>
    <div class="ir-opts" data-checks="x-lights">
      <label><input type="checkbox" name="x-lights" value="Navigation lights"> Navigation lights</label>
      <label><input type="checkbox" name="x-lights" value="Strobe lights"> Strobe lights</label>
      <label><input type="checkbox" name="x-lights" value="Cabin lights"> Cabin lights</label>
      <label><input type="checkbox" name="x-lights" value="Red anti-collision lights"> Red anti-collision lights</label>
      <label><input type="checkbox" name="x-lights" value="Landing / taxi lights"> Landing / taxi lights</label>
      <label><input type="checkbox" name="x-lights" value="Logo (tail fin) lights"> Logo (tail fin) lights</label>
      <label><input type="checkbox" name="x-lights" value="Other"> Other</label>
      <label><input type="checkbox" name="x-lights" value="None"> None</label>
      <label><input type="checkbox" name="x-lights" value="Unknown"> Unknown</label>
    </div>
    <label class="ir-q">g) Traffic avoidance advice issued by ATS</label>
    <div class="ir-opts" data-radio="x-taa">
      <label><input type="radio" name="x-taa" value="Yes, based on radar"> Yes, based on radar</label>
      <label><input type="radio" name="x-taa" value="Yes, based on visual sighting"> Yes, based on visual sighting</label>
      <label><input type="radio" name="x-taa" value="Yes, based on other information"> Yes, based on other information</label>
      <label><input type="radio" name="x-taa" value="No"> No</label>
      <label><input type="radio" name="x-taa" value="Unknown"> Unknown</label>
    </div>
    <label class="ir-q">h) Traffic information issued</label>
    <div class="ir-opts" data-radio="x-ti">
      <label><input type="radio" name="x-ti" value="Yes, based on radar"> Yes, based on radar</label>
      <label><input type="radio" name="x-ti" value="Yes, based on visual sighting"> Yes, based on visual sighting</label>
      <label><input type="radio" name="x-ti" value="Yes, based on other information"> Yes, based on other information</label>
      <label><input type="radio" name="x-ti" value="No"> No</label>
      <label><input type="radio" name="x-ti" value="Unknown"> Unknown</label>
    </div>
    <label class="ir-q">i) Avoiding action taken</label>
    <div class="ir-opts" data-radio="x-avoid">
      <label><input type="radio" name="x-avoid" value="Yes"> Yes</label>
      <label><input type="radio" name="x-avoid" value="No"> No</label>
      <label><input type="radio" name="x-avoid" value="Unknown"> Unknown</label>
    </div>

    <div class="ir-sub">4. Distance</div>
    <div class="ir-grid2">
      <div><label class="ir-q" for="ir-dist-h">a) Closest horizontal distance <span class="ir-hint">(state units)</span></label><input type="text" id="ir-dist-h" placeholder="e.g. 0.5 NM"></div>
      <div><label class="ir-q" for="ir-dist-v">b) Closest vertical distance <span class="ir-hint">(state units)</span></label><input type="text" id="ir-dist-v" placeholder="e.g. 200 ft"></div>
    </div>

    <div class="ir-sub">5. Flight weather conditions</div>
    <label class="ir-q">a) IMC / VMC</label>
    <div class="ir-opts" data-radio="wx-imcvmc">
      <label><input type="radio" name="wx-imcvmc" value="IMC"> IMC</label>
      <label><input type="radio" name="wx-imcvmc" value="VMC"> VMC</label>
    </div>
    <label class="ir-q" for="ir-wx-cloudrel">b) Above / below clouds / fog / haze or between layers</label>
    <input type="text" id="ir-wx-cloudrel">
    <label class="ir-q">c) Distance vertically from cloud</label>
    <div class="ir-grid2">
      <div><input type="text" id="ir-wx-cloudbelow" placeholder="m / ft below"></div>
      <div><input type="text" id="ir-wx-cloudabove" placeholder="m / ft above"></div>
    </div>
    <label class="ir-q">d) In cloud / rain / snow / sleet / fog / haze</label>
    <div class="ir-opts" data-checks="wx-in">
      <label><input type="checkbox" name="wx-in" value="In cloud"> In cloud</label>
      <label><input type="checkbox" name="wx-in" value="Rain"> Rain</label>
      <label><input type="checkbox" name="wx-in" value="Snow"> Snow</label>
      <label><input type="checkbox" name="wx-in" value="Sleet"> Sleet</label>
      <label><input type="checkbox" name="wx-in" value="Fog"> Fog</label>
      <label><input type="checkbox" name="wx-in" value="Haze"> Haze</label>
    </div>
    <label class="ir-q">e) Flying into / out of sun</label>
    <div class="ir-opts" data-radio="wx-sun">
      <label><input type="radio" name="wx-sun" value="Flying into sun"> Flying into sun</label>
      <label><input type="radio" name="wx-sun" value="Flying out of sun"> Flying out of sun</label>
      <label><input type="radio" name="wx-sun" value="N/A"> N/A</label>
    </div>
    <label class="ir-q" for="ir-wx-vis">f) Flight visibility</label>
    <input type="text" id="ir-wx-vis" placeholder="e.g. 10 km">

    <div class="ir-sub">6. Any other information considered important by the pilot-in-command</div>
    <textarea id="ir-other" style="min-height:110px;"></textarea>
  </fieldset>

  <fieldset>
    <legend>D — Miscellaneous</legend>
    <div class="ir-sub">1. Information regarding reporting aircraft</div>
    <div class="ir-grid2">
      <div><label class="ir-q" for="ir-d-reg">a) Aircraft registration</label><input type="text" id="ir-d-reg"></div>
      <div><label class="ir-q" for="ir-d-type">b) Aircraft type</label><input type="text" id="ir-d-type"></div>
      <div><label class="ir-q" for="ir-d-operator">c) Operator</label><input type="text" id="ir-d-operator"></div>
      <div><label class="ir-q" for="ir-d-adep">d) Aerodrome of departure</label><input type="text" id="ir-d-adep"></div>
      <div><label class="ir-q" for="ir-d-firstland">e) Aerodrome of first landing</label><input type="text" id="ir-d-firstland"></div>
      <div><label class="ir-q" for="ir-d-dest">&nbsp;&nbsp;&nbsp;destination</label><input type="text" id="ir-d-dest"></div>
    </div>
    <label class="ir-q">f) Reported by radio or other means to</label>
    <div class="ir-grid2">
      <div><input type="text" id="ir-d-reportedto" placeholder="name of ATS unit"></div>
      <div><input type="text" id="ir-d-reportedtime" placeholder="at time UTC"></div>
    </div>
    <label class="ir-q" for="ir-d-completion">g) Date / time / place of completion of form</label>
    <input type="text" id="ir-d-completion">
    <div class="ir-sub">2. Function, address and signature of person submitting report</div>
    <div class="ir-grid2">
      <div><label class="ir-q" for="ir-d-function">a) Function</label><input type="text" id="ir-d-function"></div>
      <div><label class="ir-q" for="ir-d-phone">d) Telephone number</label><input type="text" id="ir-d-phone"></div>
      <div><label class="ir-q" for="ir-d-address">b) Address</label><input type="text" id="ir-d-address"></div>
      <div><label class="ir-q" for="ir-d-signature">c) Signature (name)</label><input type="text" id="ir-d-signature"></div>
      <div><label class="ir-q" for="ir-d-cid">VATSIM CID</label><input type="text" id="ir-d-cid" inputmode="numeric" placeholder="e.g. 1234567"></div>
    </div>
  </fieldset>

  <fieldset>
    <legend>E — Supplementary information by ATS unit concerned</legend>
    <p class="ir-note">Completed by the receiving ATS unit. Leave blank if you are the reporter.</p>
    <div class="ir-sub">1. Receipt of report</div>
    <label class="ir-q">a) Report received via</label>
    <div class="ir-opts" data-radio="e-via">
      <label><input type="radio" name="e-via" value="AFTN"> AFTN</label>
      <label><input type="radio" name="e-via" value="radio"> radio</label>
      <label><input type="radio" name="e-via" value="telephone"> telephone</label>
      <label><input type="radio" name="e-via" value="other"> other</label>
    </div>
    <input type="text" id="ir-e-viaother" placeholder="if other, specify">
    <label class="ir-q" for="ir-e-recvby">b) Report received by <span class="ir-hint">(name of ATS unit)</span></label>
    <input type="text" id="ir-e-recvby">
    <div class="ir-sub">2. Details of ATS action</div>
    <p class="ir-note">Clearance, incident seen (radar/visually), warning given, result of local enquiry, etc.</p>
    <textarea id="ir-e-action" style="min-height:110px;"></textarea>
  </fieldset>

  <fieldset>
    <legend>Diagrams of AIRPROX <span class="ir-hint" style="text-transform:none;">(optional)</span></legend>
    <p class="ir-note">Click on each grid to plot the <strong>other</strong> aircraft's passage relative to you. The first click marks the first sighting; each further click extends its track, with an arrow on the last leg.</p>
    <div class="ir-diagrams">
      <div class="ir-diag">
        <div class="ir-diag-h">View from above (plan)</div>
        <canvas id="ir-cv-above" width="336" height="240" aria-label="Plot the other aircraft, plan view"></canvas>
        <div class="ir-diag-btns"><button type="button" data-undo="above">Undo point</button><button type="button" data-clear="above">Clear</button></div>
      </div>
      <div class="ir-diag">
        <div class="ir-diag-h">View from astern (elevation)</div>
        <canvas id="ir-cv-astern" width="336" height="240" aria-label="Plot the other aircraft, elevation view"></canvas>
        <div class="ir-diag-btns"><button type="button" data-undo="astern">Undo point</button><button type="button" data-clear="astern">Clear</button></div>
      </div>
    </div>
  </fieldset>

</form>

<div id="ir-actions">
  <button type="button" id="ir-gen">Generate PDF</button>
  <button type="button" id="ir-send">Send to staff</button>
  <button type="button" id="ir-reset">Clear form</button>
  <span id="ir-status"></span>
</div>

</div>

<script>
(function () {
  var root = document.getElementById('ir-root');
  if (!root || root._irInit) return;
  root._irInit = true;

  var STAFF_EMAIL = 'staff@vatphil.com';
  // Discord webhook that receives reports (posts the PDF + a summary to a staff channel).
  // Set to your channel's webhook URL, e.g. "https://discord.com/api/webhooks/<id>/<token>".
  // NOTE: this URL is visible in the page source of this public site — anyone who finds it can
  // post to that channel. Use a dedicated channel and regenerate the webhook if it is abused.
  // While empty, "Send to staff" downloads the PDF and opens an email draft instead.
  var WEBHOOK_URL = 'https://discord.com/api/webhooks/1554869982104649758/mou2wLjW1T7EORlSQCa9g02AtPBwHWW_t3-aiF8oYgaJhg8L5z4rf5NtaYQ37CG4FeEA';

  var PDFMAKE = 'https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.2.10/pdfmake.min.js';
  var PDFVFS  = 'https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.2.10/vfs_fonts.js';

  function statusMsg(msg, cls) {
    var el = document.getElementById('ir-status');
    if (el) { el.textContent = msg || ''; el.className = cls || ''; }
  }
  function loadScript(src) {
    return new Promise(function (res, rej) {
      var s = document.createElement('script'); s.src = src;
      s.onload = res; s.onerror = function () { rej(new Error('load ' + src)); };
      document.head.appendChild(s);
    });
  }
  var pdfReady = null;
  function ensurePdf() {
    if (window.pdfMake && window.pdfMake.vfs) return Promise.resolve();
    if (!pdfReady) {
      pdfReady = loadScript(PDFMAKE).then(function () { return loadScript(PDFVFS); })
        .catch(function (e) { pdfReady = null; throw e; });
    }
    return pdfReady;
  }

  // ---- field readers ----
  function txt(id) { var e = document.getElementById('ir-' + id); return e ? e.value.trim() : ''; }
  function radio(name) { var e = document.querySelector('#ir-form input[name="' + name + '"]:checked'); return e ? e.value : ''; }
  function checks(name) { return Array.prototype.map.call(document.querySelectorAll('#ir-form input[name="' + name + '"]:checked'), function (e) { return e.value; }); }

  // ---- pdf helpers ----
  var GREY = '#e6e6e6';
  function sectionHeader(text) {
    return { table: { widths: ['*'], body: [[{ text: text, bold: true, fontSize: 10, fillColor: GREY, margin: [4, 3, 4, 3] }]] }, margin: [0, 8, 0, 3] };
  }
  function subHeader(text) { return { text: text, bold: true, fontSize: 9, fillColor: GREY, margin: [0, 4, 0, 2], padding: 2 }; }
  function line(label, value) {
    return { text: [{ text: label + '  ', bold: true }, { text: value || '', color: value ? 'black' : '#888' }], fontSize: 9, margin: [0, 1.5, 0, 1.5] };
  }
  // option list rendered as ( )/(X) across N columns; selected may be string or array
  function opts(options, selected, cols) {
    cols = cols || 3;
    var sel = Array.isArray(selected) ? selected : (selected ? [selected] : []);
    var rows = [];
    for (var i = 0; i < options.length; i += cols) {
      var slice = options.slice(i, i + cols);
      rows.push({
        columns: slice.map(function (o) {
          var on = sel.indexOf(o) !== -1;
          return { text: (on ? '(X)  ' : '(  )  ') + o, width: '*', fontSize: 8.5, bold: on };
        }),
        columnGap: 6, margin: [12, 1, 0, 1]
      });
    }
    return rows;
  }
  // a lettered question with its option rows
  function q(letter, label, options, selected, cols) {
    var out = [{ text: letter + ')  ' + label, fontSize: 9, bold: false, margin: [0, 3, 0, 1] }];
    return out.concat(opts(options, selected, cols));
  }
  function qtext(letter, label, value) {
    return { text: [{ text: letter + ')  ' + label + ':  ', fontSize: 9 }, { text: value || '', fontSize: 9, bold: true }], margin: [0, 3, 0, 1] };
  }
  // "delete as appropriate" — show all, bold+underline the chosen
  function deleteAsApt(options, selected) {
    var parts = [];
    options.forEach(function (o, i) {
      if (i) parts.push({ text: '  /  ', fontSize: 10 });
      parts.push(o === selected ? { text: o, bold: true, decoration: 'underline', fontSize: 10 } : { text: o, fontSize: 10, color: '#555' });
    });
    return { text: parts, margin: [0, 2, 0, 2] };
  }

  // reporter-plotted points per view, normalised [0..1] over the grid
  var PLOT = { above: [], astern: [] };
  var MARK = '#c0392b';

  // ---- airprox diagram (grid + own-aircraft silhouette + scale + plotted track) ----
  function diagram(view, plan, vlabel, pts) {
    var cell = 8.5, cols = 28, rows = 20;         // 14..0..14 horizontal, 10..0..10 vertical
    var w = cols * cell, h = rows * cell, cx = w / 2, cy = h / 2;
    var c = [];
    for (var i = 0; i <= cols; i++) c.push({ type: 'line', x1: i * cell, y1: 0, x2: i * cell, y2: h, lineWidth: (i % 2 ? 0.2 : 0.4), lineColor: '#999' });
    for (var j = 0; j <= rows; j++) c.push({ type: 'line', x1: 0, y1: j * cell, x2: w, y2: j * cell, lineWidth: (j % 2 ? 0.2 : 0.4), lineColor: '#999' });
    // own-aircraft silhouette at centre
    if (plan) { // view from above: nose up
      c.push({ type: 'line', x1: cx, y1: cy - 16, x2: cx, y2: cy + 12, lineWidth: 2 });
      c.push({ type: 'line', x1: cx - 15, y1: cy - 1, x2: cx + 15, y2: cy - 1, lineWidth: 2 });
      c.push({ type: 'line', x1: cx - 6, y1: cy + 11, x2: cx + 6, y2: cy + 11, lineWidth: 2 });
    } else { // view from astern: front-on
      c.push({ type: 'line', x1: cx - 16, y1: cy, x2: cx + 16, y2: cy, lineWidth: 2 });
      c.push({ type: 'line', x1: cx, y1: cy, x2: cx, y2: cy - 12, lineWidth: 2 });
      c.push({ type: 'ellipse', x: cx, y: cy, r1: 3, r2: 3, color: 'black' });
    }
    // plotted track of the other aircraft
    if (pts && pts.length) {
      var P = pts.map(function (p) { return { x: p.x * w, y: p.y * h }; });
      if (P.length >= 2) c.push({ type: 'polyline', lineWidth: 1.4, lineColor: MARK, points: P });
      c.push({ type: 'ellipse', x: P[0].x, y: P[0].y, r1: 3.5, r2: 3.5, lineColor: MARK, lineWidth: 1.4 }); // first sighting (hollow)
      P.forEach(function (p) { c.push({ type: 'ellipse', x: p.x, y: p.y, r1: 1.6, r2: 1.6, color: MARK }); });
      if (P.length >= 2) {
        var a = P[P.length - 2], b = P[P.length - 1], ang = Math.atan2(b.y - a.y, b.x - a.x), L = 6;
        c.push({ type: 'line', x1: b.x, y1: b.y, x2: b.x - L * Math.cos(ang - 0.5), y2: b.y - L * Math.sin(ang - 0.5), lineWidth: 1.4, lineColor: MARK });
        c.push({ type: 'line', x1: b.x, y1: b.y, x2: b.x - L * Math.cos(ang + 0.5), y2: b.y - L * Math.sin(ang + 0.5), lineWidth: 1.4, lineColor: MARK });
      }
    }
    var nums = [];
    for (var a2 = 14; a2 >= 0; a2 -= 2) nums.push(a2);
    for (var b2 = 2; b2 <= 14; b2 += 2) nums.push(b2);
    var hstrip = { columns: nums.map(function (n) { return { text: String(n), fontSize: 5, alignment: 'center', width: '*' }; }), columnGap: 0, margin: [0, 1, 0, 0] };
    return {
      stack: [
        { text: 'Hundreds of metres', fontSize: 7, margin: [0, 0, 0, 1] },
        { canvas: c },
        hstrip,
        { text: view, alignment: 'center', bold: true, fontSize: 8, margin: [0, 2, 0, 0] },
        vlabel ? { text: vlabel, alignment: 'center', fontSize: 6, color: '#555', margin: [0, 1, 0, 0] } : ''
      ], width: w
    };
  }

  function buildDoc() {
    var content = [];
    content.push({ text: 'AIR TRAFFIC INCIDENT REPORT FORM', style: 'title', alignment: 'center' });
    content.push({ text: 'For use when submitting and receiving reports on air traffic incidents. In an initial report by radio, shaded items should be included.', italics: true, fontSize: 8.5, margin: [0, 2, 0, 4] });

    // A / B side by side
    content.push({
      table: {
        widths: ['*', '*'],
        body: [[
          { stack: [{ text: 'A — AIRCRAFT IDENTIFICATION', bold: true, fontSize: 9 }, { text: txt('acid') || ' ', bold: true, fontSize: 11, margin: [0, 6, 0, 0] }], fillColor: GREY, margin: [4, 3, 4, 6] },
          { stack: [{ text: 'B — TYPE OF INCIDENT', bold: true, fontSize: 9 }, deleteAsApt(['AIRPROX', 'PROCEDURE', 'FACILITY'], radio('inctype'))], margin: [4, 3, 4, 6] }
        ]]
      }, margin: [0, 4, 0, 0]
    });

    // C
    content.push(sectionHeader('C — THE INCIDENT'));
    content.push({ text: '1.  General', bold: true, fontSize: 9.5, fillColor: GREY, margin: [0, 2, 0, 2] });
    content.push(qtext('a', 'Date / time of incident UTC', txt('datetime')));
    content.push(qtext('b', 'Position', txt('position')));

    content.push({ text: '2.  Own aircraft', bold: true, fontSize: 9.5, margin: [0, 6, 0, 2] });
    content.push(qtext('a', 'Heading and route', txt('o-headroute')));
    content.push(qtext('b', 'True airspeed', (txt('o-tas') ? txt('o-tas') + (radio('o-tasunit') ? ' ' + radio('o-tasunit') : '') : '')));
    content.push(qtext('c', 'Level and altimeter setting', txt('o-level')));
    content = content.concat(q('d', 'Aircraft climbing or descending', ['Level flight', 'Climbing', 'Descending'], radio('o-vs')));
    content = content.concat(q('e', 'Aircraft bank angle', ['Wings level', 'Slight bank', 'Moderate bank', 'Steep bank', 'Inverted', 'Unknown'], radio('o-bank')));
    content = content.concat(q('f', 'Aircraft direction of bank', ['Left', 'Right', 'Unknown'], radio('o-bankdir')));
    content = content.concat(q('g', 'Restrictions to visibility (select as many as required)', ['Sunglare', 'Windscreen pillar', 'Dirty windscreen', 'Other cockpit structure', 'None'], checks('o-vis')));
    content = content.concat(q('h', 'Use of aircraft lighting (select as many as required)', ['Navigation lights', 'Strobe lights', 'Cabin lights', 'Red anti-collision lights', 'Landing / taxi lights', 'Logo (tail fin) lights', 'Other', 'None'], checks('o-lights')));
    content = content.concat(q('i', 'Traffic avoidance advice issued by VATPHIL', ['Yes, based on radar', 'Yes, based on visual sighting', 'Yes, based on other information', 'No'], radio('o-taa')));
    content = content.concat(q('j', 'Traffic information issued', ['Yes, based on radar', 'Yes, based on visual sighting', 'Yes, based on other information', 'No'], radio('o-ti')));
    content = content.concat(q('k', 'Airborne collision avoidance system — ACAS', ['Not carried', 'Traffic advisory issued', 'Resolution advisory issued', 'Traffic advisory or resolution advisory not issued'], radio('o-acas')));
    if (txt('o-acastype')) content.push({ text: [{ text: '     ACAS type:  ', fontSize: 8.5 }, { text: txt('o-acastype'), bold: true, fontSize: 8.5 }], margin: [12, 0, 0, 1] });
    content = content.concat(q('l', 'Radar identification', ['No radar available', 'Radar identification', 'No radar identification'], radio('o-radar')));
    content = content.concat(q('m', 'Other aircraft sighted', ['Yes', 'No', 'Wrong aircraft sighted'], radio('o-sighted')));
    content = content.concat(q('n', 'Avoiding action taken', ['Yes', 'No'], radio('o-avoid')));
    content.push(qtext('o', 'Type of flight plan', radio('o-fpl')));

    content.push({ text: '3.  Other aircraft', bold: true, fontSize: 9.5, margin: [0, 6, 0, 2] });
    content.push(qtext('a', 'Type and call sign / registration (if known)', txt('x-typecs')));
    content = content.concat(q('b', 'If a) above not known, describe below', ['High wing', 'Mid wing', 'Low wing', 'Rotorcraft'], checks('x-wing')));
    content = content.concat(opts(['1 engine', '2 engines', '3 engines', '4 engines', 'More than 4 engines'], checks('x-eng')));
    content.push({ text: [{ text: '     Marking, colour or other available details:  ', fontSize: 8.5 }, { text: txt('x-marking') || '', bold: true, fontSize: 8.5 }], margin: [12, 1, 0, 1] });
    content = content.concat(q('c', 'Aircraft climbing or descending', ['Level flight', 'Climbing', 'Descending', 'Unknown'], radio('x-vs')));
    content = content.concat(q('d', 'Aircraft bank angle', ['Wings level', 'Slight bank', 'Moderate bank', 'Steep bank', 'Inverted', 'Unknown'], radio('x-bank')));
    content = content.concat(q('e', 'Aircraft direction of bank', ['Left', 'Right', 'Unknown'], radio('x-bankdir')));
    content = content.concat(q('f', 'Lights displayed', ['Navigation lights', 'Strobe lights', 'Cabin lights', 'Red anti-collision lights', 'Landing / taxi lights', 'Logo (tail fin) lights', 'Other', 'None', 'Unknown'], checks('x-lights')));
    content = content.concat(q('g', 'Traffic avoidance advice issued by VATPHIL', ['Yes, based on radar', 'Yes, based on visual sighting', 'Yes, based on other information', 'No', 'Unknown'], radio('x-taa')));
    content = content.concat(q('h', 'Traffic information issued', ['Yes, based on radar', 'Yes, based on visual sighting', 'Yes, based on other information', 'No', 'Unknown'], radio('x-ti')));
    content = content.concat(q('i', 'Avoiding action taken', ['Yes', 'No', 'Unknown'], radio('x-avoid')));

    content.push({ text: '4.  Distance', bold: true, fontSize: 9.5, fillColor: GREY, margin: [0, 6, 0, 2] });
    content.push(qtext('a', 'Closest horizontal distance', txt('dist-h')));
    content.push(qtext('b', 'Closest vertical distance', txt('dist-v')));

    content.push({ text: '5.  Flight weather conditions', bold: true, fontSize: 9.5, margin: [0, 6, 0, 2] });
    content = content.concat(q('a', 'IMC / VMC', ['IMC', 'VMC'], radio('wx-imcvmc')));
    content.push(qtext('b', 'Above / below clouds / fog / haze or between layers', txt('wx-cloudrel')));
    content.push(qtext('c', 'Distance vertically from cloud', (txt('wx-cloudbelow') ? txt('wx-cloudbelow') + ' below' : '') + (txt('wx-cloudabove') ? (txt('wx-cloudbelow') ? '   ' : '') + txt('wx-cloudabove') + ' above' : '')));
    content = content.concat(q('d', 'In cloud / rain / snow / sleet / fog / haze', ['In cloud', 'Rain', 'Snow', 'Sleet', 'Fog', 'Haze'], checks('wx-in')));
    content = content.concat(q('e', 'Flying into / out of sun', ['Flying into sun', 'Flying out of sun', 'N/A'], radio('wx-sun')));
    content.push(qtext('f', 'Flight visibility', txt('wx-vis')));

    content.push({ text: '6.  Any other information considered important by the pilot-in-command', bold: true, fontSize: 9.5, margin: [0, 6, 0, 2] });
    content.push({ text: txt('other') || ' ', fontSize: 9, margin: [4, 0, 0, 4] });

    // D
    content.push(sectionHeader('D — MISCELLANEOUS'));
    content.push({ text: '1.  Information regarding reporting aircraft', bold: true, fontSize: 9.5, margin: [0, 2, 0, 2] });
    content.push(qtext('a', 'Aircraft registration', txt('d-reg')));
    content.push(qtext('b', 'Aircraft type', txt('d-type')));
    content.push(qtext('c', 'Operator', txt('d-operator')));
    content.push(qtext('d', 'Aerodrome of departure', txt('d-adep')));
    content.push(qtext('e', 'Aerodrome of first landing / destination', (txt('d-firstland') + (txt('d-dest') ? '  /  ' + txt('d-dest') : '')).replace(/^ +\/ +/, '')));
    content.push(qtext('f', 'Reported by radio or other means to (name of VATPHIL unit) at time UTC', (txt('d-reportedto') + (txt('d-reportedtime') ? '  at  ' + txt('d-reportedtime') : ''))));
    content.push(qtext('g', 'Date / time / place of completion of form', txt('d-completion')));
    content.push({ text: '2.  Function, address and signature of person submitting report', bold: true, fontSize: 9.5, margin: [0, 6, 0, 2] });
    content.push(qtext('a', 'Function', txt('d-function')));
    content.push(qtext('b', 'Address', txt('d-address')));
    content.push(qtext('c', 'Signature', txt('d-signature')));
    content.push(qtext('d', 'Telephone number', txt('d-phone')));

    // E
    content.push(sectionHeader('E — SUPPLEMENTARY INFORMATION BY VATPHIL UNIT CONCERNED'));
    content.push({ text: '1.  Receipt of report', bold: true, fontSize: 9.5, margin: [0, 2, 0, 2] });
    content = content.concat(q('a', 'Report received via' + (txt('e-viaother') ? ' — ' + txt('e-viaother') : ''), ['AFTN', 'radio', 'telephone', 'other'], radio('e-via'), 4));
    content.push(qtext('b', 'Report received by (name of VATPHIL unit)', txt('e-recvby')));
    content.push({ text: '2.  Details of VATPHIL action', bold: true, fontSize: 9.5, margin: [0, 6, 0, 2] });
    content.push({ text: 'Clearance, incident seen (radar/visually), warning given, result of local enquiry, etc.', italics: true, fontSize: 8, margin: [0, 0, 0, 2] });
    content.push({ text: txt('e-action') || ' ', fontSize: 9, margin: [4, 0, 0, 4] });

    // Diagrams
    content.push({ text: 'DIAGRAMS OF AIRPROX', bold: true, fontSize: 11, alignment: 'center', margin: [0, 10, 0, 2] });
    content.push({ text: 'Mark passage of other aircraft relative to you, in plan on the left and in elevation on the right, assuming YOU are at the centre of each diagram. Include first sighting and passing distance.', fontSize: 8.5, margin: [0, 0, 0, 6] });
    content.push({ columns: [diagram('VIEW FROM ABOVE', true, null, PLOT.above), { width: 20, text: '' }, diagram('VIEW FROM ASTERN', false, 'Vertical: hundreds of feet / metres', PLOT.astern)] });

    content.push({ text: '* Delete as appropriate', fontSize: 8, italics: true, margin: [0, 10, 0, 0] });

    return {
      pageSize: 'A4', pageMargins: [32, 30, 32, 30],
      content: content,
      styles: { title: { fontSize: 13, bold: true } },
      defaultStyle: { fontSize: 9, lineHeight: 1.05 }
    };
  }

  function fileName() {
    var cs = (txt('acid') || 'report').replace(/[^A-Za-z0-9]/g, '');
    var d = new Date().toISOString().slice(0, 10);
    return 'ATS-Incident-Report-' + cs + '-' + d + '.pdf';
  }

  function generate(then) {
    statusMsg('Building PDF…');
    ensurePdf().then(function () {
      var pdf = pdfMake.createPdf(buildDoc());
      if (then) then(pdf); else { pdf.download(fileName()); statusMsg('PDF downloaded.', 'ok'); }
    }).catch(function (e) {
      console.error(e); statusMsg('Could not build the PDF (failed to load the PDF library). Check your connection and try again.', 'err');
    });
  }

  function emailSummary() {
    var L = [];
    L.push('AIR TRAFFIC INCIDENT REPORT (VATSIM / flight-sim use only)');
    L.push('');
    L.push('Aircraft identification: ' + (txt('acid') || '-'));
    L.push('Type of incident: ' + (radio('inctype') || '-'));
    L.push('Date/time (UTC): ' + (txt('datetime') || '-'));
    L.push('Position: ' + (txt('position') || '-'));
    L.push('Reporter: ' + (txt('d-signature') || '-') + '  (' + (txt('d-function') || '-') + ')');
    L.push('');
    L.push('The full report is in the attached PDF (' + fileName() + ').');
    L.push('Please attach the PDF that was just downloaded before sending.');
    return L.join('\n');
  }

  // ---- interactive AIRPROX plotting (on-screen canvases) ----
  function cvGrid(ctx, W, H, plan) {
    ctx.clearRect(0, 0, W, H);
    var cols = 28, rows = 20, cw = W / cols, ch = H / rows, i, j;
    ctx.strokeStyle = '#bcbcbc';
    for (i = 0; i <= cols; i++) { ctx.lineWidth = i % 2 ? 0.4 : 0.7; ctx.beginPath(); ctx.moveTo(i * cw, 0); ctx.lineTo(i * cw, H); ctx.stroke(); }
    for (j = 0; j <= rows; j++) { ctx.lineWidth = j % 2 ? 0.4 : 0.7; ctx.beginPath(); ctx.moveTo(0, j * ch); ctx.lineTo(W, j * ch); ctx.stroke(); }
    var cx = W / 2, cy = H / 2; ctx.strokeStyle = '#111'; ctx.fillStyle = '#111'; ctx.lineWidth = 2.4;
    if (plan) { ctx.beginPath(); ctx.moveTo(cx, cy - 22); ctx.lineTo(cx, cy + 17); ctx.moveTo(cx - 21, cy - 1); ctx.lineTo(cx + 21, cy - 1); ctx.moveTo(cx - 8, cy + 16); ctx.lineTo(cx + 8, cy + 16); ctx.stroke(); }
    else { ctx.beginPath(); ctx.moveTo(cx - 22, cy); ctx.lineTo(cx + 22, cy); ctx.moveTo(cx, cy); ctx.lineTo(cx, cy - 17); ctx.stroke(); ctx.beginPath(); ctx.arc(cx, cy, 4, 0, 7); ctx.fill(); }
  }
  function cvRedraw(which) {
    var cv = document.getElementById(which === 'above' ? 'ir-cv-above' : 'ir-cv-astern');
    if (!cv) return;
    var ctx = cv.getContext('2d'), W = cv.width, H = cv.height, pts = PLOT[which];
    cvGrid(ctx, W, H, which === 'above');
    if (!pts.length) return;
    ctx.strokeStyle = MARK; ctx.fillStyle = MARK; ctx.lineWidth = 2;
    if (pts.length >= 2) { ctx.beginPath(); pts.forEach(function (p, i) { var x = p.x * W, y = p.y * H; if (i) ctx.lineTo(x, y); else ctx.moveTo(x, y); }); ctx.stroke(); }
    ctx.lineWidth = 2; ctx.beginPath(); ctx.arc(pts[0].x * W, pts[0].y * H, 5, 0, 7); ctx.stroke();     // first sighting
    pts.forEach(function (p) { ctx.beginPath(); ctx.arc(p.x * W, p.y * H, 2.4, 0, 7); ctx.fill(); });
    if (pts.length >= 2) {
      var a = pts[pts.length - 2], b = pts[pts.length - 1], ax = a.x * W, ay = a.y * H, bx = b.x * W, by = b.y * H;
      var ang = Math.atan2(by - ay, bx - ax), L = 9;
      ctx.beginPath(); ctx.moveTo(bx, by); ctx.lineTo(bx - L * Math.cos(ang - 0.5), by - L * Math.sin(ang - 0.5));
      ctx.moveTo(bx, by); ctx.lineTo(bx - L * Math.cos(ang + 0.5), by - L * Math.sin(ang + 0.5)); ctx.stroke();
    }
  }
  ['above', 'astern'].forEach(function (which) {
    var cv = document.getElementById(which === 'above' ? 'ir-cv-above' : 'ir-cv-astern');
    if (!cv) return;
    cvRedraw(which);
    cv.addEventListener('pointerdown', function (ev) {
      ev.preventDefault();
      var r = cv.getBoundingClientRect();
      var x = Math.max(0, Math.min(1, (ev.clientX - r.left) / r.width));
      var y = Math.max(0, Math.min(1, (ev.clientY - r.top) / r.height));
      PLOT[which].push({ x: x, y: y }); cvRedraw(which);
    });
  });
  document.querySelectorAll('.ir-diag-btns button').forEach(function (b) {
    b.addEventListener('click', function () {
      var u = b.getAttribute('data-undo'), c = b.getAttribute('data-clear');
      if (u) { PLOT[u].pop(); cvRedraw(u); }
      else if (c) { PLOT[c] = []; cvRedraw(c); }
    });
  });

  document.getElementById('ir-gen').addEventListener('click', function () { generate(null); });
  document.getElementById('ir-reset').addEventListener('click', function () {
    document.getElementById('ir-form').reset();
    PLOT.above = []; PLOT.astern = []; cvRedraw('above'); cvRedraw('astern');
    statusMsg('Form cleared.');
  });
  function fld(name, value) { return { name: name, value: (value && value.length) ? value.slice(0, 1024) : '—', inline: true }; }
  function webhookPayload() {
    return {
      username: 'Incident Reports',
      content: 'New air traffic incident report' + (txt('acid') ? ' — **' + txt('acid') + '**' : ''),
      embeds: [{
        title: 'Air Traffic Incident Report',
        color: 0x8c7804,
        fields: [
          fld('Aircraft', txt('acid')),
          fld('Type of incident', radio('inctype')),
          fld('Date / time (UTC)', txt('datetime')),
          { name: 'Position', value: (txt('position') || '—').slice(0, 1024), inline: false },
          { name: 'Reporter', value: ((txt('d-signature') || '—') + (txt('d-function') ? ' (' + txt('d-function') + ')' : '') + (txt('d-cid') ? '\nCID: ' + txt('d-cid') : '')).slice(0, 1024), inline: false }
        ]
      }]
    };
  }

  document.getElementById('ir-send').addEventListener('click', function () {
    if (WEBHOOK_URL) {
      statusMsg('Sending to staff…');
      generate(function (pdf) {
        pdf.getBlob(function (blob) {
          var fd = new FormData();
          fd.append('payload_json', JSON.stringify(webhookPayload()));
          fd.append('files[0]', new File([blob], fileName(), { type: 'application/pdf' }));
          fetch(WEBHOOK_URL, { method: 'POST', body: fd })
            .then(function (r) { if (!r.ok) throw new Error('HTTP ' + r.status); statusMsg('Report sent to the staff Discord channel.', 'ok'); })
            .catch(function (e) {
              console.error(e);
              statusMsg('Could not reach the Discord webhook. The PDF was downloaded — please send it to staff manually.', 'err');
              pdf.download(fileName());
            });
        });
      });
    } else {
      // no webhook configured: download the PDF and open an email draft to attach it
      generate(function (pdf) {
        pdf.download(fileName());
        var subj = encodeURIComponent('ATS Incident Report — ' + (txt('acid') || 'unknown'));
        var body = encodeURIComponent(emailSummary());
        statusMsg('PDF downloaded. Your email draft opened — attach the PDF and send.', 'ok');
        setTimeout(function () { window.location.href = 'mailto:' + STAFF_EMAIL + '?subject=' + subj + '&body=' + body; }, 400);
      });
    }
  });
})();
</script>
