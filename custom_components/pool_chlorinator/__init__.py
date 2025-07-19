import asyncio
from homeassistant.core import HomeAssistant, callback
from homeassistant.components.websocket_api import async_register_command
from datetime import datetime, timedelta
from homeassistant.helpers.event import async_track_time_change
from . import get_chlorinator_forecast_schedule

# Store runtime schedule in hass.data for retrieval by custom card
async def async_setup_entry(hass: HomeAssistant, config_entry):
    domain = "swimmingpool_scheduler"
    hass.data.setdefault(domain, {})

    weather_entity = config_entry.data.get("weather_entity", "weather.openweathermap")

    # Register WebSocket API for frontend card to fetch schedule
    @callback
    async def handle_get_schedule(hass, connection, msg):
        schedule = hass.data[domain].get("hourly_schedule")
        connection.send_result(msg["id"], {"schedule": schedule})

    async_register_command(hass, "swimmingpool_scheduler.get_schedule", handle_get_schedule)

    # Run once on setup
    await store_hourly_schedule(hass, weather_entity)

    # Schedule it to run daily at 00:10
    async_track_time_change(
        hass,
        lambda *_: hass.async_create_task(store_hourly_schedule(hass, weather_entity)),
        hour=0,
        minute=10,
        second=0
    )

    return True

# Called daily to compute and store the schedule for the next 5 days
async def store_hourly_schedule(hass: HomeAssistant, weather_entity: str):
    domain = "swimmingpool_scheduler"
    forecast_schedule_by_day = await get_chlorinator_forecast_schedule(hass, weather_entity)

    # Expected format: dict[int(day_index)] -> dict[int(hour)] = bool
    # Convert to a list of lists of hours (hourly schedule per day)
    full_schedule = []
    for day_index in range(5):
        daily_hours = [hour for hour, active in forecast_schedule_by_day.get(day_index, {}).items() if active]
        full_schedule.append(daily_hours)

    hass.data[domain]["hourly_schedule"] = full_schedule