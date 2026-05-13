# TopSky Tag Reference

This page hopefully teaches you what you will see as an Approach and ACC Controller

---
Hover over an item if you are not familiar with what they do.

<style>
  .tag-container {
    display: inline-block;
    position: relative;
    line-height: 0;
    margin: 20px 16px 20px 0;
    vertical-align: top;
  }
  .tag-container img { display: block; image-rendering: pixelated; }

  .hotspot {
    position: absolute;
    cursor: crosshair;
    border: 1px solid transparent;
    border-radius: 2px;
    transition: border-color 0.1s, background 0.1s;
    z-index: 10;
  }
  .hotspot:hover {
    border-color: rgba(255, 167, 38, 0.75);
    background: rgba(255, 167, 38, 0.15);
  }

  .tag-label {
    display: block;
    font-family: var(--md-text-font-family, Roboto, sans-serif);
    font-size: 11px;
    color: var(--md-default-fg-color--light, #78909c);
    text-align: center;
    margin-top: 6px;
    line-height: normal;
  }

  /*
   * position:fixed + clientX/clientY keeps the tooltip pinned to the
   * viewport regardless of MkDocs Material's inner scrolling article.
   * The tooltip is moved to <body> via JS so no transformed ancestor
   * can hijack the fixed stacking context.
   */
  #hs-tt {
    display: none;
    position: fixed;
    z-index: 9999;
    background: var(--md-default-bg-color, #fff);
    border: 1px solid var(--md-default-fg-color--lightest, #e0e0e0);
    border-left: 3px solid #f57f17;
    border-radius: 4px;
    padding: 11px 14px;
    min-width: 210px;
    max-width: 280px;
    box-shadow: 0 4px 16px rgba(0,0,0,0.12);
    font-family: var(--md-text-font-family, Roboto, sans-serif);
    font-size: 14px;
    color: var(--md-default-fg-color, #37474f);
    pointer-events: none;
    line-height: 1.5;
  }
  #hs-tt.show { display: block; }

  .tt-title {
    font-weight: 700;
    font-size: 13px;
    letter-spacing: 0.8px;
    color: var(--md-default-fg-color, #263238);
    text-transform: uppercase;
    margin-bottom: 6px;
    padding-bottom: 6px;
    border-bottom: 1px solid var(--md-default-fg-color--lightest, #eceff1);
  }
  .tt-desc {
    margin-bottom: 8px;
    font-size: 13px;
    color: var(--md-default-fg-color--light, #607d8b);
  }
  .tt-desc:empty { display: none; }
  .tt-actions { border-top: 1px solid var(--md-default-fg-color--lightest, #eceff1); padding-top: 6px; }
  .tt-actions:empty { display: none; border: none; padding: 0; }
  .tt-action { display: flex; gap: 8px; margin-bottom: 3px; font-size: 13px; align-items: baseline; }
  .tt-key {
    font-family: var(--md-code-font-family, 'Roboto Mono', monospace);
    font-size: 12px;
    font-weight: 500;
    color: #e65100;
    min-width: 82px;
    flex-shrink: 0;
  }
  .tt-val { color: var(--md-default-fg-color--light, #78909c); }
</style>

<div id="hs-tt">
  <div class="tt-title" id="hs-tt-title"></div>
  <div class="tt-desc"  id="hs-tt-desc"></div>
  <div class="tt-actions" id="hs-tt-acts"></div>
</div>

<div class="tag-container">
  <img src="/assets/img/Tagged.png" width="244" alt="" />
  <div class="hotspot" style="left:55px;top:82px;width:25px;height:106px"
       data-title="Track"
       data-desc="Shows the direction of the aircraft"></div>
  <div class="hotspot" style="left:97px;top:52px;width:87px;height:21px"
       data-title="Callsign"
       data-l="to open Flight plan"
       data-r="to open Callsign Menu"></div>
  <div class="hotspot" style="left:100px;top:74px;width:40px;height:20px"
       data-title="Current Altitude"
       data-desc="Indicated Altitude"
       data-r="to select altitude"></div>
  <div class="hotspot" style="left:144px;top:73px;width:48px;height:21px"
       data-title="Assigned Altitude"
       data-l="to aircraft waypoints"
       data-r="to select altitude"></div>
  <div class="hotspot" style="left:100px;top:31px;width:54px;height:21px"
       data-title="CLAM / RAM"
       data-desc="Form of warning system. Can be CLAM or RAM."
       data-l="to open SSR"
       data-r="to open SSR"></div>
  <span class="tag-label">Tag (Normal)</span>
</div>

<div class="tag-container">
  <img src="/assets/img/Hover.png" width="195" alt="" />
  <div class="hotspot" style="left:0px;top:23px;width:48px;height:22px"
       data-title="Scratch Pad"
       data-desc="Add anything related to the aircraft here eg, &quot;/VOR&quot; best to add a &quot;/&quot; to prevent errors"
       data-l="Open scratch pad"></div>
  <div class="hotspot" style="left:96px;top:45px;width:88px;height:21px"
       data-title="Aircraft / Wake"
       data-r="toggle track"></div>
  <div class="hotspot" style="left:108px;top:66px;width:65px;height:21px"
       data-title="Assigned Heading"
       data-desc="Magnetic Heading"
       data-l="and drag to give a heading"
       data-r="open heading menu"></div>
  <div class="hotspot" style="left:2px;top:88px;width:57px;height:20px"
       data-title="Speed"
       data-desc="Shows either &quot;N000&quot; for knots or &quot;M.00&quot; for Mach"
       data-r="to open speed menu"></div>
  <div class="hotspot" style="left:70px;top:89px;width:61px;height:19px"
       data-title="True Heading"
       data-desc="Similar to the Assigned Heading but, is what the aircraft is truly on (not magnetic)"
       data-l="open heading menu"
       data-r="open heading menu"></div>
  <span class="tag-label">Tag (When Hovering)</span>
</div>

<script>
(function () {
  var tt    = document.getElementById('hs-tt');
  var title = document.getElementById('hs-tt-title');
  var desc  = document.getElementById('hs-tt-desc');
  var acts  = document.getElementById('hs-tt-acts');

  /* Append tooltip to <body> so absolute positioning is
     relative to the document, not a scrolled ancestor. */
  document.body.appendChild(tt);

  document.querySelectorAll('.hotspot').forEach(function (el) {

    el.addEventListener('mouseenter', function () {
      title.textContent = el.dataset.title || '';
      desc.textContent  = el.dataset.desc  || '';

      var h = '';
      if (el.dataset.l) h += '<div class="tt-action"><span class="tt-key">Left click</span><span class="tt-val">'  + el.dataset.l + '</span></div>';
      if (el.dataset.r) h += '<div class="tt-action"><span class="tt-key">Right click</span><span class="tt-val">' + el.dataset.r + '</span></div>';
      acts.innerHTML = h;

      tt.classList.add('show');
    });

    el.addEventListener('mousemove', function (e) {
      /*
       * clientX/clientY = viewport-relative. Correct for position:fixed.
       * pageX/pageY would be wrong here because it includes document scroll
       * but fixed elements are positioned against the viewport, not the page.
       */
      var x = e.clientX + 16;
      var y = e.clientY + 16;

      /* Keep tooltip inside viewport horizontally */
      if (e.clientX + 296 > window.innerWidth)  x = e.clientX - 296;
      /* Keep tooltip inside viewport vertically */
      if (e.clientY + 160 > window.innerHeight) y = e.clientY - 140;

      tt.style.left = x + 'px';
      tt.style.top  = y + 'px';
    });

    el.addEventListener('mouseleave', function () {
      tt.classList.remove('show');
    });
  });
}());
</script>

