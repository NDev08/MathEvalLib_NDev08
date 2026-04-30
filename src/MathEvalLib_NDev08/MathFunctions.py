class MathFunctions:

    def __init__(self):
        pass


    def evaluate_exponent(self, number1, number2):
        return number1 ** number2

    def evaluate_multiplication(self, number1, number2):
        return number1 * number2

    def evaluate_division(self, number1, number2):
        if number2 == 0:
            raise ValueError("Cannot divide by zero")
        return number1 / number2

    def evaluate_addition(self, number1, number2):
        return number1 + number2

    def evaluate_subtraction(self, number1, number2):
        return number1 - number2