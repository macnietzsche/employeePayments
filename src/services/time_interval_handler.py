from services.array_methods import binarySearch

MIN_TIME = 1
MAX_TIME = 2400
START_TIME_KEY = 'start_time'
END_TIME_KEY = 'end_time'
class TimeIntervalHandler():
    def __init__(self,time_intervals, segments_must_be_continuous = False):
        self.segments_must_be_continuous = segments_must_be_continuous
        self.validated_time_intervals = time_intervals
    
    @property
    def validated_time_intervals(self):
        return self._validated_time_intervals
    
    @validated_time_intervals.setter
    def validated_time_intervals(self,time_intervals):
        validated_settings = []
        for setting in time_intervals:
            start_time = setting[START_TIME_KEY]   
            end_time = setting[END_TIME_KEY]
            if not (self.__is_time_value_valid(start_time) and self.__is_time_value_valid(end_time)):
                raise Exception("Time value is not valid")

            if not (start_time<end_time):
                raise Exception('End time must be greater than start time')

            for item in validated_settings:
                sorted_start_time = item[START_TIME_KEY]
                sorted_end_time = item [END_TIME_KEY]

                if not (end_time<sorted_start_time or start_time>sorted_end_time):
                    raise Exception('No overlapping time segments are allowed.')

            validated_settings.append(setting)

        sorted_settings = sorted(validated_settings,key=lambda item: item[START_TIME_KEY])
        if len(sorted_settings)>1 and self.segments_must_be_continuous:
            last_time_segment = sorted_settings[-1]
            for sorted_setting in sorted_settings:
                if last_time_segment:
                    end_time_to_be_compared = self.__sum_minutes_to_time(last_time_segment[END_TIME_KEY],1)
                    if not end_time_to_be_compared==sorted_setting[START_TIME_KEY]:
                        raise Exception("Time segments must be continous")     
                last_time_segment = sorted_setting

        self._validated_time_intervals = sorted_settings

    def find_time_segment(self, time):
        return binarySearch(self.validated_time_intervals,time,START_TIME_KEY,END_TIME_KEY)

    def __sum_minutes_to_time(self,time, minutes_to_be_added):
        hours=time//100
        minutes=time%100

        minutes += minutes_to_be_added
        if minutes > 59:
            hours += 1
            minutes = 0

        result = hours * 100 + minutes
        if result > MAX_TIME:
            return MIN_TIME

        return result

    def __is_time_value_valid(self, time):
        hours=time//100
        minutes=time%100

        MAX_HOUR = MAX_TIME//100
        MIN_HOUR = MIN_TIME//100

        if hours < MIN_HOUR or hours > MAX_HOUR or minutes > 59 or minutes < 0:
            return False
        
        return True