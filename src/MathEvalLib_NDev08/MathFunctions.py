class MathFunctions:
    @staticmethod
    def evaluate_exponent(index: int, equation: list[str]) -> list[str]:
        number1 = float(equation[index - 1][1:])
        number2 = float(equation[index + 1][1:])
        return [f"n{number1 ** number2}"]

    @staticmethod
    def evaluate_multiplication(index: int, equation: list[str]) -> list[str]:
        number1 = float(equation[index - 1][1:])
        number2 = float(equation[index + 1][1:])
        return [f"n{number1 * number2}"]

    @staticmethod
    def evaluate_division(index: int, equation: list[str]) -> list[str]:
        number1 = float(equation[index - 1][1:])
        number2 = float(equation[index + 1][1:])
        if number2 == 0:
            raise ValueError("Cannot divide by zero")
        return [f"n{number1 / number2}"]

    @staticmethod
    def evaluate_addition(index: int, equation: list[str]) -> list[str]:
        number1 = float(equation[index - 1][1:])
        number2 = float(equation[index + 1][1:])
        return [f"n{number1 + number2}"]

    @staticmethod
    def evaluate_subtraction(index: int, equation: list[str]) -> list[str]:
        number1 = float(equation[index - 1][1:])
        number2 = float(equation[index + 1][1:])
        return [f"n{number1 - number2}"]
