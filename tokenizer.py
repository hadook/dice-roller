
class Tokenizer:
    """This class tokenizes the user input expression into a set of tokens."""

    def __init__(self, exp) -> None:
        self.exp = ' '.join(exp.removeprefix('/roll').split())
        self.tokens = self.exp.split()
        print(self.exp)
        print(self.tokens)



tk = Tokenizer('/roll  a      bc d   e ff g    hh   ')
