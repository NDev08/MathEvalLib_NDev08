class MathFunctions:
    @staticmethod
    def evaluate_exponent(number1, number2):
        return number1**number2

    @staticmethod
    def evaluate_multiplication(number1, number2):
        return number1 * number2

    @staticmethod
    def evaluate_division(number1, number2):
        if number2 == 0:
            raise ValueError("Cannot divide by zero")
        return number1 / number2

    @staticmethod
    def evaluate_addition(number1, number2):
        return number1 + number2

    @staticmethod
    def evaluate_subtraction(number1, number2):
        return number1 - number2
