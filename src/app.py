from domain.employee import Employee
from services.input_handler import InputHandler

if __name__ == '__main__':
    file = open("employees_input.txt", "r")
    for count,line in enumerate(file):
        try:
            input_handler_service = InputHandler(line)
            name = input_handler_service.normalized_input['label']
            worked_days_summary = input_handler_service.normalized_input['value']

            employee = Employee(name,worked_days_summary)
            employee.print_payment_receipt()
        except Exception as e:
            print(f"Unable to process line {count + 1}. Error message: {str(e)}")

        