from util.diceroller import DiceRoller
from util.tokenizer import Tokenizer
from util.validator import Validator
from util.roll import Roll
from util.calc import Calculator as calc


"""This class parses the tokens list and evaluates the symbols."""
class Parser:

    operators_1 = ['*', '/', 'd', 'kh', 'kl', 'cs']
    operators_2 = ['+', '-']

    def __init__(self, exp: str) -> None:
        t = Tokenizer(exp)
        v = Validator(t.tokens)
        self.result = None
        if v.valid:
            self.result = self.evaluate(v.tokens)

    # returns the object represented as a string
    def __repr__(self) -> str:
        return f'Result\t: {self.result}'

    # evaluates the tokenized expression to a number
    def evaluate(self, _tokens: list[str]):
        tokens = _tokens.copy()

        # resolve groups: ()
        while self.__get_group(tokens) is not None:
            i, j = self.__get_group(tokens)
            group = tokens[i+1:j]
            tokens[i:j+1] = [self.evaluate(group)]
        
        # resolve operators_1: *, /, d, kh, kl, cs
        while self.__get_operator(tokens, self.operators_1) is not None:
            i = self.__get_operator(tokens, self.operators_1)
            operator = tokens[i]
            left, right = self.__get_neighbours(tokens, i)
            tokens[i-1:i+2] = [self.__calculate(left, operator, right)]

        # resolve operators_2: +, -
        while self.__get_operator(tokens, self.operators_2) is not None:
            i = self.__get_operator(tokens, self.operators_2)
            operator = tokens[i]
            left, right = self.__get_neighbours(tokens, i)
            tokens[i-1:i+2] = [self.__calculate(left, operator, right)]
        
        # return result
        if len(tokens) == 1:
            x = tokens[0]
            if isinstance(x, Roll) or isinstance(x, int):
                return x
        return None

    # calculates a simple operation with 2 arguments
    def __calculate(self, left, operator: str, right):
        if operator in self.operators_1 or operator in self.operators_2:
            if operator == '+':
                if (isinstance(left, int) or isinstance(left, Roll)) and (isinstance(right, int) or isinstance(right, Roll)):
                    return calc.add(left, right)
            elif operator == '-':
                if (isinstance(left, int) or isinstance(left, Roll)) and (isinstance(right, int) or isinstance(right, Roll)):
                    return calc.substract(left, right)
            elif operator == '*':
                if (isinstance(left, int) or isinstance(left, Roll)) and (isinstance(right, int) or isinstance(right, Roll)):
                    return calc.multiply(left, right)
            elif operator == '/':
                if (isinstance(left, int) or isinstance(left, Roll)) and (isinstance(right, int) or isinstance(right, Roll)):
                    return calc.divide(left, right)
            elif operator == 'd':
                if (isinstance(left, int) or isinstance(left, Roll)) and (isinstance(right, int) or isinstance(right, Roll)):
                    roll = calc.roll_dice(left, right)
                    print(roll)
                    return roll
            elif operator == 'kh':
                if isinstance(left, Roll) and (isinstance(right, int) or isinstance(right, int)):
                    return calc.keep_high(left, right)
            elif operator == 'kl':
                if isinstance(left, Roll) and (isinstance(right, int) or isinstance(right, int)):
                    return calc.keep_low(left, right)
            elif operator == 'cs':
                if isinstance(left, Roll) and isinstance(right, str):
                    return calc.count_success(left, right)
        return None

    # returns the position (start, end) of the first group '(...)' from tokens list
    @staticmethod
    def __get_group(tokens: list[str]):
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

    # returns the position of the first list element that is an operator from a specified operators list
    @staticmethod
    def __get_operator(tokens: list[str], operators: list[str]):
        for i, x in enumerate(tokens):
            if x in operators:
                return i
        return None
                
    # returns a tuple of 2 list elements: to the left and right of the element given by index
    @staticmethod
    def __get_neighbours(tokens: list[str], idx: int):
        if idx == 0:
            left = None
        else:
            left = tokens[idx-1]
        if idx == len(tokens) - 1:
            right = None
        else:
            right = tokens[idx+1]
        return (left, right)

