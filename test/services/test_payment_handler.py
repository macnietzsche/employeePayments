from json import load as json_load
from unittest import TestCase;
from services.payment_handler import PaymentHandler

with open("test/config/payment_settings_test.json") as file:
        payment_settings_data = json_load(file)

class TestPaymentHandler(TestCase):
    None
 
    