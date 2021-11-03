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

    # def test_singleton_pattern(self):
    #     instance1 = PaymentHandler(payment_settings_data)
    #     instance2 = PaymentHandler(payment_settings_data)
    #     instance3 = PaymentHandler(payment_settings_data)

    #     self.assertEqual(instance1,instance2)
    #     self.assertEqual(instance1,instance3)
    #     self.assertEqual(instance2,instance3)

    def test_calculate_payment_amount(self):
        worked_days_summary = worked_days_summaries[0]['value']
        expected_payment_amount = 215.0
        payment_amount = self.payment_handler_instance.calculate_payment_amount(worked_days_summary)

        self.assertEqual(expected_payment_amount,payment_amount)

        worked_days_summary = worked_days_summaries[1]['value']
        expected_payment_amount = 85.0
        payment_amount = self.payment_handler_instance.calculate_payment_amount(worked_days_summary)

        self.assertEqual(expected_payment_amount,payment_amount)



 
    