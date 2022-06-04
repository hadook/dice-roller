from util.diceroller import DiceRoller


"""This class validates the tokens and their order."""
class Validator(DiceRoller):
    
    # validates the token list and converts strings to numbers
    def __init__(self, tokens: list[str]) -> None:
        self.tokens = tokens.copy()
        self.valid = self.__validate()

    # validates the tokens list against basic syntax rules
    def __validate(self) -> bool:
        if not self.__tokens_allowed():
            return False
        if not self.__brackets_paired('(', ')'):
            return False
        if not self.__brackets_paired('[', ']'):
            return False
        if not self.__merge_cs():
            return False
        self.__convert_numbers()
        return True

    # returns True if all tokens are allowed_tokens
    def __tokens_allowed(self) -> bool:
        for token in self.tokens:
            if not self.is_token(token):
                return False
        return True
    
    # returns True if all left brackets have a matching right bracket
    def __brackets_paired(self, left: str, right: str) -> bool:
        count = 0
        for token in self.tokens:
            if count < 0:
                return False
            if token == left:
                count += 1
            elif token == right:
                count -= 1
        if count != 0:
            return False
        else:
            return True

    # merges the count success operators and their quantifiers, returns True if successful
    def __merge_cs(self) -> bool:
        for i, token in enumerate(self.tokens):
            if token in ['=', '<', '>', '<=', '>=']:
                if self.tokens[i+1].isdecimal():
                    new = token + self.tokens[i+1]
                    del self.tokens[i:i+2]
                    self.tokens.insert(i, new)
                else:
                    return False
        return True

    # returns a list with all numeric values (str) converted to int
    def __convert_numbers(self) -> None:
        for i, s in enumerate(self.tokens):
            if s.isdecimal():
                self.tokens.pop(i)
                self.tokens.insert(i, int(s))

