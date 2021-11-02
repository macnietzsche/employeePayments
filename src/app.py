from json import load as json_load
from subdomains.payment_handler import PaymentHandler
from services.input_handler import InputHandler

if __name__ == '__main__':
    with open("test/input_files/payment_settings_test.json") as file:
        payment_settings_data = json_load(file)

    with open("test/input_files/worked_days_summaries_test.json") as file:
        worked_days_summaries = json_load(file)

    incorrect_inputs=[]
    file = open("test/input_files/incorrect_input_test.txt", "r")
    for line in file:
        incorrect_inputs.append(line)

    correct_inputs=[]
    file = open("test/input_files/correct_input_test.txt", "r")
    for line in file:
        correct_inputs.append(line)

    input = correct_inputs[0]
    example = InputHandler(input)
    test = example.normalized_input

    print("hello")