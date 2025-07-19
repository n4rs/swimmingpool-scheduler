# Swimming Pool Scheduler for Home Assistant

This custom integration automates your pool chlorinator and includes a custom Lovelace card to visualize daily runtime based on forecast temperature and UV index.

---

## 🔧 Features
- Automatically determines runtime based on weather forecast
- Takes into account temperature and UV Index
- Built-in delays between pump, chlorinator and fan
- Interactive Lovelace card shows schedule over 5 days
- Full UI configuration
- Compatible with HACS

---

## 📦 Installation via HACS

### Step 1: Add Custom Repository

1. Go to HACS → Integrations → 3-dot menu → **Custom Repositories**
2. Add this repository URL:
```
https://github.com/YOUR_USERNAME/swimmingpool-scheduler
```
3. Select **Integration**

---

### Step 2: Install the Integration

1. Go to HACS → Integrations → Search `Swimming Pool Scheduler`
2. Click Install
3. Restart Home Assistant

---

### Step 3: Configure the Integration

1. Go to Settings → Devices & Services → `+ Add Integration`
2. Select **Swimming Pool Scheduler**
3. Choose:
   - Pump entity (input_boolean)
   - Chlorinator entity (input_boolean)
   - Fan entity (input_boolean)
   - Weather entity (e.g. `weather.openweathermap`)

---

## 🖼️ Custom Card Setup

### Step 1: Add Resource

Add to `configuration.yaml` or via UI → Dashboards → Resources:

```yaml
lovelace:
  resources:
    - url: /hacsfiles/swimmingpool-scheduler/swimmingpool_scheduler_card.js
      type: module
```

### Step 2: Add to Dashboard

```yaml
type: custom:swimmingpool-scheduler-card
```

---

## 📊 Card Layout

The card shows 5 columns (1 per day), and 4 rows:

1. Temperatures: `min - avg - max`
2. Max UV Index
3. Estimated runtime (in hours)
4. Hourly timeline:
   - 🟩 Green = chlorinator ON
   - 🟨 Yellow = chlorinator OFF
   - Each hour block is labeled

---

## 📁 File Structure

```
swimmingpool-scheduler/
├── custom_components/
│   └── swimmingpool_scheduler/
│       ├── __init__.py
│       ├── manifest.json
│       ├── config_flow.py
│       ├── options_flow.py
│       ├── get_chlorinator_forecast_schedule.py
│       └── translations/
│           └── en.json
├── www/
│   └── swimmingpool_scheduler_card.js
├── LICENSE
└── README.md
```

---

## 🧠 How it works

- On startup and daily at 00:10, it calculates the next 5 days’ schedule
- Uses your configured weather entity to forecast temperature & UV
- Serves hourly ON periods via WebSocket to the dashboard

---

## 📜 License

MIT