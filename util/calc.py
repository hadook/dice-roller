from util.roll import Roll


"""This class is responsible for performing integer calculations."""
class Calculator:
    
    @staticmethod
    def add(a: int, b: int) -> int:
        return int(a) + int(b)

    @staticmethod
    def substract(a: int, b: int) -> int:
        return int(a) - int(b)

    @staticmethod
    def multiply(a: int, b: int) -> int:
        return int(a) * int(b)

    @staticmethod
    def divide(a: int, b: int) -> int:
        return int(a) // int(b)

    @staticmethod
    def roll_dice(n: int, d: int) -> Roll:
        return Roll(int(n), int(d))
    
    @staticmethod
    def keep_high(r: Roll, n: int) -> int:
        result = 0
        rolls = sorted(r.rolls, reverse=True)
        for i in range(min(len(rolls), int(n))):
            result += rolls[i]
        return result

    @staticmethod
    def keep_low(r: Roll, n: int) -> int:
        result = 0
        rolls = sorted(r.rolls, reverse=False)
        for i in range(min(len(rolls), int(n))):
            result += rolls[i]
        return result

    @staticmethod
    def count_success(r: Roll, cs: str) -> int:
        for i, c in enumerate(cs):
            if c.isdecimal():
                operator = cs[:i]
                target = int(cs[i:])
                break
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

