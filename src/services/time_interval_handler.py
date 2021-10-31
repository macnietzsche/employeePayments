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
            start_time = setting['start_time']   
            end_time = setting['end_time']
            if not (start_time<end_time):
                raise Exception('End time must be greater than start time')

            for item in validated_settings:
                sorted_start_time = item['start_time']
                sorted_end_time = item ['end_time']

                if not (end_time<sorted_start_time or start_time>sorted_end_time):
                    raise Exception('No overlapping time segments are allowed.')

            validated_settings.append(setting)

        sorted_settings = sorted(validated_settings,key=lambda item: item['start_time'])
        if len(sorted_settings)>1 and self.segments_must_be_continuous:
            last_time_segment = sorted_settings[-1]
            for sorted_setting in sorted_settings:
                if last_time_segment:
                    end_time_to_be_compared = last_time_segment["end_time"]
                    if end_time_to_be_compared >= 2400:
                        end_time_to_be_compared = 0

                    if not end_time_to_be_compared+1==sorted_setting['start_time']:
                        raise Exception("Time segments must be continous")     
                last_time_segment = sorted_setting

        self._validated_time_intervals = sorted_settings