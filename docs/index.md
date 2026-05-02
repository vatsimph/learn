# Mabuhay!

Welcome to **Philippines vACC Knowledge Base!** This serves as a guide for observers, controllers, and pilots flying in and out of the Philippine Airspace.

For additional information, please see our [website](https://vatphil.com)!

# Reporting Errors
If you spot an error in any of the content on this site, please report it to the Operations team by either:

Emailing staff@vatphil.com or Join our [Discord Server](https://community.vatsim.net/)!

Thank you for choosing to fly in our airspace. We wish that you have a safe and enjoyable flight! Remember that if you are unsure about something on your flight, it is always best to ask the controllers.

# Events

Upcoming events organised by VATSIM Philippines.

<div id="vatphil-events">
  <p style="color: var(--md-default-fg-color--light)">Loading events...</p>
</div>

<style>
  .event-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.25rem;
    margin-top: 1rem;
  }

  .event-card {
    border: 1px solid var(--md-default-fg-color--lightest, #e0e0e0);
    border-radius: 8px;
    overflow: hidden;
    background: var(--md-default-bg-color);
    box-shadow: 0 2px 6px rgba(0,0,0,0.08);
    transition: box-shadow 0.2s;
    text-decoration: none;
    display: flex;
    flex-direction: column;
    color: inherit;
  }

  .event-card:hover {
    box-shadow: 0 4px 14px rgba(0,0,0,0.15);
  }

  .event-card img {
    width: 100%;
    aspect-ratio: 16/7;
    object-fit: cover;
    display: block;
  }

  .event-card-body {
    padding: 0.85rem 1rem 1rem;
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 0.35rem;
  }

  .event-type-badge {
    font-size: 0.7rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--md-primary-fg-color, #1976d2);
  }

  .event-name {
    font-size: 1rem;
    font-weight: 700;
    line-height: 1.3;
    margin: 0;
  }

  .event-meta {
    font-size: 0.8rem;
    color: var(--md-default-fg-color--light, #666);
    margin-top: auto;
    padding-top: 0.5rem;
    display: flex;
    flex-direction: column;
    gap: 0.2rem;
  }

  .event-airports {
    font-size: 0.75rem;
    color: var(--md-default-fg-color--light, #888);
  }

  .no-events {
    color: var(--md-default-fg-color--light);
    font-style: italic;
  }
</style>

<script>
(async function () {
  const container = document.getElementById('vatphil-events');

  function formatDate(iso) {
    const d = new Date(iso);
    return d.toLocaleDateString('en-PH', {
      weekday: 'long', year: 'numeric', month: 'long', day: 'numeric'
    });
  }

  function formatTime(start, end) {
    const fmt = t => new Date(t).toISOString().substr(11, 5) + 'Z';
    return `${fmt(start)} – ${fmt(end)}`;
  }

  try {
    // Use the SEA division endpoint — VATPHIL is a subdivision under SEA
    const res = await fetch('https://my.vatsim.net/api/v2/events/view/division/SEA');
    if (!res.ok) throw new Error('API error');
    const json = await res.json();

    const PHIL_KEYWORDS = ['phi', 'phil', 'vatphil', 'philippines'];

    // Temporary: log all organiser strings so you can verify the correct value
    console.log('[VATPHIL Events] All organisers in SEA feed:',
      (json.data || []).flatMap(e => e.organisers).map(o => JSON.stringify(o))
    );

    const events = (json.data || []).filter(e =>
      e.organisers && e.organisers.some(o => {
        const div = (o.division || '').toLowerCase();
        const sub = (o.subdivision || '').toLowerCase();
        return PHIL_KEYWORDS.some(k => div.includes(k) || sub.includes(k));
      })
    );

    if (events.length === 0) {
      container.innerHTML = '<p class="no-events">No upcoming VATPHIL events at this time. Check back soon!</p>';
      return;
    }

    const grid = document.createElement('div');
    grid.className = 'event-grid';

    events.forEach(e => {
      const airports = e.airports.map(a => a.icao).join(', ');
      const card = document.createElement('a');
      card.className = 'event-card';
      card.href = e.link;
      card.target = '_blank';
      card.rel = 'noopener noreferrer';

      card.innerHTML = `
        ${e.banner ? `<img src="${e.banner}" alt="${e.name}" loading="lazy">` : ''}
        <div class="event-card-body">
          <div class="event-type-badge">${e.type}</div>
          <div class="event-name">${e.name}</div>
          <div class="event-meta">
            <span>${formatDate(e.start_time)}</span>
            <span>${formatTime(e.start_time, e.end_time)}</span>
            ${airports ? `<span class="event-airports">${airports}</span>` : ''}
          </div>
        </div>
      `;

      grid.appendChild(card);
    });

    container.innerHTML = '';
    container.appendChild(grid);

  } catch (err) {
    container.innerHTML = '<p class="no-events"No events just yet!</p>';
    console.error('VATPHIL events error:', err);
  }
})();
</script>