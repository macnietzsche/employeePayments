from services.time_interval_handler import TimeIntervalHandler, START_TIME_KEY, END_TIME_KEY
class InputHandler():
    def __init__(self, plain_text_line) -> None:
        self.normalized_input = plain_text_line

    @property
    def normalized_input(self):
        return self._normalized_input
    
    @normalized_input.setter
    def normalized_input(self, plain_text_line):
        clean_line = plain_text_line.replace(" ","").replace("\n","").replace(":","")
        head_body = clean_line.split("=")

        if not len(head_body)==2:
            raise Exception("Input head or body is missing")
        
        head = head_body[0]
        body = head_body[1]

        raw_day_summaries = body.split(",")
        if not len(raw_day_summaries)>0:
            raise Exception("Body must contain at least one day summary")
        
        day_summaries = {}
        for raw_day_summary in raw_day_summaries:
            day = raw_day_summary[:2]
            time_data = raw_day_summary[2:]
            
            start_end_time_values = time_data.split("-")
            if not len(start_end_time_values)==2:
                raise Exception("There must be only start and end time values")

            try:
                start_time = int(start_end_time_values[0])
                end_time = int(start_end_time_values[1])
            except:
                raise Exception("Start and end time values must be numeric")

            day_summary = {
                START_TIME_KEY: start_time,
                END_TIME_KEY: end_time
            }

            time_interval_handler = TimeIntervalHandler([day_summary])
            if not time_interval_handler.get_day_type(day):
                raise Exception("Day key is not valid")

            day_summaries[day] = time_interval_handler.validated_time_intervals
           
        self._normalized_input = {
            'label': head,
            'value': day_summaries
        }