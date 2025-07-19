class SwimmingPoolSchedulerCard extends HTMLElement {
  set hass(hass) {
    const entity = "swimmingpool_scheduler.get_schedule";
    this._hass = hass;

    if (!this.loaded) {
      this.loaded = true;
      this.fetchSchedule();
    }
  }

  async fetchSchedule() {
    const connection = await window.hassConnection;
    connection.sendMessagePromise({
      type: "swimmingpool_scheduler.get_schedule",
      id: Math.floor(Math.random() * 10000),
    }).then(response => {
      const schedule = response.schedule;
      this.renderCard(schedule);
    }).catch(error => {
      this.innerHTML = "<ha-card><div class='card-content'>Error loading schedule</div></ha-card>";
      console.error(error);
    });
  }

  renderCard(schedule) {
    const days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
    const today = new Date();
    const labels = Array.from({ length: 5 }, (_, i) => {
      const d = new Date(today);
      d.setDate(d.getDate() + i);
      return days[d.getDay()];
    });

    let style = `
      <style>
        .day-column {
          display: grid;
          grid-template-rows: repeat(4, auto);
          padding: 4px;
          border: 1px solid #ccc;
        }
        .hour-grid {
          display: grid;
          grid-template-columns: repeat(24, 1fr);
          gap: 1px;
        }
        .hour-block {
          height: 16px;
          font-size: 8px;
          text-align: center;
          line-height: 16px;
        }
        .on  { background-color: green; color: white; }
        .off { background-color: yellow; color: black; }
        .summary {
          text-align: center;
          font-size: 12px;
          padding: 4px 0;
        }
        .days-wrapper {
          display: grid;
          grid-template-columns: repeat(5, 1fr);
          gap: 8px;
        }
      </style>
    `;

    let html = `<ha-card header="Swimming Pool Scheduler"><div class="card-content">${style}<div class="days-wrapper">`;

    for (let i = 0; i < 5; i++) {
      const hours = schedule[i] || [];
      const hourGrid = Array.from({ length: 24 }, (_, h) => {
        const active = hours.includes(h);
        return `<div class="hour-block ${active ? 'on' : 'off'}">${h}</div>`;
      }).join("");

      html += `
        <div class="day-column">
          <div class="summary"><b>${labels[i]}</b></div>
          <div class="summary">Min - Avg - Max</div>
          <div class="summary">UV Index</div>
          <div class="summary">${hours.length}h</div>
          <div class="hour-grid">${hourGrid}</div>
        </div>
      `;
    }

    html += `</div></div></ha-card>`;
    this.innerHTML = html;
  }

  setConfig(config) {
    this.config = config;
  }

  getCardSize() {
    return 4;
  }
}

customElements.define("swimmingpool-scheduler-card", SwimmingPoolSchedulerCard);