from services.time_interval_handler import TimeIntervalHandler, START_TIME_KEY, END_TIME_KEY
from common.singleton_metaclass import SingletonMetaClass

WEEKEND_PAYMENT_VALUE_KEY = 'weekend_payment'
WEEKDAY_PAYMENT_VALUE_KEY = 'weekday_payment'

class PaymentHandler():
    def __init__(self,settings) -> None:
        self.time_interval_handler = TimeIntervalHandler(settings,True)

    def calculate_payment_amount(self, worked_days_summary):
        settings = self.time_interval_handler.validated_time_intervals
        settings_max_index = len(settings) - 1
        day_keys = list(worked_days_summary.keys())

        total_ammount = 0
        for day_key in day_keys:
            day_type = self.time_interval_handler.get_day_type(day_key)
            if day_type == 'weekday':
                payment_value_key = WEEKDAY_PAYMENT_VALUE_KEY
            elif day_type == 'weekend':
                payment_value_key = WEEKEND_PAYMENT_VALUE_KEY
            else:
                return -1

            day_summary = worked_days_summary[day_key]
            day_amount = 0
            for worked_segment in day_summary:
                start_time  = worked_segment[START_TIME_KEY]
                end_time = worked_segment[END_TIME_KEY]
                
                index = self.time_interval_handler.find_time_segment(start_time)
                lower = start_time
                segment_amount = 0
                while True:
                    current_setting = settings[index]
                    max_time  = current_setting[END_TIME_KEY]
                    upper = max_time if(end_time > max_time) else end_time               
                    segment_amount += self.time_interval_handler.time_diff_in_hours(lower,upper) * current_setting[payment_value_key]
                    
                    lower = upper
                    index += 1
                    if(index > settings_max_index or end_time<=max_time):
                        break

                day_amount+=segment_amount

            total_ammount += day_amount

        return total_ammount


    