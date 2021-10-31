
from services.time_interval_handler import TimeIntervalHandler

REQUIRED_PARAMETERS = ['start_time','end_time', 'payment_amount_on_weekdays','payment_amount_on_weekends']
class SettingsHandler():
    def __init__(self,settings) -> None:
        self.time_interval_handler = TimeIntervalHandler(settings,True)
        self.validated_settings = self.time_interval_handler.validated_time_intervals

    @property
    def validated_settings(self):
        return self._validated_settings

    @validated_settings.setter
    def validated_settings(self,settings):
        validated_settings = []
        for setting in settings:
            for parameter in REQUIRED_PARAMETERS:
                if not parameter in setting:
                    raise Exception(f'Parameter {parameter} is missing.')

            validated_settings.append(setting)

        self._validated_settings = settings