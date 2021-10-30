
REQUIRED_PARAMETERS = ['start_time','end_time', 'payment_amount_on_weekdays','payment_amount_on_weekends']
class SettingsHandler():
    def __init__(self,settings) -> None:
        self.validated_settings = settings

    @property
    def validated_settings(self):
        return self.validate_settings

    @validated_settings.setter
    def validated_settings(self,settings):
        for setting in settings:
            for parameter in REQUIRED_PARAMETERS:
                if not parameter in setting:
                    raise Exception(f'Parameter {parameter} is missing.')