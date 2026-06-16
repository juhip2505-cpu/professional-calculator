from app.operation.operations import Add, Subtract, Multiply, Divide


class Calculation:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def perform(self):
        return self.operation.calculate(self.a, self.b)


class CalculationFactory:
    @staticmethod
    def create_calculation(operation_name, a, b):
        operations = {
            "add": Add,
            "subtract": Subtract,
            "multiply": Multiply,
            "divide": Divide
        }

        if operation_name not in operations:
            raise ValueError("Invalid operation")

        return Calculation(a, b, operations[operation_name]) 