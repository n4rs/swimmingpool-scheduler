from homeassistant import config_entries
import voluptuous as vol
from homeassistant.const import CONF_ENTITY_ID

DOMAIN = "swimmingpool_scheduler"

class SwimmingPoolSchedulerConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="Swimming Pool Scheduler", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("pump_entity"): str,
                vol.Required("chlorinator_entity"): str,
                vol.Required("fan_entity"): str,
                vol.Required("weather_entity", default="weather.openweathermap"): str,
            })
        )