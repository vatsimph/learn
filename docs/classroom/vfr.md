# Visual Flight Rules (VFR)

Is a set of regulations under which a pilot operates an aircraft in generally clear weather conditions that allows the pilot to maintain visual contact to his/her surroundings. While there are minimum daylight, visibility, and cloud distance requirements in the real world, as the weather can be changed in the sim, said minimum criteria for VFR flights are relaxed in the VATSIM Network. However this does not reduce the responsibilities of the pilot-in-command. The pilot-in-command still must be able to see outside the cockpit to control the aircraft's altitude, navigate and find visual reference points, avoid obstacles and other aircraft.

## Topographic Map

The Philippine 1:250,000 topographic index below is a useful VFR reference for visual navigation. Hover over a sheet to see its number and area, and click it to open the full topographic chart (opens on the NAMRIA website).

<style>
  #topo-tt {
    display:none; position:fixed; z-index:9999;
    background:var(--md-default-bg-color); border:1px solid var(--md-default-fg-color--lightest);
    border-left:3px solid #f57f17; border-radius:4px; padding:9px 13px;
    min-width:150px; max-width:260px; box-shadow:0 4px 16px rgba(0,0,0,.15);
    font-family:var(--md-text-font-family, Roboto, sans-serif); font-size:14px;
    color:var(--md-default-fg-color); pointer-events:none; line-height:1.5;
  }
  #topo-tt.show { display:block; }
  #topo-tt .tt-title { font-weight:700; font-size:12px; letter-spacing:.6px; text-transform:uppercase; color:var(--md-default-fg-color); margin-bottom:4px; }
  #topo-tt .tt-desc { font-size:13px; color:var(--md-default-fg-color--light); }
  #topo-tt .tt-desc:empty { display:none; }

  .topo-container { display:block; position:relative; line-height:0; max-width:500px; margin:1rem auto; }
  .topo-container img { display:block; width:100%; height:auto; border:1px solid var(--md-default-fg-color--lightest); border-radius:6px; }
  .topo-hotspot {
    position:absolute; cursor:pointer; border:1px solid transparent; border-radius:2px;
    transition:border-color .1s, background .1s; z-index:10;
  }
  .topo-hotspot:hover { border-color:rgba(255,167,38,.85); background:rgba(255,167,38,.18); }
</style>

<div id="topo-tt"><div class="tt-title"></div><div class="tt-desc"></div></div>

<div class="topo-container">
<img src="https://www.namria.gov.ph/Images/indxTopoMap250.png" alt="Philippine Topographic Index Map — Scale 1:250,000">
  <a class="topo-hotspot" style="left:49.0%;top:1.366%;width:11.0%;height:5.766%" href="https://www.namria.gov.ph/Downloads/topoMap250/2501%20Batan.jpg" target="_blank" rel="noopener" data-title="Batan Island" data-desc="Sheet 2501"></a>
  <a class="topo-hotspot" style="left:48.8%;top:6.829%;width:11.2%;height:5.918%" href="https://www.namria.gov.ph/Downloads/topoMap250/2502%20Calayan%20Island.jpg" target="_blank" rel="noopener" data-title="Calayan Island" data-desc="Sheet 2502"></a>
  <a class="topo-hotspot" style="left:41.2%;top:12.747%;width:11.2%;height:5.766%" href="https://www.namria.gov.ph/Downloads/topoMap250/2503%20Laoag%20City.jpg" target="_blank" rel="noopener" data-title="Laoag" data-desc="Sheet 2503"></a>
  <a class="topo-hotspot" style="left:52.4%;top:12.443%;width:11.4%;height:6.222%" href="https://www.namria.gov.ph/Downloads/topoMap250/2504%20Aparri.jpg" target="_blank" rel="noopener" data-title="Aparri" data-desc="Sheet 2504"></a>
  <a class="topo-hotspot" style="left:40.8%;top:18.513%;width:11.6%;height:5.766%" href="https://www.namria.gov.ph/Downloads/topoMap250/2505%20Bontoc.jpg" target="_blank" rel="noopener" data-title="Bontoc" data-desc="Sheet 2505"></a>
  <a class="topo-hotspot" style="left:52.4%;top:18.209%;width:11.2%;height:6.222%" href="https://www.namria.gov.ph/Downloads/topoMap250/2506%20City%20of%20Ilagan.jpg" target="_blank" rel="noopener" data-title="Ilagan" data-desc="Sheet 2506"></a>
  <a class="topo-hotspot" style="left:37.2%;top:24.127%;width:11.2%;height:5.766%" href="https://www.namria.gov.ph/Downloads/topoMap250/2507%20Dagupan%20City.jpg" target="_blank" rel="noopener" data-title="Dagupan City" data-desc="Sheet 2507"></a>
  <a class="topo-hotspot" style="left:48.6%;top:24.127%;width:11.6%;height:5.766%" href="https://www.namria.gov.ph/Downloads/topoMap250/2508%20Solano.jpg" target="_blank" rel="noopener" data-title="Solano" data-desc="Sheet 2508"></a>
  <a class="topo-hotspot" style="left:37.0%;top:29.894%;width:11.0%;height:5.766%" href="https://www.namria.gov.ph/Downloads/topoMap250/2509%20Tarlac.jpg" target="_blank" rel="noopener" data-title="Tarlac" data-desc="Sheet 2509"></a>
  <a class="topo-hotspot" style="left:48.2%;top:29.894%;width:11.8%;height:5.918%" href="https://www.namria.gov.ph/Downloads/topoMap250/2510%20Laur.jpg" target="_blank" rel="noopener" data-title="Laur" data-desc="Sheet 2510"></a>
  <a class="topo-hotspot" style="left:40.6%;top:35.508%;width:11.8%;height:6.222%" href="https://www.namria.gov.ph/Downloads/topoMap250/2511%20City%20of%20Manila.jpg" target="_blank" rel="noopener" data-title="Manila" data-desc="Sheet 2511"></a>
  <a class="topo-hotspot" style="left:52.0%;top:35.508%;width:11.6%;height:6.222%" href="https://www.namria.gov.ph/Downloads/topoMap250/2512%20Daet.jpg" target="_blank" rel="noopener" data-title="Daet" data-desc="Sheet 2512"></a>
  <a class="topo-hotspot" style="left:63.6%;top:35.66%;width:12.0%;height:6.07%" href="https://www.namria.gov.ph/Downloads/topoMap250/2513%20Pandan.jpg" target="_blank" rel="noopener" data-title="Pandan" data-desc="Sheet 2513"></a>
  <a class="topo-hotspot" style="left:40.8%;top:41.73%;width:11.8%;height:5.615%" href="https://www.namria.gov.ph/Downloads/topoMap250/2514%20Batangas%20City.jpg" target="_blank" rel="noopener" data-title="Batangas" data-desc="Sheet 2514"></a>
  <a class="topo-hotspot" style="left:52.2%;top:41.426%;width:11.8%;height:5.918%" href="https://www.namria.gov.ph/Downloads/topoMap250/2515%20Lucena.jpg" target="_blank" rel="noopener" data-title="Lucena City" data-desc="Sheet 2515"></a>
  <a class="topo-hotspot" style="left:63.8%;top:41.73%;width:12.0%;height:5.463%" href="https://www.namria.gov.ph/Downloads/topoMap250/2516%20City%20of%20Legazpi.jpg" target="_blank" rel="noopener" data-title="Legaspi City" data-desc="Sheet 2515"></a>
  <a class="topo-hotspot" style="left:38.4%;top:47.193%;width:12.0%;height:5.766%" href="https://www.namria.gov.ph/Downloads/topoMap250/2517%20San%20Jose.jpg" target="_blank" rel="noopener" data-title="San Jose" data-desc="Sheet 2517"></a>
  <a class="topo-hotspot" style="left:50.2%;top:47.193%;width:12.0%;height:5.766%" href="https://www.namria.gov.ph/Downloads/topoMap250/2518%20Romblon.jpg" target="_blank" rel="noopener" data-title="Romblon" data-desc="Sheet 2518"></a>
  <a class="topo-hotspot" style="left:62.0%;top:47.041%;width:11.6%;height:6.07%" href="https://www.namria.gov.ph/Downloads/topoMap250/2519%20Bulan.jpg" target="_blank" rel="noopener" data-title="Bulan" data-desc="Sheet 2519"></a>
  <a class="topo-hotspot" style="left:73.4%;top:47.041%;width:11.6%;height:5.766%" href="https://www.namria.gov.ph/Downloads/topoMap250/2520%20City%20of%20Calbayog.jpg" target="_blank" rel="noopener" data-title="Calbayog" data-desc="Sheet 2520"></a>
  <a class="topo-hotspot" style="left:28.6%;top:52.656%;width:12.0%;height:6.07%" href="https://www.namria.gov.ph/Downloads/topoMap250/2521%20El%20Nido.jpg" target="_blank" rel="noopener" data-title="El Nido" data-desc="Sheet 2521"></a>
  <a class="topo-hotspot" style="left:40.4%;top:52.656%;width:12.2%;height:6.222%" href="https://www.namria.gov.ph/Downloads/topoMap250/2522%20Coron%20Island.jpg" target="_blank" rel="noopener" data-title="Coron Island" data-desc="Sheet 2522"></a>
  <a class="topo-hotspot" style="left:52.2%;top:52.807%;width:11.6%;height:5.918%" href="https://www.namria.gov.ph/Downloads/topoMap250/2523%20City%20of%20Roxas.jpg" target="_blank" rel="noopener" data-title="Roxas City" data-desc="Sheet 2523"></a>
  <a class="topo-hotspot" style="left:63.6%;top:52.959%;width:12.0%;height:5.918%" href="https://www.namria.gov.ph/Downloads/topoMap250/2524%20Bogo.jpg" target="_blank" rel="noopener" data-title="Bogo" data-desc="Sheet 2524"></a>
  <a class="topo-hotspot" style="left:75.2%;top:52.807%;width:12.0%;height:5.918%" href="https://www.namria.gov.ph/Downloads/topoMap250/2525%20Ormoc%20City.jpg" target="_blank" rel="noopener" data-title="Ormoc City" data-desc="Sheet 2525"></a>
  <a class="topo-hotspot" style="left:29.8%;top:58.574%;width:11.8%;height:5.918%" href="https://www.namria.gov.ph/Downloads/topoMap250/2526%20Taytay.jpg" target="_blank" rel="noopener" data-title="Taytay" data-desc="Sheet 2526"></a>
  <a class="topo-hotspot" style="left:41.2%;top:58.725%;width:12.4%;height:5.766%" href="https://www.namria.gov.ph/Downloads/topoMap250/2527%20Cuyo.jpg" target="_blank" rel="noopener" data-title="Cuyo" data-desc="Sheet 2527"></a>
  <a class="topo-hotspot" style="left:53.4%;top:58.574%;width:11.6%;height:5.918%" href="https://www.namria.gov.ph/Downloads/topoMap250/2528%20Iloilo.jpg" target="_blank" rel="noopener" data-title="Iloilo City" data-desc="Sheet 2528"></a>
  <a class="topo-hotspot" style="left:64.8%;top:58.725%;width:12.0%;height:5.918%" href="https://www.namria.gov.ph/Downloads/topoMap250/2529%20Cebu%20City.jpg" target="_blank" rel="noopener" data-title="Cebu City" data-desc="Sheet 2529"></a>
  <a class="topo-hotspot" style="left:76.8%;top:58.574%;width:11.6%;height:5.766%" href="https://www.namria.gov.ph/Downloads/topoMap250/2530%20City%20of%20Baybay.jpg" target="_blank" rel="noopener" data-title="Baybay" data-desc="Sheet 2530"></a>
  <a class="topo-hotspot" style="left:20.4%;top:64.036%;width:12.6%;height:6.222%" href="https://www.namria.gov.ph/Downloads/topoMap250/2531%20City%20of%20Puerto%20Princesa.jpg" target="_blank" rel="noopener" data-title="Puerto Princesa" data-desc="Sheet 2531"></a>
  <a class="topo-hotspot" style="left:44.6%;top:64.34%;width:11.2%;height:5.918%" href="https://www.namria.gov.ph/Downloads/topoMap250/2532%20Cagayan%20Island.jpg" target="_blank" rel="noopener" data-title="Cagayan Island" data-desc="Sheet 2532"></a>
  <a class="topo-hotspot" style="left:55.8%;top:64.492%;width:11.6%;height:5.766%" href="https://www.namria.gov.ph/Downloads/topoMap250/2533%20City%20of%20Dumaguete.jpg" target="_blank" rel="noopener" data-title="Dumaguete City" data-desc="Sheet 2533"></a>
  <a class="topo-hotspot" style="left:67.6%;top:64.34%;width:12.0%;height:5.918%" href="https://www.namria.gov.ph/Downloads/topoMap250/2534%20City%20of%20Tagbilaran.jpg" target="_blank" rel="noopener" data-title="City of Tagbilaran" data-desc="Sheet 2534"></a>
  <a class="topo-hotspot" style="left:79.4%;top:64.188%;width:11.8%;height:5.918%" href="https://www.namria.gov.ph/Downloads/topoMap250/2535%20Surigao%20City.jpg" target="_blank" rel="noopener" data-title="Surigao" data-desc="Sheet 2535"></a>
  <a class="topo-hotspot" style="left:15.2%;top:69.803%;width:12.2%;height:5.918%" href="https://www.namria.gov.ph/Downloads/topoMap250/2536%20Brookes%20Point.jpg" target="_blank" rel="noopener" data-title="Brookes Point" data-desc="Sheet 2536"></a>
  <a class="topo-hotspot" style="left:32.4%;top:68.134%;width:11.8%;height:5.918%" href="https://www.namria.gov.ph/Downloads/topoMap250/2537%20Tubbataha%20Reefs.jpg" target="_blank" rel="noopener" data-title="Tubbataha Reefs" data-desc="Sheet 2537"></a>
  <a class="topo-hotspot" style="left:56.0%;top:69.954%;width:11.8%;height:5.615%" href="https://www.namria.gov.ph/Downloads/topoMap250/2538%20Dipolog%20City.jpg" target="_blank" rel="noopener" data-title="Dipolog" data-desc="Sheet 2538"></a>
  <a class="topo-hotspot" style="left:67.6%;top:69.954%;width:11.8%;height:5.615%" href="https://www.namria.gov.ph/Downloads/topoMap250/2539%20Cagayan%20De%20Oro%20City.jpg" target="_blank" rel="noopener" data-title="Cagayan de Oro City" data-desc="Sheet 2539"></a>
  <a class="topo-hotspot" style="left:79.4%;top:70.106%;width:11.8%;height:5.463%" href="https://www.namria.gov.ph/Downloads/topoMap250/2540%20Butuan%20City.jpg" target="_blank" rel="noopener" data-title="Butuan City" data-desc="Sheet 2540"></a>
  <a class="topo-hotspot" style="left:12.8%;top:75.569%;width:11.6%;height:5.918%" href="https://www.namria.gov.ph/Downloads/topoMap250/2541%20Balabac%20Island.jpg" target="_blank" rel="noopener" data-title="Balabac Islangd" data-desc="Sheet 2541"></a>
  <a class="topo-hotspot" style="left:24.2%;top:75.721%;width:12.2%;height:5.766%" href="https://www.namria.gov.ph/Downloads/topoMap250/2542%20Cagayan%20de%20Tawi-Tawi%20Island.jpg" target="_blank" rel="noopener" data-title="Cagayan Sulu Island" data-desc="Sheet 2542"></a>
  <a class="topo-hotspot" style="left:52.0%;top:75.721%;width:12.2%;height:5.918%" href="https://www.namria.gov.ph/Downloads/topoMap250/2543%20Kabasalan.jpg" target="_blank" rel="noopener" data-title="Kabasalan" data-desc="Sheet 2543"></a>
  <a class="topo-hotspot" style="left:63.8%;top:75.569%;width:12.4%;height:6.07%" href="https://www.namria.gov.ph/Downloads/topoMap250/2544%20Cotabato%20City.jpg" target="_blank" rel="noopener" data-title="Cotabato City" data-desc="Sheet 2544"></a>
  <a class="topo-hotspot" style="left:75.6%;top:75.569%;width:12.0%;height:6.07%" href="https://www.namria.gov.ph/Downloads/topoMap250/2545%20Davao%20City.jpg" target="_blank" rel="noopener" data-title="Davao City" data-desc="Sheet 2545"></a>
  <a class="topo-hotspot" style="left:87.4%;top:75.417%;width:11.6%;height:6.222%" href="https://www.namria.gov.ph/Downloads/topoMap250/2546%20Caraga.jpg" target="_blank" rel="noopener" data-title="Caraga" data-desc="Sheet 2546"></a>
  <a class="topo-hotspot" style="left:24.2%;top:81.184%;width:12.2%;height:6.07%" href="https://www.namria.gov.ph/Downloads/topoMap250/2547%20Turtle%20Islands.jpg" target="_blank" rel="noopener" data-title="Turtle Islands" data-desc="Sheet 2547"></a>
  <a class="topo-hotspot" style="left:40.0%;top:81.487%;width:12.2%;height:5.918%" href="https://www.namria.gov.ph/Downloads/topoMap250/2548%20Jolo.jpg" target="_blank" rel="noopener" data-title="Jolo" data-desc="Sheet 2548"></a>
  <a class="topo-hotspot" style="left:52.0%;top:81.487%;width:12.0%;height:6.222%" href="https://www.namria.gov.ph/Downloads/topoMap250/2549%20Zamboanga%20City.jpg" target="_blank" rel="noopener" data-title="Zamboanga City" data-desc="Sheet 2549"></a>
  <a class="topo-hotspot" style="left:67.4%;top:81.487%;width:12.4%;height:5.918%" href="https://www.namria.gov.ph/Downloads/topoMap250/2550%20City%20of%20Koronadal.jpg" target="_blank" rel="noopener" data-title="City of Koronadal" data-desc="Sheet 2550"></a>
  <a class="topo-hotspot" style="left:79.6%;top:81.487%;width:12.0%;height:5.918%" href="https://www.namria.gov.ph/Downloads/topoMap250/2551%20City%20of%20Digos.jpg" target="_blank" rel="noopener" data-title="Digos" data-desc="Sheet 2551"></a>
  <a class="topo-hotspot" style="left:28.0%;top:87.253%;width:12.4%;height:5.766%" href="https://www.namria.gov.ph/Downloads/topoMap250/2552%20Tawi-Tawi%20Islands.jpg" target="_blank" rel="noopener" data-title="Tawi-Tawi" data-desc="Sheet 2552"></a>
  <a class="topo-hotspot" style="left:40.2%;top:87.253%;width:12.0%;height:6.373%" href="https://www.namria.gov.ph/Downloads/topoMap250/2553%20Maimbung.jpg" target="_blank" rel="noopener" data-title="Maimbung" data-desc="Sheet 2553"></a>
  <a class="topo-hotspot" style="left:75.4%;top:87.253%;width:12.2%;height:6.07%" href="https://www.namria.gov.ph/Downloads/topoMap250/2554%20Jose%20Abad%20Santos.jpg" target="_blank" rel="noopener" data-title="Jose Abad Santos" data-desc="Sheet 2554"></a>
  <a class="topo-hotspot" style="left:28.0%;top:92.868%;width:12.0%;height:5.766%" href="https://www.namria.gov.ph/Downloads/topoMap250/2555%20Sibutu%20Island.jpg" target="_blank" rel="noopener" data-title="Sibutu Island" data-desc="Sheet 2555"></a>
</div>

[Open the topographic index on NAMRIA](https://www.namria.gov.ph/topo250Index.aspx){ .md-button .md-button--primary }

<script>
(function () {
  var tt = document.getElementById('topo-tt');
  if (!tt) return;
  var title = tt.querySelector('.tt-title');
  var desc  = tt.querySelector('.tt-desc');
  Array.prototype.slice.call(document.querySelectorAll('body > #topo-tt')).forEach(function (n) { if (n !== tt) n.remove(); });
  document.body.appendChild(tt);

  document.querySelectorAll('.topo-hotspot').forEach(function (el) {
    el.addEventListener('mouseenter', function () {
      title.textContent = el.dataset.title || '';
      desc.textContent  = el.dataset.desc  || '';
      tt.classList.add('show');
    });
    el.addEventListener('mousemove', function (e) {
      var x = e.clientX + 16, y = e.clientY + 16;
      if (e.clientX + 276 > window.innerWidth)  x = e.clientX - 276;
      if (e.clientY + 120 > window.innerHeight) y = e.clientY - 100;
      tt.style.left = x + 'px'; tt.style.top = y + 'px';
    });
    el.addEventListener('mouseleave', function () { tt.classList.remove('show'); });
  });
}());
</script>

## General rules for VFR

In the Philippine airpsace, VFR flights shall not be operated above FL200 (or other defined lower limit of Class A airspace) and shall not be flown at transonic and supersonic speeds.

When cruising level of a VFR flight is above 3000 feet, the tables in the [RVSM](rvsm.md) page shows the valid VFR cruising altitudes.
