# Mabuhay!

Welcome to **Philippines vACC Knowledge Base!** This serves as a guide for observers, controllers, and pilots flying in and out of the Philippine Airspace.

For additional information, please see our [website](https://vatphil.com)!

# Events
<div id="vatphil-events">
  <p style="color: var(--md-default-fg-color--light)">Loading events...</p>
</div>

<div id="event-modal-overlay" onclick="closeEventModal()"></div>
<div id="event-modal">
  <button id="event-modal-close" onclick="closeEventModal()">&#x2715;</button>
  <div id="event-modal-content"></div>
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
    display: flex;
    flex-direction: column;
    color: inherit;
    cursor: pointer;
  }

  .event-card:hover {
    box-shadow: 0 4px 14px rgba(0,0,0,0.15);
  }

  .event-card-banner {
    width: 100%;
    background: #111;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
  }

  .event-card-banner img {
    width: 100%;
    height: auto;
    display: block;
    object-fit: contain;
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

  .event-read-more {
    margin-top: 0.65rem;
    font-size: 0.8rem;
    font-weight: 600;
    color: var(--md-primary-fg-color, #1976d2);
    align-self: flex-start;
    border-bottom: 1px solid transparent;
    transition: border-color 0.15s;
  }

  .event-card:hover .event-read-more {
    border-bottom-color: var(--md-primary-fg-color, #1976d2);
  }

  .no-events {
    color: var(--md-default-fg-color--light);
    font-style: italic;
  }

  #event-modal-overlay {
    display: none;
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.55);
    z-index: 9998;
  }

  #event-modal {
    display: none;
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: min(640px, 94vw);
    max-height: 85vh;
    overflow-y: auto;
    background: var(--md-default-bg-color);
    border-radius: 10px;
    box-shadow: 0 8px 40px rgba(0,0,0,0.25);
    z-index: 9999;
    padding: 1.5rem;
  }

  #event-modal.open,
  #event-modal-overlay.open {
    display: block;
  }

  #event-modal-close {
    position: absolute;
    top: 0.9rem;
    right: 1rem;
    background: none;
    border: none;
    font-size: 1.2rem;
    cursor: pointer;
    color: var(--md-default-fg-color--light);
    line-height: 1;
    padding: 0.2rem 0.4rem;
  }

  #event-modal-close:hover {
    color: var(--md-default-fg-color);
  }

  .modal-banner img {
    width: 100%;
    height: auto;
    border-radius: 6px;
    margin-bottom: 1rem;
    display: block;
  }

  .modal-type-badge {
    font-size: 0.7rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--md-primary-fg-color, #1976d2);
    margin-bottom: 0.3rem;
  }

  .modal-title {
    font-size: 1.25rem;
    font-weight: 700;
    line-height: 1.3;
    margin: 0 0 0.75rem;
  }

  .modal-meta {
    font-size: 0.85rem;
    color: var(--md-default-fg-color--light, #666);
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
    margin-bottom: 1rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid var(--md-default-fg-color--lightest, #e0e0e0);
  }

  .modal-description {
    font-size: 0.9rem;
    line-height: 1.65;
    white-space: pre-wrap;
    margin-bottom: 1.25rem;
  }

  .modal-link {
    display: inline-block;
    padding: 0.5rem 1.1rem;
    background: var(--md-primary-fg-color, #1976d2);
    color: #fff !important;
    border-radius: 5px;
    font-size: 0.85rem;
    font-weight: 600;
    text-decoration: none;
  }

  .modal-link:hover {
    opacity: 0.88;
  }
</style>

<script>
function closeEventModal() {
  document.getElementById('event-modal').classList.remove('open');
  document.getElementById('event-modal-overlay').classList.remove('open');
  document.body.style.overflow = '';
}

document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') closeEventModal();
});

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

  function openModal(ev) {
    const airports = ev.airports.map(a => a.icao).join(', ');
    const content = document.getElementById('event-modal-content');
    content.innerHTML = `
      ${ev.banner ? `<div class="modal-banner"><img src="${ev.banner}" alt="${ev.name}"></div>` : ''}
      <div class="modal-type-badge">${ev.type}</div>
      <div class="modal-title">${ev.name}</div>
      <div class="modal-meta">
        <span>${formatDate(ev.start_time)}</span>
        <span>${formatTime(ev.start_time, ev.end_time)}</span>
        ${airports ? `<span>${airports}</span>` : ''}
      </div>
      <div class="modal-description">${ev.short_description || ev.description || ''}</div>
      <a class="modal-link" href="${ev.link}" target="_blank" rel="noopener noreferrer">View on myVATSIM</a>
    `;
    document.getElementById('event-modal').classList.add('open');
    document.getElementById('event-modal-overlay').classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  try {
    const res = await fetch('https://my.vatsim.net/api/v2/events/view/division/SEA');
    if (!res.ok) throw new Error('API error');
    const json = await res.json();

    const PHIL_KEYWORDS = ['phi', 'phil', 'vatphil', 'philippines', 'rpll', 'rpvp', 'rpmd', 'rplb', 'rplc'];

    const events = (json.data || []).filter(e => {
      const hasRPAirport = e.airports && e.airports.some(a => a.icao.toUpperCase().startsWith('RP'));
      const hasPhilKeyword = [e.name, e.short_description, e.description].some(
        t => t && PHIL_KEYWORDS.some(k => t.toLowerCase().includes(k))
      );
      return hasRPAirport || hasPhilKeyword;
    });

    if (events.length === 0) {
      container.innerHTML = '<p class="no-events">No upcoming VATPHIL events at this time. Check back soon!</p>';
      return;
    }

    const grid = document.createElement('div');
    grid.className = 'event-grid';

    events.forEach(ev => {
      const airports = ev.airports.map(a => a.icao).join(', ');
      const card = document.createElement('div');
      card.className = 'event-card';
      card.onclick = () => openModal(ev);

      card.innerHTML = `
        ${ev.banner ? `<div class="event-card-banner"><img src="${ev.banner}" alt="${ev.name}" loading="lazy"></div>` : ''}
        <div class="event-card-body">
          <div class="event-type-badge">${ev.type}</div>
          <div class="event-name">${ev.name}</div>
          <div class="event-meta">
            <span>${formatDate(ev.start_time)}</span>
            <span>${formatTime(ev.start_time, ev.end_time)}</span>
            ${airports ? `<span class="event-airports">${airports}</span>` : ''}
          </div>
          <span class="event-read-more">Read more</span>
        </div>
      `;

      grid.appendChild(card);
    });

    container.innerHTML = '';
    container.appendChild(grid);

  } catch (err) {
    container.innerHTML = '<p class="no-events">Could not load events. Please try again later or visit <a href="https://vatphil.com/events" target="_blank">vatphil.com/events</a>.</p>';
    console.error('VATPHIL events error:', err);
  }
})();
</script>
# Reporting Errors
If you spot an error in any of the content on this site, please report it to the Operations team by either:

Emailing staff@vatphil.com or Join our [Discord Server](https://community.vatsim.net/)!

Thank you for choosing to fly in our airspace. We wish that you have a safe and enjoyable flight! Remember that if you are unsure about something on your flight, it is always best to ask the controllers.