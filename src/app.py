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

    input = incorrect_inputs[3]
    example = InputHandler(input)

    summary = worked_days_summaries['summary_case1'];
    payment_service =PaymentHandler(payment_settings_data)

    ammount = payment_service.calculate_payment_amount(summary)    
    print("hello world")