from .MathTokenizer import Tokenizer
from .MathFunctions import MathFunctions
from .MathExceptions import ExpressionSyntaxError
from collections.abc import Callable


class MathEvalLib:
    def __init__(self):
        self.tokenizer = Tokenizer()
        self.MathFunctions = MathFunctions()

    def evaluate(self, equation: str):
        result = self.solver(equation)
        answer = result[0]
        if answer.startswith("n"):
            answer = answer[1:]
        return float(answer)

    def solver(self, equation: str | list[str]) -> list[str]:
        if isinstance(equation, str):
            tokenEquation: list[str] = self.tokenizer.tokenize(equation)
        else:
            tokenEquation: list[str] = equation

        tokenEquation = self.dealWithNeg(tokenEquation)
        self.checkErrors(tokenEquation)
        tokenEquation = self.dealWithPare("s(", "s)", tokenEquation)
        tokenEquation = self.findToken(
            "o^", tokenEquation, self.MathFunctions.evaluate_exponent
        )
        tokenEquation = self.findToken(
            ["o*", "o/"],
            tokenEquation,
            [
                self.MathFunctions.evaluate_multiplication,
                self.MathFunctions.evaluate_division,
            ],
        )
        tokenEquation = self.findToken(
            ["o+", "o-"],
            tokenEquation,
            [
                self.MathFunctions.evaluate_addition,
                self.MathFunctions.evaluate_subtraction,
            ],
        )
        return tokenEquation

    def findToken(
        self,
        token: str | list[str],
        equation: list[str],
        call: (
            Callable[[int, list[str]], list[str]]
            | list[Callable[[int, list[str]], list[str]]]
        ),
    ) -> list[str]:
        if isinstance(token, str) and isinstance(call, list):
            raise SyntaxError(
                f"{token} is {type(token)} and {call} is {type(call)} which will cause an illegal state!"
            )
        while True:
            for equation_index, tok in enumerate(equation):
                if isinstance(token, list):
                    for token_index, i in enumerate(token):
                        if tok == i:
                            if isinstance(call, list):
                                result = call[token_index](equation_index, equation)
                            else:
                                result = call(equation_index, equation)
                            equation = (
                                equation[: equation_index - 1]
                                + result
                                + equation[equation_index + 2 :]
                            )
                            break
                    else:
                        continue
                    break
                else:
                    if tok == token:
                        if isinstance(call, list):
                            result = call[0](equation_index, equation)
                            raise Warning(
                                f"parameter call should be a Callable not a list of Callables"
                            )
                        else:
                            result = call(equation_index, equation)
                        equation = (
                            equation[: equation_index - 1]
                            + result
                            + equation[equation_index + 2 :]
                        )
                        break
            else:
                break
        return equation

    def dealWithNeg(self, equation: list[str]):
        newEquation = equation
        for index, tok in enumerate(equation):
            if tok == "o-":
                if index == 0:
                    if equation[index + 1][0] == "n":
                        newEquation[index] = (
                            "DEL"  # place holder so index stays the same
                        )
                        newEquation[index + 1] = (
                            f"{equation[index + 1][0]}-{equation[index + 1][1:]}"
                        )
                elif index < len(equation) - 1:
                    if equation[index - 1][0] == "o":
                        if equation[index + 1][0] == "n":
                            newEquation[index] = (
                                "DEL"  # place holder so index stays the same
                            )
                            newEquation[index + 1] = (
                                f"{equation[index + 1][0]}-{equation[index + 1][1:]}"
                            )
                        else:
                            newEquation[index] = "NEG"
        newEquation = [x for x in newEquation if x != "DEL"]
        return newEquation

    def checkErrors(self, equation: list[str]):
        for index, tok in enumerate(equation):
            if tok[0] == "o":
                if index == 0:
                    raise ExpressionSyntaxError(
                        f"Equation can not start with operation '{tok[1:]}'"
                    )
                elif index == len(equation) - 1:
                    raise ExpressionSyntaxError(
                        f"Equation can not end with operation '{tok[1:]}'"
                    )
                elif equation[index - 1][0] == "o":
                    raise ExpressionSyntaxError(
                        f"Operation '{equation[index][1:]}' can not follow operation '{equation[index - 1][1:]}'"
                    )

        if equation.count("s(") != equation.count("s)"):
            raise ExpressionSyntaxError("Mismatched Parentheses")

    def dealWithPare(
        self, startSymbol: str, endSymbol: str, equation: list[str]
    ) -> list[str]:
        inParentheses: int = 0
        parenthesesEquation: list[str] = []
        index = 0
        enterIndex = None
        exitIndex = None
        while index < len(equation):
            if equation[index] == "s)":
                if inParentheses == 1:
                    exitIndex = index
                inParentheses -= 1
            if inParentheses > 0:
                parenthesesEquation.append(equation[index])
            elif enterIndex is not None and exitIndex is not None:
                if equation[enterIndex - 1] == "NEG":
                    preNegative = self.solver(parenthesesEquation)
                    number = preNegative[0][1:]

                    if number.startswith("-"):
                        number = number[1:]
                    else:
                        number = "-" + number

                    equation[enterIndex - 1 : exitIndex + 1] = [number]
                equation[enterIndex : exitIndex + 1] = self.solver(parenthesesEquation)
                index = enterIndex
                enterIndex = exitIndex = None

            if equation[index] == "s(":
                if inParentheses == 0:
                    enterIndex = index
                inParentheses += 1

            index += 1
        return equation

    @staticmethod
    def testMath(index: int, equation: list[str]) -> list[str]:
        return equation
