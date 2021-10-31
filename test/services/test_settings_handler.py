from json import load as json_load
from unittest import TestCase;
from services.settings_handler import SettingsHandler

with open("test/config/settings_test.json") as file:
        settings_data = json_load(file)

class TestSettingsHandler(TestCase):
    def test_settings_have_missing_parameters(self):
        setting = settings_data['missing_one_parameter']
        with self.assertRaises(Exception):
            SettingsHandler(setting,True)

        setting = settings_data['missing_two_parameters']
        with self.assertRaises(Exception):
            SettingsHandler(setting,True)

        setting = settings_data['missing_three_parameters']
        with self.assertRaises(Exception):
            SettingsHandler(setting,True)

        setting = settings_data['missing_all_parameters']
        with self.assertRaises(Exception):
            SettingsHandler(setting,True)

        setting = settings_data['missing_random_parameters']
        with self.assertRaises(Exception):
            SettingsHandler(setting,True)
    