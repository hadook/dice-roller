from random import randint

class Calculator:
    """This class is responsible for performing integer calculations."""

    def __init__() -> None:
        pass

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def substract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a // b

    @staticmethod
    def roll(a, b):
        rolls = []
        for i in range(a):
            rolls.append(randint(1, b))
        return rolls


class Roll:
    """Thiss class represents a simple dice roll."""

    # rolls the dice and calculates total on init
    def __init__(self, dice: int, sides: int) -> None:
        self.exp = f'{dice}d{sides}'
        self.rolls = self.__get_rolls(dice, sides)
        self.total = self.__get_total(self.rolls)

    # returns the object represented as a string
    def __repr__(self) -> str:
        return f'{self.exp} : {self.rolls}'

    # returns a list of dice results from a single roll
    @staticmethod
    def __get_rolls(dice: int, sides: int) -> list[int]:
        rolls = []
        for i in range(dice):
            rolls.append(randint(1, sides))
        return rolls
    
    # returns the total sum of a set of dice rolls
    @staticmethod
    def __get_total(rolls: list[int]) -> int:
        total = 0
        for roll in rolls:
            total += roll
        return total