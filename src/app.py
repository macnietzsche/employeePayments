from json import load as json_load
from services.settings_handler import SettingsHandler

if __name__ == '__main__':
    with open("test/config/settings.json") as file:
        settings_data = json_load(file)

    setting = settings_data["payment_config_unsorted_case1"]
    SettingsHandler(setting)    
    print("hello world")