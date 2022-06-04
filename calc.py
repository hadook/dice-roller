from roll import Roll


class Calculator:
    """This class is responsible for performing integer calculations."""

    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b

    @staticmethod
    def substract(a: int, b: int) -> int:
        return a - b

    @staticmethod
    def multiply(a: int, b: int) -> int:
        return a * b

    @staticmethod
    def divide(a: int, b: int) -> int:
        return a // b

    @staticmethod
    def roll_dice(n: int, d: int) -> Roll:
        return Roll(n, d)
    
    @staticmethod
    def keep_high(r: Roll, n: int) -> int:
        result = 0
        rolls = sorted(r.rolls, reverse=True)
        for i in range(min(len(rolls), n)):
            result += rolls[i]
        return result

    @staticmethod
    def keep_low(r: Roll, n: int) -> int:
        result = 0
        rolls = sorted(r.rolls, reverse=False)
        for i in range(min(len(rolls), n)):
            result += rolls[i]
        return result

    @staticmethod
    def count_success(r: Roll, operator: str, target: int) -> int:
        result = 0
        if operator == '=':
            result = r.rolls.count(target)
        elif operator == '>':
            for x in r.rolls:
                if x > target:
                    result += 1
        elif operator == '>=':
            for x in r.rolls:
                if x >= target:
                    result += 1
        elif operator == '<':
            for x in r.rolls:
                if x < target:
                    result += 1
        elif operator == '<=':
            for x in r.rolls:
                if x <= target:
                    result += 1
        return result
