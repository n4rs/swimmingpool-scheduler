DOMAIN = "swimmingpool_scheduler"

CONF_PUMP = "pump_entity"
CONF_CHLORINATOR = "chlorinator_entity"
CONF_FAN = "fan_entity"
CONF_WEATHER = "weather_entity"

CONF_MANUAL_OVERRIDE = "manual_override"
CONF_OVERRIDE_DURATION = "override_duration"

DEFAULT_WEATHER = "weather.openweathermap"
DEFAULT_OVERRIDE_DURATION = 60  # in minutes

WS_COMMAND_GET_SCHEDULE = f"{DOMAIN}.get_schedule"
DATA_HOURLY_SCHEDULE = "hourly_schedule"

SCHEDULE_UPDATE_HOUR = 0
SCHEDULE_UPDATE_MINUTE = 10