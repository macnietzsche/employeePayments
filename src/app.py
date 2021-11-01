from json import load as json_load
from services.time_interval_handler import TimeIntervalHandler

if __name__ == '__main__':
    with open("test/config/time_intervals_test.json") as file:
        settings_data = json_load(file)

    setting = settings_data["correct_time_segments_case1"]
    TimeIntervalHandler(setting,True)    
    print("hello world")