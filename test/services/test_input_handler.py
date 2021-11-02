from unittest import TestCase
from services.input_handler import InputHandler

incorrect_inputs=[]
file = open("test/input_files/incorrect_input_test.txt", "r")
for line in file:
    incorrect_inputs.append(line)

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

