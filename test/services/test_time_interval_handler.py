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

        time_intervals_instance = TimeIntervalHandler(unsorted_time_interval)
        sorted_time_interval = time_intervals_instance.validated_time_intervals

        self.assertEqual(sorted_time_interval,expected_sorted_time_interval)

        # Case 2
        unsorted_time_interval = time_interval_data["unsorted_case2"]
        expected_sorted_time_interval = time_interval_data["sorted_case2"]

        time_intervals_instance = TimeIntervalHandler(unsorted_time_interval)
        sorted_time_interval = time_intervals_instance.validated_time_intervals

        self.assertEqual(sorted_time_interval,expected_sorted_time_interval)

        # Case 3
        unsorted_time_interval = time_interval_data["unsorted_case3"]
        expected_sorted_time_interval = time_interval_data["sorted_case3"]

        time_intervals_instance = TimeIntervalHandler(unsorted_time_interval)
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

    def test_intervals_have_invalid_time_values(self):
        time_interval = time_interval_data["invalid_time_values_case1"]
        with self.assertRaises(Exception):
            TimeIntervalHandler(time_interval,True)

        time_interval = time_interval_data["invalid_time_values_case2"]
        with self.assertRaises(Exception):
            TimeIntervalHandler(time_interval,True)

        time_interval = time_interval_data["invalid_time_values_case3"]
        with self.assertRaises(Exception):
            TimeIntervalHandler(time_interval,True)


    def test_find_time_segment_by_time(self):
        # Case 1
        time_interval = time_interval_data["correct_time_segments_case1"]
        time_intervals_instance = TimeIntervalHandler(time_interval,True)
        # Case 1: Test 1
        time = 1200
        expected_time_segment_to_be_found = 1
        time_segment_found = time_intervals_instance.find_time_segment(time)
        self.assertEqual(expected_time_segment_to_be_found,time_segment_found)

        # Case 1: Test 2
        time = 1900
        expected_time_segment_to_be_found = 2
        time_segment_found = time_intervals_instance.find_time_segment(time)
        self.assertEqual(expected_time_segment_to_be_found,time_segment_found)

        # Case 1: Test 3
        time = 300
        expected_time_segment_to_be_found = 0
        time_segment_found = time_intervals_instance.find_time_segment(time)
        self.assertEqual(expected_time_segment_to_be_found,time_segment_found)

        # Case 2
        time_interval = time_interval_data["correct_time_segments_case2"]
        time_intervals_instance = TimeIntervalHandler(time_interval,True)
        # Case 2: Test 1
        time = 1920
        expected_time_segment_to_be_found = 3
        time_segment_found = time_intervals_instance.find_time_segment(time)
        self.assertEqual(expected_time_segment_to_be_found,time_segment_found)

        # Case 2: Test 2
        time = 1500
        expected_time_segment_to_be_found = 1
        time_segment_found = time_intervals_instance.find_time_segment(time)
        self.assertEqual(expected_time_segment_to_be_found,time_segment_found)

        # Case 3: Test 3
        time = 1730
        expected_time_segment_to_be_found = 2
        time_segment_found = time_intervals_instance.find_time_segment(time)
        self.assertEqual(expected_time_segment_to_be_found,time_segment_found)

        #Case 3
        time_interval = time_interval_data["correct_time_segments_case3"]
        time_intervals_instance = TimeIntervalHandler(time_interval,True)
        # Case 3: Test 1
        time = 1920
        expected_time_segment_to_be_found = 4
        time_segment_found = time_intervals_instance.find_time_segment(time)
        self.assertEqual(expected_time_segment_to_be_found,time_segment_found)

        # Case 3: Test 2
        time = 1300
        expected_time_segment_to_be_found = 2
        time_segment_found = time_intervals_instance.find_time_segment(time)
        self.assertEqual(expected_time_segment_to_be_found,time_segment_found)

         # Case 3: Test 3
        time = 1000
        expected_time_segment_to_be_found = 1
        time_segment_found = time_intervals_instance.find_time_segment(time)
        self.assertEqual(expected_time_segment_to_be_found,time_segment_found)

    def test_time_diff_in_hours(self):
        start_time = 1500
        end_time = 1600
        expected_time_diff_in_hours = 1
        time_diff_in_hours = TimeIntervalHandler.time_diff_in_hours(start_time,end_time)
        self.assertEqual(expected_time_diff_in_hours,time_diff_in_hours)