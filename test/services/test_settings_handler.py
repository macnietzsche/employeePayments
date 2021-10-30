from json import load as json_load
from unittest import TestCase;
from services.settings_handler import SettingsHandler

with open("test/config/settings.json") as file:
        settings_data = json_load(file)

class TestSettingsHandler(TestCase):
    def test_setting_is_missing_one_parameter(self):
        setting = settings_data['payment_config_missing_one_parameter']
        with self.assertRaises(Exception):
            SettingsHandler(setting)

    def test_setting_is_missing_two_parameters(self):
        setting = settings_data['payment_config_missing_two_parameters']
        with self.assertRaises(Exception):
            SettingsHandler(setting)

    def test_setting_is_missing_three_parameters(self):
        setting = settings_data['payment_config_missing_three_parameters']
        with self.assertRaises(Exception):
            SettingsHandler(setting)
    
    def test_setting_is_missing_all_parameters(self):
        setting = settings_data['payment_config_missing_all_parameters']
        with self.assertRaises(Exception):
            SettingsHandler(setting)

    def test_setting_is_missing_random_parameters(self):
        setting = settings_data['payment_config_missing_random_parameters']
        with self.assertRaises(Exception):
            SettingsHandler(setting)

    def test_setting_has_overlapping_time_intervals_case1(self):
        setting = settings_data["payment_config_overlapping_time_intervals_case1"]
        with self.assertRaises(Exception):
            SettingsHandler(setting)

    def test_setting_has_overlapping_time_intervals_case2(self):
        setting = settings_data["payment_config_overlapping_time_intervals_case3"]
        with self.assertRaises(Exception):
            SettingsHandler(setting)
    
    def test_setting_has_overlapping_time_intervals_case3(self):
        setting = settings_data["payment_config_overlapping_time_intervals_case3"]
        with self.assertRaises(Exception):
            SettingsHandler(setting)
        

            
        