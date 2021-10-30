class SettingsHandler():
    def __init__(self,settings) -> None:
        self.validated_settings = settings

    @property
    def validated_settings(self):
        return self.validate_settings

    @validated_settings.setter
    def validated_settings(self,settings):
        return None


    


    

