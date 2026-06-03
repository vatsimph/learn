(function () {
  function initChartEmbeds() {
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
        // No observer support: just load it (no behavioural regression).
        frame.setAttribute("src", src);
        return;
      }

      var observer = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            if (!entry.isIntersecting) return;
            var el = entry.target;
            var deferred = el.getAttribute("data-chart-src");
            if (deferred && !el.getAttribute("src")) {
              el.setAttribute("src", deferred);
            }
            observer.unobserve(el);
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
