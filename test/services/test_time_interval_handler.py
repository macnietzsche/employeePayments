from json import load as json_load
from unittest import TestCase;
from services.time_interval_handler import TimeIntervalHandler

with open("test/config/time_intervals_test.json") as file:
        time_interval_data = json_load(file)

class TestTimeIntervalHandler(TestCase):
    def test_intervals_have_overlapping_time_segments(self):
        time_interval = time_interval_data["overlapping_time_intervals_case1"]
        with self.assertRaises(Exception):
            TimeIntervalHandler(time_interval,True)

        time_interval = time_interval_data["overlapping_time_intervals_case2"]
        with self.assertRaises(Exception):
            TimeIntervalHandler(time_interval,True)
        
        time_interval = time_interval_data["overlapping_time_intervals_case3"]
        with self.assertRaises(Exception):
            TimeIntervalHandler(time_interval,True)
        
    def test_intervals_sorted_ascending_by_start_time(self):
        # Case 1
        unsorted_time_interval = time_interval_data["unsorted_case1"]
        expected_sorted_time_interval = time_interval_data["sorted_case1"]

        time_intervals_instance = TimeIntervalHandler(unsorted_time_interval,True)
        sorted_time_interval = time_intervals_instance.validated_time_intervals

        self.assertEqual(sorted_time_interval,expected_sorted_time_interval)

        # Case 2
        unsorted_time_interval = time_interval_data["unsorted_case2"]
        expected_sorted_time_interval = time_interval_data["sorted_case2"]

        time_intervals_instance = TimeIntervalHandler(unsorted_time_interval,True)
        sorted_time_interval = time_intervals_instance.validated_time_intervals

        self.assertEqual(sorted_time_interval,expected_sorted_time_interval)

        # Case 3
        unsorted_time_interval = time_interval_data["unsorted_case3"]
        expected_sorted_time_interval = time_interval_data["sorted_case3"]

        time_intervals_instance = TimeIntervalHandler(unsorted_time_interval,True)
        sorted_time_interval = time_intervals_instance.validated_time_intervals

        self.assertEqual(sorted_time_interval,expected_sorted_time_interval)
    
    def test_intervals_have_missing_time_segments(self):
        time_interval = time_interval_data["missing_time_segments_case1"]
        with self.assertRaises(Exception):
            TimeIntervalHandler(time_interval,True)

        time_interval = time_interval_data["missing_time_segments_case2"]
        with self.assertRaises(Exception):
            TimeIntervalHandler(time_interval,True)

        time_interval = time_interval_data["missing_time_segments_case3"]
        with self.assertRaises(Exception):
            TimeIntervalHandler(time_interval,True)