


class Tokenizer():
    
    def __init__(self):
        self.tokens = ["n","s","o"]
        self.numbers = ["1","2","3","4","5","6","7","8","9","0","."]
        self.symbols = ["(",")","-"]
        self.operators = ["+","*","/","^"]

    def get_type(self, c: str) -> str:
        if c in self.numbers: return self.tokens[0]
        if c in self.symbols: return self.tokens[1]
        if c in self.operators: return self.tokens[2]
        return ""


    def tokenize(self,equation:str):
        tokenized_equation = []
        token = ""
        for c in equation:
            typ = self.get_type(c)
            if typ == "":
                raise ValueError(f"Invalid Character: {c}")

            if token == "":
                token = typ + c
            elif token[0] != typ:
                tokenized_equation.append(token)
                token = "" + typ + c
            else:
                token += c
                
            

        tokenized_equation.append(token)
        return tokenized_equation


if __name__ == "__main__":
    print(Tokenizer().tokenize("25+10-5(50+65^2)"))
    