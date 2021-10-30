from json import load as json_load
from unittest import TestCase;
from services.settings_handler import SettingsHandler

with open("test/config/settings.json") as file:
        settings_data = json_load(file)

class TestSettingsHandler(TestCase):
    def test_settings_have_missing_parameters(self):
        setting = settings_data['payment_config_missing_one_parameter']
        with self.assertRaises(Exception):
            SettingsHandler(setting)

        setting = settings_data['payment_config_missing_two_parameters']
        with self.assertRaises(Exception):
            SettingsHandler(setting)

        setting = settings_data['payment_config_missing_three_parameters']
        with self.assertRaises(Exception):
            SettingsHandler(setting)

        setting = settings_data['payment_config_missing_all_parameters']
        with self.assertRaises(Exception):
            SettingsHandler(setting)

        setting = settings_data['payment_config_missing_random_parameters']
        with self.assertRaises(Exception):
            SettingsHandler(setting)

    def test_settings_have_overlapping_time_intervals(self):
        setting = settings_data["payment_config_overlapping_time_intervals_case1"]
        with self.assertRaises(Exception):
            SettingsHandler(setting)

        setting = settings_data["payment_config_overlapping_time_intervals_case2"]
        with self.assertRaises(Exception):
            SettingsHandler(setting)
        
        setting = settings_data["payment_config_overlapping_time_intervals_case3"]
        with self.assertRaises(Exception):
            SettingsHandler(setting)
        
        setting = settings_data["payment_config_overlapping_time_intervals_case4"]
        with self.assertRaises(Exception):
            SettingsHandler(setting)

    def test_settings_sorted_ascending_by_start_time(self):
        # Case 1
        unsorted_setting = settings_data["payment_config_unsorted_case1"]
        expected_sorted_setting = settings_data["payment_config_sorted_case1"]

        settings_instance = SettingsHandler(unsorted_setting)
        sorted_setting = settings_instance.validated_settings

        self.assertEqual(sorted_setting,expected_sorted_setting)

        # Case 2
        unsorted_setting = settings_data["payment_config_unsorted_case2"]
        expected_sorted_setting = settings_data["payment_config_sorted_case2"]

        settings_instance = SettingsHandler(unsorted_setting)
        sorted_setting = settings_instance.validated_settings

        self.assertEqual(sorted_setting,expected_sorted_setting)

        # Case 3
        unsorted_setting = settings_data["payment_config_unsorted_case3"]
        expected_sorted_setting = settings_data["payment_config_sorted_case3"]

        settings_instance = SettingsHandler(unsorted_setting)
        sorted_setting = settings_instance.validated_settings

        self.assertEqual(sorted_setting,expected_sorted_setting)

            
        