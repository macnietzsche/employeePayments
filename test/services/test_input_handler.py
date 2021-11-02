from unittest import TestCase
from services.input_handler import InputHandler
from json import load as json_load

incorrect_inputs=[]
file = open("test/input_files/incorrect_input_test.txt", "r")
for line in file:
    incorrect_inputs.append(line)

correct_inputs=[]
file = open("test/input_files/correct_input_test.txt", "r")
for line in file:
    correct_inputs.append(line)

with open("test/input_files/worked_days_summaries_test.json") as file:
        worked_days_summaries = json_load(file)

class TestInputHandler(TestCase):
    def test_incorrect_input(self):
        input = incorrect_inputs[0]
        with self.assertRaises(Exception):
            InputHandler(input)

        input = incorrect_inputs[1]
        with self.assertRaises(Exception):
            InputHandler(input)
        
        input = incorrect_inputs[2]
        with self.assertRaises(Exception):
            InputHandler(input)
        
        input = incorrect_inputs[3]
        with self.assertRaises(Exception):
            InputHandler(input)

        input = incorrect_inputs[4]
        with self.assertRaises(Exception):
            InputHandler(input)

    def test_normalized_input(self):

        case_number = 0
        expected_normalized_input = worked_days_summaries[case_number]
        input_handler_instance = InputHandler(correct_inputs[case_number])
        normalized_input = input_handler_instance.normalized_input
        self.assertEqual(expected_normalized_input,normalized_input)

        case_number = 1
        expected_normalized_input = worked_days_summaries[case_number]
        input_handler_instance = InputHandler(correct_inputs[case_number])
        normalized_input = input_handler_instance.normalized_input
        self.assertEqual(expected_normalized_input,normalized_input)

