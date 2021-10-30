
REQUIRED_PARAMETERS = ['start_time','end_time', 'payment_amount_on_weekdays','payment_amount_on_weekends']
class SettingsHandler():
    def __init__(self,settings) -> None:
        self.validated_settings = settings

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

            start_time = setting['start_time']   
            end_time = setting['end_time']
            if not (start_time<end_time):
                raise Exception('End time must be greater than start time')

            for item in validated_settings:
                sorted_start_time = item['start_time']
                sorted_end_time = item ['end_time']
                
                if not (end_time<sorted_start_time or start_time>sorted_end_time):
                    raise Exception('No overlapping time segments are allowed.')

            validated_settings.append(setting) 

        self._validated_settings = sorted(validated_settings,key=lambda item: item['start_time'])