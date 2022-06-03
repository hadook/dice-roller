from typing import List
from diceroller import DiceRoller


"""This class validates the tokens and their order"""
class Validator(DiceRoller):
    
    # validates the token list on init
    def __init__(self, _tokens: list[str]) -> None:
        self.tokens = _tokens
        self.valid = self.__validate(_tokens)
        if self.valid:
            self.tokens = self.__convert_numbers(_tokens)

    # validates the tokens list against basic syntax rules
    def __validate(self, tokens: list[str]) -> bool:
        if not self.__tokens_allowed(tokens):
            return False
        if not self.__brackets_paired(tokens, '(', ')'):
            return False
        if not self.__brackets_paired(tokens, '[', ']'):
            return False
        return True

    # returns True if all tokens are allowed_tokens
    def __tokens_allowed(self, tokens: list[str]) -> bool:
        for token in tokens:
            if not self.is_token(token):
                return False
        return True
    
    # returns True if all left brackets have a matching right bracket
    @staticmethod
    def __brackets_paired(tokens: list[str], left: str, right: str) -> bool:
        count = 0
        for token in tokens:
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

    # returns a 3-element sublist of 'tokens' with the index element as the middle one
    @staticmethod
    def __get_neighbours(tokens: list[str], idx: int) -> list[str]:
        neighbours = []
        if idx == 0:
            neighbours.append(None)
        else:
            neighbours.append(tokens[idx - 1])
        neighbours.append(tokens[idx])
        if idx == len(tokens) - 1:
            neighbours.append(None)
        else:
            neighbours.append(tokens[idx + 1])
        return neighbours

    # returns a list with all numeric values (str) converted to int
    @staticmethod
    def __convert_numbers(tokens: list[str]) -> list[str]:
        for i, s in enumerate(tokens):
            if s.isdecimal():
                tokens.pop(i)
                tokens.insert(i, int(s))
        return tokens
