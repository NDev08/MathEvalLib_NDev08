from .MathFunctions import MathFunctions

class MathEvalLib:
    def __init__(self):
        self.math_functions = MathFunctions()

    def evaluate(self, equation):
        converted_equation = equation
        if isinstance(equation, str):
            equation = equation.replace(" ", "")
            converted_equation = self.convert_to_list(equation)
        while len(converted_equation) > 1:
            converted_equation = self.check_for_parenthesis(converted_equation)
            converted_equation = self.check_for_simble_and_exicute(converted_equation, "^", self.math_functions.evaluate_exponent)
            converted_equation = self.check_for_both_simble_and_exicute(converted_equation, "*", "/",
                                                                        self.math_functions.evaluate_multiplication, self.math_functions.evaluate_division)
            converted_equation = self.check_for_both_simble_and_exicute(converted_equation, "+", "-",
                                                                        self.math_functions.evaluate_addition, self.math_functions.evaluate_subtraction)
        return converted_equation[0]


    def check_for_both_simble_and_exicute(self, equation: list, symbol1: str, symbol2: str, function1, function2):
        while symbol1 in equation or symbol2 in equation:
            for i in range(len(equation)):
                if equation[i] == symbol1:
                    solve = function1(float(equation[i-1]), float(equation[i+1]))
                    equation[i-1:i+2] = [solve]
                    break
                elif equation[i] == symbol2:
                    solve = function2(float(equation[i-1]), float(equation[i+1]))
                    equation[i-1:i+2] = [solve]
                    break
        return equation

    def check_for_simble_and_exicute(self, equation: list, symbol: str, function):
        while symbol in equation:
            for i in range(len(equation)):
                if equation[i] == symbol:
                    solve = function(float(equation[i-1]), float(equation[i+1]))
                    equation[i-1:i+2] = [solve]
                    break
                
        return equation

    def check_for_parenthesis(self, equation: list):
        start = 0
        while equation.count("(") > 0:
            for i in range(len(equation)):
                if equation[i] == "(":
                    start = i
                elif equation[i] == ")":
                    end = i
                    inner_equation = equation[start+1:end]
                    result = self.evaluate(inner_equation)
                    equation[start:end+1] = [result]
                    break

        return equation

    def convert_to_list(self, equation: str):
        item_list:str = ""
        final_equasion = []
        for i in range(len(equation)):
            if equation[i] in "0123456789":
                item_list += equation[i]
                if i == len(equation) - 1:
                    final_equasion.append(item_list)
            else:                
                if item_list:
                    final_equasion.append("".join(item_list))
                item_list = ""
                final_equasion.append(equation[i])
        return final_equasion
