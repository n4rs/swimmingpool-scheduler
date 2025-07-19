from datetime import datetime, timedelta
from homeassistant.core import HomeAssistant

async def get_chlorinator_forecast_schedule(hass: HomeAssistant, weather_entity: str) -> dict:
    forecast = hass.states.get(weather_entity)
    if forecast is None:
        return {}

    forecast_data = forecast.attributes.get("forecast", [])
    if not forecast_data:
        return {}

    # Initialize a dict to hold active hours per day (0-4)
    hourly_schedule = {}

    for day_index, day in enumerate(forecast_data[:5]):
        high_temp = day.get("temperature")
        uv_index = day.get("uv_index", 5)  # fallback if not provided
        date_str = day.get("datetime")

        # Estimate chlorinator runtime based on temp and UV
        runtime = calculate_runtime(high_temp, uv_index)
        start_hour = 12 - runtime // 2
        end_hour = start_hour + runtime

        daily_hours = {h: True for h in range(start_hour, end_hour)}
        hourly_schedule[day_index] = daily_hours

    return hourly_schedule

def calculate_runtime(temp: float, uv_index: float) -> int:
    # Simple logic: base runtime on temperature and UV index
    if temp is None:
        return 4
    base_hours = min(max((temp - 18) * 0.3 + uv_index * 0.2, 2), 12)
    return round(base_hours)