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
