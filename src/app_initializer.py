from domain.employee import Employee
from services.input_handler import InputHandler

def process_line(line, count):
    try:
        input_handler_service = InputHandler(line)
        name = input_handler_service.normalized_input['label']
        worked_days_summary = input_handler_service.normalized_input['value']

        employee = Employee(name,worked_days_summary)
        return employee.payment_receipt()
    except Exception as e:
        return f"Unable to process line {count + 1}. Error message: {str(e)}"
