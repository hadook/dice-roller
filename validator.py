from typing import List
from diceroller import DiceRoller


"""This class validates the tokens and their order"""
class Validator(DiceRoller):
    
    # TODO - remove typehints, add comment
    def __init__(self, tokens: list[str]) -> None:
        self.tokens = tokens

    # returns a 3-element sublist of 'tokens' with the index element as the middle one
    def get_neighbours(self, idx: int) -> list[str]:
        neighbours = []
        if idx == 0:
            neighbours.append(None)
        else:
            neighbours.append(self.tokens[idx - 1])
        neighbours.append(self.tokens[idx])
        if idx == len(self.tokens) - 1:
            neighbours.append(None)
        else:
            neighbours.append(self.tokens[idx + 1])
        return neighbours


x = ['a', 'b', 'c', 'd']
v = Validator(x)
for i in range(len(x)):
    print(i, v.get_neighbours(i))