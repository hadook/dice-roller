from diceroller import DiceRoller


class Tokenizer(DiceRoller):
    """This class tokenizes the user input expression into a set of tokens."""

    def __init__(self, exp) -> None:
        self.exp = ' '.join(exp.removeprefix('/roll').split())
        self.tokens = self.get_tokens()
        print(self.exp)
        print(self.tokens)

    def get_tokens(self):
        self.tokens = self.exp.split()
        for item in self.tokens:
            substrings = self.get_substrings(item)

    @staticmethod
    def get_substrings(input_string):
        length = len(input_string)
        return [input_string[i:j] for i in range(length) for j in range(i+1, length)]



tk = Tokenizer('/roll  a      bc d   e ff g    hh   ')
print(tk.get_substrings("ASDFGHJKL"))
