# Mabuhay!

Welcome to **Philippines vACC Knowledge Base!** This serves as a guide for observers, controllers, and pilots flying in and out of the Philippine Airspace.

For additional information, please see our [website](https://vatphil.com)!

# Events

<!DOCTYPE html>
<html lang="en">
  <h2>Upcoming Events</h2>
  <div id="vatsim-events" class="loading">Loading events...</div>

  <script>
    function toZulu(dateStr) {
      const d = new Date(dateStr);
      const pad = n => String(n).padStart(2, '0');
      return `${d.getUTCFullYear()}-${pad(d.getUTCMonth()+1)}-${pad(d.getUTCDate())} ${pad(d.getUTCHours())}:${pad(d.getUTCMinutes())}z`;
    }

    fetch('https://my.vatsim.net/api/v2/events/latest')
      .then(res => res.json())
      .then(data => {
        const events = data.data.filter(e =>
          e.airports && e.airports.some(a => a.icao && a.icao.startsWith('RP'))
        );

        const container = document.getElementById('vatsim-events');

        if (!events.length) {
          container.innerHTML = '<p class="no-events">No upcoming events found for the Philippines.</p>';
          return;
        }

        container.classList.remove('loading');
        container.innerHTML = `<div class="events-grid">${events.map(e => {
          const airports = e.airports.map(a => a.icao).join(', ');
          const route = e.routes && e.routes.length
            ? e.routes.map(r => `${r.departure} → ${r.arrival}${r.route ? ': <code>' + r.route + '</code>' : ''}`).join('<br>')
            : null;

          const poster = e.banner
            ? `<img class="event-poster" src="${e.banner}" alt="${e.name} poster" onerror="this.outerHTML='<div class=event-poster-placeholder>${e.name}</div>'">`
            : `<div class="event-poster-placeholder">${e.name}</div>`;

          return `
            <div class="event-card">
  ${poster}
  <div class="event-body">
    <h3>${e.name}</h3>
    <div class="event-row"><span class="label">Starts:</span> ${toZulu(e.start_time)}</div>
    <div class="event-row"><span class="label">Ends:</span> ${toZulu(e.end_time)}</div>
    <div class="event-row"><span class="label">Airports:</span> ${airports}</div>
    ${route ? `<div class="event-row"><span class="label">Route:</span> <span>${route}</span></div>` : ''}
    <a class="event-link" href="${e.link}" target="_blank">View on VATSIM →</a>
  </div>
</div>
          `;
        }).join('')}</div>`;
      })
      .catch(() => {
        document.getElementById('vatsim-events').innerHTML = '<p class="no-events">Could not load events. Please try again later.</p>';
      });
  </script>

</body>
</html>


# Reporting Errors
If you spot an error in any of the content on this site, please report it to the Operations team by either:

Emailing staff@vatphil.com or Join our [Discord Server](https://community.vatsim.net/)!

Thank you for choosing to fly in our airspace. We wish that you have a safe and enjoyable flight! Remember that if you are unsure about something on your flight, it is always best to ask the controllers.