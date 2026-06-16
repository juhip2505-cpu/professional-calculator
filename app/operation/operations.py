class Add:
    @staticmethod
    def calculate(a, b):
        return a + b


class Subtract:
    @staticmethod
    def calculate(a, b):
        return a - b


class Multiply:
    @staticmethod
    def calculate(a, b):
        return a * b


class Divide:
    @staticmethod
    def calculate(a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b 