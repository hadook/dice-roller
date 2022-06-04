"""

    2*3d6*4
    4d6 cs=6 d 3 + 2
    4d6 cs=6 + 2

    (() (()))

"""


"""This class parses the tokens list and evaluates the symbols."""
class Parser:

    def __init__(self, tokens: list[str]) -> None:
        self.tokens = tokens.copy()

    def evaluate(self) -> int:
        # resolve: ()
        # resolve: *, /, d, kh, kl, cs
        # resolve: +, -

        pass

    # returns the position (start, end) of the first group '(...)' from tokens list
    @staticmethod
    def get_group(tokens: list[str]):
        for i in range(len(tokens)):
            if tokens[i] == '(':
                count = 1
                for j in range(i+1, len(tokens)):
                    if tokens[j] == '(':
                        count += 1
                    elif tokens[j] == ')':
                        count -= 1
                        if count == 0:
                            return (i, j)
                
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

