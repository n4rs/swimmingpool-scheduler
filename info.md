# Swimming Pool Scheduler

A custom Home Assistant integration that automates your pool chlorinator runtime based on weather forecast (temperature and UV index), with built-in logic for safe pump/chlorinator/fan sequencing. Includes a Lovelace card to visualize the hourly operation schedule.

---

## 💡 Features

- Adjusts runtime daily based on temperature and UV forecast
- Controls pump, chlorinator and fan with delays
- Shows 5-day schedule in a visual dashboard card
- Works with OpenWeatherMap or any compatible weather entity
- Manual override support (via options)
- Fully configurable from the UI
- HACS compatible

---

## 📊 Custom Lovelace Card

Displays:
- Min / Avg / Max temperature
- Max UV index
- Estimated chlorinator runtime
- Hour-by-hour ON/OFF status (color-coded)

---

## 🧠 How it Works

- Forecast fetched daily at 00:10 or on startup
- Runtime is estimated using temperature & UV index
- Schedule is stored in memory and made available via WebSocket API
- Frontend card fetches and renders the current 5-day hourly schedule

---

## ⚙️ Configuration

- Set up via UI: Select pump, chlorinator, fan, and weather entity
- Optional override duration can be set via the integration options

---

## 📦 Installation

1. Add this repo to HACS as a custom integration
2. Install the integration and restart Home Assistant
3. Add the card via Lovelace: `custom:swimmingpool-scheduler-card`
4. Make sure the JavaScript file is loaded in Lovelace resources

---

MIT License