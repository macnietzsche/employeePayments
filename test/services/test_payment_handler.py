from json import load as json_load
from unittest import TestCase;
from subdomains.payment_handler import PaymentHandler

with open("test/input_files/payment_settings_test.json") as file:
        payment_settings_data = json_load(file)

with open("test/input_files/worked_days_summaries_test.json") as file:
        worked_days_summaries = json_load(file)

class TestPaymentHandler(TestCase):
    def setUp(self) -> None:
        self.payment_handler_instance = PaymentHandler(payment_settings_data)

    def test_calculate_payment_amount(self):
        worked_days_summary = worked_days_summaries['summary_case1']
        expected_payment_amount = 215.0
        payment_amount = self.payment_handler_instance.calculate_payment_amount(worked_days_summary)

        self.assertEqual(expected_payment_amount,payment_amount)

        worked_days_summary = worked_days_summaries['summary_case2']
        expected_payment_amount = 85.0
        payment_amount = self.payment_handler_instance.calculate_payment_amount(worked_days_summary)

        self.assertEqual(expected_payment_amount,payment_amount)



 
    