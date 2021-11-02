
from subdomains.payment_handler import PaymentHandler
from json import load as json_load

with open("config/payment_settings.json") as file:
    payment_settings_data = json_load(file)

class Employee():
    def __init__(self, name, worked_days_summary):
        self.name = name
        self.worked_days_summary = worked_days_summary
        # This is a singleton instance
        self.payment_handler_service = PaymentHandler(payment_settings_data)

    def calculate_amount_to_be_paid(self):
        return self.payment_handler_service.calculate_payment_amount(self.worked_days_summary)

    def print_payment_receipt(self):
        print(f"The amount to pay {self.name} is: {self.calculate_amount_to_be_paid()}")