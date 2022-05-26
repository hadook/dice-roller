from diceroller import DiceRoller


"""This class tokenizes the user input expression into a set of tokens."""
class Tokenizer(DiceRoller):
    
    # tokenizes the expression on init
    def __init__(self, exp) -> None:
        self.exp = ' '.join(exp.casefold().removeprefix('/roll').split())
        self.tokens = self.get_tokens(self.exp)

    # returns a list of substrings of string s, sorted by length (longest first)
    @staticmethod
    def get_substrings(s):
        return [s[i:i+n] for n in range(len(s)-1, 0, -1) for i in range(0, len(s)-n+1)]

    # returns True if s is a valid token
    @classmethod
    def is_token(cls, s):
        return s.isdecimal() or (s in cls.operators) or (s in cls.organizers)

    # returns True if s has a valid token substring
    @classmethod
    def has_token(cls, s):
        if cls.is_token(s):
            return False
        for substring in cls.get_substrings(s):
            if cls.is_token(substring):
                return True
        return False
    
    # splits a string into tokens and returns a list
    @classmethod
    def split(cls, s):
        if cls.is_token(s):
            return [s]
        for substring in cls.get_substrings(s):
            if cls.is_token(substring):
                start = s.find(substring)
                end = start + len(substring)
                tokens = [s[:start], s[start:end], s[end:]]
                if '' in tokens:
                    tokens.remove('')
                return tokens
        return [s]

    # returns True if all list items are tokenized
    @classmethod
    def are_tokenized(cls, items):
        for s in items:
            if cls.has_token(s):
                return False
        return True

    # tokenizes the expression
    @classmethod
    def get_tokens(cls, exp):
        items = exp.split()
        while not cls.are_tokenized(items):
            for i, s in enumerate(items):
                tokens = cls.split(s)
                items.pop(i)
                while len(tokens) > 0:
                    items.insert(i, tokens.pop())
        return items
