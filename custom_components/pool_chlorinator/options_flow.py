from homeassistant import config_entries
import voluptuous as vol

class SwimmingPoolSchedulerOptionsFlowHandler(config_entries.OptionsFlow):
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Optional("manual_override", default=False): bool,
                vol.Optional("override_duration", default=60): int,
            })
        )