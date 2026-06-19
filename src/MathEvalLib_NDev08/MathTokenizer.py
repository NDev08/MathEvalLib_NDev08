from MathEvalLib_NDev08 import MathEvalLib

class Tokenizer:
    """Tokenizes mathematical equations into groups of tokens.
    
    Converts an equation string into lists of grouped characters,
    where each group represents a number, symbol, or operator.
    """

    # Token type identifiers
    tokens = ["n", "s", "o"]  # n = numbers, s = symbols, o = operators
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."] # all number symbols
    symbols = ["(", ")", "-"] # all math symbols
    operators = ["+", "*", "/", "^"] # all operator symbols

    def get_type(self, c: str) -> str:
        """checks the symbol and returns its corresponding token"""
        if c in self.numbers:
            return self.tokens[0]
        if c in self.symbols:
            return self.tokens[1]
        if c in self.operators:
            return self.tokens[2]
        return ""

    def tokenize(self, equation: str) -> list[str]:
        """Tokenizes an equation string into grouped tokens.
        
        Groups consecutive characters of the same type (numbers, symbols, or operators)
        into single tokens. For example, '123+45' becomes ['n123', 'o+', 'n45'].
        """
        equation = equation.replace(" ", "")
        print(equation)
        tokenized_equation: list[str] = []
        token = ""
        for c in equation:
            typ = self.get_type(c)
            if typ == "":
                raise ValueError(f"Invalid Character: {c}")

            if token == "":  # Start a new token with type prefix and character
                token = typ + c
            elif token[0] != typ:  # Type changed, append previous token and start new one
                tokenized_equation.append(token)
                token = "" + typ + c
            else:  # Same type, append to current token
                token += c

        tokenized_equation.append(token)
        return tokenized_equation


if __name__ == "__main__":
    toknize= Tokenizer()
    print(toknize.tokenize("-5 + 10 * -( 50 - 40 )"))
