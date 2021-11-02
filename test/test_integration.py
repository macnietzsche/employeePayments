from unittest import TestCase
from app_initializer import process_line

correct_inputs=[]
file = open("test/input_files/integration_input_test.txt", "r")
for line in file:
    correct_inputs.append(line)

class TestIntegration(TestCase):
    def test_integration(self):
        case_number = 0
        input_line = correct_inputs[case_number]
        expected_result_message = "The amount to pay RENE is: 215.00 USD"
        result_message = process_line(input_line,case_number)
        self.assertEqual(expected_result_message,result_message)

        case_number = 1
        input_line = correct_inputs[case_number]
        expected_result_message = "The amount to pay ASTRID is: 85.00 USD"
        result_message = process_line(input_line,case_number)
        self.assertEqual(expected_result_message,result_message)

        case_number = 2
        input_line = correct_inputs[case_number]
        expected_part_of_message = "Unable to process line"
        result_message = process_line(input_line,case_number)
        self.assertIn(expected_part_of_message,result_message)

        case_number = 3
        input_line = correct_inputs[case_number]
        expected_part_of_message = "Unable to process line"
        result_message = process_line(input_line,case_number)
        self.assertIn(expected_part_of_message,result_message)
