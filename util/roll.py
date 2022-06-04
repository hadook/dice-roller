from random import randint


"""Thiss class represents a simple dice roll."""
class Roll:

    # rolls the dice and calculates total on init
    def __init__(self, dice: int, sides: int) -> None:
        self.exp = f'{dice}d{sides}'
        self.rolls = self.__get_rolls(dice, sides)
        self.total = self.__get_total(self.rolls)

    # returns the object represented as a string
    def __repr__(self) -> str:
        return f'{self.exp}\t: {self.total}\t: {self.rolls}'
    
    # returns the object represented as an integer
    def __int__(self):
        return self.total
    
    # alternative constructor
    @classmethod
    def from_list(cls, rolls: list[int]):
        roll = cls(0, 0)
        roll.exp = ''
        roll.rolls = rolls
        roll.total = cls.__get_total(rolls)
        return roll

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

