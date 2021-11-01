
from services.time_interval_handler import TimeIntervalHandler

class PaymentHandler():
    def __init__(self,settings) -> None:
        self.time_interval_handler = TimeIntervalHandler(settings,True)

    