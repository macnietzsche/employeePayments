
REQUIRED_PARAMETERS = ['start_time','end_time', 'payment_amount_on_weekdays','payment_amount_on_weekends']
class SettingsHandler():
    def __init__(self,settings) -> None:
        self.validated_settings = settings

    @property
    def validated_settings(self):
        return self.validate_settings

    @validated_settings.setter
    def validated_settings(self,settings):
        end_time_stack = []
        for setting in settings:
            for parameter in REQUIRED_PARAMETERS:
                if not parameter in setting:
                    raise Exception(f'Parameter {parameter} is missing.')

            start_time = setting['start_time']   
            end_time = setting['end_time']
            if not (start_time<end_time):
                raise Exception('End time must be greater than start time')

            for end_time_item in end_time_stack:
                if start_time<=end_time_item:
                    raise Exception('Overlapping time segments are not allowed')
            end_time_stack.append(end_time)
        self.settings = settings