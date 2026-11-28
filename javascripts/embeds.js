/*
 * Defer-load the vatphil.com chart embeds and stop them from hijacking scroll.
 *
 * The embedded charts page autofocuses its "Search Charts" input on load. When
 * an element inside a cross-origin iframe receives focus, the browser scrolls
 * the parent document to bring that iframe into view. On briefings where the
 * Charts section sits within the initial viewport, this yanks the page down to
 * the charts on load.
 *
 * Two-part defence:
 *   1. Strip each iframe's src on load and only restore it via IntersectionObserver,
 *      so nothing loads (or steals focus) until the section is on screen.
 *   2. When an iframe loads while the user has NOT scrolled yet, snap the scroll
 *      position back for a short window to cancel the autofocus jump. This is
 *      disabled the moment the user makes a real scroll gesture, so we never
 *      fight someone who is deliberately scrolling to the charts.
 */
(function () {
  var userScrolled = false;

  // Only genuine user gestures count — our own window.scrollTo() fires "scroll"
  // events but none of these, so the snap-back can't trigger itself.
  ["wheel", "touchmove", "keydown", "pointerdown"].forEach(function (evt) {
    window.addEventListener(evt, function () { userScrolled = true; },
      { passive: true, capture: true });
  });

  function loadFrame(el) {
    var deferred = el.getAttribute("data-chart-src");
    if (!deferred || el.getAttribute("src")) return;

    var y = window.scrollY;
    el.setAttribute("src", deferred);

    if (userScrolled) return; // user is in control — let the browser be

    // Hold the scroll position for a short window so the iframe's autofocus
    // (which fires around its load event) can't drag the page down.
    var start = Date.now();
    var iv = setInterval(function () {
      if (userScrolled || Date.now() - start > 2000) { clearInterval(iv); return; }
      if (window.scrollY !== y) window.scrollTo(window.scrollX, y);
    }, 30);
    el.addEventListener("load", function () {
      if (!userScrolled) window.scrollTo(window.scrollX, y);
    }, { once: true });
  }

  function initChartEmbeds() {
    // Reset per page load. With Material's instant navigation the script (and
    // this flag) persist across page changes, so without this a scroll on an
    // earlier page would leave userScrolled=true and disable the guard on the
    // next briefing page. Navigating resets scroll to the top, so we start
    // each page fresh.
    userScrolled = false;

    var iframes = document.querySelectorAll(
      'iframe[src*="vatphil.com/charts"], iframe[data-chart-src]'
    );

    iframes.forEach(function (frame) {
      if (frame.__chartDeferred) return;

      var src = frame.getAttribute("data-chart-src") || frame.getAttribute("src");
      if (!src) return;

      frame.__chartDeferred = true;
      frame.setAttribute("data-chart-src", src);
      // Remove src so the embed does not load (and cannot steal focus/scroll)
      // until it is scrolled into view.
      frame.removeAttribute("src");

      if (!("IntersectionObserver" in window)) {
        loadFrame(frame);
        return;
      }

      var observer = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            if (!entry.isIntersecting) return;
            loadFrame(entry.target);
            observer.unobserve(entry.target);
          });
        },
        { rootMargin: "0px" }
      );

      observer.observe(frame);
    });
  }

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(initChartEmbeds);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initChartEmbeds);
  } else {
    initChartEmbeds();
  }
})();
